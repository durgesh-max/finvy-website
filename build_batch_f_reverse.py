# -*- coding: utf-8 -*-
"""Batch F: Reverse flip + fund structures (5 pages)."""
from build_lib import page, write_page

# 1. US-India reverse flip
write_page("us-india-reverse-flip-structure", page(
    slug="us-india-reverse-flip-structure",
    title="US-India Reverse Flip 2026 | Delaware Parent to Indian Parent - BQP",
    description="US-India reverse flip: converting a Delaware C-Corp parent back to Indian parent structure. FEMA, tax, shareholder consent, SEC/MCA mechanics. Used for Indian IPO track, listing shifts, operational realignment. CA guide.",
    keywords="US India reverse flip, Delaware to India parent, reverse flip tax India, Indian IPO foreign parent, Delaware C-Corp dissolution India, Phonepe reverse flip, Groww reverse flip",
    hero_kicker="/ Restructuring &middot; Reverse flip",
    hero_title_html="US-India reverse flip, <em>Delaware parent back to India.</em>",
    hero_lead="The reverse flip &mdash; converting a Delaware C-Corp parent structure back to an Indian parent structure &mdash; has become a well-worn playbook for Indian startups preparing for Indian IPO, operational realignment, or founder tax optimisation. PhonePe, Groww, Pine Labs, Zepto, Flipkart (partial), Razorpay are known examples. Here is the mechanics.",
    sections=[
        ("/ Why reverse-flip", "The three drivers.",
         "<p><strong>1. Indian IPO track.</strong> SEBI ICDR regulations and NSE / BSE main-board listing standards favour Indian-incorporated issuers. A Delaware C-Corp parent cannot list directly on Indian exchanges without a secondary listing framework. GIFT City IFSC listing is an alternative but has limited institutional depth. The cleanest path to Indian IPO is Indian parent + Indian operations.</p>"
         "<p><strong>2. Tax rate differential.</strong> Delaware C-Corp pays 21% federal + ~1-8% state corporate tax; dividend to Indian shareholders faces 15-25% US withholding (treaty-reduced). Net tax drag ~35-40% on distributed profits. Indian corporate: 25% + DDT abolished (dividend now taxed at shareholder level). Net tax drag for distributed Indian profits can be lower.</p>"
         "<p><strong>3. Operational realignment.</strong> If US customer base shrinks and India customer base grows, the Delaware parent becomes operational overhead. Indian parent simplifies banking, hiring, regulatory, and investor-reporting structure for an India-centric business.</p>"),
        ("/ The mechanics", "Share swap in reverse.",
         "<p>The reverse flip is essentially the India-to-Delaware flip run in reverse:</p>"
         "<ol>"
         "<li><strong>Set up the Indian parent company</strong> if not already existing. Typically a Private Limited Company under Companies Act 2013.</li>"
         "<li><strong>Shareholder swap:</strong> each existing Delaware C-Corp shareholder transfers their US shares to the Indian parent in exchange for Indian shares.</li>"
         "<li><strong>The Delaware C-Corp becomes a wholly-owned subsidiary</strong> of the Indian parent.</li>"
         "<li><strong>Operations continue</strong> with Indian parent as the primary funding and operating vehicle; Delaware subsidiary retained for US-side customer contracts, US employees, US bank accounts, until or unless wound down.</li>"
         "<li><strong>Capital structure cleanup:</strong> convert any outstanding SAFEs or convertible notes into equity before the swap, or roll them into equivalent Indian instruments.</li>"
         "</ol>"
         "<p>Alternative: NCLT-approved Scheme of Arrangement under Companies Act Section 230 &mdash; more complex, more expensive, but potentially tax-advantaged in specific scenarios.</p>"),
        ("/ Tax implications", "The expensive part.",
         "<p><strong>US side (for the Delaware C-Corp shareholders):</strong></p>"
         "<ul>"
         "<li>Shareholders exchanging Delaware stock for Indian shares trigger US capital gains on the swap. For US-person shareholders this is US-taxable (15-23.8% federal + state). For Indian-resident shareholders of Delaware C-Corp: generally US-exempt under India-US DTAA Article 13 (capital gains tax only in country of residence), but Section 897 (FIRPTA) may apply if the Delaware entity holds US real property interests.</li>"
         "<li>Section 367 outbound-transfer rules can apply if the swap is structured as a Section 368 reorganisation. Gain-recognition agreements may be needed.</li>"
         "</ul>"
         "<p><strong>India side (for Indian-resident shareholders):</strong></p>"
         "<ul>"
         "<li>Receiving Indian shares in exchange for Delaware shares: taxable event under Section 2(47). Fair-value computation drives the capital gain / loss.</li>"
         "<li>LTCG on unlisted foreign shares held 24+ months: 20% with indexation (or 12.5% without, post-July 2024).</li>"
         "<li>STCG: slab rate.</li>"
         "<li>FTC under India-US DTAA Article 25 for any US tax paid.</li>"
         "</ul>"
         "<p><strong>FEMA side:</strong></p>"
         "<ul>"
         "<li>The reverse flip inbound Indian equity side is treated as Foreign Direct Investment (FDI) into the Indian parent. Standard FDI pricing guidelines (DCF or fair-value) apply. Form FC-GPR filed with RBI within 30 days.</li>"
         "<li>If US-person shareholders will hold the Indian parent shares, their holding is reported as FDI; appropriate reporting on Form FC-GPR / FC-TRS as applicable.</li>"
         "<li>No specific ODI approval needed by India-resident swap participants &mdash; they are divesting foreign holdings for Indian equity.</li>"
         "</ul>"),
        ("/ When to reverse-flip", "Timing drives everything.",
         "<p>Like the forward flip, timing drives tax outcomes:</p>"
         "<ul>"
         "<li><strong>Pre-growth-round reverse flip:</strong> Delaware FMV is still low, Indian capital gains at swap are manageable. Window: before Series B / C.</li>"
         "<li><strong>Post-growth-round reverse flip:</strong> Delaware FMV is high; shareholders face material Indian capital gains at the swap. May require shareholder-funded tax payments or structured settlement.</li>"
         "<li><strong>Pre-IPO reverse flip (18-24 months before Indian IPO):</strong> necessary for SEBI eligibility; shareholders typically accept the tax hit as the cost of Indian IPO path. Needs careful transition period for subsidiary operations.</li>"
         "</ul>"
         "<p>PhonePe reverse flip (2022-23): reported tax outlay USD 950M on the swap &mdash; highlighted the cost of reverse-flipping at high valuation. Pine Labs, Groww and others have executed similar paths with planning.</p>"),
    ],
    faqs=[
        ("Why would an Indian startup reverse-flip from Delaware to India?",
         "Three main reasons: (1) Indian IPO track &mdash; SEBI listing standards prefer Indian issuer; (2) operational / cost realignment if the business has become India-centric; (3) tax rate differential as DDT abolition made Indian structure cleaner for distributed profits. The reverse flip has become routine for India-origin unicorns preparing for Indian listings."),
        ("How much does a reverse flip cost?",
         "The transaction fees (legal, CA, valuation) are modest &mdash; typically USD 100-500K for a Series B+ company. The real cost is capital gains tax on the shareholder swap. For a USD 100M+ FMV company with Indian-resident founders, capital gains can run into tens of millions. PhonePe reported ~USD 950M tax outlay on their 2022-23 reverse flip."),
        ("Is reverse flip tax-free?",
         "No. The shareholder swap is a taxable transfer under Section 2(47) in India (and under IRC Section 367 / 368 in the US). The structure can be optimised but the base case is: shareholders pay capital gains tax on the FMV uplift from their original Delaware share cost to the current FMV."),
        ("Can we reverse-flip without a shareholder-share swap?",
         "Alternative paths: NCLT-approved Scheme of Arrangement under Section 230 can achieve similar outcome with potentially different tax treatment, but adds 12-18 months and significant legal complexity. For most companies the direct shareholder swap is faster and simpler, even with the tax cost."),
        ("Does FEMA ODI apply to a reverse flip?",
         "The reverse flip is inbound into India &mdash; the FDI framework applies, not ODI. Indian parent receives foreign shareholders' Delaware shares in exchange for Indian equity &mdash; this is an inbound FDI transaction. Form FC-GPR filed, pricing-guideline-compliant valuation certificate obtained."),
        ("Does BQP structure reverse flips?",
         "Yes. For companies planning Indian IPO track or operational realignment, we scope the reverse flip (valuation, tax model per shareholder, FEMA / FDI pathway, Scheme of Arrangement if applicable, Delaware subsidiary ongoing-operations plan). Typical engagement 60-180 days. Request via get-a-quote.html."),
    ],
    related=[
        ("india-to-delaware-flip-structure.html", "Guide", "Forward Flip (India to Delaware)"),
        ("convert-llc-to-c-corp-f-reorganization.html", "Guide", "LLC to C-Corp"),
        ("sme-ipo.html", "Service", "SME IPO Advisory"),
    ],
    cta_headline="Preparing for Indian IPO with Delaware parent? Reverse flip is 18-24 months of planning.",
    cta_body="Reverse flip at scale is one of the most expensive transactions a company runs &mdash; shareholder tax outlays can run into tens of millions. Doing it right requires valuation strategy, Scheme vs direct swap choice, subsidiary transition planning, and multi-shareholder tax modelling. We scope and execute end-to-end.",
))

# 2. GIFT City vs Mauritius vs Singapore fund
write_page("gift-city-vs-mauritius-vs-singapore-fund", page(
    slug="gift-city-vs-mauritius-vs-singapore-fund",
    title="GIFT City vs Mauritius vs Singapore Fund 2026 | India Fund Hub - BQP",
    description="GIFT City IFSC vs Mauritius GBL vs Singapore VCC for India-focused funds: tax (Section 10(23FE), 10(4D)), substance, licensing, exit mechanics, LP perspective. Working CA fund-structuring guide.",
    keywords="GIFT City vs Mauritius, Singapore VCC vs GIFT City, India fund hub, Section 10(23FE), AIF Category III GIFT City, Mauritius fund India, India focused fund structure",
    hero_kicker="/ Fund structures &middot; India hub choice",
    hero_title_html="GIFT City vs Mauritius vs Singapore, <em>for India-focused funds.</em>",
    hero_lead="The three main fund-domicile choices for India-focused private capital are: GIFT City IFSC (India's onshore-international), Mauritius GBL (legacy post-2016-protocol), and Singapore VCC (regional-fund wrapper). Each has specific tax, substance, licensing and investor-perspective trade-offs. Here is the fund-structurer's working comparison.",
    sections=[
        ("/ GIFT City IFSC", "India's onshore-international hub.",
         "<p>GIFT City (Gujarat International Finance Tec-City) is India's International Financial Services Centre, regulated by IFSCA (International Financial Services Centres Authority). It is a Special Economic Zone with a dedicated tax, forex and regulatory regime designed to onshore activity that previously went to Singapore / Mauritius.</p>"
         "<p><strong>Tax features:</strong></p>"
         "<ul>"
         "<li><strong>Section 10(23FE):</strong> exemption on specified investments by Specified Persons (sovereign wealth, pension funds).</li>"
         "<li><strong>Section 10(4D):</strong> 0% Indian tax on income earned by specified Category III AIFs operating in IFSC on specified types of investment income.</li>"
         "<li><strong>Section 10(4F):</strong> 0% on income of non-resident unit holders of IFSC Category I/II/III AIFs on specified income.</li>"
         "<li>Standard 10-year 100% tax holiday for IFSC business units (Section 80LA).</li>"
         "<li>GST 0% on specified IFSC-based services.</li>"
         "</ul>"
         "<p><strong>Licensing:</strong> IFSCA Category I/II/III AIF regulations, familiar to Indian managers. GIFT City Fund Management Entity (FME) licence required for GPs.</p>"
         "<p><strong>Growing:</strong> ~100+ AIFs set up at GIFT City by 2025-26. Treated as 'onshore but international' &mdash; Indian capital-markets regulators are comfortable; foreign LPs are increasingly comfortable.</p>"),
        ("/ Mauritius GBL", "Legacy with narrowed utility.",
         "<p>Mauritius Global Business Licence (post-2019 reforms, previously Category 1 GBL) is the historical choice for India-focused funds. Pre-2016 protocol: capital-gains exemption on Indian equity. Post-2016 protocol: grandfathered pre-2017 holdings only.</p>"
         "<p><strong>Current status:</strong></p>"
         "<ul>"
         "<li>Mauritius GBL continues to work for new India investment on dividend, interest, royalty flows (treaty-reduced rates).</li>"
         "<li>No capital-gains advantage on new Indian equity post-April 2017.</li>"
         "<li>LOB + PPT + GAAR triple test applies to any Indian treaty-benefit claim.</li>"
         "<li>Mauritius local corporate tax 15% with partial-credit regime.</li>"
         "<li>Substance requirements enforced: 2+ Mauritius resident directors, Mauritius operating expenditure, Mauritius physical office, Mauritius accounting.</li>"
         "</ul>"
         "<p>Where it still fits: funds with grandfathered pre-2017 Indian equity holdings, India-UK-Africa structures where Mauritius serves multi-jurisdiction, specialist private debt funds routed via Mauritius.</p>"),
        ("/ Singapore VCC", "Regional-fund wrapper.",
         "<p>Variable Capital Company (VCC) is Singapore's dedicated fund vehicle, launched 2020. Replaces offshore structures for Singapore-regulated managers.</p>"
         "<p><strong>Features:</strong></p>"
         "<ul>"
         "<li>Umbrella structure &mdash; one VCC can hold multiple sub-funds with ring-fenced assets and liabilities.</li>"
         "<li>Regulated by MAS as a corporate vehicle.</li>"
         "<li>17% Singapore corporate tax (effective 10-12% with partial exemption).</li>"
         "<li>Section 13X / 13R tax exemptions available for qualifying fund managers.</li>"
         "<li>Strong treaty network and investor familiarity.</li>"
         "</ul>"
         "<p>Where it fits: pan-Asia funds investing across Singapore, India, Southeast Asia, Hong Kong, Indonesia. Not optimal for India-only fund (GIFT City is becoming the better choice there) but fits regional-fund structures.</p>"),
        ("/ Decision framework", "Match structure to strategy.",
         "<p><strong>GIFT City IFSC &mdash; choose if:</strong></p>"
         "<ul>"
         "<li>Fund is India-focused (90%+ Indian investments).</li>"
         "<li>Indian LPs are present or likely.</li>"
         "<li>Fund manager is India-based or willing to establish Fund Management Entity at IFSC.</li>"
         "<li>Tax efficiency on India-source income is primary optimisation.</li>"
         "</ul>"
         "<p><strong>Mauritius GBL &mdash; choose if:</strong></p>"
         "<ul>"
         "<li>Fund has existing Mauritius infrastructure.</li>"
         "<li>Multi-jurisdiction (India + Africa + Middle East) focus.</li>"
         "<li>Private debt or specific instruments where Mauritius offers advantage.</li>"
         "<li>Grandfathered pre-2017 Indian equity positions to manage.</li>"
         "</ul>"
         "<p><strong>Singapore VCC &mdash; choose if:</strong></p>"
         "<ul>"
         "<li>Pan-Asia or regional fund (India is one of many markets).</li>"
         "<li>Singapore MAS licensing for the fund manager.</li>"
         "<li>Strong Singapore / Southeast Asia LP base.</li>"
         "<li>Multi-currency / multi-asset flexibility.</li>"
         "</ul>"
         "<p>Many India-focused fund managers now choose GIFT City IFSC as default. Mauritius use is receding to legacy. Singapore VCC fits specific regional-fund mandates.</p>"),
    ],
    faqs=[
        ("What is Section 10(4D)?",
         "An Indian Income Tax exemption for income earned by specified Category III AIFs operating in GIFT City IFSC on specified types of investment income (capital gains on specified securities, interest, dividend, portfolio management income). Combined with 100% tax holiday under Section 80LA, GIFT City can deliver effectively 0% Indian tax on fund-level income for qualifying funds."),
        ("Is Mauritius still useful for India-focused funds?",
         "Only for narrow use cases. Post-2016 protocol closed the capital-gains exemption on new Indian equity. LOB + PPT + GAAR tests are strict. For funds with grandfathered pre-2017 Indian equity holdings, Mauritius continues to work. For new India-only funds, GIFT City is almost always better. For multi-jurisdiction (India + Africa) funds, Mauritius may still fit depending on specific needs."),
        ("What is Singapore VCC?",
         "Variable Capital Company &mdash; Singapore's dedicated fund vehicle regulated by MAS. Allows umbrella structure with multiple ring-fenced sub-funds. 17% headline corporate tax but Section 13X / 13R exemptions available for qualifying fund managers. Best fit for pan-Asia / regional funds where India is one of several markets."),
        ("Can an Indian fund manager set up a GIFT City IFSC fund without moving to Gujarat?",
         "Yes. GIFT City Fund Management Entity (FME) licensing has substance requirements (local directors, operational expenditure, physical office) but allows the manager's team to operate from India across multiple cities. Many Indian fund managers maintain Mumbai / Bengaluru main offices with a GIFT City FME office for substance."),
        ("What are typical fund setup costs across the three?",
         "GIFT City IFSC: INR 20-40 lakh setup + INR 15-25 lakh per year ongoing (FME licensing + accounting + audit + legal). Mauritius GBL: USD 25-45K setup + USD 20-35K per year. Singapore VCC: SGD 30-60K setup + SGD 25-45K per year. All exclude the actual compliance / FA / fund-admin cost which scales with AUM."),
        ("Does BQP structure funds in any of these three?",
         "Yes. GIFT City primary focus (strongest India angle); Mauritius for specific legacy / multi-jurisdiction mandates; Singapore VCC via co-ordinated counsel. Scoping covers investor base, India exposure, manager residence, strategy, and multi-year AUM plan. Request via get-a-quote.html."),
    ],
    related=[
        ("gift-city.html", "Service", "GIFT City Service"),
        ("india-mauritius-tax-treaty-dtaa.html", "DTAA", "India-Mauritius"),
        ("india-singapore-tax-treaty-dtaa.html", "DTAA", "India-Singapore"),
    ],
    cta_headline="Launching an India-focused fund? GIFT City is the default.",
    cta_body="For new India-focused funds in 2026, GIFT City IFSC delivers the strongest tax + regulatory + onshore-international combination. We handle the full stack: IFSCA FME licensing, AIF registration, LP documentation, Section 10(4D) / Section 80LA optimisation. Setup from INR 25 lakh.",
))

# 3. AIF Category II vs III tax
write_page("aif-category-ii-vs-iii-tax-india", page(
    slug="aif-category-ii-vs-iii-tax-india",
    title="AIF Category II vs III Tax 2026 | India Fund Choice - BQP",
    description="India AIF Category II vs Category III: pass-through status (Section 115UB), fund-level tax, LP-level tax, listed securities treatment, GAAR, GIFT City alternative. Working CA fund-structuring guide.",
    keywords="AIF Category II vs III, AIF tax India, Section 115UB AIF, pass through AIF, Category III AIF tax, PMS vs AIF, GAAR AIF",
    hero_kicker="/ Fund structures &middot; AIF choice",
    hero_title_html="AIF Category II vs III, <em>the tax choice.</em>",
    hero_lead="India's Alternative Investment Fund (AIF) framework under SEBI Regulations 2012 defines three categories. Category II (private equity, debt) and Category III (hedge, long-short, listed strategies) differ materially in tax treatment: Category II is pass-through (Section 115UB), Category III is fund-level taxable. This is the structural fork for Indian fund managers.",
    sections=[
        ("/ Category II vs Category III", "What each is.",
         "<p><strong>Category I AIF:</strong> social impact, SME funds, infrastructure &mdash; narrow category with specific government-backed treatment.</p>"
         "<p><strong>Category II AIF:</strong> funds that invest in private equity, private debt, real estate, structured credit &mdash; investments not falling in Category I or III and not using leverage beyond operational requirements.</p>"
         "<p><strong>Category III AIF:</strong> funds employing complex trading strategies, including long-short, derivatives, hedge-style strategies, listed-equity trading. May use leverage.</p>"
         "<p>Minimum investment per investor: INR 1 crore in all three categories. Minimum fund size: INR 20 crore. Lifecycle 7+ years for close-ended Category II.</p>"),
        ("/ Taxation of Category II AIF", "Pass-through under Section 115UB.",
         "<p>Category II AIF (and Category I) is a <strong>pass-through vehicle</strong> for Indian tax purposes under Section 115UB:</p>"
         "<ul>"
         "<li>Fund-level: no tax on income passing through to investors. Fund files return but tax liability flows up.</li>"
         "<li>Investor-level: each investor is taxed on their proportionate share of the fund's income, in the character of the underlying income (capital gain remains capital gain, dividend remains dividend, interest remains interest).</li>"
         "<li>Losses pass through to investors subject to specified conditions.</li>"
         "<li>TDS: fund deducts TDS on specific income types before distribution.</li>"
         "</ul>"
         "<p>Practical effect: a Category II AIF investing in unlisted Indian equity realises capital gains; investor receives LTCG (if 24+ month holding) at 12.5% (post-July 2024, without indexation) or 20% with indexation. Same tax rate as if the investor held the equity directly.</p>"),
        ("/ Taxation of Category III AIF", "Fund-level taxable.",
         "<p>Category III AIF does <strong>NOT</strong> get pass-through treatment:</p>"
         "<ul>"
         "<li>Fund-level: taxed as a 'specified fund' at MMR (maximum marginal rate &mdash; currently 42.744% including surcharge and cess for high-income trusts) or Section 115AD rate on specified income.</li>"
         "<li>Investor-level: receives distributions post-fund-tax; investor pays no further tax on the distributed amount.</li>"
         "<li>Effective tax drag at fund level is higher than Category II pass-through structure.</li>"
         "</ul>"
         "<p>Why Category III if it is tax-worse? Strategies that need Category III (long-short, derivatives, listed equity with leverage) are not permissible in Category II.</p>"
         "<p><strong>GIFT City IFSC Category III AIF under Section 10(4D):</strong> 0% Indian tax on specified investment income &mdash; this transforms the Category III economics and is why GIFT City IFSC has attracted so many Category III fund managers.</p>"),
        ("/ Decision framework", "When each category fits.",
         "<p><strong>Category II:</strong></p>"
         "<ul>"
         "<li>Private equity, venture capital, growth equity funds.</li>"
         "<li>Private debt funds (structured credit, mezzanine, direct lending).</li>"
         "<li>Real estate funds (Category II real estate, not REIT).</li>"
         "<li>Any fund investing primarily in unlisted equity.</li>"
         "</ul>"
         "<p><strong>Category III:</strong></p>"
         "<ul>"
         "<li>Long-short equity hedge funds.</li>"
         "<li>Macro, global-macro, derivatives strategies.</li>"
         "<li>Multi-asset absolute-return strategies.</li>"
         "<li>Listed-equity funds using leverage.</li>"
         "</ul>"
         "<p><strong>GIFT City IFSC Category III:</strong></p>"
         "<ul>"
         "<li>Same strategies as above but with Section 10(4D) + Section 80LA optimisation at IFSC.</li>"
         "<li>Effectively 0% Indian tax on specified fund income &mdash; a material advantage for high-turnover Category III strategies.</li>"
         "</ul>"),
    ],
    faqs=[
        ("Is Category II AIF tax-free for the fund?",
         "The fund itself does not pay income tax &mdash; income passes through to investors under Section 115UB. The investors pay tax on their proportionate share of fund income in the character of the underlying income. So the fund is 'tax-neutral' at fund level, not 'tax-free' in the system."),
        ("Why is Category III AIF taxed at the fund level?",
         "Category III employs trading strategies that make attribution of specific income to specific investors complex (constant portfolio churn, mixed asset types, derivatives). SEBI and the Income Tax Act chose fund-level taxation for simplicity. The MMR rate (~42.7%) is the trade-off."),
        ("Can an Indian LP invest in both Category II and Category III AIFs?",
         "Yes. Many Indian HNI investors hold diversified portfolios across Category II (PE, VC) and Category III (hedge, long-short) funds. Minimum investment INR 1 crore in each AIF."),
        ("What is Section 115AD?",
         "A specific rate for Category III AIF or certain Specified Persons on specified income &mdash; 15% on short-term capital gains, 10% on long-term capital gains, 20% on dividend / interest. This is lower than MMR and is the operative rate for Category III AIF on specified income types."),
        ("How does GIFT City IFSC change Category III economics?",
         "Section 10(4D) exempts specified income of Category III AIFs operating in IFSC. Combined with Section 80LA 100% tax holiday, GIFT City Category III can effectively deliver 0% Indian tax on fund-level income for qualifying funds. This has pulled Category III managers from Mumbai to GIFT City over the past 3-4 years."),
        ("Does BQP structure Category II and Category III AIFs?",
         "Yes. SEBI AIF registration (Category I/II/III), GIFT City IFSC AIF under IFSCA regulations where applicable, fund documentation (PPM, trust deed, investment management agreement), LP commitment co-ordination, ongoing fund administration setup. Request via get-a-quote.html."),
    ],
    related=[
        ("gift-city-vs-mauritius-vs-singapore-fund.html", "Guide", "GIFT City vs Mauritius vs SG"),
        ("what-is-aif-india.html", "Glossary", "What is AIF (India)"),
        ("gift-city.html", "Service", "GIFT City Service"),
    ],
    cta_headline="Launching an AIF? Category + domicile choice drives everything.",
    cta_body="Category II (PE / debt) is pass-through friendly. Category III (hedge / long-short) is MMR-taxed unless GIFT City. We scope the fund structure holistically: category, domicile, LP base, tax efficiency, SEBI/IFSCA licensing path. Request via get-a-quote.html.",
))

# 4. FDI vs FPI India startup investment
write_page("fdi-vs-fpi-india-startup-investment", page(
    slug="fdi-vs-fpi-india-startup-investment",
    title="FDI vs FPI India 2026 | Foreign Investment in Indian Startups - BQP",
    description="FDI vs FPI for foreign investors in Indian startups: automatic route vs approval, sector caps, FPI SEBI registration, aggregate limits, pricing guidelines, exit mechanics. Working CA guide.",
    keywords="FDI vs FPI India, foreign direct investment India startup, FPI registration India, FDI automatic route, FDI approval route India, Press Note 3, India startup foreign investor",
    hero_kicker="/ Cross-border investment &middot; FDI vs FPI",
    hero_title_html="FDI vs FPI, <em>how foreigners invest in Indian startups.</em>",
    hero_lead="Foreign Direct Investment (FDI) and Foreign Portfolio Investment (FPI) are the two primary routes for foreign capital into Indian companies. For Indian startup founders raising from US / UK / UAE / Singapore investors, understanding which route each investor uses determines sector eligibility, approval requirements, pricing, and exit mechanics.",
    sections=[
        ("/ FDI framework", "The default route for strategic investors.",
         "<p>Foreign Direct Investment (FDI) is governed by the FDI Policy and FEMA (Non-debt Instruments) Rules 2019. Foreign investors acquiring equity or compulsorily-convertible instruments in Indian companies for long-term participation use FDI.</p>"
         "<p><strong>Routes:</strong></p>"
         "<ul>"
         "<li><strong>Automatic Route:</strong> no prior approval needed; investor remits capital, Indian company issues shares, reports to RBI via Form FC-GPR within 30 days.</li>"
         "<li><strong>Approval Route:</strong> prior approval from the relevant administrative Ministry via FIFP portal; applies to specific sectors with caps (defence, retail, print media, etc.).</li>"
         "</ul>"
         "<p><strong>Sector caps:</strong> most Indian sectors permit 100% FDI automatic route. Specific caps apply: insurance 74%, defence 74%, banking (private) 74%, pharma brownfield 74%, print media 26%, broadcasting content 49%, multi-brand retail 51% (approval). Agriculture, lottery, gambling, chit funds &mdash; FDI prohibited.</p>"
         "<p><strong>Press Note 3 of 2020:</strong> investment from entities / individuals in countries sharing land borders with India (China, Pakistan, Nepal, Bhutan, Bangladesh, Myanmar, Afghanistan) requires prior approval regardless of sector. Includes beneficial owner tests. Delayed many China-origin VC rounds post-2020.</p>"),
        ("/ FPI framework", "The listed-equity portfolio route.",
         "<p>Foreign Portfolio Investment (FPI) is regulated by SEBI under FPI Regulations 2019. FPIs are foreign investors acquiring listed Indian equities, debt securities, or specified instruments for portfolio (not strategic) participation.</p>"
         "<p><strong>FPI registration categories:</strong></p>"
         "<ul>"
         "<li>Category I: government / sovereign-related entities, pension funds, banks, insurance companies &mdash; broadest access, lowest KYC burden.</li>"
         "<li>Category II: regulated funds, individual investors, family offices &mdash; standard access, higher KYC.</li>"
         "</ul>"
         "<p><strong>What FPIs can invest in:</strong></p>"
         "<ul>"
         "<li>Listed equities (primary + secondary market).</li>"
         "<li>Debt securities (government, corporate).</li>"
         "<li>Mutual fund units, ReITs, InvITs.</li>"
         "<li>Specified unlisted instruments (debt, hybrid) within limits.</li>"
         "</ul>"
         "<p><strong>Aggregate limits:</strong> FPI holding in a single listed Indian company capped at 10% of paid-up capital per FPI; aggregate FPI cap 24% of paid-up (increasable by board / shareholder resolution up to sector cap).</p>"),
        ("/ FDI vs FPI for startup founders", "Which investors use which route.",
         "<p><strong>FDI investors (for Indian startup rounds):</strong></p>"
         "<ul>"
         "<li>US / UK / EU venture capital funds directly investing in Indian company.</li>"
         "<li>Strategic corporate investors.</li>"
         "<li>HNI individual investors from treaty-benefit jurisdictions.</li>"
         "<li>Mauritius / Singapore / UAE holding companies of foreign funds.</li>"
         "</ul>"
         "<p><strong>FPI investors:</strong></p>"
         "<ul>"
         "<li>Portfolio investors in listed Indian equities (post-IPO).</li>"
         "<li>Debt-fund investors in listed Indian bonds.</li>"
         "<li>Mutual fund buyers (where FPI route applies).</li>"
         "</ul>"
         "<p>For an Indian startup raising a venture round from US / UK / Singapore VC: the investor uses FDI route. Form FC-GPR filed. If the investor is from a Press Note 3 country or has significant Chinese beneficial ownership, approval route applies.</p>"
         "<p>For an Indian listed company issuing an FPO or offering OFS: FPI route for foreign portfolio participants.</p>"),
        ("/ Pricing and exit mechanics", "Both routes have pricing guidelines.",
         "<p><strong>FDI pricing (unlisted companies):</strong></p>"
         "<ul>"
         "<li>Issue price must be at or above fair value determined by SEBI-registered Merchant Banker (DCF, NAV, or comparable company method).</li>"
         "<li>Fair value floor on primary issuance; discount only in specified circumstances with disclosure.</li>"
         "<li>Transfer of FDI holdings (secondary) similarly must be at or above fair value.</li>"
         "</ul>"
         "<p><strong>Exit from FDI investment:</strong></p>"
         "<ul>"
         "<li>Secondary sale to another foreign investor: FEMA-compliant pricing + Form FC-TRS within 60 days.</li>"
         "<li>Secondary sale to Indian resident: FEMA-compliant pricing + Form FC-TRS.</li>"
         "<li>Buyback by Indian company: subject to tax at company level post-Oct 2024.</li>"
         "<li>IPO: foreign holding converts to listed FPI-eligible equity.</li>"
         "</ul>"
         "<p><strong>FPI exit:</strong> standard stock-market sale subject to STT; capital gains tax applies at 12.5% LTCG / 20% STCG (post-July 2024).</p>"),
    ],
    faqs=[
        ("What is the difference between FDI and FPI?",
         "FDI (Foreign Direct Investment) is strategic / long-term equity investment, typically in unlisted companies, with investor playing an active role. FPI (Foreign Portfolio Investment) is passive / portfolio investment in listed securities for financial return. Different regulatory frameworks (FEMA + sector FDI policy for FDI; SEBI FPI regulations for FPI), different limits, different exit mechanics."),
        ("Does Press Note 3 of 2020 affect Indian startup rounds?",
         "Yes. Any investor from a land-border-sharing country (China, Pakistan, Nepal, Bhutan, Bangladesh, Myanmar, Afghanistan) or an investor with beneficial ownership traced to such a country needs prior government approval. In practice, mainland China HNI / fund investment into Indian startups has slowed dramatically since 2020. Startups with 2016-19-vintage Chinese investors may face scrutiny on subsequent rounds."),
        ("Can a US VC invest in an Indian Pvt Ltd through FDI automatic route?",
         "Yes, for most sectors. The US VC remits capital to the Indian company's bank account; the company issues shares; Form FC-GPR filed with RBI within 30 days. Pricing-guideline-compliant valuation certificate required. For restricted sectors (defence, insurance, media), approval route applies regardless of investor nationality."),
        ("What is Form FC-GPR?",
         "Foreign Currency - Government of Pakistan Rupee &mdash; no, it is Foreign Currency-General Permission Return. Form filed by the Indian company with RBI reporting fresh issuance of shares to a foreign investor. Filed via the RBI's FIRMS portal within 30 days of share issue. Mandatory for every FDI inbound transaction."),
        ("Can the same foreign investor invest via both FDI and FPI?",
         "Yes, in different capacities for different purposes. A US pension fund might hold FDI equity in a pre-IPO Indian company and FPI exposure to listed Indian equities. Each investment follows its respective framework; the investor must comply with both."),
        ("Does BQP handle FDI / FPI compliance for Indian startups?",
         "Yes. Pre-round scoping, pricing-guideline-compliant valuation certificate (via SEBI-registered Merchant Banker partner), Form FC-GPR filing within 30 days of share issue, Form FC-TRS for secondary transactions, FDI compliance for the Indian company's cap table. FPI setup for foreign funds investing in Indian listed securities also handled. Request via get-a-quote.html."),
    ],
    related=[
        ("us-incorporation.html", "Guide", "US Incorporation"),
        ("india-to-delaware-flip-structure.html", "Guide", "India to Delaware Flip"),
        ("gift-city-vs-mauritius-vs-singapore-fund.html", "Guide", "Fund Hubs"),
    ],
    cta_headline="Raising from US / UK / Singapore VC into your Indian company?",
    cta_body="FDI compliance drives whether the money arrives smoothly. We handle pre-round pricing certificate, Form FC-GPR within 30 days, FC-TRS for secondary, and the specific-sector approval if your investor's structure triggers Press Note 3. Standard FDI compliance per round from INR 50,000.",
))

# 5. NRI returning startup moving to India
write_page("nri-returning-startup-moving-to-india", page(
    slug="nri-returning-startup-moving-to-india",
    title="NRI Founder Moving Startup to India 2026 | Structure, Tax, FEMA - BQP",
    description="NRI founder moving back to India with their US / UAE / Singapore startup: entity migration, reverse flip, tax residence transition, FEMA inbound, employee / IP transfer. Working CA guide.",
    keywords="NRI startup move to India, returning entrepreneur India, Delaware company Indian founder relocate, Indian startup move from US, NRI founder RNOR startup",
    hero_kicker="/ Returning founder &middot; Moving startup",
    hero_title_html="NRI founder moving startup to India, <em>the full checklist.</em>",
    hero_lead="Indian founders with overseas startups (Delaware, UAE, Singapore) who decide to return to India permanently face a coordinated transition: personal tax residence shift (RNOR window), company domicile / IP migration, employee transition, FEMA inbound compliance, and ongoing tax structure. The sequence matters.",
    sections=[
        ("/ Four parallel workstreams", "What has to happen simultaneously.",
         "<p><strong>Workstream 1: Personal tax residence transition.</strong></p>"
         "<ul>"
         "<li>Day-count log in year of return.</li>"
         "<li>RNOR eligibility confirmation.</li>"
         "<li>NRE / FCNR account re-designation within 60-90 days.</li>"
         "<li>Foreign asset planning during RNOR window (sell appreciated US / UAE equity, convert IRA / 401(k) / pension).</li>"
         "<li>Section 6(1A) deemed-residency check if coming from zero-tax jurisdiction.</li>"
         "</ul>"
         "<p><strong>Workstream 2: Company domicile.</strong></p>"
         "<ul>"
         "<li>Keep overseas entity (Delaware / UAE / Singapore) as parent, continue operating; India becomes subsidiary.</li>"
         "<li>Reverse flip: overseas parent becomes Indian parent; overseas entity becomes subsidiary.</li>"
         "<li>Shutdown overseas entity, migrate operations fully to Indian entity.</li>"
         "<li>Choice depends on customer location, VC history, exit plan, tax arbitrage.</li>"
         "</ul>"
         "<p><strong>Workstream 3: Employee / contractor transition.</strong></p>"
         "<ul>"
         "<li>If moving operations to India: offer India employment to overseas employees willing to relocate or offer separation.</li>"
         "<li>Set up Indian payroll (Pvt Ltd, PF, ESI, Professional Tax).</li>"
         "<li>Handle contractor migration from overseas to Indian engagement.</li>"
         "<li>ESOP transition: re-grant under India plan, or honour overseas grants with proper tax at exercise.</li>"
         "</ul>"
         "<p><strong>Workstream 4: IP ownership + Transfer Pricing.</strong></p>"
         "<ul>"
         "<li>Where does IP live? Overseas parent? Indian subsidiary? New Indian parent (post reverse flip)?</li>"
         "<li>Transfer pricing documentation for ongoing cross-border service / royalty flows.</li>"
         "<li>Section 92CE / BEPS Action 13 CbCR if the group grows past applicable thresholds.</li>"
         "</ul>"),
        ("/ The decision tree", "Four scenarios for the returning founder.",
         "<p><strong>Scenario A: Delaware C-Corp, VC-funded, US customer base. Returning for personal reasons; operations stay global.</strong></p>"
         "<ul>"
         "<li>Keep Delaware parent. Set up Indian subsidiary.</li>"
         "<li>Founder operates from India as Indian resident; takes salary from Indian subsidiary.</li>"
         "<li>Delaware C-Corp continues US operations; Indian subsidiary services it (cost-plus 15% TP).</li>"
         "<li>Dividend to founder: 15-25% US withholding; India FTC.</li>"
         "<li>No reverse flip needed.</li>"
         "</ul>"
         "<p><strong>Scenario B: Delaware C-Corp, VC-funded, India has become 70%+ of customers.</strong></p>"
         "<ul>"
         "<li>Consider reverse flip &mdash; Indian parent + Delaware subsidiary for remaining US customers.</li>"
         "<li>Model shareholder-level capital gains at swap. Often prohibitive at scale.</li>"
         "<li>Alternative: operational realignment (shift IP + billing + employees to Indian subsidiary) without changing holding structure.</li>"
         "</ul>"
         "<p><strong>Scenario C: Dubai Free Zone LLC, consulting / trading business.</strong></p>"
         "<ul>"
         "<li>Keep Dubai entity for Dubai customers if any.</li>"
         "<li>Set up Indian Pvt Ltd for Indian customers.</li>"
         "<li>Founder's residence shifts to India &mdash; Dubai entity's POEM must still defend Dubai residence (local directors, Dubai expenditure) for Indian tax authority not to assert Indian residency on the Dubai company.</li>"
         "<li>Alternative: wind down Dubai entity if 90%+ Indian business, move all operations to Indian Pvt Ltd.</li>"
         "</ul>"
         "<p><strong>Scenario D: Singapore Pte Ltd, pan-Asia services business.</strong></p>"
         "<ul>"
         "<li>Keep Singapore parent for regional business.</li>"
         "<li>Set up Indian subsidiary for India operations.</li>"
         "<li>Nominee director service in Singapore if founder no longer resident there.</li>"
         "<li>POEM test: Singapore parent needs genuine SG substance to avoid Indian residency assertion.</li>"
         "</ul>"),
        ("/ FEMA inbound side", "What India requires on arrival.",
         "<p>When the founder returns to India and the overseas entity (now owned by Indian resident) continues to exist, FEMA ODI compliance remains:</p>"
         "<ul>"
         "<li>Annual Performance Report (APR) to be filed under FEMA for ongoing ODI holdings.</li>"
         "<li>Any further capital contribution to the overseas entity &mdash; LRS limit USD 250K per financial year applies if from personal funds.</li>"
         "<li>Dividend / salary received from overseas entity &mdash; must be routed through authorised dealer bank; declared on Indian ITR.</li>"
         "</ul>"
         "<p>If the Indian subsidiary of an overseas parent is being established fresh:</p>"
         "<ul>"
         "<li>Standard inbound FDI compliance (Form FC-GPR within 30 days).</li>"
         "<li>Pricing-guideline-compliant valuation.</li>"
         "<li>Press Note 3 check if any beneficial owner is from land-border country.</li>"
         "</ul>"),
        ("/ Common mistakes", "What returning founders miss.",
         "<ul>"
         "<li><strong>Not using the RNOR window.</strong> 2-3 year opportunity to clean up foreign assets without Indian tax. Many returnees discover RNOR only after it has ended.</li>"
         "<li><strong>Failing to establish POEM substance of overseas parent.</strong> After return, overseas parent risks being treated as Indian tax resident under Section 6(3) POEM rule. Local directors, local meetings, local decisions needed to defend overseas residence.</li>"
         "<li><strong>Overseas entity continuing without annual compliance.</strong> Delaware franchise tax, UAE licence renewal, Singapore ACRA filing, HMRC confirmation statement &mdash; all continue regardless of founder's physical location. Missed filings compound into penalty exposure.</li>"
         "<li><strong>Not re-pricing transfer pricing.</strong> Cost-plus markup that was fine when founder was in US now has to defend arm's-length against Indian-resident founder running the Indian subsidiary. BEPS Action 13 and Section 92D documentation become critical.</li>"
         "<li><strong>Tax-inefficient ESOP transition.</strong> Overseas ESOP grants exercised after return trigger Indian perquisite tax under Section 17(2) &mdash; often unexpectedly large on highly-appreciated grants.</li>"
         "</ul>"),
    ],
    faqs=[
        ("If I move to India permanently, does my Delaware C-Corp become Indian-taxable?",
         "Potentially &mdash; under Section 6(3) POEM test, if the C-Corp's Place of Effective Management shifts to India (founder is in India making all key decisions, no US-based decision-makers), the C-Corp can be treated as Indian tax resident and taxed on worldwide income. Defence: maintain US-based directors, hold US board meetings with documented minutes, keep US operational decision-makers. CBDT 2017 POEM guidelines spell out the test."),
        ("Should I close my Delaware C-Corp if I move back to India?",
         "Depends on business reality. If US customers / US VC / US bank relationships are strategic, keep the C-Corp and defend POEM. If US exposure is incidental, winding down the C-Corp and operating purely through Indian entity simplifies the structure. Winding down a C-Corp involves US dissolution process, final returns, Form 966, and 2-3 months timeline."),
        ("Can I take salary from my Delaware C-Corp while living in India?",
         "Yes. Delaware C-Corp pays you salary; US withholding on US-source services only (if services performed outside US, generally no US withholding). India taxes the salary as foreign-source income at your Indian slab rate. India-US DTAA Article 15 governs; India has primary taxing right for services performed in India by Indian resident."),
        ("What happens to my 401(k) when I move to India?",
         "You can keep the 401(k) with the US plan administrator or roll it to an IRA. Withdrawals are US-taxed at your US marginal rate + 10% early-withdrawal penalty if under 59.5. During RNOR window: no additional Indian tax on withdrawals. After ROR: potentially Indian-taxable with FTC under India-US DTAA Article 20. The RNOR window is often the best time to execute a Roth conversion or distribution strategy."),
        ("Do I need Indian investor approval before returning permanently?",
         "Not for personal relocation. However if your startup has Indian investors (angels, Indian VCs), they typically appreciate a transparent conversation about the operational implications. If overseas investors are present (US VCs on Delaware cap table), they may have shareholder-agreement clauses triggered by material changes in management location &mdash; review your SHA / IRA before announcing."),
        ("Does BQP handle NRI founder relocation to India?",
         "Yes end-to-end. Pre-return tax model (RNOR window asset planning), personal residence transition filings, company structure review (keep / flip / wind down), FEMA inbound setup, Indian subsidiary incorporation, Indian payroll setup, transfer pricing documentation first year, ongoing cross-border tax compliance. Typical engagement 6-12 months spanning pre-move to one-year-after. Request via get-a-quote.html."),
    ],
    related=[
        ("nri-returning-india-tax-rnor-transition.html", "Guide", "NRI Return to India"),
        ("us-india-reverse-flip-structure.html", "Guide", "Reverse Flip"),
        ("india-to-delaware-flip-structure.html", "Guide", "Forward Flip"),
    ],
    cta_headline="Moving back to India with a US / UAE / Singapore company? Start planning 6 months out.",
    cta_body="The RNOR window is the single most valuable planning opportunity in an NRI founder's life &mdash; and it is often missed because the planning conversation happens too late. We scope the full relocation 6-12 months before the move, build the asset-disposal and company-restructure plan, and handle the sequential filings.",
))

print("Batch F complete: 5 reverse-flip + fund-structure pages written")
