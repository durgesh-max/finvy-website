# -*- coding: utf-8 -*-
"""Batch 3: 5 HowTo pages."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_seo import build_page, write_page

# -------- 13. How to get EIN as a foreign founder --------
write_page("how-to-get-ein-as-foreign-founder", build_page(
    slug="how-to-get-ein-as-foreign-founder",
    title="How to Get an EIN as a Foreign Founder (No SSN) - BQP",
    description="Step-by-step guide to getting an IRS Employer Identification Number (EIN) as a foreign founder with no SSN or ITIN. Form SS-4, IRS International EIN line, typical timeline.",
    keywords="EIN foreign founder, EIN no SSN, Form SS-4 foreign, IRS International EIN, EIN India, EIN Delaware LLC foreign, EIN application timeline, EIN by fax India, EIN letter CP 575",
    hero_kicker="HOW-TO · US SETUP",
    hero_title_html="Getting an EIN, <em>no SSN required.</em>",
    hero_lead="The Employer Identification Number is the tax ID your US entity needs before it can open a bank account, sign a lease, or file a return. Foreign founders can get one — the process is different from the domestic one. Here is how it actually works.",
    sections=[
        ("Overview", "What an EIN is and why you need it first",
         "<p>The EIN (Employer Identification Number) is the IRS-assigned 9-digit tax identification number for a US business entity — the corporate equivalent of an SSN. Every US-formed corporation and LLC needs one. Mercury and Brex will not open a bank account without it. Payment processors (Stripe, PayPal) will not activate the account without it. Contract counterparties want to see it on the W-9 or W-8 series form. It is the second thing you get after entity formation and the gating step for everything operational that follows.</p>"),
        ("Step-by-step process", "Four ways to file",
         "<p><strong>1. Online (US persons only):</strong> The IRS EIN online system at irs.gov/ein issues an EIN in minutes. But it requires the responsible party to have an SSN or ITIN. Foreign founders cannot use this route.</p>"
         "<p><strong>2. By fax:</strong> Complete Form SS-4 by hand or PDF, sign it, fax to the IRS at +1-855-215-1627 (international). This is the fastest route for foreign founders — the IRS typically returns the EIN by fax within 4-11 business days.</p>"
         "<p><strong>3. By mail:</strong> Post Form SS-4 to Internal Revenue Service, Attn: EIN International Operation, Cincinnati, OH 45999. Turnaround 6-8 weeks. Only use this if fax fails.</p>"
         "<p><strong>4. By phone (International EIN line):</strong> Call +1-267-941-1099 (not toll-free from India) Monday-Friday 06:00-23:00 ET. IRS agent asks the SS-4 questions verbally and issues the EIN on the call. Turnaround: same call. Line is busy but the fastest option when it works.</p>"),
        ("Form SS-4 line-by-line", "Getting the responsible party question right",
         "<p>The Form SS-4 responsible party question is where foreign founders trip up. Line 7a asks for the responsible party's name; line 7b asks for their SSN, ITIN, or EIN. Enter the founder's name in 7a. In 7b, write <strong>'Foreign / Non-US Applicant'</strong> if the founder has no SSN or ITIN. Do NOT invent an SSN. Do NOT leave it blank. This exact wording is accepted by the IRS International EIN unit and by every US bank that later reviews the EIN letter.</p>"
         "<p>Line 9a: select the correct entity type — Corporation for a Delaware C-Corp, LLC for an LLC (sub-classify as sole proprietor / partnership / corporation depending on tax elections). Line 10: reason for applying — 'Started a new business'. Line 11: date business started. Line 18: leave blank unless you had a previous EIN.</p>"),
        ("Timeline and what you receive", "The IRS CP 575 letter",
         "<p><strong>Fax route:</strong> 4-11 business days is typical; some founders get it in 2-3 days. Watch your fax daily.</p>"
         "<p><strong>Phone route:</strong> Same call if you get through. Line can be busy — dial early in the US morning (06:00-08:00 ET, which is 15:30-17:30 IST). IRS agent will verify identity questions and issue the EIN on the call, followed by the CP 575 letter by mail within 2 weeks.</p>"
         "<p>What you receive: the <strong>CP 575 confirmation letter</strong>. Store this permanently — you will need to show it to every bank, payment processor, and later tax filer. If you lose the CP 575, request a Letter 147C (EIN verification letter) from the IRS by calling the same number. The 147C is functionally equivalent for banking purposes.</p>"),
    ],
    faqs=[
        ("Can I get an EIN online if I don't have an SSN?",
         "No. The online EIN application at irs.gov/ein requires the responsible party to have a valid SSN or ITIN. Foreign founders must use fax, phone, or mail routes — fax is fastest and most reliable."),
        ("How long does the fax route actually take?",
         "IRS says 4 business days for foreign applicants; in practice 4-11 business days is typical. Some founders receive the EIN in 2-3 days when the IRS backlog is clear. Fax around 06:00-09:00 US ET for fastest handling."),
        ("Do I need an ITIN before I apply for the EIN?",
         "No. Do not apply for an ITIN just to get an EIN — the EIN can be obtained with 'Foreign / Non-US Applicant' on line 7b. ITIN application (Form W-7) takes 8-14 weeks and is unnecessary for entity EIN purposes."),
        ("Can a US registered agent get the EIN for me?",
         "Most registered agents (Stripe Atlas, Firstbase, Doola, Cogency Global, Northwest, Harvard Business Services) file SS-4 on behalf of the founder using Form 8821 (tax information authorisation) or Form 2848 (power of attorney). This is standard practice and usually faster than the founder self-filing."),
        ("What if the fax route stops working?",
         "The IRS temporarily suspended the fax route for foreign applicants in 2020-2021, then reinstated it. If fax is failing at the time you apply, use the phone route (+1-267-941-1099) or accept the mail delay. Registered agents can also expedite via their existing IRS relationships."),
        ("Does the entity need to be formed before I apply for the EIN?",
         "Yes. You need the state-filed formation document (Certificate of Incorporation, Articles of Organization) with an entity name and formation date before the IRS will issue an EIN. Formation first, EIN second, bank account third."),
    ],
    related=[
        ("us-incorporation.html", "Service", "US Incorporation for Indian Founders"),
        ("global-taxation.html", "Service", "Global Taxation Advisory"),
        ("corporate-legal.html", "Service", "Corporate Legal &amp; FEMA"),
    ],
    howto={
        "name": "How to get an EIN as a foreign founder without an SSN",
        "description": "Step-by-step process for obtaining an IRS Employer Identification Number for a US-incorporated entity when the responsible party has no US Social Security Number or ITIN.",
        "steps": [
            {"name": "Form the US entity first", "text": "File the Certificate of Incorporation (C-Corp) or Articles of Organization (LLC) with the state. Receive the state-issued formation document with entity name and formation date."},
            {"name": "Complete Form SS-4", "text": "Fill IRS Form SS-4 with entity name, address, responsible party name (line 7a), and 'Foreign / Non-US Applicant' in line 7b. Select entity type, reason for applying, and business start date."},
            {"name": "Fax Form SS-4 to IRS International", "text": "Fax the signed Form SS-4 to the IRS International EIN unit at +1-855-215-1627. Retain the fax confirmation receipt."},
            {"name": "Wait for EIN return", "text": "IRS typically returns the EIN by fax within 4-11 business days. Watch your fax and email daily. As a faster alternative, call the IRS International EIN line at +1-267-941-1099 to get the EIN issued on the call."},
            {"name": "Store the CP 575 letter", "text": "The IRS mails the CP 575 confirmation letter within 2 weeks. Store this permanently. It is required by banks, payment processors, and future tax filers. If lost, request a Letter 147C from the IRS."},
            {"name": "Proceed to bank account", "text": "With the EIN in hand, open the US business bank account (Mercury, Brex, Relay, or traditional bank). The bank will require the CP 575 or 147C letter plus your entity formation documents and passport ID."},
        ],
    },
    cta_headline="EIN stuck or need it fast?",
    cta_body="If you are stuck on line 7b, your fax is coming back blank, or the timeline is holding up your bank opening, we run the process end-to-end and get the EIN typically within 5-7 business days including the SS-4 preparation and IRS liaison.",
))

# -------- 14. How to file FBAR from India --------
write_page("how-to-file-fbar-from-india", build_page(
    slug="how-to-file-fbar-from-india",
    title="How to File FBAR (FinCEN 114) from India - BQP",
    description="Complete guide to filing FBAR (FinCEN Form 114) as an Indian resident with US accounts: thresholds, deadline, signature authority, penalties, and step-by-step BSA E-Filing System.",
    keywords="FBAR India, FinCEN 114 India, how to file FBAR, FBAR threshold 10000, FBAR signature authority, FBAR penalty, BSA E-Filing India, FBAR US person India, FBAR vs Form 8938",
    hero_kicker="HOW-TO · US TAX COMPLIANCE",
    hero_title_html="Filing FBAR from India, <em>step by step.</em>",
    hero_lead="The FBAR (FinCEN Form 114) is one of the most misunderstood US filings. If you are a US person with signature authority over any non-US financial account aggregating over USD 10,000 at any point in the year, you must file. Here is the working process.",
    sections=[
        ("Overview", "Who must file and why it matters",
         "<p>The FBAR (Report of Foreign Bank and Financial Accounts) is required under the Bank Secrecy Act. Any 'US person' with a financial interest in, or signature authority over, one or more foreign financial accounts with aggregate value exceeding USD 10,000 at any point during the calendar year must file. 'US person' includes US citizens, US resident aliens (green-card holders, substantial-presence-test satisfiers), and US entities. 'Foreign financial account' includes bank accounts, mutual fund accounts, brokerage accounts, and pension accounts held outside the US.</p>"
         "<p>For an Indian founder who has an SPV, a family bank account, or any signatory authority as a corporate officer over an Indian account, this rule applies once you become a US person. Missing the FBAR is one of the most-cited US tax mistakes for cross-border founders.</p>"),
        ("Thresholds and what counts", "The USD 10,000 aggregate test",
         "<p>The threshold is aggregate across all foreign accounts, not per-account. If you have four Indian accounts of USD 3,000 each, total USD 12,000, you must file. The threshold is tested at any single point during the year — a one-day peak above USD 10,000 triggers the filing obligation for the entire year.</p>"
         "<p><strong>Accounts that count:</strong> Indian savings and current accounts, fixed deposits, PPF, EPF (in certain readings), Indian mutual fund folios, Indian broker demat accounts, Indian company accounts where you are a signatory or beneficial owner.</p>"
         "<p><strong>Accounts that usually don't:</strong> Direct holdings of Indian real estate (not a financial account), physical gold in your possession, cryptocurrency in self-custody (unclear but usually not FBAR-reportable if in a wallet you control directly without an exchange intermediary — exchange-held crypto is a grey area FinCEN has signalled will be included).</p>"
         "<p><strong>Signature authority without financial interest:</strong> Still reportable. A corporate officer with signing authority over a corporate account must file even if they don't own it.</p>"),
        ("The BSA E-Filing System", "How to actually file",
         "<p>FBAR is filed electronically only, through the BSA E-Filing System at bsaefiling.fincen.treas.gov. Not through the IRS, not through the tax return. It is a separate FinCEN filing.</p>"
         "<p><strong>Steps:</strong></p>"
         "<ol>"
         "<li>Register at the BSA E-Filing System (first-time filers only). Get a User ID.</li>"
         "<li>Log in and select 'Report of Foreign Bank and Financial Accounts' (FinCEN 114).</li>"
         "<li>Enter filer details: name, US TIN (SSN or ITIN or EIN for entities), address.</li>"
         "<li>For each foreign account: bank name, address (full street address, city, country), account number, maximum value during the year in USD (converted at year-end Treasury exchange rate).</li>"
         "<li>Sign electronically. Submit.</li>"
         "<li>Retain the BSA acknowledgment (email + PDF) for six years.</li>"
         "</ol>"
         "<p>Deadline: <strong>15 April</strong> of the following year, with automatic extension to 15 October (no separate extension request needed — the extension is built in). No late-filing penalty if filed by 15 October.</p>"),
        ("Penalties for non-filing", "Why you never want to be here",
         "<p>Non-wilful failure to file: up to USD 10,000 per violation (per account per year, per some IRS interpretations). Wilful failure to file: up to the greater of USD 100,000 or 50% of the account balance per violation, per year. Criminal penalties possible for wilful cases (imprisonment up to 5 years).</p>"
         "<p><strong>If you missed prior years:</strong> Do not just start filing this year and forget the past. Prior-year non-filing does not go away. Cure options include: (i) the <strong>Streamlined Foreign Offshore Procedures</strong> for non-wilful cases residing outside the US (files last 6 years of FBAR + 3 years of amended 1040 — no penalty), or (ii) the <strong>Delinquent FBAR Submission Procedure</strong> (files past FBARs with an explanation — no penalty if IRS accepts the non-wilful characterisation). Consult before choosing the route; the wrong choice can escalate the exposure.</p>"),
    ],
    faqs=[
        ("Am I a US person if I have a US green card but live in India?",
         "Yes. Green card holders remain US persons for tax purposes regardless of physical residence — until the green card is formally surrendered via Form I-407. As a US person, worldwide income tax filing and FBAR both apply to you while you hold the green card."),
        ("Do I need to file FBAR if I have accounts under 10,000 USD each?",
         "Threshold is aggregate across all accounts, not per-account. If four accounts total more than USD 10,000 at any point during the year, all four are reportable. Test the peak balance, not the year-end balance."),
        ("Does FBAR replace Form 8938 or Schedule B?",
         "No. FBAR is a separate FinCEN filing. Form 8938 (Statement of Specified Foreign Financial Assets) is an IRS filing attached to Form 1040 with a higher threshold (USD 50k-200k depending on filing status and location). Schedule B (interest and dividends) has a Part III foreign account question. All three can apply to the same account holder; each has its own thresholds and requirements."),
        ("What exchange rate do I use for the maximum value?",
         "Use the US Treasury Department year-end exchange rate for the year being reported. Published on fiscal.treasury.gov. This is the standard for FBAR and gives a consistent USD conversion. Do not use the yearly average or the transaction-date rate."),
        ("What if I miss the 15 October extended deadline?",
         "File as soon as possible with an explanation. If genuinely non-wilful (unfamiliar with the rule, first-time filer, immediately corrected on becoming aware), the Delinquent FBAR Submission Procedure or Streamlined Foreign Offshore usually cures without penalty. Do not ignore — the exposure compounds year by year."),
        ("Does FBAR apply to my Indian PPF account?",
         "Contentious. FinCEN and IRS have not issued clear guidance. Most conservative practitioners report Indian PPF on FBAR because it is a foreign account under the definition. Under-reporting a PPF on FBAR while filing everything else can look selective. Ask your preparer to make an explicit decision."),
    ],
    related=[
        ("global-taxation.html", "Service", "Global Taxation Advisory"),
        ("us-incorporation.html", "Service", "US Incorporation for Indian Founders"),
        ("corporate-legal.html", "Service", "Corporate Legal &amp; FEMA"),
    ],
    howto={
        "name": "How to file FBAR (FinCEN Form 114) from India",
        "description": "Step-by-step process for US persons in India to file the FBAR reporting foreign financial accounts through the BSA E-Filing System.",
        "steps": [
            {"name": "Confirm US person status", "text": "Check that you are a US citizen, green card holder, or meet the substantial presence test. If yes, and if any foreign account (aggregate) exceeded USD 10,000 at any point in the year, FBAR applies."},
            {"name": "List all reportable accounts", "text": "List every foreign financial account you own, have financial interest in, or have signature authority over: bank accounts, brokerage, mutual funds, EPF, PPF (contentious), corporate accounts. Record bank name, address, account number, peak balance."},
            {"name": "Convert peak balances to USD", "text": "Convert each account's peak balance during the year to USD using the US Treasury year-end exchange rate for the reporting year, published on fiscal.treasury.gov."},
            {"name": "Register on BSA E-Filing System", "text": "Go to bsaefiling.fincen.treas.gov and register (first-time filers). Get a User ID and password."},
            {"name": "Complete FinCEN Form 114", "text": "Log in, select FinCEN 114, enter filer details, and enter each account with the required fields. Sign electronically."},
            {"name": "Submit before 15 October", "text": "Deadline is 15 April with automatic extension to 15 October. Submit and retain the BSA acknowledgment email and PDF for 6 years."},
        ],
    },
    cta_headline="Missed prior years or unsure if you are subject?",
    cta_body="FBAR non-filing is one of the most common and easiest-to-cure US compliance mistakes for cross-border founders — but the cure options differ dramatically by whether the past non-filing is characterised as wilful or non-wilful. Get the classification right before you file anything.",
))

# -------- 15. How to flip Indian company to US --------
write_page("how-to-flip-indian-company-to-us", build_page(
    slug="how-to-flip-indian-company-to-us",
    title="How to Flip an Indian Company to a US Parent - BQP",
    description="Step-by-step guide to the India-to-Delaware flip: share swap mechanics, FEMA ODI approval, Section 56 (angel tax) risk, valuation reports, transfer pricing, and timeline.",
    keywords="India to US flip, Delaware flip Indian startup, share swap India US, FEMA ODI approval flip, Section 56 angel tax flip, valuation report flip, US parent Indian subsidiary, restructuring Indian company to US",
    hero_kicker="HOW-TO · CROSS-BORDER RESTRUCTURING",
    hero_title_html="Flipping an Indian company to US, <em>done cleanly.</em>",
    hero_lead="The 'flip' — restructuring an Indian company so a Delaware C-Corp sits at the top — is one of the most consequential decisions a founder makes. Done right, it is tax-neutral and takes 8-14 weeks. Done wrong, it triggers Section 56, angel tax, or FEMA notices.",
    sections=[
        ("Overview", "What a flip actually is",
         "<p>A flip is a share swap: existing Indian shareholders (founders, ESOP holders, angel investors) exchange their Indian company shares for shares of a newly-formed Delaware C-Corp of equivalent value. The Delaware C-Corp thus becomes the 100% shareholder of the Indian company, which becomes its wholly-owned subsidiary. From that point on, all future equity issuance, fundraises, ESOPs, and eventually the IPO or exit happen at the Delaware parent level. This is the standard structure US-based VCs and eventual US acquirers expect.</p>"
         "<p>Not every Indian startup needs a flip. Flip only if (i) you are raising from US-based VCs who require a Delaware C-Corp portfolio company, (ii) your customer base is majority US, (iii) you are aiming for a US IPO or US acquisition. If you can raise capital in India and stay India-domiciled, don't flip — the ongoing compliance cost of a Delaware parent is meaningful and only worth paying if the strategic rationale is clear.</p>"),
        ("The core steps", "The 8-14 week process",
         "<ol>"
         "<li><strong>Form the Delaware C-Corp.</strong> Certificate of Incorporation, bylaws, initial founder stock at nominal par. 1-2 weeks.</li>"
         "<li><strong>Valuation report for both companies.</strong> Registered valuer produces Rule 11UA valuation of the Indian company on the scheme record date. US-side valuation of the Delaware C-Corp (typically nominal at this stage). 2-3 weeks.</li>"
         "<li><strong>Share swap agreement.</strong> Each Indian shareholder agrees to swap their Indian shares for Delaware C-Corp shares in the same ratio at the same valuation. Documentation includes SPA, share transfer agreements, board resolutions on both sides. 2-3 weeks.</li>"
         "<li><strong>FEMA ODI approval.</strong> Indian shareholders investing (via share swap) into the Delaware C-Corp is an Outbound Direct Investment under FEMA. Approval routes: automatic (if compliant with prescribed sectors, USD limits, and disclosure) or approval (if larger transaction or specific triggers). Form ODI filed through AD bank. 3-6 weeks.</li>"
         "<li><strong>Execute the swap.</strong> Simultaneous: (i) Indian shares transferred to Delaware C-Corp (Form SH-4 to Indian company, ROC filing), (ii) Delaware C-Corp shares issued to each former Indian shareholder in proportion. Payment: nil cash — pure share swap. 1 week.</li>"
         "<li><strong>Post-flip filings.</strong> Indian company: ROC filings, disclosure of ultimate holding company. Delaware C-Corp: Certificate of Incorporation amendments if authorised shares change, cap table update. RBI: Annual Performance Report from year 2 onwards. 2-4 weeks.</li>"
         "</ol>"),
        ("The tax traps", "Section 56, transfer pricing, capital gains",
         "<p><strong>Section 56(2)(x) — 'angel tax':</strong> If the Indian shareholder receives Delaware C-Corp shares of value greater than the value of Indian shares given up, the excess is taxable as income in the shareholder's hands at slab rate. The Rule 11UA valuation report is the primary defence — it must establish equivalence of value. Rushed valuations trigger this.</p>"
         "<p><strong>Section 9 — indirect transfer:</strong> If the flip is structured so that the ultimate beneficial owner changes (foreign investor buys the Delaware parent post-flip), the transaction can be recharacterised as an indirect transfer of Indian assets, triggering Indian capital gains tax. Timing matters — flip first, then raise; don't combine.</p>"
         "<p><strong>Transfer pricing:</strong> Post-flip, any transactions between Indian sub and Delaware parent (IP licensing, service fees, cost-sharing) are related-party transactions requiring Form 3CEB certification and arm's length pricing. Build the transfer pricing model at flip, don't wait.</p>"
         "<p><strong>DTAA position:</strong> Delaware C-Corp receiving dividends from Indian sub triggers Article 10 India-US DTAA — 15% withholding cap. Plan for this cash flow.</p>"),
        ("Timing and cost", "Typical flip profile",
         "<p>Total time: 8-14 weeks from decision to executed flip, assuming clean cap table, cooperating shareholders, and straightforward FEMA route.</p>"
         "<p>Total cost: INR 3-6 lakh for a founder-only, small-cap-table flip. INR 5-10 lakh with angel investors on the cap table (more valuation, more SPAs). INR 10-20 lakh for larger cap tables with institutional shareholders. Includes valuation reports, legal drafting on both sides, CA advisory, ROC filings, FEMA filings, US corporate filings.</p>"
         "<p>Timing rules of thumb: <strong>flip before a priced round</strong>, not during. <strong>Do not flip while an Indian tax assessment is pending</strong> on the Indian company. <strong>Do not flip if you're planning to sell the Indian sub within 24 months</strong> — Section 9 recharacterisation risk is high.</p>"),
    ],
    faqs=[
        ("Is a flip tax-neutral?",
         "It is designed to be. Done with a proper Rule 11UA valuation establishing value-equivalence, and no cash consideration on either side, Section 56 should not trigger. However, transfer pricing, capital gains on subsequent events, and DTAA-side taxation of future flows are all live considerations. Neutral at execution, not indefinitely thereafter."),
        ("How long does FEMA ODI approval take?",
         "Under the automatic route (most flips qualify), FEMA ODI is a reporting process not an approval process — filed with the AD bank, Form ODI submitted, and the transaction can proceed. Approval-route flips (larger transactions, specific sectors) can take 6-12 weeks with RBI. Most standard flips go the automatic route."),
        ("Can existing angel investors block a flip?",
         "Legally, majority shareholder consent is required for the SPA. Minority shareholders have information and consent rights depending on the shareholders' agreement. Practically, angels usually agree because a US flip is a value-accretive step for their exit. Written consent from each shareholder is required before FEMA filing."),
        ("What about ESOP holders — do they get swapped too?",
         "Yes. Existing Indian ESOP grants are cancelled and new Delaware C-Corp ESOP grants issued at equivalent value (with fresh Rule 11UA on the Indian side and 409A on the US side). The grant is a fresh grant — vesting periods can be preserved or reset by mutual agreement. Employee tax at swap depends on whether the grant is characterised as a fresh grant (usually not taxable) or a replacement (may be)."),
        ("Can I flip after raising a Series A in India?",
         "Technically yes, but much harder. Institutional investors on the cap table complicate consent, valuation, and often want anti-dilution or ratchet protections preserved. Flip pre-Series A is materially cleaner. Post-Series A flips are done, but expect 4-6 months and higher legal cost."),
        ("Do I need US legal counsel on top of Indian CA?",
         "Yes. Flip needs coordinated Indian and US counsel. The Delaware C-Corp filings, US cap table, and US tax positioning need US-qualified attorney sign-off. Indian filings need Indian company secretary and CA sign-off. BQP coordinates both sides in a single mandate."),
    ],
    related=[
        ("us-incorporation.html", "Service", "US Incorporation for Indian Founders"),
        ("global-taxation.html", "Service", "Global Taxation Advisory"),
        ("capital-advisory.html", "Service", "Capital Advisory"),
    ],
    howto={
        "name": "How to flip an Indian startup to a Delaware C-Corp parent",
        "description": "Step-by-step process for restructuring an Indian company so a newly-formed Delaware C-Corp becomes the 100% shareholder, via a tax-neutral share swap.",
        "steps": [
            {"name": "Form the Delaware C-Corp", "text": "File Delaware Certificate of Incorporation, adopt bylaws, issue nominal founder stock at par value."},
            {"name": "Obtain valuation reports", "text": "Registered valuer issues Rule 11UA valuation of the Indian company. US-side valuation of the Delaware C-Corp (typically nominal). Reports must establish value equivalence of the swap."},
            {"name": "Execute share swap agreement", "text": "Each Indian shareholder signs SPA to exchange Indian shares for Delaware C-Corp shares in the agreed ratio. Board resolutions on both sides. No cash consideration."},
            {"name": "File FEMA ODI", "text": "Indian shareholders' outbound investment into Delaware C-Corp is an ODI. File Form ODI through AD bank under automatic route (or approval route if triggered). Wait for AD bank confirmation."},
            {"name": "Complete the swap", "text": "Simultaneously transfer Indian shares (Form SH-4 + ROC filings) and issue Delaware C-Corp shares to each former Indian shareholder in proportion."},
            {"name": "Post-flip filings", "text": "ROC updates on Indian side, cap table update on US side, subsequent annual APR filings with RBI, transfer pricing documentation."},
        ],
    },
    cta_headline="Considering a flip before your next round?",
    cta_body="Flip timing is a five-figure decision that becomes a seven-figure decision if it goes wrong. The Rule 11UA valuation, FEMA ODI, share swap sequence and post-flip transfer pricing setup all need to happen in a specific order. BQP runs full flip mandates end-to-end.",
))

# -------- 16. How to file Form 5472 --------
write_page("how-to-file-form-5472", build_page(
    slug="how-to-file-form-5472",
    title="How to File Form 5472 for a Foreign-Owned US LLC - BQP",
    description="Step-by-step guide to filing Form 5472 with pro-forma Form 1120 for a foreign-owned single-member US LLC. Deadlines, penalties, reportable transactions, and safe-harbour tips.",
    keywords="Form 5472, foreign owned LLC 5472, Form 5472 filing, pro-forma 1120 LLC, Form 5472 penalty 25000, Form 5472 Indian founder, single member LLC foreign owner, Form 5472 reportable transactions",
    hero_kicker="HOW-TO · US TAX COMPLIANCE",
    hero_title_html="Filing Form 5472, <em>the LLC-owner playbook.</em>",
    hero_lead="If you are an Indian founder owning a US single-member LLC, Form 5472 is annual. Missing it is a USD 25,000 penalty. Here is the working process, the pro-forma 1120 wrapper, and the deadlines you cannot miss.",
    sections=[
        ("Overview", "Why Form 5472 exists and who must file",
         "<p>Form 5472 (Information Return of a 25% Foreign-Owned US Corporation or Foreign Corporation Engaged in a US Trade or Business) is an IRS filing that reports transactions between a US corporation (or foreign-owned disregarded LLC) and its foreign related parties. It exists so the IRS can monitor cross-border related-party dealings for transfer pricing and base-erosion purposes. Since 2017, foreign-owned single-member US LLCs (disregarded entities for US tax) are treated as separate corporations for Form 5472 purposes only, and must file annually.</p>"
         "<p>If you are an Indian resident owning 100% of a Delaware or Wyoming LLC that had any reportable transactions (including formation capital contribution, distributions, loans, services rendered) with you or another foreign related party during the year, Form 5472 applies.</p>"),
        ("The pro-forma 1120 wrapper", "How a disregarded LLC files",
         "<p>Disregarded LLCs normally do not file a US tax return — their income and expenses flow to the owner's return. But Form 5472 cannot be filed on its own; it must be attached to a Form 1120 (US Corporation Income Tax Return). So the process is:</p>"
         "<ol>"
         "<li>File a <strong>pro-forma Form 1120</strong> with the LLC's name, address, EIN, and only the top-of-form identification fields completed.</li>"
         "<li>Do <strong>not</strong> fill in income, deductions, or tax figures on the 1120 — write 'Foreign-owned US DE' across the top of the form (line 1a and 27) and 'See attached Form 5472' where relevant.</li>"
         "<li>Attach the completed Form 5472 for each foreign related party.</li>"
         "<li>Mail the package (electronic filing is technically available but the pro-forma wrapper works most reliably by paper).</li>"
         "</ol>"
         "<p>Mail to: Internal Revenue Service, 1973 Rulon White Blvd, M/S 6112, Attn: PIN Unit, Ogden, UT 84201. Or fax to +1-855-887-7737. Retain the mailing receipt (USPS registered mail or FedEx tracking).</p>"),
        ("What counts as a reportable transaction", "Line 4 of Form 5472",
         "<p>Reportable transactions include:</p>"
         "<ul>"
         "<li>Sales of tangible property between related parties</li>"
         "<li>Rents received or paid</li>"
         "<li>Royalties received or paid</li>"
         "<li>Services rendered or received</li>"
         "<li>Commissions</li>"
         "<li>Interest received or paid</li>"
         "<li>Loans and loan repayments (opening and closing balances)</li>"
         "<li>Capital contributions and distributions</li>"
         "<li>Any other consideration</li>"
         "</ul>"
         "<p>The threshold: <strong>zero.</strong> Any reportable transaction, however small, triggers the filing obligation. Even the initial capital contribution when you formed the LLC is a reportable transaction from the foreign owner to the LLC. This is why virtually every foreign-owned US LLC has a Form 5472 obligation from year one.</p>"),
        ("Deadlines and penalties", "The 15 April cliff",
         "<p><strong>Deadline:</strong> 15 April of the following year for calendar-year filers. Automatic extension to 15 October by filing Form 7004 before 15 April.</p>"
         "<p><strong>Penalty for failure to file:</strong> USD 25,000 per Form 5472 per year. Additional USD 25,000 for each 30-day period the failure continues after IRS notice. There is no de minimis. There is no small-taxpayer exception.</p>"
         "<p><strong>Late-filing cure:</strong> First-Time Abatement (FTA) may apply if the LLC has a clean prior compliance history. Reasonable-cause abatement is available if you can demonstrate genuine cause (not unfamiliarity with the rule — the IRS has explicitly said unfamiliarity is not reasonable cause for a foreign-owned LLC). Filed promptly on discovery, with an explanation, most first-time non-filings are abated. Do not ignore an IRS 5472 penalty notice.</p>"),
    ],
    faqs=[
        ("Do I need to file Form 5472 if my LLC had no income?",
         "Yes, if there were any reportable transactions with foreign related parties — including your initial capital contribution. Zero income does not exempt the filing. Every foreign-owned single-member LLC formed with capital contribution has at least one reportable transaction from day one."),
        ("What is a 'foreign related party' for Form 5472?",
         "Any person or entity that is (i) related to the reporting corporation under IRC Section 267(b) or 707(b) — generally 25%+ common ownership — and (ii) foreign. As a 100% foreign owner of a US LLC, you are automatically a foreign related party."),
        ("Can I file Form 5472 electronically?",
         "The IRS accepts electronic filing of Form 5472 attached to Form 1120 through professional tax software. For pro-forma 1120 with only Form 5472 attached, paper filing (or fax) is the most reliable route because e-file often chokes on the empty income/deduction fields."),
        ("What if I missed Form 5472 for prior years?",
         "File as soon as possible with reasonable-cause explanation. First-Time Abatement is available for one prior year if the LLC has otherwise clean compliance. Reasonable-cause abatement requires more than 'I didn't know' — need to show diligence and genuine cause. Most first-time non-filings are abated on prompt cure."),
        ("Does a US-formed multi-member LLC need Form 5472?",
         "A multi-member LLC that is a partnership for US tax files Form 1065 (not 1120) and issues K-1s. Form 5472 rules apply differently — the partnership files Form 5472 only if it has 25%+ foreign ownership through partners plus reportable transactions. Similar principle, different mechanics."),
        ("Does a Delaware C-Corp file Form 5472?",
         "Yes, if it has 25%+ foreign ownership and any reportable transactions with foreign related parties. It's filed as an attachment to the regular Form 1120 (not pro-forma). Standard for all Indian-founder-owned Delaware C-Corps that had a capital contribution from the founder."),
    ],
    related=[
        ("us-incorporation.html", "Service", "US Incorporation for Indian Founders"),
        ("global-taxation.html", "Service", "Global Taxation Advisory"),
        ("corporate-legal.html", "Service", "Corporate Legal &amp; FEMA"),
    ],
    howto={
        "name": "How to file Form 5472 for a foreign-owned US single-member LLC",
        "description": "Step-by-step process for filing IRS Form 5472 with a pro-forma Form 1120 wrapper for a US LLC 100% owned by a foreign person.",
        "steps": [
            {"name": "Identify reportable transactions", "text": "List every reportable transaction between the LLC and the foreign owner during the year: capital contributions, distributions, loans, service fees, interest, rent. Include opening and closing balances of any loans."},
            {"name": "Complete pro-forma Form 1120", "text": "Fill only the top-of-form identification: LLC name, address, EIN. Write 'Foreign-owned US DE' across relevant lines. Do not complete income, deduction, or tax fields."},
            {"name": "Complete Form 5472", "text": "Fill in the reporting corporation section, the foreign related party section, and Part IV listing each type of reportable transaction with dollar amounts."},
            {"name": "Attach and mail", "text": "Attach Form 5472 to the pro-forma 1120. Mail (or fax +1-855-887-7737) to IRS Ogden by the deadline. Use tracked mail; retain the tracking receipt."},
            {"name": "File by 15 April or extend", "text": "Deadline is 15 April of the following year. File Form 7004 before 15 April for automatic 6-month extension to 15 October if needed."},
            {"name": "Retain records", "text": "Retain a copy of the filed 5472 + pro-forma 1120, plus the mailing tracking receipt, for at least 6 years."},
        ],
    },
    cta_headline="Foreign-owned US LLC and unsure about 5472?",
    cta_body="If you have a Wyoming or Delaware LLC and were told by Atlas or Doola that 'nothing further is needed', that is wrong. Form 5472 applies from year one. BQP files 5472 + pro-forma 1120 as a standard part of our foreign-owned LLC compliance mandate.",
))

# -------- 17. How to file BOIR CTA --------
write_page("how-to-file-boir-cta", build_page(
    slug="how-to-file-boir-cta",
    title="How to File BOIR (Corporate Transparency Act) - BQP",
    description="Step-by-step guide to filing the Beneficial Ownership Information Report under the Corporate Transparency Act via FinCEN. Deadlines, exemptions, penalties, and current status of legal challenges.",
    keywords="BOIR filing, Corporate Transparency Act, CTA FinCEN, BOIR deadline, beneficial owner definition, BOIR India, BOIR exemption, BOIR penalty, FinCEN BOI report",
    hero_kicker="HOW-TO · US TRANSPARENCY REPORTING",
    hero_title_html="Filing the BOIR, <em>current position.</em>",
    hero_lead="The Corporate Transparency Act's Beneficial Ownership Information Report is one of the most-changed US filings of recent years — subject to court injunctions, revised deadlines, and successive guidance updates. Where the rule stands now and how to file when required.",
    sections=[
        ("Overview", "What the BOIR requires",
         "<p>The Corporate Transparency Act (CTA), enacted 2021, requires most US-formed entities (corporations, LLCs, and similar) to report their beneficial owners to the Financial Crimes Enforcement Network (FinCEN) via the Beneficial Ownership Information Report (BOIR). The intent is anti-money-laundering — FinCEN wants a database of who actually owns each US entity, so it can be queried by law enforcement and financial institutions.</p>"
         "<p>The rule has had a turbulent implementation. It went effective 1 January 2024, then was subject to nationwide injunctions in late 2024 and 2025 from federal courts finding constitutional issues. FinCEN has issued successive interim rules narrowing scope. Current status changes frequently — the working practice is to check FinCEN's current published position (fincen.gov/boi) before deciding whether to file.</p>"),
        ("Who must file (current position)", "Reporting companies and beneficial owners",
         "<p>A <strong>reporting company</strong> is defined as any domestic or foreign entity registered to do business in a US state by filing a document with a Secretary of State (or similar). This captures Delaware C-Corps, Wyoming LLCs, and virtually every entity Indian founders form. There are 23 exemption categories — most apply to already-regulated entities (banks, insurance, SEC-registered funds, public companies). Small operating companies generally do not qualify for an exemption.</p>"
         "<p>A <strong>beneficial owner</strong> is any individual who either (i) owns or controls at least 25% of the entity, or (ii) exercises substantial control (senior officers: CEO, CFO, general counsel, president, or any individual with direct or indirect power over important decisions). Both prongs apply — a small shareholder who serves as CEO is still a beneficial owner.</p>"
         "<p>Interim rule status: FinCEN's March 2025 interim rule narrowed the scope to exclude US persons who own or control US entities — leaving primarily <strong>foreign-owned</strong> or <strong>foreign-formed</strong> entities as the current filing population. Indian founders owning US LLCs or C-Corps clearly fall within the scope under the current interim rule. Verify the current position at fincen.gov/boi before filing.</p>"),
        ("How to file", "The BOI E-Filing System",
         "<p>Filing is electronic only at boiefiling.fincen.gov. There is no fee. There is no paper alternative.</p>"
         "<ol>"
         "<li>Go to boiefiling.fincen.gov and select 'File BOIR'.</li>"
         "<li>Enter <strong>reporting company details:</strong> legal name, any trade names, US address, jurisdiction of formation, EIN.</li>"
         "<li>For each <strong>beneficial owner:</strong> full legal name, date of birth, current residential address, unique identifying number from a valid ID (passport for foreign persons — provide passport number, issuing country, expiry date). Upload a clear image of the ID document.</li>"
         "<li>For each <strong>company applicant</strong> (individual who filed the entity formation document): same information as beneficial owner. Note: company applicant is only required for entities formed on or after 1 January 2024.</li>"
         "<li>Review the summary. Submit. Retain the BSA acknowledgment.</li>"
         "</ol>"
         "<p>Filing typically takes 20-40 minutes for a small entity. Updates (change of address, change of ownership, new beneficial owner) must be filed within 30 days of the change.</p>"),
        ("Deadlines and penalties", "As of the current interim rule",
         "<p><strong>Deadlines (current interim rule for foreign entities and their US-formed subsidiaries):</strong> For entities existing before 1 January 2024 (and now under the interim rule) — deadline extended by FinCEN's March 2025 interim rule; verify current deadline at fincen.gov. For entities formed on or after 1 January 2024 — 30 days from formation. For any change (change in beneficial owner information, address change) — 30 days from the change.</p>"
         "<p><strong>Penalties:</strong> Civil penalty up to USD 500 per day of continuing violation. Criminal penalty up to USD 10,000 and 2 years imprisonment for wilful failure or false filing. FinCEN has publicly stated it will take a good-faith-effort approach on first-time filers curing promptly on becoming aware.</p>"),
    ],
    faqs=[
        ("Is BOIR filing still required after the court injunctions?",
         "As of the current interim rule (updated multiple times in 2024-2025), filing is required for foreign-owned and foreign-formed entities and their US-formed subsidiaries. US persons owning US entities were largely excluded by the March 2025 interim rule. This position has changed several times — always check fincen.gov/boi for the current position before filing."),
        ("What information do I provide as an Indian founder?",
         "Full legal name, date of birth, current residential address, passport number, passport issuing country, passport expiry date, and a scanned image of the passport photo page. FinCEN accepts foreign passports as the identifying document for non-US beneficial owners."),
        ("What is a 'company applicant' and do I need to report one?",
         "Company applicants are the individuals who filed (or directed the filing of) the entity's formation document. Required only for entities formed on or after 1 January 2024. Usually the registered agent or a specific person at Stripe Atlas / Firstbase / your law firm. Provide their name, DOB, address, and ID details."),
        ("Is BOIR the same as Form 5472?",
         "No, they are separate filings for different purposes. BOIR is FinCEN — anti-money-laundering — reporting beneficial ownership. Form 5472 is IRS — reporting related-party transactions. Both may apply to the same LLC. Both are separate filings with separate deadlines."),
        ("What if I miss the BOIR deadline?",
         "File as soon as possible. FinCEN has publicly said it will focus enforcement on wilful non-filers, not on late first-time filers who cure promptly. Voluntary correction significantly reduces penalty exposure. Do not ignore — the daily penalty accrual is real."),
        ("Do I need to update the BOIR if my address changes?",
         "Yes. Any change to reported information — beneficial owner's residential address, entity address, ownership percentages, new beneficial owner joining, etc. — must be reported via an updated BOIR within 30 days of the change. Failing to update carries the same penalty exposure as failing the initial filing."),
    ],
    related=[
        ("us-incorporation.html", "Service", "US Incorporation for Indian Founders"),
        ("corporate-legal.html", "Service", "Corporate Legal &amp; FEMA"),
        ("global-taxation.html", "Service", "Global Taxation Advisory"),
    ],
    howto={
        "name": "How to file BOIR (Beneficial Ownership Information Report) with FinCEN",
        "description": "Step-by-step process for filing the Corporate Transparency Act BOIR at FinCEN for a US-formed entity with foreign beneficial owners.",
        "steps": [
            {"name": "Confirm filing obligation", "text": "Check fincen.gov/boi for the current interim rule position. Under the March 2025 interim rule, foreign-owned US entities and foreign entities registered in the US are within scope."},
            {"name": "Identify beneficial owners", "text": "List every individual who owns or controls 25%+ of the entity, plus any senior officer (CEO, CFO, president, general counsel, or individuals with substantial decision-making control)."},
            {"name": "Collect information for each beneficial owner", "text": "Full legal name, date of birth, current residential address, passport number, passport country of issue, passport expiry date, and a clear scanned image of the passport photo page."},
            {"name": "Go to the BOI E-Filing System", "text": "Access boiefiling.fincen.gov and select 'File BOIR'. Create an account if first-time filer."},
            {"name": "Enter reporting company and owner details", "text": "Complete reporting company section (name, address, EIN, jurisdiction) and add each beneficial owner with their details and uploaded ID image. Add company applicants if entity formed on/after 1 Jan 2024."},
            {"name": "Submit and retain acknowledgment", "text": "Review the summary, submit, and download the FinCEN acknowledgment. Retain permanently. Update within 30 days of any change to reported information."},
        ],
    },
    cta_headline="Confused about BOIR after the court injunctions?",
    cta_body="BOIR obligations have changed multiple times in the last 18 months. If you formed a US entity in 2024-2025 or have foreign owners, the current interim rule likely captures you. BQP tracks the current FinCEN position and files BOIR as part of our US compliance mandate.",
))

print("Batch 3 complete: 5 HowTo pages written")
