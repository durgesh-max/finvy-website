# -*- coding: utf-8 -*-
"""Batch X: Round 8 - 10 pages. GSTR-9 pre-filing + MAT/AMT + 10BA + state registrations + narrow positioning."""
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


PAGES = [
    {
        "slug": "gstr-9-pre-filing-audit-checklist-december-2026",
        "title": "GSTR-9 Pre-Filing Audit Checklist December 2026",
        "hero_em": "catch reconciliation gaps before filing.",
        "lead": "GSTR-9 FY 2024-25 due 31 December 2026. Pre-filing audit catches reconciliation gaps before submission - preventing scrutiny notices + enabling optimal position. Four-week pre-filing audit framework covering GSTR-1 vs 3B, 3B vs 2B, books vs GST, Section 17(5) blocked ITC, Section 16(4) time-barred, HSN summary, GSTR-9C reconciliation. Working CA checklist by Durgesh Chavda.",
        "kicker": "/ GSTR-9 Pre-Filing Audit &middot; Updated 2026-10-22",
        "sections_pairs": [
            ("/ Why pre-filing audit matters", "Prevent ASMT-10 notices.",
             "<ul>"
             "<li>GSTR-9 is reconciliation statement - not fresh declaration. Mistakes surface as discrepancies in ASMT-10 (notice of discrepancy under Section 61) within 1-2 years of filing.</li>"
             "<li>Pre-filing audit catches: GSTR-1 vs 3B gaps, 3B ITC vs 2B shortfalls, Section 17(5) blocked ITC claimed, Section 16(4) time-barred ITC, HSN summary mismatches with trade pattern, books vs GST turnover differences.</li>"
             "<li>Enables: amendment of prior-period GST returns before year-end, voluntary disclosure under Section 73 (10% penalty / INR 10K whichever higher) vs reactive 100% penalty under Section 74.</li>"
             "<li>GSTR-9C (if turnover > INR 5 crore): CA audit of reconciliation. Self-certified since FY 2020-21 but still complex.</li>"
             "</ul>"),
            ("/ 4-week pre-filing audit framework", "Phased approach.",
             "<p><strong>Week 1: Data extraction + reconciliation setup</strong></p>"
             "<ul>"
             "<li>Export GSTR-1 for all 12 months.</li>"
             "<li>Export GSTR-3B for all 12 months.</li>"
             "<li>Download GSTR-2B for all 12 months.</li>"
             "<li>Export books of accounts turnover + GST ledger.</li>"
             "<li>Compile vendor master + their GSTIN.</li>"
             "<li>Compile Section 17(5) analysis for ITC blocks.</li>"
             "</ul>"
             "<p><strong>Week 2: Four reconciliations</strong></p>"
             "<ul>"
             "<li>GSTR-1 vs 3B turnover reconciliation. Document each adjustment.</li>"
             "<li>GSTR-3B ITC vs 2B available ITC. Document shortfall / excess + reasons.</li>"
             "<li>Books vs GSTR-9 turnover. Document credit notes / debit notes timing + year-end adjustments.</li>"
             "<li>Section 17(5) blocked ITC review - must reverse via Table 7 with Section 50 interest.</li>"
             "</ul>"
             "<p><strong>Week 3: Table-by-Table preparation + Section 16(4) review</strong></p>"
             "<ul>"
             "<li>GSTR-9 Table 4 (supplies on which tax is payable) + Table 5 (not payable).</li>"
             "<li>Table 6 (ITC availed) + Table 7 (ITC reversed/ineligible).</li>"
             "<li>Table 8 (ITC per 2B vs 3B claimed).</li>"
             "<li>Table 9 (tax paid).</li>"
             "<li>Tables 10-14 (amendments, demand, refund).</li>"
             "<li>Tables 15-16 (HSN-wise summary) - must match actual trade pattern.</li>"
             "<li>Section 16(4) time-barred ITC: for FY 2024-25, maximum claim window closed with earlier of (a) October 2025 3B filing or (b) GSTR-9 filing date. Missed ITC permanently lost.</li>"
             "</ul>"
             "<p><strong>Week 4: GSTR-9C (if applicable) + voluntary disclosure</strong></p>"
             "<ul>"
             "<li>GSTR-9C Part II - turnover reconciliation books vs GSTR-9.</li>"
             "<li>Part III - taxable supplies reconciliation.</li>"
             "<li>Part IV - ITC reconciliation books vs GSTR-9 Table 6.</li>"
             "<li>Part V - reasons for unreconciled items.</li>"
             "<li>Voluntary disclosure strategy: if material under-payment identified, DRC-03 with 10% penalty / INR 10K (Section 73 non-fraud) vs waiting for notice under Section 74 (100% penalty).</li>"
             "</ul>"),
            ("/ Common pre-filing audit findings", "Where companies trip.",
             "<ul>"
             "<li><strong>GSTR-1 vs 3B gap</strong>: credit notes issued in subsequent FY but booked in current FY. Timing adjustment via GSTR-9 narrative.</li>"
             "<li><strong>3B ITC > 2B available</strong>: vendors who didn't file GSTR-1. Chase vendors or reverse ITC with Section 50 interest.</li>"
             "<li><strong>Section 17(5) blocked ITC claimed</strong>: ITC on motor vehicles (personal), construction materials for own-building, food/beverage, personal insurance - must reverse Table 7.</li>"
             "<li><strong>Section 16(4) missed window</strong>: ITC not claimed in GSTR-3B within window - permanently lost. Lesson for FY 2025-26 forward tracking.</li>"
             "<li><strong>HSN summary mismatch</strong>: Table 15/16 HSN pattern doesn't match actual trade - specific scrutiny trigger.</li>"
             "<li><strong>RCM supplies not declared</strong>: specific services under reverse charge mechanism not disclosed - Section 73 exposure.</li>"
             "<li><strong>Books turnover > GSTR-9 turnover</strong>: unreported sales. Materially significant - voluntary disclosure urgent.</li>"
             "</ul>"
             "<p><em>Last updated: 2026-10-22.</em></p>"),
        ],
        "faqs": [
            ("When should GSTR-9 pre-filing audit start?",
             "At least 60 days before 31 December 2026 deadline. So from end of October / early November 2026. 4-week audit framework fits comfortably. Earlier is better - allows time for voluntary disclosure under DRC-03 before year-end + prior-period GSTR amendments if needed."),
            ("What's the voluntary disclosure benefit?",
             "DRC-03 voluntary disclosure under Section 73 (non-fraud): 10% penalty OR INR 10,000 whichever higher. Compared to waiting for notice under Section 74 (fraud): 100% penalty + interest. Pre-filing audit identification + voluntary disclosure materially cheaper than reactive compliance under notice."),
            ("How long does GSTR-9 pre-filing audit take?",
             "4 weeks typical for companies with INR 10-100 crore turnover. 2-3 weeks for smaller companies. 6-8 weeks for complex multi-location + multi-GSTIN groups. Timing: start by early November to comfortably hit 31 December deadline + enable voluntary disclosure window."),
            ("Does GSTR-9C still need CA certification?",
             "No - from FY 2020-21 onwards GSTR-9C is self-certified (CA certification requirement removed). But reconciliation complexity remains - most taxpayers still engage CA for GSTR-9C preparation given technical depth. BQP standard engagement includes GSTR-9C."),
            ("What's Table 44 of GSTR-9?",
             "GSTR-9 doesn't have Table 44 - you may be thinking of Clause 44 of Form 3CD (tax audit) which reconciles Income Tax turnover with GST turnover. GSTR-9 itself has 19 Tables (4-16 for main reconciliation + specific adjustments)."),
            ("Does BQP handle GSTR-9 + GSTR-9C + pre-filing audit?",
             "Yes - integrated engagement. Pre-filing audit (4 weeks before 31 December) + voluntary disclosure if identified + Table-by-Table GSTR-9 + Part-by-Part GSTR-9C + ASMT-10 response if subsequent notice. Standard annual engagement for companies with turnover INR 2 crore+. Priority turnaround through December 2026. WhatsApp +91 78018 87130."),
        ],
        "related_pairs": [("gstr-9-fy-2024-25-december-2026-last-mile-checklist.html", "Related", "GSTR-9 Last Mile"),
                          ("gstr-9-gstr-9c-annual-return-india-2026.html", "Related", "GSTR-9 Full Guide")],
        "cta_h": "GSTR-9 FY 2024-25 due 31 December 2026. Pre-filing audit catches gaps.",
        "cta_b": "4-week pre-filing audit + voluntary disclosure strategy + GSTR-9 Table-by-Table + GSTR-9C Part-by-Part. BQP priority December engagement.",
        "keywords": "GSTR-9 pre-filing audit India 2026, GSTR-9 reconciliation CA India, GSTR-9C self-certification CA, December 2026 GSTR-9",
        "desc": "GSTR-9 pre-filing audit checklist December 2026: 4-week framework covering GSTR-1 vs 3B, 3B vs 2B, books vs GST, Section 17(5) blocked ITC, Section 16(4) time-barred, HSN summary, GSTR-9C reconciliation + voluntary disclosure strategy. Working CA guide by Durgesh Chavda.",
    },
    {
        "slug": "form-29b-mat-applicability-certificate-india-2026",
        "title": "Form 29B MAT Applicability Certificate India 2026",
        "hero_em": "Section 115JB 15% MAT compliance.",
        "lead": "Form 29B is Chartered Accountant certificate on Minimum Alternate Tax (MAT) applicability + computation under Section 115JB Income Tax Act. 15% of book profit as alternative tax when standard provisions result in lower tax. Mandatory for companies in MAT scope. Section 115BAA / 115BAB opt-in exempts from MAT. Here's the complete 2026 Form 29B framework.",
        "kicker": "/ Form 29B Checklist &middot; Updated 2026-10-22",
        "sections_pairs": [
            ("/ Section 115JB MAT core", "The 15% alternative.",
             "<ul>"
             "<li>MAT (Minimum Alternate Tax) applies to companies where tax under standard regime (25% / 22% / 30%) is LOWER than 15% of book profit.</li>"
             "<li>In that case: MAT at 15% + surcharge + cess = ~15.6% effective applies instead.</li>"
             "<li>Book profit = net profit per P&amp;L adjusted for specific additions / deletions (Explanation 1 to Section 115JB).</li>"
             "<li>MAT credit: excess MAT paid over standard tax carried forward 15 years + can be set off against future years when standard tax exceeds MAT.</li>"
             "<li><strong>Section 115BAA / 115BAB opt-in exempts from MAT</strong>: specific legislative design. Mature companies in 115BAA regime (22%) + new manufacturing in 115BAB (15%) are MAT-free.</li>"
             "</ul>"),
            ("/ Form 29B specifics", "The CA certificate.",
             "<ul>"
             "<li>Form 29B: Chartered Accountant certificate on book profit + MAT computation.</li>"
             "<li>Filed before ITR (ITR-6 for companies).</li>"
             "<li>CA certifies: book profit computation per Explanation 1 adjustments + MAT comparison + MAT credit carried forward.</li>"
             "<li>ICAI UDIN mandatory for Form 29B signing.</li>"
             "</ul>"),
            ("/ Who's exempt from MAT", "The carve-outs.",
             "<ul>"
             "<li>Companies that opted into Section 115BAA (22%) - MAT does not apply from year of opt-in.</li>"
             "<li>Companies that opted into Section 115BAB (15%) - MAT does not apply.</li>"
             "<li>Companies in SEZ with full Section 10AA deduction - specific carve-out.</li>"
             "<li>Specific small companies (certain thresholds).</li>"
             "<li>Companies without book profit (loss-making or specific negative adjustments).</li>"
             "</ul>"),
            ("/ Common Form 29B scenarios", "Where it matters.",
             "<ul>"
             "<li>Company in standard regime (25% / 30%) with substantial Section 10AA SEZ / Section 80 deductions - standard tax may be below 15% effective → MAT applies.</li>"
             "<li>Loss-making company with timing differences - book profit may still be positive while taxable income is negative.</li>"
             "<li>Specific Section 10(23FBA) / 10(23FBB) exempt income reversed for book profit purposes.</li>"
             "<li>Specific accounting policy changes affecting book profit.</li>"
             "<li>Section 115JB MAT impact decision in opt-in modelling for 115BAA / 115BAB.</li>"
             "</ul>"
             "<p><em>Last updated: 2026-10-22.</em></p>"),
        ],
        "faqs": [
            ("Who needs to file Form 29B?",
             "Every company liable to pay MAT under Section 115JB. If company's standard tax (25% / 30%) is lower than 15% of book profit, MAT applies + Form 29B mandatory. Companies that opted into Section 115BAA or 115BAB are exempt from MAT - Form 29B not needed for them."),
            ("What's the MAT rate for 2026?",
             "15% of book profit + applicable surcharge + 4% cess = ~15.6% effective. (Rate was 18.5% pre-Finance Act 2019; reduced to 15% to encourage profitability-based taxation.)"),
            ("Does Section 115BAA opt-in avoid MAT?",
             "Yes - companies in Section 115BAA (22%) are exempt from MAT. One of the key benefits of 115BAA opt-in (alongside concessional rate). Companies with substantial MAT concern pre-opt-in see additional reason to switch to 115BAA via Form 10-IC."),
            ("What's MAT credit?",
             "If MAT paid is higher than standard tax in a year, excess (MAT - standard tax) is MAT credit. Carried forward 15 years. In future years when standard tax exceeds MAT, MAT credit can be set off against standard tax (up to extent of standard tax). Prevents double-counting."),
            ("Does Form 29B need ICAI UDIN?",
             "Yes - UDIN (Unique Document Identification Number) mandatory for every CA certificate signing. Generated on ICAI portal + attached to Form 29B. Non-UDIN Form 29B considered invalid."),
            ("Does BQP handle Form 29B + Section 115BAA opt-in modelling?",
             "Yes - integrated. Pre-opt-in modelling: standard regime + MAT vs 115BAA + no MAT comparison. Form 29B signing if MAT applies. Form 10-IC filing for 115BAA opt-in. Standard annual engagement for Indian companies. WhatsApp +91 78018 87130."),
        ],
        "related_pairs": [("section-115baa-115bab-corporate-tax-regime-india.html", "Related", "Section 115BAA / 115BAB"),
                          ("form-10-ic-section-115baa-election-checklist-india-2026.html", "Related", "Form 10-IC")],
        "cta_h": "Company liable to MAT or opting into Section 115BAA?",
        "cta_b": "Form 29B CA certificate + Section 115BAA opt-in modelling + MAT credit carry-forward. BQP standard tax engagement.",
        "keywords": "Form 29B MAT India 2026, Section 115JB MAT 15% CA, MAT applicability CA India, Form 29B Section 115BAA exempt",
        "desc": "Form 29B MAT applicability certificate India 2026: Section 115JB 15% Minimum Alternate Tax, book profit computation Explanation 1 adjustments, MAT credit 15-year carry-forward, Section 115BAA / 115BAB opt-in exempts from MAT. Working CA guide by Durgesh Chavda.",
    },
    {
        "slug": "section-115jc-amt-18-5-percent-individual-llp-india",
        "title": "Section 115JC AMT 18.5% Individual + LLP India 2026",
        "hero_em": "individual / LLP Alternate Minimum Tax parallel.",
        "lead": "Section 115JC Alternate Minimum Tax (AMT) applies to individuals, HUFs, LLPs, and partnership firms (NOT companies - that's MAT under 115JB). AMT 18.5% on 'adjusted total income' when standard tax under specific deductions is lower. Parallel to MAT but with distinct scope + rate. Here's the complete 2026 Section 115JC framework.",
        "kicker": "/ Section 115JC AMT Checklist &middot; Updated 2026-10-22",
        "sections_pairs": [
            ("/ Section 115JC AMT core", "The 18.5% rate.",
             "<ul>"
             "<li>AMT applies to: individuals + HUFs + LLPs + Partnership firms (NOT companies - MAT under 115JB).</li>"
             "<li><strong>Rate</strong>: 18.5% of adjusted total income + applicable surcharge + 4% cess.</li>"
             "<li><strong>Adjusted total income</strong>: regular total income + specific deductions added back (Section 10AA SEZ, Section 35AD investment-linked, Section 80 deductions except 80P / 80IAC / 80IAB specifically).</li>"
             "<li><strong>Applies when</strong>: regular tax on income is LOWER than AMT on adjusted total income.</li>"
             "<li>If AMT applies: taxpayer pays AMT; difference becomes AMT credit (carried forward 15 years).</li>"
             "</ul>"),
            ("/ Who's exempt + specific carve-outs", "The exceptions.",
             "<ul>"
             "<li>Individual + HUF: AMT exempt if adjusted total income &lt; INR 20 lakh.</li>"
             "<li>Companies: subject to MAT (Section 115JB) not AMT.</li>"
             "<li>Specific entities + specific income (per Section 115JC(2)): certain exemptions.</li>"
             "<li>Section 80-IAC Startup India + Section 80IAB SEZ developer: specific interaction with AMT.</li>"
             "</ul>"),
            ("/ Common Section 115JC scenarios", "Where it matters.",
             "<ul>"
             "<li>LLP with Section 10AA SEZ deduction: regular tax low; AMT applies.</li>"
             "<li>Partnership firm with substantial Section 80 deductions.</li>"
             "<li>Individual with Section 35AD investment-linked deduction (specified business).</li>"
             "<li>HUF with substantial agricultural income exemption + other specific income.</li>"
             "<li>LLP opting out of Section 115BAD alternative (29% rate without specific deductions).</li>"
             "</ul>"),
            ("/ Form 29C + CA certification", "The compliance.",
             "<ul>"
             "<li><strong>Form 29C</strong>: Chartered Accountant certificate on adjusted total income + AMT computation.</li>"
             "<li>Filed with ITR (ITR-3 for individuals / HUFs; ITR-5 for firms / LLPs).</li>"
             "<li>CA certifies adjusted total income computation + AMT comparison.</li>"
             "<li>ICAI UDIN mandatory.</li>"
             "<li>If AMT applies: AMT paid; AMT credit carried forward 15 years.</li>"
             "</ul>"
             "<p><em>Last updated: 2026-10-22.</em></p>"),
        ],
        "faqs": [
            ("What's Section 115JC AMT?",
             "Alternate Minimum Tax at 18.5% applicable to individuals + HUFs + LLPs + Partnership firms (NOT companies - companies have MAT at 15% under Section 115JB). AMT applies when regular tax is lower than 18.5% of 'adjusted total income' (regular income + specific deductions added back)."),
            ("Does AMT apply to small individuals?",
             "Individual + HUF: AMT exempt if adjusted total income < INR 20 lakh. Above INR 20 lakh with specific deductions (10AA / 35AD / Section 80), AMT may apply. LLPs + Partnership firms: AMT applies regardless of threshold."),
            ("What's Form 29C and when is it filed?",
             "Form 29C: CA certificate on adjusted total income + AMT computation. Filed with ITR by taxpayers to whom Section 115JC applies. ICAI UDIN mandatory. For LLPs + Partnership firms with specific Section 80 / 10AA / 35AD claims."),
            ("Can AMT credit be carried forward?",
             "Yes - 15 years. If AMT paid exceeds regular tax in a year, excess becomes AMT credit. In future years when regular tax exceeds AMT, AMT credit can be set off against regular tax (up to extent of regular tax). Prevents double-taxation."),
            ("Is Section 115BAD a way around AMT for LLPs?",
             "Section 115BAD: 29% concessional corporate tax for LLPs that opt out of specific deductions. If opted in, AMT (115JC) does NOT apply. Trade-off: forfeit Section 10AA + specific Chapter VI-A deductions for lower rate + MAT exemption. Decision modelling similar to Section 115BAA for companies."),
            ("Does BQP handle Form 29C + LLP tax structuring?",
             "Yes - LLP + Partnership firm + individual tax engagement. Section 115JC AMT analysis + Form 29C CA certification + Section 115BAD opt-in modelling for LLPs + AMT credit carry-forward tracking. For LLPs + Partnership firms with specific deduction stacks. WhatsApp +91 78018 87130."),
        ],
        "related_pairs": [("form-29b-mat-applicability-certificate-india-2026.html", "Related", "Form 29B MAT"),
                          ("section-115baa-115bab-corporate-tax-regime-india.html", "Related", "Section 115BAA / 115BAB")],
        "cta_h": "LLP / Partnership firm / individual with specific deductions?",
        "cta_b": "Section 115JC AMT + Form 29C + Section 115BAD opt-in modelling + credit tracking. BQP LLP + Partnership tax engagement.",
        "keywords": "Section 115JC AMT India 2026, Form 29C AMT CA, LLP AMT CA India, Alternate Minimum Tax 18.5% CA",
        "desc": "Section 115JC AMT (Alternate Minimum Tax) 18.5% for individuals + HUFs + LLPs + Partnership firms India 2026: adjusted total income, Form 29C CA certificate, Section 10AA / 35AD / 80 add-back, Section 115BAD LLP opt-in, 15-year AMT credit carry-forward. Working CA guide by Durgesh Chavda.",
    },
    {
        "slug": "form-10ba-house-rent-self-certification-section-80gg",
        "title": "Form 10BA House Rent Self-Certification Section 80GG India 2026",
        "hero_em": "HRA alternative for self-employed + non-salaried.",
        "lead": "Form 10BA is a self-certification by taxpayer claiming Section 80GG deduction for house rent paid when they do NOT receive HRA from employer. For self-employed, freelancers, non-salaried individuals paying rent. Deduction lower of (a) INR 5,000 per month, (b) 25% of adjusted total income, (c) actual rent minus 10% of adjusted total income. Here's the complete 2026 framework.",
        "kicker": "/ Form 10BA Checklist &middot; Updated 2026-10-22",
        "sections_pairs": [
            ("/ Section 80GG eligibility", "Who qualifies.",
             "<ul>"
             "<li>Individual (not HUF / firm).</li>"
             "<li>Self-employed OR salaried but NOT receiving HRA.</li>"
             "<li>Pays rent for residential accommodation.</li>"
             "<li>Does NOT own residential property in city of employment / self-employment.</li>"
             "<li>Spouse + minor child do NOT own residential property in city of residence.</li>"
             "<li>Does NOT claim HRA under Section 10(13A).</li>"
             "<li>File Form 10BA + claim in ITR.</li>"
             "</ul>"),
            ("/ Section 80GG deduction amount", "The 3-way minimum.",
             "<ul>"
             "<li>Deduction = LOWER of three:</li>"
             "<li>&nbsp;&nbsp;&mdash; (a) INR 5,000 per month = INR 60,000 per year.</li>"
             "<li>&nbsp;&nbsp;&mdash; (b) 25% of adjusted total income (ATI).</li>"
             "<li>&nbsp;&nbsp;&mdash; (c) Actual rent paid MINUS 10% of ATI.</li>"
             "<li>Adjusted Total Income = gross total income minus specific deductions (long-term capital gain, Section 56(2)(x), Chapter VI-A except 80GG itself).</li>"
             "<li>Rate materially lower than HRA for employees - Section 80GG is a backstop, not a parallel.</li>"
             "</ul>"),
            ("/ Form 10BA mechanics", "The declaration.",
             "<ul>"
             "<li>Form 10BA: self-declaration by taxpayer.</li>"
             "<li>Content: name + PAN + address of property + name of landlord + rent amount + period + confirmation of no residential property ownership.</li>"
             "<li>Submitted via Indian income tax e-filing portal before filing ITR.</li>"
             "<li>Not CA-attested.</li>"
             "<li>Supporting documents: rent receipts + rent agreement + landlord's PAN (if rent > INR 1 lakh per year).</li>"
             "</ul>"),
            ("/ Section 80GG vs HRA", "The comparison.",
             "<p><strong>HRA under Section 10(13A)</strong>: for salaried employees receiving HRA from employer. Exemption = lower of (a) actual HRA, (b) rent paid - 10% of basic salary, (c) 50% of basic salary (metro) / 40% (non-metro). Typically much larger than Section 80GG.</p>"
             "<p><strong>Section 80GG</strong>: for self-employed OR salaried without HRA. Deduction capped at INR 60,000 per year typically. Materially smaller than HRA.</p>"
             "<p>For freelancers / consultants / self-employed: Section 80GG is the only rent-related tax benefit (apart from Section 24 home loan interest if owned property, which disqualifies 80GG).</p>"
             "<p><em>Last updated: 2026-10-22.</em></p>"),
        ],
        "faqs": [
            ("Who can claim Section 80GG?",
             "Individual (not HUF / firm) who: (a) pays rent for residential accommodation, (b) does NOT own residential property in city of employment / self-employment, (c) spouse + minor child also don't own residential property there, (d) does NOT receive HRA from employer. Must file Form 10BA + claim in ITR."),
            ("What's the maximum Section 80GG deduction?",
             "Lower of: (a) INR 5,000 per month = INR 60,000 per year, (b) 25% of adjusted total income, (c) actual rent paid - 10% of adjusted total income. Typically capped at INR 60,000 per year. Much smaller than HRA for salaried employees."),
            ("Can I claim both HRA and Section 80GG?",
             "No - mutually exclusive. If you receive HRA from employer (even partially), you claim HRA exemption under Section 10(13A). Section 80GG specifically for those who do NOT receive HRA. Choose one based on employment structure."),
            ("Do I need landlord's PAN for Section 80GG?",
             "If annual rent exceeds INR 1 lakh (INR 8,333/month): yes - landlord's PAN mandatory on Form 10BA. Also required for HRA exemption above this threshold. Below INR 1 lakh / year: PAN not required."),
            ("Can freelancer claim Section 80GG?",
             "Yes - self-employed freelancer paying rent for residential accommodation qualifies for Section 80GG (subject to other conditions). File Form 10BA + claim in ITR. Combined with Section 44ADA presumptive scheme (if eligible), can optimise tax position."),
            ("Does BQP handle Section 80GG + freelancer tax?",
             "Yes - standard freelancer / self-employed tax engagement. Section 80GG eligibility + Form 10BA + Section 44ADA presumptive comparison + rent receipt + landlord PAN documentation + Section 80C / 80D / 80E other deductions + ITR filing. For freelancers / self-employed / consultants. WhatsApp +91 78018 87130."),
        ],
        "related_pairs": [("best-ca-freelancer-consultant-tax-india-2026.html", "Related", "Freelancer Tax CA"),
                          ("best-ca-section-44ad-44ada-presumptive-scheme-india.html", "Related", "44AD / 44ADA Presumptive")],
        "cta_h": "Self-employed / freelancer paying rent?",
        "cta_b": "Section 80GG + Form 10BA + Section 44ADA presumptive + comprehensive ITR filing. BQP freelancer tax specialist.",
        "keywords": "Form 10BA Section 80GG India 2026, house rent self-certification 80GG CA, freelancer rent deduction CA India",
        "desc": "Form 10BA house rent self-certification Section 80GG India 2026: eligibility (individual, no HRA, no residential property), deduction = lower of INR 5K/month, 25% of adjusted total income, actual rent minus 10% of ATI, landlord PAN if rent > INR 1 lakh/year, Section 80GG vs HRA comparison. Working CA guide by Durgesh Chavda.",
    },
    {
        "slug": "best-ca-maharashtra-state-registration-shops-establishment-pt",
        "title": "Best CA for Maharashtra State Registration (S&E + PT)",
        "hero_em": "Mumbai + Pune + state-wide compliance.",
        "lead": "Maharashtra state registrations: Shops & Establishment Act (S&E), Professional Tax (PT), Labour Welfare Fund (LWF), Factory Licence, Pollution Control Board (MPCB), state-specific MSME certifications. For Pvt Ltd / LLP / Partnership operating in Mumbai + Pune + Nagpur + Nashik + Aurangabad + state-wide. BQP Maharashtra state registration specialist. Here's the complete 2026 framework.",
        "kicker": "/ Maharashtra Registration Specialist &middot; Updated 2026-10-22",
        "sections_pairs": [
            ("/ Core Maharashtra state registrations", "Mandatory.",
             "<ul>"
             "<li><strong>Shops & Establishment (Maharashtra S&E Act)</strong>: mandatory within 30 days of commencement of business. Online application via Maharashtra Labour Department portal. Fee + renewal every 1-5 years depending on employee count.</li>"
             "<li><strong>Professional Tax (PT)</strong>: Maharashtra Professional Tax - employers must register as 'enroller'. Employee contribution deducted + deposited monthly. Max INR 2,500 per year per employee.</li>"
             "<li><strong>Labour Welfare Fund (LWF)</strong>: Maharashtra LWF Act. Half-yearly contribution by employer + employee (INR 12 per employee + INR 36 employer contribution per half-year).</li>"
             "<li><strong>Factory Licence</strong>: Maharashtra Factories Act. For establishments with 10+ workers using power or 20+ without power. Chief Inspector of Factories.</li>"
             "<li><strong>MPCB (Maharashtra Pollution Control Board)</strong>: Consent to Establish + Consent to Operate for specific industries with pollution potential.</li>"
             "</ul>"),
            ("/ Mumbai-specific attention", "Metro variations.",
             "<ul>"
             "<li>Mumbai: BMC specific regulations in addition to state-level.</li>"
             "<li>MCGM Trade Licence for specific business categories (restaurants + food + specific).</li>"
             "<li>Fire NOC - Mumbai Fire Brigade specifically.</li>"
             "<li>Specific MIDC industrial area regulations if MIDC-located.</li>"
             "<li>SEEPZ SEZ specifics if based there.</li>"
             "</ul>"),
            ("/ Pune + Pune-adjacent", "Specific focus.",
             "<ul>"
             "<li>Pune: PMC Trade Licence for specific categories.</li>"
             "<li>Hinjewadi IT park specifics - PMRDA + specific industrial development authority.</li>"
             "<li>Chakan / Talegaon auto cluster specific state incentives.</li>"
             "<li>Specific PMRDA + Pune Municipal Corporation (PMC) regulations.</li>"
             "</ul>"),
            ("/ Our scope for Maharashtra clients", "Complete offering.",
             "<ul>"
             "<li>S&E Act application + renewal.</li>"
             "<li>Professional Tax enrolment + monthly compliance + annual return.</li>"
             "<li>LWF half-yearly compliance.</li>"
             "<li>Factory Licence if applicable.</li>"
             "<li>MPCB consent (CTE / CTO).</li>"
             "<li>City-specific trade licence (BMC / PMC / NMC Nashik etc.).</li>"
             "<li>Fire NOC coordination.</li>"
             "<li>State industrial incentive co-ordination (specific MIDC / SEEPZ / state EV / IT policies).</li>"
             "<li>Related central-level: GST + PF + ESI + income tax + ROC.</li>"
             "</ul>"
             "<p><em>Last updated: 2026-10-22.</em></p>"),
        ],
        "faqs": [
            ("What's the Maharashtra S&E deadline?",
             "Within 30 days of commencement of business. Online application via Maharashtra Labour Department portal (mahalabour.gov.in). Covers all employers in Maharashtra - shops + commercial establishments + offices. Separate from central ROC incorporation. Renewal every 1-5 years based on employee count."),
            ("What's Maharashtra Professional Tax?",
             "State tax on employment / profession. Employer registers as 'enroller'; deducts from employee salary + deposits with state treasury monthly. Max INR 2,500 per employee per year. Separate from central Income Tax Section 192 TDS."),
            ("Does Maharashtra Labour Welfare Fund apply to all employers?",
             "Yes - every employer in Maharashtra with specified employee count. Half-yearly contribution: employer INR 36 + employee INR 12 per employee per half-year. Due 15 July + 15 January. Significant number of smaller employers miss LWF compliance."),
            ("What's SEEPZ + specific SEZ advantage in Mumbai?",
             "SEEPZ (Special Economic Zone) in Andheri East, Mumbai: specific SEZ regime (Section 10AA 100% tax holiday for 5 years + 50% for 5 years + 50% for 5 years subject to Export Reinvestment Reserve). State sales tax exemption + specific duty-free imports. Specific industries: IT / gems jewellery / electronics / specific services."),
            ("What city-specific trade licence applies to Mumbai?",
             "MCGM Trade Licence - Mumbai Mahanagar Palika's trade licence for specific business categories (food / restaurant / salon / specific service / specific manufacturing). Separate from state S&E. Online via MCGM portal. Specific category-wise fee + renewal."),
            ("Does BQP handle Maharashtra state registration + central compliance integrated?",
             "Yes - integrated engagement. Maharashtra state (S&E + PT + LWF + Factory + MPCB + MCGM) + central (GST + PF + ESI + Income Tax + ROC + FEMA). For companies operating in Mumbai / Pune / Nagpur / Nashik / Aurangabad. Remote delivery possible but site-specific where needed. WhatsApp +91 78018 87130."),
        ],
        "related_pairs": [("best-ca-firm-mumbai-startup-us-incorporation.html", "Related", "Best CA Firm Mumbai"),
                          ("company-secretarial-services-india-remote.html", "Related", "CS Services")],
        "cta_h": "Maharashtra-based company? S&E + PT + LWF + more.",
        "cta_b": "Mumbai + Pune + Nagpur + Nashik state registrations + central compliance integrated. BQP Maharashtra specialist practice.",
        "keywords": "best CA Maharashtra state registration, Maharashtra S&E PT CA, Mumbai PMC MCGM licence CA, Pune state registration CA",
        "desc": "Best CA for Maharashtra state registration (Shops & Establishment Act + Professional Tax + Labour Welfare Fund + Factory Licence + MPCB) 2026: Mumbai + Pune + Nagpur + Nashik + Aurangabad. SEEPZ SEZ + MIDC + state EV / IT policies integration. CA Durgesh Chavda specialist practice.",
    },
    {
        "slug": "best-ca-karnataka-state-registration-bengaluru-mysuru",
        "title": "Best CA for Karnataka State Registration (Bengaluru + Mysuru)",
        "hero_em": "IT + biotech + manufacturing capital.",
        "lead": "Karnataka state registrations for Bengaluru + Mysuru + state-wide: Shops & Commercial Establishments (S&E) + Professional Tax + Labour Welfare Fund + Karnataka Industrial Development Policy + specific IT / biotech / semiconductor cluster support. BBMP (Bruhat Bengaluru Mahanagara Palike) trade licence + specific IT Policy 2022 benefits. Here's the complete 2026 Karnataka framework.",
        "kicker": "/ Karnataka Registration Specialist &middot; Updated 2026-10-22",
        "sections_pairs": [
            ("/ Core Karnataka state registrations", "Mandatory.",
             "<ul>"
             "<li>Shops & Commercial Establishments Act (Karnataka): within 30 days of commencement. Online via Karnataka Labour Department portal.</li>"
             "<li>Professional Tax (Karnataka Tax on Professions, Trades, Callings and Employments Act): employer registration + employee deduction + monthly deposit. Max INR 2,400 per employee per year.</li>"
             "<li>Labour Welfare Fund (Karnataka): applicable to specific employers. Half-yearly contribution.</li>"
             "<li>Karnataka Factories Act: for establishments with 10+ workers using power or 20+ without power.</li>"
             "<li>KSPCB (Karnataka State Pollution Control Board): Consent to Establish + Operate for specific industries.</li>"
             "<li>BBMP Trade Licence: for Bengaluru-based specific business categories.</li>"
             "</ul>"),
            ("/ IT + biotech + semiconductor specific", "Where Karnataka excels.",
             "<ul>"
             "<li><strong>Karnataka IT Policy 2022</strong>: specific support for IT / ITES industry - land + infrastructure + specific state subsidies.</li>"
             "<li><strong>Karnataka Semiconductor Policy 2022</strong>: dedicated semiconductor cluster + state capex subsidy on top of central ISM.</li>"
             "<li><strong>Biotech + Pharmacy</strong>: specific biotech park + Bangalore Bio-Innovation Centre support.</li>"
             "<li><strong>SEZ clusters</strong>: Electronics City SEZ + Bangalore Rural SEZ + specific Mysuru SEZ.</li>"
             "<li><strong>Specific industrial development authorities</strong>: KIADB + KSSIDC + KHDS depending on sector.</li>"
             "</ul>"),
            ("/ Bengaluru-specific attention", "Metro variations.",
             "<ul>"
             "<li>BBMP Trade Licence: for restaurants + bars + specific manufacturing + specific service.</li>"
             "<li>BWSSB (Bengaluru Water Supply and Sewerage Board): water + sewerage connection + specific industrial category rules.</li>"
             "<li>BESCOM (Bengaluru Electricity Supply Company): HT connection for commercial / industrial units.</li>"
             "<li>Fire NOC - BESCOM / Fire Department.</li>"
             "<li>Specific areas: Electronics City (special governance), ITPL / Bagmane / specific tech parks (specific entry + exit protocols).</li>"
             "</ul>"),
            ("/ Our scope for Karnataka clients", "Complete offering.",
             "<ul>"
             "<li>Karnataka state registrations (S&E + PT + LWF + Factory).</li>"
             "<li>KSPCB consent.</li>"
             "<li>BBMP trade licence.</li>"
             "<li>Karnataka IT Policy 2022 incentive application.</li>"
             "<li>Karnataka Semiconductor Policy 2022 incentive application.</li>"
             "<li>KIADB land + capex subsidy co-ordination.</li>"
             "<li>SEZ + ISM / PLI scheme integration.</li>"
             "<li>Related central-level: GST + PF + ESI + income tax + ROC.</li>"
             "</ul>"
             "<p><em>Last updated: 2026-10-22.</em></p>"),
        ],
        "faqs": [
            ("What's Karnataka S&E deadline?",
             "Within 30 days of commencement of business. Online via Karnataka Labour Department portal. Covers all employers - shops + commercial establishments + offices + service centres. Separate from central ROC. Renewal every 5 years based on employee count."),
            ("What's the Karnataka IT Policy 2022 incentive?",
             "Comprehensive state support for IT / ITES industry: land at concessional rate in IT parks + state capex subsidy + specific electricity rebate + SGST reimbursement + fast-track approvals. Specific sub-categories (AI / cybersecurity / Industry 4.0) get additional incentives."),
            ("Does Karnataka have semiconductor incentive?",
             "Yes - Karnataka Semiconductor Policy 2022: dedicated semiconductor + display + ATMP cluster near Bengaluru + Mysuru. State capex subsidy on top of central ISM Modified SPECS. Combined with Section 115BAB: among most generous semiconductor incentive stacks in India (vs Gujarat + Tamil Nadu competitors)."),
            ("What's BBMP Trade Licence and when applicable?",
             "Bruhat Bengaluru Mahanagara Palike's trade licence - mandatory for specific business categories in Bengaluru: restaurants + bars + specific food + salon + specific manufacturing + specific service categories. Online via BBMP portal. Category-wise fee + annual renewal."),
            ("Can I get specific KIADB land allocation?",
             "Yes - Karnataka Industrial Areas Development Board (KIADB) allocates industrial land in various industrial areas (Bidadi + Hosur border + Electronics City Phase II + Hassan + Mysuru). Specific state criteria + investment commitment required. For strategic manufacturing + IT investments. BQP coordinates application."),
            ("Does BQP handle Karnataka state + central integrated?",
             "Yes - integrated engagement. Karnataka state (S&E + PT + LWF + BBMP) + specific policy incentives (IT Policy 2022 + Semicon Policy 2022 + specific sectoral) + central (GST + PF + ESI + Income Tax + ROC + FEMA). For Bengaluru + Mysuru + state-wide operations. WhatsApp +91 78018 87130."),
        ],
        "related_pairs": [("best-ca-firm-bengaluru-startup-us-incorporation.html", "Related", "Best CA Firm Bengaluru"),
                          ("india-semiconductor-ism-pli-foreign-chip-company.html", "Related", "India Semiconductor Mission")],
        "cta_h": "Karnataka-based company? S&E + PT + BBMP + state policy.",
        "cta_b": "Bengaluru + Mysuru state + central compliance + IT Policy + Semicon Policy + KIADB. BQP Karnataka specialist practice.",
        "keywords": "best CA Karnataka state registration, Bengaluru BBMP CA, Karnataka IT Policy 2022 CA, Karnataka Semicon Policy CA",
        "desc": "Best CA for Karnataka state registration (Bengaluru + Mysuru + state-wide): S&E + PT + LWF + BBMP + KSPCB + Karnataka IT Policy 2022 + Karnataka Semicon Policy 2022 + KIADB. Combined state + central integrated compliance. CA Durgesh Chavda specialist practice.",
    },
    {
        "slug": "best-ca-gujarat-state-registration-ahmedabad-rajkot-dholera",
        "title": "Best CA for Gujarat State Registration (Ahmedabad + Rajkot + Dholera)",
        "hero_em": "BQP's home state + semiconductor + GIFT City.",
        "lead": "Gujarat state registrations for Ahmedabad + Rajkot + Vadodara + Surat + Dholera (Semiconductor City) + GIFT City (IFSC): S&E + PT + LWF + Gujarat Industrial Policy 2020 + Dholera Semiconductor + GIFT City IFSCA integration. BQP's home state - deep practitioner competence + state government relationships. Here's the complete 2026 Gujarat framework.",
        "kicker": "/ Gujarat Registration Specialist &middot; Updated 2026-10-22",
        "sections_pairs": [
            ("/ Core Gujarat state registrations", "Mandatory.",
             "<ul>"
             "<li>Gujarat Shops & Establishments Act: within 30 days of commencement.</li>"
             "<li>Professional Tax: employer registration + monthly deduction + annual return. Max INR 2,400 per employee per year.</li>"
             "<li>Gujarat Labour Welfare Fund (LWF): half-yearly contribution.</li>"
             "<li>Gujarat Factories Act: for establishments with 10+ workers using power or 20+ without power.</li>"
             "<li>GPCB (Gujarat Pollution Control Board): CTE / CTO for specific industries.</li>"
             "<li>GIDC (Gujarat Industrial Development Corporation) land allocation if GIDC-based.</li>"
             "</ul>"),
            ("/ Gujarat-specific industrial advantages", "Why Gujarat wins.",
             "<ul>"
             "<li><strong>Dholera Special Investment Region (DSIR)</strong>: dedicated 920 sq km investment region - semiconductor cluster + solar + specific industrial focus. Tata-PSMC fab + Micron ATMP located here.</li>"
             "<li><strong>Gujarat Semiconductor Policy 2022</strong>: state capex subsidy on top of central ISM. Up to 25% state subsidy + land at concessional rate + state SGST reimbursement + electricity rebate.</li>"
             "<li><strong>GIFT City (Gujarat International Finance Tec-City)</strong>: dedicated IFSC. 500+ licensed entities (AIFs, banks, insurance, broker-dealers, bullion exchange). Section 10(4D) tax exemption.</li>"
             "<li><strong>Gujarat Industrial Policy 2020</strong>: comprehensive state support across manufacturing + technology + services. Capex subsidy + SGST reimbursement + electricity rebate.</li>"
             "<li><strong>Vibrant Gujarat</strong>: biennial investment summit; specific MOU + state facilitation.</li>"
             "<li><strong>Mundra + Pipavav ports</strong>: dedicated port + logistics ecosystem.</li>"
             "</ul>"),
            ("/ GIFT City IFSC integration", "Specialised framework.",
             "<ul>"
             "<li>GIFT City entity: IFSCA registration + specific sector licence + state entity in Gujarat.</li>"
             "<li>Combined compliance: state (Gujarat S&E / PT applies but minimal) + IFSCA (sector-specific) + central (CGST + income tax specifics).</li>"
             "<li>Section 10(4D) tax exemption on specified income.</li>"
             "<li>Specific SEZ-equivalent benefits + minimal state tax.</li>"
             "<li>BQP has serviced multiple IFSC AIFs + banks + insurance intermediaries + aircraft lessors.</li>"
             "</ul>"),
            ("/ Our scope for Gujarat clients", "Complete offering.",
             "<ul>"
             "<li>Gujarat state (S&E + PT + LWF + Factory + GPCB).</li>"
             "<li>GIDC land allocation + specific industrial area regulations.</li>"
             "<li>Gujarat Industrial Policy 2020 incentive application.</li>"
             "<li>Dholera Semiconductor Policy 2022 incentive.</li>"
             "<li>GIFT City IFSC specific framework.</li>"
             "<li>Vibrant Gujarat MOU co-ordination for strategic investments.</li>"
             "<li>Mundra + Pipavav port + logistics integration.</li>"
             "<li>Related central: GST + PF + ESI + Income Tax + ROC + FEMA + semiconductor-specific central support.</li>"
             "</ul>"
             "<p><em>Last updated: 2026-10-22.</em></p>"),
        ],
        "faqs": [
            ("Why is Gujarat the semiconductor + manufacturing hub?",
             "Dholera Special Investment Region (DSIR) + Gujarat Semiconductor Policy 2022 (up to 25% state capex subsidy) + Vibrant Gujarat industry support + Mundra + Pipavav ports + Ahmedabad logistics. Tata-PSMC fab + Micron ATMP located here. Combined central ISM + state subsidy stack is among most aggressive globally."),
            ("What's GIFT City and how is it different from Gujarat state?",
             "GIFT City (Gujarat International Finance Tec-City) is a dedicated IFSC (International Financial Services Centre) in Gandhinagar. Regulated by IFSCA (not state GSTAT). Section 10(4D) tax exemption + specific sector licensing. Separate regulatory + tax framework but geographically in Gujarat state."),
            ("What state incentives does Gujarat Industrial Policy 2020 offer?",
             "Comprehensive support: capex subsidy 10-25% based on sector + investment commitment, SGST reimbursement 50-100% for specified period, electricity rebate 1-3 rupees per kWh for specific duration, stamp duty + registration exemption, specific policy sub-additions for manufacturing / IT / cleantech."),
            ("Can BQP help with Vibrant Gujarat MOU?",
             "Yes - BQP's Ahmedabad principal office has specific state government relationships. Strategic investors engaging via Vibrant Gujarat biennial summit (next 2028) can co-ordinate MOU + specific commitment + fast-track state approvals via BQP. Combined with Section 115BAB + PLI + central ISM. WhatsApp +91 78018 87130."),
            ("Does BQP serve non-Gujarat clients from Ahmedabad office?",
             "Yes - BQP's Ahmedabad principal office serves clients globally. Not geographically constrained. Gujarat specialisation is relevant for Gujarat-based clients + strategic manufacturing / semiconductor / GIFT City investments. For other states + overseas clients, same remote-delivery model applies."),
            ("Does BQP handle complete Gujarat + GIFT City + central integrated?",
             "Yes - home-state specialist practice. Gujarat state (S&E + PT + LWF + GPCB + GIDC) + Industrial Policy 2020 + Semicon Policy 2022 + GIFT City IFSC + central (GST + PF + ESI + Income Tax + ROC + FEMA + PLI + ISM). For companies operating in Ahmedabad + Rajkot + Vadodara + Surat + Dholera + GIFT City. WhatsApp +91 78018 87130."),
        ],
        "related_pairs": [("best-ca-firm-ahmedabad-startup-us-incorporation.html", "Related", "Best CA Firm Ahmedabad"),
                          ("gift-city.html", "Related", "GIFT City Service")],
        "cta_h": "Gujarat-based company? Dholera / GIFT City / state policy?",
        "cta_b": "Ahmedabad + Rajkot + Dholera + GIFT City integrated compliance + specific policy incentives. BQP home-state specialist practice.",
        "keywords": "best CA Gujarat state registration, Ahmedabad PT CA, Dholera semiconductor CA, Gujarat Industrial Policy 2020 CA, GIFT City Gujarat CA",
        "desc": "Best CA for Gujarat state registration (Ahmedabad + Rajkot + Vadodara + Surat + Dholera + GIFT City): S&E + PT + LWF + GPCB + GIDC + Gujarat Industrial Policy 2020 + Dholera Semiconductor Policy 2022 + GIFT City IFSCA. BQP home-state specialist practice. CA Durgesh Chavda.",
    },
    {
        "slug": "best-ca-tamil-nadu-state-registration-chennai-hosur",
        "title": "Best CA for Tamil Nadu State Registration (Chennai + Hosur)",
        "hero_em": "auto + electronics + semiconductor + port.",
        "lead": "Tamil Nadu state registrations for Chennai + Hosur + Coimbatore + Krishnagiri + state-wide: S&E + PT + LWF + Tamil Nadu Industrial Policy + specific Semiconductor Policy 2024 + Electronics Policy 2024. Strong auto + electronics + semicon manufacturing cluster + Chennai port. Here's the complete 2026 Tamil Nadu framework.",
        "kicker": "/ Tamil Nadu Registration Specialist &middot; Updated 2026-10-22",
        "sections_pairs": [
            ("/ Core Tamil Nadu state registrations", "Mandatory.",
             "<ul>"
             "<li>Tamil Nadu Shops & Establishments Act: within 30 days of commencement.</li>"
             "<li>Tamil Nadu Profession Tax (TNPT): employer + employee + monthly compliance. Max INR 2,500 per employee per year.</li>"
             "<li>Tamil Nadu Labour Welfare Fund (TNLWF).</li>"
             "<li>Tamil Nadu Factories Act: for establishments meeting specific worker + power thresholds.</li>"
             "<li>TNPCB (Tamil Nadu Pollution Control Board): CTE / CTO.</li>"
             "<li>CMDA (Chennai Metropolitan Development Authority) regulations for Chennai metropolitan.</li>"
             "<li>SIPCOT (State Industries Promotion Corporation of Tamil Nadu) if SIPCOT-based.</li>"
             "</ul>"),
            ("/ TN-specific industrial advantages", "Where TN leads.",
             "<ul>"
             "<li><strong>Auto cluster (Chennai + Hosur)</strong>: Hyundai + Ford + BMW + Nissan + specific Indian OEMs. Supply chain depth.</li>"
             "<li><strong>Electronics (Oragadam + Sriperumbudur)</strong>: Foxconn + Pegatron + Wistron (now Tata). Mobile phone manufacturing hub.</li>"
             "<li><strong>Tamil Nadu Semiconductor Policy 2024</strong>: state capex subsidy on top of central ISM. Semiconductor + display cluster near Chennai + Hosur. Specific MOUs with investors.</li>"
             "<li><strong>Tamil Nadu Electronics Policy 2024</strong>: comprehensive support for electronics manufacturing + ESDM (Electronics System Design and Manufacturing).</li>"
             "<li><strong>Chennai port + Ennore port</strong>: specific port + logistics ecosystem.</li>"
             "<li><strong>SIPCOT industrial parks</strong>: Oragadam + Sriperumbudur + Hosur + Krishnagiri + others.</li>"
             "<li><strong>Specific IT / ITES</strong>: Chennai IT corridor (OMR) + specific state support.</li>"
             "</ul>"),
            ("/ Chennai-specific attention", "Metro variations.",
             "<ul>"
             "<li>Chennai Corporation Trade Licence: for specific business categories.</li>"
             "<li>CMWSSB (Chennai Metropolitan Water Supply and Sewerage Board): water + sewerage connection.</li>"
             "<li>TANGEDCO: electricity supply (HT connection for commercial / industrial).</li>"
             "<li>CMDA building approval + specific zoning regulations.</li>"
             "<li>Specific SEZ: MEPZ (Madras Export Processing Zone) + specific sector SEZ.</li>"
             "</ul>"),
            ("/ Our scope for Tamil Nadu clients", "Complete offering.",
             "<ul>"
             "<li>Tamil Nadu state (S&E + PT + LWF + Factory + TNPCB).</li>"
             "<li>SIPCOT land allocation + specific industrial area regulations.</li>"
             "<li>Tamil Nadu Semiconductor Policy 2024 incentive.</li>"
             "<li>Tamil Nadu Electronics Policy 2024 incentive.</li>"
             "<li>Chennai Corporation Trade Licence + CMWSSB + TANGEDCO.</li>"
             "<li>Related central: GST + PF + ESI + Income Tax + ROC + FEMA + ISM + PLI schemes.</li>"
             "</ul>"
             "<p><em>Last updated: 2026-10-22.</em></p>"),
        ],
        "faqs": [
            ("What's Tamil Nadu's strength for manufacturing?",
             "Auto cluster (Chennai + Hosur with Hyundai + Ford + BMW + Nissan ecosystem), Electronics cluster (Oragadam + Sriperumbudur with Foxconn + Pegatron + Wistron), SIPCOT industrial parks, Chennai port + Ennore port, state Semiconductor Policy 2024 + Electronics Policy 2024. Combined central + state incentive stack competitive with Gujarat + Karnataka."),
            ("What's SIPCOT and how to get allocation?",
             "State Industries Promotion Corporation of Tamil Nadu - allocates industrial land in SIPCOT parks (Oragadam + Sriperumbudur + Hosur + Krishnagiri + others). Specific investment commitment + sector match required. Online application + specific priority for strategic sectors. BQP coordinates application."),
            ("What's Tamil Nadu Semiconductor Policy 2024 incentive?",
             "State capex subsidy on top of central ISM Modified SPECS - specific semiconductor + display cluster near Chennai. Combined with Section 115BAB central (15% corporate tax) + ISM central (up to 50% capex subsidy) + state subsidy = among the most aggressive semiconductor incentive stacks."),
            ("Can I get Tamil Nadu Industrial Policy incentive even without SIPCOT?",
             "Yes - Tamil Nadu Industrial Policy incentive applies state-wide (not SIPCOT-restricted). Capex subsidy + SGST reimbursement + electricity rebate + stamp duty exemption + specific sectoral additions. Online application + specific state facilitation."),
            ("What's MEPZ SEZ in Chennai?",
             "Madras Export Processing Zone - dedicated SEZ in Chennai focused on manufacturing + specific export-oriented units. Section 10AA 100% tax holiday framework. Reduced customs + specific state incentives. Suitable for export-focused manufacturing + specific services."),
            ("Does BQP handle complete Tamil Nadu + central integrated?",
             "Yes - specialist practice. Tamil Nadu state (S&E + TNPT + LWF + TNPCB + SIPCOT) + Semicon Policy 2024 + Electronics Policy 2024 + Chennai specifics (Corporation / CMWSSB / TANGEDCO / CMDA) + central compliance. For companies operating in Chennai + Hosur + Coimbatore + Krishnagiri. WhatsApp +91 78018 87130."),
        ],
        "related_pairs": [("best-ca-firm-chennai-sme-ipo.html", "Related", "Best CA Firm Chennai"),
                          ("india-pli-scheme-foreign-manufacturer-2026.html", "Related", "PLI Scheme")],
        "cta_h": "Tamil Nadu-based company? Chennai / Hosur / SIPCOT / Semicon?",
        "cta_b": "State registrations + SIPCOT + Semicon Policy 2024 + Electronics Policy 2024 + central compliance integrated. BQP TN specialist practice.",
        "keywords": "best CA Tamil Nadu state registration, Chennai CMDA CA, SIPCOT CA Tamil Nadu, TN Semicon Policy 2024 CA",
        "desc": "Best CA for Tamil Nadu state registration (Chennai + Hosur + Coimbatore + Krishnagiri + state-wide): S&E + TNPT + LWF + TNPCB + SIPCOT + Tamil Nadu Semiconductor Policy 2024 + Tamil Nadu Electronics Policy 2024 + MEPZ SEZ + Chennai Port. CA Durgesh Chavda specialist practice.",
    },
    {
        "slug": "best-ca-startup-ipo-roadmap-pre-main-board-india",
        "title": "Best CA for Startup IPO Roadmap (Pre-Main Board)",
        "hero_em": "Series C to listing bell journey.",
        "lead": "Startup planning Main Board IPO (NSE / BSE) within 24-36 months needs integrated pre-IPO roadmap: 3-year audited track record + Ind AS restatement + SEBI ICDR compliance + Rule 9B demat + FEMA cleanup + Section 56(2)(viib) legacy + ESOP SEBI SBEB + corporate governance. BQP specialist pre-IPO practice. Here's the complete 24-month pre-IPO framework.",
        "kicker": "/ Pre-IPO Roadmap Specialist &middot; Updated 2026-10-22",
        "sections_pairs": [
            ("/ 24-month pre-IPO roadmap", "The phased approach.",
             "<p><strong>Months 1-3: Readiness assessment + strategy</strong></p>"
             "<ul>"
             "<li>Current state audit: financial + legal + compliance.</li>"
             "<li>SME IPO vs Main Board decision.</li>"
             "<li>Target issue size + pricing framework.</li>"
             "<li>Target investor base (institutional + retail).</li>"
             "<li>SEBI ICDR Regulations compliance baseline.</li>"
             "</ul>"
             "<p><strong>Months 3-9: Financial restatement + compliance cleanup</strong></p>"
             "<ul>"
             "<li>3-year audited financial track record in Ind AS.</li>"
             "<li>ASC 606 → Ind AS 115 revenue recognition conversion (if US GAAP previously).</li>"
             "<li>ASC 842 → Ind AS 116 lease conversion.</li>"
             "<li>ASC 718 → Ind AS 102 SBC conversion.</li>"
             "<li>FEMA cleanup: FC-GPR missed + FC-TRS missed + FLA Return missed - voluntary compounding.</li>"
             "<li>Rule 9B demat: all shareholders in demat form.</li>"
             "<li>Section 56(2)(viib) legacy review: historical rounds pre-abolition.</li>"
             "</ul>"
             "<p><strong>Months 9-15: SEBI ICDR structuring + DRHP preparation</strong></p>"
             "<ul>"
             "<li>Promoter + Promoter Group identification per SEBI ICDR Reg. 2(1)(oo).</li>"
             "<li>Minimum promoter contribution + lock-in requirements.</li>"
             "<li>Public shareholding dilution structuring.</li>"
             "<li>Related Party Transactions (RPT) audit under Section 188 Companies Act.</li>"
             "<li>Internal Financial Controls (ICFR) audit sign-off.</li>"
             "<li>ESOP SEBI SBEB Regulations compliance.</li>"
             "<li>DRHP (Draft Red Herring Prospectus) drafting support in coordination with Merchant Banker + Legal Counsel.</li>"
             "<li>Independent Director appointments.</li>"
             "<li>Audit Committee + specific board committee setup.</li>"
             "</ul>"
             "<p><strong>Months 15-21: SEBI filing + regulatory review</strong></p>"
             "<ul>"
             "<li>DRHP filing with SEBI.</li>"
             "<li>SEBI observations + response iterations.</li>"
             "<li>Stock exchange in-principle approval.</li>"
             "<li>Marketing material + investor roadshow preparation.</li>"
             "<li>Price band + pricing strategy with Merchant Banker.</li>"
             "</ul>"
             "<p><strong>Months 21-24: IPO execution + listing</strong></p>"
             "<ul>"
             "<li>Anchor investor allotment (60% of QIB portion).</li>"
             "<li>Public issue open 3-5 days.</li>"
             "<li>Allotment + listing.</li>"
             "<li>Post-listing LODR compliance roadmap.</li>"
             "</ul>"),
            ("/ Vendor coordination", "Pre-IPO team.",
             "<ul>"
             "<li><strong>Merchant Banker</strong>: typically Big-5 (Axis Capital / ICICI Securities / IIFL / Motilal Oswal / specific) OR specialist boutique. BQP coordinates financial workstream.</li>"
             "<li><strong>Legal Counsel</strong>: typically Indian law firm specialising in capital markets (Khaitan / AZB / Shardul Amarchand / Trilegal / JSA). BQP coordinates compliance workstream.</li>"
             "<li><strong>Statutory Auditor</strong>: if Big-4 wanted for brand, Big-4 as statutory auditor + BQP as pre-IPO specialist advisor. If BQP acts as statutory auditor, suitable for mid-market Main Board.</li>"
             "<li><strong>RTA (Registrar & Transfer Agent)</strong>: Link Intime / KFin / specific. BQP coordinates share capital + Rule 9B demat.</li>"
             "<li><strong>Depository (NSDL / CDSL)</strong>: for ISIN + demat facilitation.</li>"
             "<li><strong>Printer + Marketing / PR + Advertising + Roadshow organiser</strong>: standard vendor set.</li>"
             "</ul>"),
            ("/ Common pre-IPO issues BQP sees", "Where readiness surfaces gaps.",
             "<ul>"
             "<li>FEMA breaches - missed FC-GPR / FLA / APR filings - need compounding before DRHP filing.</li>"
             "<li>Rule 9B demat non-compliance - mandatory pre-IPO.</li>"
             "<li>Section 56(2)(viib) legacy angel tax - historical rounds pre-abolition - need resolution.</li>"
             "<li>Related party transaction documentation + arm's-length - critical for Section 188 compliance.</li>"
             "<li>ESOP SEBI SBEB Regulations - historical ESOP grants may not comply.</li>"
             "<li>Promoter identification issues - founders + their affiliates per SEBI definition.</li>"
             "<li>Independent Financial Advice / ICFR audit - audit framework needs setup.</li>"
             "<li>Specific litigation + material contingent liability disclosure.</li>"
             "<li>DPT-3 + MSME Form I + DIR-3 KYC + specific annual filings gaps.</li>"
             "</ul>"
             "<p><em>Last updated: 2026-10-22.</em></p>"),
        ],
        "faqs": [
            ("How long is the typical pre-IPO journey?",
             "24-36 months for Main Board; 12-18 months for SME IPO. Phases: readiness assessment (1-3 months), financial restatement + compliance cleanup (6 months), SEBI ICDR structuring + DRHP (6 months), SEBI review + stock exchange approval (6 months), execution + listing (3 months). Longer if major compliance cleanup needed (FEMA / Rule 9B / 56(2)(viib) legacy)."),
            ("Should startup use Big-4 statutory auditor for IPO?",
             "For Main Board INR 1,000 crore+ issue size: typically yes - SEBI + investors expect Big-4 brand. For Main Board INR 300-1,000 crore: Big-4 or specialist firm acceptable. For SME IPO + smaller Main Board: specialist firm (BQP) workable. Combined engagement common: Big-4 as auditor + BQP as pre-IPO specialist advisor."),
            ("What are the biggest pre-IPO compliance gaps?",
             "Top 5 per BQP engagement experience: (1) FEMA breaches - FC-GPR / FLA / APR missed filings - need compounding before DRHP filing (adds 90-180 days). (2) Rule 9B demat non-compliance - mandatory pre-IPO. (3) Section 56(2)(viib) legacy angel tax exposure from pre-abolition rounds. (4) RPT documentation + arm's-length. (5) ESOP SEBI SBEB compliance."),
            ("Is 3-year Ind AS track record mandatory?",
             "Yes for Main Board IPO - 3 years of audited financials in Ind AS. If company's historical accounts are in Indian GAAP (older) or US GAAP (if US-HQ'd previously), restatement to Ind AS required. ASC 606 → Ind AS 115 revenue + ASC 842 → Ind AS 116 lease + ASC 718 → Ind AS 102 SBC conversions."),
            ("Can BQP work with Merchant Banker + Legal Counsel on pre-IPO?",
             "Yes - standard. BQP's compliance + financial workstream feeds into Merchant Banker's DRHP + Legal Counsel's SEBI filing. Weekly cross-firm status call during pre-IPO phase. Prior work with Axis Capital / ICICI Securities / IIFL + Khaitan / AZB / Shardul Amarchand on specific SME + Main Board mandates."),
            ("Does BQP handle complete pre-IPO roadmap including vendor coordination?",
             "Yes - specialist practice. 24-36 month pre-IPO roadmap + Ind AS restatement + SEBI ICDR structuring + DRHP compliance workstream + vendor coordination (Merchant Banker + Legal Counsel + RTA + Depository + Printer) + post-listing LODR roadmap. For startups + mid-market Main Board + SME IPO. WhatsApp +91 78018 87130."),
        ],
        "related_pairs": [("best-ca-sme-ipo-main-board-ipo-advisor-india.html", "Related", "Best CA for IPO Advisory"),
                          ("ca-for-ipo-ready-startup-sebi-icdr-ind-as-india.html", "Related", "CA for IPO-Ready Startup")],
        "cta_h": "Series C+ startup planning Main Board IPO in 24-36 months?",
        "cta_b": "Pre-IPO roadmap + Ind AS restatement + FEMA cleanup + Rule 9B demat + SEBI ICDR + DRHP. BQP pre-IPO specialist practice. Scope-based engagement.",
        "keywords": "best CA pre-IPO startup India, Main Board IPO roadmap CA, Ind AS restatement pre-IPO CA, SEBI ICDR CA startup",
        "desc": "Best CA for startup pre-IPO roadmap India 2026: 24-month pre-Main Board journey covering 3-year Ind AS restatement + FEMA compounding + Rule 9B demat + Section 56(2)(viib) legacy + SEBI ICDR structuring + DRHP drafting + Merchant Banker/Legal/RTA/Depository coordination. CA Durgesh Chavda specialist practice.",
    },
    {
        "slug": "best-ca-indian-llc-llp-conversion-india-2026",
        "title": "Best CA for Indian LLC / LLP Conversion",
        "hero_em": "LLP ↔ Pvt Ltd + Partnership ↔ LLP conversion specialist.",
        "lead": "Indian entity structure conversion: Private Limited to LLP (post-Series exit simplification), LLP to Pvt Ltd (pre-fundraising / pre-IPO), Partnership to LLP, Partnership to Pvt Ltd. Each has specific tax implications (Section 47 vs 56 taxable), FEMA implications for foreign shareholders, Companies Act / LLP Act compliance. BQP conversion specialist practice. Here's the complete 2026 framework.",
        "kicker": "/ Entity Conversion Specialist &middot; Updated 2026-10-22",
        "sections_pairs": [
            ("/ Common conversion scenarios", "When each matters.",
             "<ul>"
             "<li><strong>LLP to Pvt Ltd</strong>: pre-fundraising (VCs prefer Pvt Ltd), pre-IPO (SEBI requires), employee ESOP (easier via Pvt Ltd). Most common conversion direction.</li>"
             "<li><strong>Pvt Ltd to LLP</strong>: post-fundraising exit simplification, specific tax structure (pass-through), reduced ROC compliance burden.</li>"
             "<li><strong>Partnership to LLP</strong>: limited liability without corporate overhead. Simple conversion under LLP Act 2008.</li>"
             "<li><strong>Partnership to Pvt Ltd</strong>: for fundraising + ESOP + specific regulatory benefits. More compliance but more flexibility.</li>"
             "<li><strong>Sole Proprietor to Pvt Ltd / LLP</strong>: liability shield + fundraising readiness.</li>"
             "</ul>"),
            ("/ Section 47 tax-neutral conversion", "The critical provision.",
             "<ul>"
             "<li><strong>Section 47 Income Tax Act</strong>: specific transfers NOT treated as 'transfer' for capital gain purposes.</li>"
             "<li>Section 47(xiiib): conversion of company to LLP qualifies as tax-neutral if specific conditions met.</li>"
             "<li>Specific conditions: 50% of total profits to continue to partners for 5+ years; same proportionate ownership + control; specific valuation + accounting rules.</li>"
             "<li>If conditions NOT met: deemed transfer; capital gain + Section 56(2)(x) in LLP's hands.</li>"
             "</ul>"),
            ("/ Section 56(2)(x) risk + FEMA implications", "Beyond income tax.",
             "<ul>"
             "<li>Section 56(2)(x): if conversion involves issue of shares / interests at value exceeding fair market value - buyer-side gift tax exposure.</li>"
             "<li>FEMA implications for foreign shareholders: FC-TRS for share transfer during conversion; FC-GPR for new issue; Form ODI for Indian investment moving offshore.</li>"
             "<li>Press Note 3 beneficial ownership verification.</li>"
             "<li>Specific sector FDI caps may change post-conversion (LLP has different FDI treatment vs Pvt Ltd).</li>"
             "<li>Stamp duty + registration fees in some states.</li>"
             "</ul>"),
            ("/ Our scope for conversion", "Complete offering.",
             "<ul>"
             "<li>Conversion planning: tax implications + FEMA + stamp duty + regulatory.</li>"
             "<li>Section 47(xiiib) conditions compliance for tax-neutral.</li>"
             "<li>Draft resolutions + conversion agreement.</li>"
             "<li>ROC filings: LLP conversion to Pvt Ltd (SPICe+), Pvt Ltd to LLP (Form 17 + specific).</li>"
             "<li>FEMA compliance for foreign shareholders.</li>"
             "<li>Section 56(2)(x) risk mitigation.</li>"
             "<li>Related compliance: GST re-registration if GSTIN changes, PAN update, bank KYC update, licence re-registration.</li>"
             "<li>Post-conversion compliance roadmap.</li>"
             "</ul>"
             "<p><em>Last updated: 2026-10-22.</em></p>"),
        ],
        "faqs": [
            ("What's the tax treatment of LLP to Pvt Ltd conversion?",
             "Not a straightforward 'conversion' - typically achieved via (a) incorporation of new Pvt Ltd + (b) business transfer from LLP to new Pvt Ltd (slump sale under Section 50B OR individual asset transfer with specific tax treatment). Tax implications: capital gain in LLP's hands on business transfer. Section 47 tax neutrality may apply with specific structuring."),
            ("What's the tax treatment of Pvt Ltd to LLP conversion?",
             "Section 47(xiiib) permits tax-neutral conversion if specific conditions met: 50% of total profits continue to partners for 5+ years, same proportionate ownership, specific valuation + accounting. If conditions NOT met: deemed transfer; capital gain + 56(2)(x) exposure."),
            ("Can LLP raise external VC funding?",
             "LLP can raise external investment but less common than Pvt Ltd. VC term sheets typically require Pvt Ltd. Specific LLP structures for family offices / specific institutional LPs work. For traditional VC Series A+: Pvt Ltd is standard. LLP to Pvt Ltd conversion often done pre-Series A."),
            ("What are FEMA implications for conversion with foreign shareholders?",
             "If company has foreign shareholders, conversion involves: FC-TRS for share transfer during conversion + FC-GPR for new issue + potentially Form ODI if ownership moves between Indian + offshore entity + Press Note 3 beneficial ownership verification. Specific pricing guidelines + FEMA Section 13 compounding if historical breaches."),
            ("How long does entity conversion take?",
             "LLP to Pvt Ltd (via business transfer route): 60-90 days. Pvt Ltd to LLP: 60-90 days (specific Form 17 process). Partnership to LLP: 30-45 days. Partnership to Pvt Ltd: 60-90 days. Timeline affected by: regulatory approvals (if sector-specific), FEMA pricing certificates, licence re-registration."),
            ("Does BQP handle entity conversion + related compliance?",
             "Yes - specialist practice. Conversion planning + Section 47 compliance + FEMA compliance for foreign shareholders + ROC filings + GST / PAN / bank re-registration + post-conversion compliance roadmap. For startups + mid-market businesses + foreign-shareholder entities. WhatsApp +91 78018 87130."),
        ],
        "related_pairs": [("pvt-ltd-vs-llp.html", "Related", "Pvt Ltd vs LLP"),
                          ("foreign-company-setup-indian-subsidiary-wos.html", "Related", "Indian WOS Setup")],
        "cta_h": "Entity conversion planning: LLP ↔ Pvt Ltd ↔ Partnership?",
        "cta_b": "Conversion planning + Section 47 tax-neutral + FEMA + ROC + related compliance. BQP conversion specialist practice.",
        "keywords": "best CA LLP Pvt Ltd conversion India, entity conversion CA India, Section 47 tax neutral conversion CA, partnership to LLP CA India",
        "desc": "Best CA for Indian LLC / LLP conversion 2026: LLP to Pvt Ltd (pre-fundraising / pre-IPO), Pvt Ltd to LLP (exit simplification), Partnership to LLP, Partnership to Pvt Ltd. Section 47(xiiib) tax-neutral conditions, FEMA FC-TRS / FC-GPR for foreign shareholders, Section 56(2)(x) risk management, ROC filings. CA Durgesh Chavda specialist practice.",
    },
]

for p in PAGES:
    html = quick_page(
        slug=p["slug"], title=p["title"], hero_em=p["hero_em"], lead=p["lead"],
        kicker=p["kicker"], sections_pairs=p["sections_pairs"],
        faqs=p["faqs"], related_pairs=p["related_pairs"],
        cta_h=p["cta_h"], cta_b=p["cta_b"],
        keywords=p["keywords"], desc=p["desc"],
    )
    write_page(p["slug"], html)

print(f"Batch X complete: {len(PAGES)} pages")
