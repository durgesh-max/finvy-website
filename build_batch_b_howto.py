# -*- coding: utf-8 -*-
"""Batch B: 5 HowTo pages (Form 5472, FBAR, India-to-Delaware flip, BOIR, F-reorg)."""
from build_lib import page, write_page

# 1. Form 5472 filing
write_page("file-form-5472-foreign-owned-us-llc", page(
    slug="file-form-5472-foreign-owned-us-llc",
    title="How to File Form 5472 for Foreign-Owned US LLC 2026 | BQP",
    description="Form 5472 for a 25%+ foreign-owned US single-member LLC &mdash; who files, what reports, the pro forma 1120, due dates, USD 25,000 penalty exposure. Working CA guide for Indian founders.",
    keywords="Form 5472, foreign owned LLC Form 5472, pro forma 1120 LLC, 25% foreign owned LLC filing, Form 5472 penalty, DE LLC Indian owner Form 5472, Form 5472 due date, Form 5472 reportable transaction",
    hero_kicker="/ US compliance &middot; Form 5472",
    hero_title_html="File Form 5472, <em>without triggering a USD 25,000 penalty.</em>",
    hero_lead="Form 5472 is the single most-missed US filing for Indian founders. A Delaware single-member LLC owned 25%+ by a non-US person must file an annual pro forma Form 1120 + Form 5472 reporting related-party transactions &mdash; even if the LLC has no US income, no US activity, and owes no US tax. Miss it and the automatic penalty is USD 25,000 per form per year.",
    sections=[
        ("/ Who must file", "The trigger rules.",
         "<p>Form 5472 (Information Return of a 25% Foreign-Owned US Corporation or a Foreign Corporation Engaged in a US Trade or Business) is required where either:</p>"
         "<ul>"
         "<li>A US corporation is 25%+ foreign-owned (directly or by attribution) and has reportable transactions with a related party, OR</li>"
         "<li>A foreign-owned US disregarded entity &mdash; typically a single-member LLC with a non-US owner &mdash; has reportable transactions with its foreign owner or any related party.</li>"
         "</ul>"
         "<p>The disregarded-entity rule is the trap for Indian founders. A Delaware LLC with an Indian individual as single member is a disregarded entity for US federal tax &mdash; it files no Form 1040 of its own and the owner has no US tax liability where there is no US-source income. But since the 2017 regulations (TD 9796), that disregarded LLC is treated as a reporting corporation for Form 5472 purposes and must file.</p>"
         "<p>Reportable transactions include: any contribution of capital by the foreign owner to the LLC, any distribution, any inter-company payment, any loan or interest payment, any shared services. In practice almost every active LLC has at least one reportable transaction with the foreign owner each year &mdash; the capital funding of the US bank account alone qualifies.</p>"),
        ("/ What to file", "The pro forma 1120 + Form 5472 pair.",
         "<p>A foreign-owned disregarded LLC files:</p>"
         "<ol>"
         "<li><strong>Pro forma Form 1120</strong> &mdash; the US corporate income tax return skeleton. Only the identifying information section (name, EIN, address, foreign owner identification) is completed. Income, deductions, and tax lines remain blank because the LLC is disregarded for income-tax purposes. Mark the form 'FOREIGN-OWNED US DE' at the top.</li>"
         "<li><strong>Form 5472</strong> &mdash; the information return reporting the related-party transactions. One Form 5472 per related party is required.</li>"
         "<li>Both are filed together as a single filing packet.</li>"
         "</ol>"
         "<p>The LLC needs an EIN (Employer Identification Number) to file. If you incorporated via Stripe Atlas or a direct Delaware filing, the EIN is already in place. If not, Form SS-4 is used to obtain the EIN &mdash; the standard route for non-SSN applicants is fax or international phone, taking 4-8 weeks.</p>"),
        ("/ Due dates &amp; mechanics", "When and where to file.",
         "<p>Due date: 15th day of the 4th month following the end of the LLC's tax year. For a calendar-year LLC: <strong>15 April</strong>. Automatic 6-month extension via Form 7004 &mdash; moves the due date to 15 October.</p>"
         "<p>Filing method: paper filing to the Ogden, Utah IRS service center address specified on the Form 5472 instructions. The IRS does not accept e-file for foreign-owned disregarded entity 5472 filings as a standalone package &mdash; it must be mailed.</p>"
         "<p>Processing time: the IRS does not acknowledge receipt. US Postal Service Certified Mail + Return Receipt, or an international courier with tracking, is the only way to prove filing.</p>"),
        ("/ Common mistakes &amp; penalty exposure", "What triggers the USD 25,000.",
         "<p>The Form 5472 penalty is USD 25,000 per form per year under IRC Section 6038A &mdash; automatic, not discretionary, and generally not reduced for first-time offenders. Separate penalty for each year not filed.</p>"
         "<p>Common failures:</p>"
         "<ul>"
         "<li><strong>Didn't know it existed.</strong> The Indian founder relied on a Stripe Atlas incorporation and never saw a 5472 reminder. The LLC has no US income, so the founder assumed no US filing was due.</li>"
         "<li><strong>Filed Form 1120 only.</strong> The CA treated the LLC like a C-Corp and filed a full 1120 with zero income, missing the 5472 companion. The 5472 non-filing penalty still applies.</li>"
         "<li><strong>Missed the 'any reportable transaction' threshold.</strong> Even a USD 500 contribution of initial capital qualifies. Dormant LLCs with the single capital contribution still need to file for that year.</li>"
         "<li><strong>Named the related party wrong.</strong> Form 5472 asks for the foreign owner's identification details. A missing or incorrect foreign TIN / country is enough to invalidate the filing in a 6038A examination.</li>"
         "</ul>"
         "<p>If you have missed prior years, voluntary filing of back years before the IRS reaches out is the standard approach. Each back year still carries the penalty, but late-but-voluntary filers sometimes negotiate reduced penalties on reasonable-cause grounds.</p>"),
    ],
    faqs=[
        ("Does my Delaware LLC need to file Form 5472 if it had no US activity?",
         "Yes, if there was any reportable transaction with the foreign owner or a related party. The initial contribution of capital to fund the US bank account counts as a reportable transaction. In practice, almost every foreign-owned LLC has a Form 5472 obligation in each year of its existence, including dormant years."),
        ("What is the penalty for missing Form 5472?",
         "USD 25,000 per form per year under IRC Section 6038A. The penalty is automatic and separate for each year not filed. A single missed year is USD 25,000; three missed years is USD 75,000. The IRS does not typically reduce for first-time offenders."),
        ("Can I e-file Form 5472 for my single-member LLC?",
         "No. The foreign-owned disregarded entity Form 5472 package (pro forma 1120 + Form 5472) must be paper-filed to the Ogden, Utah IRS service center. E-file is not available for this standalone filing. Use USPS Certified Mail or an international courier with tracking."),
        ("Is Form 5472 required for a US C-Corp with Indian owners?",
         "Yes, if the C-Corp is 25%+ foreign-owned and has reportable transactions with related parties. For a C-Corp the Form 5472 is attached to the C-Corp's own Form 1120 (not a pro forma skeleton). This is the standard Delaware C-Corp with Indian founder-shareholders scenario."),
        ("What is the Form 5472 due date for a Delaware LLC owned by an Indian founder?",
         "15 April for a calendar-year LLC. Form 7004 extends it to 15 October. If the LLC uses a non-calendar tax year, the 15th day of the 4th month after year-end."),
        ("Does BQP handle Form 5472 for Indian founders?",
         "Yes. We handle one-off back-year clean-up and ongoing annual filings. Standard annual package covers the pro forma 1120 + Form 5472 + state franchise tax (Delaware) + registered agent coordination. Request via get-a-quote.html."),
    ],
    related=[
        ("us-incorporation.html", "Guide", "US LLC &amp; C-Corp incorporation"),
        ("delaware-franchise-tax-calculator.html", "Tool", "Delaware franchise tax calc"),
        ("get-a-quote.html", "Mandate", "Get a firm quote"),
    ],
    cta_headline="Missed Form 5472 for prior years?",
    cta_body="If you have a Delaware LLC and never filed Form 5472, each unfiled year is a USD 25,000 exposure. The clean-up is voluntary back-filing with a reasonable-cause statement. We handle the full stack: pro forma 1120, 5472s for each related party, back-year statements, and ongoing annual compliance.",
    howto={"name": "Steps", "description": "Step-by-step working-CA procedure.", "steps": [
        {"name": "Confirm reporting obligation", "text": "Verify the LLC is 25%+ foreign-owned (yes for a single-member LLC owned by an Indian individual) and had at least one reportable transaction in the year."},
        {"name": "Obtain EIN if missing", "text": "File Form SS-4 by fax or international phone if the LLC does not already have an EIN. Allow 4-8 weeks."},
        {"name": "Prepare pro forma Form 1120", "text": "Complete only identifying information; mark 'FOREIGN-OWNED US DE' at the top; income/deduction/tax lines blank."},
        {"name": "Prepare Form 5472 for each related party", "text": "Separate 5472 for the foreign owner and any other related party with reportable transactions."},
        {"name": "Paper-file to Ogden, Utah", "text": "Mail with USPS Certified Mail + Return Receipt or international courier with tracking. E-file is not available."},
        {"name": "Retain tracking confirmation", "text": "File tracking is your only proof of filing &mdash; retain for six years."}
    ]},
))

# 2. FBAR from India
write_page("file-fbar-from-india-indian-founder", page(
    slug="file-fbar-from-india-indian-founder",
    title="How to File FBAR from India 2026 | Indian Founder With US Entity - BQP",
    description="FBAR (FinCEN 114) for Indian founders with signatory authority over US bank accounts. Who files, USD 10,000 threshold, 30 June deadline (automatic extension 15 October), penalty exposure, from-India mechanics.",
    keywords="FBAR India, FinCEN 114 India, Indian founder US bank FBAR, FBAR signatory authority, FBAR deadline India, FBAR penalty India, FBAR Delaware LLC owner",
    hero_kicker="/ US compliance &middot; FBAR",
    hero_title_html="FBAR from India, <em>without the USD 10,000 penalty trap.</em>",
    hero_lead="FBAR &mdash; the Report of Foreign Bank and Financial Accounts, FinCEN Form 114 &mdash; is a US Treasury filing, not an IRS filing. It applies to US persons with signatory authority or financial interest in non-US accounts aggregating USD 10,000+. For Indian founders holding US entities, the mirror obligation applies to their US accounts if they are also US persons. Here is who, when, and how to file.",
    sections=[
        ("/ Who must file", "US-person test, signatory authority, threshold.",
         "<p>FBAR applies to a <strong>US person</strong> with a <strong>financial interest in</strong> or <strong>signatory authority over</strong> one or more foreign accounts the aggregate maximum value of which exceeded <strong>USD 10,000</strong> at any time during the calendar year.</p>"
         "<p>Three triggers for an Indian founder scenario:</p>"
         "<ol>"
         "<li><strong>Green-card-holder or dual-tax-resident founder</strong> with a US entity: the founder is a US person. All non-US accounts (Indian bank, Indian brokerage, Indian mutual funds, Indian PPF, Indian NPS, Indian insurance with cash value) aggregating USD 10,000+ at any point in the year must be reported.</li>"
         "<li><strong>Pure Indian-resident founder</strong> with a US entity: generally not a US person &mdash; no FBAR obligation for Indian accounts. However, if the founder is also a signatory on the US entity's US bank account, no FBAR filing is required for the US account itself (US accounts are not foreign to a US person; and for a non-US-person founder, there is no US person obligation at all).</li>"
         "<li><strong>Indian entity holding US bank account</strong>: no FBAR &mdash; FBAR is a US-person filing, not a US-entity filing. The US bank account held by an Indian company does not trigger FBAR.</li>"
         "</ol>"
         "<p>The ambiguous case &mdash; and the one that catches people &mdash; is the Indian founder on an H-1B, L-1, or green card. Once US-person status attaches (183-day substantial-presence test, green-card test, or voluntary election), the FBAR obligation attaches to all non-US accounts worldwide, including those held in India and never used while US-resident.</p>"),
        ("/ What qualifies as a reportable account", "Broader than you expect.",
         "<p>Reportable foreign accounts include:</p>"
         "<ul>"
         "<li>Bank savings and current accounts in India (SBI, HDFC, ICICI, Axis, etc.).</li>"
         "<li>Fixed deposits, recurring deposits.</li>"
         "<li>Demat and brokerage accounts (Zerodha, Groww, ICICI Direct, HDFC Securities).</li>"
         "<li>Mutual fund accounts (if held in a custody arrangement).</li>"
         "<li>PPF (Public Provident Fund) and EPF (Employee Provident Fund).</li>"
         "<li>NPS (National Pension System).</li>"
         "<li>Insurance policies with cash surrender value (ULIPs, endowment plans).</li>"
         "<li>Any Indian account over which the US person has signatory authority &mdash; including spouse-held or company-held accounts if signatory authority exists.</li>"
         "</ul>"
         "<p>Not reportable: direct real estate holdings, gold held outside a vault account, direct equity shares held in physical form (vanishingly rare after dematerialisation).</p>"),
        ("/ Due date &amp; mechanics", "15 October after automatic extension.",
         "<p>Due date: 15 April of the following year, with an automatic 6-month extension to 15 October &mdash; no extension form required. In practice almost everyone files by 15 October.</p>"
         "<p>Filing method: electronic only, through the FinCEN BSA E-Filing System at bsaefiling.fincen.treas.gov. No paper filing accepted. Requires creating an individual-filer account (one-time setup, 10-15 minutes).</p>"
         "<p>Information required per account:</p>"
         "<ul>"
         "<li>Account number.</li>"
         "<li>Name and address of the financial institution.</li>"
         "<li>Type of account (bank, securities, other).</li>"
         "<li>Maximum value during the calendar year, in USD (translate at the exchange rate on the date of maximum value or the Treasury year-end rate; be consistent).</li>"
         "<li>Nature of interest (own, joint, signatory only).</li>"
         "</ul>"),
        ("/ Penalty exposure", "The USD 10,000-plus trap.",
         "<p>FBAR penalties under 31 USC 5321 have two tiers:</p>"
         "<ul>"
         "<li><strong>Non-wilful violation:</strong> up to USD 10,000 per violation. The IRS has historically interpreted 'per violation' as per account per year, which the US Supreme Court narrowed in <em>Bittner v United States</em> (2023) to per form per year. Still a meaningful penalty for a filer with multiple missed years.</li>"
         "<li><strong>Wilful violation:</strong> up to the greater of USD 100,000 or 50% of the account balance per violation. Criminal referral possible for aggravated cases.</li>"
         "</ul>"
         "<p>Streamlined Foreign Offshore Procedures (SFOP) is the IRS clean-up route for non-wilful missed FBAR filers who are not under examination: file three years of amended 1040s + six years of back FBARs + a non-wilful certification. No penalty under SFOP if accepted.</p>"
         "<p>Streamlined Domestic Offshore Procedures (SDOP) for US-resident taxpayers has a 5% miscellaneous offshore penalty. Different route; same six-year back-filing requirement.</p>"),
    ],
    faqs=[
        ("I'm an Indian citizen living in India. Do I need to file FBAR for my Indian accounts?",
         "No. FBAR applies to US persons &mdash; US citizens, green-card holders, and tax residents (183-day substantial-presence test). A pure Indian tax resident with no US-person status has no FBAR obligation on Indian accounts."),
        ("I'm a green-card holder in the US with Indian accounts. Threshold?",
         "USD 10,000 aggregate maximum across all foreign accounts at any point in the calendar year. If your Indian SBI savings peaked at USD 7,000 and your mutual fund account peaked at USD 5,000, the USD 12,000 aggregate exceeds the threshold and FBAR is required for both accounts."),
        ("Does FBAR cover my Indian PPF and EPF?",
         "PPF yes &mdash; it is a financial account at a government-sponsored institution. EPF is also generally reportable. NPS also reportable. Several court decisions have held PPF reportable, and the conservative approach is to include it on FBAR."),
        ("What if I missed FBAR for multiple years?",
         "If the omission was non-wilful (did not know about the obligation; or knew but did not understand it applied to Indian accounts), the Streamlined Foreign Offshore Procedures (if foreign-resident) or Streamlined Domestic Offshore Procedures (if US-resident) is the standard clean-up. SFOP has no penalty if accepted; SDOP has a 5% miscellaneous offshore penalty. Both require six years of back FBARs plus three amended 1040s."),
        ("Does my US LLC's US bank account go on FBAR?",
         "No &mdash; the US bank account is a US-domestic account, not a foreign account. FBAR reports foreign accounts of a US person. For an Indian founder who is also a US person, the US LLC's US bank account is not an FBAR item; the Indian accounts are."),
        ("Does BQP handle FBAR filings for Indian founders in the US?",
         "Yes. One-off back-year clean-up via SFOP or SDOP, and ongoing annual FBAR filings for green-card and dual-tax-resident founders. Standard pricing per filer per year, with scoping for Streamlined back-year clean-ups separately. Request via get-a-quote.html."),
    ],
    related=[
        ("file-form-5472-foreign-owned-us-llc.html", "Guide", "Form 5472"),
        ("india-us-dtaa-withholding-rates.html", "Guide", "India-US DTAA Rates"),
        ("get-a-quote.html", "Mandate", "Get a firm quote"),
    ],
    cta_headline="Green-card or dual-tax-resident with Indian accounts?",
    cta_body="FBAR is the single most-missed US filing for Indian founders who moved to the US. If you have never filed, Streamlined Procedures let you clean up six years with no penalty (if non-wilful). We handle intake, back-FBAR preparation, amended 1040s, and the non-wilful certification.",
    howto={"name": "Steps", "description": "Step-by-step working-CA procedure.", "steps": [
        {"name": "Determine US-person status", "text": "Green card, US citizen, or substantial presence (183-day) test. Non-US persons have no FBAR obligation."},
        {"name": "List all foreign accounts", "text": "Include bank, demat, mutual fund, PPF, EPF, NPS, insurance with cash value, and any account with signatory authority."},
        {"name": "Determine maximum year value", "text": "The highest balance at any point in the calendar year, converted to USD."},
        {"name": "Check threshold", "text": "USD 10,000 aggregate across all foreign accounts. Yes to any point? File."},
        {"name": "Register on FinCEN BSA E-Filing", "text": "One-time individual filer setup at bsaefiling.fincen.treas.gov."},
        {"name": "File FinCEN 114 by 15 October", "text": "Due 15 April with automatic extension to 15 October. No form required for extension."},
        {"name": "Retain records for 5 years", "text": "Account statements showing maximum year value, kept for 5 years from the filing date."}
    ]},
))

# 3. India-to-Delaware flip
write_page("india-to-delaware-flip-structure", page(
    slug="india-to-delaware-flip-structure",
    title="India-to-Delaware Flip 2026 | Structure, FEMA, Tax, Mechanics - BQP",
    description="How to flip an Indian startup to Delaware C-Corp parent for US venture funding. FEMA/RBI valuation requirements, share-swap mechanics, Indian capital gains, 83(b) elections, timing. Working CA guide.",
    keywords="India Delaware flip, flip structure India US, Indian startup Delaware parent, FEMA flip, share swap India US, 83(b) election flip, Indian startup US funding flip",
    hero_kicker="/ Cross-border structure &middot; India-US flip",
    hero_title_html="India-to-Delaware flip, <em>without breaking FEMA.</em>",
    hero_lead="The flip &mdash; converting an Indian startup into a Delaware C-Corp parent with the Indian company as a wholly-owned subsidiary &mdash; is the standard structure for Indian founders raising from US venture capital. Done right it unlocks the Delaware investment, 83(b) elections for founders, and QSBS eligibility for US investors. Done wrong it triggers Indian capital gains, FEMA violations, and future tax deadlock.",
    sections=[
        ("/ Why flip", "What the Delaware parent delivers.",
         "<p>US venture capital invests into Delaware C-Corps. The reasons are structural: Delaware corporate law is familiar, VC-friendly, well-litigated. Standard preferred share terms (participating liquidation preferences, anti-dilution, protective provisions, drag-along) have Delaware case law support. SAFE and convertible-note instruments assume Delaware law.</p>"
         "<p>Secondary benefits:</p>"
         "<ul>"
         "<li><strong>83(b) elections:</strong> founders of a Delaware C-Corp can file an 83(b) election on their founder equity within 30 days of grant, locking in a nil capital-gains basis. The Indian equivalent (Section 17 ESOP rules) does not deliver the same tax outcome.</li>"
         "<li><strong>QSBS eligibility:</strong> US-resident founders holding Delaware C-Corp stock for 5+ years may qualify for USD 10M+ of capital gains exclusion under Section 1202 (QSBS).</li>"
         "<li><strong>Clean exit path:</strong> a Delaware acquiror prefers to acquire a Delaware target. An Indian target with Delaware parent gives a US acquiror a Delaware takeover with the Indian operations as a subsidiary.</li>"
         "</ul>"),
        ("/ The mechanics", "Share swap, valuation, FEMA approvals.",
         "<p>The standard flip structure:</p>"
         "<ol>"
         "<li>Incorporate a Delaware C-Corp as the new ultimate parent, with the founders as shareholders.</li>"
         "<li>Each Indian shareholder of the existing Indian company transfers their Indian shares to the Delaware parent in exchange for Delaware stock &mdash; a share-for-share swap.</li>"
         "<li>The Indian company becomes a wholly-owned subsidiary of the Delaware parent.</li>"
         "<li>Future funding rounds happen in the Delaware parent; cash is downstream-ed to the Indian subsidiary as needed via equity or inter-company loans (per FEMA Overseas Direct Investment / Downstream Investment rules).</li>"
         "</ol>"
         "<p>FEMA mechanics:</p>"
         "<ul>"
         "<li>The share transfer requires a Chartered Accountant valuation certificate &mdash; the Delaware parent's shares received must have fair market value at least equal to the Indian shares surrendered.</li>"
         "<li>If any Indian shareholder is receiving less than fair value in the swap, FEMA (Section 6 / Overseas Investment Rules 2022) requires RBI approval.</li>"
         "<li>Each Indian individual shareholder's outbound investment into the Delaware parent uses the Liberalised Remittance Scheme (LRS) limit of USD 250,000 per financial year, if cash is also moving; a pure share-for-share swap uses the Overseas Investment Regulations with Form FC-GPR / FC-TRS.</li>"
         "<li>Form ODI reporting to RBI within 30 days of the swap.</li>"
         "</ul>"),
        ("/ Indian tax consequences", "Capital gains on the swap.",
         "<p>From the Indian tax side, a share-for-share swap is a transfer under Section 2(47) of the Income Tax Act and triggers capital gains in the hands of each Indian shareholder:</p>"
         "<ul>"
         "<li>Capital gains = Fair market value of Delaware shares received <em>minus</em> cost of acquisition of Indian shares surrendered.</li>"
         "<li>Long-term if the Indian shares were held 24+ months (unlisted); otherwise short-term.</li>"
         "<li>LTCG on unlisted shares: 20% with indexation (or 12.5% without indexation post-July 2024).</li>"
         "<li>STCG on unlisted shares: taxed at slab rates.</li>"
         "</ul>"
         "<p>Section 47(viab) exempts share-for-share swaps in certain cross-border scheme-of-amalgamation scenarios, but these are structured court-approved amalgamations &mdash; not available for a founder-level flip. In practice founders flip at low valuations (before venture rounds) to minimise the capital gains exposure.</p>"
         "<p>Timing is critical: flipping at a USD 1-5M FMV (pre-seed, early seed) triggers manageable Indian capital gains. Flipping at a USD 20M+ FMV (Series A done, now trying to add Delaware parent to attract US investors) triggers large and often-unaffordable Indian LTCG.</p>"),
        ("/ Post-flip operating model", "Running Delaware over India.",
         "<p>After the flip the Delaware parent is the fundraising vehicle and employer of US-side employees; the Indian subsidiary is the operating entity for India-based team, product, and customers (if any). Cash flows:</p>"
         "<ul>"
         "<li><strong>Delaware receives investment</strong>, holds it, uses it for Delaware operations (US salaries, legal, accounting, go-to-market) and downstream-s to India via inter-company payments or new equity rounds in India.</li>"
         "<li><strong>Inter-company service agreement</strong> between Delaware (customer) and India (service provider) &mdash; the India subsidiary invoices Delaware for engineering, product, and operations services at a transfer-pricing-compliant markup (cost-plus 10-15% is standard; higher markups for IP-generating activity).</li>"
         "<li><strong>IP ownership</strong>: structuring IP ownership at Delaware level (with India performing services) is the US VC-preferred model. IP ownership at India level (with Delaware as a sales front) is sometimes used but faces more questions at Series B+ diligence.</li>"
         "<li><strong>Transfer pricing documentation</strong>: Indian TP study annual under Section 92D; US contemporaneous TP documentation under Section 482. Must be contemporaneous &mdash; retrofitting at year 5 is weak defence.</li>"
         "</ul>"),
    ],
    faqs=[
        ("When is the right time to flip?",
         "Before raising from US VCs if US VCs are the plan. Flipping at pre-seed or seed valuation (USD 1-5M FMV) keeps the Indian capital gains manageable. Flipping after Series A (USD 20M+ FMV) often triggers Indian LTCG at a scale that founders cannot afford to pay personally. If you know you want US VC money, flip early."),
        ("Does a flip trigger Indian capital gains tax?",
         "Yes. The share-for-share swap is a transfer under Section 2(47) and triggers Indian capital gains for each Indian shareholder. Long-term rate 20% with indexation (or 12.5% without, post-July 2024) on unlisted shares. The valuation at swap time determines the gain. Flipping early at low valuation minimises the tax exposure."),
        ("Do I need RBI approval to flip?",
         "Typically no explicit approval if the swap is at fair value and uses the Overseas Investment Regulations 2022 automatic-route path. Form ODI reporting within 30 days is required. RBI approval is needed where the swap is not at fair value, or where the resulting structure violates the automatic-route conditions (e.g., sector-specific restrictions)."),
        ("Can we flip after we have already taken Indian angel funding?",
         "Yes. Indian angels become shareholders of the Delaware parent via the swap. Their consent is required (they are participating in the share-for-share transaction). Their Indian capital gains apply to them. Typically angels understand the mechanic and consent, especially where the flip unlocks a US venture round."),
        ("Does the Indian subsidiary continue to pay Indian corporate tax?",
         "Yes. The Indian subsidiary is an Indian tax resident and pays Indian corporate tax (25% for most SME companies under the new regime, or lower rates for specific manufacturing). The service revenue it earns from the Delaware parent is Indian-taxable income. The Delaware parent pays US tax on its US-source income."),
        ("Does BQP structure flips?",
         "Yes end-to-end: valuation certificate, FEMA Form ODI, Delaware incorporation, share-swap documentation, Indian capital gains return, transfer-pricing documentation setup, inter-company service agreement, and ongoing annual compliance. Scoping depends on current cap table and timing. Request via get-a-quote.html."),
    ],
    related=[
        ("us-incorporation.html", "Guide", "US LLC &amp; C-Corp incorporation"),
        ("fema-odi-us-entity-indian-founder.html", "Guide", "FEMA ODI for Indian founders"),
        ("get-a-quote.html", "Mandate", "Get a firm quote"),
    ],
    cta_headline="Planning a US venture round? Flip first.",
    cta_body="The flip is the single most consequential structural decision for an India-founded company planning to raise US VC. Timing (early vs late) controls Indian capital gains exposure. Mechanics (valuation certificate, FEMA, Form ODI, transfer pricing) must be clean on day one. We scope, structure, document, and file.",
    howto={"name": "Steps", "description": "Step-by-step working-CA procedure.", "steps": [
        {"name": "Model Indian capital gains at current FMV", "text": "Each founder's capital gains = FMV of Delaware shares received minus cost of Indian shares. Flip early when FMV is low."},
        {"name": "Incorporate Delaware C-Corp", "text": "Standard Delaware incorporation via registered agent. Share classes mirror Indian cap table."},
        {"name": "Obtain CA valuation certificate for Indian shares", "text": "Required for FEMA fair-value compliance on the share swap."},
        {"name": "Execute share-swap agreements", "text": "Each Indian shareholder transfers Indian shares to Delaware parent in exchange for Delaware shares."},
        {"name": "File Form FC-TRS / FC-GPR with RBI", "text": "Within 30 days of the swap, via the RBI's FIRMS portal."},
        {"name": "File Form ODI for outbound investment", "text": "Via authorised dealer bank within 30 days."},
        {"name": "Set up inter-company service agreement", "text": "Delaware customer, India service provider, cost-plus 10-15% markup, documented."},
        {"name": "Transfer-pricing documentation", "text": "Indian TP study (Section 92D) annual; US contemporaneous TP documentation. First year sets the pattern."}
    ]},
))

# 4. BOIR CTA (Beneficial Ownership Information Report)
write_page("boir-cta-us-llc-indian-owner", page(
    slug="boir-cta-us-llc-indian-owner",
    title="BOIR / CTA for US LLC with Indian Owner 2026 | Current Status - BQP",
    description="Corporate Transparency Act BOIR filing status for US entities with Indian owners. 2024-2025 litigation and FinCEN enforcement timeline. Who files, what to report, current obligations. CA guide.",
    keywords="BOIR CTA India, Corporate Transparency Act Indian owner, BOIR filing US LLC, beneficial ownership US LLC India, FinCEN BOIR 2026, CTA injunction status, BOIR exemption",
    hero_kicker="/ US compliance &middot; BOIR / CTA",
    hero_title_html="BOIR / CTA for Indian owners, <em>current status 2026.</em>",
    hero_lead="The US Corporate Transparency Act (CTA) requires Beneficial Ownership Information Reports (BOIR) for US entities, naming the ultimate human owners. For Indian founders with US LLCs, the obligation was in force, then enjoined, then narrowed. Here is the current state and the practical filing position as of 2026.",
    sections=[
        ("/ Background", "What CTA requires in principle.",
         "<p>The Corporate Transparency Act (part of the National Defense Authorization Act 2021) requires 'reporting companies' &mdash; broadly, US-formed corporations and LLCs and foreign entities registered to do business in the US &mdash; to file a Beneficial Ownership Information Report with FinCEN naming each beneficial owner (individual with 25%+ ownership or substantial control).</p>"
         "<p>Original penalties: USD 500 per day for ongoing non-compliance, up to USD 10,000 criminal penalty and 2 years imprisonment for wilful violation.</p>"
         "<p>Information reported per beneficial owner: full name, date of birth, residential address, unique identifying number (passport, driver licence), image of the identification document.</p>"),
        ("/ The 2024-2025 litigation path", "Why it stopped, then changed.",
         "<p>Multiple federal courts enjoined CTA enforcement in 2024 on constitutional grounds (commerce-clause overreach, Fourth Amendment privacy). The Fifth Circuit and other circuits produced conflicting rulings.</p>"
         "<p>In March 2025 FinCEN issued an interim final rule narrowing CTA's scope: domestic US entities and US-citizen beneficial owners of foreign entities registered in the US were exempted from BOIR filing. The remaining obligation applies to <strong>foreign reporting companies</strong> (non-US entities registered to do business in US states) with <strong>non-US-citizen beneficial owners</strong>.</p>"
         "<p>Status as of 2026: the interim final rule remains in effect. Domestic US LLCs and C-Corps &mdash; the standard Delaware entity used by Indian founders &mdash; are not subject to BOIR filing under the current rule. This may change if the final rule or further litigation shifts position.</p>"),
        ("/ Current practical position", "Who should file now, who should not.",
         "<p>Based on the March 2025 interim final rule:</p>"
         "<ul>"
         "<li><strong>Delaware LLC owned by an Indian individual (standard case):</strong> domestic US entity, not currently required to file BOIR. Monitor FinCEN updates for the final rule.</li>"
         "<li><strong>Delaware C-Corp with Indian founder-shareholders:</strong> same &mdash; domestic entity, not currently filing. Monitor.</li>"
         "<li><strong>Indian company registered to do business in a US state (foreign reporting company):</strong> potentially within scope. Beneficial-owner analysis required; if any non-US-citizen beneficial owner, filing may be required.</li>"
         "<li><strong>Non-US-formed holding entity (e.g. BVI, Cayman, Singapore) registered in a US state:</strong> potentially within scope. Case-by-case analysis.</li>"
         "</ul>"
         "<p>Important caveat: FinCEN's interim rule is subject to revision. The final rule or a subsequent executive-order change could restore domestic-entity obligations. Entities that previously filed under the pre-2025 rules do not need to withdraw &mdash; filed BOIRs remain on file with FinCEN.</p>"),
        ("/ What to do operationally", "The 2026 BOIR workflow.",
         "<p>For an Indian founder with a Delaware LLC or C-Corp (the standard case):</p>"
         "<ol>"
         "<li>Document the current entity classification (domestic reporting company; exempt from BOIR under the March 2025 interim final rule).</li>"
         "<li>Retain beneficial-ownership documentation internally &mdash; names, dates of birth, addresses, ID copies &mdash; so that filing can be executed within 30 days if the rule changes.</li>"
         "<li>Subscribe to FinCEN updates and/or have a US CA/attorney who monitors final rule issuance.</li>"
         "<li>If the entity is a foreign reporting company (unusual for Indian founders): engage a specialist to run the beneficial-owner analysis and file BOIR as required.</li>"
         "</ol>"
         "<p>For entities that filed BOIR under the pre-2025 rule: the filing remains on record with FinCEN. No action required to withdraw. Future updates (change of address, change of ID document) should be reported under the pre-2025 process even if newly-arising obligations are different.</p>"),
    ],
    faqs=[
        ("Does my Delaware LLC still need to file BOIR in 2026?",
         "Based on the FinCEN interim final rule effective March 2025, a Delaware LLC that is a domestic reporting company is currently exempt from BOIR filing. The rule is subject to revision; monitor FinCEN for the final rule. This is subject to change."),
        ("What is the penalty for not filing BOIR?",
         "Under the original CTA, USD 500 per day of ongoing non-compliance plus criminal penalties up to USD 10,000 and 2 years imprisonment for wilful violation. Under the current interim final rule the enforcement against domestic reporting companies is deprioritised, but the statutory penalties remain on the books. If the rule reverts, back-filing with a reasonable-cause explanation is the standard path."),
        ("I filed BOIR in 2024 before the rules changed. Do I need to withdraw?",
         "No. The 2024 BOIR filing remains on record with FinCEN. No withdrawal mechanism is required. Keep internal records of what was filed."),
        ("Should I file BOIR anyway as a precaution?",
         "FinCEN is not currently accepting voluntary BOIRs from domestic reporting companies under the interim rule. If the rule reverts and filing becomes mandatory again, there will be a filing window announced. Monitor and be ready."),
        ("Does CTA / BOIR apply to Indian company that is NOT registered in a US state?",
         "No. CTA applies to entities formed in the US and foreign entities <em>registered to do business</em> in a US state. A pure Indian company with no US registration is outside CTA's scope entirely &mdash; CTA has nothing to do with Indian entities not operating formally in the US."),
        ("Does BQP monitor BOIR status for clients?",
         "Yes. For all clients with US entities we track the BOIR / CTA regulatory status and notify when a filing obligation activates. For entities currently exempt we retain the beneficial-ownership documentation pack internally so we can file within 30 days of a rule change. Request via get-a-quote.html."),
    ],
    related=[
        ("file-form-5472-foreign-owned-us-llc.html", "Guide", "Form 5472"),
        ("us-incorporation.html", "Guide", "US LLC &amp; C-Corp incorporation"),
        ("get-a-quote.html", "Mandate", "Get a firm quote"),
    ],
    cta_headline="BOIR / CTA still unclear? We monitor the rule, you keep operating.",
    cta_body="FinCEN's position on BOIR has shifted twice in 18 months. For Indian founders with Delaware entities, the current position is exempt &mdash; but regulations may revert. We maintain the beneficial-ownership documentation pack for every client entity so that filing can execute within 30 days of any rule change.",
    howto={"name": "Steps", "description": "Step-by-step working-CA procedure.", "steps": [
        {"name": "Classify entity type", "text": "Domestic (US-formed) or foreign reporting company (non-US formed, registered in a US state)?"},
        {"name": "Check current rule applicability", "text": "March 2025 interim final rule: domestic entities exempt; foreign reporting companies with non-US beneficial owners within scope."},
        {"name": "If exempt, retain BO documentation internally", "text": "Names, dates of birth, addresses, ID copies, ownership percentages &mdash; ready to file if the rule reverts."},
        {"name": "If within scope, prepare BOIR", "text": "File via FinCEN's BOI E-Filing System: boiefiling.fincen.gov. Information per each beneficial owner (25%+ or substantial control)."},
        {"name": "Monitor FinCEN final rule issuance", "text": "Subscribe to FinCEN updates or use a service that monitors regulatory status."},
        {"name": "Report material changes within 30 days", "text": "If a BOIR has been filed, changes to beneficial ownership, address, or ID documents must be reported within 30 days."}
    ]},
))

# 5. LLC-to-C-Corp F-reorganization
write_page("convert-llc-to-c-corp-f-reorganization", page(
    slug="convert-llc-to-c-corp-f-reorganization",
    title="Convert LLC to C-Corp (F-Reorganization) 2026 | India Founder Guide - BQP",
    description="How to convert a Delaware LLC into a Delaware C-Corp via F-reorganization under IRC Section 368(a)(1)(F). Tax-free mechanics, 83(b) elections, QSBS holding period preservation. Working CA guide.",
    keywords="LLC to C-Corp conversion, F reorganization LLC C-Corp, Delaware LLC to C-Corp Indian founder, QSBS LLC C-Corp conversion, 368(a)(1)(F), 83(b) election C-Corp conversion",
    hero_kicker="/ Entity conversion &middot; LLC to C-Corp",
    hero_title_html="LLC to C-Corp, <em>via F-reorganization.</em>",
    hero_lead="Many Indian founders incorporate a Delaware LLC first (simpler, lower cost, Stripe Atlas default) and later discover that US venture capital invests only in Delaware C-Corps. The conversion is routine &mdash; done as an F-reorganization under IRC Section 368(a)(1)(F) it is tax-free, preserves founder equity holding periods, and sets up 83(b) elections and QSBS eligibility.",
    sections=[
        ("/ Why convert", "LLC worked at inception; C-Corp works at Series A.",
         "<p>Reasons to start as an LLC:</p>"
         "<ul>"
         "<li>Lower formation cost and simpler setup (Stripe Atlas offers both, but LLC is cheaper and faster).</li>"
         "<li>Pass-through tax at the owner level &mdash; no C-Corp double taxation. Attractive if the entity is cash-flow positive early.</li>"
         "<li>Minimal annual compliance for a dormant or small-revenue single-member LLC.</li>"
         "</ul>"
         "<p>Reasons to convert at scale:</p>"
         "<ul>"
         "<li>US VCs invest only (or almost only) in Delaware C-Corps. Preferred stock terms, SAFEs, convertible notes, voting agreements all assume C-Corp structure.</li>"
         "<li>Stock options (ISOs, NSOs) are a C-Corp instrument &mdash; LLC profits-interests do not translate cleanly to standard employee equity.</li>"
         "<li>83(b) elections on founder equity need the founders holding restricted stock in a C-Corp (not LLC member units).</li>"
         "<li>QSBS (Section 1202) applies to C-Corp stock only. 5-year holding period starts from the conversion date on the shares received in the F-reorg (the LLC holding period does not carry over for QSBS).</li>"
         "</ul>"),
        ("/ F-reorganization mechanics", "The tax-free path.",
         "<p>IRC Section 368(a)(1)(F) defines an F-reorganization as a 'mere change in identity, form, or place of organization'. The LLC-to-C-Corp conversion where the ownership and operations continue unchanged qualifies as an F-reorg.</p>"
         "<p>Structure:</p>"
         "<ol>"
         "<li>Form a new Delaware C-Corp with the same ownership as the existing LLC.</li>"
         "<li>Each LLC member contributes their LLC interest to the new C-Corp in exchange for C-Corp stock.</li>"
         "<li>The LLC becomes a wholly-owned subsidiary of the C-Corp.</li>"
         "<li>Then the LLC is dissolved into the C-Corp (merger or liquidation), making the C-Corp the sole surviving entity.</li>"
         "</ol>"
         "<p>Alternative Delaware statutory conversion: file a Certificate of Conversion with the Delaware Secretary of State converting the LLC directly to a C-Corp in one step. This is often cleaner, with the same F-reorg tax treatment if executed properly.</p>"),
        ("/ Tax consequences", "Mostly zero, but watch the triggers.",
         "<p>For a true F-reorganization:</p>"
         "<ul>"
         "<li><strong>No gain or loss recognised</strong> at the member or entity level on the conversion.</li>"
         "<li><strong>C-Corp stock basis</strong> = LLC member's basis in the LLC interest, adjusted for any boot received.</li>"
         "<li><strong>Holding period</strong> of the C-Corp stock tacks on to the LLC interest holding period for general capital-gains purposes &mdash; but note the QSBS 5-year holding period is separate and starts afresh from the conversion date.</li>"
         "<li><strong>LLC accumulated losses</strong>: suspended losses do not carry forward into the C-Corp (one of the real costs of the conversion).</li>"
         "<li><strong>Section 752 debt allocations</strong>: changes to how LLC debt is allocated can trigger gain for a member whose share of debt decreases below their basis. Model each member's position.</li>"
         "</ul>"
         "<p>For an Indian founder scenario where the LLC is a disregarded entity (single member) with modest capital contributions and no accumulated losses, the F-reorg is typically fully tax-free with trivial model-out.</p>"),
        ("/ Post-conversion to-do list", "The 30-day window.",
         "<ol>"
         "<li><strong>Delaware Certificate of Incorporation</strong> for the new C-Corp (or Certificate of Conversion for the statutory conversion route).</li>"
         "<li><strong>Delaware franchise tax filings</strong>: the entity transitions from LLC franchise tax (USD 300 flat) to C-Corp franchise tax (minimum USD 400, scales with authorised shares).</li>"
         "<li><strong>83(b) elections</strong> for founder restricted stock: file within 30 days of the stock issuance. Mandatory window &mdash; miss it and you cannot recover.</li>"
         "<li><strong>EIN update</strong>: the C-Corp typically obtains a new EIN. The old LLC EIN is retained for closing out the LLC's final tax filings.</li>"
         "<li><strong>Form 2553 (optional S-Corp election)</strong>: generally NOT elected for founders planning US venture funding &mdash; non-US-citizen owners disqualify S-Corp status, and S-Corp cannot have preferred stock. Skip for VC-track companies.</li>"
         "<li><strong>Bank account</strong>: open new C-Corp account; close LLC account after moving funds and final payroll.</li>"
         "<li><strong>Contracts</strong>: assign LLC contracts to the C-Corp (or novate with each counterparty). Customer contracts, SaaS subscriptions, SaaS tools, employment agreements, independent-contractor agreements.</li>"
         "<li><strong>State registrations</strong>: foreign qualification in any states where the LLC was registered; renew for the C-Corp.</li>"
         "<li><strong>Form 5472 continuity</strong>: if the LLC was foreign-owned-disregarded, the final partial-year 5472 is filed. The C-Corp's ongoing 5472 obligation starts from the conversion date.</li>"
         "</ol>"),
    ],
    faqs=[
        ("Can I convert LLC to C-Corp without triggering US tax?",
         "Yes, under IRC Section 368(a)(1)(F) F-reorganization treatment, the conversion is tax-free at both the entity and the owner level. The owner's basis and holding period carry over to the C-Corp stock. The main exceptions are specific scenarios involving debt allocation changes or boot &mdash; model each shareholder's position before conversion."),
        ("Does the QSBS 5-year holding period include my LLC time?",
         "No. QSBS under Section 1202 requires 5 years of holding C-Corp stock. The holding period starts on the F-reorg conversion date. The time held as LLC member does not count for QSBS. If you are planning to rely on QSBS, convert early so the 5-year clock starts sooner."),
        ("Can I do a statutory conversion in Delaware instead of a full F-reorg?",
         "Yes. Delaware allows a direct statutory conversion of an LLC to a C-Corp by filing a Certificate of Conversion plus a Certificate of Incorporation. If structured so that the former LLC members hold the C-Corp stock, the transaction is treated as an F-reorg for US federal tax purposes. One filing vs the multi-step F-reorg structure; same tax outcome."),
        ("When should an Indian founder convert LLC to C-Corp?",
         "Before raising US VC capital, if US VC capital is the plan. Many Indian founders start with an LLC via Stripe Atlas, operate for 1-2 years, then convert when a US VC term sheet appears. The conversion is routine and typically completed in 30-60 days with the Delaware filings, legal documents, and tax elections."),
        ("Do I need an 83(b) election after the conversion?",
         "Yes if the founder receives C-Corp stock that is subject to vesting. The 83(b) election is filed within 30 days of the stock issuance (not 30 days from the conversion filing). It locks in the then-FMV as the taxable amount, so founder equity in a low-FMV early-stage C-Corp has essentially zero 83(b) tax cost. Missing the 30-day window is unrecoverable."),
        ("Does BQP handle LLC-to-C-Corp conversions?",
         "Yes. Standard engagement covers: Delaware Certificate of Conversion + Certificate of Incorporation; member-to-shareholder exchange documentation; 83(b) election preparation; EIN update; final LLC tax filings (pro forma 1120 + 5472 if foreign-owned-disregarded); first C-Corp year-start compliance setup. Request via get-a-quote.html."),
    ],
    related=[
        ("us-incorporation.html", "Guide", "US LLC &amp; C-Corp incorporation"),
        ("india-to-delaware-flip-structure.html", "Guide", "India-to-Delaware flip"),
        ("get-a-quote.html", "Mandate", "Get a firm quote"),
    ],
    cta_headline="Have a Stripe Atlas LLC and now talking to US VCs?",
    cta_body="Convert first. The LLC-to-C-Corp F-reorg is routine (30-60 days), tax-free in the standard founder scenario, and starts the QSBS 5-year clock. 83(b) elections on the conversion-date C-Corp stock issuance must file within 30 days &mdash; miss it and you cannot recover.",
    howto={"name": "Steps", "description": "Step-by-step working-CA procedure.", "steps": [
        {"name": "Model tax consequences", "text": "F-reorg is tax-free in the standard scenario. Check debt allocation changes and boot before proceeding."},
        {"name": "File Delaware Certificate of Conversion + Certificate of Incorporation", "text": "Direct statutory conversion is cleaner than a multi-step F-reorg structure. Same tax outcome."},
        {"name": "Issue C-Corp stock to former LLC members", "text": "Mirror the LLC ownership percentages. Vesting schedules can be added for founder restricted stock."},
        {"name": "File 83(b) election within 30 days of stock issuance", "text": "Mandatory window for founders with vesting restrictions. Missing is unrecoverable."},
        {"name": "Obtain new EIN for C-Corp", "text": "Via Form SS-4; keep old LLC EIN active until LLC final return filed."},
        {"name": "Transition Delaware franchise tax regime", "text": "LLC USD 300 flat to C-Corp min USD 400 scaling with authorised shares. Choose authorised share count carefully."},
        {"name": "Assign or novate contracts", "text": "LLC contracts (customers, vendors, employees, SaaS) assigned to or novated with the C-Corp."},
        {"name": "File final LLC tax filings", "text": "Pro forma 1120 + 5472 for the stub period if the LLC was foreign-owned disregarded."}
    ]},
))

print("Batch B complete: 5 HowTo pages written")
