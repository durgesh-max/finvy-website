# -*- coding: utf-8 -*-
"""Batch I: 4 current-regulatory blog posts (October 2026)."""
from build_lib import page, write_page

# 1. LTCG 12.5% new capital gains rule 2026
write_page("ltcg-12-5-percent-new-capital-gains-india-2026", page(
    slug="ltcg-12-5-percent-new-capital-gains-india-2026",
    title="LTCG 12.5% New Capital Gains Rule 2026 | Impact on Founders - BQP",
    description="The post-July-2024 LTCG 12.5% capital gains rule affects every Indian founder, NRI, and investor. Listed equity, unlisted equity, property, mutual funds, bonds - full impact map. Indexation grandfathering, STCG 20%, buyback tax. Working CA analysis.",
    keywords="LTCG 12.5% new rule, LTCG without indexation 2026, Finance Act 2024 capital gains, STCG 20% listed equity, LTCG property India 2026, buyback tax October 2024, LTCG unlisted equity 12.5",
    hero_kicker="/ Blog &middot; Capital Gains &middot; Updated October 2026",
    hero_title_html="LTCG 12.5%, <em>the capital-gains regime that rewrote everything.</em>",
    hero_lead="The Finance Act 2024 flipped India's capital-gains framework in July 2024. By October 2026, every Indian founder, NRI and investor is operating under the new regime: 12.5% LTCG without indexation, 20% STCG on listed equity, buyback tax at the shareholder level, debt MF slab-rate taxation. This is the full impact map with the specific numbers.",
    sections=[
        ("/ The headline changes", "What Finance Act 2024 did.",
         "<p>Three structural changes to India's capital-gains framework, effective <strong>23 July 2024</strong> for transfers on or after that date:</p>"
         "<ol>"
         "<li><strong>LTCG rate unified at 12.5%</strong> across asset classes (listed equity previously 10%; unlisted and property previously 20% with indexation). All assets now at 12.5% without indexation.</li>"
         "<li><strong>Indexation benefit removed</strong> for new transfers. Pre-23-July-2024 transfers retain the 20%-with-indexation option as grandfathering.</li>"
         "<li><strong>STCG on listed equity raised</strong> from 15% to 20%.</li>"
         "</ol>"
         "<p>Separately, the buyback tax regime was reinstated at the shareholder level effective <strong>1 October 2024</strong> &mdash; buyback distributions are now taxed as dividend income in the shareholder's hands at slab rates (previously the company paid buyback-distribution tax).</p>"),
        ("/ Impact on listed equity holders", "The 10% to 12.5% move.",
         "<p>For retail and HNI investors in listed Indian equity (NSE / BSE direct or via equity mutual funds):</p>"
         "<ul>"
         "<li><strong>LTCG rate:</strong> 10% &rarr; 12.5% on gains above INR 1.25 lakh per year (up from INR 1 lakh exemption).</li>"
         "<li><strong>STCG rate:</strong> 15% &rarr; 20%.</li>"
         "<li><strong>STT must still be paid</strong> at redemption to qualify for the preferential rate.</li>"
         "</ul>"
         "<p>Worked example &mdash; LTCG on listed equity sale of INR 50 lakh gain in FY 2025-26:</p>"
         "<ul>"
         "<li>Taxable gain: INR 50,00,000 - INR 1,25,000 exemption = INR 48,75,000</li>"
         "<li>LTCG tax at 12.5%: INR 6,09,375</li>"
         "<li>Plus surcharge + 4% cess based on total income</li>"
         "</ul>"
         "<p>For a high-net-worth seller the 2.5-percentage-point increase on a INR 1 crore gain is INR 2.5 lakh more tax than pre-July-2024.</p>"),
        ("/ Impact on unlisted equity + property", "The 20%-with-indexation vs 12.5%-without choice.",
         "<p>For unlisted equity, immovable property, debentures, bonds and similar long-held assets, Finance Act 2024 removed indexation. The transition rules:</p>"
         "<ul>"
         "<li><strong>Transfers on or after 23 July 2024:</strong> LTCG at 12.5% without indexation. No choice.</li>"
         "<li><strong>Assets acquired before 23 July 2024 and sold after:</strong> taxpayer can choose between (a) 12.5% without indexation or (b) 20% with indexation &mdash; whichever is lower. Choice is on a per-transaction basis.</li>"
         "</ul>"
         "<p>Worked example &mdash; sale of ancestral property acquired 2015 for INR 50 lakh, sold October 2026 for INR 1.8 crore (COA indexed cost INR 70 lakh using CII):</p>"
         "<ul>"
         "<li><strong>Option A (20% with indexation):</strong> Indexed cost INR 70 lakh. Gain INR 1.8cr - INR 70 lakh = INR 1.10 crore. Tax at 20% = INR 22 lakh.</li>"
         "<li><strong>Option B (12.5% without indexation):</strong> Nominal cost INR 50 lakh. Gain INR 1.8cr - INR 50 lakh = INR 1.30 crore. Tax at 12.5% = INR 16.25 lakh.</li>"
         "<li><strong>Lower tax: Option B.</strong></li>"
         "</ul>"
         "<p>For post-23-July-2024 asset acquisitions, only Option B applies &mdash; no choice.</p>"
         "<p>Rule of thumb: for very old assets (10+ years, high indexation), 20% with indexation sometimes wins. For medium-held assets (3-10 years), 12.5% without indexation almost always wins. Model each transaction.</p>"),
        ("/ Impact on debt mutual funds", "The grandfathering that stayed.",
         "<p>Debt mutual funds purchased on or after <strong>1 April 2023</strong> lost the LTCG preferential rate entirely. All gains, regardless of holding period, are taxed at the investor's slab rate.</p>"
         "<p>Debt MF units acquired before 1 April 2023 remain under the earlier regime (20% with indexation after 3-year holding) until sold. This grandfathering survives Finance Act 2024.</p>"
         "<p>Practical effect: investors with pre-April-2023 debt MF holdings have a one-time planning window. If you expect to hold the units long term and have significant indexation benefit, holding to the current regime is often better than switching strategies.</p>"),
        ("/ Impact on founders at exit", "Flip, reverse flip, acquisition.",
         "<ul>"
         "<li><strong>Flipping Indian startup to Delaware C-Corp:</strong> share-swap triggers Indian capital gains for each shareholder. Post-July-2024, LTCG at 12.5% without indexation on the FMV uplift. For Indian cost-of-acquisition founders, the delta from 20%-with-indexation to 12.5%-without is small on short holding; larger on long holding.</li>"
         "<li><strong>Reverse flip (Delaware parent to Indian parent):</strong> same taxable event per shareholder. Shareholders exchanging Delaware stock for Indian stock trigger capital gains on the FMV uplift from their Delaware cost basis. For founders with low original Delaware cost, almost all of the current FMV is gain &mdash; 12.5% rate helps vs the earlier 20%.</li>"
         "<li><strong>Acquisition exit on Indian shares:</strong> founders selling in M&amp;A pay LTCG at 12.5% on gain over cost basis. For a founder exiting at INR 100 crore with INR 1 lakh founder cost basis, tax at 12.5% is INR 12.5 crore (vs INR 20 crore under pre-July-2024 20%-with-indexation if indexation was minimal). Material savings.</li>"
         "<li><strong>Buyback by Indian company:</strong> post-October-2024, buyback distribution is taxed at the shareholder level as dividend income at slab rate. For high-income shareholders (slab rate ~43% including surcharge), buyback is now punitive compared to pre-October-2024 regime (where company paid 23.3% buyback tax and shareholder received post-tax). Think twice before using buyback as exit mechanism; direct secondary sale often better.</li>"
         "</ul>"),
        ("/ What to do", "The planning checklist.",
         "<p><strong>If you are a listed-equity investor:</strong> no action required; higher rates are the new normal. Rebalance timing of realisations where possible to use the INR 1.25 lakh annual LTCG exemption.</p>"
         "<p><strong>If you own ancestral or long-held property:</strong> model both 20%-with-indexation and 12.5%-without-indexation before selling. Pre-July-2024 acquisitions still have the choice. Section 54 / 54F / 54EC reinvestment options are unchanged and can further reduce tax.</p>"
         "<p><strong>If you are an Indian startup founder planning a flip:</strong> flip early, at low FMV. The 12.5% rate is already low; low FMV x 12.5% x founder cap table is nearly trivial. Delaying costs geometrically more.</p>"
         "<p><strong>If you are a US-returning NRI with foreign assets:</strong> the Indian 12.5% regime is favourable for post-RNOR capital gains on foreign asset sales. Combined with FTC under India-US DTAA Article 25, net Indian tax after US tax is often zero.</p>"
         "<p><strong>If you are planning to exit via buyback:</strong> re-model vs secondary sale. Buyback is now shareholder-taxable at slab rate; secondary sale is LTCG at 12.5%. For high-income shareholders, secondary sale wins by 25+ percentage points.</p>"
         "<p><em>Last updated: 2026-10-07.</em></p>"),
    ],
    faqs=[
        ("What is the new LTCG rate in India from October 2026?",
         "12.5% without indexation across most asset classes (listed equity, unlisted equity, property, bonds, debentures) for transfers on or after 23 July 2024. Pre-July-2024 acquisitions retain the choice of 20% with indexation for grandfathered holdings. STCG on listed equity is 20% (up from 15%)."),
        ("Did Finance Act 2024 remove indexation entirely?",
         "For new acquisitions (on or after 23 July 2024), yes - no indexation available. For pre-July-2024 acquisitions sold after that date, the taxpayer can choose between 20% with indexation and 12.5% without indexation on a per-transaction basis. The lower option wins."),
        ("Is the LTCG exemption on listed equity still INR 1 lakh?",
         "No - raised to INR 1.25 lakh per year per taxpayer effective 23 July 2024. Gains up to INR 1.25 lakh on listed equity (NSE/BSE direct or via equity mutual funds) are exempt."),
        ("What is the buyback tax change effective October 2024?",
         "Pre-October-2024: Indian company paid buyback-distribution tax at 23.3% at the company level; shareholder received post-tax amount tax-free. Post-October-2024: buyback distribution is taxed at the shareholder level as dividend income at the shareholder's slab rate. For high-income shareholders this is often punitive compared to secondary sale (which is LTCG at 12.5%). Model both before using buyback as exit."),
        ("Are debt mutual funds still LTCG-eligible?",
         "Only for units purchased before 1 April 2023 (grandfathered under the earlier 20%-with-indexation regime). Debt MF units purchased on or after 1 April 2023 are taxed at the investor's slab rate regardless of holding period - no LTCG preferential rate."),
        ("Does BQP help with capital gains planning under the new regime?",
         "Yes - transaction-by-transaction modelling (20% with indexation vs 12.5% without), Section 54/54F/54EC reinvestment structuring, flip/reverse-flip tax impact, buyback vs secondary sale decision, and ongoing capital-gains ITR filing. WhatsApp +91 78018 87130 or email durgesh@bharatquantumprospera.com."),
    ],
    related=[
        ("nri-selling-indian-property-capital-gains.html", "Guide", "NRI Property Sale"),
        ("india-to-delaware-flip-structure.html", "Guide", "Flip Structure"),
        ("us-india-reverse-flip-structure.html", "Guide", "Reverse Flip"),
    ],
    cta_headline="LTCG 12.5% changes real transactions.",
    cta_body="Scoping call covers your specific capital-gains event under the new regime: property sale, flip, reverse flip, buyback, acquisition exit. We model all options (20%+indexation vs 12.5%, buyback vs secondary) and recommend the lower-tax path.",
))

# 2. TCS 20% on LRS
write_page("tcs-20-foreign-remittance-lrs-india-2026", page(
    slug="tcs-20-foreign-remittance-lrs-india-2026",
    title="TCS 20% on Foreign Remittance LRS 2026 | Full Guide + Avoidance - BQP",
    description="TCS 20% on foreign remittance under LRS above INR 10 lakh per year. Section 206C(1G) full impact: how it works, when it applies, who's exempt, how founders avoid or recover it, education/medical carve-outs. Working CA guide.",
    keywords="TCS 20% foreign remittance 2026, LRS TCS calculator, Section 206C(1G), TCS on foreign remittance India, TCS LRS exemption, TCS refund LRS, 20% TCS on dollar remittance",
    hero_kicker="/ Blog &middot; TCS on LRS &middot; Updated October 2026",
    hero_title_html="TCS 20% on foreign remittance, <em>what every Indian founder needs to know.</em>",
    hero_lead="Since 1 October 2023, Indian residents remitting money abroad under the Liberalised Remittance Scheme (LRS) face 20% Tax Collected at Source (TCS) on remittances above INR 10 lakh per financial year (per source category). Section 206C(1G). It is NOT a tax; it is advance-tax collection &mdash; but it drains working capital for 12-18 months. Here's the full map, with the carve-outs, exemptions and recovery process.",
    sections=[
        ("/ How TCS on LRS works", "The mechanics.",
         "<p><strong>Section 206C(1G)</strong> of the Income Tax Act requires Authorised Dealer (AD) banks to collect TCS on outward remittances under LRS. Current rates (effective 1 October 2023):</p>"
         "<ul>"
         "<li><strong>Overseas education financed by education loan:</strong> 0.5% above INR 7 lakh/year</li>"
         "<li><strong>Overseas education from own funds:</strong> 5% above INR 7 lakh/year</li>"
         "<li><strong>Medical treatment abroad:</strong> 5% above INR 7 lakh/year</li>"
         "<li><strong>Overseas tour package:</strong> 5% up to INR 7 lakh/year, 20% above</li>"
         "<li><strong>All other LRS remittances (investment, maintenance, gift, inheritance):</strong> 20% above INR 10 lakh/year</li>"
         "</ul>"
         "<p>The TCS is collected by the AD bank at the time of remittance and deposited with the government. The remitter receives a TCS certificate (Form 27D). TCS is credited against the remitter's final income tax liability for the year.</p>"
         "<p>Who it affects for Indian founders:</p>"
         "<ul>"
         "<li>Investing in a Delaware C-Corp (FEMA ODI route) &mdash; any outbound equity investment above INR 10 lakh in a year triggers 20% TCS.</li>"
         "<li>Funding a Dubai Free Zone LLC setup from India &mdash; same.</li>"
         "<li>Paying overseas tuition fees above INR 7 lakh &mdash; 0.5% (loan-funded) or 5% (own-funded).</li>"
         "<li>Buying US stocks via Indian broker platforms using LRS &mdash; 20% above INR 10 lakh/year.</li>"
         "<li>Gift to overseas relative &mdash; 20% above INR 10 lakh.</li>"
         "</ul>"),
        ("/ Worked example", "Setting up a Delaware C-Corp.",
         "<p>Scenario: Indian founder remits USD 20,000 (~INR 16.6 lakh at INR 83/USD) to fund a new Delaware C-Corp as equity contribution.</p>"
         "<ul>"
         "<li>LRS category: Investment (equity in overseas entity) &mdash; falls under 'all other' at 20%.</li>"
         "<li>Threshold: TCS applies on amount above INR 10 lakh. Taxable amount = INR 16.6 lakh - INR 10 lakh = INR 6.6 lakh.</li>"
         "<li>TCS at 20%: INR 1,32,000 collected by the AD bank.</li>"
         "<li>Founder actually remits INR 16.6 lakh to Delaware + INR 1,32,000 to the government via TCS = INR 17.92 lakh cash outflow.</li>"
         "</ul>"
         "<p>The INR 1.32 lakh TCS is NOT a tax; it is advance tax credit against the founder's final income tax for the year. Claimed on ITR as TCS credit (Section 206C(4)). If the founder's final tax liability is lower than the TCS collected, excess is refunded (12-18 months typical).</p>"),
        ("/ Who is exempt", "The carve-outs.",
         "<p>TCS on LRS does NOT apply where:</p>"
         "<ul>"
         "<li><strong>Remitter is below the threshold</strong> &mdash; aggregate LRS remittances in the financial year are below INR 10 lakh (or INR 7 lakh for education/medical).</li>"
         "<li><strong>Remitter is a non-resident</strong> &mdash; NRIs transferring their own foreign-currency balances abroad are not under LRS (LRS applies only to Resident Indians).</li>"
         "<li><strong>Payment via credit card for overseas transactions</strong> is EXCLUDED from LRS under current CBDT clarification (though this has been contested; check current status). Credit-card spend abroad is not currently subject to the 20% TCS on LRS.</li>"
         "<li><strong>Business remittances under FEMA automatic/approval route (not LRS)</strong> &mdash; Indian company remitting to foreign vendor for business services does not use LRS; different reporting framework; no TCS under 206C(1G).</li>"
         "<li><strong>Repayment of foreign loans</strong> and specific business-purpose remittances have their own frameworks.</li>"
         "</ul>"),
        ("/ How to recover TCS", "The ITR claim process.",
         "<ol>"
         "<li><strong>TCS certificate (Form 27D)</strong> &mdash; retrieve from the AD bank after remittance. Shows TCS amount deducted.</li>"
         "<li><strong>Form 26AS / AIS verification</strong> &mdash; TCS will reflect in your Annual Information Statement within 1-2 months of deposit.</li>"
         "<li><strong>Claim as advance tax credit on ITR</strong> &mdash; file ITR by 31 July (or 31 October for audit cases); TCS credit automatically applied to final tax liability.</li>"
         "<li><strong>Excess refund</strong> &mdash; if TCS collected exceeds final tax, refund processed by Income Tax Department. 12-18 months typical from ITR filing to refund receipt (sometimes faster).</li>"
         "<li><strong>Section 206CC higher rate</strong> &mdash; applies if remitter is a 'specified person' who has not filed ITR for prior years. Rate becomes 10% or 20% depending on circumstances. Keep ITR filings current to avoid.</li>"
         "</ol>"
         "<p>Working-capital impact: for a founder remitting USD 50K-100K to seed a Delaware structure, TCS is INR 7-15 lakh locked up for a year. Factor this into cash planning.</p>"),
        ("/ Planning strategies", "What founders actually do.",
         "<ul>"
         "<li><strong>Spread remittances across financial years</strong> if timing allows. Threshold is per financial year (April-March).</li>"
         "<li><strong>Use spouse's LRS limit</strong> for larger structures. Each Indian resident individual has a separate USD 250K LRS limit and separate INR 10 lakh TCS threshold.</li>"
         "<li><strong>Combine credit-card spend (not LRS)</strong> and LRS for mixed overseas obligations where feasible under current CBDT position.</li>"
         "<li><strong>File ITR promptly</strong> after TCS to accelerate refund processing.</li>"
         "<li><strong>Keep TCS certificates organised</strong> &mdash; one certificate per remittance. Store with ITR papers.</li>"
         "<li><strong>Factor TCS into FEMA ODI cash planning</strong> &mdash; if setting up a USD 50K Delaware structure needs INR 42 lakh at INR 83/USD, plan for ~INR 46 lakh total cash outflow including TCS.</li>"
         "</ul>"
         "<p><em>Use our TCS LRS Calculator: <a href=\"lrs-tcs-calculator.html\">lrs-tcs-calculator.html</a></em></p>"
         "<p><em>Last updated: 2026-10-07.</em></p>"),
    ],
    faqs=[
        ("What is TCS on LRS in India in 2026?",
         "Tax Collected at Source under Section 206C(1G). AD bank collects 20% on outward remittances above INR 10 lakh per financial year for investment, maintenance and most other LRS purposes. Education-loan-funded 0.5%, education-self-funded or medical 5% above INR 7 lakh. Overseas tour package: 5% up to INR 7 lakh, 20% above."),
        ("Is TCS on LRS a tax or a deposit?",
         "A deposit, not a tax. It is advance tax collection credited against the remitter's final income tax liability for the year. If TCS collected exceeds final tax, excess is refunded. The problem is the 12-18 month working-capital lock-up."),
        ("Does TCS on LRS apply to credit-card spend abroad?",
         "Under current CBDT clarification, credit-card spend abroad is excluded from LRS and therefore NOT subject to the 20% TCS. However, this has been contested in policy announcements. For large credit-card obligations, verify current CBDT position before relying on this exclusion."),
        ("How do I recover TCS collected on my LRS remittance?",
         "Claim it as advance tax credit when filing your annual Indian ITR. TCS reflects in your Form 26AS / AIS. If TCS collected exceeds final tax liability, excess is refunded by the Income Tax Department - typically 12-18 months after ITR filing."),
        ("Can an NRI avoid TCS by routing through family in India?",
         "NRIs don't come under LRS at all - LRS applies only to Resident Indians. However, NRI gifts or inheritance received by Resident Indian family members, if later remitted back abroad under LRS, would be subject to the standard 20% TCS. Direct routing through NRI's own foreign-currency account is cleaner."),
        ("Does BQP handle TCS planning and recovery?",
         "Yes - LRS cash-flow planning for FEMA ODI investments, TCS certificate collection, ITR filing with TCS credit, refund tracking. Scoping call for Indian founders planning overseas investments or NRI tax planning is free. WhatsApp +91 78018 87130."),
    ],
    related=[
        ("fema-odi-us-entity-indian-founder.html", "Guide", "FEMA ODI"),
        ("us-incorporation.html", "Hub", "US Incorporation"),
        ("lrs-tcs-calculator.html", "Tool", "LRS TCS Calculator"),
    ],
    cta_headline="Planning a USD 50K+ remittance abroad?",
    cta_body="Calculate TCS with our free tool, then WhatsApp Durgesh to plan the FEMA ODI + ITR recovery workflow. Setting up a Delaware entity, Dubai Free Zone, or Singapore structure &mdash; we handle the full cash + compliance stack.",
))

# 3. UAE Corporate Tax 2026 FTA Updates
write_page("uae-corporate-tax-2026-qfzp-fta-update", page(
    slug="uae-corporate-tax-2026-qfzp-fta-update",
    title="UAE Corporate Tax 2026 Update | QFZP + ESR + FTA Clarifications - BQP",
    description="UAE Corporate Tax 2026 practical update: FTA clarifications on Qualifying Free Zone Person (QFZP), Qualifying Income definition, ESR substance requirements, Transfer Pricing documentation, Pillar 2 interaction. Working CA analysis for Dubai holdcos.",
    keywords="UAE Corporate Tax 2026 update, QFZP 2026, Qualifying Free Zone Person UAE, FTA clarification UAE CT, UAE ESR 2026, UAE transfer pricing 2026, Pillar 2 UAE",
    hero_kicker="/ Blog &middot; UAE Corporate Tax &middot; October 2026",
    hero_title_html="UAE Corporate Tax, <em>what changed through late 2026.</em>",
    hero_lead="UAE Corporate Tax took effect 1 June 2023 at 9% above AED 375,000 profit, with a 0% route for Qualifying Free Zone Persons (QFZP) meeting substance and Qualifying Income tests. Through 2024-2026 the FTA (Federal Tax Authority) has issued multiple clarifications on QFZP mechanics, ESR documentation, Transfer Pricing requirements, and interaction with OECD Pillar 2. This is the current state for Indian-founder Dubai holdcos.",
    sections=[
        ("/ The core framework (unchanged since 2023)", "What UAE CT does.",
         "<p><strong>Federal Decree-Law 47 of 2022</strong>, effective 1 June 2023:</p>"
         "<ul>"
         "<li>Standard rate 9% on taxable income above AED 375,000 (~USD 102K / INR 85 lakh).</li>"
         "<li>0% rate on first AED 375,000 (small-business relief for all entities).</li>"
         "<li>Free Zone Qualifying Free Zone Person (QFZP) regime: 0% on Qualifying Income; 9% on non-qualifying.</li>"
         "<li>Economic Substance Regulations (ESR) parallel compliance for Relevant Activities.</li>"
         "<li>Transfer Pricing arm's-length principle, OECD-aligned, mandatory documentation for related-party transactions.</li>"
         "<li>CbCR (Country-by-Country Reporting) for MNE groups above EUR 750M consolidated revenue.</li>"
         "</ul>"),
        ("/ QFZP mechanics - 2026 FTA position", "The qualifying tests.",
         "<p>The <strong>Qualifying Free Zone Person</strong> status requires an entity to satisfy ALL of the following:</p>"
         "<ol>"
         "<li><strong>Adequate substance in a UAE Free Zone</strong> &mdash; actual activities carried out in the Free Zone with qualifying employees, operating expenditure proportional to activity, physical office space.</li>"
         "<li><strong>Derives Qualifying Income</strong> &mdash; specific list of qualifying activities and transactions updated through Cabinet Decision 55 of 2023 and subsequent FTA guidance.</li>"
         "<li><strong>Maintains audited financial statements.</strong></li>"
         "<li><strong>Complies with Transfer Pricing documentation requirements.</strong></li>"
         "<li><strong>Does not elect out of the QFZP regime</strong> (election is irrevocable for 5 years).</li>"
         "</ol>"
         "<p><strong>Qualifying Income</strong> (2024-2026 clarified position) includes:</p>"
         "<ul>"
         "<li>Income from transactions with other Free Zone persons (except for excluded activities).</li>"
         "<li>Income from Qualifying Activities with non-Free Zone persons.</li>"
         "<li>Income from ownership and exploitation of qualifying intangible assets (specific sub-regime).</li>"
         "<li>Treasury financing to related parties within the Free Zone group.</li>"
         "<li>Specified ancillary income (e.g., up to 5% of total revenue from non-qualifying activities under de minimis rule).</li>"
         "</ul>"
         "<p><strong>Excluded activities</strong> (always taxed at 9%):</p>"
         "<ul>"
         "<li>Transactions with natural persons (individuals) &mdash; except specific carve-outs.</li>"
         "<li>Banking, insurance, finance (certain categories).</li>"
         "<li>Ownership or exploitation of UAE real estate (except in specific Free Zone contexts).</li>"
         "<li>Transactions with non-Free Zone UAE Mainland (above the de minimis).</li>"
         "</ul>"),
        ("/ ESR + CT interaction - 2026 practice", "Two compliance tracks, one entity.",
         "<p>Economic Substance Regulations (ESR) were pre-existing (effective 2019) and continue alongside Corporate Tax. For entities carrying out Relevant Activities (banking, insurance, fund management, headquarters, holding, IP, distribution, lease-finance, shipping, service centre):</p>"
         "<ul>"
         "<li><strong>ESR Notification</strong> filed within 6 months of financial year-end (specific deadlines by Free Zone).</li>"
         "<li><strong>ESR Report</strong> filed within 12 months of year-end if the entity derived income from Relevant Activities.</li>"
         "<li><strong>Substance tests</strong> &mdash; core income-generating activities in UAE, adequate employees, operating expenditure, physical premises.</li>"
         "<li><strong>Non-compliance penalty</strong> &mdash; AED 20,000-50,000 for failures, with potential escalation.</li>"
         "</ul>"
         "<p>CT and ESR substance tests overlap but are not identical. Entities should run both separately: QFZP qualification for CT + ESR substance notification/report for applicable Relevant Activities.</p>"),
        ("/ Transfer Pricing - 2026 practice", "Documentation requirements for Dubai holdcos.",
         "<p>UAE CT requires arm's-length pricing for related-party transactions. Documentation levels:</p>"
         "<ul>"
         "<li><strong>Local File</strong> &mdash; mandatory for entities with related-party transactions above AED 40 million.</li>"
         "<li><strong>Master File</strong> &mdash; for MNE groups above AED 3.15 billion consolidated revenue.</li>"
         "<li><strong>CbCR</strong> &mdash; for MNE groups above EUR 750M.</li>"
         "<li><strong>Disclosure Form</strong> in the annual CT return.</li>"
         "</ul>"
         "<p>For an Indian-founder Dubai holdco with cross-border intercompany flows (IP licensing from Dubai parent to Indian subsidiary; service fees from Indian sub to Dubai parent; dividend upstream), the TP documentation needs careful construction. Functional analysis, benchmarking against OECD comparables, consistent application across years.</p>"),
        ("/ Pillar 2 (Global Minimum Tax) - UAE status 2026", "The 15% minimum tax conversation.",
         "<p>OECD Pillar 2 introduces a 15% global minimum effective tax rate for MNE groups above EUR 750M consolidated revenue. UAE has signalled intent to implement Pillar 2 through a Domestic Minimum Top-up Tax (DMTT) &mdash; effective status as of October 2026 is subject to confirmation via FTA guidance.</p>"
         "<p>If implemented:</p>"
         "<ul>"
         "<li>UAE 9% CT rate alone falls below 15% minimum.</li>"
         "<li>In-scope MNEs could face additional top-up tax to reach 15% effective rate on UAE profits.</li>"
         "<li>DMTT, if enacted, would keep the top-up tax within UAE rather than ceded to home-country IIR (Income Inclusion Rule).</li>"
         "</ul>"
         "<p>For Indian-founder UAE holdcos below the EUR 750M threshold, Pillar 2 does not directly apply at the entity level. For larger structures or Indian parent companies with UAE subsidiaries that aggregate across groups above EUR 750M, Pillar 2 modelling becomes essential.</p>"
         "<p>Monitor FTA announcements; the DMTT framework is expected to crystallise through late 2026 and 2027.</p>"),
        ("/ What to do", "The compliance checklist for Indian-founder Dubai holdcos.",
         "<ol>"
         "<li><strong>Register for CT</strong> with the FTA (deadlines by legal form; most entities registered by late 2024-2025).</li>"
         "<li><strong>Determine QFZP eligibility</strong> &mdash; substance, Qualifying Income analysis, de minimis compliance.</li>"
         "<li><strong>File CT return</strong> within 9 months of financial year-end.</li>"
         "<li><strong>Maintain Transfer Pricing documentation</strong> &mdash; Local File if above AED 40M related-party threshold.</li>"
         "<li><strong>File ESR Notification</strong> and Report for Relevant Activities.</li>"
         "<li><strong>Build audited financial statements</strong> &mdash; QFZP requires audited accounts.</li>"
         "<li><strong>Monitor Pillar 2 / DMTT updates</strong> if in a large MNE group.</li>"
         "</ol>"
         "<p><em>Last updated: 2026-10-07.</em></p>"),
    ],
    faqs=[
        ("Is UAE Corporate Tax a flat 9%?",
         "No - 0% on first AED 375,000 of taxable income (small-business relief), 9% above. Qualifying Free Zone Persons may qualify for 0% on Qualifying Income with 9% on non-qualifying. Pillar 2 for MNEs above EUR 750M may add further layers."),
        ("What activities qualify for QFZP 0% rate?",
         "Transactions with other Free Zone persons (except excluded activities), Qualifying Activities with non-Free Zone persons, ownership/exploitation of qualifying intangible assets, treasury financing to related parties, specified ancillary income within de minimis. Excluded activities (transactions with natural persons, UAE real estate, specific finance activities) are always 9%."),
        ("Can I move my shell Dubai holdco to QFZP status?",
         "Only if you build genuine UAE substance (local employees, operating expenditure proportional to activity, UAE physical office with staff) AND the entity derives Qualifying Income. A nominee-director + outsourced-accounting structure typically fails QFZP. Substance uplift is a 60-90 day engagement in our practice."),
        ("Does my Dubai holdco need an audit?",
         "QFZP requires audited financial statements. Non-QFZP (9% CT) entities above AED 50 million revenue require audit. Even smaller entities often need audit for banking, visa or regulatory purposes. Plan for ongoing audit cost in your UAE structure."),
        ("What is DMTT and does it affect my Dubai holdco?",
         "Domestic Minimum Top-up Tax (DMTT) is UAE's expected Pillar 2 implementation adding top-up tax to reach 15% effective rate for in-scope MNEs. Only MNE groups above EUR 750M consolidated revenue are in scope. For most Indian-founder Dubai holdcos (standalone or small groups), DMTT is not directly applicable. Monitor FTA guidance."),
        ("Does BQP handle UAE CT compliance for Indian founders?",
         "Yes - CT registration, QFZP qualification analysis, Qualifying Income structuring, Local File Transfer Pricing documentation, ESR Notification and Report, annual CT return filing, substance uplift. Co-ordinated with India-side FEMA ODI + Section 6(3) POEM defence. WhatsApp +91 78018 87130."),
    ],
    related=[
        ("india-uae-tax-treaty-dtaa.html", "DTAA", "India-UAE DTAA"),
        ("uae-incorporation-indian-founder.html", "Guide", "UAE Incorporation"),
        ("uae-corporate-tax-calculator.html", "Tool", "UAE CT Calculator"),
    ],
    cta_headline="Dubai holdco needs UAE CT compliance pack built or audited?",
    cta_body="Standard engagement: QFZP qualification, Qualifying Income analysis, ESR Notification + Report, Local File TP documentation, annual CT return, substance uplift if needed. Integrated with India-side FEMA ODI and POEM defence. 90-day diagnostic.",
))

# 4. ITR AY 2026-27 Changes
write_page("itr-filing-ay-2026-27-deadlines-changes-india", page(
    slug="itr-filing-ay-2026-27-deadlines-changes-india",
    title="ITR Filing AY 2026-27 India | Deadlines + New Forms + Changes - BQP",
    description="ITR filing for Assessment Year 2026-27 (Financial Year 2025-26): due dates, new form changes, Section 115BAC default regime, Section 44AB tax audit threshold, Schedule FA, Schedule FSI, interest + penalty for late filing. Working CA guide.",
    keywords="ITR filing AY 2026-27, ITR deadline 2026, new ITR forms 2026, Section 115BAC default new regime, Section 44AB audit threshold 2026, ITR-2 ITR-3 2026, Schedule FA ITR",
    hero_kicker="/ Blog &middot; ITR AY 2026-27 &middot; October 2026",
    hero_title_html="ITR filing AY 2026-27, <em>deadlines, forms, changes.</em>",
    hero_lead="For Assessment Year 2026-27 (Financial Year 2025-26, income earned 1 April 2025 to 31 March 2026), ITRs are being filed through 2026. This is the current state: due dates, Section 115BAC default new tax regime, Section 44AB tax audit threshold, Schedule FA for foreign assets, ITR form choice, and the specific penalties for late filing or non-disclosure.",
    sections=[
        ("/ Due dates for AY 2026-27", "The calendar.",
         "<ul>"
         "<li><strong>Non-audit taxpayers (individuals, HUFs, firms not requiring audit):</strong> 31 July 2026 (filed by now; late-filing applies if not).</li>"
         "<li><strong>Audit-requiring taxpayers (companies, firms above Section 44AB threshold):</strong> 31 October 2026 (approaching).</li>"
         "<li><strong>Taxpayers with international transactions / transfer pricing:</strong> 30 November 2026.</li>"
         "<li><strong>Belated return:</strong> up to 31 December 2026 with late-filing fee under Section 234F.</li>"
         "<li><strong>Updated return (ITR-U):</strong> up to 2 years from the end of the relevant assessment year (ITR-U for AY 2026-27 remains open until 31 March 2029) with additional tax.</li>"
         "</ul>"
         "<p>If you have not filed and the 31 July 2026 deadline has passed, file belated by 31 December 2026 with Section 234F late fee (INR 1,000 if income &lt; INR 5 lakh; INR 5,000 otherwise) + Section 234A interest at 1% per month on unpaid tax.</p>"),
        ("/ Section 115BAC - default new regime", "The regime switch.",
         "<p>Finance Act 2023 made the new tax regime (Section 115BAC(1A)) the default for individual taxpayers from AY 2024-25 onwards. For AY 2026-27:</p>"
         "<p><strong>New regime slabs (default):</strong></p>"
         "<ul>"
         "<li>Up to INR 3,00,000: Nil</li>"
         "<li>INR 3,00,001 - INR 7,00,000: 5%</li>"
         "<li>INR 7,00,001 - INR 10,00,000: 10%</li>"
         "<li>INR 10,00,001 - INR 12,00,000: 15%</li>"
         "<li>INR 12,00,001 - INR 15,00,000: 20%</li>"
         "<li>Above INR 15,00,000: 30%</li>"
         "</ul>"
         "<p>Plus surcharge (10% / 15% / 25% / 37% - with 37% effective only in old regime; new regime capped at 25%) and 4% cess.</p>"
         "<p><strong>Old regime remains available</strong> but requires explicit election each year via Form 10IEA (for salaried, filed before due date). Deductions under Chapter VI-A (80C, 80D, HRA, etc.) are available only under the old regime; the new regime allows only standard deduction (INR 75,000 salaried) and NPS employer contribution (14%).</p>"
         "<p><strong>Which regime wins:</strong> depends on total deductions you can claim under old regime. Rough rule: if your Section 80C + 80D + HRA + 24(b) home loan interest deductions sum to over INR 4-5 lakh, old regime typically wins for incomes above INR 10 lakh. Lower deductions = new regime wins. Model both before filing &mdash; our calculator at <a href=\"new-vs-old-tax-regime-calculator.html\">new-vs-old-tax-regime-calculator.html</a>.</p>"),
        ("/ Section 44AB tax audit threshold", "Who needs tax audit.",
         "<p>Tax audit under Section 44AB is required if:</p>"
         "<ul>"
         "<li><strong>Business turnover</strong> exceeds INR 1 crore (threshold raised to INR 10 crore if cash receipts and cash payments together are &le; 5% of turnover and payments).</li>"
         "<li><strong>Professional receipts</strong> exceed INR 50 lakh (threshold raised to INR 75 lakh if cash receipts and cash payments together are &le; 5%).</li>"
         "<li><strong>Presumptive scheme taxpayers</strong> (Section 44AD / 44ADA) opting out below the deemed profit percentage, where income exceeds basic exemption.</li>"
         "</ul>"
         "<p>Audit report (Form 3CA/3CB + 3CD) filed by 30 September 2026; ITR due by 31 October 2026.</p>"),
        ("/ Schedule FA + FSI - foreign assets disclosure", "Mandatory for ROR with foreign holdings.",
         "<p><strong>Schedule FA (Foreign Assets)</strong> &mdash; mandatory for Resident and Ordinarily Resident (ROR) taxpayers to disclose:</p>"
         "<ul>"
         "<li>Foreign bank accounts (balance, interest earned).</li>"
         "<li>Foreign financial interests (shares, securities, mutual funds held abroad).</li>"
         "<li>Foreign real estate.</li>"
         "<li>Foreign bank-signatory authority.</li>"
         "<li>Foreign trusts.</li>"
         "<li>Any other foreign asset or signatory authority.</li>"
         "</ul>"
         "<p><strong>Schedule FSI (Foreign Source Income)</strong> &mdash; mandatory for ROR to disclose foreign income (dividend, interest, capital gains, business, salary) and claim FTC (Foreign Tax Credit) under India-DTAA.</p>"
         "<p><strong>Non-disclosure penalty under Black Money Act</strong> &mdash; up to INR 10 lakh per undisclosed foreign asset, plus potential prosecution. Non-disclosure is high-risk; make Schedule FA complete and accurate.</p>"
         "<p>NRIs and RNORs: Schedule FA is NOT required (they are taxed on India-source only, not worldwide). But once ROR status attaches, Schedule FA is mandatory from year 1 of ROR.</p>"),
        ("/ Common ITR filing mistakes AY 2026-27", "What we see.",
         "<ul>"
         "<li><strong>Choosing wrong regime without modelling.</strong> New regime is default; old regime requires explicit election via Form 10IEA. Many salaried taxpayers accidentally stay on new regime without comparing.</li>"
         "<li><strong>Capital gains Schedule CG errors.</strong> Post-July-2024 LTCG at 12.5% without indexation. Common error: still applying old 20%-with-indexation rate for transfers after 23 July 2024.</li>"
         "<li><strong>TCS on LRS not claimed as credit.</strong> Form 27D must be matched; TCS flows into Form 26AS; claim as advance tax credit. Common oversight for first-time LRS remitters.</li>"
         "<li><strong>Schedule FA incomplete.</strong> Foreign brokerage accounts (US Fidelity / Schwab / Vanguard), foreign retirement accounts (401(k) / IRA), foreign bank accounts, UAE real estate &mdash; all must be disclosed year 1 of ROR status.</li>"
         "<li><strong>Form 10F missed for DTAA treaty-rate withholding claims.</strong> If you received India-source payments with 25% TDS when treaty rate was 15%, the correct position is to have filed Form 10F in advance to the payer. Post-fact, refund via ITR with FTC/Section-199 claim.</li>"
         "<li><strong>NRI not filing even with India-source income.</strong> NRO interest, Indian mutual fund LTCG, Indian property rent &mdash; all require ITR if above basic exemption or if TDS has been deducted (to claim refund).</li>"
         "</ul>"
         "<p><em>Last updated: 2026-10-07.</em></p>"),
    ],
    faqs=[
        ("What is the ITR deadline for AY 2026-27 in India?",
         "31 July 2026 for non-audit taxpayers (individuals, HUFs, non-audit firms). 31 October 2026 for audit taxpayers. 30 November 2026 for transfer-pricing cases. Belated return allowed up to 31 December 2026 with Section 234F late fee + Section 234A interest. Updated return (ITR-U) up to 31 March 2029."),
        ("Is the new tax regime default for FY 2025-26?",
         "Yes - Section 115BAC(1A) new regime is default from AY 2024-25 onwards. Old regime available but requires explicit election via Form 10IEA (filed before ITR due date). The new regime slabs are more favourable for taxpayers without large Section 80C/80D/HRA deductions; old regime wins where deductions exceed roughly INR 4-5 lakh at incomes above INR 10 lakh."),
        ("What is the Section 44AB tax audit threshold?",
         "Business turnover above INR 1 crore (or INR 10 crore if cash transactions are below 5%). Professional receipts above INR 50 lakh (or INR 75 lakh with low cash). Presumptive scheme (Section 44AD/44ADA) opt-out below deemed profit also triggers audit. Audit report Form 3CA/3CB + 3CD by 30 September 2026."),
        ("Do NRIs need to file an Indian ITR?",
         "Yes if NRI has India-source income above basic exemption (NRO interest, rental, Indian equity dividend, Indian property sale, Indian mutual fund redemption). ITR-2 for salary/capital gains income; ITR-3 for business income. NRIs are NOT required to file Schedule FA (foreign assets). Zero-India-source NRIs typically do not need to file."),
        ("What is Schedule FA and who files it?",
         "Schedule Foreign Assets - mandatory for ROR (Resident and Ordinarily Resident) taxpayers to disclose all foreign bank accounts, foreign financial interests, foreign real estate, foreign retirement accounts, trusts, and signatory authorities. Non-disclosure penalty up to INR 10 lakh per asset under Black Money Act plus potential prosecution. NRIs and RNORs are NOT required to file Schedule FA."),
        ("Does BQP file ITRs for AY 2026-27?",
         "Yes - annual ITR filing for individual taxpayers (ITR-2 for salary/capital gains, ITR-3 for business income), NRIs (ITR-2 with DTAA relief claim), audit-case ITR-5 for firms, and ITR-6 for companies with transfer-pricing documentation. New-vs-old regime modelling included. WhatsApp +91 78018 87130."),
    ],
    related=[
        ("ltcg-12-5-percent-new-capital-gains-india-2026.html", "Blog", "LTCG 12.5% Rule"),
        ("tcs-20-foreign-remittance-lrs-india-2026.html", "Blog", "TCS 20% on LRS"),
        ("new-vs-old-tax-regime-calculator.html", "Tool", "New vs Old Regime Calculator"),
    ],
    cta_headline="ITR AY 2026-27 due by 31 October (audit) / already due 31 July (non-audit).",
    cta_body="Audit-case ITRs still open until 31 October 2026. Belated non-audit ITRs allowed until 31 December with Section 234F fee + interest. We handle individual / NRI / audit-case / transfer-pricing ITRs for AY 2026-27. WhatsApp Durgesh.",
))

print("Batch I complete: 4 current-regulatory blog posts written")
