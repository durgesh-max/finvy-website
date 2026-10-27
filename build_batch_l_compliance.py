# -*- coding: utf-8 -*-
"""Batch L: 10 compliance-gap SEO pages (Oct 2026).

Topics picked by overlapping (a) high verifiable search volume with
(b) gaps in BQP's content library. These are current, real-time
regulations with evergreen high search demand.
"""
from build_lib import page, write_page

# 1. Dematerialisation of Unlisted Shares
write_page("dematerialisation-unlisted-shares-india-mandatory", page(
    slug="dematerialisation-unlisted-shares-india-mandatory",
    title="Dematerialisation of Unlisted Shares India | MCA Oct 2024 Mandate - BQP",
    description="MCA Rule 9B (Companies PAS Second Amendment Rules 2023) mandates demat form for all unlisted public and private company share transfers / allotments from Oct 2024. ISIN, NSDL/CDSL route, LLP exemption, penalty for non-compliance. Working CA guide by Durgesh Chavda.",
    keywords="dematerialisation unlisted shares India 2024, Rule 9B MCA demat mandate, ISIN private limited company, NSDL CDSL unlisted shares, Form PAS-6 compliance, private company demat requirement",
    hero_kicker="/ Blog &middot; Demat of Unlisted Shares &middot; Updated 2026-10-12",
    hero_title_html="Dematerialisation of unlisted shares, <em>MCA mandate explained.</em>",
    hero_lead="MCA notified Rule 9B of Companies (Prospectus and Allotment of Securities) Rules, requiring every unlisted public and private company (except small companies and government companies) to issue, allot, buy back, transmit or transfer securities only in dematerialised form from <strong>October 2024</strong>. Two years in, many private companies are still not compliant. Non-compliance blocks share transfers, fundraising, and ESOP issuance. Here is the practitioner's execution guide.",
    sections=[
        ("/ What Rule 9B actually requires", "The core mandate.",
         "<p>Rule 9B of the Companies (Prospectus and Allotment of Securities) Rules 2014 (introduced via Companies PAS Second Amendment Rules 2023, effective <strong>27 October 2023</strong>):</p>"
         "<ul>"
         "<li>Every <strong>unlisted public company AND private company</strong> (other than small company and government company) must:</li>"
         "<li>&nbsp;&nbsp;&mdash; Issue securities only in dematerialised form.</li>"
         "<li>&nbsp;&nbsp;&mdash; Facilitate dematerialisation of existing shareholders' securities before any new issuance / transfer / buyback / transmission.</li>"
         "<li>Effective for private companies from <strong>30 September 2024</strong> (extended once from 30 September 2024 to accommodate implementation).</li>"
         "<li>Deadline for existing holders to demat: 30 September 2024 (post-notification; some extensions granted for specific company sizes).</li>"
         "</ul>"
         "<p><strong>Exempt from Rule 9B:</strong></p>"
         "<ul>"
         "<li>Small companies (paid-up capital up to INR 4 crore + turnover up to INR 40 crore under Section 2(85)).</li>"
         "<li>Government companies.</li>"
         "<li>Nidhi companies and specific other categories per MCA notification.</li>"
         "</ul>"
         "<p>In practice, most mid-sized Indian startups and growth-stage private companies cross the small-company threshold once their funding round or revenue scales &mdash; Rule 9B applies.</p>"),
        ("/ What non-compliance blocks", "Material consequences.",
         "<ul>"
         "<li><strong>Any new share issuance / allotment</strong> cannot proceed in physical form &mdash; must be demat. Means every subsequent fundraising round, ESOP allotment, bonus issue, rights issue requires demat setup first.</li>"
         "<li><strong>Share transfers blocked</strong> &mdash; share transfer in physical form is not permissible under Rule 9B.</li>"
         "<li><strong>Buyback blocked</strong>.</li>"
         "<li><strong>Transmission (on shareholder death) blocked</strong>.</li>"
         "<li><strong>Form PAS-6 (Reconciliation of Share Capital Audit Report) filing</strong> &mdash; mandatory half-yearly filing starting 60 days from end of each half-year. Non-filing attracts penalty.</li>"
         "<li>Potential Section 450 penalty under Companies Act (default where no specific penalty is specified) &mdash; up to INR 10,000 and INR 1,000 per day of continuing default.</li>"
         "</ul>"
         "<p>Operational impact: your Series A term sheet closes, you need to allot new preferred shares, and demat is not set up. The round delays by 30-60 days while demat gets completed. Common in 2024-2025; still happens.</p>"),
        ("/ Step-by-step compliance", "The execution workflow.",
         "<ol>"
         "<li><strong>Obtain ISIN</strong> (International Securities Identification Number) for each class of security from NSDL or CDSL. Submit application via a Registrar &amp; Transfer Agent (RTA). Fee ~INR 10,000-20,000 one-time per ISIN.</li>"
         "<li><strong>Appoint a Depository Participant (DP)</strong> &mdash; the company itself engages a DP (NSDL / CDSL registered broker) to facilitate demat.</li>"
         "<li><strong>Communicate to all shareholders</strong>: formal letter + email instructing them to open demat accounts and submit demat request through their respective DPs.</li>"
         "<li><strong>Shareholders open demat accounts</strong> (if they don't have one) with any DP of their choice; submit Dematerialisation Request Form (DRF) + physical share certificate to the DP.</li>"
         "<li><strong>DP forwards demat request</strong> to the company's RTA.</li>"
         "<li><strong>Company's RTA / company verifies</strong> and confirms demat; shares credited to shareholder's demat account.</li>"
         "<li><strong>Physical share certificates are cancelled</strong> by the company and defaced.</li>"
         "<li><strong>File Form PAS-6</strong> with ROC half-yearly within 60 days of end of each half-year (30 September and 31 March), reporting demat reconciliation.</li>"
         "</ol>"
         "<p>Timeline: 30-90 days end-to-end depending on shareholder responsiveness and number of folios. For companies with foreign shareholders or scattered small holders, longer.</p>"),
        ("/ Common execution problems", "What trips companies up.",
         "<ul>"
         "<li><strong>Shareholders can't be reached</strong> &mdash; especially angel investors or ESOP holders who have moved jobs/countries. Chase relentlessly; document attempts.</li>"
         "<li><strong>Share certificates lost</strong> &mdash; original physical certificate missing. Need to issue duplicate under Rule 6, which has its own procedure (public notice, indemnity bond, Rule 6 cert).</li>"
         "<li><strong>Foreign shareholders</strong> &mdash; need to open NRO / NRE-linked demat account or hold through FPI route. Longer timeline. KYC and FATCA / CRS declarations.</li>"
         "<li><strong>Shareholders' bank account mismatch</strong> &mdash; demat KYC requires PAN + bank linkage; small folders often have outdated info.</li>"
         "<li><strong>ISIN approval delay</strong> &mdash; NSDL / CDSL can take 15-30 days. Apply early.</li>"
         "<li><strong>Form PAS-6 skipped</strong> &mdash; many companies get the demat done but forget the half-yearly PAS-6 filing. Penalty accrues.</li>"
         "</ul>"
         "<p><em>Last updated: 2026-10-12.</em></p>"),
    ],
    faqs=[
        ("Which companies must dematerialise shares under Rule 9B?",
         "All unlisted public companies and private companies (except small companies, government companies, Nidhi companies). Small company threshold under Section 2(85): paid-up capital up to INR 4 crore + turnover up to INR 40 crore. Most growth-stage startups and mid-sized private companies cross this and are in scope."),
        ("What is the deadline for private company demat under Rule 9B?",
         "Rule 9B became effective for private companies from 30 September 2024 (extended once). Existing shareholders should have their physical shares dematerialised by then. From that date, any new issuance / transfer / buyback / transmission cannot proceed in physical form."),
        ("How do I get ISIN for my private limited company shares?",
         "Apply via a Registrar & Transfer Agent (RTA) to NSDL or CDSL (depositories). Submit application with company documents (MOA, AOA, incorporation certificate, latest audited balance sheet). One-time fee approximately INR 10,000-20,000 per class of security (equity, preference, debentures). Approval typically 15-30 days."),
        ("What is Form PAS-6 and when do I file it?",
         "Half-yearly Reconciliation of Share Capital Audit Report under Rule 9A. Filed within 60 days of each half-year end (30 September and 31 March). Reports reconciliation between issued capital and demat-held capital. Mandatory for companies in demat form; non-filing attracts penalty under Section 450."),
        ("What if a shareholder refuses or cannot be contacted for demat?",
         "Company documents the attempts (RPAD letters, emails, newspaper notice if needed). Share remains physical in that shareholder's name but the company's compliance obligation is to facilitate demat, not force it. For share transfer / further allotment, that specific shareholder's shares will not be transferable until they demat. Chase persistently."),
        ("Does BQP handle demat execution for private companies?",
         "Yes - ISIN application co-ordination, RTA engagement, shareholder communication templates, Form PAS-6 half-yearly filing, duplicate share certificate issuance under Rule 6 for lost certificates, foreign shareholder demat co-ordination. Standard engagement scoped per shareholder count. WhatsApp +91 78018 87130."),
    ],
    related=[
        ("us-incorporation-intake.html", "Form", "Intake Form"),
        ("insights.html", "Library", "All Guides"),
    ],
    cta_headline="Private company with shareholders still in physical form?",
    cta_body="Compliance already overdue since Sep 2024. Blocks every new allotment / transfer / fundraising. BQP engagement: ISIN + RTA + shareholder coordination + PAS-6 filing. Standard 30-90 day execution scoped per shareholder count.",
))

# 2. Section 148 / 148A Reassessment
write_page("section-148-148a-reassessment-notice-response-india", page(
    slug="section-148-148a-reassessment-notice-response-india",
    title="Section 148 / 148A Reassessment Notice Response India 2026 - BQP",
    description="Section 148 reassessment notice received: understand Section 148A show-cause procedure, 4-year vs 10-year time limits, response window, Finance Act 2021 amendments, income escaping assessment thresholds, how to respond. Working CA guide by Durgesh Chavda.",
    keywords="Section 148 reassessment notice response, Section 148A show cause notice reply, income escaping assessment India, reopening of assessment Finance Act 2021",
    hero_kicker="/ Blog &middot; Section 148 Reassessment &middot; Updated 2026-10-12",
    hero_title_html="Section 148 / 148A reassessment, <em>what to do in the first 7 days.</em>",
    hero_lead="Section 148 reassessment notice means the Assessing Officer has reason to believe income has escaped assessment in a prior year. Post Finance Act 2021, there's a new procedure: Section 148A (show-cause before formal notice). Time limits are 4 years (standard) or 10 years (where escaped income is INR 50 lakh+ in asset form). First response, document access, and legal position taken in Section 148A often decide the entire proceeding. Here's the practitioner's playbook.",
    sections=[
        ("/ The new procedure (Finance Act 2021)", "148A then 148.",
         "<p>Finance Act 2021 restructured reassessment under Sections 147-153. The current framework:</p>"
         "<p><strong>Step 1 - Information with the AO</strong>: AO must have information (from risk-based selection, SFT, foreign tax authority exchange, search operations, or specified sources) suggesting income has escaped assessment.</p>"
         "<p><strong>Step 2 - Section 148A(a) Enquiry</strong>: AO may conduct enquiry regarding the information (not mandatory in all cases).</p>"
         "<p><strong>Step 3 - Section 148A(b) Show-cause Notice</strong>: AO issues show-cause notice to the taxpayer with the information + proposed grounds for reopening. Taxpayer gets opportunity to respond.</p>"
         "<p><strong>Step 4 - Section 148A(d) Order</strong>: AO passes order deciding whether to issue Section 148 notice. Order considers taxpayer's response. If AO proceeds, formal Section 148 notice is issued.</p>"
         "<p><strong>Step 5 - Section 148 Formal Notice</strong>: taxpayer must file return within time specified in notice (typically 30 days).</p>"
         "<p><strong>Step 6 - Assessment under Section 147</strong>: regular reassessment proceedings follow (akin to Section 143(3) scrutiny).</p>"),
        ("/ Time limits (Section 149)", "4 years vs 10 years.",
         "<p><strong>Standard limit: 4 years</strong> from the end of the relevant AY. Example: for AY 2021-22, standard reopening possible until 31 March 2026.</p>"
         "<p><strong>Extended limit: 10 years</strong> &mdash; applies only where:</p>"
         "<ul>"
         "<li>AO has evidence (books, documents, bank entries) suggesting income escaping assessment is INR 50 lakh or more.</li>"
         "<li>Income escaping is represented in the form of an ASSET (immovable property, financial asset like shares/MF, bullion, jewellery, foreign asset, etc.).</li>"
         "</ul>"
         "<p>Example: AO finds the taxpayer owns a USD 1M US property not disclosed on prior ITRs. Since escaped income is embodied in asset form and value &gt; INR 50 lakh, 10-year window applies &mdash; AY 2016-17 can still be reopened in AY 2026-27.</p>"),
        ("/ Section 148A(b) response - first critical juncture", "The 7-day window.",
         "<p>Section 148A(b) show-cause gives you an opportunity to argue BEFORE formal Section 148 notice. If you successfully convince the AO that no income has escaped assessment, no Section 148 is issued. If you don't respond or respond weakly, Section 148 follows and you move into full reassessment.</p>"
         "<p><strong>Response window</strong>: typically 7-30 days as specified in the show-cause notice.</p>"
         "<p><strong>Response strategy</strong>:</p>"
         "<ul>"
         "<li>Request the complete 'information' the AO relied on (RTI if needed) &mdash; often third-party reports have classification errors.</li>"
         "<li>If the information is wrong (e.g., SFT misreported, same transaction counted twice, PAN mismatch), submit documentary refutation.</li>"
         "<li>If the information is correct but income was actually declared (just under a different head), produce the ITR extract showing it.</li>"
         "<li>If the income exists but is below taxable threshold or exempt (gift from relative under 56(2)(x), inheritance, capital gain reinvested under Section 54), produce supporting docs.</li>"
         "<li>If limitation period has expired or 10-year carve-out doesn't apply (because escaped income not asset-form or below INR 50L), argue jurisdictional point.</li>"
         "</ul>"
         "<p>Many 148A notices are quashed at this stage with properly drafted response.</p>"),
        ("/ If Section 148 is issued", "Reassessment proceedings.",
         "<p>If AO's Section 148A(d) order proceeds and Section 148 formal notice follows:</p>"
         "<ol>"
         "<li><strong>File return</strong> within time specified (typically 30 days). You can file the same return or revise it based on your position.</li>"
         "<li><strong>Reassessment under Section 147</strong>: AO proceeds like a Section 143(3) scrutiny &mdash; document calls, personal hearing (physical or faceless), additions proposed, order under Section 147.</li>"
         "<li><strong>Time limit for completion</strong>: 12 months from end of FY in which Section 148 notice was served. Extended for complex cases.</li>"
         "<li><strong>Appeal</strong>: Section 147 order appealable to CIT(A) within 30 days.</li>"
         "</ol>"
         "<p><strong>Penalty under Section 270A</strong>: if additional income is confirmed, 50% penalty (under-reporting) or 200% penalty (misreporting) applies.</p>"
         "<p><em>Last updated: 2026-10-12.</em></p>"),
    ],
    faqs=[
        ("What is Section 148A?",
         "Pre-Section-148 show-cause procedure introduced by Finance Act 2021. AO must issue 148A(b) show-cause notice with the 'information' justifying reopening, give taxpayer opportunity to respond, consider response in 148A(d) order, and only then can issue formal 148 notice. Significant procedural protection for taxpayer."),
        ("What is the time limit for Section 148 reopening?",
         "Standard: 4 years from end of relevant AY (e.g., AY 2021-22 reopenable until 31 March 2026). Extended: 10 years where escaped income is INR 50 lakh+ and represented in asset form (immovable property, shares/MF, bullion, jewellery, foreign assets). For AY 2016-17 and later, 10-year extended limit can apply."),
        ("How much time do I have to respond to Section 148A(b)?",
         "7-30 days as specified in the show-cause notice. Request extension if needed within the deadline. The response window is a critical juncture - a well-drafted response can prevent Section 148 formal notice entirely."),
        ("Can Section 148A show-cause be challenged in writ?",
         "Yes - if the 148A procedure is defective (no proper information, no genuine opportunity, mechanical satisfaction, pre-decided outcome), writ in High Court can quash the proceeding. Several High Courts have struck down defective 148A proceedings. Legal strategy matters."),
        ("What is the penalty if Section 148 reassessment confirms additional income?",
         "Section 270A: 50% penalty for under-reporting (good faith); 200% penalty for misreporting (fraud / wilful concealment). Can be avoided if taxpayer makes voluntary disclosure under Section 270AA before the order. The 50% vs 200% classification is a key battle in reassessment."),
        ("Does BQP handle Section 148 / 148A response?",
         "Yes - Section 148A(b) response drafting, information review (RTI if needed), documentary refutation, legal position for jurisdictional challenges, reassessment proceedings if 148 is issued, CIT(A) appeal if 147 order is adverse. Urgent engagement given 7-30 day response windows. WhatsApp +91 78018 87130."),
    ],
    related=[
        ("section-143-2-scrutiny-notice-response-india.html", "Blog", "Section 143(2) Scrutiny"),
        ("section-143-1-intimation-response-india-2026.html", "Blog", "Section 143(1) Intimation"),
    ],
    cta_headline="Section 148A show-cause received? First 7 days decide the proceeding.",
    cta_body="Working-CA urgent engagement: review the AO's 'information', draft refutation / documentary response, argue jurisdictional points where applicable. A well-drafted 148A response often prevents formal Section 148 notice entirely.",
))

# 3. Section 115BAA / 115BAB
write_page("section-115baa-115bab-corporate-tax-regime-india", page(
    slug="section-115baa-115bab-corporate-tax-regime-india",
    title="Section 115BAA & 115BAB Corporate Tax 2026 | 22% + 15% Explained - BQP",
    description="Section 115BAA (22% concessional corporate tax) + Section 115BAB (15% for new manufacturing companies) 2026: eligibility, conditions, forfeited deductions (80-IAC, carry-forward loss), one-time election irrevocability, MAT exemption, comparison with 25% standard rate. Working CA guide by Durgesh Chavda.",
    keywords="Section 115BAA 22% corporate tax India, Section 115BAB 15% new manufacturing, concessional corporate tax regime, Finance Act 2019 corporate tax, Section 115BAA MAT exemption",
    hero_kicker="/ Blog &middot; Section 115BAA / 115BAB &middot; Updated 2026-10-12",
    hero_title_html="Section 115BAA (22%) &amp; 115BAB (15%), <em>when to opt in.</em>",
    hero_lead="Taxation Laws (Amendment) Act 2019 introduced two concessional corporate tax regimes for Indian companies: Section 115BAA (22% + surcharge + cess for any domestic company) and Section 115BAB (15% + surcharge + cess for new manufacturing companies). Choice is one-time and IRREVOCABLE. For most Indian corporate taxpayers in 2026, 115BAA is the default winning choice. For specific manufacturing companies, 115BAB can save 7 percentage points. Here's the practitioner's decision framework.",
    sections=[
        ("/ The three corporate tax regimes", "What applies when.",
         "<p>Three regimes for Indian domestic companies as of FY 2025-26:</p>"
         "<p><strong>1. Standard regime</strong>:</p>"
         "<ul>"
         "<li>Rate: 25% (if turnover up to INR 400 crore in FY preceding by 2) or 30% (above).</li>"
         "<li>Full access to all deductions, carry-forward losses, Section 80 benefits.</li>"
         "<li>MAT applies at 15%.</li>"
         "</ul>"
         "<p><strong>2. Section 115BAA (concessional for any domestic company)</strong>:</p>"
         "<ul>"
         "<li>Rate: <strong>22%</strong> + 10% surcharge + 4% cess = effective ~25.17%.</li>"
         "<li>No MAT applies.</li>"
         "<li>Specific deductions FORFEITED (see below).</li>"
         "<li>One-time election by filing Form 10-IC on or before due date for ITR of the FY of election. Irrevocable.</li>"
         "</ul>"
         "<p><strong>3. Section 115BAB (concessional for NEW manufacturing company)</strong>:</p>"
         "<ul>"
         "<li>Rate: <strong>15%</strong> + 10% surcharge + 4% cess = effective ~17.16%.</li>"
         "<li>No MAT.</li>"
         "<li>Available only for new manufacturing companies incorporated on or after 1 October 2019 and commencing production on or before 31 March 2024 (deadline extended for specific sectors).</li>"
         "<li>Form 10-ID election. Irrevocable.</li>"
         "</ul>"),
        ("/ Section 115BAA conditions + what you lose", "The trade-off.",
         "<p>To opt into Section 115BAA, the company must NOT claim:</p>"
         "<ul>"
         "<li>Section 10AA (SEZ unit deduction).</li>"
         "<li>Section 32(1)(iia) (additional depreciation 20% in year 1).</li>"
         "<li>Section 32AD (investment allowance).</li>"
         "<li>Section 33AB (Tea/Coffee/Rubber Development Account).</li>"
         "<li>Section 33ABA (Site Restoration Fund).</li>"
         "<li>Section 35(1)(ii) / (iia) / (iii) (donations for scientific research).</li>"
         "<li>Section 35(2AA) / (2AB) (approved research deduction).</li>"
         "<li>Section 35AD (investment-linked deduction).</li>"
         "<li>Section 35CCC / 35CCD (agricultural extension / skill dev projects).</li>"
         "<li>Chapter VI-A deductions except Section 80JJAA (new employment) and Section 80M (inter-corporate dividend).</li>"
         "<li><strong>Carry-forward of losses</strong> related to the forfeited deductions.</li>"
         "</ul>"
         "<p>For most companies (that are NOT SEZ-based, not heavy on scientific research, not operating in specified sectors), the forfeited deductions are minimal. Section 115BAA's 22% beats the standard 25%/30% in nearly every case for non-specialist companies.</p>"),
        ("/ Section 115BAB conditions", "New manufacturing only.",
         "<p>Section 115BAB applies only if the company meets ALL conditions:</p>"
         "<ul>"
         "<li>Set up and registered on or after 1 October 2019.</li>"
         "<li>Commences manufacturing or production on or before 31 March 2024 (date extended for specific sectors; verify current state).</li>"
         "<li>Not formed by splitting up or reconstruction of an existing business.</li>"
         "<li>Does not use plant and machinery previously used in India (second-hand &gt; 20% threshold triggers disqualification).</li>"
         "<li>Does not use building previously used as a hotel or convention centre.</li>"
         "<li>Engaged in manufacturing or production of article or thing. NOT engaged in: generating electricity (specific exception), mining, software development (controversial, see 2022 clarifications), book printing, re-labelling / packing.</li>"
         "<li>Same forfeited-deductions list as 115BAA plus more restrictive.</li>"
         "</ul>"
         "<p>Transfer pricing with related parties: any related-party transaction at non-arm's-length pricing can trigger disqualification of 115BAB election.</p>"),
        ("/ Decision framework", "Which regime wins.",
         "<p><strong>For most domestic companies</strong>: Section 115BAA (22%) is the default best choice. The forfeited deductions are not meaningful for most businesses; the 3-8 percentage-point saving vs 25%/30% is real.</p>"
         "<p><strong>Exception - stay on standard regime if</strong>:</p>"
         "<ul>"
         "<li>You have significant SEZ Section 10AA deduction (reduces to zero under 115BAA).</li>"
         "<li>You have large carry-forward losses from prior years that would be forfeited.</li>"
         "<li>You have substantial Section 35 scientific research deductions.</li>"
         "<li>You are a research-driven pharma / biotech company with Section 35(2AB) in-house R&amp;D deduction.</li>"
         "</ul>"
         "<p><strong>Opt into Section 115BAB if</strong>:</p>"
         "<ul>"
         "<li>You are a new manufacturing company (post-Oct-2019 incorporation).</li>"
         "<li>You will commence production by the deadline.</li>"
         "<li>You are confident of meeting all substantive conditions (not reconstruction, no prior plant &amp; machinery, pure manufacturing).</li>"
         "</ul>"
         "<p><strong>Irrevocable election</strong>: once opted into 115BAA or 115BAB, cannot revert to standard regime. Think carefully.</p>"
         "<p><em>Last updated: 2026-10-12.</em></p>"),
    ],
    faqs=[
        ("What is Section 115BAA?",
         "Concessional corporate tax regime for Indian domestic companies: 22% + 10% surcharge + 4% cess = effective ~25.17%. No MAT applies. In exchange, company forfeits specific deductions (SEZ 10AA, additional depreciation, scientific research 35, Chapter VI-A except 80JJAA and 80M) and related-loss carry-forward. One-time irrevocable election via Form 10-IC."),
        ("What is Section 115BAB?",
         "Concessional 15% corporate tax regime for NEW manufacturing companies incorporated on or after 1 October 2019 that commence production by specified deadline. 15% + 10% surcharge + 4% cess = effective ~17.16%. More restrictive than 115BAA - must be pure manufacturing, no reconstruction, no prior plant & machinery. Irrevocable via Form 10-ID."),
        ("Is 22% under Section 115BAA always better than standard 25%?",
         "For most companies, yes. The forfeited deductions under 115BAA are not material for typical operating companies (no SEZ, no heavy R&D, no large carry-forward losses). The 3-8 percentage-point saving on tax is real. Exception: SEZ-based, research-heavy, or loss-carrying companies may prefer standard regime."),
        ("Can I switch from Section 115BAA back to standard regime?",
         "No. Section 115BAA election is irrevocable. Once Form 10-IC is filed for a given FY, the company is permanently in the 22% regime (subject to meeting the ongoing conditions). Same for Section 115BAB (Form 10-ID)."),
        ("Does Section 115BAA company get carry-forward of losses?",
         "Losses attributable to forfeited deductions (SEZ 10AA, additional depreciation, scientific research) are forfeited. Normal business losses continue to be carried forward subject to standard rules. Companies with large forfeited-category losses may be better off on standard regime."),
        ("Does BQP help with 115BAA / 115BAB election?",
         "Yes - decision modelling (compare standard vs 115BAA vs 115BAB with your company's deduction profile and projected income), Form 10-IC / 10-ID filing, ongoing compliance verification. Standard engagement for Indian corporate clients. WhatsApp +91 78018 87130."),
    ],
    related=[
        ("itr-filing-ay-2026-27-deadlines-changes-india.html", "Blog", "ITR AY 2026-27"),
        ("new-vs-old-tax-regime-calculator.html", "Tool", "New vs Old Regime (Individual)"),
    ],
    cta_headline="Private limited company - 22% or 25%? Decision is irrevocable.",
    cta_body="Standard engagement: compare current year + 5-year projection under all three regimes with your actual deduction profile. Form 10-IC election by due date of ITR. Most companies win on Section 115BAA; verify yours.",
))

# 4. Section 56(2)(x) Gift Tax
write_page("section-56-2-x-gift-tax-india-2026", page(
    slug="section-56-2-x-gift-tax-india-2026",
    title="Section 56(2)(x) Gift Tax India 2026 | Threshold, Relatives, Exemptions - BQP",
    description="Section 56(2)(x) gift tax India 2026: INR 50,000 threshold, relative exemption, marriage gift exemption, inheritance exemption, property gift stamp duty value, immovable property vs movable property treatment. Working CA guide by Durgesh Chavda.",
    keywords="Section 56(2)(x) gift tax India 2026, gift from relative tax, INR 50000 gift limit, marriage gift tax, inheritance tax India, property gift stamp duty value tax",
    hero_kicker="/ Blog &middot; Section 56(2)(x) Gift Tax &middot; Updated 2026-10-12",
    hero_title_html="Section 56(2)(x) gift tax, <em>the complete India 2026 framework.</em>",
    hero_lead="India does not have a standalone gift tax or estate duty. Instead, Section 56(2)(x) treats certain receipts without consideration (gifts) as 'Income from Other Sources' in the recipient's hands, taxed at slab rate. INR 50,000 annual threshold. Relatives exempt. Marriage gift exempt. Inheritance exempt. But understanding what qualifies as 'relative' and when stamp-duty value becomes the deemed consideration catches many people out. Here's the practitioner's guide.",
    sections=[
        ("/ Section 56(2)(x) core rule", "The INR 50,000 threshold.",
         "<p>Section 56(2)(x) of the Income Tax Act, inserted by Finance Act 2017, applies to any individual, HUF, firm, LLP, company, or AOP receiving (from any person) in a FY:</p>"
         "<ul>"
         "<li><strong>Any sum of money</strong> exceeding INR 50,000 aggregate in the FY &rarr; the whole amount is taxable as income from other sources at slab rate.</li>"
         "<li><strong>Any immovable property</strong> without consideration + stamp duty value &gt; INR 50,000 &rarr; stamp duty value is taxable.</li>"
         "<li><strong>Any immovable property with inadequate consideration</strong> &mdash; difference between stamp duty value and consideration if difference &gt; INR 50,000 and &gt; 10% of consideration (safe harbour).</li>"
         "<li><strong>Any specified movable property</strong> without consideration + FMV &gt; INR 50,000 &rarr; FMV is taxable.</li>"
         "<li><strong>Any specified movable property with inadequate consideration</strong> &mdash; difference between FMV and consideration if difference &gt; INR 50,000.</li>"
         "</ul>"
         "<p><strong>Specified movable property</strong>: shares + securities, jewellery, archaeological collections, drawings, paintings, sculptures, any work of art, bullion. Other movable property (e.g., car, laptop, watch) is generally NOT covered by 56(2)(x) &mdash; outside gift tax scope.</p>"
         "<p><strong>Threshold mechanism</strong>: INR 50,000 is per FY aggregate per taxpayer across all gift receipts. The whole amount above INR 50,000 is taxable, not just the excess (slight nuance in how it's computed).</p>"),
        ("/ Who is a 'relative' under Section 56(2)(x)", "The exempt list.",
         "<p>Gifts from <strong>relatives</strong> are fully exempt regardless of amount. The exhaustive list under Explanation to Section 56(2)(x):</p>"
         "<p>For an individual:</p>"
         "<ul>"
         "<li>Spouse.</li>"
         "<li>Brother or sister (of the individual).</li>"
         "<li>Brother or sister of the spouse of the individual.</li>"
         "<li>Brother or sister of either of the parents of the individual.</li>"
         "<li>Any lineal ascendant or descendant of the individual (parents, grandparents, children, grandchildren).</li>"
         "<li>Any lineal ascendant or descendant of the spouse (parents-in-law, children's spouses as lineal descendant's spouses).</li>"
         "<li>Spouse of any of the above persons.</li>"
         "</ul>"
         "<p>For HUF: any member of the HUF.</p>"
         "<p><strong>NOT relatives</strong> (gifts from these ARE taxable above INR 50,000):</p>"
         "<ul>"
         "<li>Friend.</li>"
         "<li>Uncle's or aunt's spouse (if the uncle/aunt is not blood-related).</li>"
         "<li>Cousin.</li>"
         "<li>Niece, nephew (unless lineal descendant via another route).</li>"
         "<li>Employer (except specific perquisite rules).</li>"
         "</ul>"),
        ("/ Specific exempt situations", "Beyond relatives.",
         "<p>Section 56(2)(x) does NOT apply (fully exempt) in these additional scenarios:</p>"
         "<ul>"
         "<li><strong>Gift on occasion of marriage</strong> of the individual &mdash; any gift (any amount) from anyone, exempt. Specific to the individual getting married, not for parents / siblings.</li>"
         "<li><strong>Gift under a will or inheritance</strong>.</li>"
         "<li><strong>Gift in contemplation of death</strong> of the payer.</li>"
         "<li><strong>Gift from any local authority (as defined in Explanation to Section 10(20))</strong>.</li>"
         "<li><strong>Gift from any registered trust / institution</strong> approved under Section 10(23C) or 12AA / 12AB.</li>"
         "<li><strong>Gift from any trust or institution</strong> on behalf of government or local authority.</li>"
         "<li><strong>Transactions not treated as transfer under Section 47</strong>.</li>"
         "<li><strong>Specific transactions on amalgamation / demerger / resulting company reorganisations</strong>.</li>"
         "</ul>"),
        ("/ Property gift mechanics", "Stamp duty value trap.",
         "<p><strong>Immovable property gift from non-relative</strong>:</p>"
         "<ul>"
         "<li>Full stamp duty value is taxed in recipient's hands (at slab rate) if value &gt; INR 50,000.</li>"
         "<li>Not the actual cash paid &mdash; the stamp duty value.</li>"
         "<li>Example: father's friend 'sells' recipient a property for INR 10 lakh when stamp duty value is INR 50 lakh. INR 40 lakh is taxed in recipient's hands under 56(2)(x) (because consideration inadequate by &gt;10% + &gt; INR 50,000).</li>"
         "</ul>"
         "<p><strong>Immovable property gift from relative</strong>: exempt under 56(2)(x). But for GST / stamp duty, actual stamp duty on gift deed still applies to the recipient.</p>"
         "<p><strong>Shares gift from non-relative</strong>:</p>"
         "<ul>"
         "<li>FMV of shares at receipt is taxed in recipient's hands at slab rate.</li>"
         "<li>FMV determined by Rule 11UA (NAV method for unlisted; closing price for listed).</li>"
         "<li>Example: friend gifts you shares of your Indian startup worth INR 5 lakh. Recipient pays slab tax on INR 5 lakh.</li>"
         "</ul>"
         "<p><strong>Shares gift from relative</strong>: exempt. Cost of acquisition for subsequent capital gains = original cost in donor's hands (Section 49(1)).</p>"
         "<p><em>Last updated: 2026-10-12.</em></p>"),
    ],
    faqs=[
        ("Does India have gift tax?",
         "Not as a standalone tax. Section 56(2)(x) of the Income Tax Act treats certain gifts above INR 50,000 as 'Income from Other Sources' in the recipient's hands, taxed at slab rate. Gifts from relatives, inheritance, marriage gifts to the individual getting married, and specific other categories are exempt."),
        ("Is a gift from parents taxable in India?",
         "No. Parents are 'relatives' under Explanation to Section 56(2)(x). Gift from parent to child (and vice versa) is fully exempt, any amount. Same for gifts from siblings, spouse, grandparents, lineal ascendants/descendants, and spouse's relatives in the specified list."),
        ("Is cash gift above INR 50,000 from a friend taxable?",
         "Yes - friend is NOT a 'relative' under Section 56(2)(x). Cash gift from friend above INR 50,000 aggregate in a FY is fully taxable in recipient's hands at slab rate as 'Income from Other Sources'. Even multiple small gifts totaling above INR 50,000 in a FY become taxable."),
        ("Are marriage gifts taxable?",
         "Gifts received by the individual on the occasion of his / her OWN marriage are fully exempt - any amount, from anyone. However: gifts to parents of bride/groom, gifts received at a sibling's wedding, gifts received post-marriage date all fall back under standard Section 56(2)(x) rules (INR 50,000 threshold + relative exemption)."),
        ("Is inheritance taxable in India?",
         "No. Section 56(2)(x) specifically exempts gifts received under will or by way of inheritance. India has no estate duty or inheritance tax. However: income earned from inherited assets after inheritance (e.g., rent, interest, capital gains on sale) is taxable in the inheritor's hands under normal provisions."),
        ("Does BQP help with gift tax planning?",
         "Yes - gift documentation (gift deed drafting), relative-exemption verification, stamp-duty-value vs consideration analysis for property gifts, share-gift tax planning, subsequent-year ITR disclosure, cost-of-acquisition tracking for subsequent capital gains. WhatsApp +91 78018 87130."),
    ],
    related=[
        ("ltcg-12-5-percent-new-capital-gains-india-2026.html", "Blog", "LTCG 12.5% Rule"),
        ("itr-filing-ay-2026-27-deadlines-changes-india.html", "Blog", "ITR AY 2026-27"),
    ],
    cta_headline="Receiving a large gift / property transfer? Verify Section 56(2)(x) first.",
    cta_body="Working-CA engagement: verify relative status, draft compliant gift deed, model Section 56(2)(x) tax if non-relative, co-ordinate with stamp-duty value for property gifts. Avoid future notice via proper documentation now.",
))

# 5. DIR-3 KYC + Director Compliance
write_page("dir-3-kyc-director-annual-compliance-india", page(
    slug="dir-3-kyc-director-annual-compliance-india",
    title="DIR-3 KYC + Director Annual Compliance 2026 | DIN Deactivation Fix - BQP",
    description="DIR-3 KYC annual filing for all DIN holders: 30 September deadline, INR 5,000 late fee, DIN deactivation consequences, how to reactivate deactivated DIN, DIR-3 KYC Web vs eForm. Director compliance calendar. Working CA guide by Durgesh Chavda.",
    keywords="DIR-3 KYC annual filing, DIN deactivation fix, DIR-3 KYC due date 2026, how to reactivate DIN, director annual compliance India",
    hero_kicker="/ Blog &middot; DIR-3 KYC &middot; Updated 2026-10-12",
    hero_title_html="DIR-3 KYC, <em>annual filing every director forgets.</em>",
    hero_lead="Every individual holding a Director Identification Number (DIN) in India must file DIR-3 KYC annually by 30 September. Missing it costs INR 5,000 late fee AND deactivates the DIN &mdash; which blocks MCA filings, ROC compliance, board resolutions, bank KYC, and most corporate actions. The filing takes 10 minutes. Here's the complete practitioner's guide.",
    sections=[
        ("/ Who must file DIR-3 KYC", "The scope.",
         "<p>Every individual who was allotted a DIN on or before 31 March of a given financial year must file DIR-3 KYC on or before <strong>30 September</strong> of the immediately next financial year.</p>"
         "<p>Scope:</p>"
         "<ul>"
         "<li>Active directors of Indian companies.</li>"
         "<li>Resigned directors (if the DIN is still active &mdash; which it usually is).</li>"
         "<li>Prospective directors who obtained DIN for a company that was never incorporated.</li>"
         "<li>Directors of LLPs (DPIN merged with DIN under MCA framework).</li>"
         "</ul>"
         "<p>If you ever obtained a DIN and haven't surrendered it, you must file DIR-3 KYC every year.</p>"
         "<p>Non-filing consequence: DIN is marked 'Deactivated due to non-filing of DIR-3 KYC'. Status visible on MCA portal.</p>"),
        ("/ Two filing routes", "DIR-3 KYC Web vs eForm.",
         "<p><strong>DIR-3 KYC (Web-based)</strong>:</p>"
         "<ul>"
         "<li>Available if the director has filed DIR-3 KYC in any previous year with no changes to KYC details (name, DOB, nationality, email, mobile, address, PAN, Aadhaar).</li>"
         "<li>Login to MCA v3 portal with DSC or MCA credentials.</li>"
         "<li>Navigate to DIR-3 KYC Web.</li>"
         "<li>Verify OTP sent to registered email + mobile.</li>"
         "<li>Submit. Filing completes.</li>"
         "<li>No fee if filed within 30 September deadline.</li>"
         "</ul>"
         "<p><strong>DIR-3 KYC (eForm)</strong>:</p>"
         "<ul>"
         "<li>Required for first-time filers (filing DIR-3 KYC for the first time ever).</li>"
         "<li>Required if any KYC detail (name, DOB, nationality, email, mobile, address, PAN, Aadhaar) has changed from last filing.</li>"
         "<li>Download eForm, attach supporting documents (PAN, Aadhaar, address proof), self-attest, apply DSC.</li>"
         "<li>Upload and submit via MCA portal.</li>"
         "<li>Processing: 24-48 hours typically.</li>"
         "</ul>"),
        ("/ Deactivated DIN - how to reactivate", "The INR 5,000 fix.",
         "<p>If DIR-3 KYC not filed by 30 September deadline:</p>"
         "<ol>"
         "<li>DIN marked 'Deactivated due to non-filing of DIR-3 KYC'.</li>"
         "<li>File DIR-3 KYC (Web or eForm as applicable) with <strong>INR 5,000 late fee</strong> paid via MCA portal.</li>"
         "<li>DIN reactivated within 24-72 hours after filing processed.</li>"
         "</ol>"
         "<p><strong>What breaks while DIN is deactivated</strong>:</p>"
         "<ul>"
         "<li>Cannot file any MCA eForm with your DIN (AOC-4, MGT-7, DIR-12, PAS-6, etc.).</li>"
         "<li>Cannot sign board resolutions as per MCA records (though board decisions internally still valid).</li>"
         "<li>Cannot incorporate new companies as a director.</li>"
         "<li>Bank KYC / enhanced due diligence may flag the deactivation.</li>"
         "<li>GST director KYC refresh may fail (depends on state).</li>"
         "</ul>"
         "<p>Materially the DIN deactivation blocks you from signing any ROC filing. For a director with multiple directorships, this is a serious operational problem.</p>"),
        ("/ Related director compliance", "The full annual calendar.",
         "<p>Director-level annual compliance beyond DIR-3 KYC:</p>"
         "<ul>"
         "<li><strong>Disclosure of Interest (MBP-1)</strong>: every director must disclose directorship / shareholding / interest in other entities at the first board meeting of each FY. Filed internally.</li>"
         "<li><strong>DIR-8</strong>: declaration by director that they are not disqualified under Section 164. First board meeting of each FY.</li>"
         "<li><strong>Form DIR-11</strong>: resignation intimation by director to ROC within 30 days of resignation.</li>"
         "<li><strong>Form DIR-12</strong>: company intimation to ROC of director appointment / resignation / change within 30 days.</li>"
         "<li><strong>Form MR-1</strong>: appointment of managerial personnel (MD, WTD, Manager) within 60 days.</li>"
         "<li><strong>DPT-3</strong>: company's annual return of deposits (90 days from FY-end).</li>"
         "<li><strong>MSME Form 1</strong>: half-yearly return of outstanding dues to MSME suppliers (over 45 days).</li>"
         "<li><strong>Form AOC-4 (financial statements)</strong>: within 30 days of AGM.</li>"
         "<li><strong>Form MGT-7 (annual return)</strong>: within 60 days of AGM.</li>"
         "<li><strong>Form PAS-6 (demat reconciliation)</strong>: within 60 days of each half-year end (for Rule 9B companies).</li>"
         "</ul>"
         "<p>For companies with foreign shareholders / subsidiaries: additional FEMA + FLA Return + Form FC-GPR / FC-TRS compliance.</p>"
         "<p><em>Last updated: 2026-10-12.</em></p>"),
    ],
    faqs=[
        ("What is DIR-3 KYC?",
         "Annual KYC filing for every individual holding a Director Identification Number (DIN). Due by 30 September each year for DINs allotted on or before 31 March of the preceding FY. Filed via MCA v3 portal as DIR-3 KYC Web (returning filers with no KYC changes) or DIR-3 KYC eForm (first-time filers or those with KYC changes)."),
        ("What happens if I miss the DIR-3 KYC deadline?",
         "DIN is marked 'Deactivated due to non-filing of DIR-3 KYC'. Blocks all MCA eForm filings with that DIN. Fix: file DIR-3 KYC with INR 5,000 late fee via MCA portal. DIN reactivated within 24-72 hours after filing processed. The INR 5,000 fee is standard; no multiplier for extended delays."),
        ("Do I need to file DIR-3 KYC if I resigned as director?",
         "Yes if your DIN is still active. Resignation from a company does not deactivate your DIN - the DIN remains in your name until you surrender it via Form DIR-5. If you have no plan to be director again, you can surrender DIN. If uncertain or planning future directorship, maintain DIR-3 KYC annually to keep DIN active."),
        ("Can I file DIR-3 KYC Web every year?",
         "Yes if your KYC details (name, DOB, nationality, email, mobile, address, PAN, Aadhaar) are unchanged from last filing. First-time filers must use DIR-3 KYC eForm. Any change in any KYC field in subsequent year also requires eForm."),
        ("What is DPIN and how does it relate to DIN?",
         "DPIN (Designated Partner Identification Number) was for LLP designated partners. Since July 2017, DPIN and DIN have been merged - LLP designated partners use DIN. Any individual (whether director of company or designated partner of LLP) uses one unified DIN. DIR-3 KYC applies equally to LLP designated partners."),
        ("Does BQP handle DIR-3 KYC and director compliance?",
         "Yes - annual DIR-3 KYC filing for all your directorships (even if you have multiple), MBP-1 + DIR-8 preparation, DIR-11 and DIR-12 filings for resignations / appointments, DPT-3 + MSME Form 1 + PAS-6 + AOC-4 + MGT-7 full ROC compliance calendar. Standard annual director + company compliance package. WhatsApp +91 78018 87130."),
    ],
    related=[
        ("itr-filing-ay-2026-27-deadlines-changes-india.html", "Blog", "ITR AY 2026-27"),
        ("dematerialisation-unlisted-shares-india-mandatory.html", "Blog", "Demat of Unlisted Shares"),
    ],
    cta_headline="DIN deactivated or heading toward deactivation?",
    cta_body="File DIR-3 KYC + INR 5,000 late fee + 24-72 hour reactivation. For directors with multiple directorships + full ROC compliance calendar, BQP annual engagement covers everything &mdash; one firm, no surprises.",
))

# 6. Section 194Q TDS Purchase of Goods
write_page("section-194q-tds-purchase-goods-india", page(
    slug="section-194q-tds-purchase-goods-india",
    title="Section 194Q TDS on Purchase of Goods 2026 | 0.1% + Threshold - BQP",
    description="Section 194Q TDS 0.1% on purchase of goods above INR 50 lakh from a seller in FY: buyer threshold INR 10 crore turnover, interaction with Section 206C(1H) seller TCS, PAN non-availability 5% rate, computation mechanics. Working CA guide by Durgesh Chavda.",
    keywords="Section 194Q TDS purchase goods, 194Q 0.1% TDS buyer, Section 194Q threshold INR 50 lakh, 194Q 206C(1H) overlap, Finance Act 2021 Section 194Q",
    hero_kicker="/ Blog &middot; Section 194Q TDS &middot; Updated 2026-10-12",
    hero_title_html="Section 194Q, <em>buyer-side TDS on goods purchase.</em>",
    hero_lead="Finance Act 2021 introduced Section 194Q effective 1 July 2021: a buyer with annual turnover above INR 10 crore in the preceding FY must deduct 0.1% TDS on purchase of goods from a seller where aggregate purchases exceed INR 50 lakh in the FY. The compliance workload is real, especially given overlap with seller-side Section 206C(1H) TCS. Here's the practitioner's map.",
    sections=[
        ("/ Section 194Q core rule", "Buyer-side TDS.",
         "<p>Section 194Q applies when:</p>"
         "<ul>"
         "<li><strong>Buyer</strong> &mdash; any person (individual, HUF, firm, LLP, company, trust) whose aggregate turnover / receipts / sales in the <strong>immediately preceding FY</strong> exceeded <strong>INR 10 crore</strong>.</li>"
         "<li><strong>Seller</strong> &mdash; resident Indian seller of goods.</li>"
         "<li><strong>Purchase threshold</strong> &mdash; aggregate purchases from that seller in the current FY exceed <strong>INR 50 lakh</strong>.</li>"
         "<li>TDS deducted at <strong>0.1%</strong> of the amount in excess of INR 50 lakh.</li>"
         "</ul>"
         "<p><strong>Timing of deduction</strong>: at the time of credit of the amount to the seller's account OR at payment, whichever is earlier.</p>"
         "<p><strong>PAN non-availability</strong>: if seller does not provide PAN, Section 206AA kicks in &mdash; rate becomes 5% (or applicable rate, whichever higher).</p>"
         "<p><strong>Exempt transactions</strong>: purchase from government entity (Central Govt, State Govt, local authority), import of goods from outside India (buyer-side TDS on import not applicable; separate customs regime), transaction already subject to seller-side TCS under Section 206C(1H).</p>"),
        ("/ The 194Q vs 206C(1H) overlap", "Who deducts what.",
         "<p>Finance Act 2021 added Section 194Q (buyer TDS) alongside existing Section 206C(1H) (seller TCS). Both apply to the same transaction &mdash; sale of goods. Rule: <strong>Section 194Q takes precedence</strong> where both would apply.</p>"
         "<p>Overlap rules:</p>"
         "<ul>"
         "<li>Buyer turnover &gt; INR 10 crore AND Seller turnover &gt; INR 10 crore AND purchases from seller &gt; INR 50 lakh: <strong>Section 194Q applies</strong> (buyer deducts); Section 206C(1H) is not deducted by seller.</li>"
         "<li>Buyer turnover &gt; INR 10 crore but Seller turnover &lt; INR 10 crore: Section 194Q applies; buyer deducts.</li>"
         "<li>Buyer turnover &lt; INR 10 crore but Seller turnover &gt; INR 10 crore AND sales to this buyer &gt; INR 50 lakh: <strong>Section 206C(1H) applies</strong>; seller deducts (collects as TCS).</li>"
         "<li>Both buyer and seller turnover &lt; INR 10 crore: neither 194Q nor 206C(1H) applies.</li>"
         "</ul>"
         "<p>Practical consequence: buyers should proactively tell sellers 'we deduct 194Q, do not collect 206C(1H) TCS'. Written declaration helps prevent duplicate deduction / collection.</p>"),
        ("/ Compliance workflow", "The quarterly rhythm.",
         "<ol>"
         "<li><strong>Confirm buyer eligibility</strong>: turnover for immediately preceding FY exceeds INR 10 crore? If yes, you are 194Q liable.</li>"
         "<li><strong>Identify sellers with &gt; INR 50 lakh purchases in current FY</strong>: review purchase register. Track cumulative purchases per seller.</li>"
         "<li><strong>Request PAN from sellers</strong>: without PAN, rate jumps to 5% under Section 206AA.</li>"
         "<li><strong>Confirm no Section 206C(1H) TCS applied</strong> by seller on your purchases. If seller has already applied TCS, you cannot also deduct 194Q TDS &mdash; coordinate.</li>"
         "<li><strong>Deduct 0.1% at the first invoice that crosses INR 50 lakh cumulative</strong>, and continue on all subsequent purchases in that FY.</li>"
         "<li><strong>Deposit TDS</strong> by 7th of the following month (last month: 30 April).</li>"
         "<li><strong>File Form 26Q</strong> quarterly (Q1 by 31 July, Q2 by 31 October, Q3 by 31 January, Q4 by 31 May).</li>"
         "<li><strong>Issue Form 16A</strong> to seller within quarterly timeline.</li>"
         "</ol>"),
        ("/ Common 194Q compliance mistakes", "Where buyers trip.",
         "<ul>"
         "<li><strong>Missing seller PAN</strong>: 0.1% becomes 5% under Section 206AA. On INR 1 crore invoice, that's INR 5 lakh vs INR 1,000. Chase PAN before invoice crosses threshold.</li>"
         "<li><strong>Double deduction / collection</strong>: seller collecting 206C(1H) TCS while buyer also deducting 194Q TDS. Overlap resolution: 194Q takes precedence; seller should not collect 206C(1H) when buyer deducts 194Q. Written communication prevents this.</li>"
         "<li><strong>Missing the INR 50 lakh threshold tracking</strong>: 194Q applies on amount above INR 50 lakh per seller per FY. Cumulative tracking essential; missing the threshold boundary means under-deduction + Section 201 interest.</li>"
         "<li><strong>Not filing Form 26Q quarterly</strong>: late filing fee under Section 234E at INR 200 per day. Section 271H penalty for non-filing or incorrect filing.</li>"
         "<li><strong>Not issuing Form 16A to seller</strong>: seller cannot claim TDS credit on their ITR without it. Vendor relationships suffer.</li>"
         "<li><strong>194Q on exempt transactions</strong>: deducting on import purchases (customs regime applies, not 194Q), government supplier (exempt), or where seller is government. Over-deduction wastes TDS pool and creates reconciliation headaches.</li>"
         "</ul>"
         "<p><em>Last updated: 2026-10-12.</em></p>"),
    ],
    faqs=[
        ("What is Section 194Q?",
         "Buyer-side TDS introduced by Finance Act 2021 (effective 1 July 2021). Any buyer with aggregate turnover above INR 10 crore in the preceding FY must deduct 0.1% TDS on purchases from a seller where cumulative purchases exceed INR 50 lakh in the current FY. TDS on the amount above INR 50 lakh."),
        ("How does Section 194Q interact with Section 206C(1H)?",
         "Both apply to the same sale-of-goods transaction. Rule: Section 194Q takes precedence. If buyer is 194Q-liable (turnover > INR 10 crore + cumulative purchases > INR 50 lakh), buyer deducts 194Q and seller does NOT collect 206C(1H) TCS. If buyer not 194Q-liable but seller is 206C(1H)-liable, seller collects TCS."),
        ("What is the rate if seller doesn't provide PAN under Section 194Q?",
         "Rate jumps from 0.1% to 5% under Section 206AA. On a large invoice this is punitive. Always collect seller PAN before purchases cross the INR 50 lakh threshold. Written PAN declaration from seller is sufficient documentation."),
        ("Is import of goods subject to Section 194Q?",
         "No - Section 194Q applies only to purchases from resident Indian sellers. Imports are governed by customs regime; buyer-side TDS on import is not applicable. For import payments, Section 195 (TDS on payments to non-residents) may apply depending on nature of payment, not Section 194Q."),
        ("When is Section 194Q TDS deposited and filed?",
         "Deposited by 7th of the following month (last month: 30 April). Filed quarterly in Form 26Q (Q1 by 31 July, Q2 by 31 October, Q3 by 31 January, Q4 by 31 May). Form 16A issued to seller within quarterly timeline for seller to claim credit on their ITR."),
        ("Does BQP handle Section 194Q compliance?",
         "Yes - 194Q applicability analysis, seller PAN collection + verification, cumulative purchase tracking per seller, TDS deduction + deposit, Form 26Q quarterly filing, Form 16A issuance, co-ordination with Section 206C(1H) overlap. Standard quarterly compliance for mid-size and large Indian companies. WhatsApp +91 78018 87130."),
    ],
    related=[
        ("section-194r-tds-business-perquisites-india.html", "Blog", "Section 194R"),
        ("section-194t-tds-partnership-firm-partners-india.html", "Blog", "Section 194T"),
    ],
    cta_headline="Company turnover > INR 10 crore? Section 194Q applies to your purchases.",
    cta_body="Quarterly compliance: cumulative tracking per seller, deduction + deposit + Form 26Q + Form 16A. For mid-size and large Indian companies BQP runs this as standard annual engagement under one firm.",
))

# 7. Section 206C(1H) TCS Sale of Goods
write_page("section-206c-1h-tcs-sale-goods-india", page(
    slug="section-206c-1h-tcs-sale-goods-india",
    title="Section 206C(1H) TCS on Sale of Goods 2026 | 0.1% + Threshold - BQP",
    description="Section 206C(1H) TCS 0.1% on sale of goods above INR 50 lakh to a buyer in FY: seller threshold INR 10 crore turnover, interaction with Section 194Q buyer TDS, PAN non-availability 1% rate, exempt transactions. Working CA guide by Durgesh Chavda.",
    keywords="Section 206C(1H) TCS sale goods, 206C(1H) 0.1% TCS seller, Section 206C(1H) threshold INR 50 lakh, 194Q 206C(1H) overlap, Finance Act 2020 TCS",
    hero_kicker="/ Blog &middot; Section 206C(1H) TCS &middot; Updated 2026-10-12",
    hero_title_html="Section 206C(1H), <em>seller-side TCS on goods.</em>",
    hero_lead="Finance Act 2020 introduced Section 206C(1H) effective 1 October 2020: a seller with annual turnover above INR 10 crore in the preceding FY must collect 0.1% TCS on sale of goods to a buyer where aggregate sales exceed INR 50 lakh in the FY. In 2021, Section 194Q (buyer TDS) was introduced on the same transactions &mdash; the overlap rules are precise. Here's the full practitioner's guide.",
    sections=[
        ("/ Section 206C(1H) core rule", "Seller-side TCS.",
         "<p>Section 206C(1H) applies when:</p>"
         "<ul>"
         "<li><strong>Seller</strong> &mdash; any person whose aggregate turnover / receipts / sales in the <strong>immediately preceding FY</strong> exceeded <strong>INR 10 crore</strong>.</li>"
         "<li><strong>Buyer</strong> &mdash; any Indian resident buyer of goods.</li>"
         "<li><strong>Sales threshold</strong> &mdash; aggregate sales to that buyer in the current FY exceed <strong>INR 50 lakh</strong>.</li>"
         "<li>TCS collected at <strong>0.1%</strong> of the amount in excess of INR 50 lakh.</li>"
         "</ul>"
         "<p><strong>Timing of collection</strong>: at the time of receipt of the amount from the buyer.</p>"
         "<p><strong>PAN non-availability</strong>: if buyer does not provide PAN, Section 206CC kicks in &mdash; rate becomes 1% (not 5% unlike 194Q, note the asymmetry).</p>"
         "<p><strong>Exempt transactions</strong>: export of goods (outside India), sale to government, sale subject to TCS under other 206C sub-sections (e.g., 206C(1) on alcoholic liquor / scrap / minerals), sale where buyer deducts 194Q TDS (overlap rule).</p>"),
        ("/ Section 194Q vs 206C(1H) overlap", "Who collects / deducts.",
         "<p>Both sections cover the same transaction type (sale of goods). Both have INR 10 crore turnover thresholds and INR 50 lakh transaction thresholds. Both have 0.1% rate.</p>"
         "<p><strong>Rule: Section 194Q (buyer TDS) takes precedence</strong>. If both would apply, buyer deducts 194Q and seller does NOT collect 206C(1H).</p>"
         "<p>Combinations:</p>"
         "<table style='width:100%;border-collapse:collapse;margin:12px 0;font:400 13px Inter'>"
         "<tr style='background:#f8f3e8'><th style='padding:8px;border:1px solid #ece4d5;text-align:left'>Buyer</th><th style='padding:8px;border:1px solid #ece4d5;text-align:left'>Seller</th><th style='padding:8px;border:1px solid #ece4d5;text-align:left'>Who acts</th></tr>"
         "<tr><td style='padding:8px;border:1px solid #ece4d5'>Turnover &gt; 10 cr</td><td style='padding:8px;border:1px solid #ece4d5'>Turnover &gt; 10 cr</td><td style='padding:8px;border:1px solid #ece4d5'><strong>Buyer deducts 194Q</strong>. Seller does not collect 206C(1H).</td></tr>"
         "<tr><td style='padding:8px;border:1px solid #ece4d5'>Turnover &gt; 10 cr</td><td style='padding:8px;border:1px solid #ece4d5'>Turnover &lt; 10 cr</td><td style='padding:8px;border:1px solid #ece4d5'>Buyer deducts 194Q. 206C(1H) does not apply.</td></tr>"
         "<tr><td style='padding:8px;border:1px solid #ece4d5'>Turnover &lt; 10 cr</td><td style='padding:8px;border:1px solid #ece4d5'>Turnover &gt; 10 cr</td><td style='padding:8px;border:1px solid #ece4d5'><strong>Seller collects 206C(1H)</strong>. 194Q does not apply.</td></tr>"
         "<tr><td style='padding:8px;border:1px solid #ece4d5'>Turnover &lt; 10 cr</td><td style='padding:8px;border:1px solid #ece4d5'>Turnover &lt; 10 cr</td><td style='padding:8px;border:1px solid #ece4d5'>Neither applies.</td></tr>"
         "</table>"
         "<p>Written communication between buyer and seller at start of FY: 'We will deduct 194Q under Finance Act 2021' or 'We will collect 206C(1H)' prevents duplicate deduction + collection.</p>"),
        ("/ Compliance workflow for sellers", "Quarterly cycle.",
         "<ol>"
         "<li><strong>Confirm seller eligibility</strong>: preceding FY turnover &gt; INR 10 crore &rarr; 206C(1H) applicable.</li>"
         "<li><strong>Identify buyers with &gt; INR 50 lakh purchases from you</strong>: review sales register, track cumulative per buyer.</li>"
         "<li><strong>Request buyer PAN</strong>: without PAN, rate is 1% under Section 206CC.</li>"
         "<li><strong>Determine 194Q override</strong>: is the buyer 194Q-liable? Request written confirmation of buyer's turnover &gt; INR 10 crore. If yes, buyer deducts 194Q; you do NOT collect 206C(1H).</li>"
         "<li><strong>Collect 0.1% TCS at receipt</strong> on amounts above INR 50 lakh cumulative per buyer in FY.</li>"
         "<li><strong>Deposit TCS</strong> by 7th of the following month.</li>"
         "<li><strong>File Form 27EQ</strong> quarterly (Q1 by 15 July, Q2 by 15 October, Q3 by 15 January, Q4 by 15 May).</li>"
         "<li><strong>Issue Form 27D</strong> to buyer within quarterly timeline. Buyer claims TCS credit on their ITR.</li>"
         "</ol>"),
        ("/ Common 206C(1H) compliance mistakes", "Where sellers trip.",
         "<ul>"
         "<li><strong>Double collection + deduction</strong>: not confirming buyer's 194Q applicability. Buyer deducts 194Q and seller also collects 206C(1H). Buyer refund requires manual process.</li>"
         "<li><strong>No PAN from buyer</strong>: rate jumps from 0.1% to 1% under Section 206CC.</li>"
         "<li><strong>Missing cumulative tracking</strong>: INR 50 lakh is cumulative per buyer per FY. Partial-year tracking causes under-collection.</li>"
         "<li><strong>206C(1H) on exempt transactions</strong>: collecting on exports (exempt), government sales (exempt), or sales already under 206C(1) sub-sections (alcoholic liquor / scrap / minerals have specific TCS). Over-collection.</li>"
         "<li><strong>Timing error</strong>: 206C(1H) collection is at RECEIPT, not at invoice. If payment is deferred, TCS not collected till payment is received.</li>"
         "<li><strong>Not issuing Form 27D</strong>: buyer cannot claim TCS credit; relationship suffers; buyer may push back on TCS collection.</li>"
         "<li><strong>Not filing Form 27EQ quarterly</strong>: late-filing fee Section 234E at INR 200 per day; Section 271H penalty.</li>"
         "</ul>"
         "<p><em>Last updated: 2026-10-12.</em></p>"),
    ],
    faqs=[
        ("What is Section 206C(1H)?",
         "Seller-side TCS on sale of goods, introduced by Finance Act 2020 (effective 1 October 2020). Sellers with turnover above INR 10 crore in preceding FY must collect 0.1% TCS from buyer on sales above INR 50 lakh cumulative in current FY. TCS on amount above INR 50 lakh. Collected at time of receipt from buyer."),
        ("How does 206C(1H) interact with 194Q?",
         "Both apply to the same sale-of-goods transaction. Rule: Section 194Q (buyer TDS) takes precedence. If buyer is 194Q-liable (turnover > INR 10 crore + cumulative purchases from you > INR 50 lakh), buyer deducts 194Q and seller does NOT collect 206C(1H). Request written confirmation from buyer of their turnover tier."),
        ("Is export of goods subject to Section 206C(1H)?",
         "No - export is exempt from 206C(1H). Export is treated as outside India sale; TCS does not apply. Only domestic sale (buyer is Indian resident) triggers 206C(1H). For exports, standard GST export mechanics (LUT bond, zero-rated) apply."),
        ("What is the rate if buyer doesn't provide PAN?",
         "Rate increases from 0.1% to 1% under Section 206CC (note: higher than 194Q's PAN-absent rate of 5%). Still request buyer PAN before sales cross the INR 50 lakh threshold - written PAN declaration from buyer is sufficient."),
        ("When is 206C(1H) TCS collected - at invoice or at receipt?",
         "At RECEIPT. Unlike 194Q (which is at credit OR payment, whichever earlier), 206C(1H) is specifically at receipt. If buyer pays only part of the invoice, TCS applies on the amount received above INR 50 lakh. Full-invoice TCS collection at invoice stage is NOT correct."),
        ("Does BQP handle Section 206C(1H) compliance?",
         "Yes - 206C(1H) applicability check, buyer PAN collection, 194Q vs 206C(1H) overlap analysis per buyer, written buyer declarations, TCS collection + deposit, Form 27EQ quarterly filing, Form 27D issuance. Co-ordinated with buyer-side 194Q where you also act as buyer in other transactions. WhatsApp +91 78018 87130."),
    ],
    related=[
        ("section-194q-tds-purchase-goods-india.html", "Blog", "Section 194Q (Buyer TDS)"),
        ("tcs-20-foreign-remittance-lrs-india-2026.html", "Blog", "TCS on LRS"),
    ],
    cta_headline="Seller with turnover > INR 10 crore? Section 206C(1H) tracks every buyer.",
    cta_body="Quarterly compliance: 194Q overlap analysis per buyer, cumulative sales tracking, Form 27EQ filing, Form 27D issuance. BQP annual engagement scopes the full TDS + TCS compliance stack for mid-size and large sellers.",
))

# 8. GSTR-9 / GSTR-9C
write_page("gstr-9-gstr-9c-annual-return-india-2026", page(
    slug="gstr-9-gstr-9c-annual-return-india-2026",
    title="GSTR-9 & GSTR-9C Annual Return 2026 | Threshold, Due Date, Reconciliation - BQP",
    description="GSTR-9 annual return + GSTR-9C reconciliation statement for FY 2025-26: INR 2 crore threshold for GSTR-9, INR 5 crore for GSTR-9C, 31 December deadline, late fee INR 200/day, reconciliation with books, common mismatches. Working CA guide by Durgesh Chavda.",
    keywords="GSTR-9 annual return 2026, GSTR-9C reconciliation statement, GSTR-9 due date 2026, GSTR-9 vs GSTR-9C, GSTR-9 late fee, GSTR-9 threshold INR 2 crore",
    hero_kicker="/ Blog &middot; GSTR-9 / GSTR-9C &middot; Updated 2026-10-12",
    hero_title_html="GSTR-9 and GSTR-9C, <em>annual GST reconciliation.</em>",
    hero_lead="GSTR-9 (annual return) and GSTR-9C (reconciliation statement) are the yearly GST filings that consolidate all monthly / quarterly returns. For FY 2024-25, due by 31 December 2025 (deadline typically extended). Threshold: GSTR-9 mandatory for turnover above INR 2 crore; GSTR-9C mandatory above INR 5 crore. The reconciliation between GSTR-1, GSTR-3B, GSTR-2A/2B, and books of accounts is where most notices originate. Here's the practitioner's playbook.",
    sections=[
        ("/ GSTR-9 scope + threshold", "Who must file.",
         "<p><strong>GSTR-9 (Annual Return)</strong>:</p>"
         "<ul>"
         "<li>Mandatory for every registered taxpayer under GST (except specified categories).</li>"
         "<li><strong>Turnover threshold</strong>: turnover above <strong>INR 2 crore</strong> in the FY. Below INR 2 crore &mdash; filing is <strong>optional</strong> (made optional via Notification 47/2019 and subsequent amendments).</li>"
         "<li><strong>Exempt from GSTR-9</strong>: Casual Taxable Person, Non-Resident Taxable Person, Input Service Distributor, Composition dealer (files GSTR-9A instead), person deducting TDS under Section 51 (files GSTR-7), person collecting TCS under Section 52 (files GSTR-8).</li>"
         "</ul>"
         "<p><strong>Due date</strong>: 31 December following the FY. For FY 2024-25, due 31 December 2025. For FY 2025-26, due 31 December 2026. Deadlines are typically extended via CBIC notification &mdash; verify current status.</p>"
         "<p><strong>Late fee</strong>: INR 200 per day (INR 100 CGST + INR 100 SGST), capped at 0.25% of turnover.</p>"),
        ("/ GSTR-9C scope + threshold", "Reconciliation with books.",
         "<p><strong>GSTR-9C (Reconciliation Statement)</strong>:</p>"
         "<ul>"
         "<li>Mandatory for taxpayers with <strong>turnover above INR 5 crore</strong> in the FY.</li>"
         "<li>Reconciles GST returns (GSTR-9) with audited financial statements (books of accounts).</li>"
         "<li>Prepared and self-certified by the taxpayer (CA certification requirement was removed effective FY 2020-21).</li>"
         "<li>Includes reconciliation of turnover, taxable supplies, ITC, tax paid.</li>"
         "<li>Filed as part of or alongside GSTR-9 on GST portal.</li>"
         "</ul>"
         "<p><strong>Note</strong>: GSTR-9C was earlier required with CA certification. Finance Act 2021 removed the CA attestation requirement; now self-certified by the taxpayer. The underlying reconciliation workload remains the same.</p>"),
        ("/ Reconciliation sections (the core work)", "What GSTR-9 and 9C actually reconcile.",
         "<p>GSTR-9 has 19 Tables. Core reconciliation areas:</p>"
         "<ul>"
         "<li><strong>Table 4 - Supplies on which tax is payable</strong>: outward supplies declared in GSTR-1 vs reported in GSTR-3B. Mismatch here means either under- or over-reported sales.</li>"
         "<li><strong>Table 5 - Supplies on which tax is NOT payable</strong>: nil-rated, exempt, non-GST supplies. Must match GSTR-1 and GSTR-3B.</li>"
         "<li><strong>Table 6 - ITC availed</strong>: ITC claimed in GSTR-3B during the FY. Must match reconciled 2B/2A ledger.</li>"
         "<li><strong>Table 7 - ITC reversed / ineligible</strong>: Section 17(5) blocks (motor vehicles, construction materials), Rule 42/43 proportional reversal, Section 16(4) time-barred ITC.</li>"
         "<li><strong>Table 8 - Other ITC-related information</strong>: ITC as per GSTR-2A/2B vs 3B claimed. Shortfall triggers reversal with interest; excess available-not-claimed is forgone.</li>"
         "<li><strong>Table 9 - Payment of tax</strong>: tax paid under reverse charge, CGST/SGST/IGST/CESS breakdown.</li>"
         "<li><strong>Tables 10-14 - Amendments, demand, refund</strong>.</li>"
         "<li><strong>Table 15 - HSN-wise summary of outward supplies</strong>: HSN code and quantity breakdown.</li>"
         "<li><strong>Table 16 - HSN-wise summary of inward supplies</strong>: for inputs/capital goods.</li>"
         "</ul>"
         "<p>GSTR-9C adds Books-of-Accounts reconciliation:</p>"
         "<ul>"
         "<li>Turnover per audited books vs turnover declared in GSTR-9.</li>"
         "<li>Taxable supplies reconciliation (Part II).</li>"
         "<li>ITC reconciliation vs books ITC ledger (Part III).</li>"
         "<li>Tax paid reconciliation (Part IV).</li>"
         "<li>Reasons for unreconciled items (Part V).</li>"
         "</ul>"),
        ("/ Common mismatches + fixes", "Where notices originate.",
         "<ul>"
         "<li><strong>GSTR-1 vs GSTR-3B turnover mismatch</strong>: common when invoices are entered in 3B but not pushed to 1, or vice versa. Fix: reconcile monthly; correct via amendment in subsequent 3B or GSTR-1A.</li>"
         "<li><strong>GSTR-3B ITC vs GSTR-2B claimed</strong>: 3B ITC exceeds 2B &mdash; indicates ITC on invoices not reported by vendor. Fix: chase vendor for GSTR-1 filing OR reverse ITC with interest.</li>"
         "<li><strong>Books turnover vs GSTR-9 turnover</strong>: credit notes, debit notes, discounts, year-end adjustments not reflected in GST returns. Fix: reconcile Books-to-GST turnover with adjustment column in GSTR-9C.</li>"
         "<li><strong>ITC claimed but ineligible under Section 17(5)</strong>: motor vehicles (personal), construction materials for own-building, food and beverage, employee insurance (certain categories), club membership. Fix: reverse via Table 7 of GSTR-9 with interest.</li>"
         "<li><strong>ITC time-barred under Section 16(4)</strong>: ITC claimable only by the earlier of (a) due date of GSTR-3B for September of next FY, or (b) date of filing of annual return. Missed ITC lost; cannot be revived.</li>"
         "<li><strong>Reverse charge mechanism (RCM) under Section 9(3) / 9(4) not paid</strong>: specified categories (import of services, GTA services, legal services, security services, rent of residential dwelling to registered person). Fix: pay RCM in GSTR-3B with interest; claim ITC in next period.</li>"
         "<li><strong>HSN-wise summary missing or inaccurate</strong>: Tables 15-16 require HSN-wise breakdown of supplies. Books-level HSN tracking essential year-round.</li>"
         "</ul>"
         "<p><em>Last updated: 2026-10-12.</em></p>"),
    ],
    faqs=[
        ("Is GSTR-9 mandatory for all GST-registered taxpayers?",
         "No. GSTR-9 is mandatory only for taxpayers with aggregate turnover above INR 2 crore in the FY. For taxpayers with turnover below INR 2 crore, GSTR-9 is optional (made optional via Notification 47/2019 and subsequent amendments). Composition dealers file GSTR-9A instead."),
        ("What is the difference between GSTR-9 and GSTR-9C?",
         "GSTR-9 is the annual return summarising all monthly / quarterly returns for the FY. GSTR-9C is the reconciliation statement reconciling GSTR-9 figures with audited financial statements (books of accounts). GSTR-9C mandatory for turnover above INR 5 crore. GSTR-9C was earlier CA-certified; now self-certified from FY 2020-21 onwards."),
        ("When is GSTR-9 for FY 2025-26 due?",
         "31 December 2025 (standard deadline). CBIC typically extends via notification; verify current status before filing. Late fee if filed after extended due date: INR 200 per day (INR 100 CGST + INR 100 SGST), capped at 0.25% of turnover."),
        ("Can I claim missed ITC in GSTR-9?",
         "No. GSTR-9 is only a summary / reconciliation statement; it does not allow fresh ITC claims. Missed ITC must be claimed in GSTR-3B by the earlier of (a) due date of September's 3B of the next FY, or (b) date of filing GSTR-9 for the FY (effectively 30 November following FY, with annual return deadline). Beyond this, ITC is time-barred under Section 16(4)."),
        ("What are the common GSTR-9 mismatches that trigger notices?",
         "GSTR-1 vs GSTR-3B turnover mismatch, GSTR-3B ITC vs GSTR-2B shortfall, books turnover vs GST turnover (credit notes, discounts, year-end adjustments), Section 17(5) blocked ITC claimed, RCM supplies not reported, HSN-wise summary missing. Each of these can trigger ASMT-10 (notice of discrepancy) or Section 61 scrutiny proceedings."),
        ("Does BQP handle GSTR-9 / GSTR-9C filing?",
         "Yes - full year-end reconciliation (GSTR-1 vs GSTR-3B, 3B vs 2B, books vs GSTR-9), ITC blocking under Section 17(5) analysis, RCM reconciliation, HSN-wise summary preparation, GSTR-9C self-certification. Annual engagement typically scoped alongside quarterly GSTR-3B / GSTR-1 compliance. WhatsApp +91 78018 87130."),
    ],
    related=[
        ("gst-notice-response-india-asmt-drc-gstr.html", "Blog", "GST Notice Response"),
        ("section-194q-tds-purchase-goods-india.html", "Blog", "Section 194Q"),
    ],
    cta_headline="GST turnover > INR 2 crore? GSTR-9 is annual mandatory.",
    cta_body="Working-CA year-end reconciliation: GSTR-1 vs GSTR-3B, 3B vs 2B, books vs GST, Section 17(5) blocking, RCM supplies, HSN summary. Filed by 31 December. BQP annual engagement scopes GSTR-9 + GSTR-9C alongside quarterly 3B/GSTR-1.",
))

# 9. FLA Return
write_page("fla-return-foreign-liabilities-assets-rbi-india", page(
    slug="fla-return-foreign-liabilities-assets-rbi-india",
    title="FLA Return (Foreign Liabilities & Assets) 2026 | RBI July 15 Deadline - BQP",
    description="FLA Return 2026 under FEMA: mandatory annual filing by Indian companies / LLPs with foreign direct investment or outbound investment, 15 July deadline, FLAIR portal filing process, consequences of non-filing, exemption criteria. Working CA guide by Durgesh Chavda.",
    keywords="FLA Return RBI 2026, Foreign Liabilities Assets Return, FLAIR portal filing, FEMA annual return foreign investment, FLA Return due date 15 July",
    hero_kicker="/ Blog &middot; FLA Return (RBI) &middot; Updated 2026-10-12",
    hero_title_html="FLA Return, <em>RBI's annual foreign-investment filing.</em>",
    hero_lead="FLA (Foreign Liabilities and Assets) Return is an annual mandatory filing to the RBI under FEMA by every Indian company, LLP, or AIF that has received foreign direct investment (FDI) OR made outbound investment (ODI) in any prior financial year. Due 15 July each year. Non-compliance can trigger FEMA compounding + penalty. Many Indian companies with foreign shareholders miss this filing. Here's the practitioner's guide.",
    sections=[
        ("/ Who must file FLA Return", "The scope.",
         "<p>FLA Return is mandatory under FEMA Master Direction on Reporting under Foreign Exchange Management Act, for every:</p>"
         "<ul>"
         "<li><strong>Indian company</strong> that has received <strong>FDI (inbound foreign equity investment)</strong> in the current or any previous FY AND still has outstanding foreign liability (foreign-shareholder balance) at the end of the FY.</li>"
         "<li><strong>Indian company</strong> that has made <strong>ODI (outbound overseas investment)</strong> in the current or any previous FY AND still has outstanding foreign asset at the end of the FY.</li>"
         "<li><strong>LLP</strong> with foreign capital contribution.</li>"
         "<li><strong>AIF, Partnership firm, Public Private Partnership</strong> with foreign liabilities / assets.</li>"
         "</ul>"
         "<p>Even if there is no fresh transaction in the current FY, if the opening balance of foreign liability / asset exists, FLA Return is mandatory.</p>"
         "<p><strong>Exempt (no FLA Return required)</strong>:</p>"
         "<ul>"
         "<li>Companies with no foreign shareholder and no overseas investment.</li>"
         "<li>Companies where all foreign shareholding has been fully exited (nil opening balance for the FY).</li>"
         "<li>Non-reporting companies specifically identified by RBI.</li>"
         "</ul>"),
        ("/ Due date + filing route", "15 July via FLAIR portal.",
         "<p><strong>Due date</strong>: on or before <strong>15 July</strong> of the year following the FY. For FY 2024-25, due by 15 July 2025. For FY 2025-26, due by 15 July 2026.</p>"
         "<p>If audited financial statements are not available by 15 July, the FLA Return can be filed with <strong>provisional (unaudited) numbers</strong> &mdash; a revised FLA Return with audited numbers must then be filed within 30 days of signing of audited financials.</p>"
         "<p><strong>Filing route</strong>:</p>"
         "<ol>"
         "<li>FLA Return filed on the <strong>FLAIR portal</strong> (RBI's Foreign Liabilities and Assets Information Reporting system) at <code style='font:400 12px Inter;background:#f8f3e8;padding:1px 6px;border-radius:3px'>flair.rbi.org.in</code>.</li>"
         "<li>First-time users register on the portal with company's PAN + entity type + authorised person details.</li>"
         "<li>Fill the online FLA Return form with company's shareholding pattern, foreign shareholders' details, outbound investments, equity + reserves + surplus, borrowing, assets.</li>"
         "<li>Attach supporting documents: audited balance sheet (or provisional), auditor's report, share capital register.</li>"
         "<li>Submit with DSC of the authorised signatory.</li>"
         "<li>Download acknowledgement.</li>"
         "</ol>"),
        ("/ Information required in FLA Return", "What RBI wants.",
         "<p>Core sections of FLA Return:</p>"
         "<ul>"
         "<li><strong>Section 1</strong>: identification details (PAN, CIN, incorporation date, main activity, SBI RRN if applicable).</li>"
         "<li><strong>Section 2</strong>: equity position &mdash; paid-up capital, foreign shareholder equity breakdown, resident shareholder equity. End-of-FY numbers.</li>"
         "<li><strong>Section 3</strong>: foreign direct investment inward &mdash; foreign shareholder-wise paid-up equity, country of residence, breakup of equity, preference shares, convertible instruments.</li>"
         "<li><strong>Section 4</strong>: outbound direct investment &mdash; details of overseas subsidiaries / JVs with equity + loans given.</li>"
         "<li><strong>Section 5</strong>: other foreign liabilities &mdash; External Commercial Borrowings (ECBs), trade credit, foreign bank loans.</li>"
         "<li><strong>Section 6</strong>: foreign assets &mdash; overseas bank accounts, foreign securities, loans given to foreign parties.</li>"
         "<li><strong>Section 7</strong>: income &amp; dividends &mdash; dividend paid to foreign shareholders in FY, dividend received from overseas subsidiaries.</li>"
         "</ul>"),
        ("/ Non-compliance consequences", "What breaks.",
         "<ul>"
         "<li><strong>FEMA compounding</strong>: non-filing is a FEMA breach under Section 13. Compounding application can be filed voluntarily to pay reduced penalty (approximately INR 10,000-50,000 per year of non-filing, scaling with company size).</li>"
         "<li><strong>Compounding + penalty</strong>: for persistent non-filing, RBI can impose compounding fee + penalty up to 3 times the amount involved.</li>"
         "<li><strong>Operational</strong>: AD banks may hesitate to process future foreign remittances (inward FDI or outward ODI dividend repatriation) if FLA Return history is non-compliant.</li>"
         "<li><strong>Diligence red flag</strong>: in M&amp;A diligence, future FDI, future ODI, auditor review &mdash; FLA Return non-compliance surfaces and must be fixed.</li>"
         "</ul>"
         "<p>Clean-up: file all missed FLA Returns for prior years (if the data can be reconstructed), then apply for compounding on FEMA breaches. Typical compounding timeline: 90-180 days from application to RBI order.</p>"
         "<p><em>Last updated: 2026-10-12.</em></p>"),
    ],
    faqs=[
        ("What is FLA Return?",
         "Foreign Liabilities and Assets Return - annual filing to RBI under FEMA by Indian companies / LLPs / AIFs with foreign direct investment (inward FDI) or outbound overseas investment (ODI). Reports foreign shareholder equity, dividend paid to foreign shareholders, overseas subsidiary investments, ECBs, foreign assets. Due 15 July each year via FLAIR portal (flair.rbi.org.in)."),
        ("Who is required to file FLA Return?",
         "Every Indian company / LLP / AIF with (a) foreign shareholder equity outstanding at end of FY, OR (b) outbound overseas investment outstanding at end of FY. Even companies with no fresh transaction in the current FY must file if the opening balance of foreign liability / asset exists. Companies with no foreign shareholder and no outbound investment are exempt."),
        ("What is the FLA Return due date for FY 2025-26?",
         "15 July 2026 for FY 2025-26 (FY 1 April 2025 to 31 March 2026). Can be filed with provisional (unaudited) financials if audited not available by 15 July; revised FLA Return with audited numbers must then be filed within 30 days of audit completion."),
        ("Where do I file FLA Return?",
         "FLAIR portal (Foreign Liabilities and Assets Information Reporting) at flair.rbi.org.in. First-time users register with PAN + entity type + authorised person details. Fill online form, attach audited (or provisional) financials, submit with DSC. Download acknowledgement."),
        ("What happens if I miss FLA Return?",
         "FEMA breach under Section 13. Voluntary compounding application reduces penalty - approximately INR 10,000-50,000 per year of non-filing. Persistent non-filing can attract higher penalty up to 3 times the amount involved. Also blocks AD banks from processing future foreign remittances. Clean up: file all missed years + apply compounding."),
        ("Does BQP handle FLA Return filing?",
         "Yes - FLA Return preparation + FLAIR portal filing, foreign shareholder-wise equity breakdown, outbound investment reconciliation with FEMA ODI records, past-year FLA cleanup if any missed, voluntary compounding application if non-filing is historic. Annual engagement for companies with FDI / ODI. Co-ordinated with Form FC-GPR, FC-TRS, Form ODI, APR under one FEMA compliance stack. WhatsApp +91 78018 87130."),
    ],
    related=[
        ("fema-odi-us-entity-indian-founder.html", "Guide", "FEMA ODI"),
        ("fdi-vs-fpi-india-startup-investment.html", "Guide", "FDI vs FPI"),
    ],
    cta_headline="Indian company with foreign shareholder or overseas subsidiary?",
    cta_body="FLA Return by 15 July is annual mandatory. BQP FEMA compliance stack: FLA Return + Form FC-GPR + FC-TRS + Form ODI + APR + voluntary compounding of missed filings. One firm, one engagement, no surprises.",
))

# 10. Udyam MSME Registration
write_page("udyam-msme-registration-benefits-india-2026", page(
    slug="udyam-msme-registration-benefits-india-2026",
    title="Udyam MSME Registration + Benefits 2026 | Micro, Small, Medium Classification - BQP",
    description="Udyam Registration 2026: MSME classification by investment + turnover, Micro / Small / Medium thresholds, benefits (collateral-free loan, interest subvention, GEM procurement, delayed-payment protection Section 15 MSMED Act), online registration process, Udyam Assist Platform. Working CA guide by Durgesh Chavda.",
    keywords="Udyam Registration 2026, MSME registration India, Udyam portal registration process, MSME classification investment turnover, MSME benefits India, Section 15 MSMED Act delayed payment",
    hero_kicker="/ Blog &middot; Udyam MSME Registration &middot; Updated 2026-10-12",
    hero_title_html="Udyam MSME Registration, <em>benefits and process 2026.</em>",
    hero_lead="Udyam Registration is the current (replaced Udyog Aadhaar from July 2020) government recognition for Micro, Small, and Medium Enterprises (MSMEs) in India. Registration is free, online, takes 10 minutes, and unlocks collateral-free credit, interest subvention, GEM procurement access, delayed-payment protection under Section 15 of MSMED Act, and sector-specific government schemes. Every MSME-eligible business should register. Here's the complete 2026 guide.",
    sections=[
        ("/ MSME classification criteria (post-2020)", "Investment + turnover.",
         "<p>Post-July-2020, MSME classification uses <strong>composite criteria</strong>: investment in plant and machinery / equipment AND turnover. Enterprise classified based on <strong>higher of the two</strong> metrics (promotes-up classification; no demotion):</p>"
         "<table style='width:100%;border-collapse:collapse;margin:12px 0;font:400 13px Inter'>"
         "<tr style='background:#f8f3e8'><th style='padding:8px;border:1px solid #ece4d5;text-align:left'>Classification</th><th style='padding:8px;border:1px solid #ece4d5;text-align:left'>Investment in P&amp;M / Equipment</th><th style='padding:8px;border:1px solid #ece4d5;text-align:left'>Turnover</th></tr>"
         "<tr><td style='padding:8px;border:1px solid #ece4d5'><strong>Micro</strong></td><td style='padding:8px;border:1px solid #ece4d5'>Up to INR 2.5 crore</td><td style='padding:8px;border:1px solid #ece4d5'>Up to INR 10 crore</td></tr>"
         "<tr><td style='padding:8px;border:1px solid #ece4d5'><strong>Small</strong></td><td style='padding:8px;border:1px solid #ece4d5'>Up to INR 25 crore</td><td style='padding:8px;border:1px solid #ece4d5'>Up to INR 100 crore</td></tr>"
         "<tr><td style='padding:8px;border:1px solid #ece4d5'><strong>Medium</strong></td><td style='padding:8px;border:1px solid #ece4d5'>Up to INR 125 crore</td><td style='padding:8px;border:1px solid #ece4d5'>Up to INR 500 crore</td></tr>"
         "</table>"
         "<p><em>Note: thresholds revised upward by Finance Act 2024 effective April 2025 (from earlier INR 1 crore / INR 10 crore for Micro etc.). The current limits above reflect FY 2025-26 onwards.</em></p>"
         "<p><strong>Exports excluded from turnover</strong>: for classification purposes, export turnover is excluded (encouraging exports without pushing MSMEs out of their category).</p>"
         "<p><strong>Both manufacturing and services sectors covered</strong>: unified criteria for both sectors post-July 2020. Earlier manufacturing and services had different thresholds.</p>"),
        ("/ Benefits of Udyam Registration", "What MSMEs unlock.",
         "<p><strong>Credit benefits</strong>:</p>"
         "<ul>"
         "<li><strong>Collateral-free loan up to INR 10 crore</strong> under CGTMSE (Credit Guarantee Fund Trust for Micro and Small Enterprises). Loans up to INR 10 crore from banks and NBFCs covered by CGTMSE guarantee &mdash; borrower does not pledge personal / property collateral.</li>"
         "<li><strong>Interest subvention</strong> under specific schemes (varies by sector, Union Budget allocations).</li>"
         "<li>Priority sector lending compliance for banks &mdash; banks actively seek MSME-registered borrowers.</li>"
         "</ul>"
         "<p><strong>Procurement benefits</strong>:</p>"
         "<ul>"
         "<li><strong>GEM (Government e-Marketplace) registration</strong> &mdash; Udyam-registered MSMEs can bid on central and state government procurement. Mandatory 25% procurement from MSMEs under Public Procurement Policy for MSEs 2012.</li>"
         "<li><strong>Preference in CPSE (Central Public Sector Enterprise) tenders</strong>.</li>"
         "<li><strong>Exemption from EMD (Earnest Money Deposit)</strong> and reduced tender fee for Micro and Small Enterprises.</li>"
         "</ul>"
         "<p><strong>Delayed payment protection</strong>:</p>"
         "<ul>"
         "<li><strong>Section 15 of MSMED Act 2006</strong>: if buyer (any person) delays payment to MSE beyond 45 days from acceptance of goods / services, interest at <strong>3 times RBI bank rate</strong> (compounded monthly) is payable by buyer. This is a powerful recovery lever.</li>"
         "<li><strong>Section 16 MSMED</strong>: dispute resolution via Micro and Small Enterprises Facilitation Council (MSEFC), relatively fast arbitration.</li>"
         "<li><strong>Section 23 Income Tax Act</strong>: amount payable to Micro and Small Enterprise beyond 45 days is disallowed as deduction in the buyer's hands under Section 43B(h). Finance Act 2023 inserted Section 43B(h) &mdash; delayed payments beyond 45 days result in buyer's expense being deductible only on actual payment, not on accrual. Material P&amp;L impact on buyers who delay MSE payments.</li>"
         "</ul>"
         "<p><strong>Tax benefits</strong>:</p>"
         "<ul>"
         "<li>Direct tax benefits are limited; Section 15 recovery leverage is the bigger benefit.</li>"
         "<li>Specific state-level stamp duty / electricity concessions in some states for MSMEs.</li>"
         "</ul>"
         "<p><strong>Other benefits</strong>:</p>"
         "<ul>"
         "<li>Patent registration subsidy (up to 50% reimbursement under Patent Reimbursement Scheme).</li>"
         "<li>ISO certification subsidy.</li>"
         "<li>Barcode registration subsidy.</li>"
         "<li>Market access support (TReDS platform for invoice discounting).</li>"
         "<li>MSME Samadhaan portal for delayed payment grievance (free online complaint mechanism).</li>"
         "</ul>"),
        ("/ Udyam Registration process", "Step-by-step.",
         "<ol>"
         "<li><strong>Visit Udyam Registration portal</strong>: <code style='font:400 12px Inter;background:#f8f3e8;padding:1px 6px;border-radius:3px'>udyamregistration.gov.in</code>.</li>"
         "<li><strong>For new registration</strong>: 'For New Entrepreneurs who are not Registered yet as MSME'. For existing Udyog Aadhaar holders: 'For those having registration as EM-II or UAM' (one-time migration).</li>"
         "<li><strong>Enter Aadhaar number</strong> of the applicant. For individual proprietor: own Aadhaar. For partnership firm: any partner's Aadhaar. For HUF: Karta's Aadhaar. For company / LLP: authorised signatory's Aadhaar.</li>"
         "<li><strong>Verify OTP</strong> sent to Aadhaar-linked mobile number.</li>"
         "<li><strong>Enter PAN</strong>: of the enterprise. System auto-fetches ITR data to classify as Micro / Small / Medium based on investment and turnover.</li>"
         "<li><strong>Fill enterprise details</strong>: enterprise name, type (proprietorship / partnership / company / LLP / HUF / cooperative / trust), social category of applicant, major activity (manufacturing / service), NIC code, number of employees, bank account.</li>"
         "<li><strong>Submit</strong>: Udyam Registration Number (URN) generated instantly. Udyam Registration Certificate downloadable.</li>"
         "<li><strong>No fee</strong>: free registration.</li>"
         "</ol>"
         "<p>Timeline: 10 minutes if PAN + Aadhaar are in order. Registration can be done directly by the applicant without needing a professional.</p>"),
        ("/ Udyam Assist Platform (UAP)", "For unregistered enterprises.",
         "<p>Many micro enterprises (especially street vendors, informal businesses) don't have PAN or formal registration. Udyam Assist Platform (UAP) was launched 2023 for these informal micro enterprises:</p>"
         "<ul>"
         "<li>Registration via designated agencies (banks, NBFCs, Public Sector Insurance companies, DIC, PGUP etc.).</li>"
         "<li>Issues Udyam Assist Certificate (UAC) which has similar legal effect for benefit eligibility.</li>"
         "<li>Lower documentation threshold; agency verifies informal enterprise details.</li>"
         "</ul>"
         "<p>For registered formal businesses, standard Udyam portal is the route.</p>"
         "<p><em>Last updated: 2026-10-12.</em></p>"),
    ],
    faqs=[
        ("What is Udyam Registration?",
         "Current government MSME recognition system (replaced Udyog Aadhaar from July 2020). Free, online, 10-minute registration at udyamregistration.gov.in. Classifies enterprises as Micro, Small, or Medium based on investment in P&M/equipment and turnover. Unlocks collateral-free loan, interest subvention, GEM procurement, Section 15 MSMED Act delayed-payment protection, Section 43B(h) Income Tax interaction."),
        ("What are the Micro / Small / Medium thresholds?",
         "Post FY 2025-26: Micro - investment up to INR 2.5 crore, turnover up to INR 10 crore. Small - investment up to INR 25 crore, turnover up to INR 100 crore. Medium - investment up to INR 125 crore, turnover up to INR 500 crore. Enterprise classified based on higher of the two metrics. Export turnover excluded. Both manufacturing and services covered."),
        ("What is Section 43B(h) and how does it affect buyers of MSE?",
         "Finance Act 2023 inserted Section 43B(h): expenses payable to Micro and Small Enterprise beyond 45 days from acceptance of goods / services are disallowed in the buyer's hands and allowed only on actual payment, not on accrual. Material P&L impact on buyers who delay MSE payments - creates strong commercial pressure to pay MSEs on time."),
        ("Can an MSME lose MSME status if it grows?",
         "Previously, MSME classification was reviewed and could demote enterprises crossing thresholds. Post-2020 rules provide a 3-year grace period before reclassification. Udyam also allows 'promotion' (upgrading from Micro to Small) but not demotion for 3 years. Growing enterprises retain benefits for defined period."),
        ("Is Udyam Registration mandatory?",
         "Not mandatory - voluntary. But practically essential if you want to claim MSME benefits (collateral-free loan, GEM procurement, delayed-payment Section 15 protection). Without Udyam Registration, you cannot invoke MSE status or claim MSE-specific benefits. Takes 10 minutes; no fee. No reason not to register if eligible."),
        ("Does BQP handle Udyam Registration?",
         "Yes - standard one-time engagement. We handle Udyam Registration for new entities, migration from legacy Udyog Aadhaar, classification queries (whether enterprise qualifies as Micro / Small / Medium), Section 43B(h) buyer compliance analysis, Section 15 MSMED Act recovery against delayed-paying customers via MSME Samadhaan portal. WhatsApp +91 78018 87130."),
    ],
    related=[
        ("startup-registration.html", "Service", "Startup Registration"),
        ("how-to-register-startup-india-dpiit.html", "Guide", "DPIIT Startup India"),
    ],
    cta_headline="Running an eligible business without Udyam Registration?",
    cta_body="Free + 10 minutes + significant benefits (collateral-free loans, GEM procurement, Section 15 payment protection, Section 43B(h) leverage). BQP standard one-time engagement covers registration + ongoing MSME-benefit utilisation.",
))

print("Batch L complete: 10 compliance-gap SEO pages written")
