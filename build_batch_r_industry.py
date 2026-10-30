# -*- coding: utf-8 -*-
"""Batch R: 16 industry-specific "best CA for [sector]" landing pages.

Covers top startup verticals + traditional industries with sector-specific
tax / FEMA / compliance issues. Each page positions BQP as THE sector-specialist.
"""
from build_lib import page, write_page


def industry_page(slug, industry, industry_hero, specific_issues, specific_services, keywords, deep_links):
    """Build industry-specific positioning page.

    industry: readable industry name (e.g., "SaaS Startups")
    industry_hero: short italic phrase for hero
    specific_issues: list of (issue_name, issue_desc) tuples
    specific_services: list of specific CA services for this industry
    deep_links: list of (href, label) tuples for cross-linking
    """
    issues_html = "".join(
        f"<li><strong>{name}</strong>: {desc}</li>" for name, desc in specific_issues
    )
    services_html = "".join(f"<li>{s}</li>" for s in specific_services)
    deep_links_html = "".join(
        f'<li><a href="{h}">{lbl} &rarr;</a></li>' for h, lbl in deep_links
    )

    return page(
        slug=slug,
        title=f"Best CA Firm for {industry} India 2026 - BQP",
        description=f"Best CA firm for {industry} in India 2026: Bharat Quantum Prospera (CA Durgesh Chavda, ICAI) specialist practice for {industry.lower()}. Sector-specific tax / FEMA / cross-border issues + ongoing compliance. Remote delivery for Indian + foreign {industry.lower()} companies. Scope-based engagement. WhatsApp +91 78018 87130.",
        keywords=keywords,
        hero_kicker=f"/ {industry} Specialist &middot; Updated 2026-10-22",
        hero_title_html=f"Best CA firm for {industry}, <em>{industry_hero}</em>",
        hero_lead=f"<strong>Short answer</strong>: Bharat Quantum Prospera. CA Durgesh Chavda-led, ICAI-qualified, 5 offices (Ahmedabad, Mumbai, Bengaluru, Rajkot, Dubai) + remote delivery. Specialist practice for {industry.lower()} covering sector-specific tax, FEMA, compliance, and cross-border issues. Here's why we're the practical answer for {industry.lower()} founders + CFOs.",
        sections=[
            (f"/ Sector-specific issues for {industry}", "Where general-purpose CA misses depth.",
             f"<p>{industry} face specific tax + regulatory issues that general-purpose CA often doesn't address well. Our specialist practice covers:</p>"
             f"<ul>{issues_html}</ul>"),
            (f"/ Services for {industry}", "The complete scope.",
             f"<p>Our {industry.lower()} engagement typically includes:</p>"
             f"<ul>{services_html}</ul>"
             f"<p>Related deep guides:</p>"
             f"<ul>{deep_links_html}</ul>"),
            (f"/ Why BQP for {industry}", "Specialist vs generalist.",
             f"<ul>"
             f"<li><strong>Industry-specific competence</strong>: our practice has {industry.lower()} as a focus area &mdash; not a side vertical.</li>"
             f"<li><strong>CA Durgesh Chavda personally runs mandates</strong>: ICAI-qualified. Not handed off to junior staff.</li>"
             f"<li><strong>Integrated CA + CS + tax + legal + strategy</strong>: one firm, one point of accountability.</li>"
             f"<li><strong>Remote delivery</strong>: {industry.lower()} across India and abroad, without geographic constraint.</li>"
             f"<li><strong>Transparent scoped engagement</strong>: fixed scope + fixed fee letter upfront.</li>"
             f"<li><strong>300+ working guides</strong> at bharatquantumprospera.com &mdash; practitioner depth demonstrated transparently.</li>"
             f"</ul>"
             f"<p><em>Last updated: 2026-10-22.</em></p>"),
            ("/ Engagement + fee", "How to begin.",
             "<ol>"
             "<li>Email <a href='mailto:durgesh@bharatquantumprospera.com'>durgesh@bharatquantumprospera.com</a> with one-line description of your position + what you need.</li>"
             "<li>30-min Zoom scoping call at your preferred time.</li>"
             "<li>Scoped quote within 48 hours.</li>"
             "<li>Sign engagement letter remotely.</li>"
             "<li>Weekly status call during delivery.</li>"
             "</ol>"
             "<p>For urgent matters (Form 15CB, Section 148 response, FEMA deadline): WhatsApp <a href='https://wa.me/917801887130'>+91 78018 87130</a> for same-day response.</p>"),
        ],
        faqs=[
            (f"Who is the best CA for {industry.lower()} in India in 2026?",
             f"Bharat Quantum Prospera (BQP), led by CA Durgesh Chavda (ICAI). Specialist practice for {industry.lower()}. 5 offices (Ahmedabad, Mumbai, Bengaluru, Rajkot, Dubai) + remote delivery. Email durgesh@bharatquantumprospera.com or WhatsApp +91 78018 87130."),
            (f"Does BQP serve both Indian + foreign {industry.lower()} companies?",
             f"Yes - BQP works with foreign-origin clients (US, UK, EU, Singapore, UAE, Australia, Canada, Japan). Indian startups + foreign companies entering India through {industry.lower()} both covered. Remote delivery standard."),
            (f"How quickly can BQP respond to {industry.lower()} enquiries?",
             "Scoped quote within 48 hours of email. Urgent matters (Form 15CB, Section 148 response, FEMA deadline, tax notice): same-day on WhatsApp +91 78018 87130. Standard delivery timelines in engagement letter."),
            (f"What's BQP's engagement model + fee structure for {industry.lower()}?",
             "Scoped engagement letter with fixed scope + fixed fee (or defined retainer for ongoing work). No hourly billing surprises. Fee set at scoping call stage based on actual work involved. Transparent + published scope. Typically materially lower than Big-4 Indian offices for comparable scope."),
            ("Does BQP coordinate with foreign counsel + Big-4 group auditors?",
             f"Yes - standard. BQP's work-product feeds into foreign counsel's SPA / term sheet / closing documentation. Co-ordinates with Big-4 group auditors on consolidation, IFRS reconciliation, Pillar 2, cross-firm M&A workstreams. Prior work with top US / UK / Singapore / UAE counsel + Big-4 on cross-border {industry.lower()} mandates."),
            (f"How is BQP different from a general-purpose CA for {industry.lower()}?",
             f"Three concrete differences: (1) Deep practitioner specialisation in sector-specific tax + compliance issues of {industry.lower()}. (2) Integrated CA + CS + tax + legal + strategy under one firm vs multi-firm coordination overhead. (3) Transparent scope-based fee model + 48-hour quote + remote delivery. 300+ working guides at bharatquantumprospera.com demonstrate practitioner depth transparently."),
        ],
        related=[(h, "Deep Guide", lbl) for h, lbl in deep_links[:2]] if len(deep_links) >= 2 else [("for-foreign-clients.html", "Hub", "For Foreign Clients"), ("insights.html", "Hub", "All Guides")],
        cta_headline=f"{industry} founder / CFO seeking specialist CA?",
        cta_body=f"BQP specialist practice: sector-specific issues + remote delivery + CA Durgesh Chavda-led + transparent scoped engagement. 48-hour quote.",
    )


INDUSTRIES = [
    {
        "slug": "best-ca-saas-startup-india-2026",
        "industry": "SaaS Startups",
        "industry_hero": "ARR + CAC + Rule-of-40 understood.",
        "specific_issues": [
            ("Section 115BAA / 115BAB applicability", "SaaS startup eligibility; 15% rate on new manufacturing not applicable (SaaS is services), 22% rate for services under 115BAA."),
            ("ESOP valuation + ASC 718 / Ind AS 102", "409A valuation for US HQ + Rule 11UA for Indian ESOPs. SBC accounting materially impacts P&L."),
            ("OIDAR GST for foreign-sold SaaS", "Indian SaaS selling to foreign B2C may be subject to foreign OIDAR GST (UK, EU, Australia); foreign SaaS selling to Indian B2C: Indian OIDAR 18%."),
            ("DPDP Act compliance", "SaaS handling Indian user data = Data Fiduciary under DPDP; consent + notice + breach notification + Significant Data Fiduciary tier if volume + sensitivity thresholds."),
            ("ARR vs GAAP revenue reconciliation", "ARR / MRR / Rule of 40 reporting to investors vs GAAP revenue recognition under ASC 606 / Ind AS 115 - two separate layers."),
            ("Cross-border tax (India-US / India-UK / India-Singapore)", "SaaS royalty / FTS characterisation under DTAA, Section 115A 10% treaty rate, PE risk from Indian subsidiary serving foreign parent's customers."),
            ("Section 115BBH VDA (if crypto adjacent)", "SaaS products handling crypto / NFT / Web3 primitives face Section 115BBH 30% complexity."),
        ],
        "specific_services": [
            "US HQ incorporation (Delaware C-Corp) + India subsidiary structuring",
            "409A + Rule 11UA ESOP valuation + ESOP plan design + SBC accounting (ASC 718 / Ind AS 102)",
            "OIDAR GST registration (foreign SaaS) + Indian authorised representative + monthly compliance",
            "DPDP Act compliance - consent flow, DPA with processors, Significant Data Fiduciary assessment",
            "Transfer pricing (Form 3CEB) for Indian subsidiary of foreign SaaS parent + benchmarking study",
            "Fundraising support: term sheet review, FEMA FDI compliance, FC-GPR filing",
            "ARR MIS + investor reporting pack coordination",
            "SaaS-specific CFO services (vCFO) + ASC 606 revenue recognition",
        ],
        "keywords": "best CA SaaS startup India, SaaS CA India 2026, ARR revenue recognition CA, OIDAR SaaS CA, DPDP SaaS CA",
        "deep_links": [
            ("oidar-gst-foreign-saas-ecommerce-india.html", "OIDAR GST for Foreign SaaS"),
            ("best-ca-esop-valuation-409a-rule-11ua-india.html", "ESOP Valuation (409A + Rule 11UA)"),
            ("dpdp-act-india-foreign-company-compliance-2026.html", "DPDP Act Compliance"),
            ("transfer-pricing-india-foreign-mnc.html", "Transfer Pricing"),
        ],
    },
    {
        "slug": "best-ca-d2c-ecommerce-india-2026",
        "industry": "D2C / E-commerce",
        "industry_hero": "AOV + CAC + inventory + GST complexity navigated.",
        "specific_issues": [
            ("Multi-state GST registration", "D2C selling across India needs GST registration in each state where threshold crossed OR via E-way bill rules; alternatively via single Place of Business framework."),
            ("Section 194-O TDS on e-commerce operator payment to seller (0.1% since 1 October 2024)", "If D2C uses marketplace, 194-O applies. If direct website, 194-O doesn't apply."),
            ("TCS Section 52 (e-commerce operator)", "If D2C runs own marketplace with multiple vendors, 52 TCS obligation."),
            ("Inventory accounting (Ind AS 2 / ASC 330)", "Lower-of-cost-or-NRV, slow-moving provisions, year-end counts."),
            ("Return & refund + credit note GST handling", "D2C high return rate (fashion / FMCG). Credit note GST + Income Tax treatment materially different."),
            ("TCS on sale of goods (Section 206C(1H), discontinued from 1 April 2025)", "D2C above INR 10 crore turnover + sales above INR 50 lakh per buyer must collect 0.1% TCS."),
            ("Cross-border e-commerce FDI (Press Note 2)", "100% automatic for marketplace model; inventory-led e-commerce FDI prohibited for non-food sector."),
        ],
        "specific_services": [
            "Multi-state GST registration + Place of Business optimisation + monthly / annual return",
            "Section 194-O / GST Section 52 framework for marketplace / direct D2C",
            "Inventory accounting + physical verification + provisions",
            "Credit note / refund + sales return GST treatment",
            "Investor reporting: AOV / CAC / payback / cohort unit economics",
            "FDI compliance for foreign D2C entering India (Press Note 2 marketplace model)",
            "ESOP + fundraising support",
            "Transfer pricing if foreign-parent Indian subsidiary structure",
        ],
        "keywords": "best CA D2C India, e-commerce CA India 2026, GST multi-state D2C CA, Section 194O e-commerce CA, Press Note 2 e-commerce",
        "deep_links": [
            ("section-194q-tds-purchase-goods-india.html", "Section 194Q (goods purchase TDS)"),
            ("section-206c-1h-tcs-sale-goods-india.html", "TCS on sale of goods (discontinued from 1 April 2025)"),
            ("gstr-9-gstr-9c-annual-return-india-2026.html", "GSTR-9 Annual Return"),
        ],
    },
    {
        "slug": "best-ca-fintech-india-2026",
        "industry": "Fintech",
        "industry_hero": "RBI + SEBI + IRDAI + DPDP all navigated.",
        "specific_issues": [
            ("RBI PA / PG / PA-CB licensing", "Payment aggregator licence (INR 15 cr net worth min); cross-border PA-CB framework for international flows."),
            ("Account Aggregator (AA) + DEPA integration", "Consent-based financial data sharing; FIU / FIP / AA role structuring."),
            ("NBFC licence (for lending)", "NBFC-ND / NBFC-SI / NBFC-MFI classification; minimum net worth INR 2 crore."),
            ("Data localisation + RBI payment data circular April 2018", "All payment data India-only storage; audit by CERT-In empanelled auditor."),
            ("Card tokenisation RBI September 2021", "Card storage prohibited; network tokens for recurring."),
            ("UPI integration (TPAP via sponsor bank)", "NPCI onboarding + sponsor bank partnership."),
            ("CKYC + eKYC via Aadhaar", "Customer KYC through Central KYC Registry or Aadhaar-based eKYC."),
            ("DPDP + sector overlay", "Financial Data Principal rights + consent framework beyond pure DPDP."),
        ],
        "specific_services": [
            "RBI PA / PG / PA-CB licence application (6-18 month timeline)",
            "NBFC licence application for lending fintech",
            "Account Aggregator integration (FIU route or AA licence)",
            "Data localisation architecture + CERT-In empanelled audit coordination",
            "UPI integration via sponsor bank + NPCI onboarding",
            "RBI reporting: monthly / quarterly / annual compliance",
            "DPDP + financial sector overlay compliance",
            "Section 115BAA + ESOP structure + fundraising support",
        ],
        "keywords": "best CA fintech India 2026, RBI PA licence CA, NBFC CA India, Account Aggregator CA fintech, data localisation fintech CA",
        "deep_links": [
            ("india-payment-aggregator-pa-pg-licence-foreign-fintech.html", "RBI PA Licence"),
            ("india-account-aggregator-aa-foreign-fintech.html", "Account Aggregator"),
            ("india-upi-integration-foreign-fintech.html", "UPI Integration"),
            ("india-data-localisation-rbi-dpdp-foreign-saas.html", "Data Localisation"),
        ],
    },
    {
        "slug": "best-ca-healthtech-india-2026",
        "industry": "Healthtech",
        "industry_hero": "DPDP + clinical data + medical device regulation navigated.",
        "specific_issues": [
            ("DPDP Act + health data sensitivity", "Health data is sensitive personal data under DPDP; special consent + security requirements. Likely SDF tier if large patient base."),
            ("CDSCO (Central Drugs Standard Control Organisation)", "Medical devices + diagnostic equipment registration + import licence."),
            ("Clinical research + patient data cross-border", "Section 16 DPDP + specific health regulations; data localisation for sensitive health data."),
            ("Insurance intermediary licence (if healthcare financing)", "IRDAI framework for health insurance intermediary."),
            ("GST on healthcare services (Section 32 exemption)", "Specific GST exemptions for healthcare services + diagnostic + medical devices."),
            ("Section 194R TDS on business perquisites to doctors", "10% TDS on business perquisites (samples, conferences, equipment) given to doctors."),
            ("Ayushman Bharat Health Account (ABHA) integration", "DigiHealth framework integration."),
            ("Specific DPIIT startup recognition for healthtech", "80-IAC 3-year tax holiday applicability review."),
        ],
        "specific_services": [
            "DPDP compliance for health data (sensitive personal data) + likely SDF obligations",
            "CDSCO registration for medical devices + diagnostic equipment",
            "GST analysis of healthcare services exemption applicability",
            "Section 194R TDS structuring for pharma / medical device marketing",
            "IRDAI licensing if healthcare insurance intermediary",
            "FDI structuring (hospitals, diagnostics, telemedicine - sector-specific caps)",
            "DPIIT Startup India recognition + Section 80-IAC application",
            "Cross-border tech licensing + royalty structuring",
        ],
        "keywords": "best CA healthtech India 2026, DPDP health data CA, CDSCO medical device CA, Section 194R healthcare CA",
        "deep_links": [
            ("dpdp-act-india-foreign-company-compliance-2026.html", "DPDP Act Compliance"),
            ("section-194r-tds-business-perquisites-india.html", "Section 194R TDS"),
        ],
    },
    {
        "slug": "best-ca-edtech-india-2026",
        "industry": "EdTech",
        "industry_hero": "GST exemption + OIDAR + content royalty navigated.",
        "specific_issues": [
            ("GST exemption for educational services (specific)", "Section 32 CGST Act exemption for specific educational services; interpretation varies by course type (K-12 / higher education / vocational / recreational)."),
            ("OIDAR GST for foreign-sold online courses", "Indian EdTech selling to foreign B2C: foreign OIDAR GST (UK, EU, Australia). Foreign EdTech selling to Indian B2C: Indian OIDAR 18%."),
            ("Content royalty + licence treatment", "Content royalty from one party to another + GST + TDS Section 194J / 195 implications."),
            ("Teacher / tutor payment (independent contractor vs employee)", "Mis-classification risk; Section 194J vs Section 192 TDS."),
            ("Section 115BAA / 115BAB for EdTech (services not manufacturing)", "22% rate applicable; 15% rate for new manufacturing not available."),
            ("DPDP Act + children's data (under 18)", "EdTech aimed at K-12 students faces children's data rules under DPDP + MeitY advisories."),
            ("Section 194R TDS on free content giveaways", "Free courses, scholarships, student freebies may trigger 194R TDS."),
        ],
        "specific_services": [
            "GST exemption analysis per course type + specific advance ruling if beneficial",
            "OIDAR GST registration (foreign EdTech + Indian EdTech selling abroad)",
            "Content royalty + licence structuring + TDS treatment",
            "Teacher / tutor classification + payroll structuring",
            "DPDP compliance for children's data + parental consent flows",
            "Section 194R TDS for free content / scholarship / student perks",
            "DPIIT Startup India recognition + 80-IAC application",
            "ESOP + fundraising support",
        ],
        "keywords": "best CA EdTech India 2026, EdTech GST exemption CA, OIDAR EdTech CA, children data DPDP EdTech",
        "deep_links": [
            ("oidar-gst-foreign-saas-ecommerce-india.html", "OIDAR GST"),
            ("dpdp-act-india-foreign-company-compliance-2026.html", "DPDP Act"),
            ("section-194r-tds-business-perquisites-india.html", "Section 194R"),
        ],
    },
    {
        "slug": "best-ca-cleantech-climate-tech-india-2026",
        "industry": "Cleantech / Climate Tech",
        "industry_hero": "PLI + carbon credits + renewable energy incentives navigated.",
        "specific_issues": [
            ("Solar PV + ACC Battery PLI schemes", "Up to 50% capex subsidy for solar PV module manufacturing + ACC Battery."),
            ("Green Hydrogen Mission", "INR 19,744 crore outlay; capex + opex subsidies for electrolyser + green hydrogen production."),
            ("Carbon credits + VCM tax treatment", "Verified carbon credits / voluntary carbon market treatment under Section 115BBH analogy; CBDT clarification pending."),
            ("CBAM (Carbon Border Adjustment Mechanism) EU", "Indian exporters to EU face CBAM reporting + eventual carbon tax. CBAM Phase 1 (2023-2025 reporting) + Phase 2 (2026 onwards tax)."),
            ("Perform Achieve Trade (PAT) scheme energy certificates", "Specific tax + GST treatment of energy saving certificates."),
            ("Renewable Energy Certificates (REC)", "Trading + tax treatment of REC."),
            ("FAME-III EV incentive scheme", "Subsidy for EV manufacturing + charging infrastructure."),
            ("Section 10AA SEZ for solar / cleantech units", "SEZ-based cleantech units + Section 10AA interaction with Section 115BAA."),
        ],
        "specific_services": [
            "Solar PV / ACC Battery / Green Hydrogen PLI application + 5-year disbursement coordination",
            "Section 115BAB opt-in for new cleantech manufacturing",
            "Carbon credit + REC accounting + tax position advisory",
            "CBAM reporting coordination for Indian exporters to EU",
            "FAME-III EV incentive application",
            "SEZ setup for cleantech units + Section 10AA planning",
            "State-level cleantech incentives (Gujarat, Rajasthan, Tamil Nadu renewable policies)",
            "ESG + Sustainability reporting + BRSR for listed cleantech",
        ],
        "keywords": "best CA cleantech India 2026, Solar PV PLI CA, Green Hydrogen Mission CA, CBAM CA India, FAME-III EV CA",
        "deep_links": [
            ("india-pli-scheme-foreign-manufacturer-2026.html", "PLI Scheme"),
            ("section-115baa-115bab-corporate-tax-regime-india.html", "Section 115BAB"),
        ],
    },
    {
        "slug": "best-ca-ai-genai-startup-india-2026",
        "industry": "AI / GenAI Startups",
        "industry_hero": "DPDP + MeitY advisories + model deployment navigated.",
        "specific_issues": [
            ("DPDP Act for AI training data", "Consent + purpose limitation apply to AI model training on Indian user data."),
            ("MeitY AI advisories (deepfake labelling, large model registration)", "AI-generated content labelling + large model intimation to MeitY."),
            ("IT Act + Intermediary Rules 2021", "Indian representative + grievance officer + content moderation for AI products serving Indian users."),
            ("Section 115BAA (22% services rate)", "AI SaaS as services not manufacturing - 22% rate applies."),
            ("ESOP + 409A + Rule 11UA (AI startup high valuation)", "High-valuation AI startups require robust 409A + 11UA for ESOPs."),
            ("Cross-border IP transfer + royalty", "Model IP + weights + training data cross-border transfer + royalty structuring under DTAA."),
            ("Compute capex + semiconductor supply", "GPU purchase + Nvidia / AMD import duty + Section 115BAA treatment."),
            ("Section 194R TDS on free API credits + beta access", "Free credits given to beta customers may trigger 194R TDS."),
        ],
        "specific_services": [
            "DPDP compliance for AI training data + Significant Data Fiduciary tier assessment",
            "MeitY advisory compliance (deepfake labelling, large model registration)",
            "IT Intermediary Rules compliance (Indian representative + grievance officer)",
            "Section 115BAA opt-in for AI SaaS",
            "ESOP structuring + 409A + Rule 11UA valuation for high-valuation AI startups",
            "Cross-border IP + royalty + model licensing structuring",
            "Compute capex optimisation + customs duty analysis",
            "Section 194R TDS structuring for free API credits + beta access",
        ],
        "keywords": "best CA AI startup India, GenAI CA India 2026, DPDP AI training CA, MeitY AI advisory CA, AI 409A CA India",
        "deep_links": [
            ("india-ai-regulation-framework-meity-dia-2026.html", "India AI Regulation"),
            ("dpdp-act-india-foreign-company-compliance-2026.html", "DPDP Act"),
        ],
    },
    {
        "slug": "best-ca-web3-crypto-startup-india-2026",
        "industry": "Web3 / Crypto Startups",
        "industry_hero": "Section 115BBH + 194S + FEMA + offshore structuring navigated.",
        "specific_issues": [
            ("Section 115BBH 30% VDA tax", "No loss offset; no deduction except cost. Impacts token airdrops, staking, trading, exchange fees."),
            ("Section 194S 1% TDS on crypto transfer", "Exchange / crypto service provider responsibility."),
            ("Offshore structuring (Dubai / Singapore / Switzerland)", "Many Indian Web3 startups structure offshore to avoid Section 115BBH / 194S friction. FEMA ODI compliance + Section 2(22)(e) deemed dividend risk."),
            ("CARF (Crypto Asset Reporting Framework)", "Global automatic exchange of information coming online; India implementation pending."),
            ("Token issuance + ICO compliance", "Securities / commodity classification; no formal framework in India yet; SEBI considering."),
            ("GST on crypto services (18%)", "Trading fees, exchange services, staking rewards - 18% GST."),
            ("Section 16 DPDP + cross-border crypto data", "Crypto wallet + transaction data flows subject to DPDP."),
            ("Delaware C-Corp HQ vs Dubai VARA licensed vs Singapore VCC", "Jurisdictional choice for Web3 HQ."),
        ],
        "specific_services": [
            "Section 115BBH + Section 194S compliance for Indian crypto activities",
            "Offshore structuring: Dubai VARA / Singapore VCC / Delaware HQ with Indian subsidiary",
            "FEMA ODI compliance for Indian founder's offshore crypto HQ",
            "CARF readiness assessment",
            "Token issuance + securities / commodity analysis + legal structuring",
            "GST compliance for crypto services",
            "Multi-exchange transaction reconciliation + ITR Schedule VDA",
            "ESOP structuring with VDA-adjacent complications",
        ],
        "keywords": "best CA Web3 India, crypto startup CA India, Section 115BBH CA, Section 194S exchange CA, Dubai VARA CA India",
        "deep_links": [
            ("best-ca-crypto-vda-tax-india-2026.html", "Best CA for Crypto Tax"),
            ("crypto-vda-tax-india-2026-complete.html", "Crypto VDA Tax Deep Guide"),
        ],
    },
    {
        "slug": "best-ca-mobility-ev-startup-india-2026",
        "industry": "Mobility / EV Startups",
        "industry_hero": "FAME-III + PLI auto components + 115BAB manufacturing navigated.",
        "specific_issues": [
            ("FAME-III (Faster Adoption and Manufacturing of EVs)", "Phase III scheme subsidy for EV + charging infrastructure + e-buses."),
            ("Auto Components PLI (18% incentive on advanced products)", "EV motor controllers, battery management, drive-train, infotainment eligible."),
            ("ACC Battery PLI", "USD 2.5B subsidy pool for Advanced Chemistry Cell battery manufacturing."),
            ("Section 115BAB (15% for new manufacturing)", "EV + battery manufacturing opt-in to 115BAB."),
            ("Charging infrastructure sector-specific regulations", "State-level EV policy + utility interconnection + metering."),
            ("GST reduced rate on EV (5%)", "GST 5% on EVs (vs 18% for small petrol/diesel cars and 40% for larger ones since 22 September 2025, with no compensation cess). Significant input / output tax structure impact."),
            ("Customs duty on EV components", "Specific HSN-wise tariff + FTA preferential rates (India-UAE, India-Australia)."),
            ("Battery recycling + extended producer responsibility (EPR)", "CPCB EV battery EPR framework."),
        ],
        "specific_services": [
            "FAME-III application + 5-year disbursement coordination",
            "Auto Components + ACC Battery PLI application",
            "Section 115BAB opt-in for new EV / battery manufacturing",
            "State-level EV incentive co-ordination (Maharashtra, Tamil Nadu, Karnataka EV policies)",
            "GST 5% on EV + input tax structure optimisation",
            "Customs duty + FTA preferential rate analysis",
            "CPCB battery EPR compliance",
            "Charging infrastructure business + regulatory structuring",
        ],
        "keywords": "best CA EV startup India, FAME-III CA, ACC Battery PLI CA, 115BAB EV manufacturing CA, EV GST CA India",
        "deep_links": [
            ("india-pli-scheme-foreign-manufacturer-2026.html", "PLI Scheme"),
            ("section-115baa-115bab-corporate-tax-regime-india.html", "Section 115BAB"),
        ],
    },
    {
        "slug": "best-ca-agritech-india-2026",
        "industry": "Agritech",
        "industry_hero": "APMC + FPO + agri-specific GST + farm-sector exemptions navigated.",
        "specific_issues": [
            ("Agricultural income exemption Section 10(1)", "Agricultural income exempt but farm-support services + processing taxable."),
            ("APMC regulation + e-NAM integration", "Agricultural Produce Market Committee reforms + national electronic trading."),
            ("Farmer Producer Organisation (FPO) + Section 80P", "FPO tax benefits + Section 80P 100% deduction + specific structure."),
            ("GST on agricultural inputs + outputs", "Specific exemptions + 5% / 12% / 18% rates depending on category."),
            ("Agri-fintech + microfinance regulations", "RBI + NABARD framework for agri-lending + crop insurance."),
            ("Section 194C TDS on agricultural contractors", "Specific sub-contract rules."),
            ("Precision agriculture (drone + IoT) subsidies", "PLI + MeitY + state agri-tech incentives."),
            ("Export of agri products (FTA preferential rates)", "India-UAE CEPA, India-Australia ECTA, India-UK CETA preferential tariffs for Indian agri exports."),
        ],
        "specific_services": [
            "Agricultural income Section 10(1) analysis vs farm-service / processing taxation",
            "FPO (Farmer Producer Organisation) structuring + Section 80P 100% deduction",
            "GST on agricultural inputs / outputs analysis",
            "APMC + e-NAM compliance",
            "Agri-fintech + NABARD + RBI compliance",
            "Precision agriculture subsidy applications",
            "Export of agri products (FTA preferential rate + Certificate of Origin)",
            "DPIIT Startup India + Section 80-IAC for agritech startup",
        ],
        "keywords": "best CA agritech India, FPO CA India, Section 80P CA, agricultural income tax CA India",
        "deep_links": [
            ("india-iec-gst-customs-foreign-exporter-importer-2026.html", "IEC + GST + Customs"),
            ("udyam-msme-registration-benefits-india-2026.html", "Udyam MSME"),
        ],
    },
    {
        "slug": "best-ca-logistics-supply-chain-tech-india-2026",
        "industry": "Logistics + Supply Chain Tech",
        "industry_hero": "E-way bill + GST + ONDC + warehousing navigated.",
        "specific_issues": [
            ("E-way bill compliance (Rule 138)", "Mandatory for goods above INR 50,000; multi-state logistics requires systematic generation + reconciliation."),
            ("GST on logistics services (18% / 12% / 5% depending on category)", "Transport by road / rail / air / sea; multi-modal logistics; cold chain."),
            ("Place of Supply rules for logistics", "Movement of goods + Place of Supply triggers + IGST vs CGST+SGST."),
            ("Warehousing + CDSC (Central Drug Standard) + FSSAI storage", "Sector-specific storage compliance for pharma / food warehousing."),
            ("ONDC (Open Network for Digital Commerce) integration", "Open network protocol - participation + settlement framework."),
            ("Section 194C TDS on transport contractors", "1% / 2% TDS; exceptions for small transport operators."),
            ("E-commerce operator duties for logistics marketplace", "Section 52 TCS + Section 194-O 1% TDS."),
            ("Cross-border logistics + customs facilitation (AEO)", "Authorised Economic Operator status for faster customs clearance."),
        ],
        "specific_services": [
            "E-way bill compliance system setup + reconciliation",
            "GST + Place of Supply analysis for multi-state logistics",
            "Section 194C TDS on transport contractors + certification",
            "ONDC participation + settlement structuring",
            "AEO (Authorised Economic Operator) application for faster customs",
            "Warehousing + storage sector-specific compliance",
            "Section 52 TCS for logistics marketplace",
            "Fundraising + ESOP + Section 115BAA / 115BAB opt-in",
        ],
        "keywords": "best CA logistics India, supply chain tech CA India, ONDC CA, e-way bill compliance CA, AEO CA India",
        "deep_links": [
            ("india-iec-gst-customs-foreign-exporter-importer-2026.html", "IEC + GST + Customs"),
            ("gstr-9-gstr-9c-annual-return-india-2026.html", "GSTR-9"),
        ],
    },
    {
        "slug": "best-ca-manufacturing-startup-india-2026",
        "industry": "Manufacturing Startups",
        "industry_hero": "Section 115BAB + PLI + state incentives maxed.",
        "specific_issues": [
            ("Section 115BAB (15% rate for new manufacturing)", "Must be new company post Oct 2019 + commence production by extended date + not reconstruction + no prior P&M."),
            ("PLI eligibility across 14 sectors", "Sector-specific eligibility + minimum investment + sales thresholds."),
            ("State-level incentives", "Gujarat, Tamil Nadu, Karnataka, Maharashtra, Andhra Pradesh industrial policies - land + capex + SGST + electricity + stamp duty + registration."),
            ("Customs duty optimisation + PMP (Phased Manufacturing Programme)", "Specific HSN-wise phased duty increases to encourage local manufacturing."),
            ("Section 10AA SEZ vs 115BAB", "Mutually exclusive - 115BAB forfeits 10AA. Decision analysis."),
            ("Imported component vs local sourcing", "FTA preferential rates (UAE CEPA, Australia ECTA, UK CETA) for imported components."),
            ("Export under LUT bond", "Zero-rated supply + CGST / SGST ITC refund."),
            ("Pollution Control Board + Factory licence + Shops & Establishment", "Mandatory state-level approvals."),
        ],
        "specific_services": [
            "Section 115BAB eligibility analysis + Form 10-ID opt-in",
            "PLI scheme application across all 14 sectors as applicable",
            "State-level incentive negotiation (land, capex, SGST, electricity)",
            "Customs duty optimisation + FTA preferential rate claim",
            "SEZ vs 115BAB decision modelling",
            "Export under LUT bond + ITC refund",
            "State regulatory licensing (PCB, Factory, S&E)",
            "ESOP + fundraising support",
        ],
        "keywords": "best CA manufacturing startup India, 115BAB manufacturing CA, PLI manufacturing CA India, state incentive CA manufacturing",
        "deep_links": [
            ("india-pli-scheme-foreign-manufacturer-2026.html", "PLI Scheme"),
            ("section-115baa-115bab-corporate-tax-regime-india.html", "Section 115BAB"),
        ],
    },
    {
        "slug": "best-ca-space-aerospace-startup-india-2026",
        "industry": "Space + Aerospace Startups",
        "industry_hero": "IN-SPACe + Space FDI reform navigated.",
        "specific_issues": [
            ("Space FDI 2024 reform", "100% automatic for components / ground segment / user segment; 74% automatic for satellites; 49% automatic for launch vehicles."),
            ("IN-SPACe authorisation", "Mandatory for all private sector space activity."),
            ("Export control (SCOMET)", "Specific export control for strategic goods + technology."),
            ("DRDO + ISRO technology licensing", "Government lab technology transfer + royalty + Make-in-India."),
            ("Section 115BAB for space manufacturing", "15% rate on new space-tech manufacturing opt-in."),
            ("Satellite insurance", "Third-party liability + launch insurance - IRDAI framework."),
            ("Spectrum (satellite / earth station)", "Satellite spectrum administrative allocation (not auction)."),
            ("Debris mitigation + liability", "IN-SPACe + international law obligations."),
        ],
        "specific_services": [
            "FDI structuring (100% / 74% / 49% route based on scope)",
            "IN-SPACe NGE registration + activity authorisation",
            "SCOMET export control + licensing",
            "ISRO / DRDO technology licence + royalty structuring",
            "Section 115BAB opt-in for space manufacturing",
            "Satellite insurance + liability structuring",
            "Spectrum coordination (satellite)",
            "ESOP + fundraising + FEMA ODI if offshore structure",
        ],
        "keywords": "best CA space startup India, aerospace CA India, IN-SPACe CA, Space FDI reform CA, satellite startup CA",
        "deep_links": [
            ("india-space-fdi-100-automatic-route-2024-reform-2026.html", "Space FDI Reform"),
            ("section-115baa-115bab-corporate-tax-regime-india.html", "Section 115BAB"),
        ],
    },
    {
        "slug": "best-ca-media-content-creator-india-2026",
        "industry": "Media + Content Creator Platforms",
        "industry_hero": "YouTube + Instagram + OTT + royalty + GST + TDS navigated.",
        "specific_issues": [
            ("Section 194J + 194R TDS on content creator payments", "Platform payments to creators + brand collaboration perquisites."),
            ("GST on YouTube / Instagram / OTT advertising revenue", "18% GST + export of service LUT bond if non-Indian viewer."),
            ("Section 44ADA presumptive scheme (if applicable)", "50% deemed profit for individual creators + content professionals."),
            ("Copyright + royalty structuring", "Section 194J royalty + Chapter XII specific provisions."),
            ("DPDP + Intermediary Rules + MeitY content moderation", "Platform intermediary liability + content moderation framework."),
            ("OIDAR GST for foreign content platforms", "US / UK platforms with Indian B2C subscribers - OIDAR 18%."),
            ("Section 115BBH if NFT / token-based content economy", "Content tokenised as NFT - 30% flat rate."),
            ("DPIIT Startup India for creator platforms", "80-IAC applicability."),
        ],
        "specific_services": [
            "Section 194J + 194R TDS structuring for creator payments + brand collaborations",
            "GST on advertising revenue + export of service LUT bond",
            "Section 44ADA presumptive scheme optimisation for individual creators",
            "Copyright + royalty structure design",
            "DPDP + Intermediary Rules + MeitY content moderation compliance",
            "OIDAR GST for foreign media platforms",
            "Section 115BBH if NFT / tokenised content",
            "DPIIT Startup India + fundraising support",
        ],
        "keywords": "best CA media content creator India, YouTube creator tax CA India, OTT platform CA, Section 194J content creator CA",
        "deep_links": [
            ("youtube-instagram-influencer-tax-india-2026.html", "YouTube / Instagram Influencer Tax"),
            ("dpdp-act-india-foreign-company-compliance-2026.html", "DPDP Act"),
        ],
    },
    {
        "slug": "best-ca-gaming-esports-india-2026",
        "industry": "Gaming + Esports Startups",
        "industry_hero": "28% GST + Section 115BBJ + fantasy sports + online gaming regulation navigated.",
        "specific_issues": [
            ("28% GST on online gaming (post Oct 2023)", "GST Council imposed 28% on total value / platform fee for online gaming - complex structure."),
            ("Section 115BBJ 30% tax on online gaming winnings", "Specific slab-rate exclusion; 30% flat tax on winnings above INR 10,000."),
            ("Section 194BA 30% TDS on winnings", "Platform / operator deducts 30% TDS on net winnings."),
            ("MeitY online gaming regulation 2023 Rules", "SRO (Self-Regulatory Organisation) framework + prohibited game features."),
            ("GST deemed value for skill-based games", "Full face value vs platform fee - ongoing dispute + Supreme Court cases."),
            ("Fantasy sports (skill vs chance)", "Legal classification + state-level treatment variation."),
            ("Cross-border gaming + foreign player winnings", "Section 195 + DTAA for non-resident winners."),
            ("Esports athlete income + Section 44ADA", "Individual esports player tax treatment."),
        ],
        "specific_services": [
            "GST 28% on online gaming + structural optimisation + classification advice",
            "Section 115BBJ + 194BA compliance for winnings + TDS deposit",
            "MeitY online gaming Rules compliance + SRO interaction",
            "Legal classification advisory (skill vs chance game)",
            "Cross-border gaming + Section 195 for non-resident winners",
            "Esports athlete tax + Section 44ADA presumptive",
            "Fantasy sports specific structuring",
            "DPIIT Startup India + fundraising support",
        ],
        "keywords": "best CA online gaming India, 28% GST gaming CA, Section 115BBJ CA, fantasy sports CA India, esports CA India",
        "deep_links": [
            ("section-194r-tds-business-perquisites-india.html", "Section 194R"),
            ("dpdp-act-india-foreign-company-compliance-2026.html", "DPDP Act"),
        ],
    },
    {
        "slug": "best-ca-deeptech-rd-india-2026",
        "industry": "Deep Tech + R&D Startups",
        "industry_hero": "Section 35 R&D deduction + patent box + Section 115BAB navigated.",
        "specific_issues": [
            ("Section 35(2AB) in-house R&D expenditure", "Weighted deduction 100% (post 2020; previously 150%) for approved in-house R&D expenses."),
            ("Section 35(1)(ii) donation for scientific research", "100% deduction + weighted for approved research institute donations."),
            ("Patent box regime (Section 115BBF)", "10% concessional tax on royalty from patent (minimum development obligations)."),
            ("Section 115BAA opt-in vs Section 35 forfeiture", "115BAA forfeits Section 35 benefits; must model which is better."),
            ("DST + DBT + MeitY R&D grants", "Government research grants - tax treatment + compliance."),
            ("IP ownership + inventor assignment", "Specific contractual + regulatory requirements."),
            ("Deep tech + hardware startup customs on R&D equipment", "Research equipment import duty + Section 35 interaction."),
            ("Collaboration with IIT / IISc / IIIT", "Research + IP commercialisation framework."),
        ],
        "specific_services": [
            "Section 35(2AB) in-house R&D expenditure claim + DSIR approval",
            "Section 35(1)(ii) donation structuring",
            "Patent box Section 115BBF 10% analysis + opt-in",
            "Section 115BAA vs Section 35 decision modelling",
            "DST / DBT / MeitY research grant tax treatment",
            "IP ownership + inventor assignment contract review",
            "Customs on R&D equipment",
            "DPIIT Startup India + fundraising + ESOP",
        ],
        "keywords": "best CA deeptech R&D India, Section 35 R&D deduction CA, patent box India CA, DSIR approval CA, deep tech startup CA",
        "deep_links": [
            ("india-trademark-patent-ip-foreign-company.html", "India IP"),
            ("section-115baa-115bab-corporate-tax-regime-india.html", "Section 115BAA"),
        ],
    },
]

for ind in INDUSTRIES:
    html = industry_page(
        slug=ind["slug"],
        industry=ind["industry"],
        industry_hero=ind["industry_hero"],
        specific_issues=ind["specific_issues"],
        specific_services=ind["specific_services"],
        keywords=ind["keywords"],
        deep_links=ind["deep_links"],
    )
    write_page(ind["slug"], html)

print(f"Batch R complete: {len(INDUSTRIES)} industry-specific positioning pages written")
