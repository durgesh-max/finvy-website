# -*- coding: utf-8 -*-
"""Batch 5a: LatAm hub + 4 country-specific US incorp guides (Brazil, Mexico, Argentina, Chile)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_seo import build_page, write_page

# -------- Hub: Latin America --------
write_page("latin-america", build_page(
    slug="latin-america",
    title="Latin America | US Incorporation, Cross-Border Advisory - BQP",
    description="BQP serves Latin American founders setting up US entities (Delaware C-Corp, Wyoming LLC), and Indian firms expanding into LatAm. Country desks: Brazil, Mexico, Argentina, Chile, Colombia, Peru, Uruguay, Costa Rica. English, Spanish, Portuguese support.",
    keywords="Latin America CA firm, US incorporation Latin America, Delaware C-Corp Latin American founders, cross-border advisory LatAm India, incorporacion Delaware desde Latinoamerica, abrir LLC Estados Unidos, india LatAm business",
    hero_kicker="REGIONAL HUB · LATIN AMERICA",
    hero_title_html="Latin America, <em>cross-border advisory.</em>",
    hero_lead="Delaware C-Corp or Wyoming LLC formation for LatAm founders. India-LatAm trade and tax structuring. Spanish and Portuguese support. Country desks for Brazil, Mexico, Argentina, Chile, Colombia, Peru, Uruguay and Costa Rica.",
    sections=[
        ("What we do", "Two directions, one practice",
         "<p>BQP is a CA-led advisory firm historically focused on India-US cross-border work. Over the last three years our mandate has broadened: we now serve Latin American founders forming US entities (Delaware C-Corp and Wyoming LLC) with the same end-to-end approach we offer Indian founders, and we support Indian clients expanding operations and sales into Latin American markets.</p>"
         "<p>The LatAm desk is positioned around the practical realities most LatAm founders face: capital controls (Argentina), narrow or missing US tax treaties (Brazil, Argentina, Colombia, Peru, Uruguay, Costa Rica), CFC regimes at home, and the operational need for a US entity to accept Stripe, close US customers, or raise from US venture capital.</p>"),
        ("Country desks", "Where we have active mandates",
         "<p><strong>Brazil:</strong> Delaware C-Corp formation, no US-Brazil tax treaty considerations, CBE declaration to BCB, DEEE registration. Portuguese-speaking support available. See <a href='us-incorporation-for-brazilian-founders.html'>US incorporation for Brazilian founders</a>.</p>"
         "<p><strong>Mexico:</strong> Delaware or Wyoming formation, US-Mexico tax treaty application (10% dividend WHT, 15% interest, 10% royalties), REFIPRES CFC rules, SAT reporting. See <a href='us-incorporation-for-mexican-founders.html'>US incorporation for Mexican founders</a>.</p>"
         "<p><strong>Argentina:</strong> Delaware/Wyoming formation with capital-controls aware structuring, 1981 narrow US-Argentina treaty considerations, Bienes Personales planning. See <a href='us-incorporation-for-argentine-founders.html'>US incorporation for Argentine founders</a>.</p>"
         "<p><strong>Chile:</strong> Delaware/Wyoming formation under the new 2024 US-Chile tax treaty (15% dividend WHT, 10% interest, 2-10% royalties), SII DJ 1929 compliance, DL 824 Form 50. See <a href='us-incorporation-for-chilean-founders.html'>US incorporation for Chilean founders</a>.</p>"
         "<p><strong>Colombia, Peru, Uruguay, Costa Rica:</strong> Country-specific guides available via the direct URLs. All desks handle US formation + home-country reporting in one mandate.</p>"),
        ("Services for LatAm founders", "What we actually deliver",
         "<p>The LatAm desk covers the same scope as our India desk, calibrated to the home jurisdiction:</p>"
         "<ul>"
         "<li><strong>US entity formation</strong> — Delaware C-Corp or Wyoming LLC with EIN, Operating Agreement, Registered Agent, Mercury/Brex banking introduction</li>"
         "<li><strong>Home-country compliance</strong> — outbound investment reporting to the central bank or tax authority (BCB, BACEN, BCRA, BCCh, SAT, SII, BanRep, SBS, BCU, BCCR as applicable)</li>"
         "<li><strong>Tax treaty positioning</strong> — Form W-8BEN / W-8BEN-E, Certificate of Residence, treaty-rate claim at US withholding</li>"
         "<li><strong>CFC analysis</strong> — home-country Controlled Foreign Corporation rules (REFIPRES in Mexico, Normas de Rentas Pasivas in Chile, ECE in Colombia, Transparencia Fiscal in Argentina/Peru)</li>"
         "<li><strong>Ongoing US compliance</strong> — Form 1120, Form 5472, Delaware franchise tax, BOIR</li>"
         "<li><strong>Language support</strong> — Spanish and Portuguese for key documents; English for all technical filings</li>"
         "</ul>"),
        ("Content in Spanish and Portuguese", "Native-language resources",
         "<p>Core guides are available in Spanish at <strong>/es/</strong> and in Brazilian Portuguese at <strong>/pt/</strong>:</p>"
         "<ul>"
         "<li><a href='/es/incorporacion-delaware-fundadores-latinoamericanos.html'>Incorporaci&oacute;n Delaware para fundadores latinoamericanos</a></li>"
         "<li><a href='/es/incorporacion-wyoming-llc.html'>Incorporaci&oacute;n Wyoming LLC desde Latinoam&eacute;rica</a></li>"
         "<li><a href='/es/ein-sin-ssn.html'>C&oacute;mo obtener el EIN sin SSN</a></li>"
         "<li><a href='/pt/incorporacao-delaware-fundadores-brasileiros.html'>Incorpora&ccedil;&atilde;o Delaware para fundadores brasileiros</a></li>"
         "<li><a href='/pt/incorporacao-wyoming-llc.html'>Incorpora&ccedil;&atilde;o Wyoming LLC do Brasil</a></li>"
         "</ul>"
         "<p>Working-session discussion in Spanish or Portuguese is available on request. Written filings and formal advisory remain in English for consistency with US regulators.</p>"),
    ],
    faqs=[
        ("Why would a Latin American founder work with an India-based CA firm?",
         "The service substance (US entity formation, EIN, banking, ongoing compliance, home-country reporting) is agnostic of the advisor's physical location. Our LatAm clients pick us for cost-effectiveness (materially lower than US law firms for the same scope), direct-access working style, and the depth we bring from running India-US cross-border mandates for several years. Communication is in English with Spanish/Portuguese on request."),
        ("Do you handle Brazilian BCB and DEEE reporting?",
         "Yes. For Brazilian clients incorporating in the US, we handle (or liaise with a local Brazilian partner for) the CBE declaration to BCB when outbound capital exceeds the threshold, DEEE registration for direct investment, and ongoing reporting on the Receita Federal side (DIRPF for individuals, ECF for Brazilian companies with foreign holdings)."),
        ("What languages do you work in?",
         "Written formal advisory and all US-regulator filings in English. Working-session discussion available in English, Spanish, or Portuguese on request. Key client-facing guides published in Spanish at /es/ and Portuguese at /pt/."),
        ("Do you take Mexican, Chilean, or Colombian tax-residence clients?",
         "Yes — for US entity formation and US-side ongoing compliance, we take clients from any Latin American jurisdiction. For home-country tax positions where local counsel is critical, we work alongside your in-country tax advisor rather than replacing them. Our strength is the US-India-LatAm cross-border coordination."),
        ("How do you handle Argentine capital controls (CEPO)?",
         "The CEPO constrains how Argentine residents move capital out of Argentina — this is a BCRA-side regulatory issue, not something we resolve in Buenos Aires. We advise on US-side structuring that is compatible with Argentine controls (e.g., keeping founder stock at nominal values, timing capital contributions to coincide with legal outbound windows). An Argentine lawyer handles the AFIP/BCRA side; we handle Delaware/Wyoming."),
        ("Can you support India-LatAm trade clients?",
         "Yes. India has DTAAs with Brazil, Mexico, Chile, Colombia and Uruguay. For Indian clients selling into LatAm or Indian firms setting up LatAm subsidiaries (fintech, SaaS, pharma), we structure the India side (ODI compliance, Form 3CEB, transfer pricing) with LatAm-local tax advisory on the LatAm leg."),
    ],
    related=[
        ("us-incorporation.html", "Service", "US Incorporation (Overview)"),
        ("global-taxation.html", "Service", "Global Taxation Advisory"),
        ("international-expansion.html", "Service", "International Expansion"),
    ],
    cta_headline="LatAm founder looking at the US?",
    cta_body="20 minutes on WhatsApp (Spanish, Portuguese or English) and we tell you whether Delaware C-Corp or Wyoming LLC fits, what your home-country reporting looks like, and what the total year-1 cost is going to be. No commitment.",
))

# -------- Brazil --------
write_page("us-incorporation-for-brazilian-founders", build_page(
    slug="us-incorporation-for-brazilian-founders",
    title="US Incorporation for Brazilian Founders | Delaware C-Corp - BQP",
    description="Delaware C-Corp or Wyoming LLC for Brazilian founders: no US-Brazil tax treaty, CBE declaration to BCB, DEEE, Receita Federal reporting, CFC lucros no exterior. CA-led mandate.",
    keywords="US incorporation Brazilian founders, Delaware C-Corp Brazil, Wyoming LLC from Brazil, CBE declaration BCB, DEEE Brazil, incorporacao Delaware do Brasil, LLC Estados Unidos brasileiro, Receita Federal lucros exterior",
    hero_kicker="US INCORPORATION · BRAZIL",
    hero_title_html="US Incorporation for <em>Brazilian founders.</em>",
    hero_lead="Delaware C-Corp or Wyoming LLC from Brazil. The missing US-Brazil tax treaty, CBE to BCB when outbound capital exceeds the threshold, DEEE registration, Receita Federal reporting, and the lucros no exterior CFC regime - all handled.",
    sections=[
        ("Overview", "Why Brazilian founders incorporate in the US",
         "<p>The three most common drivers for Brazilian startups and SaaS firms to form a US entity are: (i) accepting Stripe or similar US payment rails that are not available or are limited in Brazil; (ii) closing US enterprise customers who prefer contracting with a US entity for legal and payment-rail reasons; (iii) raising from US venture capital funds that require a Delaware C-Corp portfolio structure. The underlying service rendered from Brazil (dev work, SaaS platform operation, consulting) stays in Brazil - the US entity exists to receive revenue and raise capital.</p>"
         "<p>Brazilian corporate tax (34% combined IRPJ + CSLL) is materially higher than US federal corporate tax (21%). But the mechanical savings from the rate difference are usually overwhelmed by the Brazilian lucros no exterior CFC regime, which generally captures the US entity's profits in the Brazilian parent's taxable income unless specific conditions are met. The decision is rarely a pure tax arbitrage.</p>"),
        ("Brazilian-side considerations", "What makes Brazil distinctive",
         "<p><strong>No comprehensive US-Brazil tax treaty.</strong> Unlike Mexico, Chile, or many European countries, Brazil has no bilateral income tax treaty with the US. Consequence: no treaty-reduced withholding on US dividends/royalties/interest paid to Brazilian shareholders. Brazilian-side taxation of US income is governed entirely by Brazilian domestic rules.</p>"
         "<p><strong>CBE (Capital Brasileiro no Exterior) declaration to BCB.</strong> Brazilian residents (individuals and companies) holding assets outside Brazil must file the CBE with the Banco Central do Brasil annually when total foreign assets exceed USD 1 million (quarterly filing if above USD 100 million). Capital contribution to a Delaware C-Corp counts.</p>"
         "<p><strong>DEEE (Declaracao Economico-Financeira do Capital Estrangeiro) and BACEN.</strong> Direct outbound investment by Brazilian companies requires BACEN registration (Modulo RDE-IED for inbound, equivalent framework for outbound).</p>"
         "<p><strong>Receita Federal reporting.</strong> Brazilian individuals: DIRPF Schedule of Assets Abroad declares the US entity holding. Brazilian companies: ECF reports foreign subsidiary. Form of filing changes depending on individual vs company founder.</p>"
         "<p><strong>Lucros no exterior CFC regime (Lei 12.973/2014).</strong> For Brazilian legal entities with foreign subsidiaries, the subsidiary's profits are generally included in the Brazilian parent's taxable income at year-end on an accrual basis, regardless of actual repatriation. Narrow carve-outs apply (active business income from treaty-country subsidiaries - but no US treaty).</p>"),
        ("Delaware C-Corp vs Wyoming LLC for Brazilians", "Picking the right vehicle",
         "<p><strong>Delaware C-Corp:</strong> Required if raising US venture capital. Standard founder-stock structure, 83(b) election, 4-year vesting. Annual franchise tax USD 400+, Form 1120 federal, Form 5472 reporting on foreign related parties. For Brazilian founders without near-term US VC plans, the ongoing compliance cost is substantial.</p>"
         "<p><strong>Wyoming LLC:</strong> Materially cheaper to run (USD 60 state fee, USD 50-150 registered agent). Single-member LLC owned by a Brazilian individual is a disregarded entity for US tax - no Form 1120 - but Form 5472 with pro-forma 1120 is still required (USD 25,000 penalty if missed). Good default for Brazilian solo founders doing SaaS, e-commerce, consulting with US customers.</p>"
         "<p><strong>Our usual recommendation:</strong> Wyoming LLC for the first 12-24 months of a Brazilian startup's US presence; convert to Delaware C-Corp (F-reorganisation) when a priced US venture round becomes concrete. This defers Delaware franchise tax and Form 1120 preparation cost until there is capital to pay for it.</p>"),
        ("Timeline from Brazil", "Typical workflow",
         "<p><strong>Weeks 1-2:</strong> Entity selection, Delaware/Wyoming filing with state, Operating Agreement or Bylaws drafting, Registered Agent appointment.</p>"
         "<p><strong>Weeks 2-4:</strong> EIN application via Form SS-4 fax to IRS International (+1-855-215-1627). Brazilian founder provides passport, CPF, Brazilian address, and the Delaware/Wyoming formation document.</p>"
         "<p><strong>Weeks 4-6:</strong> Mercury or Brex bank account application. Brazilian passport, EIN letter, formation documents, business description. Approval usually within 1-3 weeks after EIN is received.</p>"
         "<p><strong>Weeks 6-8:</strong> Stripe account activation if US-customer facing. Operational launch.</p>"
         "<p><strong>Weeks 6-10:</strong> Brazilian-side reporting - CBE assessment (file in year-end window if threshold exceeded), DIRPF schedule, DEEE/BACEN as applicable.</p>"
         "<p>Total time to operational US entity with bank account: 6-8 weeks from kickoff. Brazilian-side ongoing filings continue annually thereafter.</p>"),
    ],
    faqs=[
        ("Do I need a Brazilian lawyer in addition to BQP?",
         "For US-side formation and US compliance, no - BQP handles end to end. For Brazilian-side regulatory filings (CBE, DEEE, BACEN registration, Brazilian income tax positions on the US entity's results), we recommend a Brazilian tax advisor or contabilista working alongside. We coordinate the two sides."),
        ("Does the lucros no exterior regime capture my Wyoming LLC's income automatically?",
         "If you are a Brazilian individual holding the LLC personally, the LLC is tax-transparent for US purposes (disregarded entity), so you report the LLC's income on your Brazilian DIRPF as if directly earned. If you are a Brazilian company holding the LLC, the lucros no exterior regime applies and the LLC's profits are included in the Brazilian parent's taxable income at year-end. Entity holder matters materially."),
        ("Is there any Brazil-US tax treaty I can rely on?",
         "No comprehensive income-tax treaty. There is a Social Security Totalization Agreement and various non-income-tax arrangements, but for income tax (withholding on dividends/royalties/interest/capital gains), Brazilian domestic rules apply end to end. US withholding on payments to Brazilian recipients is the US domestic default rate (30% on many categories), with no treaty reduction available."),
        ("Can I pay myself a salary from the US LLC without triggering Brazilian tax?",
         "No. As a Brazilian tax resident, your worldwide income is taxable in Brazil regardless of where it is paid. Salary from the US LLC is Brazilian taxable income, reported on DIRPF. The US side may also require withholding depending on characterisation. Discuss with us before setting up personal compensation flows."),
        ("What is the typical total year-1 cost for a Brazilian founder?",
         "For Wyoming LLC: approximately USD 1,500-2,500 covering formation, EIN, bank account setup, Form 5472 + pro-forma 1120 preparation, Delaware franchise tax (if DE) or Wyoming filing fees, plus Brazilian-side CBE and DIRPF filings via a local partner. For Delaware C-Corp: USD 2,500-4,500 including Form 1120. Figures are indicative; concrete quote on scoping call."),
        ("Do you have Portuguese-speaking resources?",
         "Yes. See /pt/incorporacao-delaware-fundadores-brasileiros.html for a Portuguese guide and /pt/incorporacao-wyoming-llc.html for Wyoming LLC in Portuguese. Working sessions available in Portuguese on request. Formal US filings remain in English."),
    ],
    related=[
        ("us-incorporation.html", "Service", "US Incorporation (Overview)"),
        ("latin-america.html", "Hub", "Latin America Regional Desk"),
        ("how-to-get-ein-as-foreign-founder.html", "Guide", "How to Get an EIN as a Foreign Founder"),
    ],
    cta_headline="Brazilian founder considering a US entity?",
    cta_body="The missing tax treaty makes some common approaches that work for Mexican or Chilean founders inefficient for Brazilians. 20 minutes and we scope the right structure for your business - Wyoming LLC, Delaware C-Corp, or a holding setup - including the Brazilian-side reporting footprint.",
))

# -------- Mexico --------
write_page("us-incorporation-for-mexican-founders", build_page(
    slug="us-incorporation-for-mexican-founders",
    title="US Incorporation for Mexican Founders | Delaware & LLC - BQP",
    description="Delaware C-Corp or Wyoming LLC for Mexican founders: US-Mexico tax treaty (10% dividend WHT), REFIPRES CFC rules, SAT reporting, UBO filing. CA-led mandate.",
    keywords="US incorporation Mexican founders, Delaware C-Corp Mexico, Wyoming LLC from Mexico, US Mexico tax treaty, REFIPRES Mexico, SAT reporting foreign, incorporacion Delaware desde Mexico, LLC EEUU mexicano",
    hero_kicker="US INCORPORATION · MEXICO",
    hero_title_html="US Incorporation for <em>Mexican founders.</em>",
    hero_lead="Delaware C-Corp or Wyoming LLC from Mexico, under the US-Mexico tax treaty (10% dividend WHT, 15% interest, 10% royalties). REFIPRES CFC analysis, SAT foreign-asset reporting, UBO filing - all addressed in one mandate.",
    sections=[
        ("Overview", "Why Mexican founders use US entities",
         "<p>For Mexican SaaS, fintech, e-commerce and manufacturing-adjacent companies, a US entity is often the practical gateway to US customers who want to pay a US entity, to Stripe/payment infrastructure, and to US venture capital. Mexico's own tax regime (ISR corporate rate 30%) is close enough to the US rate (21% federal) that pure tax arbitrage is rarely the driver. The driver is operational and commercial.</p>"
         "<p>Mexico's position is distinctive because of the US-Mexico tax treaty: a long-standing bilateral treaty that reduces US withholding on cross-border flows and makes several structuring strategies cleaner than they are for Brazilian or Argentine founders without comparable treaty coverage.</p>"),
        ("US-Mexico tax treaty", "The reduced rates and what they apply to",
         "<p>The US-Mexico Convention for the Avoidance of Double Taxation (originally 1992, protocols 2002) caps US withholding on key cross-border flows:</p>"
         "<ul>"
         "<li><strong>Dividends:</strong> 10% treaty cap (vs 30% US domestic default) for shareholders owning less than 10% of the US company; further reduced to 5% for 10%+ corporate shareholders meeting LOB conditions</li>"
         "<li><strong>Interest:</strong> 15% treaty cap, reduced to 10% for bank-sourced interest</li>"
         "<li><strong>Royalties:</strong> 10% treaty cap (vs 30% US default)</li>"
         "<li><strong>Business profits:</strong> Article 7 - Mexican resident has no US tax on business profits unless attributable to a US permanent establishment</li>"
         "<li><strong>Capital gains:</strong> Article 13 - most capital gains taxable in residence country only (Mexico), with narrow carve-outs for US real estate (FIRPFA) and substantial-US-ownership positions</li>"
         "</ul>"
         "<p>To claim treaty benefits, provide Form W-8BEN (individual) or W-8BEN-E (entity) to the US payer, with the appropriate article invoked and a Mexican Certificate of Fiscal Residence from the SAT.</p>"),
        ("Mexican-side considerations", "REFIPRES, SAT, UBO",
         "<p><strong>REFIPRES (Regimen Fiscal Preferente / low-tax regime).</strong> Mexican CFC rules in LISR Articles 176-178 attribute foreign subsidiary income to Mexican parent if the foreign entity is in a jurisdiction with effective tax rate below 75% of the Mexican rate. US federal 21% is approximately 93% of Mexican 30% - so US entities are generally outside the REFIPRES ambit on this metric alone. But state-tax variation and specific income characterisations can shift the analysis.</p>"
         "<p><strong>SAT reporting.</strong> Mexican residents must report foreign holdings on the annual Declaracion Anual (ISR) and specific filings including Declaracion Informativa Multiple on operations with related parties. Mexican entities with US subsidiaries file transfer pricing documentation locally.</p>"
         "<p><strong>UBO (Beneficiario Controlador) reporting.</strong> From 2022, Mexican entities must identify and report ultimate beneficial owners to the SAT. The UBO file is kept at the Mexican entity, available for inspection on SAT request. Fines for non-compliance range from MXN 500,000 to 2,000,000 per unreported beneficial owner.</p>"
         "<p><strong>Transfer pricing between Mexican parent and US subsidiary.</strong> Required where intercompany transactions exist (services, royalties, cost-sharing, financing). Mexican documentation requirements include a Local File and (for larger groups) Country-by-Country Report.</p>"),
        ("Workflow and timeline", "From Mexico to operational US entity",
         "<p><strong>Weeks 1-2:</strong> Entity selection (Delaware C-Corp vs Wyoming LLC), state filing, Operating Agreement/Bylaws, Registered Agent appointment.</p>"
         "<p><strong>Weeks 2-4:</strong> EIN via Form SS-4 fax (+1-855-215-1627). Mexican passport, RFC, Mexican address, formation document.</p>"
         "<p><strong>Weeks 4-6:</strong> Mercury or Brex banking. Mexican RFC verification, passport, EIN, formation docs. 1-3 weeks for approval.</p>"
         "<p><strong>Weeks 4-8:</strong> SAT-side preparation - Certificate of Fiscal Residence request for treaty-rate claims, UBO file setup if the Mexican parent is a company, transfer pricing scoping if intercompany transactions planned.</p>"
         "<p><strong>Ongoing annual:</strong> US side - Form 1120 (C-Corp) or Form 5472 + pro-forma 1120 (foreign-owned disregarded LLC), Delaware franchise tax, BOIR. Mexican side - Declaracion Anual, Declaracion Informativa Multiple, UBO maintenance, transfer pricing documentation.</p>"),
    ],
    faqs=[
        ("Can I claim the 10% dividend withholding rate under the treaty?",
         "Yes, with Form W-8BEN (individual) or W-8BEN-E (entity) provided to the US payer plus a Mexican SAT Certificate of Fiscal Residence. For the 5% rate (10%+ corporate shareholder), additional LOB conditions apply - documentation of the Mexican entity's substance and business purpose."),
        ("Does REFIPRES catch my Delaware C-Corp?",
         "Generally no - the US federal 21% effective rate is above the REFIPRES threshold (75% of Mexican 30% = 22.5%). But if US state taxes effectively lower the combined rate below the threshold, or if specific income is subject to a reduced US rate, individual facts matter. Review required for borderline cases."),
        ("What about Mexico's UBO rules - how does that affect my US entity?",
         "The UBO rule applies to the Mexican legal entity (if any), not the US entity directly. If you hold the US entity through a Mexican SA de CV or S de RL de CV, your UBO file at the Mexican entity level reports the ultimate individuals. If you hold the US LLC personally as a Mexican individual, UBO doesn't apply (no Mexican legal entity in the chain)."),
        ("Can I claim Mexican foreign tax credit for US tax paid?",
         "Yes, under LISR Article 5. Credit for actual US tax paid, limited to Mexican tax that would have applied to the same income. File supporting documentation (Form 1099, 1120, tax receipts). Credit cannot exceed Mexican tax on worldwide income times the ratio of foreign-source to total income."),
        ("What is the total year-1 cost for a Mexican founder?",
         "Wyoming LLC: approximately USD 1,500-2,500 for US-side formation, EIN, banking, Form 5472 preparation, plus Mexican-side SAT filings via local tax advisor. Delaware C-Corp: USD 2,500-4,500 including Form 1120. Transfer pricing documentation adds USD 1,500-5,000 if required."),
        ("Do you have Spanish resources?",
         "Yes - see /es/incorporacion-delaware-fundadores-latinoamericanos.html for a Spanish-language guide, /es/incorporacion-wyoming-llc.html for Wyoming LLC in Spanish, /es/ein-sin-ssn.html for EIN process. Working sessions in Spanish available on request."),
    ],
    related=[
        ("us-incorporation.html", "Service", "US Incorporation (Overview)"),
        ("latin-america.html", "Hub", "Latin America Regional Desk"),
        ("how-to-get-ein-as-foreign-founder.html", "Guide", "How to Get an EIN as a Foreign Founder"),
    ],
    cta_headline="Mexican founder planning a US entity?",
    cta_body="The US-Mexico treaty is one of the cleanest in Latin America and your structuring options are broader than for most LatAm peers. 20 minutes and we design the right vehicle (LLC vs C-Corp) and SAT-side footprint for your business.",
))

# -------- Argentina --------
write_page("us-incorporation-for-argentine-founders", build_page(
    slug="us-incorporation-for-argentine-founders",
    title="US Incorporation for Argentine Founders | Delaware & LLC - BQP",
    description="Delaware C-Corp or Wyoming LLC for Argentine founders: capital controls (CEPO) awareness, narrow 1981 US-Argentina treaty, Bienes Personales planning, AFIP reporting, Transparencia Fiscal CFC rules.",
    keywords="US incorporation Argentine founders, Delaware C-Corp Argentina, Wyoming LLC from Argentina, CEPO Argentina, Bienes Personales US entity, incorporacion Delaware desde Argentina, LLC Estados Unidos argentino, AFIP outbound reporting",
    hero_kicker="US INCORPORATION · ARGENTINA",
    hero_title_html="US Incorporation for <em>Argentine founders.</em>",
    hero_lead="Delaware C-Corp or Wyoming LLC from Argentina. Capital controls (CEPO)-aware structuring, narrow 1981 US-Argentina treaty considerations, Bienes Personales positioning, Transparencia Fiscal CFC analysis, AFIP reporting. CA-led mandate.",
    sections=[
        ("Overview", "The Argentine founder's challenge",
         "<p>Argentine founders face a tighter regulatory and operational environment than peers in Mexico or Chile when forming US entities. The country's capital controls (collectively the CEPO) constrain how pesos can be converted to US dollars and remitted abroad; the Bienes Personales regime taxes personal foreign assets annually at escalating rates; and the US-Argentina relationship lacks a comprehensive income tax treaty, so US-source income flows face the full 30% US domestic withholding on dividends/royalties/interest without treaty reduction.</p>"
         "<p>Despite these frictions, Argentine founders routinely form US entities - the operational need (US customer contracting, Stripe acceptance, VC fundraise) is strong enough that the regulatory burden is accepted. The structuring question is how to do it compliantly with AFIP and BCRA while minimising the Bienes Personales footprint.</p>"),
        ("Argentine-side considerations", "CEPO, Bienes Personales, Transparencia Fiscal, AFIP",
         "<p><strong>CEPO (capital controls).</strong> The BCRA regime restricts outbound FX. Direct ongoing capital contribution to a Delaware entity in dollars from Argentina is operationally difficult; many Argentine founders fund the US entity through alternative routes (converted earnings held outside Argentina, Argentine clients paying the US entity directly for services, prior-period dollar holdings). Each path has its own BCRA and AFIP implications.</p>"
         "<p><strong>Bienes Personales.</strong> Argentine individuals are taxed annually on worldwide personal assets. Rates escalate to 2.25% for high-value foreign assets. Shareholding in a US entity is a Bienes Personales asset. Planning: hold through a controlled vehicle only where it generates a net benefit; evaluate the Bienes Personales cost against the shareholding's commercial value.</p>"
         "<p><strong>Transparencia Fiscal Internacional (Argentine CFC).</strong> Argentine Income Tax Law Article 125 et seq. attributes foreign entity income to Argentine resident shareholders where the foreign entity derives primarily passive income or is in a low-tax jurisdiction. US entities with active operating income generally fall outside; US holding structures with passive income generally fall inside.</p>"
         "<p><strong>Narrow 1981 US-Argentina treaty.</strong> A bilateral tax treaty exists from 1981 but is not comprehensive and does not deliver the general withholding reductions seen in US-Mexico or US-Chile treaties. For most purposes, the Argentine founder faces US domestic withholding rates without meaningful treaty reduction. A new treaty has been under discussion for years without being signed - do not plan on it.</p>"
         "<p><strong>AFIP reporting.</strong> Argentine residents must report foreign holdings via the Declaracion Jurada de Ganancias and foreign-asset informative filings. Non-reporting is actively enforced.</p>"),
        ("Delaware C-Corp vs Wyoming LLC for Argentines", "Picking the vehicle given CEPO",
         "<p><strong>Wyoming LLC:</strong> Our usual starting recommendation for Argentine founders. Low ongoing cost (USD 60/yr state fee), simple structure, Form 5472 + pro-forma 1120 the main annual US filing. If the LLC earns primarily US business profits (not passive), the Transparencia Fiscal regime generally does not pull them into Argentine attribution. CEPO exposure is lower because capital contribution needs are smaller.</p>"
         "<p><strong>Delaware C-Corp:</strong> Required for US VC fundraise. Higher ongoing cost (Delaware franchise tax + Form 1120). US VC pricing - and funding - is strong enough for well-positioned Argentine startups (Mercado Libre, Globant, Tiendanube pedigree) that this cost is justified when the fundraise path is credible.</p>"
         "<p><strong>Holding through an Argentine SA or SRL:</strong> Rarely useful. The Argentine entity in the chain triggers transfer pricing documentation, local corporate tax on attributed income, and does not improve Bienes Personales footprint. Direct personal shareholding by the Argentine founder is usually cleaner.</p>"),
        ("Timeline and workflow from Argentina", "Practical sequence",
         "<p><strong>Weeks 1-3:</strong> Entity formation (Delaware or Wyoming), EIN application. Timing is slightly longer than for Mexican/Chilean founders because document notarisation (apostille) from Argentina adds steps.</p>"
         "<p><strong>Weeks 3-6:</strong> Mercury or Brex banking. Argentine passport + CDI + formation docs + EIN. Argentine founders have slightly higher friction at Mercury underwriting (CEPO-related perception) but approvals have been consistent since 2023 for clean documentation.</p>"
         "<p><strong>Weeks 4-8:</strong> AFIP-side setup - Declaracion Jurada updated, Bienes Personales positioning if year-end approaching, Transparencia Fiscal analysis documented.</p>"
         "<p><strong>Ongoing:</strong> Annual AFIP filings (Ganancias, Bienes Personales), US filings (Form 1120 or Form 5472 + pro-forma 1120, Delaware franchise, BOIR). We coordinate with an Argentine contador on the AFIP side.</p>"),
    ],
    faqs=[
        ("How do I fund the US LLC without breaking CEPO?",
         "Depends on your specific sources. Common compliant paths: (i) US customers paying the US entity directly (no outbound capital movement from Argentina), (ii) dollar holdings held outside Argentina pre-CEPO used to fund the entity, (iii) nominal capital contribution (USD 500-1,000) only. Discuss specific sources with us and an Argentine lawyer before any dollar movement."),
        ("Does my US LLC trigger Bienes Personales?",
         "Yes - your shareholding in the US LLC is a Bienes Personales asset, included at valuation in your annual Argentine wealth tax base. Rates escalate; current foreign-asset top rate approximately 2.25%. Plan the structure (direct vs through entity) with Bienes Personales cost in view - usually direct personal shareholding is optimal."),
        ("Is the 1981 US-Argentina treaty useful?",
         "Limited. It is a narrower treaty than most, and does not provide the broad withholding reductions on dividends/royalties/interest seen in modern bilateral tax treaties. For most practical structuring, assume US domestic withholding rates apply with no treaty reduction."),
        ("Can I avoid Transparencia Fiscal attribution of my US LLC income?",
         "Generally yes if the LLC conducts active US business operations (SaaS, consulting, e-commerce) and does not derive primarily passive income. Document the active-business characterisation contemporaneously. Passive holding structures are more likely to be attributed."),
        ("Does Mercury or Brex accept Argentine founders?",
         "Yes, both do. Mercury has been consistent with Argentine passport-holders since 2023. Expect slightly more documentation requests (source of initial capital, business explanation) than for US-passport founders, which is standard underwriting."),
        ("Do you work with an Argentine lawyer?",
         "We handle US-side formation and ongoing US compliance end to end. For AFIP, BCRA, Bienes Personales positioning, and any CEPO-adjacent capital movement questions, we coordinate with a Buenos Aires-based contador or tax lawyer. This keeps the local-law risk with locally-licensed counsel."),
    ],
    related=[
        ("us-incorporation.html", "Service", "US Incorporation (Overview)"),
        ("latin-america.html", "Hub", "Latin America Regional Desk"),
        ("how-to-get-ein-as-foreign-founder.html", "Guide", "How to Get an EIN as a Foreign Founder"),
    ],
    cta_headline="Argentine founder navigating the CEPO?",
    cta_body="Structuring a US entity from Argentina is a different exercise than from Mexico or Chile - capital controls, Bienes Personales, and the narrow treaty all shape the right answer. 20 minutes and we work through the CEPO-compatible funding routes and the Bienes Personales-aware holding structure for your business.",
))

# -------- Chile --------
write_page("us-incorporation-for-chilean-founders", build_page(
    slug="us-incorporation-for-chilean-founders",
    title="US Incorporation for Chilean Founders | Delaware & LLC - BQP",
    description="Delaware C-Corp or Wyoming LLC for Chilean founders under the new 2024 US-Chile tax treaty (15% dividend WHT, 10% interest). SII DJ 1929 reporting, DL 824 Form 50, Normas de Rentas Pasivas CFC.",
    keywords="US incorporation Chilean founders, Delaware C-Corp Chile, Wyoming LLC from Chile, US Chile tax treaty 2024, SII DJ 1929, DL 824 Chile Form 50, Normas de Rentas Pasivas, incorporacion Delaware desde Chile",
    hero_kicker="US INCORPORATION · CHILE",
    hero_title_html="US Incorporation for <em>Chilean founders.</em>",
    hero_lead="Delaware C-Corp or Wyoming LLC from Chile, under the long-awaited US-Chile tax treaty that entered into force in 2024 (15% dividend WHT, 10% interest, 2-10% royalties). SII DJ 1929 reporting, DL 824 Form 50, Normas de Rentas Pasivas CFC analysis - all handled.",
    sections=[
        ("Overview", "Why 2024 changed the game for Chilean founders",
         "<p>Chile and the US signed a bilateral tax treaty in 2010; after a 13-year ratification saga, it entered into force on 1 January 2024. The treaty materially reduces US withholding on cross-border income flows between the two countries and brings Chile into alignment with Mexico among LatAm countries that have functional modern tax treaties with the US. For Chilean founders forming US entities or Chilean residents receiving US-source income, this is a significant positive change.</p>"
         "<p>Chile's own corporate tax (First Category Tax, 27%) is close to the US federal rate (21%), so most Chilean founders' decisions to form US entities are driven by operational factors (US customer contracting, Stripe, VC fundraise) rather than pure tax arbitrage. The treaty primarily affects ongoing cross-border flows (how dividends/royalties flow back from Delaware to Santiago) rather than the formation decision itself.</p>"),
        ("US-Chile tax treaty 2024", "What applies from 1 January 2024",
         "<p>The headline provisions:</p>"
         "<ul>"
         "<li><strong>Dividends:</strong> 15% treaty cap on US withholding (vs 30% US default); 5% for 10%+ corporate shareholders meeting LOB</li>"
         "<li><strong>Interest:</strong> 10% treaty cap (vs 30%); 4% for bank-sourced interest</li>"
         "<li><strong>Royalties:</strong> 2% for industrial, commercial or scientific equipment; 10% otherwise (vs 30%)</li>"
         "<li><strong>Business profits (Article 7):</strong> Chilean resident has no US tax on business profits unless attributable to a US PE</li>"
         "<li><strong>Capital gains (Article 13):</strong> Most gains taxable in residence country (Chile), except US real estate (FIRPTA) and substantial-US-ownership shares in certain cases</li>"
         "<li><strong>Limitation on Benefits (Article 24):</strong> Substance tests to prevent treaty shopping - key for holding companies</li>"
         "</ul>"
         "<p>To claim treaty rates: Form W-8BEN or W-8BEN-E to the US payer plus a Chilean SII Certificate of Residence invoking the specific article.</p>"),
        ("Chilean-side considerations", "SII, DL 824, CFC",
         "<p><strong>SII DJ 1929 (Declaracion Jurada 1929).</strong> Chilean residents with foreign-source investment income or control over foreign entities must file annual informative declarations with the SII. DJ 1929 declares foreign investments by individuals; related forms cover foreign subsidiaries held by Chilean companies.</p>"
         "<p><strong>DL 824 Form 50.</strong> Form 50 is the Chilean payment-and-withholding form used for cross-border remittances. Where a Chilean entity makes a payment to a US entity (service fees, royalties, interest), Form 50 captures the outbound and any Chilean withholding.</p>"
         "<p><strong>Normas de Rentas Pasivas (Chilean CFC).</strong> Articles 41 G and 41 H of the Chilean Income Tax Law attribute foreign entity passive income to Chilean controlling shareholders where the foreign entity is in a low-tax jurisdiction or derives principally passive income. US entities with active business income generally fall outside; US holding entities with passive portfolio income generally fall inside. The analysis is fact-specific.</p>"
         "<p><strong>Chilean integrated system vs semi-integrated.</strong> For Chilean companies holding US subsidiaries, the choice between the integrated and semi-integrated (now semi-integrated for most larger companies after the 2020 reforms) regime affects how US-source income is taxed at the Chilean level.</p>"),
        ("Workflow and timeline from Chile", "Practical sequence",
         "<p><strong>Weeks 1-2:</strong> Delaware/Wyoming entity formation, Operating Agreement/Bylaws, Registered Agent.</p>"
         "<p><strong>Weeks 2-4:</strong> EIN via Form SS-4 fax. Chilean passport, RUT, Chilean address, formation docs.</p>"
         "<p><strong>Weeks 4-6:</strong> Mercury or Brex banking. Chilean RUT, passport, EIN letter, formation documents. 1-3 weeks for approval.</p>"
         "<p><strong>Weeks 4-8:</strong> Chilean-side setup - SII Certificate of Residence request if treaty-rate claims expected in near term, DJ 1929 filing coordination for the following tax year.</p>"
         "<p><strong>Ongoing annual:</strong> US side - Form 1120 (C-Corp) or Form 5472 + pro-forma 1120 (foreign-owned disregarded LLC), Delaware franchise, BOIR. Chilean side - DJ 1929 by 30 June, Form 22 Operacion Renta, Normas de Rentas Pasivas analysis documented.</p>"),
    ],
    faqs=[
        ("Can I use the new US-Chile treaty from day one?",
         "The treaty is in force from 1 January 2024. For dividends/interest/royalties paid on or after that date to a Chilean resident, treaty rates apply - provided the W-8BEN/BEN-E is correctly filed with the US payer and SII certificate of residence is in hand. Prior-period flows do not benefit retroactively."),
        ("Does the LOB clause affect my Chilean operating company?",
         "The Limitation on Benefits article in the US-Chile treaty requires substance and non-shell character for the Chilean treaty-claimant. An operating Chilean company (SpA or SA with Chilean business, staff, operations) comfortably passes. A pure Chilean holding company set up only to receive US dividends needs more careful substance documentation. Discuss on scoping."),
        ("Will Normas de Rentas Pasivas attribute my Wyoming LLC's income to me?",
         "If the LLC's income is active US business profits (SaaS, services, e-commerce), the active-business carve-out in Article 41 G generally applies and attribution is avoided. Passive portfolio income or passive holding structures are more likely to be attributed to the Chilean shareholder. Document the active-business facts contemporaneously."),
        ("Chilean integrated vs semi-integrated - which fits me?",
         "The 2020 Chilean tax reform largely moved mid-to-large companies to the semi-integrated system (Partially Integrated Regime, PIR). For an individual Chilean founder forming a Wyoming LLC personally, the question doesn't arise at the LLC level. If you hold the US LLC through a Chilean SpA or SA, the Chilean entity's regime determines how US dividends are taxed on receipt and distribution to shareholders."),
        ("Does Chile require Form 50 for every US payment?",
         "Form 50 is required where a Chilean withholding agent (payer) makes certain outbound payments. If your Chilean entity pays the US entity for services, royalties, or interest, Form 50 captures the transaction and applicable withholding (potentially treaty-reduced). Not relevant where the US entity receives payment from US customers directly without a Chilean payer intermediary."),
        ("What is the total year-1 cost for a Chilean founder?",
         "Wyoming LLC: approximately USD 1,500-2,500 for US-side formation, EIN, banking, Form 5472, plus Chilean-side DJ 1929 filing via local tax advisor. Delaware C-Corp: USD 2,500-4,500. Transfer pricing documentation adds USD 1,500-5,000 if intercompany transactions require it."),
    ],
    related=[
        ("us-incorporation.html", "Service", "US Incorporation (Overview)"),
        ("latin-america.html", "Hub", "Latin America Regional Desk"),
        ("how-to-get-ein-as-foreign-founder.html", "Guide", "How to Get an EIN as a Foreign Founder"),
    ],
    cta_headline="Chilean founder planning around the 2024 treaty?",
    cta_body="The new US-Chile treaty materially changes the cross-border economics - but only if the Form W-8BEN, SII Certificate of Residence, and LOB positioning are set up correctly from day one. 20 minutes and we structure the US entity and the Chilean-side filings to use the treaty from day one.",
))

print("Batch 5a complete: 5 pages written (hub + Brazil + Mexico + Argentina + Chile)")
