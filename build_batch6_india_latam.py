# -*- coding: utf-8 -*-
"""Batch 6: 4 India-LatAm DTAA pages + 1 LatAm expansion hub."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_seo import build_page, write_page

# -------- 1. India-Brazil DTAA --------
write_page("india-brazil-tax-treaty-dtaa", build_page(
    slug="india-brazil-tax-treaty-dtaa",
    title="India-Brazil Tax Treaty (DTAA) | Rates, Articles, Forms - BQP",
    description="India-Brazil DTAA: withholding on dividends, interest, royalties and FTS; tie-breaker residency; Form 10F and TRC for Indian claimants; practical mechanics for Indian firms selling to or operating in Brazil.",
    keywords="India Brazil DTAA, India Brazil tax treaty, Brazil withholding India, royalties India Brazil, FTS India Brazil, Receita Federal India, Indian company Brazilian subsidiary, Form 10F Brazil",
    hero_kicker="CROSS-BORDER TAX · DTAA · INDIA-BRAZIL",
    hero_title_html="The India-Brazil DTAA, <em>working guide.</em>",
    hero_lead="Signed 1988, in force since 1992. The treaty that governs how royalties, FTS, dividends and interest flow between the two largest democracies in their hemispheres. For Indian IT/engineering firms, pharma exporters and manufacturing operators engaging Brazil, this is the load-bearing document.",
    sections=[
        ("Overview", "What the treaty does",
         "<p>The India-Brazil Double Taxation Avoidance Agreement allocates taxing rights between two countries that each tax worldwide income. For Indian service exporters invoicing Brazilian customers, Indian firms setting up Brazilian subsidiaries, and Brazilian investors in Indian equity, the treaty determines whether gross withholding rates (potentially 15-25% Brazilian source rates) are reduced to treaty-capped levels. Brazil's domestic withholding on technical services and royalties is historically among the highest in the hemisphere, which makes the treaty materially valuable for Indian service providers.</p>"),
        ("Key articles", "Rates and residence",
         "<p><strong>Article 10 (Dividends):</strong> Cap of 15% withholding (vs Brazilian domestic position which currently exempts dividend WHT but may change under proposed reforms).</p>"
         "<p><strong>Article 11 (Interest):</strong> Cap of 15% on cross-border interest.</p>"
         "<p><strong>Article 12 (Royalties and FTS):</strong> Cap of 15% for royalties generally; 25% for trademarks (unusual provision). Fees for technical services covered at 15%.</p>"
         "<p><strong>Article 7 (Business profits):</strong> Standard PE-based taxation. An Indian firm with no Brazilian PE is not taxed in Brazil on business profits earned from Brazilian customers.</p>"
         "<p><strong>Article 4 (Residence):</strong> Tie-breaker cascade for dual residents.</p>"),
        ("Applicability for Indian claimants", "What to put together",
         "<p>For an Indian resident claiming treaty benefits on Brazilian-source income:</p>"
         "<ol>"
         "<li>Obtain an <strong>Indian Tax Residency Certificate (TRC)</strong> under Rule 21AB from the Indian tax department.</li>"
         "<li><strong>File Form 10F</strong> electronically on the Indian tax portal before the Brazilian payer makes the first payment.</li>"
         "<li>Submit the TRC + Form 10F to the Brazilian payer with a treaty invocation letter referencing the specific Article.</li>"
         "<li>Where the Brazilian characterisation of the payment differs (common for software, SaaS, consulting), prepare technical opinion supporting the treaty position.</li>"
         "<li>Claim foreign tax credit for Brazilian tax paid on your Indian ITR via Form 67, filed before the ITR due date.</li>"
         "</ol>"),
        ("Common disputes", "Software, consulting, FTS classification",
         "<p>Brazilian tax authorities have historically taken expansive views on characterising cross-border payments as royalties or FTS - categories that attract significant Brazilian withholding. For Indian software firms, SaaS providers, and consultants, the characterisation often determines whether the Brazilian customer withholds 15% (treaty-capped) or whether the payment escapes withholding under Article 7 as business profits.</p>"
         "<p>Written contract terms, scope of work, and the economic substance of the engagement all matter. Classifying a one-time SaaS subscription payment as a royalty vs a service fee has different outcomes under both Brazilian and Indian characterisation rules. The practice-tested approach: structure contracts explicitly, obtain supporting opinion where values are material, and document positions contemporaneously.</p>"),
    ],
    faqs=[
        ("Does the treaty eliminate Brazilian withholding on my SaaS revenue?",
         "If the payment is characterised as Article 7 business profits and your Indian firm has no Brazilian PE, Brazilian withholding does not apply. If characterised as Article 12 royalties/FTS, 15% treaty-capped withholding applies. Classification is the game."),
        ("What is the 25% rate for trademarks?",
         "The India-Brazil DTAA provides a higher cap (25%) for trademark royalties, unusual among Indian treaties. Mark the contract clearly if the payment is for trademark licence versus other IP."),
        ("Do I need Form 10F for a Brazilian payer?",
         "Yes - Form 10F is an Indian-side filing that the Brazilian payer may request as evidence of your Indian treaty-claimant status. File electronically on the Indian portal."),
        ("Can an Indian firm run Brazilian operations through a representative office?",
         "Possible but creates a Brazilian PE under the treaty, which pulls business profits into Brazilian tax. Most Indian firms contract directly from India without a Brazilian presence to stay outside Brazilian tax net on business profits."),
        ("How is capital gains on Brazilian equity taxed?",
         "Article 13 - most gains taxable in source country (Brazil) with few carve-outs. Brazilian capital gains tax on non-resident disposals is typically 15-22.5% depending on size and nature of gain."),
        ("What about Brazilian CSLL and PIS/COFINS on service payments?",
         "These are Brazilian domestic contributions that are not covered by the DTAA (not income taxes). They apply alongside any treaty-reduced income withholding. Factor into Brazilian pricing."),
    ],
    related=[
        ("global-taxation.html", "Service", "Global Taxation Advisory"),
        ("india-latin-america-expansion-guide.html", "Guide", "India-LatAm Expansion"),
        ("latin-america.html", "Hub", "Latin America Desk"),
    ],
    cta_headline="Indian firm invoicing Brazil, or Brazilian investor in India?",
    cta_body="The India-Brazil DTAA works - if the TRC, Form 10F, treaty invocation letter and (sometimes) the Brazilian characterisation defence are all in place from day one. BQP sets up and defends the treaty position end to end.",
))

# -------- 2. India-Mexico DTAA --------
write_page("india-mexico-tax-treaty-dtaa", build_page(
    slug="india-mexico-tax-treaty-dtaa",
    title="India-Mexico Tax Treaty (DTAA) | Rates, Articles, Forms - BQP",
    description="India-Mexico DTAA: withholding caps on dividends (10%), interest (10%), royalties and FTS (10%), tie-breaker residency, Form 10F and TRC for Indian claimants.",
    keywords="India Mexico DTAA, India Mexico tax treaty, Mexico withholding India, royalties India Mexico, FTS India Mexico, Indian company Mexican subsidiary, nearshoring India Mexico",
    hero_kicker="CROSS-BORDER TAX · DTAA · INDIA-MEXICO",
    hero_title_html="The India-Mexico DTAA, <em>working guide.</em>",
    hero_lead="Signed 2007, in force since 2010. The India-Mexico treaty is one of the cleaner LatAm bilaterals - 10% caps across the main heads, standard OECD architecture. For Indian firms exporting services to Mexico or setting up Mexican subsidiaries in the India-Mexico-US nearshoring corridor, this is the operative document.",
    sections=[
        ("Overview", "What the treaty does",
         "<p>Signed in September 2007 and effective from 2010, the India-Mexico Double Taxation Avoidance Agreement follows the OECD Model Tax Convention closely. It caps Mexican withholding on cross-border payments to Indian residents, provides tie-breaker residency rules, and gives Indian residents a credit on Indian ITR for Mexican tax paid. For Indian IT services firms, pharma exporters, and manufacturing operators engaging the Mexican market (either as customers or as nearshoring platform to the US), the treaty supports clean economics on cross-border flows.</p>"),
        ("Key articles", "The rate schedule",
         "<p><strong>Article 10 (Dividends):</strong> Cap of 10% withholding across the board (vs Mexican domestic 10% default - treaty confirms rather than reduces at this level).</p>"
         "<p><strong>Article 11 (Interest):</strong> Cap of 10% on cross-border interest.</p>"
         "<p><strong>Article 12 (Royalties and FTS):</strong> Cap of 10% on both royalties and FTS. Narrower FTS definition than the India-US treaty, closer to OECD norm.</p>"
         "<p><strong>Article 7 (Business profits):</strong> Standard - no Mexican tax on business profits of Indian residents without a Mexican PE.</p>"
         "<p><strong>Article 24 (Non-discrimination), Article 25 (MAP), Article 26 (Exchange of information):</strong> Standard protective articles, including BEPS-aligned information exchange.</p>"),
        ("Applicability for Indian claimants", "Operational mechanics",
         "<p>For an Indian resident claiming the 10% treaty cap on Mexican-source income:</p>"
         "<ol>"
         "<li>Obtain an Indian <strong>TRC</strong> under Rule 21AB (annually).</li>"
         "<li><strong>File Form 10F</strong> electronically on the Indian portal before Mexican payer disburses first payment.</li>"
         "<li>Provide the TRC + Form 10F to the Mexican payer, who claims the treaty rate on the Mexican side via SAT self-certification.</li>"
         "<li>Claim foreign tax credit for Mexican WHT paid on Indian ITR via Form 67.</li>"
         "</ol>"
         "<p>Mexican SAT and Indian AO both accept the treaty position when documentation is clean. Disputes rarely arise over rates; characterisation of specific payments (royalty vs service vs business profit) can still be contested.</p>"),
        ("India-Mexico-US nearshoring corridor", "An emerging use case",
         "<p>Since 2022, the India-Mexico-US corridor has become a visible structural play. Indian IT services firms (TCS, Infosys, Wipro, HCL and many mid-market peers) have expanded Mexican delivery centres to serve US customers under USMCA preferential terms with LatAm time zone coverage. The structure typically involves (i) Indian parent, (ii) Mexican operating subsidiary (SA de CV or S de RL de CV), (iii) US customer contracting entity. Intercompany flows between India and Mexico attract the treaty's 10% rates; transfer pricing documentation applies on all three sides.</p>"
         "<p>BQP supports this structure from the Indian side (ODI compliance, Form 3CEB, transfer pricing documentation, APR filings) with Mexican tax advisory on the Mexican side.</p>"),
    ],
    faqs=[
        ("Does the India-Mexico DTAA cover both federal and state Mexican tax?",
         "The treaty covers Mexican federal income tax (ISR). Mexican state taxes (payroll tax at state level, local real estate tax) are not covered and remain subject to Mexican domestic rules."),
        ("Can I claim 10% withholding on Mexican dividends via a Mauritius or Singapore holdco instead?",
         "Possibly, but the current India-Mauritius and India-Singapore treaties have significant LOB/GAAR safeguards and the Mauritius/Singapore-Mexico treaties have their own rate schedules. Direct India-Mexico claim via the India-Mexico DTAA is typically cleaner for operating income flows."),
        ("Is the FTS definition the same as India-US treaty?",
         "No - the India-Mexico FTS definition is closer to OECD norm (narrower than the India-US 'make available' version). Mexican-sourced services payments to Indian firms are more likely to be characterised as business profits under Article 7 than FTS under Article 12."),
        ("Do I need a Mexican representative to claim the treaty rate?",
         "No - the Mexican payer handles the treaty-rate withholding on the Mexican side with your TRC and Form 10F in hand. You do not need Mexican representation unless the Mexican payer requires it operationally."),
        ("How is intercompany transfer pricing documented?",
         "Mexican side: Local File, Country-by-Country Report (if applicable). Indian side: Form 3CEB with benchmarking study. Both must be consistent. We prepare both sides."),
        ("What if a Mexican tax audit challenges the treaty position?",
         "MAP (Mutual Agreement Procedure) under Article 25 is the escalation path, run jointly by Mexican SAT and Indian CBDT competent authorities. Timeline 24-36 months. BQP supports MAP filings from the Indian side."),
    ],
    related=[
        ("global-taxation.html", "Service", "Global Taxation Advisory"),
        ("india-latin-america-expansion-guide.html", "Guide", "India-LatAm Expansion"),
        ("latin-america.html", "Hub", "Latin America Desk"),
    ],
    cta_headline="Indian firm with Mexican operations or customers?",
    cta_body="The India-Mexico DTAA plus USMCA nearshoring structural tailwinds have made this corridor one of the most interesting cross-border opportunities for Indian services firms in the last decade. BQP structures the India-Mexico-US triangle from the Indian side.",
))

# -------- 3. India-Chile DTAA --------
write_page("india-chile-tax-treaty-dtaa", build_page(
    slug="india-chile-tax-treaty-dtaa",
    title="India-Chile Tax Treaty (DTAA) | 2020 Treaty Explained - BQP",
    description="India-Chile DTAA (2020): withholding caps on dividends (10%), interest (10%/15%), royalties (10%), FTS (10%), tie-breaker, Form 10F for Indian claimants. Lithium supply chain, mining, pharma considerations.",
    keywords="India Chile DTAA, India Chile tax treaty 2020, Chile withholding India, lithium India Chile, mining India Chile DTAA, SII India, Indian pharma Chile",
    hero_kicker="CROSS-BORDER TAX · DTAA · INDIA-CHILE",
    hero_title_html="The India-Chile DTAA, <em>since 2020.</em>",
    hero_lead="Signed 2020, in force from April 2021. The newest India-LatAm treaty, concluded as India seeks structural access to Chile's lithium reserves for the EV supply chain and as Chilean mining and services firms engage India's growing market.",
    sections=[
        ("Overview", "What the treaty does and why it matters now",
         "<p>The India-Chile DTAA was signed in March 2020 and entered into force in April 2021 (effective for tax years beginning 1 April 2022 in India and 1 January 2022 in Chile). The treaty closes a long-standing gap in India's LatAm treaty network and sits alongside India's older treaties with Brazil, Mexico, Colombia and Uruguay. Its practical significance has grown with India's electric vehicle expansion, which depends heavily on lithium - and Chile holds some of the world's largest lithium reserves in the Salar de Atacama. Indian battery and EV companies engaging Chilean lithium miners, Chilean exporters invoicing Indian customers, and Indian pharma firms engaging the Chilean market all operate under this treaty.</p>"),
        ("Key articles", "The rate schedule",
         "<p><strong>Article 10 (Dividends):</strong> Cap of 10% withholding across the board.</p>"
         "<p><strong>Article 11 (Interest):</strong> Cap of 10% for bank-sourced interest; 15% otherwise.</p>"
         "<p><strong>Article 12 (Royalties):</strong> Cap of 10% on royalties.</p>"
         "<p><strong>Article 12A (FTS):</strong> Separate dedicated article with 10% cap. Distinct from royalties and allowing clearer categorisation of technical fees.</p>"
         "<p><strong>Article 7 (Business profits):</strong> Standard PE-based taxation.</p>"
         "<p><strong>Article 13 (Capital gains):</strong> Source-country taxation on real estate and substantial-ownership shares; otherwise residence-country.</p>"
         "<p><strong>Article 27 (Entitlement to benefits - PPT):</strong> Principal Purpose Test built into the treaty from day one (aligned with BEPS Action 6). Benefits denied if obtaining the benefit was one of the principal purposes.</p>"),
        ("Applicability for Indian claimants", "Operational mechanics",
         "<p>For Indian residents claiming treaty benefits on Chilean-source income:</p>"
         "<ol>"
         "<li>Indian TRC under Rule 21AB (annually).</li>"
         "<li>Form 10F electronically on the Indian portal.</li>"
         "<li>Provide to Chilean payer who applies the treaty rate on Form 50 (or equivalent withholding form) at source.</li>"
         "<li>Claim foreign tax credit on Indian ITR via Form 67.</li>"
         "</ol>"
         "<p>Because the treaty includes PPT from inception, treaty-benefit claims must be defensible on commercial substance grounds. Pure holding structures without Chilean or Indian business substance are vulnerable to PPT denial.</p>"),
        ("Industry-specific application", "Lithium, mining, pharma, services",
         "<p><strong>Lithium / battery supply chain:</strong> Indian EV battery firms sourcing lithium carbonate or lithium hydroxide from Chilean miners pay Chilean suppliers for goods (not royalties/FTS), which generally sits outside WHT scope entirely as goods trade. Where supply agreements include technical fees, royalties, or financing arrangements, treaty rates apply.</p>"
         "<p><strong>Mining services:</strong> Indian engineering firms providing services to Chilean mining operators - treaty's 10% FTS cap applies if characterised as FTS; Article 7 business profits (nil Chilean WHT) if no Chilean PE and the service is pure consulting.</p>"
         "<p><strong>Pharma:</strong> Indian pharmaceutical companies licensing APIs or finished formulations to Chilean distributors pay 10% treaty-capped royalty WHT in Chile. Clinical trial services, regulatory consulting - typically Article 7 business profits.</p>"
         "<p><strong>SaaS / IT services:</strong> Treaty characterisation hinges on whether the service is FTS or business profits. For most SaaS subscriptions without 'make available' character, Article 7 applies with nil Chilean WHT.</p>"),
    ],
    faqs=[
        ("Is the India-Chile DTAA fully in force for both countries?",
         "Yes - entered into force April 2021. Effective for taxes beginning 1 April 2022 in India and 1 January 2022 in Chile. Applies to income earned after those dates."),
        ("Does PPT limit treaty access from day one?",
         "Yes - unlike older treaties where PPT came in via the Multilateral Instrument (MLI), the India-Chile DTAA includes PPT in Article 27 from the original text. Treaty-benefit claims must be defensible on commercial substance throughout."),
        ("Why does lithium matter in this treaty's practical use?",
         "Chile holds roughly 40% of global lithium reserves in the Salar de Atacama. India's EV battery sector (Reliance, Ola Electric, Tata, Exide and others) is building supply chains that depend on Chilean lithium. The treaty supports clean economics on associated technical fees, royalties, and financing flows between the two countries."),
        ("Can I use the treaty for Chilean mining investment via India?",
         "Possible but Chilean mining investment faces regulatory specifics (Chilean mining concession, DL 600 or current foreign investment regime) and the treaty's capital gains article (Article 13) taxes gains on substantial mining shareholdings in Chile at source. Structure with both treaty and local regulatory considerations in view."),
        ("How does the India-Chile DTAA compare to India-Mexico or India-Brazil?",
         "India-Chile is more modern (OECD/BEPS-aligned, PPT, separate FTS article at 10%, standard capital gains source rule). India-Brazil is older with higher cap for trademark royalties (25%) and standard FTS included in Article 12. India-Mexico is between the two, OECD-standard, no PPT at inception."),
        ("Do I need Chilean counsel for a treaty claim?",
         "The treaty-claim mechanics (W-8 equivalents, SII certification) require Chilean-side filing by the Chilean payer. If you have no Chilean entity, your Chilean payer handles it. If you have Chilean operations or a subsidiary, local counsel supports annual filings."),
    ],
    related=[
        ("global-taxation.html", "Service", "Global Taxation Advisory"),
        ("india-latin-america-expansion-guide.html", "Guide", "India-LatAm Expansion"),
        ("latin-america.html", "Hub", "Latin America Desk"),
    ],
    cta_headline="Indian firm engaging Chile - lithium, services, pharma?",
    cta_body="The 2020 India-Chile DTAA is modern, well-structured, and increasingly load-bearing as the India-Chile commercial relationship expands around EV supply chain and services. BQP structures Indian-side positions and documents treaty claims with PPT-defensible substance.",
))

# -------- 4. India-Colombia DTAA --------
write_page("india-colombia-tax-treaty-dtaa", build_page(
    slug="india-colombia-tax-treaty-dtaa",
    title="India-Colombia Tax Treaty (DTAA) | Rates, Articles, Forms - BQP",
    description="India-Colombia DTAA: withholding caps on dividends (5%/15%), interest (10%), royalties and FTS (10%), tie-breaker residency, Form 10F for Indian claimants.",
    keywords="India Colombia DTAA, India Colombia tax treaty, Colombia withholding India, royalties India Colombia, FTS India Colombia, Pacific Alliance India, Indian pharma Colombia",
    hero_kicker="CROSS-BORDER TAX · DTAA · INDIA-COLOMBIA",
    hero_title_html="The India-Colombia DTAA, <em>working guide.</em>",
    hero_lead="Signed 2011, in force since 2014. The treaty that governs Indian-Colombian cross-border income - royalties, FTS, dividends and interest. Core to Indian pharma, IT services and manufacturing engagement with Colombia and the broader Pacific Alliance market.",
    sections=[
        ("Overview", "What the treaty does",
         "<p>The India-Colombia DTAA was signed in May 2011 and entered into force in July 2014 (effective for tax periods starting 1 April 2015 in India and 1 January 2015 in Colombia). The treaty is a standard OECD/UN hybrid providing withholding rate reductions, tie-breaker residency, and credit for taxes paid. For Indian pharmaceutical exporters, IT services firms, and manufacturers engaging the Colombian market or the broader Pacific Alliance (Chile, Colombia, Mexico, Peru), the treaty establishes predictable economics.</p>"),
        ("Key articles", "The rate schedule",
         "<p><strong>Article 10 (Dividends):</strong> 5% cap for shareholdings of 25%+ by companies; 15% in other cases.</p>"
         "<p><strong>Article 11 (Interest):</strong> 10% cap generally.</p>"
         "<p><strong>Article 12 (Royalties and FTS):</strong> 10% cap on both royalties and FTS. FTS definition includes a 'make available' element similar to India-US but with Colombian characterisation nuances.</p>"
         "<p><strong>Article 7 (Business profits):</strong> Standard PE-based.</p>"
         "<p><strong>Article 13 (Capital gains):</strong> Standard - source country taxation on real estate and substantial-ownership shares.</p>"
         "<p><strong>Article 27 (Entitlement to benefits):</strong> PPT applied via MLI from 2020 (India and Colombia both signatories).</p>"),
        ("Applicability for Indian claimants", "Operational mechanics",
         "<p>For Indian residents claiming treaty benefits on Colombian-source income:</p>"
         "<ol>"
         "<li>Indian TRC (Rule 21AB).</li>"
         "<li>Form 10F electronically on the Indian portal.</li>"
         "<li>Provide to Colombian payer who claims the reduced treaty rate on the Colombian WHT return.</li>"
         "<li>Claim foreign tax credit on Indian ITR via Form 67.</li>"
         "</ol>"
         "<p>Colombia's domestic WHT rates on cross-border payments without treaty are high (20% on many categories). The 10% treaty cap on royalties/FTS is a material cash-flow reduction.</p>"),
        ("Common industry contexts", "Where the treaty gets used",
         "<p><strong>Indian pharma exporters:</strong> Licensing APIs and formulations to Colombian distributors - 10% treaty royalty WHT. Clinical trial services often fall under Article 7 business profits with nil Colombian WHT.</p>"
         "<p><strong>Indian IT services firms:</strong> Service contracts with Colombian banks, telcos, retailers - characterisation drives whether the Colombian payer withholds 10% (FTS treaty cap) or nil (Article 7 business profits with no Colombian PE).</p>"
         "<p><strong>Indian manufacturing / engineering:</strong> Equipment supply contracts (goods trade, no WHT) often combined with installation and commissioning services (potential FTS at 10% treaty cap). Contract structuring matters.</p>"
         "<p><strong>Pacific Alliance platform:</strong> Colombia is one of the four Pacific Alliance members (with Chile, Mexico, Peru) that have mutual free trade and labour mobility. Indian firms engaging Colombia often use it as a platform for the broader PA market.</p>"),
    ],
    faqs=[
        ("Can I claim 5% dividend WHT via the India-Colombia treaty?",
         "Yes - if your Indian company holds 25%+ of the Colombian paying company and meets any applicable LOB/PPT conditions. Below 25% ownership, 15% cap applies. Standard documentation (TRC + Form 10F) required."),
        ("How does FTS characterisation work under India-Colombia treaty?",
         "Article 12(3) defines FTS. Colombian characterisation of specific payments can differ from Indian characterisation; disputes historically have arisen over software, consulting, and management service payments. Contract language and SOW documentation matter."),
        ("Does PPT apply to the India-Colombia DTAA?",
         "Yes - via the Multilateral Instrument (MLI) from 2020 for Indian tax periods and corresponding Colombian periods. Treaty-benefit claims must be defensible on commercial substance."),
        ("What about Colombian ICA (Industria y Comercio) tax on service payments?",
         "ICA is a Colombian municipal tax on gross service revenue earned in a specific municipality. Not an income tax, not covered by the treaty. Applies to Colombian-performed services based on municipal jurisdiction."),
        ("Can I use the treaty for Pacific Alliance regional structuring?",
         "The India-Colombia DTAA covers India-Colombia bilateral flows only. Pacific Alliance regional structuring uses the Chile-Colombia-Mexico-Peru intra-alliance treaties on the Colombian side; your Indian flows need Colombia-India treaty, with Colombia-origin flows to other PA countries using those intra-PA treaties."),
        ("Does Colombia have a REIT/preferred regime that affects the treaty?",
         "Colombian ECE (CFC) rules and the ZESE (Zonas Economicas Especiales Sostenibles) regimes can affect how Indian-sourced income is treated on the Colombian side. Structure with both treaty and Colombian domestic regimes in view."),
    ],
    related=[
        ("global-taxation.html", "Service", "Global Taxation Advisory"),
        ("india-latin-america-expansion-guide.html", "Guide", "India-LatAm Expansion"),
        ("latin-america.html", "Hub", "Latin America Desk"),
    ],
    cta_headline="Indian firm engaging Colombia or the Pacific Alliance?",
    cta_body="The India-Colombia DTAA provides predictable economics and the Pacific Alliance provides regional platform. BQP structures Indian-side positions, documents treaty claims, and coordinates with Colombian counsel on the local-law side.",
))

# -------- 5. India-LatAm expansion hub guide --------
write_page("india-latin-america-expansion-guide", build_page(
    slug="india-latin-america-expansion-guide",
    title="India to Latin America Expansion Guide | DTAAs & Setup - BQP",
    description="Comprehensive guide for Indian firms expanding to Latin America: country-specific DTAA positions, FEMA ODI compliance, subsidiary setup, transfer pricing, repatriation planning for Brazil, Mexico, Chile, Colombia, Uruguay.",
    keywords="India LatAm expansion, India Latin America business guide, India LatAm DTAA, ODI LatAm India, Indian pharma LatAm, Indian IT services LatAm, Pacific Alliance India",
    hero_kicker="REGIONAL GUIDE · INDIA TO LATAM",
    hero_title_html="India to Latin America, <em>expansion playbook.</em>",
    hero_lead="India has DTAAs with Brazil, Mexico, Chile, Colombia, and Uruguay. For Indian pharma, IT services, manufacturing, and services firms expanding into LatAm, this is the structural map - country choices, treaty rates, ODI compliance, and the practical playbook.",
    sections=[
        ("Overview", "Why LatAm is on the Indian corporate radar",
         "<p>Latin America has moved from a peripheral market to a serious structural destination for Indian firms over the last 15 years. The drivers: USMCA repositioning (Mexico as a nearshore to the US), lithium and critical minerals supply (Chile, Argentina), pharmaceutical market access (Brazil, Mexico, Colombia regional heavyweights), IT services delivery centres in the US time zone (Mexico, Colombia, Costa Rica), and Pacific Alliance regional access through four economies. Indian IT services majors operate delivery centres across the region; Indian pharma companies export heavily to Brazil, Mexico, Colombia; Indian manufacturing firms (automotive, chemicals, textiles) have local subsidiaries in Mexico, Brazil, Argentina.</p>"),
        ("Country choice: where to anchor", "Comparative framework",
         "<p><strong>Mexico:</strong> US-Mexico-Canada platform via USMCA, India-Mexico treaty, strong SAT reciprocity. Default anchor for Indian firms targeting USA + LatAm.</p>"
         "<p><strong>Brazil:</strong> Largest LatAm economy, India-Brazil treaty since 1992. Complex regulatory environment, high ongoing compliance cost. Fits only if Brazilian market is specifically targeted - not as regional platform.</p>"
         "<p><strong>Chile:</strong> Open economy, India-Chile treaty (2020), lithium supply, Pacific Alliance member. Smaller market but excellent governance; strong base for Indian firms targeting the Southern Cone and resource-sector operations.</p>"
         "<p><strong>Colombia:</strong> Growing fintech/startup scene, India-Colombia treaty, Pacific Alliance. Good anchor for Indian firms targeting Andean region.</p>"
         "<p><strong>Uruguay:</strong> Territorial tax system, small market but regional holdco potential. Mercosur member. Niche but useful.</p>"
         "<p><strong>Peru, Costa Rica, Argentina:</strong> Country-specific plays; see individual country guides.</p>"),
        ("Indian-side setup: FEMA, ODI, filings", "What India requires",
         "<p>When an Indian company (or Indian individual via LRS) invests into a LatAm subsidiary, Indian regulatory compliance kicks in on day one:</p>"
         "<ol>"
         "<li><strong>FEMA ODI route:</strong> Automatic route for most LatAm destinations and most sectors; approval route if specific thresholds are crossed. Form ODI filed through AD bank within 30 days of remittance.</li>"
         "<li><strong>Annual Performance Report (APR):</strong> Filed with RBI every year the LatAm subsidiary is held, reporting investment value, performance, and any additional investments.</li>"
         "<li><strong>Transfer pricing (India-side):</strong> Form 3CEB with benchmarking study for any intercompany transactions (services, royalties, cost-sharing, financing).</li>"
         "<li><strong>ROC filings:</strong> Board resolutions on the Indian company's books, ODI declarations in the Indian audit.</li>"
         "<li><strong>Treaty position documentation:</strong> TRC + Form 10F if claiming treaty benefits on LatAm-sourced income flows back to India.</li>"
         "</ol>"
         "<p>BQP handles the Indian-side setup and ongoing compliance; local counsel in each LatAm jurisdiction handles the LatAm-side company formation and tax filings.</p>"),
        ("Working with BQP on your LatAm expansion", "What a mandate looks like",
         "<p>Typical BQP mandate scope for an Indian company expanding into one or more LatAm markets:</p>"
         "<ul>"
         "<li><strong>Pre-decision:</strong> Country choice analysis (treaty, regulatory, operational), transfer pricing framework, holdco structure option (direct vs via GIFT City, Mauritius, Singapore), total cost of ownership estimate.</li>"
         "<li><strong>Setup:</strong> FEMA ODI structure, Form ODI filing, intercompany agreement drafting, transfer pricing documentation setup, local counsel coordination for LatAm company formation.</li>"
         "<li><strong>Ongoing:</strong> Annual APR filing, Form 3CEB with benchmarking, treaty position maintenance, treaty benefit claims where income flows back to India, repatriation planning.</li>"
         "<li><strong>Exit:</strong> Sale of LatAm subsidiary, capital gains treatment under treaty, repatriation of proceeds, FEMA closure.</li>"
         "</ul>"
         "<p>We work with Indian firms from the pre-decision stage through long-term ongoing operations. See country-specific guides linked below.</p>"),
    ],
    faqs=[
        ("What is the first step for an Indian firm considering LatAm expansion?",
         "A pre-decision scoping call to work out (i) which LatAm country anchors your business, (ii) whether the structure should route through a holdco (GIFT City, Mauritius, Singapore) or go direct from India, (iii) the ODI route (automatic or approval), and (iv) the realistic cost of ongoing compliance. We do this on a free 20-minute call."),
        ("Can I use a GIFT City entity to hold my LatAm subsidiary?",
         "Yes - GIFT City IFSC entities (specifically GIFT City SPVs or AIFs) can hold foreign investments including LatAm subsidiaries. This can be tax-efficient for larger structures. For most mid-market Indian companies with a single LatAm subsidiary, direct Indian-company ownership is simpler."),
        ("Which LatAm country has the most India-friendly tax treaty?",
         "India-Mexico (10% caps, standard OECD architecture) and India-Chile (2020, modern, PPT-defensible from day one) are the cleanest and most predictable. India-Brazil (older, higher trademark royalty cap) and India-Colombia (standard but with Colombian characterisation nuances) are serviceable."),
        ("Can an Indian individual (not company) invest in LatAm via LRS?",
         "Yes - under the Liberalised Remittance Scheme (USD 250,000 per person per year), Indian individuals can invest personally in LatAm equity or operating businesses. ODI route applies to the extent the LRS is used for business/strategic investment vs portfolio."),
        ("Do you handle LatAm-side filings or just Indian-side?",
         "We handle Indian-side end-to-end (ODI, APR, 3CEB, treaty claims, repatriation planning). LatAm-side filings (local corporate formation, local tax returns, UBO filings) are handled by local counsel in each jurisdiction, coordinated by us."),
        ("How long does a typical India-to-LatAm setup take?",
         "Entity formation in most LatAm countries: 2-4 weeks. Indian ODI compliance: 3-6 weeks. Mercado banking (if US entity in the structure): 2-4 weeks. Transfer pricing documentation: 2-4 weeks parallel. Total from decision to operational structure: 8-14 weeks typical."),
    ],
    related=[
        ("global-taxation.html", "Service", "Global Taxation Advisory"),
        ("latin-america.html", "Hub", "Latin America Desk"),
        ("international-expansion.html", "Service", "International Expansion"),
    ],
    cta_headline="Indian firm scoping LatAm expansion?",
    cta_body="Picking the right anchor country, the right ODI route, and the right treaty position upfront saves 10x the cost of fixing it retroactively. 20 minutes on WhatsApp and we scope your options honestly - including whether LatAm is actually the right next step for your business.",
))

print("Batch 6 complete: 5 pages written (India-Brazil, India-Mexico, India-Chile, India-Colombia DTAAs + India-LatAm expansion hub)")
