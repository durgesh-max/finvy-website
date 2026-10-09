# Client Portal — Honest SaaS Alternatives Comparison

**Context:** you asked for a client documentation portal with phone-OTP auth + folder-organised uploads to Drive. I've built the bespoke Firebase + Drive version (`/playbook/09-client-portal-firebase-setup.md`). This file compares that against purpose-built CA client portal SaaS products so you can pick the right path.

**TL;DR recommendation:**

- **1–20 active clients, you want full control + branding:** build the bespoke Firebase + Drive version. 60–90 min setup; near-zero cost; your brand on everything.
- **20–100 active clients, you want a proper CA workflow (not just file storage):** use **SuiteFiles** or **Karbon** (CA-built, integrated with document workflow + e-sign + task management).
- **100+ active clients, enterprise compliance (SOC 2, ISO 27001, Indian data residency):** use **Clio** (if law-adjacent) or **Zoho WorkDrive** (Indian data residency available).

---

## Honest comparison

| | **Bespoke (Firebase + Drive)** | **SuiteFiles** | **Karbon** | **Zoho WorkDrive** | **SmartVault** |
|---|---|---|---|---|---|
| **Monthly cost** | ~$0–5 (free tiers) | ~$10–30 per user | ~$59 per user | ~$3–9 per user | ~$25–65 per user |
| **Setup time** | 60–90 min + 2 hr dev | 1–2 days | 2–5 days | 2–4 hr | 2–3 days |
| **Branded (BQP look)** | Fully | Partial (via subdomain) | Limited (Karbon brand) | Partial (custom logo) | Limited |
| **Phone OTP** | ✓ (Firebase Auth) | Email/SMS 2FA | Email/password + 2FA | ✓ | ✓ |
| **Auto folder structure** | Fully customisable | Template-based | Workflow-based | Manual + templates | Template-based |
| **Year/month sub-folders** | ✓ (coded) | ✓ (manual template) | ✓ | ✓ | ✓ |
| **E-signature** | ✗ (DIY integration) | ✓ built-in | ✓ built-in | ✓ via Zoho Sign | ✓ built-in |
| **Task + workflow (per client)** | ✗ | ✓ limited | ✓ excellent | ✗ | ✓ |
| **Audit log** | ✓ (Firestore) | ✓ | ✓ | ✓ | ✓ |
| **Indian data residency** | ✗ (Google US/EU) | ✗ (Australia default) | ✗ (US) | ✓ (India DC option) | ✗ (US) |
| **SOC 2 / ISO 27001** | ✗ (Firebase inherits Google SOC 2) | ✓ SOC 2 | ✓ SOC 2 | ✓ SOC 2 + ISO 27001 | ✓ SOC 2 |
| **Mobile app** | PWA only (works but not native) | ✓ iOS/Android | ✓ iOS/Android | ✓ iOS/Android | ✓ iOS/Android |
| **Who signs in** | Clients + you | Clients + staff | Clients + staff | Clients + staff | Clients + staff |

---

## Detailed look at each

### 1. Bespoke Firebase + Google Drive (what I built)

**Pros:**
- Zero third-party monthly fee at your current scale.
- Fully branded `bharatquantumprospera.com/client-portal` — no SaaS logo.
- You own the data in your own Drive — no vendor lock-in.
- Codebase is yours; swap or extend any part.
- Folder structure you asked for (Income Tax / GST / ROC / etc. with year + month) baked in exactly as you specified.

**Cons:**
- You maintain it. If Google Drive API changes, Firebase SDK changes, SMS pricing changes — you adapt the code.
- No built-in e-signature, no task workflow, no engagement letter automation. Just file storage + auth.
- No native mobile app (works on mobile browsers, but no app-store presence).
- Google Drive data stored on Google US/EU servers unless you pay for Workspace Indian data region (~$5/user/month).

**When to pick this:** small practice (under 50 clients), you value control and brand, happy to grow it later.

---

### 2. SuiteFiles (`suitefiles.com`)

Built for accounting + legal practices. OneDrive-backed. Strong template system.

**Pros:**
- Purpose-built for CA/legal workflows. Templates per engagement type.
- Built-in e-signature (included in middle plan).
- Secure client portal with its own OTP/2FA.
- OneDrive backend — Microsoft infrastructure, 99.9% uptime SLA.
- 1–2 day setup — their onboarding team configures the templates.

**Cons:**
- Monthly cost scales with staff users (not client users): $10–30 per staff seat per month.
- Portal is branded "powered by SuiteFiles" (removable on higher tier).
- Australia-headquartered, data in Microsoft Azure (region picks available but not India).

**When to pick this:** 20–50 clients, you want a professional out-of-the-box portal, happy with SuiteFiles branding or willing to pay for white-label tier.

---

### 3. Karbon (`karbonhq.com`)

Full practice-management platform (not just document storage). Workflow + email + tasks + client collaboration.

**Pros:**
- Industry-standard for growing CA practices globally.
- Email + tasks + client requests + document portal all in one UI.
- Automated client-request workflows (e.g., "Request IT docs from client X by date Y").
- Clients see a dedicated portal; you see the full workflow dashboard.
- Deep integrations with Xero, QuickBooks, Zapier.

**Cons:**
- $59 per staff user per month — real money at 3+ staff.
- Overkill if you just want file storage.
- Learning curve: 1–2 weeks for a new practice to adopt.
- US-headquartered, data on AWS US.

**When to pick this:** you want practice management (not just a portal). 50+ clients. Multi-partner firm.

---

### 4. Zoho WorkDrive (`zoho.com/workdrive`)

Zoho's enterprise file collaboration, part of Zoho One. Indian company.

**Pros:**
- **Indian data residency available** (opt in to IN datacenter).
- Low cost: $3–9 per user per month.
- Integrates with Zoho Sign (e-sign), Zoho CRM, Zoho Books.
- Native mobile apps.
- Strong team-folder + access-control model.

**Cons:**
- Portal UI is Zoho-branded; limited white-label.
- Folder templates are manual (no auto-creation per client type the way our bespoke solution does).
- Workflow + task management requires Zoho Projects separately.
- Clients need to create Zoho accounts (minor friction).

**When to pick this:** you want Indian data residency + low cost + Zoho ecosystem integration. Common choice for Indian CA firms.

---

### 5. SmartVault (`smartvault.com`)

US-based document portal + e-sign specifically targeting accounting + legal.

**Pros:**
- Deep integrations with QuickBooks, Lacerte, UltraTax (US accounting software — less relevant in India).
- Built-in e-signature.
- Strong client portal with branded login.
- Good audit log + compliance reporting.

**Cons:**
- Expensive: $25–65 per staff user per month.
- US-focused; limited India-specific features.
- Data on US AWS.

**When to pick this:** cross-border US-serving practices with US software integrations. Less relevant for an India-primary firm.

---

## Decision framework

Pick based on your 12-month plan:

**Scenario A — You want portal LIVE this week, under 20 clients, brand-forward:**
→ Build the bespoke Firebase + Drive version. 60–90 min of your Firebase setup time; follow `/playbook/09-client-portal-firebase-setup.md`. Nothing else to buy.

**Scenario B — You want portal LIVE this week, under 20 clients, cost + Indian data residency matter:**
→ Zoho WorkDrive. $3–9/month. Indian DC. Enable in 2–4 hours.

**Scenario C — You want full practice management (tasks + emails + portal + billing), 20+ clients:**
→ Karbon. $59/user/month. Multi-week adoption.

**Scenario D — You want a mid-ground: professional portal with templates + e-sign but not full PM:**
→ SuiteFiles. $10–30/user/month. 1–2 day setup.

---

## My honest recommendation for BQP

Given where BQP is right now (growing practice, cost-sensitive, brand-focused, under 50 active clients):

**Phase 1 (now → 50 clients):** deploy the bespoke Firebase + Drive version I built. 60–90 min of your setup time. Zero monthly cost. Branded `bharatquantumprospera.com/client-portal`. Covers the exact folder structure you specified. No vendor lock-in.

**Phase 2 (50 → 200 clients):** when the practice outgrows the bespoke stack, migrate to **Karbon** (if you want workflow) or **Zoho WorkDrive** (if you just want more scalable storage with Indian data residency). Both can import file history from Drive.

**Phase 3 (200+ clients, multi-partner):** add a dedicated practice-management layer. Likely Karbon, possibly a bespoke CRM.

The bespoke version I built is designed to be good-enough-for-today without blocking later migration. If you prefer to skip Phase 1 and go straight to a SaaS, Zoho WorkDrive is the fastest path with Indian data residency. Say the word if you want me to wire the Zoho WorkDrive integration instead.
