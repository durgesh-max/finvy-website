# -*- coding: utf-8 -*-
"""Batch 5b: 4 more country-specific US incorp guides (Colombia, Peru, Uruguay, Costa Rica)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_seo import build_page, write_page

# -------- Colombia --------
write_page("us-incorporation-for-colombian-founders", build_page(
    slug="us-incorporation-for-colombian-founders",
    title="US Incorporation for Colombian Founders | Delaware & LLC - BQP",
    description="Delaware C-Corp or Wyoming LLC for Colombian founders: no US-Colombia treaty, DIAN Formulario 160 (activos en el exterior), ECE CFC rules, UBO filing via RUB.",
    keywords="US incorporation Colombian founders, Delaware C-Corp Colombia, Wyoming LLC from Colombia, DIAN Formulario 160, ECE Colombia CFC, RUB Colombia UBO, incorporacion Delaware desde Colombia, LLC EEUU colombiano",
    hero_kicker="US INCORPORATION · COLOMBIA",
    hero_title_html="US Incorporation for <em>Colombian founders.</em>",
    hero_lead="Delaware C-Corp or Wyoming LLC from Colombia. No comprehensive US-Colombia tax treaty, DIAN Formulario 160 reporting on foreign assets, ECE (Entidades Controladas del Exterior) CFC analysis, UBO filing via RUB - all handled.",
    sections=[
        ("Overview", "The Colombian founder's position",
         "<p>Colombia has become one of Latin America's most dynamic startup markets — Bogota and Medellin have both produced globally-noticed companies (Rappi, Habi, Addi). Many of those companies raised from US venture capital, which means Delaware C-Corp was part of their structure from an early stage. The Colombian founder forming a US entity today walks a path many Colombian predecessors have already walked, with reasonably stable regulatory treatment on both sides.</p>"
         "<p>The structural question for Colombian founders is similar to Mexican and Chilean peers: Delaware C-Corp for VC-backed startups, Wyoming LLC for bootstrapped operations, with Colombian-side DIAN reporting handled through a Colombian tax advisor working alongside the US-side mandate.</p>"),
        ("Colombian-side considerations", "DIAN, ECE, RUB",
         "<p><strong>No comprehensive US-Colombia tax treaty.</strong> Colombia and the US exchange information under the 2004 FATCA IGA, but there is no bilateral income tax treaty providing withholding rate reductions. Consequence: US withholding on dividends to Colombian recipients is the US domestic 30% rate; interest and royalties similarly. Treaty-rate planning is not available for Colombia-side flows.</p>"
         "<p><strong>DIAN Formulario 160 (Declaracion anual de activos en el exterior).</strong> Colombian residents with foreign assets above approximately 2,000 UVT must file Formulario 160 each year listing all foreign holdings - US entity shareholding, US bank accounts, US securities. Reporting is informative; the tax consequences flow through the main income tax return (Formulario 110 for companies, Formulario 210 for individuals).</p>"
         "<p><strong>ECE (Entidades Controladas del Exterior) CFC regime.</strong> Articles 882-893 of the Colombian Tax Statute attribute passive foreign entity income to Colombian controlling shareholders where control exists (generally 10%+ ownership or voting rights) and the entity derives principally passive income. US active-business entities are generally outside; US holding structures with passive income are generally caught.</p>"
         "<p><strong>UBO reporting via RUB (Registro Unico de Beneficiarios Finales).</strong> From 2022, Colombian entities must identify and report ultimate beneficial owners to the DIAN via RUB. Updates required within 30 days of any change. Penalty for non-compliance includes fines up to 200 UVT per violation.</p>"
         "<p><strong>Transfer pricing.</strong> Colombian entities with foreign related-party transactions above certain thresholds file transfer pricing documentation (DIAN Form 120) and comparable analysis.</p>"),
        ("Delaware C-Corp vs Wyoming LLC for Colombians", "Picking the vehicle",
         "<p><strong>Delaware C-Corp:</strong> Standard choice for Colombian startups raising from US VC. Mercado-visible precedents (Rappi, Habi) show the structure works at scale. Annual Delaware franchise tax (approximately USD 400+), Form 1120, Form 5472 for foreign related parties. VC-driven cost justified by fundraise ability.</p>"
         "<p><strong>Wyoming LLC:</strong> Preferred for Colombian solo founders, SaaS operators, e-commerce, bootstrapped service businesses. Lower annual cost (USD 60 state fee), Form 5472 + pro-forma 1120 as the main US filing. Good first step before any VC conversation becomes concrete.</p>"
         "<p><strong>Holding through a Colombian SAS:</strong> Possible but adds friction - Colombian corporate tax on attributed income, transfer pricing documentation requirements, UBO filing at the SAS level, and no US treaty benefit to extract. Direct personal shareholding by the Colombian founder is usually cleaner unless the SAS already exists for operational reasons.</p>"),
        ("Timeline and workflow from Colombia", "Practical sequence",
         "<p><strong>Weeks 1-2:</strong> Delaware/Wyoming formation, Operating Agreement/Bylaws, Registered Agent appointment.</p>"
         "<p><strong>Weeks 2-4:</strong> EIN via Form SS-4 fax. Colombian passport, cedula/NIT, Colombian address, formation document.</p>"
         "<p><strong>Weeks 4-6:</strong> Mercury or Brex banking. Colombian passport, EIN, formation documents. Mercury has been consistent for Colombian founders; expect 1-3 weeks approval.</p>"
         "<p><strong>Weeks 4-10:</strong> Colombian-side setup. DIAN Formulario 160 scoping if year-end approaching, ECE analysis documented (active vs passive characterisation), UBO filing on any Colombian SAS in the chain, transfer pricing scope assessment.</p>"
         "<p><strong>Ongoing annual:</strong> US side - Form 1120 (C-Corp) or Form 5472 + pro-forma 1120 (foreign-owned disregarded LLC), Delaware franchise tax, BOIR. Colombian side - Formulario 160 (by August of following year typically), Formulario 110/210 income tax, Formulario 120 transfer pricing if applicable.</p>"),
    ],
    faqs=[
        ("No US-Colombia tax treaty - what does that cost me?",
         "US withholding on cross-border payments (dividends, royalties, interest) applies at the US domestic 30% rate without treaty reduction. If your US entity primarily earns business profits from US customers (not dividend/royalty/interest flows back to Colombia), the treaty absence is operationally minor. If you plan passive income flows back to Colombia, the 30% withholding is a real cost."),
        ("Will my US LLC's income be attributed to me under ECE?",
         "If the LLC earns primarily active US business income (SaaS, services, e-commerce from US customers), the ECE active-business carve-out generally applies and attribution is avoided. If the LLC holds passive investments (dividends from US stock portfolio, rental income), ECE attribution is likely. Document the business facts contemporaneously."),
        ("How does the RUB UBO filing affect my US entity?",
         "RUB applies to the Colombian legal entity (if you hold the US entity through a Colombian SAS). If you hold the US LLC personally as a Colombian individual, RUB doesn't apply to the US entity directly. Where a Colombian SAS is in the chain, the SAS must register ultimate beneficial owners."),
        ("Can I claim Colombian foreign tax credit for US tax paid?",
         "Yes, under Colombian Tax Statute Article 254. Credit for actual US income tax paid, limited to Colombian tax that would have applied to the same foreign-source income. File supporting documentation (Form 1099, 1120, tax receipts). Credit cannot exceed Colombian tax on worldwide income times the ratio of foreign-source to total income."),
        ("Does Mercury accept Colombian founders?",
         "Yes - Mercury has approved Colombian passport-holders consistently since 2022. Expect standard underwriting (business explanation, source of initial capital). Approval 1-3 weeks after EIN. Alternative: Brex for VC-backed startups with visible funding."),
        ("What is the total year-1 cost for a Colombian founder?",
         "Wyoming LLC: approximately USD 1,500-2,500 covering formation, EIN, banking, Form 5472, plus Colombian-side Formulario 160 and 110/210 filings via local contador. Delaware C-Corp: USD 2,500-4,500 including Form 1120. Transfer pricing documentation adds USD 1,500-5,000 if required."),
    ],
    related=[
        ("us-incorporation.html", "Service", "US Incorporation (Overview)"),
        ("latin-america.html", "Hub", "Latin America Regional Desk"),
        ("how-to-get-ein-as-foreign-founder.html", "Guide", "How to Get an EIN as a Foreign Founder"),
    ],
    cta_headline="Colombian founder planning a US entity?",
    cta_body="Colombia has produced some of LatAm's biggest startup successes - and they all needed a clean Delaware or Wyoming structure plus DIAN-side reporting to work. 20 minutes and we scope the right vehicle for your business, including the ECE and DIAN footprint.",
))

# -------- Peru --------
write_page("us-incorporation-for-peruvian-founders", build_page(
    slug="us-incorporation-for-peruvian-founders",
    title="US Incorporation for Peruvian Founders | Delaware & LLC - BQP",
    description="Delaware C-Corp or Wyoming LLC for Peruvian founders: no US-Peru tax treaty, SUNAT foreign asset reporting, Regimen de Transparencia Fiscal CFC, Peruvian ongoing compliance.",
    keywords="US incorporation Peruvian founders, Delaware C-Corp Peru, Wyoming LLC from Peru, SUNAT foreign assets, Transparencia Fiscal Peru, incorporacion Delaware desde Peru, LLC EEUU peruano",
    hero_kicker="US INCORPORATION · PERU",
    hero_title_html="US Incorporation for <em>Peruvian founders.</em>",
    hero_lead="Delaware C-Corp or Wyoming LLC from Peru. No comprehensive US-Peru tax treaty, SUNAT foreign-asset reporting, Peruvian Regimen de Transparencia Fiscal CFC analysis - all handled in one mandate.",
    sections=[
        ("Overview", "Why Peruvian founders form US entities",
         "<p>Peru's startup ecosystem has grown steadily - Culqi, Favo, Fitco and others have raised meaningful rounds. The common thread for growth-stage Peruvian startups is that US venture capital investment usually accompanies a Delaware C-Corp structure, either from day one or via a flip from a Peruvian SAC. For bootstrapped Peruvian SaaS or consulting operators, Wyoming LLC gives US customer contracting and Stripe acceptance without the fundraise-oriented complexity.</p>"
         "<p>Peru's corporate tax (29.5%) is close to the US federal rate; the formation decision is operational rather than tax-arbitrage.</p>"),
        ("Peruvian-side considerations", "SUNAT, CFC, no treaty",
         "<p><strong>No US-Peru comprehensive tax treaty.</strong> Peru has treaties with Chile, Brazil, Canada, Mexico, Portugal, Switzerland, Korea - not the US. US withholding on cross-border payments to Peruvian recipients applies at the US domestic 30% rate without treaty reduction.</p>"
         "<p><strong>SUNAT foreign asset reporting.</strong> Peruvian residents file information on foreign holdings through the main income tax declaration (Form 710 for companies, Form 713 for individuals). Specific informative returns capture transactions and ownership positions in foreign entities.</p>"
         "<p><strong>Regimen de Transparencia Fiscal Internacional (Peruvian CFC).</strong> Introduced via Legislative Decree 1424, this regime attributes passive foreign entity income to Peruvian controlling shareholders where control exists (generally 50%+) and the foreign entity derives primarily passive income. US active-business entities fall outside; US holding structures with passive income generally fall inside.</p>"
         "<p><strong>UBO reporting (Beneficiario Final).</strong> From 2019, Peruvian legal entities must identify and report ultimate beneficial owners to SUNAT. Applies to the Peruvian SAC if one is in the chain; does not apply to the US entity directly.</p>"
         "<p><strong>Transfer pricing.</strong> Peruvian entities with related-party transactions above certain thresholds file transfer pricing documentation (DAOT and Technical Study / Country-by-Country for larger groups).</p>"),
        ("Delaware vs Wyoming for Peruvians", "Picking the vehicle",
         "<p><strong>Delaware C-Corp:</strong> Required for US VC fundraise. Clean founder-stock structure, 83(b) election, standard VC term-sheet readiness. Annual Delaware franchise tax, Form 1120, Form 5472.</p>"
         "<p><strong>Wyoming LLC:</strong> Preferred for Peruvian solo founders and bootstrapped operations. Low ongoing cost, Form 5472 + pro-forma 1120 as the main US annual filing. For most non-VC-bound Peruvian founders, this is the right starting point.</p>"
         "<p><strong>Through a Peruvian SAC:</strong> Rarely useful. Adds Peruvian corporate tax on attributed income, UBO filing, and transfer pricing documentation if intercompany flows exist. Direct personal shareholding is usually cleaner.</p>"),
        ("Timeline from Peru", "Practical sequence",
         "<p><strong>Weeks 1-2:</strong> Delaware/Wyoming formation, Operating Agreement/Bylaws, Registered Agent.</p>"
         "<p><strong>Weeks 2-4:</strong> EIN via Form SS-4 fax (+1-855-215-1627). Peruvian passport, RUC/DNI, Peruvian address, formation document.</p>"
         "<p><strong>Weeks 4-6:</strong> Mercury or Brex banking. Peruvian passport, EIN, formation documents. 1-3 weeks for approval.</p>"
         "<p><strong>Weeks 4-10:</strong> Peruvian-side setup. SUNAT foreign-asset filing coordination, Transparencia Fiscal analysis documented, UBO filing on any Peruvian SAC in the chain.</p>"
         "<p><strong>Ongoing annual:</strong> US side - Form 1120 or Form 5472 + pro-forma 1120, Delaware franchise, BOIR. Peruvian side - Form 710/713 income tax, DAOT and Technical Study if transfer pricing applies, UBO maintenance.</p>"),
    ],
    faqs=[
        ("No US-Peru treaty - what are the consequences?",
         "US withholding on cross-border income to Peruvian recipients at the US domestic 30% rate without treaty reduction. If your US entity primarily earns business profits from US customers, this is operationally minor. If you plan dividend/royalty flows back to Peru, 30% withholding is a real cost."),
        ("Will Transparencia Fiscal attribute my LLC's income to me?",
         "If the LLC earns primarily active US business income (SaaS, services, e-commerce from US customers), the active-business characterisation generally keeps income outside attribution. Passive portfolio holdings or passive investment structures are more likely to be attributed. Document actively."),
        ("Does the US-Peru Trade Promotion Agreement affect this?",
         "The 2009 US-Peru Trade Promotion Agreement covers trade and investment protections, not income tax. It is useful for merchandise trade and investment dispute resolution; it does not provide withholding rate reductions on cross-border income flows."),
        ("Can I claim Peruvian foreign tax credit for US tax paid?",
         "Yes, under the Peruvian Income Tax Law. Credit for actual US tax paid, limited to Peruvian tax that would have applied to the same foreign-source income. File supporting documentation."),
        ("Does Mercury accept Peruvian founders?",
         "Yes - approvals consistent since 2022 for clean documentation. Expect standard underwriting. 1-3 weeks typical."),
        ("Total year-1 cost from Peru?",
         "Wyoming LLC: USD 1,500-2,500 for US-side + Peruvian local tax advisor fees. Delaware C-Corp: USD 2,500-4,500. Transfer pricing documentation if applicable adds USD 1,500-5,000."),
    ],
    related=[
        ("us-incorporation.html", "Service", "US Incorporation (Overview)"),
        ("latin-america.html", "Hub", "Latin America Regional Desk"),
        ("how-to-get-ein-as-foreign-founder.html", "Guide", "How to Get an EIN as a Foreign Founder"),
    ],
    cta_headline="Peruvian founder considering a US entity?",
    cta_body="Peru's startup ecosystem is growing fast and the US entity structure is well-trodden. 20 minutes and we scope the right vehicle and the SUNAT-side footprint for your business.",
))

# -------- Uruguay --------
write_page("us-incorporation-for-uruguayan-founders", build_page(
    slug="us-incorporation-for-uruguayan-founders",
    title="US Incorporation for Uruguayan Founders | Delaware & LLC - BQP",
    description="Delaware C-Corp or Wyoming LLC for Uruguayan founders: Uruguay's territorial system, Law 19.484 CFC rules (2017), DGI foreign asset reporting, Zonas Francas option, no US treaty.",
    keywords="US incorporation Uruguayan founders, Delaware C-Corp Uruguay, Wyoming LLC from Uruguay, Uruguay territorial tax, Ley 19484 CFC Uruguay, DGI foreign assets, Zonas Francas Uruguay",
    hero_kicker="US INCORPORATION · URUGUAY",
    hero_title_html="US Incorporation for <em>Uruguayan founders.</em>",
    hero_lead="Delaware C-Corp or Wyoming LLC from Uruguay. Uruguay's territorial system (foreign income largely exempt under IRPF/IRAE), Ley 19.484 CFC rules introduced 2017, DGI foreign asset reporting, Zonas Francas considerations - all addressed.",
    sections=[
        ("Overview", "Why Uruguay is distinctive",
         "<p>Uruguay has operated a largely territorial income tax system - resident individuals and companies are taxed on Uruguayan-source income, with foreign-source income largely outside the Uruguayan tax net (subject to specific exceptions and CFC overrides). This makes Uruguay structurally different from Mexico, Brazil, Chile or Argentina (worldwide tax systems) when a resident forms a US entity.</p>"
         "<p>For a Uruguayan founder with primarily US-source income flowing through a US entity, the Uruguayan tax burden on that income is historically limited. The 2017 reforms (Law 19.484) and subsequent amendments (2022 passive income rule) tightened the territorial system around passive income from low-tax jurisdictions - active US business income remains largely outside Uruguayan tax but passive portfolio income is now generally caught.</p>"),
        ("Uruguayan-side considerations", "Territorial system, Law 19.484, DGI, Zonas Francas",
         "<p><strong>Territorial system.</strong> Uruguayan IRAE (corporate) and IRPF (personal) tax Uruguayan-source income. Foreign-source income is generally outside unless specifically pulled in - which, post-2017 and especially post-2022 reforms, happens more often than before.</p>"
         "<p><strong>Law 19.484 (2017) CFC-like rules.</strong> Attributes certain foreign entity income to Uruguayan residents where the foreign entity is in a low-tax jurisdiction (effective tax rate below 50% of Uruguayan rate) and the shareholder controls the foreign entity. US entities generally fall outside the low-tax jurisdiction trigger (21%+ federal corporate rate).</p>"
         "<p><strong>2022 passive income reform.</strong> Under pressure from EU/OECD, Uruguay introduced reforms (Law 20.095) extending IRAE to certain foreign-source passive income (dividends, interest, royalties, capital gains) earned by qualifying Uruguayan companies - unless substance tests are met. The reform specifically targets letterbox-type Uruguayan companies holding foreign passive investments.</p>"
         "<p><strong>DGI reporting.</strong> Uruguayan residents report foreign entity holdings through the annual income tax declaration. Informative filings exist for foreign bank accounts and controlled foreign entities.</p>"
         "<p><strong>Zonas Francas.</strong> Uruguayan Free Zones (Zonamerica, World Trade Center Montevideo, others) offer tax-exempt corporate status for qualifying operations. A Uruguayan Zona Franca user can hold foreign investments with tax benefits that regular Uruguayan companies cannot access. Niche but relevant for larger structures.</p>"),
        ("Delaware vs Wyoming for Uruguayans", "Picking the vehicle",
         "<p><strong>Wyoming LLC:</strong> Our usual recommendation for Uruguayan solo founders. Low ongoing cost (USD 60/yr), simple structure, Form 5472 + pro-forma 1120 the main US filing. Uruguay's territorial system often results in minimal Uruguayan tax on active US business income earned via the LLC.</p>"
         "<p><strong>Delaware C-Corp:</strong> Required for US VC fundraise. Standard C-Corp compliance (Form 1120, Delaware franchise). Uruguay's territorial system still generally applies to the Uruguayan shareholder's position.</p>"
         "<p><strong>Zonas Francas holding:</strong> For Uruguayan high-net-worth individuals or family offices with substantial foreign portfolios, a Zona Franca Uruguayan company holding the US entity can be tax-efficient at scale. Requires substance (Zona Franca presence, staff, operations) and economic rationale. Not for everyday startup use.</p>"),
        ("Timeline from Uruguay", "Practical sequence",
         "<p><strong>Weeks 1-2:</strong> Delaware/Wyoming formation, Operating Agreement/Bylaws, Registered Agent.</p>"
         "<p><strong>Weeks 2-4:</strong> EIN via Form SS-4 fax. Uruguayan passport, cedula, address, formation docs.</p>"
         "<p><strong>Weeks 4-6:</strong> Mercury or Brex banking. Uruguayan passport, EIN, formation documents. 1-3 weeks approval.</p>"
         "<p><strong>Weeks 4-8:</strong> Uruguayan-side setup. DGI foreign-asset filing coordination, CFC/passive-income analysis documented, Zonas Francas assessment if applicable.</p>"
         "<p><strong>Ongoing annual:</strong> US side - Form 1120 or Form 5472 + pro-forma 1120, Delaware franchise, BOIR. Uruguay side - annual IRPF/IRAE declaration, foreign-asset informative filings.</p>"),
    ],
    faqs=[
        ("Does Uruguay's territorial system mean I pay no tax on US LLC income?",
         "For active US business income earned by a Wyoming LLC held personally by a Uruguayan resident, Uruguayan IRPF generally does not apply (foreign-source income outside the territorial net). The 2022 passive income reform pulled certain foreign-source passive income into IRAE for Uruguayan companies - but it does not generally extend to Uruguayan individuals holding foreign entities with active income. Fact-specific; discuss on scoping."),
        ("Is there a US-Uruguay tax treaty?",
         "No comprehensive income tax treaty. There is a Tax Information Exchange Agreement (TIEA) that supports information sharing but does not provide withholding rate reductions. US domestic withholding rates apply on US-source payments to Uruguayan recipients."),
        ("Does Law 19.484 catch my Wyoming LLC?",
         "The low-tax-jurisdiction trigger (effective rate below 50% of Uruguayan 25%) is not met by US entities (21% federal). The LLC generally falls outside the Law 19.484 CFC net. The 2022 passive income reform may still catch Uruguayan company holders if the LLC derives passive income - active business income is generally fine."),
        ("What about Zonas Francas - should I use one?",
         "For an individual startup founder, no - overkill for the use case. Zonas Francas work for substantial foreign portfolios held by Uruguayan companies with genuine substance in the Free Zone. For most Uruguayan founders forming a US LLC for operational purposes, direct personal shareholding is simpler and tax-efficient enough given the territorial system."),
        ("Does Mercury accept Uruguayan founders?",
         "Yes - Uruguayan passport-holders approved consistently. Expect standard underwriting. 1-3 weeks after EIN."),
        ("Total year-1 cost from Uruguay?",
         "Wyoming LLC: USD 1,500-2,500 for US-side + Uruguayan contador fees (lower due to simpler territorial reporting). Delaware C-Corp: USD 2,500-4,500."),
    ],
    related=[
        ("us-incorporation.html", "Service", "US Incorporation (Overview)"),
        ("latin-america.html", "Hub", "Latin America Regional Desk"),
        ("how-to-get-ein-as-foreign-founder.html", "Guide", "How to Get an EIN as a Foreign Founder"),
    ],
    cta_headline="Uruguayan founder structuring a US presence?",
    cta_body="Uruguay's territorial system can make a US LLC particularly tax-efficient for Uruguayan residents compared to Mexican or Chilean peers. 20 minutes and we scope the right vehicle given the 2022 passive-income reforms and your specific income profile.",
))

# -------- Costa Rica --------
write_page("us-incorporation-for-costa-rican-founders", build_page(
    slug="us-incorporation-for-costa-rican-founders",
    title="US Incorporation for Costa Rican Founders | Delaware & LLC - BQP",
    description="Delaware C-Corp or Wyoming LLC for Costa Rican founders: territorial system (expanded 2024 for passive income), Hacienda reporting, Zona Franca option, no US treaty.",
    keywords="US incorporation Costa Rican founders, Delaware C-Corp Costa Rica, Wyoming LLC from Costa Rica, Costa Rica territorial tax, Hacienda foreign assets, Zona Franca Costa Rica, incorporacion Delaware desde Costa Rica",
    hero_kicker="US INCORPORATION · COSTA RICA",
    hero_title_html="US Incorporation for <em>Costa Rican founders.</em>",
    hero_lead="Delaware C-Corp or Wyoming LLC from Costa Rica. Costa Rica's territorial system (expanded to foreign passive income from 2024), Hacienda reporting, Zona Franca Regime, no US-Costa Rica tax treaty - all handled.",
    sections=[
        ("Overview", "Costa Rica as a growing LatAm hub",
         "<p>Costa Rica has emerged as a regional hub for US-adjacent operations - tech services, nearshoring, SaaS, biosciences. The combination of English fluency in the Costa Rican workforce, geographic proximity to the US, stable democratic governance, and a historically-territorial tax system has made it attractive for US-facing operations and for individual founders based there.</p>"
         "<p>From a US incorporation perspective, Costa Rican founders face similar structural questions to peers in Uruguay (territorial system, no US treaty) with the recent twist that Costa Rica's territorial system has been reformed under EU/OECD pressure to pull in certain foreign-source passive income from 2024.</p>"),
        ("Costa Rican-side considerations", "Hacienda, 2024 territorial reform, Zona Franca",
         "<p><strong>Territorial system with 2024 reforms.</strong> Costa Rica's traditional territorial system taxed only Costa Rica-source income. In 2023, Costa Rica was added to the EU list of non-cooperative jurisdictions over the territorial exemption for passive income. Costa Rica reformed via Law 10.381 (effective 2024), extending Costa Rican corporate tax to certain foreign-source passive income (dividends, interest, royalties, capital gains) earned by qualifying Costa Rican entities, with substance exceptions for genuine operations.</p>"
         "<p><strong>Hacienda reporting.</strong> Costa Rican residents report income on the annual D-101 (corporate) or D-102 (individual). Foreign asset holdings are declared through the main return and informative returns where applicable.</p>"
         "<p><strong>Zona Franca Regime (Law 7210).</strong> Costa Rica's Free Zone regime grants qualifying companies tax-exempt status for operations within the Free Zone. Common for US-service-exporting operations (BPO, SaaS development, call centres). A Zona Franca user can hold US-adjacent operations tax-efficiently; direct ownership of a US entity by an individual Costa Rican founder is a separate analysis.</p>"
         "<p><strong>UBO reporting (Transparencia).</strong> Costa Rican entities report ultimate beneficial owners via the Registro de Transparencia y Beneficiarios Finales under BCCR (Banco Central). Required for Costa Rican legal entities in the chain.</p>"
         "<p><strong>Transfer pricing.</strong> Costa Rican companies with related-party transactions apply arm's length principles; documentation requirements grew after 2020 reforms.</p>"),
        ("Delaware vs Wyoming for Costa Ricans", "Picking the vehicle",
         "<p><strong>Wyoming LLC:</strong> Our usual recommendation. Low ongoing cost, Form 5472 + pro-forma 1120 as the main US filing. Costa Rica's territorial system (with 2024 passive income carve-outs) means active US business income earned via the LLC generally stays outside Costa Rican tax for individual-held structures.</p>"
         "<p><strong>Delaware C-Corp:</strong> For US VC fundraise. Full C-Corp compliance.</p>"
         "<p><strong>Zona Franca Costa Rican entity + US entity:</strong> Combination used by US-service-exporting operations with substantial Costa Rican staff. Zona Franca tax exemption on the Costa Rican side, US entity for US customer contracting. More complex structure; worth evaluating only for operations with multiple employees in Costa Rica.</p>"),
        ("Timeline from Costa Rica", "Practical sequence",
         "<p><strong>Weeks 1-2:</strong> Delaware/Wyoming formation, Operating Agreement/Bylaws, Registered Agent.</p>"
         "<p><strong>Weeks 2-4:</strong> EIN via Form SS-4 fax. Costa Rican passport, cedula, address, formation docs.</p>"
         "<p><strong>Weeks 4-6:</strong> Mercury or Brex banking. 1-3 weeks approval.</p>"
         "<p><strong>Weeks 4-8:</strong> Costa Rica-side setup. Hacienda informative filing coordination, 2024 passive income rule analysis if the entity will earn passive flows, Zona Franca scoping if applicable.</p>"
         "<p><strong>Ongoing annual:</strong> US side - Form 1120 or Form 5472 + pro-forma 1120, Delaware franchise, BOIR. Costa Rica side - D-101 or D-102, foreign asset informative filings.</p>"),
    ],
    faqs=[
        ("Does the 2024 passive income reform catch my Wyoming LLC?",
         "If you hold the LLC personally as a Costa Rican individual, the 2024 reform (Law 10.381) is directed at Costa Rican legal entities, not individuals. Individual-held active-business LLCs generally stay outside the reform. If you hold the LLC through a Costa Rican SA or SRL and the LLC generates passive income, the Costa Rican entity may now be taxed on attributed income unless substance tests are met."),
        ("No US-Costa Rica treaty - practical cost?",
         "US withholding on cross-border income to Costa Rican recipients at the US domestic 30% rate without treaty reduction. For primarily active US business income, operationally minor."),
        ("Can I use the Zona Franca Regime for my US-facing operations?",
         "Zona Franca requires substantial operating substance in Costa Rica (employees, physical space, qualifying activities). For a founder-only setup it's not a fit. For operations with 10+ Costa Rica-based staff doing US-facing services, Zona Franca can be very tax-efficient and is worth structuring deliberately."),
        ("How does Hacienda treat distributions from my US LLC?",
         "Distributions to a Costa Rican resident individual from a wholly-owned US LLC held personally are generally outside Costa Rican tax under the territorial system (foreign-source income). The 2024 reform targets Costa Rican entities, not individuals. Specific facts can shift the analysis."),
        ("Does Mercury accept Costa Rican founders?",
         "Yes - Costa Rican passport-holders approved consistently. 1-3 weeks after EIN."),
        ("Total year-1 cost from Costa Rica?",
         "Wyoming LLC: USD 1,500-2,500 for US-side + Costa Rican contador fees. Delaware C-Corp: USD 2,500-4,500. Zona Franca-integrated structures: materially higher due to local setup complexity but tax-efficient at scale."),
    ],
    related=[
        ("us-incorporation.html", "Service", "US Incorporation (Overview)"),
        ("latin-america.html", "Hub", "Latin America Regional Desk"),
        ("how-to-get-ein-as-foreign-founder.html", "Guide", "How to Get an EIN as a Foreign Founder"),
    ],
    cta_headline="Costa Rican founder structuring US-facing operations?",
    cta_body="Costa Rica's territorial system plus the 2024 passive income reform plus the Zona Franca Regime creates several structural options - and getting the right one depends on whether you are a solo founder or scaling with Costa Rica-based staff. 20 minutes and we work out the right path.",
))

print("Batch 5b complete: 4 pages written (Colombia + Peru + Uruguay + Costa Rica)")
