# -*- coding: utf-8 -*-
"""Batch D: 6 NRI Taxation pages. Big SEO cluster for 'NRI tax', 'NRI returning India', 'NRE NRO FCNR'."""
from build_lib import page, write_page

# 1. PILLAR: NRI Taxation India Complete Guide
write_page("nri-taxation-india-complete-guide", page(
    slug="nri-taxation-india-complete-guide",
    title="NRI Taxation India 2026 Complete Guide | Residency, DTAA, Returns - BQP",
    description="NRI taxation India 2026: residential status (RNOR / NRI / Resident), DTAA relief, Section 115A, capital gains, NRE / NRO / FCNR account tax, repatriation. Working CA guide by Durgesh Chavda.",
    keywords="NRI taxation India, NRI tax guide 2026, NRI residential status, RNOR status India, NRI DTAA India, NRE account tax, NRO account tax, Section 115A NRI, NRI capital gains India, NRI tax return filing",
    hero_kicker="/ NRI tax &middot; Pillar guide",
    hero_title_html="NRI taxation India, <em>the working-CA guide.</em>",
    hero_lead="India's taxation of Non-Resident Indians is governed by residential status, specific NRI sections (Section 115A, Section 195), DTAA relief under treaties with 90+ countries, and the TCS and remittance regime under FEMA. This is the pillar guide — covering residency rules, income heads, DTAA mechanics, bank-account tax, repatriation and return-of-residence transitions.",
    sections=[
        ("/ Residential status", "The single most important determination.",
         "<p>Under Section 6 of the Income Tax Act, an individual is Resident in India in a financial year if they satisfy either of two tests:</p>"
         "<ul>"
         "<li><strong>182 days or more</strong> physical presence in India during the financial year, OR</li>"
         "<li><strong>60 days or more</strong> physical presence in the financial year AND <strong>365 days or more</strong> cumulative in the preceding 4 financial years.</li>"
         "</ul>"
         "<p>The 60-day threshold is replaced with 182 days for Indian citizens who leave India for employment abroad or as crew of an Indian ship, and for persons of Indian origin visiting India.</p>"
         "<p>If neither test is met, the individual is a <strong>Non-Resident</strong> (NRI). If Resident, a further test determines Ordinary Resident (ROR) vs Resident but Not Ordinarily Resident (RNOR):</p>"
         "<ul>"
         "<li>RNOR: Resident in India in the current year but non-resident in India in 9 out of the preceding 10 years, OR physically present in India for 729 days or less in the preceding 7 years.</li>"
         "<li>ROR: Resident who does not meet the RNOR carve-outs.</li>"
         "</ul>"
         "<p>Why it matters: ROR is taxed on worldwide income. NRI and RNOR are taxed on India-source income only. This single determination can change tax liability by lakhs or crores for high-earning returnees.</p>"),
        ("/ What income India taxes for each status", "ROR vs RNOR vs NRI.",
         "<p><strong>Resident and Ordinarily Resident (ROR):</strong> taxed on worldwide income &mdash; Indian salary + foreign salary + Indian capital gains + foreign capital gains + Indian rental + foreign rental + foreign business income.</p>"
         "<p><strong>Resident but Not Ordinarily Resident (RNOR):</strong> taxed on India-source income only (same as NRI), unless the foreign income is from a business controlled from India or a profession set up in India &mdash; in which case the foreign income is also taxed. RNOR is a transitional 2-3 year window for returnees that preserves NRI-like treatment on foreign assets.</p>"
         "<p><strong>Non-Resident (NRI):</strong> taxed on India-source income only. India-source includes: salary earned in India, salary paid by Indian employer regardless of where earned, rental from Indian property, capital gains on Indian assets, dividends from Indian companies, interest on Indian bank accounts (NRO), interest from Indian debt instruments.</p>"),
        ("/ The NRI-specific tax regimes", "Section 115A, Section 115AC and more.",
         "<p>India has special lower-rate regimes for NRIs on specific income heads:</p>"
         "<p><strong>Section 115A:</strong> NRI dividend income from Indian companies &mdash; 20% rate (plus surcharge and cess) with no deduction and no need to file return if TDS is correctly deducted. Royalty and FTS from Indian payers: 10% rate.</p>"
         "<p><strong>Section 115AB:</strong> Long-term capital gains for NRIs on specified Indian equity &mdash; 12.5% (post-July 2024) without indexation.</p>"
         "<p><strong>Section 115AC:</strong> NRI income from foreign-currency bonds / GDRs of Indian companies &mdash; 10% rate.</p>"
         "<p><strong>Section 115E:</strong> NRI investment income from specified foreign-exchange assets &mdash; 20% rate; LTCG on such assets taxed at 10%.</p>"
         "<p><strong>Section 195:</strong> general TDS mechanism for payments to non-residents &mdash; the Indian payer deducts tax at the applicable rate (treaty rate if lower, with TRC + Form 10F) at the time of payment.</p>"
         "<p>Election: NRIs can choose between Section 115A/E rates (concessional) and normal slab rates &mdash; whichever is lower in their situation. The choice is made at return-filing time.</p>"),
        ("/ DTAA relief", "The treaty override.",
         "<p>Where an NRI's country of residence has a DTAA with India (90+ countries including US, UK, UAE, Singapore, Canada, Australia, Germany, France, Mauritius, Switzerland), the treaty rate overrides the Indian domestic rate if it is lower.</p>"
         "<p>Standard treaty rates for NRIs on Indian-source income:</p>"
         "<ul>"
         "<li><strong>Dividends:</strong> capped at 10-15% under most treaties (vs 20% domestic Section 115A).</li>"
         "<li><strong>Interest:</strong> 10-15% under most treaties.</li>"
         "<li><strong>Royalties and FTS:</strong> 10-15% under most treaties.</li>"
         "<li><strong>Capital gains:</strong> treaty position varies &mdash; some preserve India's right to tax, others shift to residence country. Post-2017 India-Singapore and post-2016 India-Mauritius protocols closed the earlier exemption on Indian equity capital gains.</li>"
         "</ul>"
         "<p>To claim: NRI obtains <strong>TRC (Tax Residency Certificate)</strong> from their country tax authority + files <strong>Form 10F</strong> electronically on the Indian tax portal + provides the Indian payer with both before the payment. Payer withholds at the treaty rate.</p>"),
        ("/ NRE, NRO and FCNR accounts", "Where NRIs hold money &mdash; and the tax rules.",
         "<p><strong>NRE (Non-Resident External) account:</strong> rupee-denominated, maintained from foreign earnings. Interest earned on NRE deposits is <strong>exempt from Indian tax</strong> (Section 10(4)(ii)). Principal and interest are fully repatriable.</p>"
         "<p><strong>NRO (Non-Resident Ordinary) account:</strong> rupee-denominated, for income earned in India (rent, dividend, pension). Interest earned on NRO deposits is <strong>fully taxable</strong> in India as income. Repatriation up to USD 1M per financial year with CA certificate (Form 15CA + Form 15CB).</p>"
         "<p><strong>FCNR (Foreign Currency Non-Resident) deposit:</strong> foreign-currency denominated, no exchange risk. Interest is <strong>exempt from Indian tax</strong> (Section 10(4)(ii)). Fully repatriable.</p>"
         "<p>Practical rule: route foreign earnings through NRE / FCNR (tax-free interest). Route India-source income through NRO (fully taxable). The NRE-to-NRO transfer is allowed; the reverse is not without specific authorisations.</p>"),
        ("/ Capital gains for NRIs on Indian assets", "Shares, mutual funds, property.",
         "<p><strong>Listed Indian equity shares (held 12+ months, LTCG):</strong> 12.5% post-July 2024, with INR 1.25 lakh exemption per year. STT must be paid at sale. Buyback: separate regime from Oct 2024 onwards.</p>"
         "<p><strong>Unlisted Indian equity shares (held 24+ months, LTCG):</strong> 20% with indexation, or 12.5% without indexation (post-July 2024 choice).</p>"
         "<p><strong>Equity mutual funds:</strong> same as listed equity for LTCG. Short-term 20%.</p>"
         "<p><strong>Debt mutual funds (post-April 2023):</strong> gains are taxed at slab rate regardless of holding period (grandfathering for pre-April-2023 holdings).</p>"
         "<p><strong>Immovable property:</strong> LTCG at 12.5% (without indexation, post-July 2024), 24-month holding period. Section 54 / 54F / 54EC reinvestment exemptions available. 1% TDS by buyer on sale to NRI (increases significantly where seller's PAN is linked to NRI status; Form 15CA/CB and Section 195 override).</p>"
         "<p><strong>Repatriation of sale proceeds:</strong> up to USD 1M per financial year through NRO account with Form 15CA + 15CB. Larger amounts need RBI approval or sequential year-wise repatriation.</p>"),
        ("/ Return of residence transition", "Moving back to India &mdash; the RNOR window.",
         "<p>When an NRI returns to India permanently, their status changes based on days present and the 10-year lookback. In most cases the returnee is RNOR for 2-3 financial years before becoming ROR.</p>"
         "<p>During RNOR window:</p>"
         "<ul>"
         "<li>Foreign salary (continuing employment with foreign employer) is taxable in India to the extent of services rendered in India.</li>"
         "<li>Foreign investment income (US brokerage dividends, UK ISA, UAE bank interest) is NOT taxable in India.</li>"
         "<li>Foreign real estate rental is NOT taxable in India unless business is controlled from India.</li>"
         "<li>Foreign capital gains are NOT taxable in India.</li>"
         "</ul>"
         "<p>Planning window: sell appreciated foreign assets, convert foreign IRA / 401(k) / ISA / pension corpus, during RNOR to avoid Indian tax on those gains. After the transition to ROR, worldwide income is taxable.</p>"
         "<p>Documentation: maintain a passport-stamp day log for the preceding 10 years; file ITR-2 or ITR-3 with Schedule FA (Foreign Assets) and Schedule FSI (Foreign Source Income) once ROR.</p>"),
    ],
    faqs=[
        ("What is the difference between NRI, RNOR, and ROR?",
         "NRI (Non-Resident Indian) does not meet either the 182-day or 60/365-day presence test. RNOR (Resident but Not Ordinarily Resident) is Resident for the year but satisfies a lookback carve-out (non-resident in 9 of 10 preceding years, or 729 days or less in preceding 7 years). ROR (Resident and Ordinarily Resident) is Resident without the lookback carve-out. ROR is taxed on worldwide income; NRI and RNOR are taxed on India-source only (with narrow exceptions for RNOR)."),
        ("Is NRE account interest taxable in India?",
         "No. Interest earned on NRE deposits is exempt from Indian tax under Section 10(4)(ii), provided the account holder maintains NRI status. If the account holder returns to India permanently and becomes Resident, the NRE account must be re-designated as a Resident account and the exemption ends from that date forward."),
        ("What is TRC and Form 10F?",
         "TRC (Tax Residency Certificate) is a certificate issued by the NRI's country tax authority certifying their tax residence in that country. Form 10F is an electronic self-declaration filed on the Indian income tax portal providing details of the NRI's foreign residence and treaty position. Both are required to claim DTAA treaty-reduced rates on Indian-source income."),
        ("Can an NRI claim DTAA relief if India has no treaty with their country?",
         "No. DTAA relief requires an operative tax treaty between India and the NRI's country of residence. For countries without treaties (relatively few remaining), Section 91 unilateral relief may apply where the NRI pays tax on the same income in both countries &mdash; India allows credit limited to the lower of the two rates. This is weaker and less certain than treaty relief."),
        ("How much can an NRI repatriate from India per year?",
         "Up to USD 1 million per financial year from the balances in an NRO account, including from sale of inherited or purchased Indian property, with Form 15CA + Form 15CB CA certification. Amounts beyond USD 1M in a year require RBI approval, or sequential year-wise repatriation across multiple years. NRE / FCNR account balances are freely repatriable without the USD 1M cap."),
        ("Does BQP handle NRI tax filings and planning?",
         "Yes. NRI annual ITR filing (ITR-2 or ITR-3), DTAA relief + TRC + Form 10F co-ordination, Form 15CA/CB for repatriation, Section 195 TDS positioning on India-source payments, residential-status planning for return-of-residence, and sale of Indian property for NRIs. Dubai, US, UK, Singapore NRI clients handled regularly. Request via get-a-quote.html."),
    ],
    related=[
        ("india-us-dtaa-withholding-rates.html", "Guide", "India-US DTAA"),
        ("india-uae-tax-treaty-dtaa.html", "Guide", "India-UAE DTAA"),
        ("nri-returning-india-tax-rnor-transition.html", "Guide", "Returning to India (RNOR)"),
    ],
    cta_headline="NRI with India exposure &mdash; your tax is often the single-biggest fixable line item.",
    cta_body="For NRIs selling Indian property, holding Indian mutual funds, inheriting Indian assets, or planning a return to India, the right structure saves lakhs. Working-CA engagement covers filing, TRC/Form 10F, Form 15CA/CB, residential-status planning, and sale co-ordination. 20-minute scoping is free.",
))

# 2. NRI Residential Status + RNOR
write_page("nri-residential-status-rnor-india", page(
    slug="nri-residential-status-rnor-india",
    title="NRI Residential Status & RNOR India 2026 | Full Rules - BQP",
    description="India residential status rules for NRIs under Section 6: 182-day test, 60/365-day test, deemed residency, RNOR carve-outs. Day-count examples. Working CA guide by CA Durgesh Chavda.",
    keywords="NRI residential status, Section 6 Income Tax Act, RNOR status India, 182 day rule NRI, 60 day 365 day test, deemed residency NRI, Indian citizen abroad tax",
    hero_kicker="/ NRI tax &middot; Residential status",
    hero_title_html="Residential status, <em>the single number that controls your tax.</em>",
    hero_lead="India's residential-status rules under Section 6 are the first filter on NRI taxation. Get this wrong and your entire filing is wrong. This is the full day-count playbook with worked examples, including the 2020 deemed-residency amendment and the RNOR 7-year / 10-year lookback.",
    sections=[
        ("/ The three tests", "What makes you Resident, RNOR or NRI.",
         "<p>Section 6(1): an individual is Resident in India in a financial year if they satisfy either of the two basic tests:</p>"
         "<ol>"
         "<li><strong>182-day test:</strong> physical presence in India for 182 days or more in the financial year.</li>"
         "<li><strong>60/365-day test:</strong> physical presence of 60 days or more in the current financial year AND 365 days or more cumulative in the preceding 4 financial years.</li>"
         "</ol>"
         "<p>If NEITHER is met, the individual is Non-Resident (NRI).</p>"
         "<p>Section 6(6): a Resident is further categorised as RNOR (Resident but Not Ordinarily Resident) if either:</p>"
         "<ul>"
         "<li>Non-resident in India in 9 out of the 10 preceding financial years, OR</li>"
         "<li>Physical presence in India for 729 days or less during the 7 preceding financial years.</li>"
         "</ul>"
         "<p>Residents who do not meet the RNOR carve-outs are Resident and Ordinarily Resident (ROR).</p>"),
        ("/ The India-citizen exceptions", "Why Indian passport holders get a longer rope.",
         "<p>Section 6(1)(c) Explanation modifies the 60-day test for two specific categories of Indian citizens:</p>"
         "<ul>"
         "<li><strong>Indian citizen or person of Indian origin visiting India:</strong> the 60-day threshold becomes 182 days (so this group is harder to make Resident). From AY 2021-22, if their total Indian-source income exceeds INR 15 lakh, the threshold is 120 days instead of 182.</li>"
         "<li><strong>Indian citizen leaving India for employment abroad or as crew of an Indian ship:</strong> the 60-day threshold becomes 182 days.</li>"
         "</ul>"
         "<p>Why: these carve-outs give Indian passport holders moving abroad for employment, or visiting India for short trips, a wider buffer before Residence attaches. Without the carve-out, a 60-day visit home would trigger Residence (given the 365-day preceding lookback is easy to meet for anyone with India ties).</p>"),
        ("/ The 2020 deemed residency amendment", "The INR 15 lakh trap for stateless Indians.",
         "<p>Finance Act 2020 introduced Section 6(1A): an Indian citizen whose Indian-source income exceeds INR 15 lakh in a financial year is deemed to be a Resident of India if they are not liable to tax in any other country or territory by reason of domicile or residence.</p>"
         "<p>This is the 'stateless Indian' rule. It targets Indian citizens living in zero-income-tax jurisdictions (historically UAE pre-2023, Bahrain, Monaco) who had no residence anywhere &mdash; India now claims them as Resident.</p>"
         "<p>Post-2023 UAE Corporate Tax: UAE residents who are subject to UAE Corporate Tax are now 'liable to tax' in UAE and escape Section 6(1A). Pure UAE-individual-tax-free status is still at risk; UAE tax-residence certificate helps.</p>"
         "<p>Section 6(1A) resident is treated as RNOR by default (Section 6(6)(d)), so worldwide income is NOT taxed in India &mdash; only India-source income is taxed, same as NRI. The 'deemed resident' label mainly affects return-filing obligations and specific sections.</p>"),
        ("/ Day-count worked examples", "Three NRI situations.",
         "<p><strong>Case 1: Dubai-based Indian executive, visits India for 50 days each year, has been in UAE for 6+ years.</strong></p>"
         "<ul>"
         "<li>Current year presence: 50 days.</li>"
         "<li>182-day test: not met (50 &lt; 182).</li>"
         "<li>60/365-day test (Indian citizen abroad): modified to 182 days &mdash; not met.</li>"
         "<li>Status: Non-Resident (NRI).</li>"
         "<li>Indian tax: India-source income only.</li>"
         "</ul>"
         "<p><strong>Case 2: Indian citizen moved to US on H-1B 3 years ago, visits India for 85 days (long vacation).</strong></p>"
         "<ul>"
         "<li>Current year presence: 85 days.</li>"
         "<li>182-day test: not met.</li>"
         "<li>60/365-day test for Indian citizen leaving for employment: modified to 182 days &mdash; not met.</li>"
         "<li>Status: NRI.</li>"
         "</ul>"
         "<p><strong>Case 3: Permanent return to India after 8 years in UAE, arrives mid-November.</strong></p>"
         "<ul>"
         "<li>Current year presence: ~135 days (Nov to Mar).</li>"
         "<li>182-day test: not met (135 &lt; 182).</li>"
         "<li>60/365-day test: 135 days &gt; 60. Preceding 4 years cumulative: minimal visits, say 100 days. 100 &lt; 365 &mdash; test not met.</li>"
         "<li>Status: still NRI for this year.</li>"
         "<li>Next year: full 365 days in India &mdash; Resident. 10-year lookback: non-resident in 8+ of past 10 years &mdash; passes RNOR carve-out. Status: <strong>RNOR</strong> for 2-3 years before transitioning to ROR.</li>"
         "</ul>"),
        ("/ Common mistakes", "Where NRIs trip up on their own residency.",
         "<ul>"
         "<li><strong>Not maintaining day-count log.</strong> Years later, when questioned, the taxpayer cannot prove non-presence. Keep a dated passport-stamp log year by year.</li>"
         "<li><strong>Confusing arrival/departure day inclusion.</strong> Both arrival and departure days are counted as presence in India. A one-day business trip = 1 day. A 10-day round trip = 10 or 11 days depending on arrival/departure timing.</li>"
         "<li><strong>Thinking NRI = tax-free in India.</strong> NRI is taxed on India-source income &mdash; Indian salary paid by Indian employer (regardless of where work was done), Indian rental, Indian capital gains, Indian dividends, NRO interest.</li>"
         "<li><strong>Missing RNOR window on return.</strong> The 2-3 year RNOR transition is the single most tax-efficient window to sell foreign assets, convert IRAs/401(k)s, close out foreign business. Returning CFOs often learn about it too late.</li>"
         "<li><strong>Ignoring Section 6(1A) deemed residency.</strong> UAE / Bahrain / Monaco-based Indians with INR 15 lakh+ Indian income now need to check it annually.</li>"
         "</ul>"),
    ],
    faqs=[
        ("Is Day 1 of arrival in India counted as 'present in India'?",
         "Yes. Both the arrival day and the departure day are counted as days present in India under CBDT guidance. A single-day round trip (arrive at 2am, leave at 11pm the same day) still counts as 1 day."),
        ("What if I accidentally stay over 182 days in a year as an NRI?",
         "You become Resident for that year. If your 10-year lookback still shows non-residence in 9 of 10 years, you are RNOR &mdash; still taxed on India-source only. If the 10-year lookback has flipped (you've been Resident 2+ times in the past 10 years), you become ROR &mdash; worldwide income taxable."),
        ("Can I claim NRI status after returning to India permanently?",
         "No, not for the year of return and onward, if your day-count makes you Resident. However, RNOR status (preserving India-source-only taxation) typically applies for 2-3 years post-return. Plan the transition carefully &mdash; sell appreciated foreign assets, convert foreign retirement accounts during RNOR."),
        ("Is Section 6(1A) still relevant after UAE Corporate Tax?",
         "Partially. UAE residents now subject to UAE Corporate Tax (9% above AED 375,000) are 'liable to tax' in UAE and should escape Section 6(1A). But individuals earning salary (not business income) in UAE may still fall outside UAE CT and face Section 6(1A) risk if Indian-source income exceeds INR 15 lakh. Obtain UAE TRC annually as evidence."),
        ("How do I prove my day-count to the Indian tax authority?",
         "Primary evidence: passport stamps (immigration entry / exit). Secondary: airline tickets, boarding passes, employer travel records, foreign salary pay slips. Maintain a dated spreadsheet log reconciling to passport stamps. Audits going back 7-10 years are possible &mdash; keep records that long."),
        ("Does BQP handle residential-status planning?",
         "Yes. Pre-move planning (optimising the exit date and return date), year-of-return RNOR documentation, Section 6(1A) analysis for UAE / zero-tax jurisdiction residents, and litigation support if residency is challenged. Standard scoping call is free. Request via get-a-quote.html."),
    ],
    related=[
        ("nri-taxation-india-complete-guide.html", "Pillar", "NRI Taxation Pillar Guide"),
        ("nri-returning-india-tax-rnor-transition.html", "Guide", "Returning to India (RNOR)"),
        ("india-uae-tax-treaty-dtaa.html", "DTAA", "India-UAE DTAA"),
    ],
    cta_headline="Not sure if you're NRI, RNOR or Resident this year?",
    cta_body="One-call residential-status review: your day-count, 10-year lookback, Section 6(1A) exposure, treaty-status overlap. We confirm your status in writing with the day-count math so you can file correctly or plan the return date.",
))

# 3. NRI Returning to India - RNOR transition
write_page("nri-returning-india-tax-rnor-transition", page(
    slug="nri-returning-india-tax-rnor-transition",
    title="NRI Returning to India 2026 | RNOR Transition Tax Planning - BQP",
    description="NRI permanently returning to India: RNOR 2-3 year window, foreign asset re-pricing, IRA/401(k) conversion timing, foreign property sale, re-designation of NRE accounts. Working CA planning guide.",
    keywords="NRI returning to India, RNOR transition, IRA 401k rollover India, foreign property NRI return, re-designate NRE account, moving back to India tax, repatriate retirement NRI",
    hero_kicker="/ NRI tax &middot; Return to India",
    hero_title_html="NRI returning to India, <em>the RNOR planning window.</em>",
    hero_lead="The 2-3 year RNOR window post-return is the single most tax-efficient period of an NRI's life. Foreign assets can be sold, retirement accounts converted, foreign property disposed of, all without Indian tax. After the RNOR transition ends, worldwide income is Indian-taxable. Plan the window.",
    sections=[
        ("/ What RNOR delivers", "Why this window matters.",
         "<p>Resident but Not Ordinarily Resident (RNOR) is the Indian tax status between NRI and ROR. For 2-3 financial years after returning to India permanently, the typical returnee holds RNOR status (assuming they were non-resident in 9 of the preceding 10 years, or physically present in India for 729 days or less in the preceding 7 years).</p>"
         "<p>RNOR taxability: India-source income only &mdash; same as NRI. Foreign dividends, foreign capital gains, foreign rental, foreign retirement withdrawals are NOT taxable in India during RNOR.</p>"
         "<p>After RNOR ends (usually year 3 or year 4 post-return), status becomes ROR and worldwide income is Indian-taxable. The RNOR window is a one-time planning opportunity.</p>"),
        ("/ What to do in the RNOR window", "The returnee checklist.",
         "<ol>"
         "<li><strong>Sell appreciated foreign equity holdings.</strong> US brokerage long-term capital gains at 15-20% US rate; no additional Indian tax during RNOR. After RNOR, these gains would be Indian-taxable at 12.5% LTCG (with FTC for US tax paid under India-US DTAA Article 25).</li>"
         "<li><strong>Convert / withdraw US retirement accounts.</strong> Traditional IRA / 401(k) withdrawals are US-taxable at your US marginal rate. During RNOR, no Indian tax on top. After RNOR, the Indian-taxability of foreign-pension payouts becomes complex &mdash; EET regime distinction. The RNOR window is the cleanest time to decide: distribute lump sum, Roth-convert, or roll to annuity.</li>"
         "<li><strong>Sell foreign real estate.</strong> US / UAE / UK property sold during RNOR &mdash; US / UAE / UK tax at source, no Indian tax on top. After RNOR, Indian tax on worldwide capital gains applies (with FTC).</li>"
         "<li><strong>Close dormant foreign bank accounts.</strong> Simplifies future FBAR / Schedule FA reporting. During RNOR there is no Schedule FA filing obligation; after ROR there is.</li>"
         "<li><strong>Convert foreign business income streams.</strong> If you hold a foreign business, consider taking the final distribution / liquidating / converting to passive income during RNOR. Post-RNOR, foreign business income can be Indian-taxable if controlled from India.</li>"
         "<li><strong>Re-designate NRE / FCNR accounts.</strong> On becoming Resident, NRE and FCNR accounts must be re-designated as Resident accounts (RFC or regular) within specified timelines. The interest exemption under Section 10(4)(ii) ends on re-designation.</li>"
         "<li><strong>File Schedule FA (Foreign Assets) once ROR.</strong> Mandatory annual disclosure of all foreign assets. Non-disclosure penalty: Black Money Act, up to USD 10 lakh + possible imprisonment. Build the asset log during RNOR.</li>"
         "</ol>"),
        ("/ The IRA / 401(k) decision", "A detailed walk-through.",
         "<p>For US NRIs returning to India, the US retirement account decision is the single largest financial choice. Options:</p>"
         "<p><strong>Option A: Lump-sum distribution during RNOR.</strong> Full balance withdrawn in one year. US tax on the full amount at US marginal rate (often 32-37% for a large balance), plus 10% early-withdrawal penalty if under age 59.5. No Indian tax during RNOR. Net cash available immediately in India. Downsides: punitive US rate on a one-year lump-sum, loss of future tax-deferred growth.</p>"
         "<p><strong>Option B: Rollover to IRA, periodic withdrawals.</strong> Keep the IRA in US, draw down over 10+ years. Each year's withdrawal is US-taxed at your then-marginal rate (lower if your US income is minimal post-move). But each year's withdrawal is also potentially Indian-taxable once ROR &mdash; India may treat IRA distribution as 'pension income' taxable at slab rate, with FTC for US tax paid under DTAA Article 20. Net Indian tax: typically neutral but complex.</p>"
         "<p><strong>Option C: Roth conversion during RNOR.</strong> Convert traditional IRA to Roth IRA while RNOR &mdash; US tax on the conversion amount at your then-US-marginal rate, no Indian tax during RNOR. After conversion, Roth withdrawals are US-tax-free (if 5-year rule met) and India has not clearly ruled on Roth taxability but likely tax-free. This is often the best outcome if US marginal rate is manageable in the conversion year.</p>"
         "<p>Decision depends on: your US marginal rate in RNOR year, Indian marginal rate forecast post-ROR, your age (early-withdrawal penalty), balance size, and your appetite for ongoing US tax filing. Model all three.</p>"),
        ("/ The NRE account re-designation", "An often-missed step.",
         "<p>On becoming Resident in India, FEMA requires the account holder to re-designate NRE and FCNR accounts within reasonable time. Options:</p>"
         "<ul>"
         "<li>Convert NRE Savings Account to Resident Savings Account &mdash; immediate conversion, interest from the conversion date is Indian-taxable.</li>"
         "<li>Convert NRE Fixed Deposit to RFC (Resident Foreign Currency) Account &mdash; maintains foreign-currency denomination, allows continued use of the foreign-currency corpus. Interest on RFC is taxable but can be useful for returning NRIs with pending foreign-currency obligations.</li>"
         "<li>Convert NRE Fixed Deposit to Resident Rupee Deposit &mdash; most common; rupee-denominated; interest fully taxable from conversion.</li>"
         "</ul>"
         "<p>Failure to re-designate: banks may freeze the account; FEMA penalty possible for continuing to hold NRE after becoming Resident. Act within the first 60-90 days of return.</p>"),
    ],
    faqs=[
        ("How long does RNOR status last for a returning NRI?",
         "Typically 2 to 3 financial years post-return, depending on your 10-year lookback at the time of return. If you were non-resident in 9+ of the preceding 10 years at return, you can be RNOR for 2 years in some cases, up to 3 years. The 7-year 729-day carve-out can extend RNOR further in specific cases."),
        ("Should I withdraw my US 401(k) before returning to India?",
         "Not before &mdash; use the RNOR window after return. Pre-return withdrawal while US-resident attracts your US marginal rate plus state tax (if applicable). Post-return during RNOR, the US tax applies but your US income is often lower, dropping the marginal rate. Roth conversion during RNOR is frequently the best outcome. Model your specific numbers before deciding."),
        ("Is my US IRA distribution taxed in India once I'm ROR?",
         "Yes, under current law. ROR means worldwide income is Indian-taxable. US IRA distribution is treated as pension / annuity income by Indian tax authorities, taxed at slab rate. India-US DTAA Article 20 provides FTC relief for the US tax on the same amount. Net Indian tax: often zero or small positive, but requires accurate FTC documentation."),
        ("Can I keep my US investment accounts after returning to India?",
         "Yes, generally &mdash; US brokerage accounts can remain open and continue to hold investments. However: FBAR filing applies if you remain a US person; Schedule FA filing applies when you become ROR in India; some brokerages close accounts of non-US-resident clients (check Fidelity / Schwab / Vanguard terms); and the India-US DTAA + FTC machinery must handle double-counting of US dividends and gains."),
        ("What happens to my NRE Fixed Deposit when I return?",
         "You re-designate within 60-90 days of returning. Options: convert to Resident Rupee Deposit (interest taxable from conversion), convert to RFC Account (foreign-currency, interest taxable), or withdraw and convert to another instrument. The exemption on NRE interest under Section 10(4)(ii) ends from the conversion date; interest before conversion remains exempt."),
        ("Does BQP handle NRI return-to-India planning?",
         "Yes. We handle pre-return planning (optimal exit date from host country, RNOR start-year math), RNOR-year asset disposal planning (foreign equity, real estate, retirement accounts), NRE / FCNR re-designation co-ordination, and first-year ROR filing including Schedule FA. Request via get-a-quote.html."),
    ],
    related=[
        ("nri-taxation-india-complete-guide.html", "Pillar", "NRI Taxation Pillar"),
        ("nri-residential-status-rnor-india.html", "Guide", "Residential Status Rules"),
        ("india-us-dtaa-withholding-rates.html", "DTAA", "India-US DTAA"),
    ],
    cta_headline="Returning to India in the next 24 months?",
    cta_body="The RNOR window is a one-time planning opportunity. Pre-return scoping covers US / UAE / UK asset-disposal plan, retirement-account conversion math, NRE re-designation timing, and first-year ROR filing readiness. Most clients save multiples of our fee on retirement-account tax alone.",
))

# 4. NRI Selling Indian Property
write_page("nri-selling-indian-property-capital-gains", page(
    slug="nri-selling-indian-property-capital-gains",
    title="NRI Selling Indian Property 2026 | Capital Gains, TDS, Repatriation - BQP",
    description="NRI selling Indian property: capital gains calculation, Section 195 TDS 12.5% + surcharge, Section 54 / 54F / 54EC reinvestment, repatriation USD 1M, Form 15CA/CB. Working CA guide.",
    keywords="NRI sell Indian property, NRI capital gains property, Section 195 TDS NRI, Section 54 NRI, NRI property repatriation, Form 15CA 15CB NRI, Lower Deduction Certificate NRI",
    hero_kicker="/ NRI tax &middot; Property sale",
    hero_title_html="NRI selling Indian property, <em>the full tax &amp; repatriation stack.</em>",
    hero_lead="The sale of Indian real estate by an NRI involves five distinct workstreams: capital gains computation, Section 195 TDS by the buyer, reinvestment exemptions (Section 54 / 54F / 54EC), Form 15CA / 15CB for repatriation, and the USD 1M annual repatriation cap. Each needs to be sequenced correctly or the sale closes with the wrong number.",
    sections=[
        ("/ Capital gains computation", "LTCG vs STCG, cost base, indexation.",
         "<p><strong>Holding period:</strong> property held 24+ months is long-term; less is short-term. The relevant date is the date of acquisition (purchase deed / allotment letter / RERA registration), not possession.</p>"
         "<p><strong>Long-Term Capital Gain (LTCG) rate:</strong> post-July 2024, 12.5% without indexation. Pre-July 2024 purchases retain the option of 20% with indexation. The lower of the two is the taxable rate. For inherited property, the holding period and cost base roll back to the previous owner's acquisition.</p>"
         "<p><strong>Short-Term Capital Gain (STCG) rate:</strong> slab rate for the NRI &mdash; typically 30% + surcharge + cess for higher-income NRIs.</p>"
         "<p><strong>Fair Market Value (FMV):</strong> for properties acquired before 1 April 2001, FMV as on 1 April 2001 is the cost base (grandfathering).</p>"
         "<p><strong>Indexed cost of acquisition:</strong> cost &times; (CII of sale year / CII of acquisition year). CII for FY 2024-25 is 363; FY 2001-02 is 100.</p>"),
        ("/ Section 195 TDS", "The buyer's withholding obligation.",
         "<p>Section 195 requires the buyer to deduct TDS on any payment to a non-resident. For NRI property sale, the applicable rate (post-July 2024) is <strong>12.5% + surcharge + cess</strong> of the <strong>sale consideration</strong> (not the gain) unless an LDC (Lower Deduction Certificate) is obtained.</p>"
         "<p>Surcharge rates for NRIs on LTCG above INR 50 lakh: 10% to 25% depending on income bracket.</p>"
         "<p>Effective TDS rate on sale consideration above INR 1 crore (surcharge 15%): roughly 13.75% + 4% cess = ~14.3%. For sale consideration above INR 5 crore (surcharge 25%): ~15.625% + 4% cess = ~16.25%.</p>"
         "<p><strong>LDC (Lower Deduction Certificate):</strong> NRI files Form 13 with the Indian tax authority before the sale, requesting a lower TDS rate based on expected actual capital gains tax. The authority issues a certificate specifying the lower rate (e.g., 2-5% of consideration) &mdash; applied by the buyer at closing. Processing time: 30-45 days typically. Essential for high-value sales to avoid locking up large TDS amounts refundable only after ITR filing.</p>"),
        ("/ Reinvestment exemptions", "Section 54, 54F, 54EC.",
         "<p><strong>Section 54:</strong> LTCG on residential house property is exempt if reinvested in another residential property in India within 2 years (purchase) or 3 years (construction). Reinvestment cap effectively INR 10 crore post-2023. One residential property can be purchased; two are allowed where total LTCG is INR 2 crore or less (once-in-a-lifetime).</p>"
         "<p><strong>Section 54F:</strong> LTCG on any long-term capital asset (not just house) is exempt if the net consideration is reinvested in one residential house in India within 2 years. Exemption prorated if net consideration partially reinvested.</p>"
         "<p><strong>Section 54EC:</strong> LTCG on land or building reinvested in specified bonds (NHAI, REC, PFC, IRFC) within 6 months of sale is exempt. Cap: INR 50 lakh per financial year. Bonds carry 5.25% coupon, 5-year lock-in. Useful for NRIs who don't want to reinvest in physical property but want to defer gains.</p>"
         "<p><strong>Capital Gains Account Scheme (CGAS):</strong> if the reinvestment is not completed by the ITR filing due date, the LTCG amount is parked in a CGAS account at a public-sector bank. Reinvestment from CGAS within the specified timeline preserves the exemption; failure results in taxability of the un-reinvested amount in the year the timeline expires.</p>"),
        ("/ Repatriation of sale proceeds", "USD 1M cap, Form 15CA/CB.",
         "<p>Post-sale, net proceeds credit to the NRI's NRO account. Repatriation out of India through NRO is capped at <strong>USD 1 million per financial year</strong> per account holder.</p>"
         "<p>Required documentation:</p>"
         "<ul>"
         "<li><strong>Form 15CA</strong> &mdash; self-declaration filed electronically on the Indian tax portal by the NRI, detailing the remittance and tax position.</li>"
         "<li><strong>Form 15CB</strong> &mdash; CA certificate certifying the tax paid or treaty position; required for remittances exceeding INR 5 lakh.</li>"
         "<li><strong>Sale deed, buyer's TDS certificate (Form 16A), capital gains computation, proof of tax paid, property documents (CA pack).</strong></li>"
         "</ul>"
         "<p>Where sale proceeds exceed USD 1 million: NRI can spread repatriation across multiple financial years (USD 1M year 1 + USD 1M year 2 + ...), or apply to RBI for approval of larger single-year repatriation. The USD 1M limit is per account holder &mdash; joint owners each have their own USD 1M.</p>"
         "<p>Timing: Form 15CA / 15CB is generally filed in the same week as the actual bank remittance. Banks reject remittance requests without the Form 15CA acknowledgement attached.</p>"),
    ],
    faqs=[
        ("What TDS does the buyer deduct when buying property from an NRI?",
         "Post-July 2024, 12.5% + surcharge + cess of the sale consideration (not the gain) under Section 195. Effective rate 14-16% depending on sale value. The LDC route reduces this to 2-5% if the NRI applies via Form 13 before the sale."),
        ("Can an NRI claim Section 54 exemption on an Indian property sale?",
         "Yes. Section 54 applies to any residential house capital gain, including NRI's. Reinvestment must be in Indian residential property within 2 years (purchase) or 3 years (construction). The reinvestment property can be held jointly with Indian relatives. INR 10 crore cap applies."),
        ("How do I avoid locking up large TDS on an NRI property sale?",
         "File Form 13 (LDC application) with the Indian tax authority 45-60 days before the sale. The LDC specifies a lower TDS rate (typically 2-5% of consideration based on your expected actual capital gains tax). The buyer then withholds at the LDC rate instead of 12.5-16%. Essential for sales above INR 5 crore."),
        ("Can I repatriate more than USD 1M from an Indian property sale?",
         "The default cap is USD 1M per financial year from NRO. For sale proceeds above that, you can spread across multiple financial years (USD 1M + USD 1M + ...), apply to RBI for a larger single-year repatriation, or split ownership across multiple family members each with their own USD 1M cap. Advance planning is essential &mdash; the cap is calendar-financial-year, so timing of sale and documentation matter."),
        ("What if I buy another Indian property within 2 years of sale?",
         "Section 54 exemption applies: the LTCG on the sold property is exempt to the extent reinvested in the new residential property in India. Reinvestment within 2 years from the date of sale (purchase) or 3 years (construction). If reinvestment is partial, exemption is prorated."),
        ("Does BQP handle NRI property sales?",
         "Yes. Full-service: LDC application (Form 13), capital-gains computation, buyer co-ordination, Form 15CA/CB for repatriation, Section 54/54EC/54F structuring, ITR filing. Working-CA engagement from LDC filing through final remittance. Standard timeline 60-120 days. Request via get-a-quote.html."),
    ],
    related=[
        ("nri-taxation-india-complete-guide.html", "Pillar", "NRI Taxation Pillar"),
        ("nri-mutual-funds-india-tax.html", "Guide", "NRI Mutual Funds Tax"),
        ("nre-nro-fcnr-account-tax-rules.html", "Guide", "NRE / NRO / FCNR Rules"),
    ],
    cta_headline="Selling Indian property as an NRI? LDC filing is the first move.",
    cta_body="Without a Lower Deduction Certificate, the buyer withholds 12.5-16% of the full sale consideration &mdash; often many multiples of your actual capital gains tax. The TDS can take 12-18 months to refund. We file the Form 13 LDC 45 days before closing and co-ordinate the full sale pack.",
))

# 5. NRI Mutual Funds Tax
write_page("nri-mutual-funds-india-tax", page(
    slug="nri-mutual-funds-india-tax",
    title="NRI Mutual Funds India Tax 2026 | KYC, TDS, Repatriation - BQP",
    description="NRI investing in Indian mutual funds: KYC under FEMA, equity vs debt MF taxation, TDS by AMC, repatriable vs non-repatriable schemes, FATCA-CRS filing, ITR reporting. Working CA guide.",
    keywords="NRI mutual fund India, NRI MF taxation, NRI equity mutual fund tax, NRI debt mutual fund TDS, NRI MF repatriation, FATCA mutual fund NRI, US NRI mutual fund ban",
    hero_kicker="/ NRI tax &middot; Mutual funds",
    hero_title_html="NRI mutual funds in India, <em>tax, KYC and repatriation.</em>",
    hero_lead="NRIs can invest in Indian mutual funds under FEMA, but the practical workflow differs materially from resident investors &mdash; KYC with specific documents, repatriable vs non-repatriable scheme choice, TDS by the AMC at source, FATCA-CRS classification, and the complete ban some AMCs impose on US-NRI subscriptions.",
    sections=[
        ("/ KYC and account setup", "What NRIs need to invest.",
         "<p>NRIs can invest in Indian mutual funds through two routes under FEMA:</p>"
         "<ul>"
         "<li><strong>Repatriable basis:</strong> investment from NRE / FCNR account; sale proceeds and capital gains freely repatriable without USD 1M cap.</li>"
         "<li><strong>Non-repatriable basis:</strong> investment from NRO account or inward remittance; sale proceeds and gains credited to NRO, subject to USD 1M repatriation cap.</li>"
         "</ul>"
         "<p>KYC documents:</p>"
         "<ul>"
         "<li>Passport (plus visa / residence permit of host country).</li>"
         "<li>Overseas address proof (utility bill, bank statement, driver licence).</li>"
         "<li>Indian PAN (mandatory).</li>"
         "<li>Indian bank account (NRE / NRO / FCNR).</li>"
         "<li>FATCA + CRS self-declaration specifying tax residence country.</li>"
         "<li>Signature attestation (sometimes required by Indian consulate / notary / banker).</li>"
         "</ul>"
         "<p><strong>US NRI restrictions:</strong> many Indian AMCs (ICICI Prudential, SBI MF, HDFC MF historically) do not accept US-NRI subscriptions due to US SEC compliance costs (registration under Investment Advisers Act). Some AMCs accept US NRIs with additional documentation. Canada NRIs face similar restrictions. UK, UAE, Singapore, Australia NRIs are generally fully accepted.</p>"),
        ("/ Taxation of equity mutual funds", "LTCG 12.5%, STCG 20%.",
         "<p><strong>Equity-oriented mutual funds</strong> (65%+ equity exposure):</p>"
         "<ul>"
         "<li><strong>LTCG</strong> (held 12+ months): 12.5% post-July 2024 (previously 10%). INR 1.25 lakh exemption per year (previously INR 1 lakh).</li>"
         "<li><strong>STCG</strong> (held &lt;12 months): 20% post-July 2024 (previously 15%).</li>"
         "<li><strong>STT</strong> is paid at redemption on equity MFs, qualifying them for the above rates.</li>"
         "<li><strong>TDS by AMC:</strong> yes, deducted at source on redemption for NRIs (unlike for Indian residents). Rate matches the applicable LTCG / STCG rate; refund via ITR filing if excess.</li>"
         "</ul>"
         "<p><strong>DTAA override:</strong> treaty-based lower rate may apply where available &mdash; most treaties do not reduce capital gains on Indian shares post-2016/2017 protocols. The 12.5% domestic rate typically applies in full.</p>"),
        ("/ Taxation of debt and hybrid mutual funds", "Post-April 2023 regime.",
         "<p><strong>Debt-oriented mutual funds</strong> (post-April 2023 purchases):</p>"
         "<ul>"
         "<li>Gains are taxed at the NRI's <strong>slab rate</strong>, regardless of holding period &mdash; the LTCG preferential rate was removed in Finance Act 2023 for debt MFs.</li>"
         "<li>Grandfathering: debt MF units purchased before 1 April 2023 retain the pre-amendment regime (LTCG 20% with indexation after 3-year holding) until sold.</li>"
         "</ul>"
         "<p><strong>Hybrid mutual funds:</strong> treated based on actual equity exposure. &ge;65% equity: equity MF treatment. 35-65% equity: a specific balanced-advantage category exists with a 12.5% LTCG + INR 1.25 lakh exemption treatment (post-2024 rules). &lt;35% equity: slab-rate treatment like debt MFs.</p>"
         "<p><strong>TDS by AMC:</strong> deducted at source for NRIs at the applicable rate.</p>"),
        ("/ Repatriation and reporting", "What the NRI must file.",
         "<p><strong>Repatriable scheme sales:</strong> proceeds credit to NRE account; repatriable freely outside India without USD 1M cap.</p>"
         "<p><strong>Non-repatriable scheme sales:</strong> proceeds credit to NRO; repatriation up to USD 1M per financial year with Form 15CA + 15CB.</p>"
         "<p><strong>ITR filing:</strong> NRIs file ITR-2 (or ITR-3 if business income). Capital gains from Indian mutual funds are reported in Schedule CG. TDS deducted by the AMC is claimed as credit. Refund if excess TDS.</p>"
         "<p><strong>Section 115A election:</strong> NRIs can choose the concessional 20% rate on specific income heads (not applicable to equity MF capital gains, but relevant for debt-MF dividend income).</p>"
         "<p><strong>FATCA + CRS:</strong> the Indian AMC reports NRI holdings to the IRS (if US NRI) via FATCA, and to the host country tax authority via CRS (if UK / Singapore / Australia / UAE / Canada NRI). This means your Indian MF holdings become visible to your country of residence. US NRIs may face PFIC (Passive Foreign Investment Company) treatment on Indian MFs &mdash; the IRS taxes PFIC distributions and gains at punitive excess-distribution rates unless a QEF or MTM election is made annually. This is why many US NRIs avoid Indian MFs entirely.</p>"),
    ],
    faqs=[
        ("Can a US NRI invest in Indian mutual funds?",
         "Technically yes, but practically restricted. Most Indian AMCs (ICICI Prudential, SBI MF, Nippon India etc.) do not accept US-NRI subscriptions due to US SEC registration costs. Some AMCs accept with additional documentation. Even where accepted, US-NRIs face PFIC treatment under US tax law &mdash; typically making Indian MFs tax-inefficient from the US side."),
        ("Is TDS deducted on NRI mutual fund redemption?",
         "Yes. Unlike for Indian residents (where TDS is not deducted on MF redemption), the AMC deducts TDS at source for NRIs on redemption, at the applicable LTCG / STCG rate. Any excess over actual tax liability is refunded via ITR filing."),
        ("Are gains on Indian mutual funds repatriable for NRIs?",
         "Depends on the investment source: if invested from NRE / FCNR account (repatriable basis), yes freely. If invested from NRO (non-repatriable basis), repatriation is capped at USD 1M per financial year with Form 15CA + 15CB."),
        ("What is PFIC and why does it matter for US NRIs?",
         "PFIC (Passive Foreign Investment Company) is a US tax classification under IRC Section 1297. Indian mutual funds typically meet the PFIC definition (foreign corporation with 75%+ passive income). US-person holders face: punitive excess-distribution tax rates (highest US ordinary rate + interest), Form 8621 annual filing per fund, and limited remediation unless a QEF or MTM election is made. Practical effect: US NRIs often prefer US ETFs / mutual funds over Indian MFs."),
        ("Do debt mutual funds still have LTCG benefit for NRIs?",
         "No, for post-April-2023 purchases. The Finance Act 2023 removed the LTCG preferential rate on debt mutual funds &mdash; all gains are now taxed at the NRI's slab rate regardless of holding period. Pre-April-2023 holdings are grandfathered under the earlier 20%-with-indexation regime until sold."),
        ("Does BQP handle NRI mutual fund investment and ITR filing?",
         "Yes. NRI KYC with FATCA / CRS self-declaration, repatriable vs non-repatriable scheme setup, annual ITR filing with capital gains schedule, Form 15CA / 15CB for repatriation, PFIC advisory for US NRIs. Request via get-a-quote.html."),
    ],
    related=[
        ("nri-taxation-india-complete-guide.html", "Pillar", "NRI Taxation Pillar"),
        ("nre-nro-fcnr-account-tax-rules.html", "Guide", "NRE / NRO / FCNR"),
        ("nri-selling-indian-property-capital-gains.html", "Guide", "NRI Property Sale"),
    ],
    cta_headline="NRI investing in Indian mutual funds? KYC + PFIC + repatriation need thought.",
    cta_body="For US / Canada NRIs the PFIC issue is often binding; for UK / UAE / Singapore NRIs the repatriable-vs-non-repatriable scheme choice drives post-sale flexibility. We handle KYC, FATCA-CRS classification, annual ITR, and repatriation flow.",
))

# 6. NRE / NRO / FCNR account tax
write_page("nre-nro-fcnr-account-tax-rules", page(
    slug="nre-nro-fcnr-account-tax-rules",
    title="NRE vs NRO vs FCNR Account Tax Rules 2026 | NRI Banking - BQP",
    description="NRE, NRO, FCNR account rules for NRIs: Section 10(4)(ii) tax exemption, TDS on NRO interest, repatriation USD 1M, re-designation on return to India, joint-account rules. Working CA guide.",
    keywords="NRE NRO FCNR difference, NRE account tax, NRO account tax, FCNR deposit tax, NRE account interest exemption Section 10(4)(ii), re-designate NRE on return, NRO repatriation USD 1 million",
    hero_kicker="/ NRI tax &middot; Banking accounts",
    hero_title_html="NRE, NRO, FCNR &mdash; <em>the three accounts and their tax.</em>",
    hero_lead="The NRE / NRO / FCNR account trio defines how an NRI holds money with respect to India. Each account has its own tax, repatriation and re-designation rules. Mix them up and you either pay unnecessary tax or face FEMA breach. Here is the full matrix.",
    sections=[
        ("/ The three account types", "What each is for.",
         "<p><strong>NRE (Non-Resident External) Account:</strong></p>"
         "<ul>"
         "<li>Rupee-denominated.</li>"
         "<li>Funded from foreign-currency inward remittances or transfers from another NRE / FCNR account.</li>"
         "<li>Interest is fully exempt from Indian income tax under Section 10(4)(ii) &mdash; a major incentive for NRIs.</li>"
         "<li>Principal and interest are fully repatriable (no USD 1M cap).</li>"
         "<li>Joint account only with another NRI (not with a Resident).</li>"
         "</ul>"
         "<p><strong>NRO (Non-Resident Ordinary) Account:</strong></p>"
         "<ul>"
         "<li>Rupee-denominated.</li>"
         "<li>Funded from India-source income (rent, dividend, pension, salary earned in India).</li>"
         "<li>Interest is fully taxable in India as interest income &mdash; TDS at 30% + surcharge + cess deducted by the bank at source.</li>"
         "<li>Repatriation capped at USD 1 million per financial year with Form 15CA + 15CB.</li>"
         "<li>Joint account allowed with Resident Indian relative.</li>"
         "</ul>"
         "<p><strong>FCNR (Foreign Currency Non-Resident) Deposit:</strong></p>"
         "<ul>"
         "<li>Foreign-currency denominated (USD, GBP, EUR, JPY, AUD, CAD) &mdash; no exchange risk for the NRI.</li>"
         "<li>Only term deposit (1 to 5 years); no FCNR savings account.</li>"
         "<li>Interest is fully exempt from Indian income tax under Section 10(4)(ii).</li>"
         "<li>Principal and interest are fully repatriable (no USD 1M cap).</li>"
         "<li>Protects NRI corpus from INR depreciation.</li>"
         "</ul>"),
        ("/ Taxation summary table", "What India taxes.",
         "<p><strong>NRE Savings Account interest:</strong> Nil Indian tax (Section 10(4)(ii)).</p>"
         "<p><strong>NRE Fixed Deposit interest:</strong> Nil Indian tax (Section 10(4)(ii)). Important: this exemption applies only while the account holder is NRI. On becoming Resident, the exemption ends from the re-designation date.</p>"
         "<p><strong>NRO Savings Account interest:</strong> Fully taxable in India at the NRI's slab rate. The bank deducts TDS at 30% + surcharge + cess at source. If the actual slab rate is lower, refund via ITR filing.</p>"
         "<p><strong>NRO Fixed Deposit interest:</strong> Same as NRO Savings &mdash; fully taxable; TDS at 30% deducted at source.</p>"
         "<p><strong>FCNR interest:</strong> Nil Indian tax (Section 10(4)(ii)). Foreign-currency protected.</p>"
         "<p><strong>DTAA relief on NRO interest:</strong> treaty rate (typically 10-15%) overrides 30% domestic withholding if TRC + Form 10F are filed with the bank in advance. Many NRIs miss this and pay 30% unnecessarily.</p>"),
        ("/ Repatriation rules", "What leaves India and how.",
         "<p><strong>From NRE:</strong> freely repatriable; no cap. Bank processes outward remittance to the NRI's overseas account on request. Form 15CA / 15CB generally not required (NRE funds are considered foreign-origin).</p>"
         "<p><strong>From NRO:</strong> up to USD 1 million per financial year (April to March). Form 15CA + Form 15CB required.</p>"
         "<p><strong>From FCNR:</strong> freely repatriable in the foreign currency of the deposit; no exchange, no cap.</p>"
         "<p><strong>Transfer between accounts:</strong> NRE to NRO is permitted (NRE loses its 'external' character once in NRO). NRO to NRE is NOT permitted without specific authorisation &mdash; this is a common FEMA trap. NRE to FCNR and FCNR to NRE transfers are permitted.</p>"),
        ("/ On becoming Resident", "The re-designation step.",
         "<p>When the NRI returns to India permanently and becomes Resident:</p>"
         "<ul>"
         "<li>NRE and NRO accounts must be re-designated as Resident accounts within reasonable time (practically 60-90 days post-return).</li>"
         "<li>NRE Fixed Deposits can be converted to RFC (Resident Foreign Currency) deposits &mdash; useful if the NRI wants to retain the foreign-currency corpus but is now Resident.</li>"
         "<li>FCNR deposits can continue until maturity even after becoming Resident, but the exemption on interest ends from the re-designation date; interest from re-designation onward is taxable.</li>"
         "<li>RFC Account (Resident Foreign Currency): allows Returning NRIs to continue holding foreign currency balances; interest taxable but useful for ongoing foreign-currency obligations.</li>"
         "</ul>"
         "<p>Failure to re-designate: FEMA breach; bank may freeze the account; penalty under FEMA Section 13 up to 3 times the amount involved.</p>"),
    ],
    faqs=[
        ("Can I open an NRE account without visiting India?",
         "Yes. Most Indian banks (SBI, HDFC, ICICI, Axis, Kotak) offer online NRE account opening with video KYC. Required: passport, visa / residence permit of host country, overseas address proof, Indian PAN, FATCA / CRS declaration. Processing time 7-14 days typically."),
        ("Is NRE Fixed Deposit interest tax-free in India and in my country of residence?",
         "In India: yes, under Section 10(4)(ii), provided NRI status is maintained. In your country of residence: depends. US NRIs report NRE interest as taxable income to the IRS under worldwide-income rules. UK NRIs report under self-assessment. UAE residents post-Corporate-Tax may report as business income if applicable. The tax-free Indian treatment is specifically an Indian rule, not an international one."),
        ("Can I transfer money from NRO to NRE account?",
         "Only with specific authorisation under FEMA, limited to the USD 1 million per financial year cap and only after proper documentation (Form 15CA + Form 15CB confirming tax paid on the NRO balance). It is not automatic. Many NRIs mistakenly assume NRO-to-NRE is free &mdash; it is not; the transaction is treated as outward remittance from NRO."),
        ("What happens to my NRE account when I return to India?",
         "You must re-designate within 60-90 days of return. Savings component converts to Resident Savings Account (interest fully taxable from conversion). Fixed Deposits can be converted to RFC (Resident Foreign Currency) Account to retain foreign-currency denomination, or to Resident Rupee Fixed Deposits. The Section 10(4)(ii) exemption ends on the re-designation date; interest earned before is retained tax-free."),
        ("Can I claim DTAA treaty rate on NRO interest instead of 30% domestic TDS?",
         "Yes. Submit TRC + Form 10F to the bank before the TDS cycle. Bank then deducts at the treaty rate (typically 10-15% depending on your country of residence). Most NRIs don't file this and pay 30%; refund can be claimed via ITR, but takes 12-18 months to receive."),
        ("Does BQP handle NRE / NRO / FCNR setup and ongoing tax?",
         "Yes. Account setup co-ordination with Indian banks, FATCA / CRS declaration, DTAA Form 10F for reduced NRO TDS, annual ITR including NRO interest + NRE verification, Form 15CA / 15CB for repatriation, re-designation on return to India. Request via get-a-quote.html."),
    ],
    related=[
        ("nri-taxation-india-complete-guide.html", "Pillar", "NRI Taxation Pillar"),
        ("nri-returning-india-tax-rnor-transition.html", "Guide", "Returning to India (RNOR)"),
        ("nri-residential-status-rnor-india.html", "Guide", "Residential Status Rules"),
    ],
    cta_headline="Running NRE + NRO + FCNR accounts correctly saves 20-30% of annual interest.",
    cta_body="Most NRIs we onboard have been paying 30% TDS on NRO interest when a treaty-based 10-15% rate was available via Form 10F. We fix the account setup, file the Form 10F stack, handle the DTAA rate claim, and co-ordinate repatriation. Setup + first-year filing is a one-time engagement.",
))

print("Batch D complete: 6 NRI taxation pages written")
