# Client Portal — Firebase + Google Drive Setup

**Site pages:** `/client-portal.html` (login/OTP) + `/client-portal-dashboard.html` (dashboard)

**Current state:** both pages run in **DEMO mode** by default — localStorage-backed, universal OTP `123456`, mock file storage. The UI is complete; the backend needs 60–90 minutes of your setup time to go live.

**Target:** real phone-OTP login + real Google Drive file storage + auto-created folder structure per client.

---

## Architecture

```
Browser (GitHub Pages)
   │
   ├─ Firebase Auth  (phone OTP)                ← free
   ├─ Firebase Firestore (user table)           ← free tier
   └─ Firebase Cloud Function
           │
           └─ Google Drive API
                   │
                   └─ BQP's master Drive folder
                       (/BQP Clients/{Phone}/...)
```

**Why this split:**
- Firebase Auth is the cheapest and simplest OTP provider for phone-based login.
- Google Drive API cannot be called from the browser with full write permission to BQP's Drive — the service-account key must stay on the server side. A Firebase Cloud Function wraps the Drive API with per-user access control.
- Firestore stores the mapping: `phone → Drive folder ID` so the Function knows which folder each client can touch.

**Cost estimate:** free for first ~100 clients. At scale: Firebase Auth $0.01 per phone SMS; Cloud Functions ~$0 under 2M invocations/month; Drive storage ~$2/month per 100 GB on BQP's Google Workspace.

---

## Step 1 — Create Firebase project (10 min)

1. Go to https://console.firebase.google.com and sign in with `durgesh@bharatquantumprospera.com` (or a dedicated `portal@bqpartners.in`).
2. Click **Add project** → name: `bqp-client-portal`.
3. Disable Google Analytics (not needed for the portal).
4. In the project, click **Authentication → Get started → Sign-in method**.
5. Enable **Phone**. Add your own number to the test list first (first 10 SMS/day free).
6. In Project Settings (gear icon) → **General**, scroll to **Your apps** → click **Web icon (`</>`)**.
7. Register app: nickname `BQP Client Portal`. Firebase gives you a config snippet like:

   ```js
   const firebaseConfig = {
     apiKey: "AIza...",
     authDomain: "bqp-client-portal.firebaseapp.com",
     projectId: "bqp-client-portal",
     storageBucket: "bqp-client-portal.appspot.com",
     messagingSenderId: "1234567890",
     appId: "1:1234567890:web:abc..."
   };
   ```

   **Copy this.** You'll paste it into the portal page in Step 5.

8. In **Authentication → Settings → Authorized domains**, add `bharatquantumprospera.com`.

---

## Step 2 — Enable Firestore (5 min)

1. Firebase console → **Build → Firestore Database → Create database**.
2. Pick **asia-south1 (Mumbai)** region.
3. Start in **production mode**.
4. In the **Rules** tab, paste:

   ```
   rules_version = '2';
   service cloud.firestore {
     match /databases/{database}/documents {
       match /users/{phone} {
         allow read, update: if request.auth != null && request.auth.token.phone_number == phone;
         allow create: if request.auth != null;
       }
       match /files/{fileId} {
         allow read: if request.auth != null && resource.data.phone == request.auth.token.phone_number;
       }
     }
   }
   ```

5. Publish rules.

---

## Step 3 — Enable Google Drive API + service account (15 min)

1. Go to https://console.cloud.google.com — same Google account.
2. Pick the Firebase project (it also appears as a Google Cloud project).
3. **APIs & Services → Enable APIs** → search **Google Drive API** → Enable.
4. **IAM & Admin → Service Accounts → Create service account**:
   - Name: `bqp-portal-drive`
   - Grant role: **none at project level** (we'll grant Drive folder access directly).
5. On the created account, click **Keys → Add key → Create new key → JSON**. Download the file; store securely. Service-account email looks like `bqp-portal-drive@bqp-client-portal.iam.gserviceaccount.com`.
6. Open https://drive.google.com (on `durgesh@bharatquantumprospera.com`). Create a folder named **`BQP Clients`**.
7. Right-click the folder → **Share** → paste the service-account email → give **Editor** permission → **Send**. (This grants the Function the right to write files inside this folder on your behalf.)
8. Note the folder ID from the URL: `drive.google.com/drive/folders/<THIS_IS_THE_ID>` — you'll use it in Step 4.

---

## Step 4 — Deploy the Cloud Function (20 min)

The Function does three things:
- Creates a client's folder tree on first login.
- Returns an upload URL for a specific folder.
- Lists files in a folder.

1. Install Firebase CLI on your machine: `npm install -g firebase-tools` → `firebase login`.
2. In a new local folder, run `firebase init functions`. Pick the project, language JavaScript, install dependencies.
3. In `functions/package.json`, add dependencies:

   ```json
   "googleapis": "^131.0.0",
   "firebase-admin": "^12.0.0",
   "firebase-functions": "^5.0.0"
   ```

4. Replace `functions/index.js` with:

   ```javascript
   const functions = require('firebase-functions');
   const admin = require('firebase-admin');
   const { google } = require('googleapis');
   admin.initializeApp();

   const MASTER_FOLDER_ID = 'PASTE_YOUR_FOLDER_ID_FROM_STEP_3';
   const CATEGORIES = [
     ['Income Tax', true], ['GST', true], ['ROC Filings', true],
     ['Agreements', false], ['Invoices', true], ['Bank Statements', true],
     ['TDS Form 16A', true], ['FEMA ODI', false],
     ['US Compliance', true], ['Miscellaneous', false]
   ];
   const MONTHS = ['Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec','Jan','Feb','Mar'];

   function getDrive() {
     const auth = new google.auth.GoogleAuth({
       keyFile: '/path/to/service-account.json',  // set as env var in production
       scopes: ['https://www.googleapis.com/auth/drive']
     });
     return google.drive({ version: 'v3', auth });
   }

   async function createFolder(drive, name, parent) {
     const res = await drive.files.create({
       requestBody: { name, mimeType: 'application/vnd.google-apps.folder', parents: [parent] },
       fields: 'id'
     });
     return res.data.id;
   }

   function currentFY() {
     const d = new Date();
     const y = d.getMonth() >= 3 ? d.getFullYear() : d.getFullYear() - 1;
     return `FY ${y}-${String(y+1).slice(-2)}`;
   }

   exports.initializeClient = functions.https.onCall(async (data, context) => {
     if (!context.auth) throw new functions.https.HttpsError('unauthenticated','Sign in required');
     const phone = context.auth.token.phone_number;
     const name = data.name || phone;

     const existing = await admin.firestore().collection('users').doc(phone).get();
     if (existing.exists && existing.data().rootFolderId) {
       return { rootFolderId: existing.data().rootFolderId };
     }

     const drive = getDrive();
     const rootId = await createFolder(drive, `${name} (${phone})`, MASTER_FOLDER_ID);
     const fy = currentFY();
     const subs = {};

     for (const [cat, hasYM] of CATEGORIES) {
       const catId = await createFolder(drive, cat, rootId);
       subs[cat] = { id: catId };
       if (hasYM) {
         const fyId = await createFolder(drive, fy, catId);
         subs[cat][fy] = { id: fyId, months: {} };
         for (const m of MONTHS) {
           const mId = await createFolder(drive, `${m} ${fy.slice(3,7)}`, fyId);
           subs[cat][fy].months[m] = mId;
         }
       }
     }

     await admin.firestore().collection('users').doc(phone).set({
       phone, name, email: data.email || '',
       rootFolderId: rootId, folders: subs,
       createdAt: admin.firestore.FieldValue.serverTimestamp()
     });

     return { rootFolderId: rootId };
   });

   exports.uploadFile = functions.https.onCall(async (data, context) => {
     if (!context.auth) throw new functions.https.HttpsError('unauthenticated','Sign in required');
     const phone = context.auth.token.phone_number;
     const { folderPath, fileName, fileContent, mimeType } = data;

     const userDoc = await admin.firestore().collection('users').doc(phone).get();
     if (!userDoc.exists) throw new functions.https.HttpsError('not-found','User not initialized');
     const user = userDoc.data();

     const [cat, year, month] = folderPath.split('/');
     const folderId = user.folders[cat]?.[year]?.months?.[month] || user.folders[cat]?.id;
     if (!folderId) throw new functions.https.HttpsError('not-found','Folder not found');

     const drive = getDrive();
     const buf = Buffer.from(fileContent, 'base64');
     const res = await drive.files.create({
       requestBody: { name: fileName, parents: [folderId] },
       media: { mimeType, body: require('stream').Readable.from(buf) },
       fields: 'id,name,webViewLink'
     });

     await admin.firestore().collection('files').add({
       phone, folderPath, fileId: res.data.id, name: res.data.name,
       link: res.data.webViewLink,
       uploadedAt: admin.firestore.FieldValue.serverTimestamp()
     });

     return res.data;
   });

   exports.listFiles = functions.https.onCall(async (data, context) => {
     if (!context.auth) throw new functions.https.HttpsError('unauthenticated','Sign in required');
     const phone = context.auth.token.phone_number;
     const snap = await admin.firestore().collection('files')
       .where('phone','==',phone)
       .where('folderPath','==',data.folderPath)
       .orderBy('uploadedAt','desc')
       .get();
     return snap.docs.map(d => ({ id: d.id, ...d.data() }));
   });
   ```

5. Store the service-account JSON as an env var: `firebase functions:config:set drive.key="$(cat /path/to/service-account.json | base64)"`, then adjust `getDrive()` to read `functions.config().drive.key` instead of `keyFile`.
6. Deploy: `firebase deploy --only functions`. The deployment URL looks like `https://asia-south1-bqp-client-portal.cloudfunctions.net/...`.

---

## Step 5 — Wire the website to live mode (10 min)

1. Open `client-portal.html`:
   - Flip `var DEMO = true;` → `var DEMO = false;`
   - Paste your Firebase config into the `FIREBASE_CONFIG` object (from Step 1).
   - Add these script tags inside `<head>` (above `<link rel="stylesheet" href="bqp.css"/>`):

     ```html
     <script defer src="https://www.gstatic.com/firebasejs/10.14.0/firebase-app-compat.js"></script>
     <script defer src="https://www.gstatic.com/firebasejs/10.14.0/firebase-auth-compat.js"></script>
     <script defer src="https://www.gstatic.com/firebasejs/10.14.0/firebase-firestore-compat.js"></script>
     <script defer src="https://www.gstatic.com/firebasejs/10.14.0/firebase-functions-compat.js"></script>
     ```

   - Add an invisible reCAPTCHA container inside `<body>` (anywhere, visibility hidden):

     ```html
     <div id="recaptcha-container"></div>
     ```

   - Uncomment the LIVE MODE blocks in `sendOtp()` and `verifyOtp()` (comments mark where). Call `firebase.initializeApp(FIREBASE_CONFIG)` at the top of the script.

2. Open `client-portal-dashboard.html`:
   - Flip `var DEMO = true;` → `var DEMO = false;`.
   - Replace `getFiles()` / `saveFiles()` / `handleFileUpload()` localStorage calls with Function calls:
     - `firebase.functions().httpsCallable('listFiles')({folderPath: ...})` for listing.
     - `firebase.functions().httpsCallable('uploadFile')({...})` for upload (base64-encode the file content).
   - On first sign-in, call `firebase.functions().httpsCallable('initializeClient')({name, email})` to create the folder tree.

3. Commit, push, deploy. First real sign-in triggers the folder tree creation in your Drive.

---

## Step 6 — Test checklist

- [ ] Open `/client-portal.html` in incognito. Create account with your own phone + email + name.
- [ ] Receive real SMS OTP → enter → confirm sign-in redirects to dashboard.
- [ ] Dashboard loads with your name + phone shown.
- [ ] Open BQP Clients folder in Drive → confirm `{Your Name} ({Your Phone})` folder was auto-created with the full tree (Income Tax, GST, ROC, Agreements, Invoices, Bank Statements, TDS, FEMA, US Compliance, Miscellaneous — year + month sub-folders where applicable).
- [ ] Navigate into Income Tax → FY 2025–26 → Oct 2025. Upload a test PDF.
- [ ] Open Drive → confirm the file is in that specific month folder.
- [ ] Sign out → sign in again → confirm the file list persists.
- [ ] Send to a trial client → confirm they can sign in with their own phone + see only their own folder.

---

## Security notes

- Service-account JSON must NEVER be committed to GitHub. Store it only as an env var on the Function side.
- Firestore rules (Step 2) restrict each user to their own documents by phone number — do not relax these.
- Firebase Auth phone verification is the only sign-in method; disable email/password to prevent credential-based attacks.
- Add Firebase App Check (free) to prevent abuse of the public Function endpoint.
- Each file upload / download is logged to the `files` Firestore collection — this is your audit trail.

---

## Where this breaks (and what to use instead)

- **>500 active clients** or **>100 GB file volume**: Firebase Function cold starts and Drive API quotas start to pinch. Migrate to a dedicated CA client portal SaaS (see `/playbook/10-client-portal-saas-alternatives.md`).
- **Need e-signature or workflow approvals**: not covered here. SaaS alternatives bake this in.
- **Need Indian data residency (RBI / ISO 27001)**: Google Drive stores data outside India by default. For regulated clients, use a locally-compliant alternative.

For most cases (small-to-medium CA practice, 10–200 active clients), this Firebase + Drive stack is the right balance of cost, control, and simplicity.
