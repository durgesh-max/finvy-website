# -*- coding: utf-8 -*-
"""Batch T: 12 pages targeting specific-form filing + sub-niche queries.

8 form-filing checklist pages + 4 sector sub-niche positioning pages.
"""
from build_lib import page, write_page


def quick_page(slug, title, hero_em, lead, kicker, sections_pairs, faqs, related_pairs, cta_h, cta_b, keywords, desc):
    return page(
        slug=slug, title=title, description=desc, keywords=keywords,
        hero_kicker=kicker,
        hero_title_html=f"{title.split(' | ')[0]}, <em>{hero_em}</em>",
        hero_lead=lead,
        sections=sections_pairs, faqs=faqs,
        related=[(h, "Related", l) for h, _, l in related_pairs],
        cta_headline=cta_h, cta_body=cta_b,
    )


# ===== 8 FORM-FILING CHECKLIST PAGES =====

PAGES = []

# 1. Form FC-GPR
PAGES.append({
    "slug": "form-fc-gpr-filing-checklist-india-2026",
    "title": "Form FC-GPR Filing Checklist India 2026 | FDI Reporting Guide - BQP",
    "hero_em": "30-day deadline + checklist.",
    "lead": "Form FC-GPR (Foreign Currency - Gross Provisional Return) is mandatory FEMA filing by Indian company receiving foreign inward FDI remittance: within 30 days of share allotment post remittance. Non-filing attracts FEMA Section 13 compounding. Here's the complete 2026 filing checklist.",
    "kicker": "/ FEMA Form Checklist &middot; Updated 2026-10-22",
    "sections_pairs": [
        ("/ Who must file + when", "The core rule.",
         "<ul>"
         "<li>Indian company receives foreign inward remittance for share subscription (FDI).</li>"
         "<li>Share allotment made to foreign subscriber.</li>"
         "<li>Form FC-GPR filed within <strong>30 days of allotment</strong> via FIRMS portal (RBI).</li>"
         "<li>Non-filing or late filing: FEMA Section 13 compounding (voluntary) or RBI inspection + penalty up to 3x amount involved.</li>"
         "</ul>"),
        ("/ Required documents", "The attachments.",
         "<ul>"
         "<li>FIRC (Foreign Inward Remittance Certificate) from AD bank.</li>"
         "<li>KYC of foreign subscriber (passport + address proof).</li>"
         "<li>Board resolution authorising allotment.</li>"
         "<li>Share allotment letter.</li>"
         "<li>Pricing certification: CA / Merchant Banker certificate confirming price per Rule 21 Pricing Guidelines (DCF for unlisted; closing price for listed).</li>"
         "<li>Non-resident declaration of eligibility.</li>"
         "<li>CS certificate of compliance (where applicable).</li>"
         "</ul>"),
        ("/ Filing workflow", "Step-by-step.",
         "<ol>"
         "<li>Collect foreign shareholder KYC + apostilled documents pre-allotment.</li>"
         "<li>Verify FDI route: automatic vs approval; sector cap check.</li>"
         "<li>Press Note 3 beneficial ownership check for land-bordering country investments.</li>"
         "<li>Receive foreign remittance in AD-I bank account. Obtain FIRC.</li>"
         "<li>Allot shares via board resolution within 60 days of remittance (Rule 2A Companies Act).</li>"
         "<li>Issue share certificates + file Form PAS-3 within 30 days.</li>"
         "<li>Obtain pricing certificate from CA / Merchant Banker.</li>"
         "<li>File Form FC-GPR via FIRMS portal within 30 days of allotment.</li>"
         "<li>AD bank reviews + confirms successful filing.</li>"
         "<li>Preserve filing acknowledgement + all supporting documents 8+ years.</li>"
         "</ol>"),
        ("/ Common mistakes + fixes", "What goes wrong.",
         "<ul>"
         "<li><strong>Missed 30-day deadline</strong>: FEMA compounding under Section 13 - INR 10,000-50,000 per instance typically.</li>"
         "<li><strong>Pricing below Rule 21 guidelines</strong>: FEMA breach - compounding + possible unwinding.</li>"
         "<li><strong>Press Note 3 breach</strong>: beneficial ownership from land-bordering country without approval - serious compounding + unwinding risk.</li>"
         "<li><strong>Share allotment delay beyond 60 days</strong>: separate FEMA breach (Rule 2A pre-amendment was 180 days; now 60 days).</li>"
         "<li><strong>FIRC not obtained</strong>: cannot file FC-GPR without FIRC. Chase AD bank.</li>"
         "<li><strong>Wrong pricing method</strong>: unlisted uses DCF (Rule 21); listed uses closing price. Methodology must match Rule 21.</li>"
         "</ul>"
         "<p><em>Last updated: 2026-10-22.</em></p>"),
    ],
    "faqs": [
        ("When is Form FC-GPR due?",
         "Within 30 days of share allotment to foreign subscriber. Allotment itself must be within 60 days of remittance receipt (Rule 2A Companies Act). So typical timeline: remittance → 60 days → allotment → 30 days → FC-GPR filing. Total 90 days from remittance to FC-GPR."),
        ("What's the penalty for late FC-GPR?",
         "FEMA Section 13 compounding (voluntary): typically INR 10,000-50,000 per instance for minor delay. For prolonged non-filing or sector-cap breach: significantly higher, up to 3x amount involved. Voluntary compounding is cheaper than RBI inspection-driven proceedings."),
        ("What's Rule 21 pricing guidelines?",
         "FEMA Rule 21 (Non-debt Instrument Rules 2019 + predecessors): share issue to non-resident must be at fair value. Unlisted: DCF method (discounted cash flow) by Merchant Banker or Chartered Accountant. Listed: closing price. Issue below Rule 21 pricing is FEMA breach."),
        ("Can BQP file FC-GPR for Indian subsidiary of foreign parent?",
         "Yes - standard service. Documentation collection + pricing certification + FIRMS portal filing within 30-day deadline. Also handle associated compliances: Form PAS-3 share allotment + MGT-14 board resolution + FEMA compounding if past breaches."),
        ("Does BQP handle FEMA voluntary compounding for missed FC-GPR?",
         "Yes - integrated. Historical FEMA breach audit + Section 13 compounding application + hearing representation + fee payment + closure certificate. See our FEMA compounding guide. WhatsApp +91 78018 87130."),
    ],
    "related_pairs": [("foreign-company-setup-indian-subsidiary-wos.html", "Related", "India WOS Setup"),
                      ("fema-compounding-foreign-subsidiary-india.html", "Related", "FEMA Compounding")],
    "cta_h": "Foreign FDI received? FC-GPR due in 30 days.",
    "cta_b": "FIRC + Rule 21 pricing + FIRMS portal filing. BQP end-to-end + FEMA compounding if past breaches. Scope-based engagement.",
    "keywords": "Form FC-GPR filing India 2026, FC-GPR FDI reporting CA, FEMA FC-GPR 30 days, Rule 21 pricing CA India",
    "desc": "Form FC-GPR filing checklist India 2026: 30-day deadline from share allotment, FIRC collection, Rule 21 pricing certificate, FIRMS portal filing, FEMA Section 13 compounding for missed filings. Working CA guide by Durgesh Chavda.",
})

# 2. Form FC-TRS
PAGES.append({
    "slug": "form-fc-trs-filing-checklist-india-2026",
    "title": "Form FC-TRS Filing Checklist India 2026 | Share Transfer Guide - BQP",
    "hero_em": "60-day transfer reporting.",
    "lead": "Form FC-TRS mandatory FEMA filing for transfer of shares between resident and non-resident (or between two non-residents in Indian entity): within 60 days of transaction. Covers primary + secondary market transfers. Pricing guidelines + consent letters + CA / Merchant Banker certification required. Here's the complete 2026 filing framework.",
    "kicker": "/ FEMA Form Checklist &middot; Updated 2026-10-22",
    "sections_pairs": [
        ("/ When FC-TRS applies", "Covered transfers.",
         "<ul>"
         "<li><strong>Resident to non-resident</strong>: Indian resident selling shares of Indian company to foreign buyer. FC-TRS by resident.</li>"
         "<li><strong>Non-resident to resident</strong>: Foreign shareholder selling to Indian buyer. FC-TRS by resident buyer.</li>"
         "<li><strong>Non-resident to non-resident</strong>: Foreign shareholder transferring to another foreign party. FC-TRS by the Indian company whose shares are being transferred.</li>"
         "<li>Covers primary + secondary market; equity + preference + convertible; direct + indirect.</li>"
         "<li><strong>Timeline</strong>: within 60 days of transaction via FIRMS portal.</li>"
         "</ul>"),
        ("/ Required documents", "The attachments.",
         "<ul>"
         "<li>Share transfer agreement.</li>"
         "<li>Share transfer form (SH-4) duly stamped.</li>"
         "<li>Pricing certificate from CA / Merchant Banker (Rule 21 Pricing Guidelines).</li>"
         "<li>Consent letters from both parties.</li>"
         "<li>Board resolution approving transfer.</li>"
         "<li>Non-resident party's KYC (passport + address proof + apostille if applicable).</li>"
         "<li>FIRC if money has flowed inward.</li>"
         "<li>Form 15CA + 15CB if payment flowing out of India (for non-resident to resident transfer where consideration is paid).</li>"
         "</ul>"),
        ("/ Pricing guidelines (Rule 21)", "Critical compliance.",
         "<ul>"
         "<li><strong>Transfer by resident to non-resident</strong>: price should NOT be less than fair value (DCF for unlisted). Resident cannot sell cheap to non-resident.</li>"
         "<li><strong>Transfer by non-resident to resident</strong>: price should NOT be more than fair value. Resident cannot overpay to non-resident.</li>"
         "<li><strong>Non-resident to non-resident</strong>: Indian pricing guidelines don't directly apply; but tax implications in India (capital gain) relevant.</li>"
         "<li>Methodology: DCF (unlisted) or closing price (listed). CA / Merchant Banker certificate mandatory.</li>"
         "</ul>"),
        ("/ Common FC-TRS scenarios", "Where it comes up.",
         "<ul>"
         "<li>Startup secondary - founder selling shares to foreign investor.</li>"
         "<li>Angel exit - angel investor selling to Series A VC (foreign).</li>"
         "<li>M&A exit - Indian promoters selling to foreign strategic acquirer.</li>"
         "<li>Buyback - Indian company buying back shares from foreign shareholder.</li>"
         "<li>ESOP exercise by non-resident employee of Indian company.</li>"
         "<li>Group restructuring - inter-affiliate transfers of Indian shares.</li>"
         "<li>Flip - Indian company shares transferred to new US HQ parent.</li>"
         "</ul>"
         "<p><em>Last updated: 2026-10-22.</em></p>"),
    ],
    "faqs": [
        ("When is Form FC-TRS due?",
         "Within 60 days of share transfer transaction. Filed via FIRMS portal (RBI). Non-filing attracts FEMA Section 13 compounding."),
        ("Who files FC-TRS when non-resident sells to non-resident?",
         "The Indian company whose shares are being transferred. Resident party to transaction is the Indian company itself. Specific scenario for inter-foreign-party transfers of Indian securities."),
        ("What's the pricing restriction?",
         "Rule 21: resident cannot sell below fair value to non-resident; cannot buy above fair value from non-resident. Fair value = DCF for unlisted, closing price for listed. CA / Merchant Banker certificate mandatory confirming compliance."),
        ("Does FC-TRS need Form 15CA + 15CB?",
         "If share consideration is paid in foreign currency to non-resident (e.g., Indian buyer paying foreign seller): Form 15CA + 15CB required under Rule 37BB. Payment is 'chargeable to tax in India' (capital gain) - Section 195 TDS at applicable rate (treaty rate with TRC + Form 10F)."),
        ("What if FC-TRS was missed historically?",
         "FEMA voluntary compounding under Section 13 - typical INR 10,000-50,000 per instance. Materially cheaper than RBI inspection. BQP integrated FEMA compounding service covers past FC-TRS misses."),
        ("Does BQP file FC-TRS for secondary / M&A transactions?",
         "Yes - standard service alongside M&A transaction advisory. Pricing certificate + share transfer agreement + SH-4 + FIRMS portal filing + Form 15CA/15CB if applicable. Standard turnaround 7-14 days. WhatsApp +91 78018 87130."),
    ],
    "related_pairs": [("foreign-company-setup-indian-subsidiary-wos.html", "Related", "WOS Setup"),
                      ("form-15ca-15cb-foreign-remittance-india.html", "Related", "Form 15CA/CB")],
    "cta_h": "Share transfer between resident + non-resident?",
    "cta_b": "FC-TRS within 60 days + pricing certificate + Form 15CA/CB if applicable. BQP integrated secondary / M&A compliance.",
    "keywords": "Form FC-TRS filing India, FC-TRS 60 days secondary, non-resident share transfer CA India, Rule 21 pricing CA",
    "desc": "Form FC-TRS filing checklist India 2026 for share transfer between resident + non-resident: 60-day deadline, Rule 21 pricing, documents, scenarios (startup secondary, angel exit, M&A, buyback, ESOP, flip). Working CA guide by Durgesh Chavda.",
})

# 3. Form 10-IC election
PAGES.append({
    "slug": "form-10-ic-section-115baa-election-checklist-india-2026",
    "title": "Form 10-IC Section 115BAA Election Checklist India 2026 - BQP",
    "hero_em": "22% tax regime one-time irrevocable opt-in.",
    "lead": "Form 10-IC election to opt into Section 115BAA (22% concessional corporate tax regime) is a one-time irrevocable choice. Filed with first ITR of the FY of election. Forfeits specific deductions (SEZ 10AA, Chapter VI-A except 80JJAA/80M, additional depreciation, scientific research). Must verify tax impact modelling before opt-in. Here's the complete 2026 checklist.",
    "kicker": "/ Tax Election Checklist &middot; Updated 2026-10-22",
    "sections_pairs": [
        ("/ When Form 10-IC should be filed", "The core rule.",
         "<ul>"
         "<li>Any Indian domestic company can opt into Section 115BAA via Form 10-IC with Indian ITR of the FY of election.</li>"
         "<li><strong>Timing</strong>: filed on or before due date for ITR filing of the FY in which election is desired. For AY 2026-27 (FY 2025-26): 31 October 2026 (standard) / 30 November 2026 (TP cases).</li>"
         "<li><strong>Effective</strong>: from the FY of election onwards + all future FYs. Irrevocable.</li>"
         "<li><strong>Rate</strong>: 22% + 10% surcharge + 4% cess = effective 25.17%. No MAT applies.</li>"
         "</ul>"),
        ("/ Forfeited deductions under 115BAA", "What you give up.",
         "<ul>"
         "<li>Section 10AA (SEZ unit deduction).</li>"
         "<li>Section 32(1)(iia) (additional depreciation 20% in year 1).</li>"
         "<li>Section 32AD (investment allowance).</li>"
         "<li>Section 33AB (Tea / Coffee / Rubber Development Account).</li>"
         "<li>Section 33ABA (Site Restoration Fund).</li>"
         "<li>Section 35(1)(ii) / (iia) / (iii) (scientific research donations).</li>"
         "<li>Section 35(2AA) / (2AB) (in-house R&D).</li>"
         "<li>Section 35AD (investment-linked deduction).</li>"
         "<li>Section 35CCC / 35CCD (agricultural extension / skill development).</li>"
         "<li>Chapter VI-A deductions EXCEPT Section 80JJAA (new employment) and Section 80M (inter-corporate dividend).</li>"
         "<li>Carry-forward of losses attributable to above forfeited deductions.</li>"
         "</ul>"),
        ("/ When 115BAA is NOT right", "Where to retain standard regime.",
         "<ul>"
         "<li>Significant SEZ Section 10AA deduction active (SEZ-based company with 10AA years remaining).</li>"
         "<li>Large Section 35(2AB) in-house R&D deduction (deep-tech / pharma / biotech with substantial approved R&D).</li>"
         "<li>Large carry-forward losses attributable to forfeited deductions (would be lost on opt-in).</li>"
         "<li>Research-driven pharma / biotech with specific scientific research deductions.</li>"
         "<li>Specific sectoral deductions planned (shipping Section 115VX, hotel Section 80ID, specific business under Section 35AD).</li>"
         "</ul>"),
        ("/ Decision modelling checklist", "What to verify before filing.",
         "<ol>"
         "<li>Current FY expected net profit + tax at standard regime (25% / 22% / 30% depending on turnover).</li>"
         "<li>5-year projection of profit growth + tax under both regimes.</li>"
         "<li>Current forfeited-deduction value: SEZ 10AA, additional depreciation, scientific research, Chapter VI-A.</li>"
         "<li>Carry-forward losses attributable to forfeited deductions (would be lost).</li>"
         "<li>Decision: 115BAA vs standard. Typically 115BAA wins for most mature profitable companies without SEZ / R&D intensity.</li>"
         "<li>If 115BAA chosen: file Form 10-IC with ITR of FY of election.</li>"
         "<li>Decision is irrevocable - verify before filing.</li>"
         "</ol>"
         "<p><em>Last updated: 2026-10-22.</em></p>"),
    ],
    "faqs": [
        ("When is Form 10-IC filed?",
         "With Indian ITR of the FY in which 115BAA election is desired. For AY 2026-27 (FY 2025-26): with ITR by 31 October 2026 (standard) or 30 November 2026 (TP cases). Form 10-IC + Form 3CA/3CB tax audit + ITR as a package."),
        ("Is Section 115BAA election irrevocable?",
         "Yes - once Form 10-IC is filed, decision is permanent. Company remains in 22% + 10% surcharge + 4% cess regime for all future FYs (subject to meeting ongoing conditions). No reversion to standard regime possible."),
        ("Should every Indian company opt into 115BAA?",
         "Most mature profitable companies - yes. 22% effective ~25.17% vs standard 25% / 22% / 30% + MAT. For companies with substantial SEZ / scientific research / large carry-forward losses - standard regime may be better. Decision modelling required."),
        ("What's the difference between 115BAA and 115BAB?",
         "115BAA: 22% for any Indian domestic company. 115BAB: 15% for NEW manufacturing company (post Oct 2019 incorporation + commencing production by extended date + pure manufacturing). Both forfeit similar deductions. 115BAB more restrictive but lower rate."),
        ("Can new manufacturing company choose 115BAB and later switch to 115BAA?",
         "No - both are irrevocable one-time elections. 115BAB election via Form 10-ID; 115BAA via Form 10-IC. Choose carefully. If 115BAB chosen but conditions not met in subsequent year, may fall back to standard regime (not 115BAA)."),
        ("Does BQP handle 115BAA opt-in modelling + Form 10-IC filing?",
         "Yes - standard scope. 5-year tax projection under standard vs 115BAA vs 115BAB (where applicable), forfeited-deduction impact assessment, carry-forward loss analysis, Form 10-IC drafting + filing. Standard engagement for medium + large Indian companies. WhatsApp +91 78018 87130."),
    ],
    "related_pairs": [("section-115baa-115bab-corporate-tax-regime-india.html", "Related", "Section 115BAA / 115BAB"),
                      ("ay-2026-27-itr-forms-new-disclosures-india.html", "Related", "AY 2026-27 ITR")],
    "cta_h": "Opting into Section 115BAA? Form 10-IC with ITR deadline.",
    "cta_b": "Decision modelling: forfeited deductions + 5-year projection + irrevocability. BQP + Form 10-IC filing with ITR.",
    "keywords": "Form 10-IC Section 115BAA election India, 22% corporate tax opt-in CA, Section 115BAA Form 10-IC filing",
    "desc": "Form 10-IC Section 115BAA (22% concessional corporate tax) election checklist India 2026: one-time irrevocable opt-in, forfeited deductions (SEZ 10AA, additional depreciation, scientific research, Chapter VI-A except 80JJAA/80M), decision modelling framework. Working CA guide by Durgesh Chavda.",
})

# 4. Form 10-ID election (115BAB)
PAGES.append({
    "slug": "form-10-id-section-115bab-election-checklist-india-2026",
    "title": "Form 10-ID Section 115BAB Election Checklist India 2026 - BQP",
    "hero_em": "15% new manufacturing rate opt-in.",
    "lead": "Form 10-ID election into Section 115BAB (15% concessional corporate tax for new manufacturing) is one-time irrevocable. Available only for new manufacturing company incorporated post Oct 2019 + commencing production by extended deadline. More restrictive than 115BAA but materially lower rate. Here's the complete 2026 eligibility + filing checklist.",
    "kicker": "/ Tax Election Checklist &middot; Updated 2026-10-22",
    "sections_pairs": [
        ("/ Who qualifies for 115BAB", "The strict conditions.",
         "<ul>"
         "<li>Company incorporated on or after <strong>1 October 2019</strong>.</li>"
         "<li>Commences manufacturing / production of article / thing on or before <strong>31 March 2024</strong> (extended for specific sectors - verify current state).</li>"
         "<li>Not formed by splitting up / reconstruction of existing business.</li>"
         "<li>Does not use plant and machinery previously used in India (second-hand > 20% threshold disqualifies).</li>"
         "<li>Does not use building previously used as hotel / convention centre.</li>"
         "<li>Engaged in manufacturing or production of article / thing. NOT in: electricity generation (specific exception), mining, book printing, re-labelling, software (controversial post 2022 clarifications).</li>"
         "<li>Related-party transactions at arm's-length pricing.</li>"
         "</ul>"),
        ("/ What 115BAB offers", "The 15% rate.",
         "<ul>"
         "<li>15% corporate tax rate + 10% surcharge + 4% cess = effective 17.16%.</li>"
         "<li>No MAT applies.</li>"
         "<li>Materially lower than standard 25% or 22% or 115BAA 22% effective 25.17%.</li>"
         "<li>Available only during the specific manufacturing-sector window.</li>"
         "</ul>"),
        ("/ Forfeited deductions (similar to 115BAA)", "What you give up.",
         "<ul>"
         "<li>Section 10AA (SEZ unit deduction).</li>"
         "<li>Section 32(1)(iia) (additional depreciation).</li>"
         "<li>Section 32AD (investment allowance).</li>"
         "<li>Section 33AB / 33ABA (Tea/Coffee/Rubber / Site Restoration).</li>"
         "<li>Section 35 (scientific research - all sub-sections).</li>"
         "<li>Section 35AD (investment-linked).</li>"
         "<li>Section 35CCC / 35CCD.</li>"
         "<li>Chapter VI-A except 80JJAA and 80M.</li>"
         "<li>Carry-forward losses attributable to forfeited deductions.</li>"
         "</ul>"),
        ("/ Decision workflow", "Before Form 10-ID.",
         "<ol>"
         "<li>Confirm all conditions: post-Oct-2019 incorporation + manufacturing + commenced production by deadline + no reconstruction + no prior P&M + related-party at arm's-length.</li>"
         "<li>Compare 15% (17.16% effective) vs 22% (25.17% effective) vs standard 25%/30% - 115BAB wins for manufacturing by material margin.</li>"
         "<li>Check PLI eligibility (14 sectors) + state incentive stackability.</li>"
         "<li>Verify Section 10AA SEZ not planned (forfeited).</li>"
         "<li>Verify scientific research deduction not needed.</li>"
         "<li>Carry-forward loss analysis.</li>"
         "<li>File Form 10-ID with Indian ITR of first year of election.</li>"
         "<li>Decision irrevocable - verify before filing.</li>"
         "</ol>"
         "<p><em>Last updated: 2026-10-22.</em></p>"),
    ],
    "faqs": [
        ("What's the eligibility window for Section 115BAB?",
         "Company incorporated post 1 October 2019 + commencing manufacturing/production by 31 March 2024 (extended for specific sectors - verify current state). Specific sectoral extensions may apply via Finance Act notifications. BQP eligibility verification standard scope."),
        ("Is software development eligible for 115BAB?",
         "Controversial. Original intent was physical manufacturing (article or thing). CBDT clarifications 2022+ suggest software development is NOT 'manufacturing' for 115BAB purposes. Specific sub-activities (hardware, embedded systems with substantial hardware component) may qualify. Pure SaaS = services (115BAA 22%, not 115BAB)."),
        ("Can SEZ-based new manufacturing company opt into 115BAB?",
         "Technically yes - no SEZ exclusion. But 115BAB forfeits Section 10AA SEZ deduction. If SEZ 10AA tax holiday is active, must model: 10AA 100% tax-free profit for 5 years + 50% for next 5 vs 115BAB 15% rate. Typically 115BAB wins for post-10AA-holiday mature profit stream."),
        ("Can 115BAB be combined with PLI scheme?",
         "Yes - 115BAB is Income Tax provision; PLI is cash incentive on incremental sales. Both apply simultaneously. Combined with state industrial policy incentives (Gujarat, Tamil Nadu, Karnataka, Maharashtra) - total subsidy stack can reach 15-30% capex + 7-8% recurring tax saving."),
        ("What if conditions are violated after 115BAB opt-in?",
         "If any 115BAB condition is violated in subsequent year (e.g., reconstruction, prior P&M, related-party non-arm's-length), 115BAB benefit lost from that year + all subsequent years. Falls back to standard regime (not 115BAA). Material downside - condition monitoring critical."),
        ("Does BQP handle 115BAB eligibility + Form 10-ID filing + PLI integration?",
         "Yes - specialist manufacturing / cleantech / EV / battery / semiconductor practice. Eligibility verification + 5-year tax projection + Form 10-ID filing + PLI application + state incentive negotiation + ongoing compliance monitoring. Standard engagement for strategic manufacturing investments. WhatsApp +91 78018 87130."),
    ],
    "related_pairs": [("section-115baa-115bab-corporate-tax-regime-india.html", "Related", "115BAA / 115BAB Full Guide"),
                      ("india-pli-scheme-foreign-manufacturer-2026.html", "Related", "PLI Scheme")],
    "cta_h": "New manufacturing company? Form 10-ID 15% rate opt-in.",
    "cta_b": "Eligibility verification + 115BAB vs 115BAA comparison + PLI stackability + state incentive. BQP integrated.",
    "keywords": "Form 10-ID Section 115BAB India, 15% new manufacturing CA, Form 10-ID filing India",
    "desc": "Form 10-ID Section 115BAB (15% new manufacturing concessional tax) election checklist India 2026: strict eligibility (post Oct 2019 incorporation + manufacturing + commenced production + no reconstruction), forfeited deductions, PLI stackability, decision workflow. Working CA guide by Durgesh Chavda.",
})

# Remaining 4 forms + 4 sub-niches - shorter format
# 5. APR Form ODI Part II
PAGES.append({
    "slug": "form-odi-apr-annual-performance-report-india-2026",
    "title": "Form ODI Part II (APR) Annual Report India 2026 Due 31 Dec",
    "hero_em": "overseas investment annual filing.",
    "lead": "Form ODI Part II (APR - Annual Performance Report) is annual FEMA filing by Indian company for its overseas direct investment (ODI): due 31 December each year for FY ended March. Covers overseas subsidiary performance, dividend repatriation, change in investment. Non-filing attracts FEMA Section 13 compounding. Here's the complete 2026 compliance alert.",
    "kicker": "/ FEMA Form Checklist &middot; Updated 2026-10-22",
    "sections_pairs": [
        ("/ Who files + when", "The core rule.",
         "<ul>"
         "<li>Any Indian company that has made overseas direct investment (ODI) in foreign subsidiary / JV / branch.</li>"
         "<li>Must file APR annually by <strong>31 December</strong> for FY ended previous March.</li>"
         "<li>So APR for FY 2025-26 (ended March 2026) due by 31 December 2026.</li>"
         "<li>Via FIRMS portal (RBI) through AD-I category bank.</li>"
         "<li>Non-filing: FEMA Section 13 compounding.</li>"
         "</ul>"),
        ("/ What's in APR", "The data.",
         "<ul>"
         "<li>Foreign subsidiary / JV identification: name, country, incorporation details, business activity.</li>"
         "<li>Share capital + Indian company's ownership %.</li>"
         "<li>Financial highlights: revenue + profit + net worth (audited foreign financials basis).</li>"
         "<li>Dividend received by Indian company during year (if any).</li>"
         "<li>Changes in investment: additions / disposal / dilution during year.</li>"
         "<li>Foreign subsidiary's own compliance status + relevant local filings.</li>"
         "<li>Any pending disputes / litigation.</li>"
         "</ul>"),
        ("/ Common APR issues", "Where companies trip.",
         "<ul>"
         "<li>Multi-year non-filing - cleaner via one consolidated FEMA compounding.</li>"
         "<li>Foreign subsidiary audit not completed by December - APR filing delayed. Provisional APR acceptable.</li>"
         "<li>Dividend received not reflected in Indian company Form 15CA / 15CB coordination.</li>"
         "<li>Change of foreign subsidiary name / registered office not updated in APR.</li>"
         "<li>Foreign subsidiary wound up but Indian company didn't file wind-up ODI Form - continuing APR obligation misreported.</li>"
         "</ul>"
         "<p><em>Last updated: 2026-10-22.</em></p>"),
    ],
    "faqs": [
        ("When is Form ODI Part II (APR) due?",
         "31 December each year for FY ended previous March. So APR for FY 2025-26 due by 31 December 2026."),
        ("What if foreign subsidiary audit not complete?",
         "File provisional APR with unaudited numbers; file revised APR within 30 days of foreign subsidiary audit completion. Acceptable practice; don't delay provisional filing waiting for audit."),
        ("What's the penalty for missed APR?",
         "FEMA Section 13 compounding: typically INR 10,000-50,000 per missed year. Multi-year missed APRs can be consolidated in single compounding application."),
        ("Does BQP file APR for Indian parent of foreign subsidiary?",
         "Yes - standard annual service. Foreign subsidiary financial data collection + APR drafting + FIRMS portal filing + Form 15CA/15CB coordination for dividend repatriation. Also compounding of past missed APRs. WhatsApp +91 78018 87130."),
    ],
    "related_pairs": [("fema-odi-us-entity-indian-founder.html", "Related", "FEMA ODI"),
                      ("fema-compounding-foreign-subsidiary-india.html", "Related", "FEMA Compounding")],
    "cta_h": "Form ODI Part II (APR) due 31 December 2026.",
    "cta_b": "Annual filing for Indian parent of foreign subsidiary. BQP: foreign subsidiary data + APR drafting + FIRMS filing + past missed APR compounding.",
    "keywords": "Form ODI APR India 2026, Annual Performance Report overseas investment, Form ODI Part II due December",
    "desc": "Form ODI Part II (APR - Annual Performance Report) India 2026: annual FEMA filing by Indian parent for overseas subsidiary, due 31 December, foreign subsidiary data + dividend repatriation + change in investment, FEMA Section 13 compounding for missed. Working CA guide by Durgesh Chavda.",
})

# 6. DPT-3 return
PAGES.append({
    "slug": "form-dpt-3-return-of-deposits-india-2026",
    "title": "Form DPT-3 Return of Deposits India 2026 Due 30 June",
    "hero_em": "annual deposit disclosure.",
    "lead": "Form DPT-3 annual return of deposits + exempted deposits (external borrowings) by Indian companies: due 30 June each year for position as at 31 March of same year. Covers loans from directors, inter-corporate loans, promoter contributions, external borrowings. Compliance signal for lenders + regulators. Here's the 2026 filing framework.",
    "kicker": "/ ROC Form Checklist &middot; Updated 2026-10-22",
    "sections_pairs": [
        ("/ Who must file DPT-3", "Companies in scope.",
         "<ul>"
         "<li>All companies (Pvt Ltd + Public Ltd) EXCEPT government companies, banks, NBFCs, insurance, housing finance.</li>"
         "<li>Nil DPT-3 even if no deposits/loans - specific compliance signal.</li>"
         "<li>Position reported as at <strong>31 March</strong> of each year.</li>"
         "<li>Due by <strong>30 June</strong> of the same year.</li>"
         "</ul>"),
        ("/ What's reported", "The categories.",
         "<ul>"
         "<li><strong>Deposits</strong> (Rule 2(1)(c) Companies (Acceptance of Deposits) Rules 2014): loans from public are deposits. Pvt Ltd generally cannot accept deposits from public.</li>"
         "<li><strong>Exempted deposits</strong>: loans from directors + promoters + other companies + banks + financial institutions. These are exempted from deposit rules but reportable in DPT-3.</li>"
         "<li>External Commercial Borrowings (ECB).</li>"
         "<li>Debentures (non-convertible + convertible).</li>"
         "<li>Advance received from customers above specific threshold.</li>"
         "</ul>"),
        ("/ Compliance signal", "Why DPT-3 matters.",
         "<ul>"
         "<li>Shows company's external borrowing / loan structure to regulators + lenders + auditors.</li>"
         "<li>Pre-M&A diligence: buyer reviews DPT-3 history.</li>"
         "<li>Pre-IPO: SEBI reviews DPT-3 for public offering compliance history.</li>"
         "<li>Non-filing: Section 450 default penalty.</li>"
         "<li>Form 3CD Clause 22 tax audit disclosure cross-references DPT-3.</li>"
         "</ul>"
         "<p><em>Last updated: 2026-10-22.</em></p>"),
    ],
    "faqs": [
        ("Is DPT-3 nil return mandatory?",
         "Yes - even if company has no deposits / loans, nil DPT-3 must be filed as compliance signal. Non-filing attracts Section 450 default penalty."),
        ("What's the due date for DPT-3?",
         "30 June each year, reporting position as at 31 March of same year. So DPT-3 for position as at 31 March 2026 due by 30 June 2026."),
        ("Is director loan reported in DPT-3?",
         "Yes - loan from director is 'exempted deposit' under Rule 2(1)(c). Not a 'deposit' from public but reportable in DPT-3. Both the amount + terms disclosed."),
        ("Does BQP file DPT-3 as part of annual compliance?",
         "Yes - integrated with standard annual ROC compliance (AOC-4 + MGT-7 + DPT-3 + MSME Form I + DIR-3 KYC). WhatsApp +91 78018 87130."),
    ],
    "related_pairs": [("company-secretarial-services-india-remote.html", "Related", "CS Services"),
                      ("dir-3-kyc-director-annual-compliance-india.html", "Related", "DIR-3 KYC")],
    "cta_h": "Form DPT-3 annual compliance?",
    "cta_b": "Nil or detailed return + 30 June deadline. BQP integrated annual ROC compliance.",
    "keywords": "Form DPT-3 India 2026, Return of Deposits India, DPT-3 30 June CA, exempted deposits DPT-3",
    "desc": "Form DPT-3 Return of Deposits India 2026: annual filing by companies by 30 June reporting position as at 31 March, covers deposits + exempted deposits (director loans, promoter contributions, ECB, debentures), nil return mandatory. Working CA guide by Durgesh Chavda.",
})

# 7. Form 3CA/3CB/3CD specific
PAGES.append({
    "slug": "form-3ca-3cb-3cd-tax-audit-india-2026-checklist",
    "title": "Form 3CA/3CB/3CD Tax Audit India 2026 Complete Checklist",
    "hero_em": "Section 44AB specific + Clause 44 reconciliation.",
    "lead": "Form 3CA/3CB (auditor's audit report) + Form 3CD (particulars for 44 clauses) under Section 44AB Income Tax: due 31 October each year. Specific attention 2026: Clause 22 Section 43B(h) Year 2 (MSE payment), Clause 44 GST reconciliation. ICAI UDIN mandatory. Here's the complete 2026 tax audit checklist.",
    "kicker": "/ Tax Audit Form Checklist &middot; Updated 2026-10-22",
    "sections_pairs": [
        ("/ Section 44AB tax audit threshold", "Who's in scope.",
         "<ul>"
         "<li>Turnover above <strong>INR 1 crore</strong> (goods) / <strong>INR 50 lakh</strong> (profession) for AY 2026-27.</li>"
         "<li>Business with 95%+ digital receipts: INR 10 crore turnover threshold.</li>"
         "<li>Professional with 95%+ digital receipts: INR 75 lakh threshold.</li>"
         "<li>Section 44AD / 44ADA presumptive scheme + turnover below threshold = exempt.</li>"
         "<li>Due date: 31 October of AY (vs 31 July for non-audit). TP cases 30 November.</li>"
         "</ul>"),
        ("/ Form 3CA vs 3CB", "Which applies.",
         "<ul>"
         "<li><strong>Form 3CA</strong>: for taxpayers who are required to get accounts audited under other law (Companies Act, LLP Act, etc.). Standard audit report + tax audit cross-references under same financial year.</li>"
         "<li><strong>Form 3CB</strong>: for taxpayers audited only for tax audit (not under any other statute). Specific tax-audit-only report.</li>"
         "<li><strong>Form 3CD</strong>: 44-clause particulars common to both 3CA + 3CB.</li>"
         "</ul>"),
        ("/ Clause 22 Section 43B(h) focus", "The year-2 critical clause.",
         "<ul>"
         "<li>Clause 22 expanded post Finance Act 2023 for Section 43B(h) MSE compliance.</li>"
         "<li>Current year disallowance: MSE expense paid beyond 45 days.</li>"
         "<li>Prior year reversal: MSE expense disallowed in prior year, paid during current year - allowed as deduction in current year.</li>"
         "<li>Udyam certificate collection + aging + Section 15 MSMED interest documentation.</li>"
         "<li>Cross-reference with MSME Form I half-yearly ROC filing.</li>"
         "</ul>"),
        ("/ Clause 44 GST reconciliation focus", "The IT-GST interface.",
         "<ul>"
         "<li>Clause 44 reconciles Income Tax turnover with GST turnover (GSTR-1 + GSTR-9).</li>"
         "<li>Common adjustments: credit notes / debit notes timing, exempt supplies, year-end sales returns, discounts, FX for exports.</li>"
         "<li>Narrative explanation for each unreconciled item.</li>"
         "<li>Feeds into GSTR-9 Reconciliation (31 December).</li>"
         "<li>ICAI 2024 guidance on Clause 44 methodology.</li>"
         "</ul>"),
        ("/ ICAI UDIN", "The audit identifier.",
         "<ul>"
         "<li>UDIN (Unique Document Identification Number) mandatory for every CA audit report + certificate.</li>"
         "<li>Generated on ICAI portal before signing + attached to Form 3CA/3CB.</li>"
         "<li>Verifies CA membership + prevents misuse of CA signature.</li>"
         "<li>UDIN check against ICAI records part of post-filing verification.</li>"
         "</ul>"
         "<p><em>Last updated: 2026-10-22.</em></p>"),
    ],
    "faqs": [
        ("What's the tax audit turnover threshold for AY 2026-27?",
         "INR 1 crore (goods) / INR 50 lakh (profession) standard. INR 10 crore (goods) / INR 75 lakh (profession) if 95%+ digital receipts. Section 44AD / 44ADA presumptive scheme + turnover below threshold = exempt."),
        ("What's Clause 22 of Form 3CD?",
         "Post Finance Act 2023 expansion: specific disclosure of Section 43B(h) MSE expense disallowance in current year + prior year reversal when paid during current year. Udyam certificate collection + 45-day aging + Section 15 MSMED interest. Cross-references MSME Form I half-yearly ROC filing."),
        ("What's Clause 44 Form 3CD GST reconciliation?",
         "Reconciliation of Income Tax turnover with GST turnover (GSTR-1 + GSTR-9). Common adjustments: credit notes timing, exempt supplies, year-end returns, discounts, FX exports. Narrative explanation for each unreconciled item. ICAI 2024 guidance clarifies methodology."),
        ("Is UDIN mandatory on Form 3CA/3CB?",
         "Yes - ICAI UDIN mandatory for every CA audit report + certificate since 2019. Generated on ICAI portal before signing + attached to Form 3CA/3CB. UDIN verifiable by taxpayer + tax authority against ICAI records."),
        ("What's the late fee for missing 31 October tax audit?",
         "Section 234F late ITR filing fee + Section 271B penalty for late tax audit: 0.5% of turnover or INR 1,50,000 whichever lower. ITR filing blocked until Form 3CA/3CB linked on portal. Section 148A show-cause risk from AO."),
        ("Does BQP conduct tax audit + file Form 3CA/3CB/3CD?",
         "Yes - standard engagement. CA Durgesh Chavda personally signs tax audit reports as ICAI-qualified CA. Full 44-clause Form 3CD + Form 3CA/3CB + UDIN + ITR coordination. Priority turnaround in October 2026 tax audit window. WhatsApp +91 78018 87130."),
    ],
    "related_pairs": [("tax-audit-season-november-2026-post-filing-followups.html", "Related", "Tax Audit Post-Filing"),
                      ("ay-2026-27-itr-forms-new-disclosures-india.html", "Related", "AY 2026-27 ITR")],
    "cta_h": "Tax audit threshold crossed? Form 3CA/3CB/3CD + UDIN due 31 October.",
    "cta_b": "44-clause Form 3CD + Clause 22 Section 43B(h) + Clause 44 GST reconciliation + UDIN + ITR coordination. BQP standard annual tax audit engagement.",
    "keywords": "Form 3CA 3CB 3CD tax audit India 2026, Section 44AB tax audit CA, Clause 22 Section 43B(h) CA, Clause 44 GST reconciliation CA",
    "desc": "Form 3CA/3CB/3CD tax audit India AY 2026-27 complete checklist: Section 44AB threshold, 44 clauses, Clause 22 Section 43B(h) MSE, Clause 44 GST reconciliation, ICAI UDIN, 31 October deadline. Working CA guide by Durgesh Chavda.",
})

# 8. Form 3CEB TP audit
PAGES.append({
    "slug": "form-3ceb-tp-audit-india-2026-30-november-checklist",
    "title": "Form 3CEB TP Audit India 2026 Due 30 November Checklist",
    "hero_em": "transfer pricing audit specific.",
    "lead": "Form 3CEB transfer pricing audit certificate: due 30 November 2026 for AY 2026-27. Mandatory for any Indian entity with international transactions above INR 1 crore (effectively every foreign-subsidiary subsidiary). Benchmarking study + Section 92D documentation underlying. Here's the complete 2026 Form 3CEB checklist.",
    "kicker": "/ TP Audit Form Checklist &middot; Updated 2026-10-22",
    "sections_pairs": [
        ("/ Who must file Form 3CEB", "Scope.",
         "<ul>"
         "<li>Any Indian company / entity with international transactions above <strong>INR 1 crore</strong> in aggregate in the FY.</li>"
         "<li>International transaction = transaction between Associated Enterprises (26%+ shareholding or common control) crossing border + affects profit / income / loss / assets.</li>"
         "<li>Effectively every Indian subsidiary of foreign parent (any related-party transaction triggers).</li>"
         "<li>Specified Domestic Transactions also in scope: specific tax-holiday / 115BAB-type entities.</li>"
         "<li>Due date: <strong>30 November 2026</strong> for AY 2026-27 (one month after standard tax audit).</li>"
         "</ul>"),
        ("/ Form 3CEB content", "The 24 clauses.",
         "<ul>"
         "<li>Entity details + nature of business + Associated Enterprise relationship chain.</li>"
         "<li>Each international transaction: nature + volume + value in INR + currency.</li>"
         "<li>Transaction categories: goods, services, intangibles, financing, cost allocation, business restructuring.</li>"
         "<li>Arm's-length method chosen per transaction: CUP / RPM / Cost Plus / TNMM / PSM / Other.</li>"
         "<li>Comparable set + arm's-length range.</li>"
         "<li>Material facts specific to the transaction.</li>"
         "<li>Methodology justification.</li>"
         "<li>CA signature + UDIN.</li>"
         "</ul>"),
        ("/ Underlying Section 92D documentation", "What's maintained but not filed.",
         "<ul>"
         "<li><strong>Section 92D</strong> + Rule 10D: comprehensive TP documentation to be maintained (not filed but produced on scrutiny).</li>"
         "<li>Entity profile + industry analysis + functional analysis + economic analysis + benchmarking study.</li>"
         "<li>Must be contemporaneous (prepared by Form 3CEB filing date, not after scrutiny).</li>"
         "<li>Updated annually.</li>"
         "<li>Preserved 8+ years.</li>"
         "</ul>"),
        ("/ Master File + CbCR (if applicable)", "The BEPS layer.",
         "<ul>"
         "<li><strong>Master File (Form 3CEAA)</strong>: if group consolidated revenue > INR 500 crore + international transactions > INR 50 crore (or intangible > INR 10 crore). Due 30 November same as Form 3CEB.</li>"
         "<li><strong>CbCR (Form 3CEAD)</strong>: if ultimate parent of group with consolidated revenue > INR 6,400 crore (~EUR 750M, BEPS Action 13).</li>"
         "<li><strong>Form 3CEAC</strong>: secondary notification by Indian subsidiary if ultimate parent country has no CbCR regime.</li>"
         "<li>Due dates vary - typically 12-15 months from FY-end.</li>"
         "</ul>"
         "<p><em>Last updated: 2026-10-22.</em></p>"),
    ],
    "faqs": [
        ("When is Form 3CEB due for AY 2026-27?",
         "30 November 2026. One month after standard tax audit deadline (31 October). Specific extended deadline for TP audit cases."),
        ("What's the INR 1 crore threshold for Form 3CEB?",
         "Aggregate international transactions (goods + services + intangibles + financing + cost allocation + business restructuring with Associated Enterprises) above INR 1 crore in the FY. Effectively every foreign-subsidiary Indian company triggers."),
        ("What's the penalty for missing Form 3CEB?",
         "Section 271BA: INR 1,00,000 penalty for non-filing or incomplete Form 3CEB. Section 234F ITR late fee. ITR filing blocked until Form 3CEB linked."),
        ("Does Form 3CEB alone suffice or do I need Section 92D documentation?",
         "Both. Form 3CEB is the auditor's certificate filed with ITR. Section 92D documentation (entity profile + industry analysis + functional analysis + benchmarking) is maintained + produced on scrutiny. Rule 10D specifies contents. Must be contemporaneous."),
        ("When is Master File + CbCR required?",
         "Master File (Form 3CEAA) if group consolidated revenue > INR 500 crore + aggregate international transactions > INR 50 crore (or intangible-related > INR 10 crore). CbCR (Form 3CEAD) for ultimate parent of group with consolidated revenue > INR 6,400 crore (~EUR 750M). Due 30 November for Master File; 12-15 months for CbCR."),
        ("Does BQP handle Form 3CEB + benchmarking study + Master File + CbCR?",
         "Yes - full TP compliance stack. Form 3CEB + benchmarking (TNMM / RPM / CUP / Cost Plus / PSM method) + Section 92D documentation + Master File + CbCR + BEPS Pillar 2 integration. For Indian subsidiaries of foreign MNC groups. WhatsApp +91 78018 87130."),
    ],
    "related_pairs": [("transfer-pricing-india-foreign-mnc.html", "Related", "TP for Foreign MNC"),
                      ("beps-pillar-2-india-implementation-october-2026-update.html", "Related", "BEPS Pillar 2")],
    "cta_h": "Indian subsidiary with international transactions > INR 1 crore?",
    "cta_b": "Form 3CEB + benchmarking + Section 92D + Master File + CbCR + BEPS Pillar 2. 30 November deadline. BQP full TP stack.",
    "keywords": "Form 3CEB TP audit India 2026, Transfer Pricing audit 30 November, Form 3CEB benchmarking CA, Section 92D documentation CA",
    "desc": "Form 3CEB TP audit India AY 2026-27 due 30 November 2026: INR 1 crore threshold, arm's-length methods (CUP/RPM/Cost Plus/TNMM/PSM), Section 92D documentation, Master File (Form 3CEAA), CbCR (Form 3CEAD), BEPS Pillar 2 integration. Working CA guide by Durgesh Chavda.",
})

# 4 sub-niche sector pages
PAGES.append({
    "slug": "best-ca-b2b-saas-startup-india-2026",
    "title": "Best CA for B2B SaaS Startup India 2026",
    "hero_em": "enterprise SaaS specialist.",
    "lead": "B2B SaaS startup faces distinct issues from consumer SaaS: enterprise contract + billing complexity, longer sales cycles, net dollar retention cohort reporting, custom MSAs with each customer, Section 194J B2B TDS, Section 194Q + 206C(1H) B2B TCS. BQP B2B SaaS specialist practice navigates all. Here's the framework.",
    "kicker": "/ B2B SaaS Specialist &middot; Updated 2026-10-22",
    "sections_pairs": [
        ("/ B2B SaaS specific issues", "Where general SaaS CA misses depth.",
         "<ul>"
         "<li>Enterprise contract complexity: custom MSA, multi-year prepaid, specific SLA + usage-based pricing + volume discount tiers.</li>"
         "<li>Deferred revenue + ASC 606 performance obligation across multi-year prepaid contracts.</li>"
         "<li>Section 194J TDS on B2B professional services + 194Q TDS on goods component (if integrated).</li>"
         "<li>Net Dollar Retention (NDR) cohort reporting for investors - revenue retention + expansion vs churn.</li>"
         "<li>Revenue recognition for implementation / professional services bundled with subscription (ASC 606 performance obligation separation).</li>"
         "<li>GST 18% + export of service LUT bond for foreign enterprise customers.</li>"
         "<li>Transfer pricing (Form 3CEB) if India R&D / sales entity serves foreign HQ customers.</li>"
         "<li>Section 115BAA (22% services rate) opt-in decision.</li>"
         "</ul>"),
        ("/ Our scope for B2B SaaS", "The complete offering.",
         "<ul>"
         "<li>ASC 606 / Ind AS 115 revenue recognition framework for complex B2B contracts.</li>"
         "<li>Deferred revenue accounting + variable consideration tracking.</li>"
         "<li>GST + export of service LUT bond + ITC refund.</li>"
         "<li>Section 194J + 194Q + 206C(1H) framework.</li>"
         "<li>NDR / GRR / cohort unit economics + investor reporting pack.</li>"
         "<li>Transfer pricing + Form 3CEB for India entity serving foreign customers.</li>"
         "<li>Section 115BAA opt-in.</li>"
         "<li>ESOP + 409A + Rule 11UA for high-valuation B2B SaaS.</li>"
         "<li>Fundraising + FEMA FDI compliance.</li>"
         "</ul>"
         "<p><em>Last updated: 2026-10-22.</em></p>"),
    ],
    "faqs": [
        ("How is B2B SaaS different from consumer SaaS for CA?",
         "B2B has longer sales cycles + larger contract values + multi-year prepaid + enterprise MSA complexity + NDR cohort reporting + ASC 606 performance obligation separation. Consumer SaaS is more about monthly billing + OIDAR GST for Indian B2C + simpler revenue recognition. Different compliance focus."),
        ("Does OIDAR GST apply to B2B SaaS?",
         "No - OIDAR applies to B2C (sale to non-GST-registered Indian consumer). For B2B (sale to GST-registered Indian business customer), reverse charge mechanism applies - Indian customer self-assesses GST. Foreign B2B SaaS to Indian B2B customer: no OIDAR; capture Indian customer's GSTIN at checkout."),
        ("Can B2B SaaS claim export of service for foreign enterprise customers?",
         "Yes - under GST rules, service provided to foreign customer (place of supply outside India, payment in forex) is zero-rated export. LUT bond allows invoicing without IGST; ITC can be refunded on inputs. Significant tax benefit for Indian B2B SaaS serving US / UK / EU customers."),
        ("Does BQP handle B2B SaaS specific compliance?",
         "Yes - specialist practice. ASC 606 revenue recognition + GST export of service + transfer pricing + Section 194J/194Q + NDR reporting + ESOP + fundraising. Standard engagement for Series A to Series C B2B SaaS. WhatsApp +91 78018 87130."),
    ],
    "related_pairs": [("best-ca-saas-startup-india-2026.html", "Related", "Best CA for SaaS"),
                      ("transfer-pricing-india-foreign-mnc.html", "Related", "Transfer Pricing")],
    "cta_h": "B2B SaaS startup with complex enterprise contracts?",
    "cta_b": "ASC 606 + export of service LUT + transfer pricing + Section 194J/194Q + NDR + ESOP. BQP B2B SaaS specialist practice.",
    "keywords": "best CA B2B SaaS India, enterprise SaaS CA 2026, ASC 606 B2B CA, B2B SaaS GST export CA",
    "desc": "Best CA for B2B SaaS startup India 2026: enterprise contract + ASC 606 revenue recognition, GST export of service LUT bond, Section 194J/194Q/206C(1H), Transfer Pricing Form 3CEB, Net Dollar Retention cohort reporting, ESOP 409A + Rule 11UA. CA Durgesh Chavda specialist practice.",
})

PAGES.append({
    "slug": "best-ca-fintech-lending-nbfc-india-2026",
    "title": "Best CA for Fintech Lending / NBFC India 2026",
    "hero_em": "NBFC licence + lending compliance specialist.",
    "lead": "Fintech lending platforms + NBFCs face distinct regulatory stack beyond generic fintech: NBFC-ND / NBFC-SI / NBFC-MFI / NBFC-ICC licence framework, RBI lending guidelines, FLDG (First Loss Default Guarantee) framework, co-lending arrangements, Digital Lending Guidelines (September 2022), DPDP + financial sector overlay. Here's the BQP fintech lending framework.",
    "kicker": "/ Fintech Lending Specialist &middot; Updated 2026-10-22",
    "sections_pairs": [
        ("/ The lending regulatory stack", "Specific layers.",
         "<ul>"
         "<li>NBFC licence category: ND (Non-Deposit taking), SI (Systemically Important), MFI (Microfinance), ICC (Investment and Credit Company), AFC (Asset Finance Company), ICNBFC (Infrastructure Finance).</li>"
         "<li>Minimum net worth: INR 2-10 crore depending on category.</li>"
         "<li>RBI Scale-Based Regulation (SBR) framework: NBFC-ML (Middle Layer) / NBFC-UL (Upper Layer) classification + specific requirements.</li>"
         "<li>Digital Lending Guidelines (September 2022): disclosure + fair practices + first-loss default guarantee (FLDG) framework + collection mechanisms + grievance redressal.</li>"
         "<li>Co-lending arrangements: NBFC + Bank co-lending framework specific regulatory structure.</li>"
         "<li>Priority sector lending obligations for banks + NBFC-MFI classification for microfinance.</li>"
         "<li>Capital adequacy ratio (CAR) + Tier 1 / Tier 2 capital.</li>"
         "<li>Asset classification + provisioning (NPA framework).</li>"
         "</ul>"),
        ("/ Our scope for fintech lending", "Complete offering.",
         "<ul>"
         "<li>NBFC licence application + category selection + 6-12 month RBI approval process.</li>"
         "<li>Scale-Based Regulation (SBR) classification + ongoing compliance.</li>"
         "<li>Digital Lending Guidelines compliance + FLDG framework structuring.</li>"
         "<li>Co-lending agreement + regulatory structuring with partner bank.</li>"
         "<li>Loan book accounting + Ind AS 109 Expected Credit Loss (ECL) model.</li>"
         "<li>Capital adequacy + provisioning + NPA framework.</li>"
         "<li>DPDP + sector overlay for borrower data.</li>"
         "<li>Account Aggregator (AA) integration as FIU.</li>"
         "<li>Section 194A TDS on interest paid to depositors (if applicable).</li>"
         "<li>GST 18% on service fees + ITC optimisation.</li>"
         "</ul>"
         "<p><em>Last updated: 2026-10-22.</em></p>"),
    ],
    "faqs": [
        ("What's the minimum net worth for NBFC licence?",
         "Varies by category: NBFC-ND INR 2 crore minimum; NBFC-MFI INR 5 crore (urban) / INR 2 crore (rural); NBFC-ICC INR 2 crore. Scale-Based Regulation (SBR) framework may require higher net worth for Middle Layer / Upper Layer NBFCs."),
        ("What's Digital Lending Guidelines September 2022?",
         "RBI framework for digital lending by NBFCs + banks + regulated entities. Key provisions: borrower disclosure, grievance redressal, Loan Service Provider (LSP) + Lending Service Provider (LSP) categories, First Loss Default Guarantee (FLDG) restrictions, data privacy + storage, collection mechanisms."),
        ("What's co-lending framework?",
         "RBI framework (2020) allowing NBFCs + banks to jointly originate loans with pre-defined risk sharing. Bank funds priority sector lending via NBFC's distribution. Specific accounting + regulatory requirements per co-lending agreement."),
        ("Does BQP handle NBFC licence application + ongoing compliance?",
         "Yes - specialist fintech lending practice. NBFC licence (ND / SI / MFI / ICC / AFC / IFC) application + 6-12 month RBI approval + Digital Lending Guidelines + FLDG + co-lending structuring + Ind AS 109 ECL model + capital adequacy + ongoing compliance. WhatsApp +91 78018 87130."),
    ],
    "related_pairs": [("best-ca-fintech-india-2026.html", "Related", "Best CA for Fintech"),
                      ("india-account-aggregator-aa-foreign-fintech.html", "Related", "Account Aggregator")],
    "cta_h": "Fintech lending / NBFC startup?",
    "cta_b": "NBFC licence + Digital Lending Guidelines + FLDG + co-lending + Ind AS 109 ECL + capital adequacy. BQP specialist practice.",
    "keywords": "best CA NBFC India 2026, fintech lending CA India, Digital Lending Guidelines CA, NBFC licence CA India, co-lending CA India",
    "desc": "Best CA for fintech lending / NBFC India 2026: NBFC licence (ND/SI/MFI/ICC/AFC/IFC) + RBI Scale-Based Regulation (SBR) + Digital Lending Guidelines Sept 2022 + FLDG + co-lending + Ind AS 109 ECL + capital adequacy. CA Durgesh Chavda specialist practice.",
})

PAGES.append({
    "slug": "best-ca-d2c-fashion-apparel-india-2026",
    "title": "Best CA for D2C Fashion / Apparel India 2026",
    "hero_em": "high-return rate + inventory specialist.",
    "lead": "D2C Fashion / Apparel brands face unique CA issues: high return rate (20-40% typical) + sales return GST handling + inventory obsolescence provisions + credit note treatment + 18% GST on garments + Section 206C(1H) TCS on sales + marketplace vs direct website GST + Section 194-O marketplace TDS. BQP D2C fashion specialist practice. Here's the framework.",
    "kicker": "/ D2C Fashion / Apparel Specialist &middot; Updated 2026-10-22",
    "sections_pairs": [
        ("/ D2C fashion specific issues", "Where general D2C CA misses depth.",
         "<ul>"
         "<li>High return rate (20-40%): credit note GST + Income Tax treatment + revenue recognition timing.</li>"
         "<li>Inventory obsolescence: fashion cycle 60-90 days; year-end stock write-down.</li>"
         "<li>Sales return accounting: ASC 606 variable consideration vs direct reversal.</li>"
         "<li>Garment GST: 12% / 18% / 28% (ready-made garments 18%; fabric 12%; luxury 28%).</li>"
         "<li>Marketplace (Myntra / Amazon Fashion / Flipkart) vs direct website: Section 194-O TDS vs 206C(1H) TCS different.</li>"
         "<li>Returns / COD orders handling: specific GST + accounting treatment.</li>"
         "<li>Multi-state logistics + e-way bill compliance.</li>"
         "<li>Private label vs white-label: GST classification + customs duty for imported finished goods.</li>"
         "</ul>"),
        ("/ Our scope for D2C fashion", "Complete offering.",
         "<ul>"
         "<li>GST classification by HSN + rate confirmation (ready-made garments, fabric, accessories, luxury).</li>"
         "<li>Returns + credit note GST + Income Tax treatment.</li>"
         "<li>Inventory obsolescence provision + year-end stock take.</li>"
         "<li>Section 206C(1H) TCS on direct sales + Section 194-O on marketplace.</li>"
         "<li>Multi-state logistics + e-way bill compliance.</li>"
         "<li>ASC 606 / Ind AS 115 revenue recognition with returns.</li>"
         "<li>Working capital advisory: receivables + inventory + payables (very specific for D2C).</li>"
         "<li>Customs duty on imported fabric / finished garments + FTA preferential rate (UAE CEPA, Bangladesh LDC).</li>"
         "<li>Fundraising support: unit economics (contribution margin, CM1, CM2, CM3) for investor pitch.</li>"
         "</ul>"
         "<p><em>Last updated: 2026-10-22.</em></p>"),
    ],
    "faqs": [
        ("What's the GST rate on fashion / apparel in India?",
         "Ready-made garments: 18%. Fabric / cloth: 12%. Luxury / designer segment: 28% (plus cess for very high-value). Specific HSN classification affects rate - common area of GST classification disputes."),
        ("How is sales return GST handled?",
         "Credit note under Section 34 CGST Act: supplier issues credit note; GST reversal in both parties' records. Timing: in month of credit note issue. ASC 606 revenue recognition: 'expected value' of returns provisioned at sale; actual returns reconciled against provision. Material impact on P&L for 20-40% return rate D2C fashion."),
        ("Marketplace vs direct website - how does GST + TDS differ?",
         "Marketplace: Section 194-O 1% TDS on gross receipts (e-commerce operator deducts). Section 52 TCS by marketplace. Seller gets net of these. Direct website: Section 206C(1H) 0.1% TCS by seller (if turnover + sales thresholds crossed). GST handling slightly different."),
        ("Does BQP handle D2C fashion-specific GST + accounting?",
         "Yes - specialist D2C fashion practice. Returns + credit note handling, inventory obsolescence, GST classification + rate, marketplace vs direct website compliance, unit economics for fundraising, multi-state logistics. WhatsApp +91 78018 87130."),
    ],
    "related_pairs": [("best-ca-d2c-ecommerce-india-2026.html", "Related", "Best CA for D2C"),
                      ("section-206c-1h-tcs-sale-goods-india.html", "Related", "Section 206C(1H)")],
    "cta_h": "D2C fashion / apparel brand?",
    "cta_b": "Returns + credit notes + inventory obsolescence + GST + 194-O / 206C(1H) + unit economics. BQP D2C fashion specialist practice.",
    "keywords": "best CA D2C fashion India, apparel brand CA India, D2C fashion returns GST CA, marketplace vs direct website CA",
    "desc": "Best CA for D2C fashion / apparel India 2026: high return rate + credit note GST + inventory obsolescence + 12%/18%/28% garment GST + marketplace vs direct website compliance + Section 194-O / 206C(1H) + unit economics for fundraising. CA Durgesh Chavda specialist practice.",
})

PAGES.append({
    "slug": "best-ca-saas-cfo-services-india-foreign-startup",
    "title": "Best CA for SaaS CFO Services India (Foreign Startup)",
    "hero_em": "US HQ + Indian operations vCFO.",
    "lead": "Foreign (US / UK / Singapore / UAE HQ) SaaS startup with Indian operations (engineering + support + sales) needs integrated vCFO: monthly MIS consolidation + ASC 606 revenue recognition + ARR cohort reporting + Transfer Pricing (Form 3CEB) + Indian compliance stack + fundraising prep + board reporting. BQP specialist SaaS CFO services. Here's the framework.",
    "kicker": "/ SaaS vCFO for Foreign HQ &middot; Updated 2026-10-22",
    "sections_pairs": [
        ("/ The integrated vCFO scope", "Beyond individual services.",
         "<ul>"
         "<li>Monthly MIS: Indian entity + consolidated with US HQ. ARR / MRR / NDR / GRR / cohort unit economics.</li>"
         "<li>ASC 606 (US GAAP) revenue recognition for US HQ parent + Ind AS 115 reconciliation for Indian subsidiary.</li>"
         "<li>Transfer Pricing (Form 3CEB) + benchmarking study for Indian entity-to-US parent transactions.</li>"
         "<li>Indian subsidiary annual audit + FEMA FC-GPR + FLA Return.</li>"
         "<li>FP&A: 3-5 year model + fundraising preparation.</li>"
         "<li>Board reporting pack: cohort analysis + CAC payback + burn multiple + magic number.</li>"
         "<li>Audit coordination: BQP as Indian audit + Big-4 group audit integration.</li>"
         "<li>Expense + revenue flow across entities: US direct + India subsidiary + Singapore IP holding (if applicable).</li>"
         "<li>Treasury: FX hedging across INR / USD operations.</li>"
         "</ul>"),
        ("/ Why integrated vCFO matters", "Avoid firm coordination gaps.",
         "<ul>"
         "<li>US CPA for Form 1120 / 1040 but doesn't understand Indian TP / FEMA.</li>"
         "<li>Indian CA for Indian compliance but doesn't integrate with US GAAP consolidation.</li>"
         "<li>Separate vCFO firm for strategic finance but needs data from CA / CPA.</li>"
         "<li>BQP integrates: Indian compliance + vCFO strategic + US GAAP reconciliation + Transfer Pricing + Board reporting.</li>"
         "<li>Co-ordinated with US CPA for US GAAP consolidation.</li>"
         "<li>Single India point of contact for US HQ CFO / Founder.</li>"
         "</ul>"
         "<p><em>Last updated: 2026-10-22.</em></p>"),
    ],
    "faqs": [
        ("How does BQP vCFO work for US HQ'd foreign SaaS?",
         "Monthly cadence: BQP delivers Indian entity MIS + consolidation adjustments + Transfer Pricing accrual + Indian compliance tracking. US CPA handles US GAAP consolidation + Form 1120. BQP integrates on quarterly basis + annual audit + fundraising prep. Weekly / bi-weekly status call with Indian team."),
        ("Does BQP handle both Indian audit + US GAAP consolidation input?",
         "Yes - Indian statutory audit (Companies Act 2013 + Ind AS 115) + reconciliation to US GAAP (ASC 606) + feed to US CPA for Form 1120 consolidation. Standard output: Ind AS financials + Ind AS to US GAAP reconciliation schedule + consolidation-ready data."),
        ("What's the scope of fundraising support?",
         "Pre-funding: 3-5 year model + unit economics (ARR / MRR / NDR / cohort / burn / runway) + investor pitch finance pages + Q&A support during due diligence. Post-funding: FEMA FC-GPR + FDI pricing + ongoing MIS + burn tracking + runway monitoring."),
        ("Does BQP coordinate with Big-4 group audit for US HQ?",
         "Yes - common structure. US HQ engages Big-4 for US GAAP consolidation audit; Indian subsidiary engages BQP for Indian statutory + TP + ongoing. BQP delivers to Big-4 team: Indian financials in US GAAP format + supporting workpapers + Transfer Pricing documentation. WhatsApp +91 78018 87130."),
    ],
    "related_pairs": [("virtual-cfo-india-foreign-company.html", "Related", "vCFO for Foreign Company"),
                      ("best-ca-saas-startup-india-2026.html", "Related", "Best CA for SaaS")],
    "cta_h": "US / UK / Singapore HQ foreign SaaS with Indian operations?",
    "cta_b": "Integrated vCFO: Indian compliance + US GAAP consolidation + TP + fundraising + board reporting. BQP + US CPA coordination.",
    "keywords": "best CA SaaS vCFO foreign startup India, foreign SaaS CFO services India CA, US HQ India subsidiary vCFO",
    "desc": "Best CA for SaaS CFO services India for foreign startups (US / UK / Singapore / UAE HQ): integrated vCFO covering Indian subsidiary MIS + ASC 606 / Ind AS 115 reconciliation + Transfer Pricing Form 3CEB + fundraising prep + board reporting + Big-4 coordination. CA Durgesh Chavda specialist practice.",
})

# Build all pages
for p in PAGES:
    html = quick_page(
        slug=p["slug"],
        title=p["title"],
        hero_em=p["hero_em"],
        lead=p["lead"],
        kicker=p["kicker"],
        sections_pairs=p["sections_pairs"],
        faqs=p["faqs"],
        related_pairs=p["related_pairs"],
        cta_h=p["cta_h"],
        cta_b=p["cta_b"],
        keywords=p["keywords"],
        desc=p["desc"],
    )
    write_page(p["slug"], html)

print(f"Batch T complete: {len(PAGES)} pages written")
