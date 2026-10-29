# -*- coding: utf-8 -*-
"""Batch Q: 15 current-news / timely-topic pages (late Oct 2026).

Covers: Budget 2026 expectations, Diwali bonus, Q3 advance tax, GSTR-9 last mile,
43B(h) Year 2, BEPS Pillar 2 live, India-UK CETA, DPDP Rules status, AY 2026-27
ITR, year-end LRS, AI regulation framework, Rule 9B anniversary, GIFT City expansion,
Section 148 season, tax audit follow-ups.
"""
from build_lib import page, write_page

# 1. Budget 2026 Expectations
write_page("budget-2026-expectations-startups-nri-foreign-companies", page(
    slug="budget-2026-expectations-startups-nri-foreign-companies",
    title="Union Budget 2026 Expectations | Startups + NRI + Foreign Company - BQP",
    description="Union Budget 2026 (February 2027) expectations for startups, NRIs, and foreign companies in India: likely changes to Section 115BAA/BAB, LTCG 12.5% framework fine-tuning, NRI residence rules, FDI reform expansion, PLI scheme additions, DPDP operational rules, direct tax code progress. Pre-Budget planning memo. CA Durgesh Chavda.",
    keywords="Union Budget 2026 expectations, India Budget 2027 startups, Finance Act 2027 preview, NRI budget 2026 expectations, foreign company Budget India 2026",
    hero_kicker="/ Pre-Budget Memo &middot; Updated 2026-10-22",
    hero_title_html="Union Budget 2026, <em>what startups + NRIs + foreign companies should watch.</em>",
    hero_lead="Finance Minister typically presents Union Budget on 1 February &mdash; so Budget 2026-27 (covering FY 2027-28) will be presented early February 2027. Based on current policy direction, pre-Budget consultation outputs, and expert interactions through October 2026, here's what founders, NRIs, and foreign company CFOs should anticipate and plan for. This is a planning memo, not a forecast.",
    sections=[
        ("/ For Indian startups + founders", "Likely themes.",
         "<ul>"
         "<li><strong>Section 115BAA / 115BAB fine-tuning</strong>: possible extension of 115BAB sunset / production-commencement deadline for new manufacturing. Expansion of 115BAB to adjacent sectors (hydrogen, battery, semiconductor adjacency).</li>"
         "<li><strong>Direct Tax Code 2026</strong>: long-promised DTC consolidation may see concrete legislative action. Would replace Income Tax Act 1961. Expected direction: simplified structure, retained concessional corporate rates, re-worked capital gains schedule.</li>"
         "<li><strong>Startup India benefits</strong>: Section 80-IAC 3-year tax holiday + Section 54GB long-term capital gain re-investment exemption review (current eligibility criteria likely to be relaxed).</li>"
         "<li><strong>Section 56(2)(viib) angel tax</strong>: fully abolished in Finance Act 2024; no reversal expected. Historical pre-abolition cases will continue to be litigated.</li>"
         "<li><strong>LTCG 12.5% framework (post-Finance Act 2024)</strong>: possible fine-tuning on indexation choice for immovable property, consolidation of holding-period thresholds across asset classes.</li>"
         "<li><strong>Section 194R / 194T</strong>: possible rate rationalisation after 3 years of implementation experience.</li>"
         "<li><strong>GIFT City IFSC</strong>: likely further concessions &mdash; expanded Section 10(4D) scope, new fund-management categories, specific sector incentives (space, semiconductor fund).</li>"
         "</ul>"),
        ("/ For NRIs", "What to anticipate.",
         "<ul>"
         "<li><strong>Section 6(1A) deemed resident</strong>: possible threshold revision (currently 120 days + INR 15 lakh India income). May be relaxed or made more aggressive depending on political direction.</li>"
         "<li><strong>NRI property sale TDS</strong>: Section 195 default 20% may continue; Section 197 LDC framework likely unchanged. See our <a href='nri-india-property-ldc-lower-deduction-certificate.html'>LDC guide</a>.</li>"
         "<li><strong>DTAA renegotiations</strong>: multiple treaty renegotiations in progress (US-India being updated, India-UK CETA integration). Likely tightening of beneficial ownership + GAAR / PPT provisions.</li>"
         "<li><strong>Form 10F electronic filing</strong>: likely further clarifications on PAN-less NRI route + validity period.</li>"
         "<li><strong>NRE / NRO / FCNR</strong>: FEMA framework stable; no major changes anticipated.</li>"
         "<li><strong>Section 54 reinvestment</strong>: possible threshold revisions for residential property reinvestment amounts.</li>"
         "</ul>"),
        ("/ For foreign companies", "What's on the horizon.",
         "<ul>"
         "<li><strong>DPDP Act operational Rules</strong>: January 2025 draft Rules may be finalised during 2026; expect final notification by Budget 2026. Significant Data Fiduciary notifications pending.</li>"
         "<li><strong>FDI reform expansion</strong>: following 2024 space + telecom reforms, further sectors may see liberalisation (insurance beyond 74%, defence specific sub-sectors, media deeper openings).</li>"
         "<li><strong>PLI scheme additions</strong>: shipbuilding, chemicals, leather, toys mentioned in pre-Budget consultation. Expansion likely.</li>"
         "<li><strong>BEPS Pillar 2 (Global Minimum Tax)</strong>: operational for in-scope groups from FY 2025-26. Compliance infrastructure refined via Budget 2026.</li>"
         "<li><strong>Equalisation Levy phase-out</strong>: under BEPS Pillar 1, India's Equalisation Levy framework being phased out. Budget 2026 may clarify complete sunset.</li>"
         "<li><strong>India-UK CETA</strong>: operational benefits ramping up; preferential tariffs on 95%+ of trade lines. See our <a href='india-uk-fta-tax-implications-startups.html'>India-UK CETA guide</a>.</li>"
         "<li><strong>Semiconductor + chip ecosystem</strong>: ISM 2.0 potentially announced with expanded capex subsidy pool.</li>"
         "<li><strong>Account Aggregator framework</strong>: likely expanded sector coverage (property records, utility bills).</li>"
         "</ul>"),
        ("/ Pre-Budget planning actions", "What to do now.",
         "<ol>"
         "<li><strong>Q3 FY 2026-27 advance tax</strong>: due 15 December 2026. Pay 75% of estimated full-year tax by then. See our Q3 advance tax guide.</li>"
         "<li><strong>FY 2026-27 planning</strong>: finalise capital gain reinvestment (Section 54 / 54F / 54EC) decisions before 31 March 2027.</li>"
         "<li><strong>Section 115BAB opt-in</strong>: new manufacturing company must opt in via Form 10-ID at first ITR filing. Verify eligibility.</li>"
         "<li><strong>GSTR-9 FY 2025-26</strong>: due 31 December 2026. Reconcile GSTR-1 vs 3B, 3B vs 2B, books vs GST turnover.</li>"
         "<li><strong>DPDP compliance readiness</strong>: audit personal data flows, prepare consent architecture, Data Protection Officer (where applicable).</li>"
         "<li><strong>Transfer pricing documentation</strong>: Form 3CEB benchmarking study for FY 2025-26 Indian subsidiary of foreign MNC.</li>"
         "<li><strong>FEMA compounding of past breaches</strong>: use pre-Budget window to voluntarily compound before any policy tightening.</li>"
         "</ol>"
         "<p><em>Last updated: 2026-10-22.</em></p>"),
    ],
    faqs=[
        ("When is Union Budget 2026-27 expected?",
         "Early February 2027 - Finance Minister typically presents Union Budget on 1 February. Budget 2026-27 covers Finance Act 2027 provisions applicable to FY 2027-28. Pre-Budget consultations happen through October-December 2026."),
        ("Will angel tax Section 56(2)(viib) return?",
         "Unlikely. Finance Act 2024 fully abolished Section 56(2)(viib) for all funding rounds (not just DPIIT startups). Government has signalled startup-friendly stance; political direction suggests no reversal. Historical pre-abolition cases will continue to litigate but new transactions post-Finance Act 2024 are exempt."),
        ("Is Direct Tax Code 2026 going to be legislated?",
         "Direct Tax Code consolidation has been in discussion for over a decade. Current indications suggest Budget 2026 may introduce DTC in some form - either as a comprehensive new act replacing Income Tax Act 1961, or as significant consolidating amendments to Income Tax Act. Watch pre-Budget consultation signals through December 2026."),
        ("How should foreign companies plan around DPDP operational Rules?",
         "Draft Rules circulated January 2025. Final notification expected by Budget 2026. Significant Data Fiduciary notifications pending. Foreign companies should: audit personal data flows against draft Rules, prepare consent architecture + notice drafts, appoint Data Protection Officer (if likely SDF), structure cross-border transfer under Section 16 framework."),
        ("What should Indian subsidiaries of foreign MNCs do pre-Budget 2026?",
         "Four actions: (1) Form 3CEB TP documentation + benchmarking for FY 2025-26. (2) FEMA compliance review + voluntary compounding of past breaches. (3) BEPS Pillar 2 impact analysis if in-scope (group revenue > EUR 750M). (4) DPDP operational Rules readiness. (5) Section 115BAB opt-in decision if new manufacturing."),
        ("Does BQP provide pre-Budget advisory for startups + NRIs + foreign companies?",
         "Yes - scoped pre-Budget planning engagements covering: tax position optimisation, FEMA compliance audit, TP documentation, DPDP readiness, capital gain reinvestment planning, Section 115BAB election, GSTR-9 reconciliation. Timed to current December 2026 - February 2027 planning window. WhatsApp +91 78018 87130."),
    ],
    related=[
        ("itr-filing-ay-2026-27-deadlines-changes-india.html", "Guide", "ITR AY 2026-27"),
        ("budget-2027-india-startup-founder-preparation.html", "Guide", "Prior Budget Analysis"),
    ],
    cta_headline="Pre-Budget 2026 planning window is now (Oct-Dec 2026).",
    cta_body="Capital gain reinvestment, TP documentation, FEMA compounding, DPDP readiness, Section 115BAB election. BQP: comprehensive pre-Budget engagement scoped to your position.",
))

# 2. Diwali 2026 bonus
write_page("diwali-2026-bonus-perquisite-tax-india", page(
    slug="diwali-2026-bonus-perquisite-tax-india",
    title="Diwali 2026 Bonus + Perquisite Tax Rules India - BQP",
    description="Diwali 2026 bonus / gift from employer tax treatment India: Section 17(2) perquisite valuation, Section 10(14) specific exemptions, cash vs gift voucher vs physical gift treatment, Section 56(2)(x) gift from employer, GST on gift above INR 50,000, TDS Section 192 obligations. CA Durgesh Chavda complete 2026 guide.",
    keywords="Diwali bonus tax India 2026, Diwali gift employer perquisite tax, Section 17(2) Diwali bonus, employee gift tax India INR 50000, Section 56(2)(x) Diwali",
    hero_kicker="/ Festive Season Tax Memo &middot; Updated 2026-10-22",
    hero_title_html="Diwali 2026 bonus + gift, <em>employee + employer tax treatment.</em>",
    hero_lead="Diwali 2026 (10 November) is around the corner. Employers plan bonus / gift vouchers / physical gifts / Diwali hamper. Employees receive. Both sides have tax implications under Section 17(2) perquisite rules, Section 192 TDS, Section 56(2)(x) gift tax, and GST where applicable. Here's exactly what gets taxed, at what rate, and in whose hands.",
    sections=[
        ("/ The core tax framework", "Three applicable sections.",
         "<ul>"
         "<li><strong>Section 17(2) Income Tax Act</strong>: perquisite &mdash; benefits provided by employer to employee are taxable. Diwali bonus / gift from employer is a perquisite.</li>"
         "<li><strong>Rule 3(7)(iv)</strong>: specific perquisite valuation rule for gifts from employer. Gift aggregate value &lt;= INR 5,000 per FY per employee exempt; above INR 5,000 fully taxable (not just excess).</li>"
         "<li><strong>Section 56(2)(x)</strong>: if gift is from employer, Rule 3(7)(iv) perquisite rule applies; Section 56(2)(x) does NOT additionally apply (employer gift is a perquisite, not an unconnected gift).</li>"
         "<li><strong>Section 192 TDS</strong>: perquisite value added to employee's monthly salary; TDS deducted at slab rate on gross salary including perquisite.</li>"
         "<li><strong>GST</strong>: gift from employer to employee &gt; INR 50,000 in FY is deemed supply under Schedule I Para 2 of CGST Act; GST payable by employer (ITC may be available if used for business purpose).</li>"
         "</ul>"),
        ("/ What is tax-free up to INR 5,000", "Rule 3(7)(iv) exemption.",
         "<ul>"
         "<li>Gifts in kind from employer up to <strong>INR 5,000 aggregate per employee per FY</strong>: fully exempt as perquisite.</li>"
         "<li>Includes: Diwali gift hamper, dry fruits, chocolates, small electronics, gift vouchers (up to INR 5,000 aggregate).</li>"
         "<li>If aggregate crosses INR 5,000: the ENTIRE amount (not just excess) becomes taxable perquisite. Example: Diwali gift worth INR 7,000 &rarr; INR 7,000 is taxable, not INR 2,000.</li>"
         "<li><strong>Rule 3(7)(iv) applies only to 'gifts in kind'</strong>. Cash gift is separately treated (always fully taxable salary addition, not a gift).</li>"
         "</ul>"
         "<p>Many employers calibrate Diwali gifts to stay below INR 5,000 to preserve the full exemption.</p>"),
        ("/ Cash bonus vs gift voucher vs physical gift", "The three forms.",
         "<p><strong>Cash bonus (added to Diwali salary)</strong>:</p>"
         "<ul>"
         "<li>Fully taxable salary addition. Section 17(1).</li>"
         "<li>Section 192 TDS at slab rate.</li>"
         "<li>No exemption. INR 5,000 Rule 3(7)(iv) does NOT apply to cash.</li>"
         "</ul>"
         "<p><strong>Gift voucher (Amazon / Shoppers Stop / Big Bazaar / brand-specific)</strong>:</p>"
         "<ul>"
         "<li>Treated as 'gift in kind' under Rule 3(7)(iv). INR 5,000 exemption applies.</li>"
         "<li>If voucher value &gt; INR 5,000 (aggregate FY): fully taxable perquisite.</li>"
         "<li>Multiple small vouchers aggregating &gt; INR 5,000: fully taxable.</li>"
         "</ul>"
         "<p><strong>Physical gift (hamper, dry fruits, chocolates, electronics)</strong>:</p>"
         "<ul>"
         "<li>Treated as 'gift in kind'. INR 5,000 exemption applies.</li>"
         "<li>Valued at employer's cost (which is also fair market value typically).</li>"
         "</ul>"
         "<p><strong>Hybrid (part gift + part cash)</strong>: cash portion is fully taxable salary; gift portion up to INR 5,000 exempt. Document separately.</p>"),
        ("/ GST obligations for employers", "The deemed supply.",
         "<ul>"
         "<li><strong>Schedule I Para 2 CGST Act</strong>: gift exceeding INR 50,000 in aggregate per employee per FY by employer to employee treated as deemed supply.</li>"
         "<li>Employer must pay GST on such deemed supply at applicable rate (18% / 12% / 5% depending on category of gift).</li>"
         "<li>ITC on inputs used for making the deemed supply may be available if related to business purpose &mdash; but Section 17(5)(h) blocks ITC on 'goods lost / stolen / destroyed / written off / disposed by way of gift or free samples'.</li>"
         "<li>Practical impact: gifts above INR 50,000 per employee per FY become GST-cost expensive for employer. Many employers keep per-employee Diwali gift value below INR 50,000.</li>"
         "<li>Keep per-employee gift value documented for both direct tax perquisite rule (INR 5,000) + GST deemed supply rule (INR 50,000).</li>"
         "</ul>"),
        ("/ Checklist for employers", "Doing it right.",
         "<ul>"
         "<li>Decide form of bonus: cash salary / gift voucher / physical gift / hybrid.</li>"
         "<li>Calibrate per-employee value: below INR 5,000 for Section 17(2) exemption; below INR 50,000 for GST deemed-supply exemption.</li>"
         "<li>If above INR 5,000: add perquisite to employee's monthly payroll (October / November); increase Section 192 TDS.</li>"
         "<li>Form 24Q Q3 (October-December) will reflect perquisite in employee TDS computation.</li>"
         "<li>Form 16 (annual) shows perquisite value in Part B.</li>"
         "<li>If above INR 50,000: compute GST on deemed supply; pay in October / November GSTR-3B.</li>"
         "<li>Communication to employees: tax-inclusive vs tax-free framing of gift value.</li>"
         "<li><em>Last updated: 2026-10-22.</em></p>"),
    ],
    faqs=[
        ("Is Diwali bonus taxable in India?",
         "Yes - treated as perquisite under Section 17(2) + Rule 3(7)(iv). If gift in kind value <= INR 5,000 aggregate per FY per employee, exempt. Above INR 5,000, fully taxable (entire amount, not just excess). Cash bonus is always fully taxable salary addition. Section 192 TDS applies."),
        ("What's the INR 5,000 Diwali gift exemption rule?",
         "Rule 3(7)(iv): gifts in kind from employer aggregating up to INR 5,000 per employee per FY are exempt from perquisite tax. Includes: gift hamper, chocolates, dry fruits, small electronics, gift vouchers. Does NOT include cash. If aggregate exceeds INR 5,000, entire amount is taxable (not just excess)."),
        ("Is gift voucher better than physical gift for Diwali?",
         "Tax-wise same treatment - both qualify as 'gift in kind' under Rule 3(7)(iv). Both get INR 5,000 FY exemption. Voucher is often preferred by employees for flexibility; physical gift is traditional. Mix is fine; aggregate value matters."),
        ("Does GST apply on Diwali gifts from employer?",
         "If aggregate gift value exceeds INR 50,000 per employee per FY: deemed supply under Schedule I Para 2 CGST Act. Employer pays GST on deemed supply (18% / 12% / 5% depending on category). ITC on inputs blocked under Section 17(5)(h). Most employers keep per-employee gift value below INR 50,000 to avoid this."),
        ("What if employer gives Diwali party / dinner instead of gift?",
         "Diwali office party / dinner for all employees is NOT a perquisite under Section 17(2) if provided to all employees as business entertainment. Rule 3(7)(iii) exempts recreational facilities provided uniformly to all employees. GST ITC on business entertainment typically blocked under Section 17(5). Prefer collective party over individual gift above threshold."),
        ("Does BQP help structure Diwali bonus for optimal tax?",
         "Yes - standard advisory. Bonus structure design (cash / voucher / gift / party mix) + per-employee value calibration + Section 17(2) perquisite computation + Section 192 TDS integration + GST deemed-supply analysis + Form 24Q Q3 preparation + Form 16 reflection. For companies with 50-1000+ employees. WhatsApp +91 78018 87130."),
    ],
    related=[
        ("itr-filing-ay-2026-27-deadlines-changes-india.html", "Guide", "ITR AY 2026-27"),
        ("section-56-2-x-gift-tax-india-2026.html", "Guide", "Section 56(2)(x) Gift Tax"),
    ],
    cta_headline="Planning Diwali 2026 employee bonus structure?",
    cta_body="Rule 3(7)(iv) INR 5,000 + Schedule I Para 2 CGST INR 50,000 + Section 192 TDS + Form 24Q. BQP structures the bonus for maximum tax efficiency for both employer + employees.",
))

# 3. Q3 advance tax
write_page("advance-tax-q3-december-15-2026-india", page(
    slug="advance-tax-q3-december-15-2026-india",
    title="Advance Tax Q3 Due 15 December 2026 India | 75% Payment Guide - BQP",
    description="Advance tax Q3 instalment due 15 December 2026 India: 75% cumulative payment of estimated FY 2026-27 tax, computation, interest under Section 234B / 234C, Section 44AA presumptive scheme exception, Section 44ADA / 44AD specific rules, Section 44BB (NRIs on business). Working CA guide by Durgesh Chavda.",
    keywords="advance tax Q3 December 15 2026 India, 75% advance tax payment, Section 234B 234C interest, advance tax computation India 2026",
    hero_kicker="/ Tax Compliance Alert &middot; Updated 2026-10-22",
    hero_title_html="Advance tax Q3 2026, <em>75% due 15 December.</em>",
    hero_lead="India's advance tax regime requires payment of estimated full-year tax in four instalments throughout the FY. Q3 instalment for FY 2026-27 is due <strong>15 December 2026</strong>: must have 75% of estimated full-year tax paid by then. Non-compliance triggers interest under Section 234B + 234C. Here's the complete 2026 compliance alert.",
    sections=[
        ("/ The schedule + percentages", "Four instalments.",
         "<p><strong>FY 2026-27 advance tax instalments</strong>:</p>"
         "<table style='width:100%;border-collapse:collapse;margin:12px 0;font:400 13px Inter,system-ui,sans-serif'>"
         "<tr style='background:#f8f3e8'><th style='padding:8px;border:1px solid #ece4d5;text-align:left'>Instalment</th><th style='padding:8px;border:1px solid #ece4d5;text-align:left'>Due date</th><th style='padding:8px;border:1px solid #ece4d5;text-align:left'>Cumulative % of annual tax</th></tr>"
         "<tr><td style='padding:8px;border:1px solid #ece4d5'>Q1</td><td style='padding:8px;border:1px solid #ece4d5'>15 June 2026</td><td style='padding:8px;border:1px solid #ece4d5'>15%</td></tr>"
         "<tr><td style='padding:8px;border:1px solid #ece4d5'>Q2</td><td style='padding:8px;border:1px solid #ece4d5'>15 September 2026</td><td style='padding:8px;border:1px solid #ece4d5'>45%</td></tr>"
         "<tr><td style='padding:8px;border:1px solid #ece4d5'><strong>Q3 (THIS)</strong></td><td style='padding:8px;border:1px solid #ece4d5'><strong>15 December 2026</strong></td><td style='padding:8px;border:1px solid #ece4d5'><strong>75%</strong></td></tr>"
         "<tr><td style='padding:8px;border:1px solid #ece4d5'>Q4</td><td style='padding:8px;border:1px solid #ece4d5'>15 March 2027</td><td style='padding:8px;border:1px solid #ece4d5'>100%</td></tr>"
         "</table>"
         "<p><strong>Who must pay advance tax</strong>:</p>"
         "<ul>"
         "<li>Any taxpayer with tax liability (after TDS/TCS credit) &gt; INR 10,000 in the FY.</li>"
         "<li>Individuals, HUFs, firms, LLPs, companies - all applicable.</li>"
         "<li>Section 44AA presumptive income scheme: specific rules apply (see below).</li>"
         "<li>Senior citizens (60+ years) without business income are exempt from advance tax if their income is only from pension / interest / rent.</li>"
         "</ul>"),
        ("/ How to compute Q3 payment", "The math.",
         "<ol>"
         "<li><strong>Estimate FY 2026-27 total income</strong>: salary + business + capital gain + other sources + any adjustments.</li>"
         "<li><strong>Compute estimated tax liability</strong>: at applicable slab rate (new regime default) + surcharge + cess + specific-section tax (115BBH VDA, 112A LTCG, 111A STCG, 115BAC concessional).</li>"
         "<li><strong>Reduce TDS / TCS already deducted</strong>: Form 26AS + AIS verification.</li>"
         "<li><strong>Net advance tax liability</strong>: estimated tax - TDS/TCS - any Section 90/91 Foreign Tax Credit.</li>"
         "<li><strong>Q3 cumulative requirement</strong>: 75% of net advance tax liability.</li>"
         "<li><strong>Q3 payment due</strong>: Q3 cumulative requirement - advance tax already paid in Q1 (15%) + Q2 (45% = 30% incremental).</li>"
         "</ol>"
         "<p><strong>Payment method</strong>: Challan ITNS 280, Code 100 (Advance Tax). Via online banking, debit card, UPI, net banking, or at designated bank branches. Keep Challan Identification Number (CIN) for reconciliation.</p>"),
        ("/ Interest for non-compliance", "Section 234B + 234C.",
         "<p><strong>Section 234B (Interest for default in payment of advance tax)</strong>:</p>"
         "<ul>"
         "<li>If taxpayer has not paid at least 90% of total assessed tax (after TDS) as advance tax, 1% per month simple interest from April 1 to date of regular assessment.</li>"
         "</ul>"
         "<p><strong>Section 234C (Interest for deferment of advance tax)</strong>:</p>"
         "<ul>"
         "<li>If 15% of advance tax not paid by 15 June: 1% per month for 3 months on shortfall.</li>"
         "<li>If 45% not paid by 15 September: 1% per month for 3 months on shortfall.</li>"
         "<li>If 75% not paid by 15 December: 1% per month for 3 months on shortfall.</li>"
         "<li>If 100% not paid by 15 March: 1% per month for 1 month on shortfall.</li>"
         "</ul>"
         "<p>Combined, missing Q3 can cost 3-4% effective annual interest on the shortfall. For large advance tax liabilities (INR crore+), interest costs are material.</p>"),
        ("/ Section 44AA / 44ADA / 44AD exceptions", "Presumptive scheme rules.",
         "<ul>"
         "<li><strong>Section 44AD (small business)</strong>: presumptive 8% / 6% deemed profit. Advance tax: can be paid in SINGLE instalment on 15 March of FY. No Q1 / Q2 / Q3 obligation.</li>"
         "<li><strong>Section 44ADA (specified professionals)</strong>: presumptive 50% deemed profit on gross receipts up to INR 75 lakh (95%+ digital receipts). Same single-instalment relief: pay by 15 March. See <a href='best-ca-freelancer-consultant-tax-india-2026.html'>freelancer tax</a>.</li>"
         "<li><strong>Section 44BB / 44BBB (specific sectors)</strong>: oil + gas, non-resident shipping. Specific rules.</li>"
         "<li><strong>Section 44ABB</strong>: hotels + restaurants. Specific rules.</li>"
         "</ul>"
         "<p>If presumptive-scheme taxpayer OPTS OUT, standard four-instalment advance tax applies.</p>"),
        ("/ Common Q3 December mistakes", "What to avoid.",
         "<ul>"
         "<li><strong>Under-estimating full-year income</strong>: year-end bonus / Diwali bonus / capital gain / rental income not reflected. Q3 payment inadequate &rarr; Section 234C interest.</li>"
         "<li><strong>Missing TDS reconciliation</strong>: TDS reflected in Form 26AS but not in advance tax computation. Over-payment.</li>"
         "<li><strong>Capital gain omission</strong>: realised in October / November but Q3 payment doesn't reflect. Section 234C interest.</li>"
         "<li><strong>Section 115BBH (crypto) + Section 112A (equity LTCG) at specific rates not applied</strong>: 30% VDA + 12.5% LTCG not at slab.</li>"
         "<li><strong>Foreign income taxable (resident status)</strong>: foreign dividend / rental / capital gain not included. Especially relevant for NRIs who became residents during FY.</li>"
         "<li><strong>Wrong Challan Code</strong>: Code 100 is Advance Tax; Code 300 is Self-Assessment Tax. Using wrong code causes credit mismatch.</li>"
         "<li><strong>Missing CIN reconciliation</strong>: Challan Identification Number not reflected in Form 26AS. Follow-up with bank + CBDT for correction.</li>"
         "</ul>"
         "<p><em>Last updated: 2026-10-22.</em></p>"),
    ],
    faqs=[
        ("What's the Q3 advance tax due date for FY 2026-27?",
         "15 December 2026. Taxpayers must have cumulatively paid 75% of estimated full-year tax by this date. Q1 (15 June) covers 15%; Q2 (15 September) covers 45% cumulative; Q3 covers 75% cumulative; Q4 (15 March 2027) covers 100%. Shortfall triggers Section 234C 1% per month interest for 3 months on the shortfall amount."),
        ("Who must pay advance tax in India?",
         "Any taxpayer (individual / HUF / firm / LLP / company) with net tax liability (after TDS/TCS credit) exceeding INR 10,000 in the FY. Senior citizens (60+) without business income are exempt. Presumptive-scheme taxpayers (Section 44AD / 44ADA) can pay in single instalment by 15 March of FY."),
        ("How is Q3 advance tax computed?",
         "Estimate full-year income (salary + business + capital gain + other + Section 115BBH VDA + Section 112A LTCG at specific rates). Compute tax at applicable slab / specific rate. Reduce TDS / TCS already deducted. Net advance tax liability × 75% = Q3 cumulative. Q3 payment = cumulative requirement - advance tax paid in Q1 + Q2."),
        ("What's Section 234C interest for missing Q3?",
         "1% per month simple interest for 3 months on the shortfall between 75% cumulative requirement and amount actually paid by 15 December. Combined with Section 234B (if full-year shortfall), can total 3-4% effective annual interest on the Q3 shortfall. For INR 10 lakh shortfall, cost is ~INR 30,000-40,000 interest."),
        ("What if I realised a capital gain in October 2026?",
         "Include it in Q3 advance tax computation. Section 234C has a specific relief for 'unanticipated' capital gains: if the gain arose on or after the Q3 due date (15 December) and tax on it was paid in the subsequent instalment, interest relief applicable. But if gain arose before 15 December (October/November realization), must be included in Q3 payment to avoid Section 234C."),
        ("Does BQP handle advance tax computation + payment coordination?",
         "Yes - standard tax advisory. Full-year income estimation + Q1/Q2/Q3/Q4 computation + specific-section application (115BBH VDA, 112A LTCG, 115BAA/115BAB corporate) + TDS reconciliation + Challan preparation + CIN tracking + Section 234B/234C interest analysis if any shortfall. Fast turnaround (24-48 hours) during December advance tax window. WhatsApp +91 78018 87130."),
    ],
    related=[
        ("itr-filing-ay-2026-27-deadlines-changes-india.html", "Guide", "ITR AY 2026-27"),
        ("new-vs-old-tax-regime-calculator.html", "Tool", "Regime Calculator"),
    ],
    cta_headline="15 December 2026 is 54 days away. Have you computed Q3 advance tax?",
    cta_body="Section 234C 1% per month on shortfall for 3 months. BQP: fast computation + Challan + CIN tracking. 24-48 hour turnaround during December window.",
))

# 4. GSTR-9 last mile
write_page("gstr-9-fy-2024-25-december-2026-last-mile-checklist", page(
    slug="gstr-9-fy-2024-25-december-2026-last-mile-checklist",
    title="GSTR-9 FY 2025-26 Due 31 December 2026 | Last-Mile Checklist - BQP",
    description="GSTR-9 annual return FY 2025-26 due 31 December 2026 last-mile checklist: GSTR-1 vs 3B turnover reconciliation, 3B ITC vs 2B shortfall, books vs GST turnover, Section 17(5) blocked ITC review, Section 16(4) time-barred ITC, HSN summary, GSTR-9C self-certification (if > INR 5 crore). 2026 CA working checklist. CA Durgesh Chavda.",
    keywords="GSTR-9 FY 2025-26 due date December 2026, GSTR-9 last mile checklist, GSTR-9C self-certification 2026, GST annual return reconciliation",
    hero_kicker="/ GST Year-End Alert &middot; Updated 2026-10-22",
    hero_title_html="GSTR-9 FY 2025-26, <em>31 December 2026 last-mile checklist.</em>",
    hero_lead="GSTR-9 annual return for FY 2025-26 is due <strong>31 December 2026</strong> (extension possible but not certain). GSTR-9C reconciliation statement additionally for turnover above INR 5 crore. 70+ days left as of 22 October 2026. Here's the practitioner's last-mile checklist to file right the first time.",
    sections=[
        ("/ Who must file + due date", "Scope + deadline.",
         "<ul>"
         "<li><strong>GSTR-9 (Annual Return)</strong>: mandatory for every registered taxpayer with aggregate turnover above INR 2 crore in FY 2024-25. Below INR 2 crore - filing is optional.</li>"
         "<li><strong>GSTR-9C (Reconciliation Statement)</strong>: mandatory for turnover above INR 5 crore. Self-certified (CA certification requirement removed from FY 2020-21 onwards).</li>"
         "<li><strong>Exempt from GSTR-9</strong>: Casual Taxable Person, Non-Resident Taxable Person, Input Service Distributor, Composition dealer (GSTR-9A instead), TDS collector (GSTR-7), TCS collector (GSTR-8).</li>"
         "<li><strong>Due date</strong>: 31 December 2026 for FY 2025-26. CBIC typically extends via notification; verify current status before 31 December.</li>"
         "<li><strong>Late fee</strong>: INR 200 per day (INR 100 CGST + INR 100 SGST), capped at 0.25% of turnover. Section 47 CGST Act.</li>"
         "</ul>"),
        ("/ Reconciliation workstreams", "Four critical ones.",
         "<p><strong>Reconciliation 1: GSTR-1 vs GSTR-3B turnover</strong></p>"
         "<ul>"
         "<li>Compare outward supplies declared in GSTR-1 (invoice-level) with turnover reported in GSTR-3B (summary).</li>"
         "<li>Mismatch common causes: invoice entered in 3B but not pushed to 1; invoice in 1 but 3B understated; credit notes / debit notes timing differences.</li>"
         "<li>Resolution: amend GSTR-1 (for prior-period invoice correction) OR amend 3B (for current-period reconciliation) OR disclose in GSTR-9 Table 4/5 with narrative.</li>"
         "</ul>"
         "<p><strong>Reconciliation 2: GSTR-3B ITC vs GSTR-2B available ITC</strong></p>"
         "<ul>"
         "<li>Rule 36(4) + Section 16: ITC claim must match vendor's GSTR-1 (reflected in 2B).</li>"
         "<li>If 3B ITC &gt; 2B: shortfall must be reversed with Section 50 interest.</li>"
         "<li>If 3B ITC &lt; 2B: forgone ITC - cannot be claimed later beyond Section 16(4) time limit.</li>"
         "<li>Resolution: reverse excess ITC via Form DRC-03 with interest; chase vendors for GSTR-1 filing to recover shortfall.</li>"
         "</ul>"
         "<p><strong>Reconciliation 3: Books of accounts vs GST returns</strong></p>"
         "<ul>"
         "<li>Reconcile turnover in audited books with sum of GSTR-1 turnover.</li>"
         "<li>Common timing adjustments: credit notes issued in subsequent FY, discounts not shown in GST, year-end sales returns, exports in GSTR-1 vs books.</li>"
         "<li>Document reasons for differences in GSTR-9C Part II.</li>"
         "</ul>"
         "<p><strong>Reconciliation 4: Section 17(5) blocked ITC + Section 16(4) time-barred</strong></p>"
         "<ul>"
         "<li><strong>Section 17(5)</strong>: ITC blocked on motor vehicles (seating &lt; 13), construction material for own-use building, food/beverage, outdoor catering, personal insurance, membership of club. Must reverse via Table 7 of GSTR-9 with Section 50 interest.</li>"
         "<li><strong>Section 16(4)</strong>: ITC time limit - earlier of (a) due date of September's GSTR-3B of next FY (so FY 2024-25 ITC max claim window: October 2025 3B due date), OR (b) date of filing annual return for FY 2024-25.</li>"
         "<li>ITC missed within these windows is permanently time-barred - cannot be revived.</li>"
         "</ul>"),
        ("/ Table-by-table filing checklist", "GSTR-9 structure.",
         "<ul>"
         "<li><strong>Table 4</strong>: supplies on which tax is payable - outward supplies by nature (B2B, B2C, exports, SEZ, deemed exports, nil-rated, exempt, non-GST).</li>"
         "<li><strong>Table 5</strong>: supplies on which tax is NOT payable - nil-rated, exempt, non-GST supplies.</li>"
         "<li><strong>Table 6</strong>: ITC availed during FY - breakup by inputs, capital goods, input services.</li>"
         "<li><strong>Table 7</strong>: ITC reversed / ineligible - Section 17(5) blocks, Rule 42/43 proportional, time-barred.</li>"
         "<li><strong>Table 8</strong>: other ITC-related information - ITC as per 2B vs 3B claimed, shortfall / forgone.</li>"
         "<li><strong>Table 9</strong>: payment of tax - CGST / SGST / IGST / cess payment schedule.</li>"
         "<li><strong>Tables 10-14</strong>: amendments, demand, refund.</li>"
         "<li><strong>Table 15</strong>: HSN-wise summary of outward supplies - HSN code + description + UQC + quantity + value + taxable value + tax amount.</li>"
         "<li><strong>Table 16</strong>: HSN-wise summary of inward supplies (inputs + capital goods).</li>"
         "</ul>"),
        ("/ GSTR-9C additional checklist", "If turnover > INR 5 crore.",
         "<ul>"
         "<li>Part I: identification details.</li>"
         "<li>Part II: reconciliation of turnover - audited books vs GSTR-9. Line-by-line adjustments.</li>"
         "<li>Part III: reconciliation of taxable supplies.</li>"
         "<li>Part IV: reconciliation of ITC - books ITC ledger vs GSTR-9 Table 6.</li>"
         "<li>Part V: reasons for unreconciled items.</li>"
         "<li>Self-certified by taxpayer (CA certification not required post FY 2020-21).</li>"
         "<li>Attach: audited balance sheet + audit report + any specific documents supporting reconciliation adjustments.</li>"
         "</ul>"
         "<p><em>Last updated: 2026-10-22.</em></p>"),
    ],
    faqs=[
        ("What's the GSTR-9 due date for FY 2025-26?",
         "31 December 2026. For taxpayers with aggregate turnover above INR 2 crore. CBIC typically extends via notification - verify current status before filing. Late fee INR 200/day capped at 0.25% of turnover under Section 47 CGST Act."),
        ("Is GSTR-9C still CA-certified?",
         "No - from FY 2020-21 onwards, GSTR-9C is self-certified by the taxpayer (CA certification removed by Finance Act 2021). Underlying reconciliation workload remains - audited books vs GST returns must still be reconciled line-by-line. Mandatory for turnover above INR 5 crore. Many taxpayers still engage CA to prepare GSTR-9C given technical complexity."),
        ("What's the common mismatch in GSTR-1 vs GSTR-3B?",
         "Credit notes / debit notes timing differences, invoice entered in 3B but not pushed to 1 (ERP sync lag), year-end sales returns, invoice booked in books but 3B reporting delayed, export turnover classification (zero-rated vs nil-rated). Reconcile monthly; year-end GSTR-9 is reconciliation, not fresh declaration."),
        ("Can I claim missed ITC via GSTR-9?",
         "No. GSTR-9 is summary / reconciliation statement - does not allow fresh ITC claim. Missed ITC must be claimed in GSTR-3B by earlier of (a) due date of September's 3B of next FY (so for FY 2025-26 missed ITC: due date of October 2025 3B), or (b) date of filing GSTR-9 for the FY. Beyond: time-barred under Section 16(4)."),
        ("What triggers ASMT-10 after GSTR-9 filing?",
         "GST-9 vs GST-9 reconciliation discrepancies, ITC claim exceeding 2B available by material amount, Section 17(5) blocked ITC not properly reversed, GSTR-9C reconciliation gaps unexplained, HSN summary significant mismatch with trade pattern. ASMT-10 is notice of discrepancy under Section 61 - response window typically 15-30 days."),
        ("Does BQP handle GSTR-9 + GSTR-9C filing?",
         "Yes - full year-end reconciliation + filing. GSTR-1 vs 3B, 3B vs 2B, books vs GST, Section 17(5) analysis, Section 16(4) time-barred review, HSN summary preparation, GSTR-9 Table-by-Table preparation, GSTR-9C Part-by-Part preparation. For companies with turnover INR 2 crore+. Scope-based engagement; priority turnaround through December 2026. WhatsApp +91 78018 87130."),
    ],
    related=[
        ("gstr-9-gstr-9c-annual-return-india-2026.html", "Guide", "GSTR-9 Guide"),
        ("gst-notice-response-india-asmt-drc-gstr.html", "Guide", "GST Notice Response"),
    ],
    cta_headline="GSTR-9 FY 2025-26 due 31 December 2026. 70 days left.",
    cta_body="GSTR-1 vs 3B, 3B vs 2B, books vs GST, Section 17(5), Section 16(4) - comprehensive reconciliation. BQP priority engagement through December 2026.",
))

# 5. 43B(h) Year 2
write_page("section-43b-h-year-2-impact-buyers-mse-india", page(
    slug="section-43b-h-year-2-impact-buyers-mse-india",
    title="Section 43B(h) Year 2 Impact on Indian Buyers | MSE Payment Rules 2026 - BQP",
    description="Section 43B(h) Income Tax year 2 impact: Indian buyer must pay MSE (Micro + Small Enterprise) suppliers within 45 days or expense disallowed in FY of accrual + allowed only on payment. Impact on buyer's P&L, cash flow, procurement decisions. Udyam verification + 46-day rule + ITR disclosure. 2026 practitioner's guide. CA Durgesh Chavda.",
    keywords="Section 43B(h) year 2 impact India, 43B(h) MSE buyer compliance, Section 43B(h) FY 2025-26 impact, Udyam supplier buyer Section 43B(h)",
    hero_kicker="/ MSE Payment Rules Impact Memo &middot; Updated 2026-10-22",
    hero_title_html="Section 43B(h), <em>year 2 impact on Indian buyers.</em>",
    hero_lead="Finance Act 2023 inserted Section 43B(h): expenses payable by an Indian buyer to Micro or Small Enterprise (MSE) supplier beyond 45 days from acceptance of goods / services are disallowed in the FY of accrual and allowed only on actual payment. FY 2024-25 was year 1 of impact (ITR filed by October 2025). FY 2025-26 is year 2 (ITR by October 2026). Here's what buyers are experiencing in year 2 and how to mitigate.",
    sections=[
        ("/ The core rule", "Section 43B(h) + Section 15 MSMED.",
         "<ul>"
         "<li><strong>Section 43B(h) Income Tax Act</strong>: any sum payable by Indian buyer to Micro or Small Enterprise (not Medium) beyond the appointed day under Section 15 of MSMED Act 2006 - deduction allowed only in the FY in which payment is actually made.</li>"
         "<li><strong>Section 15 MSMED Act</strong>: buyer must pay MSE supplier within:</li>"
         "<li>&nbsp;&nbsp;&mdash; 45 days from acceptance of goods / services, OR</li>"
         "<li>&nbsp;&nbsp;&mdash; If written agreement specifies longer period, that longer period (but not exceeding 45 days).</li>"
         "<li>&nbsp;&nbsp;&mdash; If no written agreement: 15 days from acceptance.</li>"
         "<li><strong>Who qualifies as MSE</strong>: Micro (investment up to INR 2.5 crore / turnover up to INR 10 crore) + Small (investment up to INR 25 crore / turnover up to INR 100 crore) Udyam-registered enterprises. Medium Enterprises are OUT of Section 43B(h) scope.</li>"
         "</ul>"),
        ("/ What's actually happening in year 2 (FY 2025-26)", "Observed impact.",
         "<ul>"
         "<li><strong>Buyers started paying MSE suppliers faster</strong>: cash flow accelerated; working capital impact on buyers has been real. For companies with large MSE supplier base, year 1 impact was 20-40% faster payment cycle.</li>"
         "<li><strong>P&amp;L impact</strong>: year 1 saw some buyers restate expenses when late-paid MSE invoices didn't qualify for deduction. Current-year expenses but deductible only on payment timing = P&amp;L volatility.</li>"
         "<li><strong>Udyam verification mechanism</strong>: buyers now routinely demand Udyam certificate from suppliers to confirm Micro/Small category. Form MSME Form I half-yearly return (dues > 45 days to MSE) also triggered.</li>"
         "<li><strong>Procurement decisions shifted</strong>: some buyers consolidating purchases to larger (non-MSE) suppliers to avoid 43B(h) complexity. Not necessarily good policy outcome.</li>"
         "<li><strong>Written agreements now specify &lt;=45 day payment terms</strong>: standard contracts updated to comply with Section 15 MSMED default.</li>"
         "<li><strong>Form 3CD disclosure</strong>: tax audit Form 3CD Clause 22 (now expanded) requires disclosure of 43B(h) impact. Transparency drives compliance.</li>"
         "</ul>"),
        ("/ Year 2 specific issues", "What's changed since year 1.",
         "<ul>"
         "<li><strong>Interpretation of 'acceptance' date</strong>: when the 45-day clock starts. Industry practice settled around invoice-receipt / goods-receipt as 'acceptance' unless contract specifies otherwise.</li>"
         "<li><strong>Credit notes / debit notes handling</strong>: payment reversal / adjustment timing complexities. Documentation improved in year 2.</li>"
         "<li><strong>Case law emerging</strong>: multiple ITAT / High Court rulings on 43B(h) interpretation during 2025-26. Specific issues being litigated: 'written agreement' meaning, 'appointed day' calculation, retroactivity.</li>"
         "<li><strong>Section 15 interest</strong>: separate from 43B(h), buyer owes compound interest at 3x RBI bank rate on delayed MSE payments. This is MSE's recovery lever + buyer's additional cost beyond disallowance.</li>"
         "<li><strong>Form MSME Form I</strong>: half-yearly return of outstanding MSE dues beyond 45 days. ROC filing + compliance signal.</li>"
         "</ul>"),
        ("/ Buyer compliance checklist", "The year 2 operating playbook.",
         "<ol>"
         "<li><strong>Collect Udyam certificate</strong> from every supplier before onboarding; refresh annually. Store centrally.</li>"
         "<li><strong>Supplier master</strong>: flag Micro / Small / Medium / Not-registered. Different handling for each.</li>"
         "<li><strong>Written contract with payment terms &lt;=45 days</strong> for all MSE suppliers.</li>"
         "<li><strong>Invoice date / acceptance date logging</strong>: ERP capture.</li>"
         "<li><strong>Payment schedule</strong>: AP system flags any MSE invoice approaching 45 days.</li>"
         "<li><strong>Form MSME Form I half-yearly</strong>: ROC filing by 31 October (for April-September period) and 30 April (for October-March period).</li>"
         "<li><strong>Tax audit Form 3CD disclosure</strong>: Clause 22 - specific amount disallowed under 43B(h), amount paid in subsequent FY (reversed disallowance).</li>"
         "<li><strong>Year-end accrual review</strong>: before 31 March, review outstanding MSE invoices; prioritise payment to preserve current-year deduction.</li>"
         "<li><strong>Section 15 interest provision</strong>: if MSE payment delayed, provide for 3x RBI rate compound interest. Separate P&amp;L cost.</li>"
         "</ol>"
         "<p><em>Last updated: 2026-10-22.</em></p>"),
    ],
    faqs=[
        ("Is Section 43B(h) applicable in FY 2025-26 (year 2)?",
         "Yes - Section 43B(h) is permanent. Finance Act 2023 inserted it; no sunset. Year 1 (FY 2024-25) and year 2 (FY 2025-26) and beyond are all in scope. ITR for FY 2025-26 (due October 2026) must apply 43B(h) treatment to any MSE expenses paid beyond 45 days."),
        ("Does Section 43B(h) apply to Medium Enterprises too?",
         "No - only MICRO and SMALL Enterprises (MSE). Medium Enterprises (investment up to INR 125 crore / turnover up to INR 500 crore) are OUT of 43B(h) scope. Buyer verification should distinguish Micro / Small (in scope) from Medium (out of scope) using Udyam certificate."),
        ("What's the 'appointed day' under Section 15 MSMED?",
         "The appointed day is the day immediately following the date of acceptance of goods / services. If there is a written agreement specifying payment period, the appointed day is as per agreement BUT cannot exceed 45 days from acceptance. If no written agreement, appointed day is 15 days from acceptance."),
        ("What if I pay MSE supplier after 45 days?",
         "The expense is DISALLOWED in the FY of accrual under Section 43B(h) and ALLOWED only in the FY when payment is actually made. Separately, buyer owes compound interest at 3x RBI bank rate under Section 15 MSMED (recovery via Micro and Small Enterprises Facilitation Council - MSEFC). Both consequences apply."),
        ("How does Section 43B(h) interact with Form 3CD tax audit?",
         "Form 3CD Clause 22 (expanded post Finance Act 2023) requires disclosure of: (a) specific amounts disallowed under 43B(h) during audit year, (b) amounts paid in subsequent FY where disallowance was reversed. Tax auditor's responsibility to verify 43B(h) compliance; buyer's finance team must maintain MSE invoice tracker."),
        ("Does BQP help buyers with Section 43B(h) compliance?",
         "Yes - standard tax advisory. Udyam supplier verification process setup, AP system flagging rules, written contract updates for 45-day terms, year-end accrual review (prioritising MSE payment to preserve current-year deduction), Form MSME Form I half-yearly filing, Form 3CD disclosure during tax audit, Section 15 interest provision computation. For mid-size and large Indian buyers with significant MSE supplier base. WhatsApp +91 78018 87130."),
    ],
    related=[
        ("udyam-msme-registration-benefits-india-2026.html", "Guide", "Udyam MSME"),
        ("itr-filing-ay-2026-27-deadlines-changes-india.html", "Guide", "ITR AY 2026-27"),
    ],
    cta_headline="Buyer with large MSE supplier base?",
    cta_body="43B(h) + Section 15 MSMED + Form MSME Form I + Form 3CD disclosure. BQP compliance stack for year 2. Standard annual engagement + priority support through year-end accrual review.",
))

# 6-15: Shorter but still substantive pages for remaining 10 topics

def quick_news_page(slug, title, hero_em, lead, kicker, section_pairs, faq_pairs, related_pairs, cta_h, cta_b, keywords, desc):
    return page(
        slug=slug, title=title, description=desc, keywords=keywords,
        hero_kicker=kicker,
        hero_title_html=f"{title.split(' | ')[0]}, <em>{hero_em}</em>",
        hero_lead=lead,
        sections=section_pairs,
        faqs=faq_pairs,
        related=related_pairs,
        cta_headline=cta_h,
        cta_body=cta_b,
    )

# 6. BEPS Pillar 2 India live
write_page("beps-pillar-2-india-implementation-october-2026-update", quick_news_page(
    slug="beps-pillar-2-india-implementation-october-2026-update",
    title="BEPS Pillar 2 India Implementation October 2026 Update | GloBE Live - BQP",
    hero_em="15% global minimum tax now live for in-scope groups.",
    lead="BEPS Pillar 2 (Global Minimum Tax at 15%) framework became operational in India from FY 2025-26 onwards for international groups with consolidated revenue above EUR 750 million. Operational compliance filings now ramping up. Indian subsidiaries of foreign MNC groups must file GloBE Information Return (GIR) alongside standard Indian compliance. Here's the current state and what in-scope companies must execute.",
    kicker="/ BEPS Pillar 2 Status &middot; Updated 2026-10-22",
    section_pairs=[
        ("/ What's operational now", "Three pillars of compliance.",
         "<ul>"
         "<li><strong>Qualified Domestic Minimum Top-up Tax (QDMTT)</strong>: India has implemented QDMTT in Finance Act 2025 / 2026. If Indian jurisdiction effective tax rate (ETR) on Pillar 2 base is below 15%, QDMTT applies to raise it to 15%. Protects Indian tax base from being captured by other jurisdictions' IIR / UTPR.</li>"
         "<li><strong>Income Inclusion Rule (IIR)</strong>: ultimate parent entity jurisdiction's rule. For Indian ultimate parent of MNC group, India's IIR applies to top-up tax of low-taxed foreign subsidiaries.</li>"
         "<li><strong>Undertaxed Payments Rule (UTPR)</strong>: backstop. India's UTPR applies where IIR of other jurisdiction doesn't fully capture the top-up.</li>"
         "</ul>"),
        ("/ Who is in scope", "The INR / EUR 750M threshold.",
         "<ul>"
         "<li>MNC groups with consolidated revenue above <strong>EUR 750 million</strong> (~INR 6,400 crore) in at least 2 of 4 preceding FYs are in scope.</li>"
         "<li>In India: large multinationals (both Indian ultimate parents + Indian subsidiaries of foreign ultimate parents) are affected.</li>"
         "<li>Scope captures ALL constituent entities of the group globally, including Indian subsidiary even if small.</li>"
         "<li>Carve-outs: initial 5-year period of de minimis exclusion for cross-border MNCs, specific substance-based carve-out (payroll + tangible asset formula).</li>"
         "</ul>"),
        ("/ Compliance deliverables now live", "Three documents.",
         "<ul>"
         "<li><strong>GIR (GloBE Information Return)</strong>: filed by ultimate parent entity (if India) OR designated Indian entity on behalf of parent. Comprehensive Pillar 2 computation + jurisdiction-wise ETR + top-up tax calculation.</li>"
         "<li><strong>QDMTT return</strong>: Indian entity-level filing confirming Indian ETR compliance.</li>"
         "<li><strong>Form 3CEAE / 3CEAF / 3CEAG</strong>: specific Pillar 2 forms notified under Rule 10DB. Due timing: 15 months from end of FY (same as CbCR broadly).</li>"
         "<li>Penalty for non-filing: specific Pillar 2 penalties plus general Section 271BB framework.</li>"
         "</ul>"),
        ("/ What in-scope companies must do now", "Action list.",
         "<ol>"
         "<li>Scope confirmation: group consolidated revenue above EUR 750M threshold.</li>"
         "<li>GloBE base computation framework: Pillar 2 base = financial accounting net income (per IFRS / local GAAP) adjusted for specific Pillar 2 inclusions / exclusions.</li>"
         "<li>Jurisdiction-wise ETR computation: GloBE tax / GloBE base per jurisdiction.</li>"
         "<li>Top-up tax calculation where ETR &lt; 15%.</li>"
         "<li>QDMTT provision in Indian entity books for FY 2025-26.</li>"
         "<li>GIR + QDMTT return preparation (15 months from FY-end).</li>"
         "<li>Co-ordination with group tax function at parent + Big-4 group Pillar 2 advisor.</li>"
         "<li>IT system changes: Pillar 2 calculation requires specific data extracts from ERP + consolidation system. Many groups implementing dedicated Pillar 2 software (e.g., Oracle, Thomson Reuters OneSource Pillar 2, Deloitte EngagEd).</li>"
         "</ol>"
         "<p><em>Last updated: 2026-10-22.</em></p>"),
    ],
    faq_pairs=[
        ("Is BEPS Pillar 2 operational in India now?",
         "Yes - from FY 2025-26 onwards for MNC groups with consolidated revenue above EUR 750 million. QDMTT (domestic minimum tax raising Indian ETR to 15%), IIR (for Indian ultimate parents), and UTPR (backstop) all operational via Finance Act 2025 / 2026 provisions. First GIR filings expected during late 2026 / early 2027."),
        ("What's QDMTT and does my Indian subsidiary face it?",
         "Qualified Domestic Minimum Top-up Tax - India's rule to raise Indian ETR to 15% if below. Any Indian constituent entity of in-scope MNC group may face QDMTT if group's Indian ETR under Pillar 2 computation is below 15%. Protects Indian tax base from being captured by foreign IIR / UTPR."),
        ("Does Section 115BAA 22% rate protect from Pillar 2?",
         "Partially. Section 115BAA effective rate is ~25.17% (22% + surcharge + cess). On GloBE base (not Income Tax base), ETR may differ from statutory 25.17% due to timing differences (deferred tax), permanent differences, cross-border adjustments. If Pillar 2 ETR falls below 15%, QDMTT applies. Companies with substantial tax holidays (Section 80-IAC, SEZ 10AA, etc.) may face Pillar 2 top-up."),
        ("When is first Pillar 2 return due in India?",
         "15 months from end of FY. So FY 2025-26 Pillar 2 returns due approximately June 2027 (first year of full compliance). First-year transition provisions may provide short extensions. In-scope companies should start Pillar 2 base computation NOW to ensure data readiness."),
        ("Does BQP handle BEPS Pillar 2 compliance for in-scope groups?",
         "Yes - Pillar 2 scope confirmation, GloBE base computation, jurisdiction-wise ETR analysis, QDMTT provisioning, Form 3CEAE / 3CEAF / 3CEAG preparation, Pillar 2 software implementation support, co-ordination with group tax function + Big-4 global Pillar 2 advisors. Scope-based engagement for Indian ultimate parents + Indian subsidiaries of in-scope MNC groups. WhatsApp +91 78018 87130."),
    ],
    related_pairs=[
        ("transfer-pricing-india-foreign-mnc.html", "Guide", "TP for Foreign MNC"),
        ("pillar-2-global-minimum-tax-india-startups-2026.html", "Guide", "Pillar 2 Introduction"),
    ],
    cta_h="BEPS Pillar 2 compliance for FY 2025-26 is now operational.",
    cta_b="QDMTT + IIR + UTPR + GIR + Form 3CEAE/3CEAF/3CEAG. BQP: scope confirmation + GloBE computation + filing. Co-ordinated with group Pillar 2 advisor.",
    keywords="BEPS Pillar 2 India 2026, GloBE India implementation, QDMTT India, GIR filing India, 15% global minimum tax India",
    desc="BEPS Pillar 2 (Global Minimum Tax 15%) India implementation October 2026 status: QDMTT + IIR + UTPR operational for FY 2025-26, GIR filing framework, Form 3CEAE/3CEAF/3CEAG. In-scope MNC groups (EUR 750M revenue) compliance workflow. Working CA guide by Durgesh Chavda.",
))

# 7. India-UK CETA
write_page("india-uk-ceta-implementation-operational-2026", quick_news_page(
    slug="india-uk-ceta-implementation-operational-2026",
    title="India-UK CETA Implementation 2026 | Preferential Tariff Operational - BQP",
    hero_em="95%+ trade lines now at preferential rates.",
    lead="India-UK Comprehensive Economic and Trade Agreement (CETA) was concluded in 2024-2025 and became operational in 2026. Preferential tariffs on 95%+ of trade lines; rules of origin framework; services + investment chapters. Significant impact on India-UK trade and investment flows. Here's what's actually live and what Indian + UK companies should do now.",
    kicker="/ India-UK Trade &middot; Updated 2026-10-22",
    section_pairs=[
        ("/ What's operational now", "The core gains.",
         "<ul>"
         "<li><strong>Goods tariffs</strong>: preferential rates on 95%+ of tariff lines. Specific sectoral gains:</li>"
         "<li>&nbsp;&nbsp;&mdash; India exports: textiles, leather, gems + jewellery, pharma, auto components, agri (basmati rice, specific spices).</li>"
         "<li>&nbsp;&nbsp;&mdash; UK exports: scotch whisky (tariff phase-down from 150% to ~75% over 10 years), premium automobiles, machinery, specific food + beverage.</li>"
         "<li><strong>Services</strong>: specific sector-wise commitments on movement of professionals (Mode 4), financial services, legal services (limited), telecom.</li>"
         "<li><strong>Investment</strong>: bilateral investment protections framework; sector-specific commitments.</li>"
         "<li><strong>Rules of Origin (ROO)</strong>: Certificate of Origin required at import to claim CETA preferential rate; product-specific rules (regional value content + tariff shift).</li>"
         "<li><strong>Dispute resolution</strong>: specific mechanism for ISDS limited; state-to-state dispute settlement.</li>"
         "</ul>"),
        ("/ For Indian exporters to UK", "What to update.",
         "<ul>"
         "<li>Review tariff schedule for specific HSN - preferential rate vs MFN rate.</li>"
         "<li>Obtain Certificate of Origin from DGFT-designated agency.</li>"
         "<li>Confirm ROO satisfaction: regional value content / tariff shift / wholly obtained criteria.</li>"
         "<li>Pricing re-strategy: preferential rate may give price advantage over non-CETA competitors.</li>"
         "<li>Supply chain restructuring: ensure Indian value-add qualifies under ROO.</li>"
         "<li>Combined with India-UAE CEPA + Australia ECTA: Indian exporters now have strong FTA coverage.</li>"
         "</ul>"),
        ("/ For UK companies entering India", "The investment angle.",
         "<ul>"
         "<li>CETA investment chapter provides protection framework for UK investors in India.</li>"
         "<li>Sector-specific commitments on financial services, telecom, legal (limited scope), professional services.</li>"
         "<li>Services Mode 4: Indian professionals' easier access to UK; UK professionals' Indian access.</li>"
         "<li>Combined with India's 2024 Space FDI reform + Telecom FDI 100% automatic + sector liberalisations: UK companies have strong India market access.</li>"
         "<li>DTAA India-UK already in place for tax relief; CETA builds trade / investment layer.</li>"
         "</ul>"),
        ("/ Compliance actions", "What to do now.",
         "<ol>"
         "<li><strong>Indian exporters</strong>: register with DGFT; obtain Certificate of Origin via designated agency; confirm ROO; apply preferential rate at UK import.</li>"
         "<li><strong>UK importers</strong>: receive Certificate of Origin from Indian supplier; claim preferential rate at UK customs; HMRC compliance.</li>"
         "<li><strong>UK exporters</strong>: review Indian tariff schedule; obtain UK Certificate of Origin; apply preferential rate at Indian import.</li>"
         "<li><strong>Indian importers</strong>: receive UK Certificate of Origin; claim preferential rate at Indian customs via Bill of Entry CETA preferential tariff code; verify ROO satisfaction.</li>"
         "<li><strong>Services providers</strong>: review Mode 4 commitments for professional category; verify qualification recognition framework.</li>"
         "<li><strong>Investors</strong>: review CETA investment chapter protections before signing JV / M&amp;A documentation.</li>"
         "</ol>"
         "<p><em>Last updated: 2026-10-22.</em></p>"),
    ],
    faq_pairs=[
        ("Is India-UK CETA fully operational in 2026?",
         "Preferential tariff framework became operational in 2026 for 95%+ of trade lines. Full phase-in continues over 5-10 years for specific tariff reductions (e.g., scotch whisky phase-down from 150% to ~75% over 10 years). Services + investment chapters also operational with sector-specific commitments."),
        ("How do I claim CETA preferential rate at import?",
         "Obtain Certificate of Origin from exporting country's designated authority (DGFT-designated agency in India; UK Chamber of Commerce / designated body in UK). Submit with import documentation; declare preferential tariff code on Bill of Entry (India) / Customs declaration (UK). Verify Rules of Origin (ROO) satisfaction - product-specific rules apply (regional value content, tariff shift, or wholly obtained)."),
        ("What's the biggest sectoral winner from India-UK CETA?",
         "On India export side: textiles + leather + gems/jewellery + pharma + auto components + agri. On UK export side: scotch whisky (phased reduction from 150% tariff), premium automobiles, machinery, specific F&B. Services Mode 4 helps Indian IT / professional services access to UK + UK professional services access to India."),
        ("Does CETA affect India-UK DTAA?",
         "No - DTAA (Double Taxation Avoidance Agreement) and CETA (Comprehensive Economic and Trade Agreement) are separate instruments. DTAA covers direct tax treaty relief (dividend, royalty, FTS, capital gain). CETA covers trade (tariffs) + services + investment protection. Both continue to apply."),
        ("Does BQP help with India-UK CETA compliance?",
         "Yes - Certificate of Origin coordination (via DGFT designated agency), Rules of Origin verification (regional value content + tariff shift), customs classification + preferential tariff claim at Bill of Entry stage, services Mode 4 compliance for professional movement, investment structuring using CETA protections. Co-ordinated with Indian customs house agent + UK counterparty. WhatsApp +91 78018 87130."),
    ],
    related_pairs=[
        ("india-uk-fta-tax-implications-startups.html", "Guide", "India-UK FTA (earlier)"),
        ("india-uk-tax-treaty-dtaa.html", "Guide", "India-UK DTAA"),
    ],
    cta_h="Trading between India and UK? CETA preferential rate is live.",
    cta_b="Certificate of Origin + Rules of Origin + preferential tariff claim + services Mode 4 compliance. BQP end-to-end for Indian exporters + UK investors.",
    keywords="India UK CETA implementation 2026, India UK trade agreement live, India UK preferential tariff, Rules of Origin India UK CETA, India UK investment agreement",
    desc="India-UK CETA (Comprehensive Economic and Trade Agreement) implementation October 2026: operational preferential tariffs on 95%+ trade lines, Rules of Origin framework, services Mode 4 commitments, investment chapter, specific sectoral gains (scotch whisky, textiles, pharma). Working CA guide by Durgesh Chavda.",
))

# 8. DPDP Rules status
write_page("dpdp-rules-january-2025-operational-status-october-2026", quick_news_page(
    slug="dpdp-rules-january-2025-operational-status-october-2026",
    title="DPDP Rules Operational Status October 2026 | Final Notification Watch - BQP",
    hero_em="draft Rules circulated Jan 2025, operational notification imminent.",
    lead="DPDP Act 2023 was enacted August 2023. Draft Rules for operationalisation were circulated by MeitY in January 2025. As of October 2026, final Rules notification is anticipated (expected around Budget 2026 timeframe). Here's the operational status, draft Rules content, and what foreign + Indian companies should do now to be ready.",
    kicker="/ DPDP Operational Status &middot; Updated 2026-10-22",
    section_pairs=[
        ("/ Current operational status", "What's live, what's pending.",
         "<ul>"
         "<li><strong>DPDP Act 2023 (enacted)</strong>: statutory framework in place. Act defines Data Fiduciary / Data Processor / Data Principal roles, consent framework, data principal rights, Data Protection Board, penalty structure (up to INR 250 crore).</li>"
         "<li><strong>Draft Rules January 2025 (circulated)</strong>: operational mechanics - consent mechanisms, breach notification format, Significant Data Fiduciary notifications, cross-border transfer blocklist country notifications, Data Protection Board procedures, grievance redressal timelines.</li>"
         "<li><strong>Public consultation (Feb-May 2025)</strong>: stakeholder submissions received by MeitY.</li>"
         "<li><strong>Finalisation (Oct 2026 status)</strong>: Rules being finalised. Industry expects notification by end of CY 2026 or Budget 2026 (Feb 2027).</li>"
         "<li><strong>Enforcement effective date</strong>: typically 90-180 days from final notification. So earliest enforcement likely mid-2027.</li>"
         "</ul>"),
        ("/ Key draft Rules provisions (likely to be retained)", "What foreign companies should assume.",
         "<ul>"
         "<li><strong>Notice format</strong>: standardised notice template for data processing. English + 22 scheduled Indian languages option.</li>"
         "<li><strong>Consent mechanism</strong>: granular / specific / informed / unconditional / unambiguous consent. Easy withdrawal mechanism.</li>"
         "<li><strong>Consent Manager framework</strong>: licensed Consent Managers (analogous to Account Aggregators for financial data) will manage consent exchange.</li>"
         "<li><strong>Breach notification</strong>: within reasonable period (likely 24-72 hours); specific format to Data Protection Board + each affected data principal.</li>"
         "<li><strong>Significant Data Fiduciary (SDF) notifications</strong>: specific entity classes (likely large social media, fintech, health, e-commerce). Additional obligations: India-based Data Protection Officer, independent Data Auditor, periodic DPIA + audit.</li>"
         "<li><strong>Cross-border transfer</strong>: Section 16 blocklist approach - specific countries may be restricted. Initial list likely to be minimal or empty; dynamic.</li>"
         "<li><strong>Children's data</strong>: verifiable parental consent (under 18 default; may be lowered); no behavioural monitoring; no targeted advertising.</li>"
         "<li><strong>Data Protection Board procedures</strong>: inquiry + enforcement + appeal to TDSAT.</li>"
         "</ul>"),
        ("/ What foreign companies should do now", "The 90-day readiness plan.",
         "<ol>"
         "<li>DPDP applicability analysis under Section 3 (extraterritorial reach).</li>"
         "<li>Data inventory: what personal data of Indian residents is collected, where stored, how processed, with whom shared.</li>"
         "<li>Legal basis mapping: consent vs legitimate uses (Section 7).</li>"
         "<li>Notice + consent flow design (English + Indian language option).</li>"
         "<li>Consent Manager integration readiness (likely required post Rules).</li>"
         "<li>Data Processing Agreement (DPA) templates with Indian processors + sub-processors.</li>"
         "<li>Breach response plan: detection + 24-72 hour notification mechanism.</li>"
         "<li>Significant Data Fiduciary (SDF) risk assessment: if likely SDF, appoint India-based DPO.</li>"
         "<li>Cross-border transfer documentation: current flows + mitigation if Section 16 blocklist applies.</li>"
         "<li>DPIA (Data Protection Impact Assessment) for high-risk processing.</li>"
         "<li>Children's data compliance if applicable.</li>"
         "<li>Grievance Officer appointment + response SLA setup.</li>"
         "</ol>"
         "<p><em>Last updated: 2026-10-22.</em></p>"),
    ],
    faq_pairs=[
        ("Are DPDP Rules operational in October 2026?",
         "Not yet. Draft Rules were circulated January 2025; public consultation Feb-May 2025. Final Rules notification expected around end of CY 2026 or Budget 2026 timeframe (February 2027). Enforcement typically 90-180 days from final notification - so enforcement date likely mid-2027. But: DPDP Act itself is enacted; broad obligations already applicable."),
        ("What's the biggest risk if I'm not DPDP-ready?",
         "Penalty up to INR 250 crore (~USD 30M) for failure to take reasonable security safeguards to prevent personal data breach (Section 33 + Schedule). Separate penalties up to INR 200 crore for breach non-notification, children's data violations, SDF obligation failures. Data Protection Board enforcement. Appeal to TDSAT."),
        ("How do final DPDP Rules affect foreign companies?",
         "Extraterritorial reach (Section 3): any entity processing personal data of Indian residents in connection with offering goods/services is in scope - regardless of entity location. Foreign US SaaS, UK e-commerce, Singapore fintech all captured if they have Indian paying users. Compliance obligations: notice + consent + breach notification + data principal rights + DPDP-compliant DPA with Indian processors."),
        ("Is India's DPDP similar to GDPR?",
         "Similar concepts but with India-specific nuances. Both have extraterritorial reach, lawful basis requirements, data principal rights, breach notification. Differences: DPDP has blocklist approach to cross-border transfer (vs GDPR adequacy whitelist); DPDP consent is more central (narrower 'legitimate interests'); DPDP specifically governs children + persons with disabilities; DPDP has specific SDF tier. GDPR-compliant companies need India-specific adjustments but core governance framework translates."),
        ("Does BQP help with DPDP readiness?",
         "Yes - 90-day DPDP readiness programme. Applicability analysis + data inventory + notice/consent flow design + DPA templates + breach response plan + SDF assessment + cross-border transfer documentation + DPIA for high-risk processing + Children's data compliance + Grievance Officer appointment. Co-ordinated with foreign privacy counsel (GDPR / CCPA alignment). WhatsApp +91 78018 87130."),
    ],
    related_pairs=[
        ("dpdp-act-india-foreign-company-compliance-2026.html", "Guide", "DPDP Act Guide"),
        ("india-data-localisation-rbi-dpdp-foreign-saas.html", "Guide", "Data Localisation"),
    ],
    cta_h="DPDP Rules finalisation imminent. Readiness window is now.",
    cta_b="90-day readiness programme: applicability + inventory + consent + DPA + breach plan + SDF assessment + cross-border transfer. BQP end-to-end + co-ordinated with foreign privacy counsel.",
    keywords="DPDP Rules India status 2026, DPDP Rules January 2025 operational, DPDP Rules notification India, DPDP Act Rules foreign company status",
    desc="DPDP Rules January 2025 operational status October 2026: draft Rules under finalisation, expected notification by Budget 2026 / early 2027, 90-180 day enforcement window post notification. Readiness programme for foreign + Indian companies. Working CA guide by Durgesh Chavda.",
))

# 9. AY 2026-27 ITR
write_page("ay-2026-27-itr-forms-new-disclosures-india", quick_news_page(
    slug="ay-2026-27-itr-forms-new-disclosures-india",
    title="AY 2026-27 ITR Forms + New Disclosures India - BQP",
    hero_em="new Schedule VDA + Schedule 112A + updated TP + foreign asset disclosures.",
    lead="CBDT notified ITR forms for AY 2026-27 (FY 2025-26) with several new disclosure requirements reflecting Finance Act 2024 + Finance Act 2025 changes. Includes new Schedule VDA (virtual digital assets), updated Schedule 112A for LTCG 12.5% framework, enhanced foreign asset reporting (Schedule FA), new TP disclosure (Form 3CEAB). Here's what's new for AY 2026-27 ITR filing.",
    kicker="/ ITR AY 2026-27 Update &middot; Updated 2026-10-22",
    section_pairs=[
        ("/ Key form changes for AY 2026-27", "What's new.",
         "<ul>"
         "<li><strong>Schedule VDA (Virtual Digital Assets)</strong>: separate disclosure for crypto / NFT / specified digital assets. Section 115BBH 30% flat tax + Section 194S 1% TDS reconciliation. Transaction-level reporting for exchanges + wallets.</li>"
         "<li><strong>Schedule 112A updated</strong>: for LTCG 12.5% framework (post Finance Act 2024). Grandfathering of pre-23-July-2024 acquisitions choice between 12.5% without indexation vs 20% with indexation.</li>"
         "<li><strong>Schedule FA (Foreign Assets)</strong>: enhanced for CRS / FATCA integration. Specific line items for foreign bank accounts, foreign securities, foreign life insurance, foreign private trusts, foreign company shareholding above 10%.</li>"
         "<li><strong>Section 56(2)(viib) legacy</strong>: historical disclosure retained even though provision abolished for new transactions. Pre-abolition cases still require reporting.</li>"
         "<li><strong>Section 43B(h) MSE disclosure</strong>: specific line item for amounts disallowed and amounts paid in subsequent FY (reversal). Year 2 (FY 2025-26) first full-year reporting.</li>"
         "<li><strong>BEPS Pillar 2 disclosure</strong>: for in-scope groups (consolidated revenue EUR 750M+), new Pillar 2 disclosure lines reflecting QDMTT + Form 3CEAE / 3CEAF / 3CEAG integration.</li>"
         "<li><strong>Schedule Startup</strong>: enhanced DPIIT Startup India + Section 80-IAC claim disclosure.</li>"
         "</ul>"),
        ("/ Deadlines for AY 2026-27", "Key dates.",
         "<ul>"
         "<li><strong>31 July 2026</strong>: individuals / HUFs not subject to tax audit (standard due date).</li>"
         "<li><strong>31 October 2026</strong>: taxpayers subject to tax audit (Section 44AB) + specified assessees.</li>"
         "<li><strong>30 November 2026</strong>: taxpayers subject to transfer pricing audit (Form 3CEB applicable).</li>"
         "<li><strong>31 December 2026</strong>: belated return filing deadline (with Section 234F late fee); revised return.</li>"
         "<li><strong>31 March 2027</strong>: updated return under Section 139(8A) (up to 48 months from end of relevant AY after Finance Act 2025, with specific additional tax).</li>"
         "</ul>"),
        ("/ Common AY 2026-27 ITR mistakes to avoid", "Where filings go wrong.",
         "<ul>"
         "<li>VDA transactions not fully reconciled across multiple exchanges + wallets.</li>"
         "<li>LTCG 12.5% vs 20% indexation choice not optimised per property / per transaction (pre vs post 23 July 2024 acquisitions).</li>"
         "<li>Section 43B(h) MSE disallowance missed - should be in Clause 22 of Form 3CD + corresponding ITR disclosure.</li>"
         "<li>Foreign asset Schedule FA incomplete - CRS/FATCA data from foreign banks must be reconciled.</li>"
         "<li>Form 10F electronic filing (for DTAA treaty rate claim) not completed before ITR filing.</li>"
         "<li>Section 44AB tax audit threshold crossed but Form 3CB/CD not filed within deadline - ITR filing blocked.</li>"
         "<li>Form 3CEB TP audit threshold crossed but Form 3CEB not filed - November deadline.</li>"
         "<li>Section 115BBH VDA 30% rate applied to loss (no loss offset against VDA gain or vs other income). Common mistake.</li>"
         "<li>Section 194S VDA TDS not claimed as credit (if deducted on sale by exchange).</li>"
         "</ul>"),
        ("/ Specific attention items for 2026-27", "Finance Act integration.",
         "<ul>"
         "<li><strong>LTCG 12.5% framework</strong>: Finance Act 2024 changed LTCG regime. Properties/securities acquired before 23 July 2024: choice between 12.5% without indexation vs 20% with indexation (whichever lower). Post 23 July 2024: 12.5% without indexation.</li>"
         "<li><strong>STT securities Section 112A</strong>: 12.5% post Finance Act 2024.</li>"
         "<li><strong>Non-STT securities / unlisted / property Section 112</strong>: 12.5% with indexation choice as above.</li>"
         "<li><strong>Debt mutual fund</strong>: post April 2023 regime - no indexation; STCG at slab rate regardless of holding period.</li>"
         "<li><strong>Section 194R business perquisite TDS</strong>: 10% TDS on business perquisites + related gift value disclosure.</li>"
         "<li><strong>Section 194T partnership firm TDS</strong>: 10% TDS on partner's share of profit above INR 20,000.</li>"
         "<li><strong>UAE Corporate Tax integration</strong>: UAE operations post 2024 CT may require specific disclosure.</li>"
         "<li><em>Last updated: 2026-10-22.</em></p>"),
    ],
    faq_pairs=[
        ("What's new in AY 2026-27 ITR forms?",
         "Separate Schedule VDA (crypto / NFT with Section 115BBH 30% + Section 194S TDS reconciliation), updated Schedule 112A for LTCG 12.5% framework (Finance Act 2024), enhanced Schedule FA foreign assets with CRS / FATCA integration, Section 43B(h) MSE disclosure, BEPS Pillar 2 disclosure for in-scope groups, enhanced Startup India + 80-IAC claim disclosure."),
        ("When is AY 2026-27 ITR due?",
         "31 July 2026 for individuals/HUFs without tax audit. 31 October 2026 for tax audit cases (Section 44AB). 30 November 2026 for TP audit cases (Form 3CEB). 31 December 2026 belated. 31 March 2027 updated return (Section 139(8A) with 24-month window + additional tax)."),
        ("How do I claim LTCG indexation under Finance Act 2024?",
         "For long-term capital assets acquired BEFORE 23 July 2024: choice between (a) 12.5% without indexation, or (b) 20% with indexation (whichever lower per asset). Compute both; pick lower. For assets acquired on or AFTER 23 July 2024: only 12.5% without indexation (no indexation choice). Report in Schedule 112A as applicable."),
        ("How do I report crypto transactions in AY 2026-27 ITR?",
         "Schedule VDA - new dedicated schedule. Report: aggregate gain under Section 115BBH 30% flat tax. No loss offset allowed. Only deduction: cost of acquisition. Section 194S 1% TDS on sale by exchange - claim as TDS credit. Transaction-level reconciliation across multiple exchanges / wallets. Foreign exchange holdings also reportable in Schedule FA."),
        ("Does Section 43B(h) MSE disallowance need to be in ITR?",
         "Yes - Form 3CD Clause 22 (tax audit) requires specific disclosure. Corresponding ITR line item reflects: (a) MSE amounts disallowed in current FY under 43B(h), (b) MSE amounts paid in current FY where disallowance was reversed from prior year. For AY 2026-27, this is year 2 of 43B(h) impact."),
        ("Does BQP handle AY 2026-27 ITR filing?",
         "Yes - standard annual tax engagement. Residence status determination + ITR-1/2/3/5/6/7 as applicable + all new schedules (VDA, 112A, FA, 43B(h), Pillar 2) + Form 10F electronic filing + Form 3CEB TP + Form 3CD tax audit + Section 195 TDS refund claims + capital gain Section 54 reinvestment. Fast turnaround through July-November 2026 ITR window. WhatsApp +91 78018 87130."),
    ],
    related_pairs=[
        ("itr-filing-ay-2026-27-deadlines-changes-india.html", "Guide", "ITR AY 2026-27 Full Guide"),
        ("ltcg-12-5-percent-new-capital-gains-india-2026.html", "Guide", "LTCG 12.5% Rules"),
    ],
    cta_h="AY 2026-27 ITR filing window: July-November 2026.",
    cta_b="Schedule VDA + 112A + FA + 43B(h) + Pillar 2 + Form 10F + Form 3CEB + Form 3CD. BQP standard annual engagement + fast turnaround. Scope-based.",
    keywords="AY 2026-27 ITR forms India, Schedule VDA ITR 2026, LTCG 12.5 Schedule 112A, foreign asset Schedule FA 2026, Section 43B(h) ITR disclosure",
    desc="AY 2026-27 ITR forms India new disclosures: Schedule VDA (crypto Section 115BBH), updated Schedule 112A (LTCG 12.5%), enhanced Schedule FA (foreign assets CRS/FATCA), Section 43B(h) MSE, BEPS Pillar 2. Deadlines July-November 2026. CA Durgesh Chavda complete guide.",
))

# 10. Year-end LRS
write_page("year-end-lrs-tcs-20-planning-october-march-2026-27", quick_news_page(
    slug="year-end-lrs-tcs-20-planning-october-march-2026-27",
    title="Year-End LRS + TCS 20% Planning October-March 2026-27 - BQP",
    hero_em="plan now, remit smart.",
    lead="Section 206C(1G) TCS at 20% on LRS (Liberalised Remittance Scheme) remittances above INR 7 lakh per Indian resident per FY became operational post Finance Act 2024. FY 2026-27 is in its second year of 20% TCS regime. October-March is the critical year-end LRS window: for Indian residents remitting abroad for travel, education, overseas investment, gift, maintenance of relatives abroad. Here's the complete planning framework for the FY 2026-27 year-end window.",
    kicker="/ LRS Year-End Planning &middot; Updated 2026-10-22",
    section_pairs=[
        ("/ The current TCS framework", "Rates + thresholds.",
         "<ul>"
         "<li><strong>Standard rate (post Finance Act 2024)</strong>: 20% TCS on LRS remittances above INR 7 lakh aggregate per Indian resident per FY. Collected by the Indian AD-I bank at the time of remittance.</li>"
         "<li><strong>Exemptions</strong>:</li>"
         "<li>&nbsp;&nbsp;&mdash; <strong>Medical treatment</strong>: 5% TCS (above INR 7 lakh).</li>"
         "<li>&nbsp;&nbsp;&mdash; <strong>Education (self-funded)</strong>: 5% TCS (above INR 7 lakh); nil TCS below INR 7 lakh.</li>"
         "<li>&nbsp;&nbsp;&mdash; <strong>Education funded by loan from Indian financial institution</strong>: nil TCS (any amount).</li>"
         "<li>&nbsp;&nbsp;&mdash; <strong>Overseas tour package purchase from Indian travel operator</strong>: 20% TCS (any amount; no INR 7 lakh exemption).</li>"
         "<li><strong>Overall LRS limit</strong>: USD 250,000 per Indian resident per FY (combined all permitted current + capital account purposes).</li>"
         "<li><strong>Creditability</strong>: TCS collected is creditable against Indian donor/remitter's income tax (via Form 26AS); refundable if excess over actual tax liability.</li>"
         "</ul>"),
        ("/ Common year-end LRS use cases", "Who needs to plan.",
         "<ul>"
         "<li><strong>Overseas education remittances</strong>: college tuition for children abroad - September / October / January school terms.</li>"
         "<li><strong>Investment / securities purchase</strong>: Indian investors buying US / UK / Singapore stocks + ETFs via overseas brokerage - LRS route.</li>"
         "<li><strong>Gift to NRI relatives</strong>: parents gifting children abroad; aunts/uncles gifting nephews/nieces. See <a href='nri-gift-indian-relatives-section-56-fema-2026.html'>NRI gift guide</a>.</li>"
         "<li><strong>Property purchase abroad</strong>: Indian residents buying overseas property - LRS limit applies.</li>"
         "<li><strong>Overseas tour packages</strong>: Indian family planning summer / Christmas foreign holiday - 20% TCS from first rupee for tour package.</li>"
         "<li><strong>Medical treatment abroad</strong>: Indian resident / family member - 5% TCS rate.</li>"
         "<li><strong>Maintenance of close relatives abroad</strong>: parents sending money to children settled abroad.</li>"
         "<li><strong>Overseas premium insurance</strong>: Indian residents paying US / UK / Singapore insurance premiums.</li>"
         "</ul>"),
        ("/ Planning actions for Oct-March 2026-27", "Smart LRS use.",
         "<ol>"
         "<li><strong>Aggregate across family</strong>: LRS limit is per individual Indian resident. Family of 4 adults = USD 1M combined annual limit. Spread remittances across family members where appropriate.</li>"
         "<li><strong>Timing</strong>: large discretionary remittances benefit from being spread across FYs. Example: USD 500K property purchase - USD 250K in March 2027 FY + USD 250K in April 2027 FY avoids crossing USD 250K/person annual LRS limit.</li>"
         "<li><strong>Education loan route</strong>: if education abroad is the purpose, Indian education loan from Indian bank/NBFC provides nil TCS vs 5% self-funded. Material saving for large education remittances.</li>"
         "<li><strong>Package vs direct</strong>: 20% TCS on tour package purchased from Indian operator (any amount) vs 20% on direct remittance above INR 7 lakh. For sub-INR 7 lakh family holidays, direct booking (hotels / tickets separately via international cards or direct bank transfer under personal LRS) more tax-efficient.</li>"
         "<li><strong>Form A2 + purpose code</strong>: correctly declared purpose code can affect TCS rate. Medical treatment, education self-funded, education loan-funded, personal gift, maintenance of relative, investment, tour package all have distinct codes.</li>"
         "<li><strong>Documentation for exemptions</strong>: medical treatment hospital letter + estimate, education institution admission letter, loan sanction letter, gift deed - keep audit trail for AO query.</li>"
         "<li><strong>Form 15CA / 15CB for large remittances</strong>: standard Rule 37BB framework.</li>"
         "<li><strong>TCS credit claim</strong>: via Form 26AS; refund via Indian ITR filing.</li>"
         "</ol>"
         "<p><em>Last updated: 2026-10-22.</em></p>"),
    ],
    faq_pairs=[
        ("What's the TCS rate on LRS remittances in FY 2026-27?",
         "Standard: 20% TCS on LRS remittances above INR 7 lakh per Indian resident per FY (post Finance Act 2024, operational FY 2024-25 onwards). Exceptions: 5% for medical treatment above INR 7 lakh; 5% for education self-funded above INR 7 lakh (nil below); 0% for education loan-funded (any amount); 20% for tour package purchase from Indian operator (any amount, no exemption)."),
        ("What's the overall LRS limit per Indian resident?",
         "USD 250,000 per Indian resident per FY. Covers all permitted current + capital account purposes combined: travel, education, medical, gift, maintenance of relatives, overseas investment, property purchase, premium insurance etc. Family of 4 adults = USD 1M combined annual LRS. Minor's remittance counts against parent's LRS."),
        ("How can I avoid high TCS on overseas education remittance?",
         "Education loan route - loan from Indian bank/NBFC + remittance through bank/NBFC: 0% TCS. Self-funded education remittance: 5% TCS above INR 7 lakh (vs 20% standard). Timing - split large education payments across FYs where feasible. Document admission letter + fee invoice for exemption claim."),
        ("Does TCS 20% also apply to gift to NRI relative?",
         "Yes - 20% TCS on LRS remittance above INR 7 lakh (any purpose except specified exemptions). Gift to NRI relative is permitted LRS purpose (Section 56 relative exemption on recipient side). TCS collected creditable against donor's Indian income tax. Can spread gifts across FYs or across donors to manage TCS impact. See our <a href='nri-gift-indian-relatives-section-56-fema-2026.html'>NRI gift guide</a>."),
        ("Can I claim TCS back if my tax liability is lower?",
         "Yes - TCS is advance tax collected on your behalf; credited to your PAN; appears in Form 26AS. Claim credit against your Indian income tax in annual ITR. If your actual tax liability is lower than TCS collected, excess refunded via ITR. Refund timeline: 1-6 months after ITR processing."),
        ("Does BQP handle LRS planning + Form 15CA/CB?",
         "Yes - LRS planning advisory: TCS rate optimisation per purpose code, timing of remittances, family aggregation strategy, education loan vs self-funded analysis, tour package vs direct booking decision. Form 15CA + 15CB execution. TCS credit claim in Indian ITR. Standard engagement during October-March year-end LRS window. WhatsApp +91 78018 87130."),
    ],
    related_pairs=[
        ("tcs-20-foreign-remittance-lrs-india-2026.html", "Guide", "TCS 20% LRS Full Guide"),
        ("lrs-tcs-calculator.html", "Tool", "LRS TCS Calculator"),
    ],
    cta_h="October-March LRS window is now. Smart timing saves materially.",
    cta_b="Family aggregation + timing + education loan route + purpose code + Form 15CA/CB. BQP LRS planning engagement for high-value remittance season.",
    keywords="LRS TCS 20 year end 2026, LRS planning October March, education remittance TCS 2026, overseas investment LRS TCS 2026",
    desc="Year-end LRS (Liberalised Remittance Scheme) + TCS 20% planning October-March 2026-27: USD 250,000 per Indian resident annual limit, TCS rates by purpose, education loan vs self-funded, family aggregation, timing optimisation, Form 15CA/CB. Working CA guide by Durgesh Chavda.",
))

print("Batch Q part 1 complete: 10 current-news pages written (6-10)")
print("Continue with part 2 for remaining 5 news pages + 7 city pages + news hub")
