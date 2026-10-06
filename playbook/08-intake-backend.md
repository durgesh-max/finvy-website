# US Incorporation Intake — Backend Setup

**Page it serves:** `/us-incorporation-intake.html`

**Current default (works today, zero signup):** on submit, the form POSTs via **FormSubmit.co** AJAX directly to `durgesh@bharatquantumprospera.com`. The user never has to click Send in an email client — the submission is relayed to your inbox automatically.

**One-time activation step (~2 minutes):** FormSubmit requires the receiving email to confirm itself. The flow:

1. The FIRST submission to the live form triggers FormSubmit to send a one-time activation email to `durgesh@bharatquantumprospera.com` (subject: "Please confirm your email").
2. Open that email. Click the activation link ("Activate Form" button).
3. From that point on, every submission arrives directly as a formatted email with the full intake data in a table.

**Test it:** submit a dummy intake from an incognito window with your own email. Check your inbox for the FormSubmit confirmation email. Click to activate. Submit a second dummy intake. The real formatted intake email should arrive within 10-30 seconds.

**If you want a dashboard / Google Sheet in addition**, two optional upgrade paths follow. These layer on top of FormSubmit (not instead of).

---

## Default (already wired) — FormSubmit.co

The form POSTs intakes to `https://formsubmit.co/ajax/durgesh@bharatquantumprospera.com`. FormSubmit is a zero-signup form backend — no account, no API key, no monthly caps on the free tier (fair-use based). Every intake arrives as a formatted email in your inbox with a table of all fields.

**Pros:** zero setup, works out of the box, free, no account to manage.
**Cons:** no searchable dashboard; if you want structured history, add Option A or B below.

---

## OPTION A — Formspree (recommended for simplicity, 10 minutes)

**What you get:** every intake arrives in your email + a Formspree dashboard with searchable history + CSV export.

**Cost:** free tier 50 submissions/month. Paid starts at USD 10/mo for 500 submissions/mo. For BQP volume right now, free tier is fine.

**Steps:**

1. Go to https://formspree.io and sign up with `durgesh@bharatquantumprospera.com`.
2. Verify your email (click the link Formspree sends).
3. Click **"+ New Form"**. Fill:
   - Form name: **BQP US Incorporation Intake**
   - Notification email: **durgesh@bharatquantumprospera.com** (and optionally a second — `info@drspv.in` or team)
   - Submit action: **Receive submissions**
4. On the form settings page, find the endpoint URL. Looks like:
   ```
   https://formspree.io/f/xayzabcd
   ```
5. Open `us-incorporation-intake.html` in your editor. Find the line (near the top of the `<script>` block, ~line 480):
   ```js
   var FORMSPREE_ENDPOINT = "";
   ```
   Change to:
   ```js
   var FORMSPREE_ENDPOINT = "https://formspree.io/f/xayzabcd";
   ```
   (Paste YOUR endpoint, not the placeholder.)
6. Commit, push. The form will now POST intakes to Formspree. You'll receive emails plus they're in your Formspree dashboard.

**Test:** submit a dummy intake from an incognito window with your own email. Confirm you receive it.

---

## OPTION B — Google Apps Script → Google Sheet (recommended if you want data in a spreadsheet)

**What you get:** every intake lands as a new row in a Google Sheet you own. Perfect for tracking the funnel in a spreadsheet, filtering by stage/country/industry, exporting to CRM, running analytics.

**Cost:** free. No third-party platform in the loop.

**Steps:**

### 1. Create the Google Sheet

- Go to https://sheets.google.com → create a new sheet
- Name it: `BQP US Incorporation Intake`
- In row 1, add these column headers (paste the whole row at once, tab-separated):

```
Timestamp	Entity Type	Full Name	DOB	Email	WhatsApp	Country	Nationality	Address	Has SSN/ITIN	US Status	Business Name 1	Business Name 2	Business Name 3	Business Description	Industry	Stage	Existing India Entity	Customer Geo	US Employees	US Physical	Payment Platforms	Y1 Revenue	Num Owners	Corporate Owner	Ownership Split	Co-owner 1	Co-owner 2	Co-owner 3	Co-owner 4	Investors	Investor Details	Services	Ongoing Compliance	Timeline	Other Provider	Other Provider Detail	Notes	Source	Source URL
```

- Save the sheet. Copy its ID from the URL: `https://docs.google.com/spreadsheets/d/[THIS_IS_THE_ID]/edit`

### 2. Add the Apps Script

- In the sheet, click **Extensions → Apps Script**
- Delete whatever boilerplate code is there
- Paste the script below in full
- Replace `YOUR_SHEET_ID_HERE` on line 2 with the ID you copied

```javascript
// BQP US Incorporation Intake — endpoint for us-incorporation-intake.html
const SHEET_ID = 'YOUR_SHEET_ID_HERE';
const SHEET_TAB = 'Sheet1';          // or whatever you named the tab
const NOTIFY_EMAIL = 'durgesh@bharatquantumprospera.com';

function doPost(e) {
  try {
    const data = JSON.parse(e.postData.contents);
    const ss = SpreadsheetApp.openById(SHEET_ID);
    const sheet = ss.getSheetByName(SHEET_TAB) || ss.getSheets()[0];

    const coOwners = [1, 2, 3, 4].map(i => {
      const name = data['co_name_' + i];
      if (!name) return '';
      return [
        name,
        data['co_email_' + i] || '',
        data['co_country_' + i] || '',
        data['co_pct_' + i] || ''
      ].filter(Boolean).join(' | ');
    });

    const row = [
      data._submitted_at || new Date().toISOString(),
      data.entity_type || '',
      data.full_name || '',
      data.dob || '',
      data.email || '',
      data.whatsapp || '',
      data.country || '',
      data.nationality || '',
      data.address || '',
      data.has_ssn_itin || '',
      data.us_status || '',
      data.name_1 || '',
      data.name_2 || '',
      data.name_3 || '',
      data.business_description || '',
      data.industry || '',
      data.stage || '',
      data.existing_india_entity || '',
      Array.isArray(data.customer_geo) ? data.customer_geo.join(', ') : (data.customer_geo || ''),
      data.us_employees || '',
      data.us_physical || '',
      Array.isArray(data.payment_platforms) ? data.payment_platforms.join(', ') : (data.payment_platforms || ''),
      data.y1_revenue || '',
      data.num_owners || '',
      data.corporate_owner || '',
      data.ownership_split || '',
      coOwners[0],
      coOwners[1],
      coOwners[2],
      coOwners[3],
      data.investors_committed || '',
      data.investor_details || '',
      Array.isArray(data.svc) ? data.svc.join(', ') : (data.svc || ''),
      Array.isArray(data.ongoing) ? data.ongoing.join(', ') : (data.ongoing || ''),
      data.timeline || '',
      data.other_provider || '',
      data.other_provider_detail || '',
      data.notes || '',
      data.source || '',
      data._source_url || ''
    ];

    sheet.appendRow(row);

    // Send email alert
    const subject = 'BQP intake: ' + (data.full_name || 'new founder') + ' — ' + (data.country || '') + ' — ' + (data.entity_type || '');
    const body = Object.keys(data).map(k => k + ': ' + JSON.stringify(data[k])).join('\n');
    MailApp.sendEmail(NOTIFY_EMAIL, subject, body);

    return ContentService
      .createTextOutput(JSON.stringify({status: 'ok'}))
      .setMimeType(ContentService.MimeType.JSON);
  } catch (err) {
    return ContentService
      .createTextOutput(JSON.stringify({status: 'error', message: err.toString()}))
      .setMimeType(ContentService.MimeType.JSON);
  }
}

function doGet(e) {
  return ContentService.createTextOutput('BQP intake endpoint — POST only');
}
```

### 3. Deploy as a Web App

- Click **Deploy → New deployment**
- Settings:
  - **Type:** Web app
  - **Description:** BQP intake endpoint v1
  - **Execute as:** Me (your Google account)
  - **Who has access:** Anyone (so the form can POST without auth)
- Click **Deploy**
- Grant permissions when Google prompts (allow Apps Script to write to your sheet and send email on your behalf)
- Copy the deployment URL. Looks like:
  ```
  https://script.google.com/macros/s/AKfyc...xyz/exec
  ```

### 4. Wire it into the form

Open `us-incorporation-intake.html` and change line ~481:

```js
var GOOGLE_APPS_SCRIPT = "";
```

to:

```js
var GOOGLE_APPS_SCRIPT = "https://script.google.com/macros/s/AKfyc...xyz/exec";
```

Commit, push.

### 5. Test

Submit a dummy intake from an incognito window. Within 5-10 seconds:
- A new row appears in your Google Sheet.
- An email arrives at `durgesh@bharatquantumprospera.com`.

If nothing arrives, open the Apps Script editor → **Executions** tab → check for errors.

---

## OPTION C — Use both (max resilience)

If you set up BOTH Formspree AND Google Apps Script, the form tries Formspree first; if that errors, falls back to GAS; if that errors, falls back to email. Both endpoints receive the data.

Recommended for high-volume operations. Overkill at current volume.

---

## What the form sends you (per intake)

Every intake includes:
- Primary applicant: full legal name, DOB, email, WhatsApp, country, nationality, address, SSN/ITIN status, US immigration status
- Business: 3 name choices, description, industry, stage, existing Indian entity
- Operations: customer geography, US employees, US physical presence, payment platforms, Year 1 revenue
- Ownership: number of owners, corporate owner flag, ownership split, up to 4 co-owners' details, investor status + details
- Scope: core services wanted, ongoing compliance wanted, timeline, prior provider
- Notes: free-form additional context, how they found BQP

Total ~40 fields. Everything you need to draft the proposal with no follow-up questions needed.

---

## Proposal workflow once intake arrives

1. **Intake lands** → email alert + Google Sheet row (if GAS set up).
2. **Review within 24 hours** → scan the intake, confirm scope.
3. **Response options:**
   - WhatsApp a 2-line reply: "Received. Scoping call this [day] at [time]?"
   - Email a scoped written proposal (template below).
   - Both.

### Proposal email template (fill in from intake)

**Subject:** BQP Proposal — [Business Name] US Incorporation ([LLC / C-Corp])

Hi [Full Name],

Thanks for the intake. Based on what you shared, here's a scoped proposal.

**Recommended structure:** [Delaware C-Corp / Wyoming LLC / Delaware LLC]
**Reasoning:** [2-3 lines tied to their business + funding + customer profile from the intake]

**Scope (included):**
- State formation + Certificate [of Incorporation / of Formation]
- Registered agent (year 1)
- EIN via Form SS-4 fax / phone route (non-SSN)
- Operating Agreement / Bylaws + Shareholder Agreement
- Mercury / Brex business bank account introduction
- FEMA Form ODI (India side)
- [83(b) election if C-Corp]
- First-year compliance calendar

**Not included (quoted separately if wanted):**
- Form 5472 annual filing — [scope-based] / per year
- Transfer pricing documentation (if India-US inter-co flow) — [scope-based]
- State foreign qualification outside Delaware — [per state]

**Timeline:** 4-6 weeks from kickoff to funded Mercury account. [Adjust if urgent.]

**Fee:** [Scope-based number], fixed in writing before kickoff. 50% advance + 50% on EIN receipt.

**Next step:** 20-30 min scoping call to confirm fit. Pick a slot: [Calendly link or three day/time options].

Direct access throughout the mandate.

Durgesh
CA Durgesh Chavda · Founder, Bharat Quantum Prospera
+91 78018 87130 · WhatsApp

---

## Monitoring

Keep the Google Sheet pinned in your bookmarks. Expected volume as inbound traffic ramps:
- Month 1-3: 1-5 intakes/month
- Month 3-6: 5-15 intakes/month (if LinkedIn + newsletter is running)
- Month 6-12: 20-50 intakes/month (if GBP + reviews + 1 backlink from DA60+ publication landed)

Low conversion-rate on intakes (under 20%) usually means proposals are too slow (>48h) or pricing is misaligned. High conversion (>40%) usually means pricing has room to firm up.
