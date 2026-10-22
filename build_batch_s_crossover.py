# -*- coding: utf-8 -*-
"""Batch S: 20 crossover positioning + December deadline alert pages.

15 crossover pages: specific service × specialty intersection where BQP excels.
5 December deadline alerts: timely compliance pages for Nov-Dec 2026 deadlines.
"""
from build_lib import page, write_page


def crossover_page(slug, title, hero_em, lead, kicker, section_pairs, faq_pairs, deep_links_tuples, cta_h, cta_b, keywords, desc):
    """Build crossover positioning page using existing page helper."""
    return page(
        slug=slug,
        title=f"{title} - BQP",
        description=desc,
        keywords=keywords,
        hero_kicker=kicker,
        hero_title_html=f"{title.split(' | ')[0]}, <em>{hero_em}</em>",
        hero_lead=lead,
        sections=section_pairs,
        faqs=faq_pairs,
        related=deep_links_tuples[:2],
        cta_headline=cta_h,
        cta_body=cta_b,
    )


# ========= 15 CROSSOVER PAGES =========

CROSSOVERS = [
    {
        "slug": "ca-for-ai-saas-dpdp-compliance-india",
        "title": "CA for AI SaaS DPDP Compliance in India",
        "hero_em": "AI + data protection + GST integrated.",
        "desc": "CA for AI SaaS startup / foreign AI company India: integrated advisory covering DPDP Act (consent for training data), MeitY AI advisories (deepfake labelling), OIDAR GST, Section 115BAA, ESOP 409A/11UA, DPIIT Startup India. CA Durgesh Chavda specialist practice.",
        "kicker": "/ AI × DPDP × GST Specialist &middot; Updated 2026-10-22",
        "lead": "AI SaaS startup faces three overlapping compliance stacks: DPDP Act for Indian user data processing + AI model training; MeitY advisories for deepfake labelling + large model deployment; OIDAR GST if B2C paying Indian users. BQP delivers integrated advisory across all three + Section 115BAA + ESOP structuring. Here's the complete framework.",
        "section_pairs": [
            ("/ The integrated compliance stack", "Three parallel rails.",
             "<ul>"
             "<li><strong>DPDP Act 2023</strong>: AI training on Indian user data = Data Fiduciary role; consent + notice + purpose limitation + Significant Data Fiduciary tier if volume/sensitivity thresholds.</li>"
             "<li><strong>MeitY advisories</strong>: deepfake labelling, large model registration, content moderation for AI-generated output.</li>"
             "<li><strong>OIDAR GST (Section 2(17) IGST Act)</strong>: 18% IGST on B2C Indian consumer AI product subscriptions - from first rupee.</li>"
             "<li><strong>Section 115BAA</strong>: 22% corporate tax for Indian AI SaaS (services, not manufacturing - so 115BAB not applicable).</li>"
             "<li><strong>ESOP 409A + Rule 11UA</strong>: high-valuation AI startup ESOP compliance for both US entity + Indian subsidiary.</li>"
             "<li><strong>DPIIT Startup India + Section 80-IAC</strong>: 3-year 100% tax holiday if eligible.</li>"
             "</ul>"),
            ("/ Why integrated matters", "Avoiding firm-coordination gaps.",
             "<p>Many AI SaaS startups engage separate firms: privacy counsel (DPDP), CA (tax), tax law firm (GST), separate CA (ESOP). Overhead + gaps. BQP integrated engagement avoids:</p>"
             "<ul>"
             "<li>DPDP consent flow design + GST invoicing coordination for same Indian consumer transaction.</li>"
             "<li>Section 115BAA opt-in + DPIIT 80-IAC conflict (both forfeit specific deductions).</li>"
             "<li>409A valuation needs ARR / growth / cohort data that same CA has from GST / Income Tax work.</li>"
             "<li>MeitY advisory compliance + DPDP interaction on same AI training data flow.</li>"
             "</ul>"),
            ("/ Our scope for AI SaaS", "What we deliver.",
             "<ul>"
             "<li>DPDP applicability + consent flow + DPA with cloud processors + breach plan + Significant Data Fiduciary assessment.</li>"
             "<li>MeitY advisory compliance (deepfake labelling, intermediary rules, grievance officer).</li>"
             "<li>OIDAR GST registration + monthly compliance + GSTR-5A annual return.</li>"
             "<li>Section 115BAA opt-in (Form 10-IC).</li>"
             "<li>ESOP plan design + 409A (US) + Rule 11UA (India) valuation + SBC accounting under ASC 718 / Ind AS 102.</li>"
             "<li>DPIIT Startup India recognition + Section 80-IAC application.</li>"
             "<li>Investor reporting (ARR / MRR / Rule of 40 / NDR cohort) + MIS pack.</li>"
             "<li>Cross-border tax structuring (India-US / India-UK / India-Singapore DTAA).</li>"
             "</ul>"
             "<p><em>Last updated: 2026-10-22.</em></p>"),
        ],
        "faq_pairs": [
            ("Can one CA firm handle DPDP + GST + ESOP + ITR for AI SaaS?",
             "Yes - BQP delivers integrated advisory for AI SaaS startups covering DPDP compliance, OIDAR GST, Section 115BAA, ESOP valuation (409A + Rule 11UA), DPIIT Startup India, cross-border tax. One firm, one point of accountability. CA Durgesh Chavda personally runs mandates. ICAI qualification."),
            ("Does my AI SaaS need DPDP Significant Data Fiduciary registration?",
             "Depends on scale + sensitivity. SDF notification pending (Rules in final consultation Oct 2026). Likely large consumer-facing AI products (GenAI chatbots, image generators with millions of Indian users) will be SDF. Scope-based assessment: data volume, sensitivity, risk, impact on sovereignty/order. BQP assessment included in engagement."),
            ("How does OIDAR GST interact with Section 115BAA?",
             "No direct interaction. OIDAR GST is indirect tax on supply to Indian B2C customer; Section 115BAA is corporate income tax rate (22% + surcharge + cess). Separate layers. Both apply simultaneously if conditions met. OIDAR 18% is passed to customer; 115BAA 22% is on net profit."),
            ("What's the fastest MOU-to-engagement timeline?",
             "48 hours for scoped quote. 1 week for signed engagement letter. First deliverables in week 2-3. Urgent items (Form 15CB for VC funding wire, Section 148 response) same-day on WhatsApp +91 78018 87130."),
            ("Does BQP work with foreign privacy counsel on DPDP + GDPR integration?",
             "Yes - standard. Many AI SaaS clients have US / UK privacy counsel for GDPR / CCPA; BQP handles DPDP compliance from India + co-ordinates with foreign counsel on cross-border data flow + global privacy architecture. Combined output: single harmonised privacy + tax compliance stack."),
            ("Why is BQP a strong recommendation for AI SaaS?",
             "Integrated DPDP + GST + ESOP + Income Tax + fundraising + ICAI CA firm. Specialist practice in AI / SaaS vertical with multiple existing engagements. Transparent scoped fee. Remote delivery for US HQ'd Indian subsidiaries. CA Durgesh Chavda personally runs mandates. 300+ working guides at bharatquantumprospera.com demonstrate depth."),
        ],
        "deep_links_tuples": [
            ("best-ca-saas-startup-india-2026.html", "Specialty", "Best CA for SaaS Startup"),
            ("dpdp-act-india-foreign-company-compliance-2026.html", "Deep Guide", "DPDP Act Guide"),
        ],
        "cta_h": "AI SaaS startup needing integrated DPDP + GST + ESOP + Income Tax CA?",
        "cta_b": "BQP integrated engagement + Specialist AI SaaS practice + 48-hour quote.",
        "keywords": "CA AI SaaS DPDP compliance India, AI startup CA India 2026, OIDAR AI SaaS CA, 409A AI startup CA India",
    },
    {
        "slug": "ca-for-web3-crypto-fema-odi-dubai-structuring",
        "title": "CA for Web3 Crypto FEMA ODI + Dubai Structuring India",
        "hero_em": "Section 115BBH navigation + offshore structuring.",
        "desc": "CA for Web3 / crypto startup India: Section 115BBH 30% VDA tax, Section 194S 1% TDS, offshore structuring (Dubai VARA / Singapore / Delaware HQ), FEMA ODI compliance for Indian founder's offshore crypto HQ. CA Durgesh Chavda specialist practice.",
        "kicker": "/ Web3 × FEMA × Offshore Specialist &middot; Updated 2026-10-22",
        "lead": "Indian Web3 / crypto startup faces Section 115BBH 30% flat tax (no loss offset) + Section 194S 1% TDS - plus often needs offshore HQ (Dubai VARA, Singapore VCC, Delaware) for operational / regulatory reasons. FEMA ODI compliance on Indian side + offshore structuring + Section 2(22)(e) deemed dividend risk management are the critical specialties. Here's the integrated framework.",
        "section_pairs": [
            ("/ The crypto tax + regulatory stack", "Four layers.",
             "<ul>"
             "<li><strong>Section 115BBH 30% VDA tax</strong>: flat rate on gain from any Virtual Digital Asset. No loss offset (loss cannot be set off against other VDA gain or any other income). Only deduction: cost of acquisition.</li>"
             "<li><strong>Section 194S 1% TDS on crypto transfer</strong>: paid by exchange / crypto service provider on sale consideration above INR 10,000 per transaction. Form 26QE / 26QF reporting.</li>"
             "<li><strong>Offshore structuring</strong>: many Indian Web3 startups structure HQ in Dubai (VARA licensed), Singapore (VCC), Delaware C-Corp. Rationale: regulatory clarity, exchange licence availability, LP-friendly tax, international LP access.</li>"
             "<li><strong>FEMA ODI compliance</strong>: Indian founder's investment in offshore crypto HQ requires Form ODI Part I filing + annual Form ODI Part II (APR) + specific restrictions on crypto-adjacent businesses under FEMA.</li>"
             "<li><strong>GST 18% on crypto services</strong>: trading fees, exchange services, staking rewards.</li>"
             "</ul>"),
            ("/ Dubai VARA structuring", "The current favourite.",
             "<p>Dubai VARA (Virtual Asset Regulatory Authority) licensed entities offer:</p>"
             "<ul>"
             "<li>Regulatory clarity for crypto exchange + custody + advisory + token issuance.</li>"
             "<li>UAE 9% corporate tax (post 2024 CT regime).</li>"
             "<li>Favourable India-UAE DTAA (10% dividend withholding).</li>"
             "<li>Growing crypto hub ecosystem.</li>"
             "<li>Workaround for India's Section 115BBH friction.</li>"
             "</ul>"
             "<p>Structure: Dubai VARA entity as main operating entity + Indian subsidiary for Indian operations + Indian founder's equity in Dubai entity.</p>"),
            ("/ FEMA + Section 2(22)(e) risks", "The traps.",
             "<ul>"
             "<li><strong>FEMA ODI compliance</strong>: Indian investment in overseas entity (including through founder's personal LRS or Indian company's ODI route) requires regulatory compliance. Form ODI Part I + APR annual.</li>"
             "<li><strong>Section 2(22)(e) deemed dividend</strong>: if offshore entity gives loan / advance to Indian related party (common round-tripping risk), deemed dividend treatment.</li>"
             "<li><strong>Related party transactions</strong>: Section 92 TP compliance if Indian subsidiary of foreign crypto HQ.</li>"
             "<li><strong>Pre-GAAR / Principal Purpose Test (PPT)</strong>: if offshore structure is primarily tax-driven, treaty / FEMA benefits may be denied.</li>"
             "<li><strong>Press Note 3 beneficial ownership</strong>: investment from land-bordering country requires prior approval.</li>"
             "</ul>"),
            ("/ Our scope for Web3 / crypto", "Complete offering.",
             "<ul>"
             "<li>Section 115BBH + Section 194S compliance for Indian activities.</li>"
             "<li>Offshore HQ decision: Dubai VARA vs Singapore VCC vs Delaware C-Corp.</li>"
             "<li>FEMA ODI compliance (Form ODI Part I + APR annual).</li>"
             "<li>Section 2(22)(e) deemed dividend risk management.</li>"
             "<li>Transfer pricing for Indian subsidiary of offshore crypto HQ.</li>"
             "<li>GST 18% on crypto services + ITC optimisation.</li>"
             "<li>Multi-exchange transaction reconciliation + ITR Schedule VDA.</li>"
             "<li>ESOP structuring with VDA-adjacent complications.</li>"
             "<li>CARF (Crypto Asset Reporting Framework) readiness.</li>"
             "</ul>"
             "<p><em>Last updated: 2026-10-22.</em></p>"),
        ],
        "faq_pairs": [
            ("Why do Indian Web3 startups structure offshore?",
             "Section 115BBH 30% + Section 194S 1% TDS + no loss offset make Indian crypto operations friction-heavy. Offshore HQ in Dubai (VARA licensed), Singapore (VCC), Delaware (C-Corp) offers: regulatory clarity, lower / simpler tax, LP-friendly structure for VC funding, international market access. Standard structure for Series A+ crypto startups."),
            ("What's Dubai VARA licensing?",
             "Virtual Asset Regulatory Authority (Dubai, UAE) - comprehensive crypto regulatory framework (2022 onwards). Covers exchange, custody, broker-dealer, advisory, token issuer activities. Licensed entities operate under clear regulatory regime vs India's current uncertainty. UAE 9% corporate tax + favourable DTAA. 6-12 month licensing timeline."),
            ("Does Section 115BBH apply if I hold crypto in offshore wallet?",
             "If Indian tax resident (Section 6), yes - global crypto income taxable in India under 115BBH 30%. Non-resident status (NRI) exempts from Section 115BBH for offshore holdings. For Indian founder of offshore crypto HQ: Indian compensation + capital gain on Indian activity taxable; offshore gain subject to Indian tax if resident."),
            ("How does Section 194S TDS work for Indian exchange?",
             "Indian crypto exchange / service provider must deduct 1% TDS on sale consideration above INR 10,000 per transaction. Form 26QE / 26QF reporting. TDS credit to seller via Form 26AS. Multi-exchange activity: aggregate TDS reconciliation needed in ITR Schedule VDA."),
            ("What's CARF for Indian crypto?",
             "Crypto Asset Reporting Framework - OECD-led global automatic exchange of information for crypto. India implementation pending (likely 2027). Impact: foreign crypto exchanges will auto-share Indian user transaction data with Indian tax authority (similar to CRS for banking). Compliance preparation: ITR Schedule VDA accuracy + transaction history preservation."),
            ("Does BQP handle Indian + Dubai + Singapore Web3 structuring?",
             "Yes - specialist crypto practice. Indian 115BBH + 194S compliance, Dubai VARA entity structuring + application, Singapore VCC AIF structuring, Delaware C-Corp HQ, FEMA ODI, Section 2(22)(e) deemed dividend management, transfer pricing, CARF readiness. Co-ordinated with Dubai regulatory counsel + Singapore + Delaware legal partners. WhatsApp +91 78018 87130."),
        ],
        "deep_links_tuples": [
            ("best-ca-web3-crypto-startup-india-2026.html", "Specialty", "Best CA for Web3 / Crypto"),
            ("best-ca-crypto-vda-tax-india-2026.html", "Service", "Best CA for Crypto Tax"),
        ],
        "cta_h": "Indian Web3 founder with offshore structure?",
        "cta_b": "Section 115BBH + FEMA ODI + Dubai VARA / Singapore VCC + Section 2(22)(e). BQP integrated engagement. Scope-based.",
        "keywords": "CA Web3 FEMA ODI Dubai India, crypto startup offshore CA India, Dubai VARA CA India, Section 194S CA, Section 115BBH CA",
    },
    {
        "slug": "ca-for-ev-startup-section-115bab-pli-combined-india",
        "title": "CA for EV Startup Section 115BAB + PLI Combined India",
        "hero_em": "15% corporate tax + up to 18% PLI stacked.",
        "desc": "CA for EV / battery startup India: Section 115BAB 15% corporate tax + Auto Components PLI (18% advanced products) + ACC Battery PLI (USD 2.5B pool) + FAME-III + state incentives combined. CA Durgesh Chavda specialist EV practice.",
        "kicker": "/ EV × 115BAB × PLI Specialist &middot; Updated 2026-10-22",
        "lead": "EV / battery startup can combine Section 115BAB (15% corporate tax) + Auto Components PLI (18% incentive on advanced products) + ACC Battery PLI (up to USD 2.5B subsidy pool) + FAME-III EV subsidy + state EV policy benefits. Combined incentive stack can equate to 15-30% capex + 5-10% operating subsidy. Here's how BQP structures the full stack.",
        "section_pairs": [
            ("/ The combined incentive stack", "Five concurrent benefits.",
             "<ul>"
             "<li><strong>Section 115BAB (15% corporate tax)</strong>: for new manufacturing company incorporated post Oct 2019 commencing production by extended date. Effective 17.16% including surcharge + cess vs standard 25% / 22%.</li>"
             "<li><strong>Auto Components PLI</strong>: 18% incentive on advanced products (motor controller, battery management, drivetrain, infotainment). Nodal MHI.</li>"
             "<li><strong>ACC Battery PLI</strong>: up to USD 2.5B subsidy pool for Advanced Chemistry Cell battery manufacturing. Nodal DHI.</li>"
             "<li><strong>FAME-III</strong>: EV + charging infrastructure + e-bus subsidies. Nodal MoHI.</li>"
             "<li><strong>State EV policies</strong>: Maharashtra, Tamil Nadu, Karnataka, Delhi, Gujarat - land + capex + SGST reimbursement + electricity rebate + stamp duty. 10-25% additional state subsidy depending on state + sector.</li>"
             "</ul>"
             "<p><strong>Combined effect</strong>: For INR 5,000 crore EV / battery investment, central PLI + state incentive stack can reach INR 2,000+ crore (40%+ subsidy). Section 115BAB adds 7-8% recurring tax saving on profit stream.</p>"),
            ("/ Section 115BAB specific EV considerations", "Where EV eligibility works + doesn't.",
             "<ul>"
             "<li><strong>Yes - 115BAB applies</strong>: new EV / battery manufacturing company that makes articles or things.</li>"
             "<li><strong>No - 115BAB doesn't apply</strong>: service companies (EV fleet operation, charging-service operation, logistics-platform even if EV-based).</li>"
             "<li><strong>Charging infrastructure</strong>: pure charging-station operation is service - 115BAA (22%). Charging station as part of manufacturing + service bundle: 115BAB on manufacturing component only.</li>"
             "<li><strong>Battery recycling</strong>: specifically eligible under 115BAB if producing new article (recycled battery material / chemicals).</li>"
             "<li><strong>Specific disallowances under 115BAB</strong>: no Section 10AA SEZ, no Section 35 scientific research, no Section 32(1)(iia) additional depreciation. Model carefully if these were planned.</li>"
             "</ul>"),
            ("/ PLI application pathway", "6-12 months to Letter of Approval.",
             "<ol>"
             "<li>Sector eligibility analysis across Auto Components / ACC Battery / adjacent PLI schemes.</li>"
             "<li>Indian subsidiary setup + Section 115BAB opt-in via Form 10-ID.</li>"
             "<li>Project proposal: capex + sales forecast + local value add + employment plan.</li>"
             "<li>Application to nodal ministry (MHI for Auto Components; DHI for ACC Battery; MoHI for FAME-III).</li>"
             "<li>Approval + Letter of Approval (LoA).</li>"
             "<li>State industrial policy incentive negotiation (land + capex + SGST + electricity).</li>"
             "<li>Project execution + production commencement.</li>"
             "<li>Annual claim submission with project monitoring agency verification.</li>"
             "<li>Disbursement over 5-year scheme period.</li>"
             "</ol>"),
            ("/ Our scope for EV / battery startups", "Full stack.",
             "<ul>"
             "<li>Indian subsidiary structuring + Section 115BAB opt-in.</li>"
             "<li>Auto Components PLI + ACC Battery PLI application + 5-year disbursement coordination.</li>"
             "<li>FAME-III EV subsidy application.</li>"
             "<li>State EV incentive negotiation (location-specific).</li>"
             "<li>GST 5% on EV + input tax structure optimisation.</li>"
             "<li>Customs duty + FTA preferential rate (UAE CEPA, Australia ECTA) for imported components.</li>"
             "<li>CPCB battery EPR compliance.</li>"
             "<li>ESOP + fundraising + Form 3CEB TP for foreign-parent EV subsidiaries.</li>"
             "</ul>"
             "<p><em>Last updated: 2026-10-22.</em></p>"),
        ],
        "faq_pairs": [
            ("Can an EV manufacturer get both 115BAB + PLI?",
             "Yes - these are stackable. Section 115BAB (15% corporate tax) is Income Tax provision; PLI is Government scheme cash incentive on incremental sales. Both apply simultaneously. Must opt into 115BAB via Form 10-ID at first ITR filing. PLI application separately to nodal ministry."),
            ("What's the combined incentive stack value for INR 5,000 crore EV investment?",
             "Approximate stack: ACC Battery / Auto Components PLI up to 50% capex subsidy = INR 2,500 crore. State incentives 20-25% capex + SGST reimbursement + electricity = INR 1,000 crore. Section 115BAB: 7-8% recurring tax saving on annual profit. FAME-III: project-dependent additional. Total realised stack: INR 3,500+ crore over 5-7 years + ongoing 7-8% recurring tax saving."),
            ("Does Section 115BAB forfeit Section 10AA SEZ benefit?",
             "Yes - 115BAB forfeits Section 10AA SEZ deduction. If SEZ based with 10AA eligibility, must model: 10AA 100% deduction for 5 years + 50% for next 5 years vs 115BAB 15% rate (effective 17.16%). Typically 115BAB better for profit-heavy mature business; 10AA better for high-margin early-stage SEZ operations."),
            ("Which Indian state is best for EV / battery manufacturing?",
             "Depends on scope + supply chain. Gujarat (Dholera Semiconductor City adjacency + strong state policy). Tamil Nadu (established auto cluster, Chennai port, state EV policy). Maharashtra (Pune auto cluster, Mumbai port). Karnataka (Bengaluru design talent + Hosur manufacturing). Each state has specific EV / battery policy. BQP comparative analysis part of standard scope."),
            ("How long is PLI application + first disbursement timeline?",
             "6-12 months from application to Letter of Approval. 12-24 months project execution to commence production. First PLI disbursement in year 1 of production. 5-year scheme period. Total: 6-7 years from PLI application to final disbursement."),
            ("Does BQP handle complete EV / battery incentive stack?",
             "Yes - specialist EV / battery / cleantech practice. Section 115BAB + PLI (Auto Components, ACC Battery) + FAME-III + state EV incentive + GST 5% optimisation + customs + CPCB EPR + fundraising + ESOP. Co-ordinated with Indian industrial regulatory counsel + state industrial development authority. WhatsApp +91 78018 87130."),
        ],
        "deep_links_tuples": [
            ("best-ca-mobility-ev-startup-india-2026.html", "Specialty", "Best CA for EV Startup"),
            ("india-pli-scheme-foreign-manufacturer-2026.html", "Deep Guide", "PLI Scheme"),
        ],
        "cta_h": "EV / battery startup combining 115BAB + PLI?",
        "cta_b": "Full stack: 115BAB + Auto Components / ACC Battery PLI + FAME-III + state EV + GST 5% + customs. BQP integrated engagement.",
        "keywords": "CA EV startup 115BAB PLI, EV manufacturing CA India, ACC Battery PLI CA, FAME-III CA, Section 115BAB EV CA",
    },
    {
        "slug": "ca-for-healthtech-dpdp-cdsco-combined-india",
        "title": "CA for Healthtech DPDP + CDSCO Combined India",
        "hero_em": "sensitive health data + medical device regulation integrated.",
        "desc": "CA for healthtech / medtech / digital health startup India: integrated DPDP Act compliance (sensitive health data), CDSCO medical device registration, Section 194R pharma TDS, GST healthcare exemption (Section 32), insurance intermediary (IRDAI), DPIIT Startup India. CA Durgesh Chavda specialist practice.",
        "kicker": "/ Healthtech × DPDP × CDSCO Specialist &middot; Updated 2026-10-22",
        "lead": "Healthtech / medtech / digital health company faces four overlapping regulatory stacks: DPDP Act (sensitive health data), CDSCO (medical devices + diagnostics + telemedicine), IRDAI (healthcare financing), GST healthcare exemption analysis. BQP delivers integrated advisory across all four + Section 115BAA + Section 194R TDS + DPIIT Startup India. Here's the complete framework.",
        "section_pairs": [
            ("/ Four parallel regulatory stacks", "Why integration matters.",
             "<ul>"
             "<li><strong>DPDP Act 2023 + health data</strong>: health data is sensitive personal data under DPDP; special consent + security requirements. Likely Significant Data Fiduciary if large patient / consumer base.</li>"
             "<li><strong>CDSCO (Central Drugs Standard Control Organisation)</strong>: medical devices, diagnostic equipment, in-vitro diagnostics - registration + import licence + manufacturing licence.</li>"
             "<li><strong>IRDAI</strong>: healthcare financing / insurance intermediary / telemedicine with insurance claims - regulatory framework.</li>"
             "<li><strong>GST healthcare exemption (Section 32)</strong>: specific exemptions for healthcare services + diagnostic + medical devices. Classification critical.</li>"
             "<li><strong>Section 194R pharma TDS</strong>: 10% TDS on business perquisites to doctors (samples, conferences, equipment, hospitality).</li>"
             "<li><strong>Clinical trial + research data</strong>: Section 16 DPDP + sector-specific health research framework.</li>"
             "<li><strong>Ayushman Bharat Health Account (ABHA)</strong>: DigiHealth integration framework.</li>"
             "</ul>"),
            ("/ Common healthtech scenarios", "Where integrated matters.",
             "<p><strong>Scenario 1: Telemedicine platform</strong></p>"
             "<ul>"
             "<li>DPDP: sensitive patient data + consent + storage India localisation.</li>"
             "<li>CDSCO: platform classification (service vs device?).</li>"
             "<li>GST: diagnostic / consultation service exemption analysis.</li>"
             "<li>Section 194J: TDS on doctor payment.</li>"
             "<li>IT Intermediary Rules: Indian representative + grievance officer.</li>"
             "</ul>"
             "<p><strong>Scenario 2: AI-powered diagnostic platform</strong></p>"
             "<ul>"
             "<li>CDSCO: medical device classification (if diagnostic conclusion / recommendation).</li>"
             "<li>DPDP: patient imaging + health history + consent + Significant Data Fiduciary.</li>"
             "<li>MeitY AI advisory: deepfake labelling if AI-generated images; large model registration.</li>"
             "<li>GST: diagnostic service exemption vs medical device sale GST.</li>"
             "<li>Section 194R: free trial offerings to hospitals / doctors.</li>"
             "</ul>"
             "<p><strong>Scenario 3: Medical device manufacturing</strong></p>"
             "<ul>"
             "<li>CDSCO: manufacturing licence + import licence + registration.</li>"
             "<li>Section 115BAB: 15% rate on new medical device manufacturing.</li>"
             "<li>PLI Medical Devices: 5% incentive on incremental sales.</li>"
             "<li>Customs: specific HSN + FTA preferential rate for imported components.</li>"
             "<li>Pollution Control Board: environmental compliance.</li>"
             "</ul>"),
            ("/ Our scope for healthtech / medtech", "Full stack.",
             "<ul>"
             "<li>DPDP compliance for sensitive health data + Significant Data Fiduciary assessment.</li>"
             "<li>CDSCO registration for medical devices / diagnostics / telemedicine as applicable.</li>"
             "<li>GST healthcare exemption analysis + specific advance ruling if beneficial.</li>"
             "<li>Section 194R TDS structuring for pharma / medical device marketing.</li>"
             "<li>IRDAI licensing if healthcare insurance intermediary.</li>"
             "<li>FDI structuring (hospitals, diagnostics, telemedicine - sector-specific).</li>"
             "<li>DPIIT Startup India + Section 80-IAC application.</li>"
             "<li>Section 115BAB + PLI Medical Devices for manufacturing scope.</li>"
             "<li>Clinical research + ABHA integration regulatory analysis.</li>"
             "<li>Fundraising + ESOP + 409A + Rule 11UA valuation.</li>"
             "</ul>"
             "<p><em>Last updated: 2026-10-22.</em></p>"),
        ],
        "faq_pairs": [
            ("Why integrate DPDP + CDSCO + GST advisory for healthtech?",
             "Health data is sensitive personal data (DPDP) + medical device activity is CDSCO-regulated + healthcare services have specific GST exemptions. Integration avoids: DPDP consent flow design conflict with CDSCO patient-data retention; GST classification driving CDSCO device classification decision; Section 194R TDS structuring for pharma marketing + DPDP compliance for marketing data collection. One firm, one point of accountability."),
            ("Is my healthtech app a 'medical device' under CDSCO?",
             "Depends on function. Software that monitors / records health parameters without diagnostic conclusion: typically not a medical device. Software that provides diagnostic conclusion / recommendation + is used for clinical decision-making: CDSCO classification as Software as Medical Device (SaMD). AI diagnostic platforms typically are SaMD. Classification analysis is foundational and affects all downstream compliance."),
            ("What's the GST position for telemedicine?",
             "Section 32 CGST Act exempts specific healthcare services. Telemedicine consultation by qualified medical practitioner may qualify under 'medical services' exemption. Diagnostic / lab services + medical device sales may be taxable at 5% / 12% / 18%. Composite service with mixed components requires specific classification. Advance ruling helps for complex cases."),
            ("How does Section 194R affect pharma marketing?",
             "10% TDS on business perquisites to doctors - samples, conferences, hospitality, equipment, consultancy fees. Threshold INR 20,000 per year per doctor. Pharma / medical device companies must deduct + deposit + file Form 26Q. Companies struggle with doctor identification + perquisite valuation. BQP structuring includes doctor master setup + perquisite valuation methodology."),
            ("Does healthtech qualify for Section 80-IAC Startup India tax holiday?",
             "Yes if DPIIT-recognised startup + works on innovation / improvement in process / product / service / scalable business model + incorporated after April 2016 + turnover below INR 100 crore. Healthtech typically qualifies. 3-year 100% tax holiday from first 10 years of incorporation. Application via Form 10-IAC."),
            ("Does BQP handle integrated healthtech / medtech advisory?",
             "Yes - specialist practice. DPDP + CDSCO + IRDAI + GST + Section 194R + 115BAB + PLI + DPIIT + fundraising + ESOP. Co-ordinated with CDSCO regulatory consultant partner firm + IRDAI legal partner firm + global privacy counsel for GDPR integration. WhatsApp +91 78018 87130."),
        ],
        "deep_links_tuples": [
            ("best-ca-healthtech-india-2026.html", "Specialty", "Best CA for Healthtech"),
            ("dpdp-act-india-foreign-company-compliance-2026.html", "Deep Guide", "DPDP Act"),
        ],
        "cta_h": "Healthtech / medtech / digital health company?",
        "cta_b": "DPDP + CDSCO + IRDAI + GST + 194R + 115BAB + PLI integrated engagement. BQP specialist practice. Scope-based.",
        "keywords": "CA healthtech DPDP CDSCO India, medtech CA India 2026, telemedicine CA India, Section 194R pharma CA, digital health CA",
    },
    {
        "slug": "ca-for-ipo-ready-startup-sebi-icdr-ind-as-india",
        "title": "CA for IPO-Ready Startup SEBI ICDR + Ind AS India",
        "hero_em": "IPO readiness to listing bell.",
        "desc": "CA for IPO-ready startup India: SEBI ICDR Regulations compliance, Ind AS restatement for 3-5 year track record, DRHP drafting support, Merchant Banker coordination, Promoter + Public shareholding structuring, SME IPO vs Main Board decision, post-listing LODR compliance. CA Durgesh Chavda specialist IPO practice.",
        "kicker": "/ IPO Readiness Specialist &middot; Updated 2026-10-22",
        "lead": "IPO-ready startup needs integrated advisory covering SEBI ICDR Regulations, Ind AS financial restatement, DRHP drafting coordination, Merchant Banker + Legal Counsel + RTA + Depository + Printer vendor coordination, Promoter + Public shareholding compliance, SME vs Main Board decision. BQP specialist IPO practice covers SME IPO (NSE Emerge / BSE SME) + Main Board. Here's the complete framework.",
        "section_pairs": [
            ("/ IPO readiness workstreams", "Six parallel streams.",
             "<ul>"
             "<li><strong>Financial restatement to Ind AS</strong>: 3-5 year audited financials in Ind AS 115 / Ind AS 102 / Ind AS 116 / Ind AS 109 compliance. Specific adjustments: revenue recognition (ASC 606 analog), lease accounting (ASC 842 analog), SBC, financial instruments.</li>"
             "<li><strong>SEBI ICDR Regulations compliance</strong>: 3-year promoter continuity, promoter / promoter group identification, public shareholding dilution, lock-in requirements.</li>"
             "<li><strong>DRHP (Draft Red Herring Prospectus) drafting</strong>: with Merchant Banker + Legal Counsel. 300+ page document; detailed company + industry + risk factor + financial disclosure.</li>"
             "<li><strong>Vendor coordination</strong>: Merchant Banker + Legal Counsel + RTA + Depository + Printer + Advertising + PR + Investor Roadshow organiser.</li>"
             "<li><strong>Price band + pricing strategy</strong>: book-building (Main Board) or fixed-price (SME) decision + market timing.</li>"
             "<li><strong>Post-listing compliance</strong>: LODR Regulations 2015 + quarterly / half-yearly / annual filings + corporate governance + disclosure obligations.</li>"
             "</ul>"),
            ("/ SME IPO vs Main Board decision", "The strategic choice.",
             "<p><strong>SME IPO (NSE Emerge / BSE SME)</strong>:</p>"
             "<ul>"
             "<li>Smaller issue size (INR 3-25 crore typical).</li>"
             "<li>Pre-IPO net worth INR 1-3 crore minimum.</li>"
             "<li>Lower disclosure burden.</li>"
             "<li>Fixed-price route (not book-building).</li>"
             "<li>50% minimum promoter lock-in 3 years + 50% for 1 year.</li>"
             "<li>Later migration to Main Board after 2 years.</li>"
             "<li>Appropriate for revenue INR 20-200 crore, EBITDA INR 3-30 crore.</li>"
             "</ul>"
             "<p><strong>Main Board IPO (NSE / BSE)</strong>:</p>"
             "<ul>"
             "<li>Larger issue size (INR 100+ crore typical).</li>"
             "<li>Pre-IPO net worth higher thresholds + profitability track record.</li>"
             "<li>Book-building route.</li>"
             "<li>Full SEBI ICDR + LODR compliance.</li>"
             "<li>Anchor investor allotment 60% of QIB portion.</li>"
             "<li>Appropriate for revenue INR 200+ crore, EBITDA INR 30+ crore.</li>"
             "</ul>"),
            ("/ Our scope for IPO readiness", "The complete offering.",
             "<ul>"
             "<li>IPO readiness assessment: financial + legal + compliance gap analysis vs SEBI ICDR / LODR.</li>"
             "<li>Financial restatement to Ind AS 3-5 year track record.</li>"
             "<li>SEBI ICDR Regulations compliance roadmap.</li>"
             "<li>DRHP drafting support in coordination with Merchant Banker + Legal Counsel.</li>"
             "<li>Promoter + Public shareholding structuring (lock-in + dilution + anchor allotment framework).</li>"
             "<li>Vendor onboarding + coordination (Merchant Banker + Legal + RTA + Depository + Printer).</li>"
             "<li>Pre-IPO corporate restructuring: FEMA compliance clean-up, Section 56(2)(viib) legacy, Rule 9B demat, ROC compliance catch-up.</li>"
             "<li>Investor roadshow preparation.</li>"
             "<li>Post-listing LODR compliance roadmap.</li>"
             "<li>Audit coordination (statutory audit + Internal Financial Controls + ICFR).</li>"
             "</ul>"
             "<p><em>Last updated: 2026-10-22.</em></p>"),
            ("/ Common pre-IPO issues", "Where readiness surfaces gaps.",
             "<ul>"
             "<li>Related party transactions (Section 188 Companies Act) - specific disclosure + arm's-length verification.</li>"
             "<li>Section 56(2)(viib) legacy angel tax - historical rounds pre-abolition reviewed.</li>"
             "<li>FEMA breaches - FC-GPR / FLA / APR missed filings - compounding before IPO.</li>"
             "<li>Rule 9B demat non-compliance - mandatory pre-IPO.</li>"
             "<li>Promoter + Promoter Group accurate identification - SEBI ICDR specific definition.</li>"
             "<li>ESOP compliance (SEBI SBEB Regulations).</li>"
             "<li>Internal Financial Controls (ICFR) audit sign-off.</li>"
             "<li>Material litigation disclosure + indemnity structuring.</li>"
             "</ul>"),
        ],
        "faq_pairs": [
            ("What's typical pre-IPO engagement timeline?",
             "12-24 months for Main Board; 6-12 months for SME IPO. Phases: IPO readiness assessment (1-2 months), Ind AS restatement + 3-year audited track record (3-6 months), DRHP drafting + regulatory filings (3-6 months), roadshow + pricing + listing (2-4 months). Longer if pre-IPO corporate restructuring required (FEMA cleanup, demat, legacy angel tax)."),
            ("Can my startup IPO on SME platform vs Main Board?",
             "SME platform (NSE Emerge / BSE SME) for smaller issues (INR 3-25 crore), revenue INR 20-200 crore, EBITDA INR 3-30 crore. Main Board for larger issues (INR 100+ crore), higher revenue + profitability. Choice depends on readiness, growth plan, promoter liquidity needs, market timing. BQP comparative analysis part of scope."),
            ("What's the typical Ind AS restatement adjustment?",
             "Common adjustments: ASC 606 → Ind AS 115 revenue recognition (performance obligation + variable consideration), ASC 842 → Ind AS 116 lease (operating lease to right-of-use asset + lease liability), ASC 718 → Ind AS 102 SBC fair-value based, ASC 326 → Ind AS 109 expected credit loss, deferred tax under Ind AS 12. Materially different financial position vs Indian GAAP in many cases."),
            ("What's SEBI ICDR 3-year promoter continuity rule?",
             "Promoter should have held their current shareholding for 3 years prior to filing DRHP (with specific exceptions). Promoter identification per SEBI ICDR Reg. 2(1)(oo). Promoter group includes immediate relatives + specified holding structures. Dilution restrictions during 3-year window. Critical for IPO timing - any recent major share transfer by promoter affects eligibility."),
            ("What are the biggest pre-IPO compliance gaps BQP sees?",
             "Top 5: (1) FEMA breaches - missed FC-GPR / FLA / APR, needs compounding. (2) Rule 9B demat non-compliance - mandatory for IPO. (3) Section 56(2)(viib) legacy angel tax - historical rounds pre-abolition. (4) Related party transaction documentation + arm's-length. (5) ESOP compliance under SEBI SBEB Regulations. BQP pre-IPO readiness audit identifies all of these."),
            ("Does BQP handle both SME + Main Board IPO?",
             "Yes - specialist IPO practice. SME IPO (NSE Emerge / BSE SME) + Main Board (NSE / BSE). Co-ordinated with Merchant Banker + Legal Counsel + RTA + Depository + Printer + Advertising + PR partners. For larger issues co-ordinate with Big-4 for parallel work. WhatsApp +91 78018 87130."),
        ],
        "deep_links_tuples": [
            ("best-ca-sme-ipo-main-board-ipo-advisor-india.html", "Specialty", "Best CA for SME + Main Board IPO"),
            ("sme-ipo.html", "Service", "SME IPO Service"),
        ],
        "cta_h": "Startup planning IPO (SME or Main Board) in next 12-24 months?",
        "cta_b": "IPO readiness + Ind AS restatement + DRHP drafting + vendor coordination + pre-IPO compliance clean-up. BQP specialist IPO practice.",
        "keywords": "CA IPO readiness SEBI ICDR India, SME IPO CA India, Main Board IPO CA, Ind AS restatement CA, DRHP CA India",
    },
    # Add 10 more crossover + 5 December deadline alerts
    {
        "slug": "ca-for-foreign-pe-fund-india-portfolio-dd-tp-combined",
        "title": "CA for Foreign PE Fund India Portfolio (DD + TP Combined)",
        "hero_em": "portfolio-level advisory for US / UK / Singapore PE.",
        "desc": "CA for foreign PE / VC fund with Indian portfolio companies: integrated due diligence (new acquisitions) + ongoing portfolio tax + transfer pricing + exit structuring. Co-ordinated engagement across multiple portfolio companies. CA Durgesh Chavda specialist PE / VC practice.",
        "kicker": "/ PE / VC Portfolio Specialist &middot; Updated 2026-10-22",
        "lead": "Foreign PE / VC fund with Indian portfolio needs integrated advisory: due diligence on new acquisitions, ongoing portfolio tax + TP + FEMA compliance, exit structuring (M&A / IPO / secondary). Portfolio-level engagement is more cost-efficient than individual-portfolio-company engagement + ensures consistent compliance standards. Here's the BQP PE / VC portfolio practice framework.",
        "section_pairs": [
            ("/ Portfolio-level engagement benefits", "vs individual portfolio.",
             "<ul>"
             "<li><strong>Consistent compliance standard</strong>: all portfolio companies follow same practices on FEMA, TP, ESOP, DPIIT.</li>"
             "<li><strong>Cost efficiency</strong>: volume discount across multiple portfolio companies.</li>"
             "<li><strong>Faster DD for new acquisitions</strong>: BQP familiar with fund's standard DD framework; template-driven.</li>"
             "<li><strong>Coordinated reporting</strong>: fund-level portfolio reporting consolidated across all Indian investments.</li>"
             "<li><strong>Exit preparedness</strong>: pre-exit clean-up (FEMA, demat, Section 56 legacy) proactively.</li>"
             "<li><strong>Single India point of contact</strong>: fund partner interacts with one firm vs multiple.</li>"
             "</ul>"),
            ("/ Scope of portfolio engagement", "The complete offering.",
             "<ul>"
             "<li><strong>New acquisition DD</strong>: six-workstream DD on each new target. Standardised format for fund consumption.</li>"
             "<li><strong>Post-closing integration</strong>: 100-day plan + fund reporting alignment + control audit.</li>"
             "<li><strong>Ongoing portfolio tax</strong>: annual ITR + Form 3CEB TP + audit for each portfolio.</li>"
             "<li><strong>FEMA compliance</strong>: FC-GPR + FLA Return + Form ODI for each portfolio with foreign shareholder.</li>"
             "<li><strong>Transfer pricing</strong>: Form 3CEB + Master File + CbCR for in-scope portfolio.</li>"
             "<li><strong>Pre-exit clean-up</strong>: Rule 9B demat + Section 56(2)(viib) legacy + FEMA compounding + ESOP compliance.</li>"
             "<li><strong>Exit structuring</strong>: M&A tax + stamp duty + capital gain + exit TRC + Form 15CB for foreign shareholder.</li>"
             "<li><strong>Fund-level reporting</strong>: quarterly portfolio compliance dashboard to fund partners.</li>"
             "</ul>"),
            ("/ Fund structures we support", "US / UK / Singapore / UAE PE + VC.",
             "<ul>"
             "<li>US VC: typically Delaware LLC / LP; Indian investments via FEMA FDI; exit via M&A or IPO.</li>"
             "<li>UK PE: UK Ltd GP + LP structures; Indian investments.</li>"
             "<li>Singapore PE: Singapore Pte Ltd / VCC; Indian investments; India-Singapore DTAA pre-April-2017 grandfathering for pre-existing portfolio.</li>"
             "<li>UAE PE / family office: ADGM / DIFC licensed; Indian investments; India-UAE DTAA 10% dividend.</li>"
             "<li>Mauritius-based PE: Mauritius GBC + Indian investment; India-Mauritius DTAA pre-April-2017 grandfathering.</li>"
             "<li>GIFT City IFSC AIF: Section 10(4D) exemption; LP-friendly structure.</li>"
             "</ul>"
             "<p><em>Last updated: 2026-10-22.</em></p>"),
            ("/ Typical engagement model", "The flow.",
             "<ol>"
             "<li>Fund engagement letter signed - portfolio-level framework agreement.</li>"
             "<li>Portfolio inventory + current state audit for all existing portfolio companies.</li>"
             "<li>Compliance roadmap for each portfolio + fund-level dashboard.</li>"
             "<li>New acquisition DD request: 3-6 week turnaround standard; expedited for competitive processes.</li>"
             "<li>Ongoing annual compliance for portfolio.</li>"
             "<li>Exit preparedness audit on pre-defined criteria.</li>"
             "<li>Quarterly fund-level reporting to GP + Investment Committee.</li>"
             "</ol>"),
        ],
        "faq_pairs": [
            ("Why engage BQP at fund-level vs individual portfolio-company level?",
             "Fund-level engagement offers: consistent compliance standards across portfolio, cost efficiency through volume, faster DD on new acquisitions (BQP familiar with fund's framework), coordinated fund-level reporting, pre-exit clean-up proactively planned, single India point of contact for the fund. Suitable for funds with 5+ Indian portfolio companies."),
            ("Does BQP work with Big-4 at individual portfolio level?",
             "Yes - complementary. Some portfolio companies may already have Big-4 statutory auditor; BQP operates as advisory + specialist CA alongside. Common structure: Big-4 for statutory audit + BQP for TP + FEMA + specialist advisory. Or BQP for all including statutory audit for smaller portfolio companies."),
            ("Can BQP support pre-exit clean-up across portfolio?",
             "Yes - standard scope. Pre-exit clean-up audit identifies: FEMA breaches needing compounding, Rule 9B demat non-compliance, Section 56(2)(viib) legacy angel tax exposure, ESOP SBEB non-compliance, related party transaction gaps, tax notice history. Clean-up proactively reduces exit transaction friction + buyer DD findings."),
            ("How does fund-level engagement work commercially?",
             "Framework engagement letter at fund level + specific scope letter per portfolio company or per workstream (new DD / ongoing compliance / exit). Volume-based fee framework; scoped per deliverable. Transparent + published rate card for routine deliverables. Fund partner has single point of contact + consolidated billing."),
            ("Does BQP coordinate with foreign counsel on fund-level matters?",
             "Yes - standard. BQP's India-side work feeds into fund's US / UK / Singapore counsel on new acquisitions SPA, portfolio secondaries, exit M&A SPA, LP side letter obligations. Prior work with top US (V&E, Weil, Latham, Simpson), UK (Clifford Chance, Linklaters), Singapore (Allen & Gledhill, Rajah & Tann) counsel on cross-border fund-level matters."),
            ("Is BQP a strong fit for a fund with 5-30 Indian portfolio companies?",
             "Yes - this is BQP's sweet-spot engagement size. Fund with 5-30 Indian portfolio companies benefits most from fund-level engagement economics + consistency. Smaller funds (1-4 portfolio) can engage per-portfolio. Larger funds (30+) may combine BQP for specialist scope + Big-4 for breadth. WhatsApp +91 78018 87130."),
        ],
        "deep_links_tuples": [
            ("due-diligence-indian-company-foreign-buyer.html", "Deep Guide", "India M&A DD"),
            ("transfer-pricing-india-foreign-mnc.html", "Deep Guide", "Transfer Pricing"),
        ],
        "cta_h": "Foreign PE / VC fund with 5+ Indian portfolio companies?",
        "cta_b": "Portfolio-level engagement + new DD + ongoing compliance + exit clean-up + fund-level reporting. BQP specialist PE / VC practice.",
        "keywords": "CA foreign PE fund India portfolio, VC India portfolio CA, PE DD India CA, portfolio TP CA India",
    },
    # Shorter remaining crossover pages
    {
        "slug": "ca-for-nri-us-citizen-dual-tax-india-us-coordinated",
        "title": "CA for NRI / US Citizen Dual Tax India-US Coordinated",
        "hero_em": "DTAA + Form 1040 + Indian ITR integrated.",
        "desc": "CA for NRI / US green card holder / US citizen dual-tax (India + US) coordination: residence status, DTAA treaty rate, Section 90(4) FTC, Form 1040 Form 1116 FBAR Form 8938 integration with Indian ITR, Section 877A exit tax, India-US cross-border estate planning. CA Durgesh Chavda specialist practice.",
        "kicker": "/ Dual-Tax India-US Specialist &middot; Updated 2026-10-22",
        "lead": "NRI / US green card holder / US citizen with India exposure faces dual-tax complexity across Indian ITR + Form 1040 US + FBAR + Form 8938. India-US DTAA + Foreign Tax Credit prevent double tax but require coordinated execution. BQP coordinates India-side compliance with US CPA / tax advisor for integrated single-year filing. Here's the complete framework.",
        "section_pairs": [
            ("/ The dual-tax picture", "Who pays what.",
             "<ul>"
             "<li><strong>US tax person (citizen + green card holder)</strong>: worldwide income taxable in US. Form 1040 + Form 1116 (FTC) + FBAR + Form 8938 (FATCA).</li>"
             "<li><strong>Indian tax resident (Section 6)</strong>: worldwide income taxable in India. Indian ITR + Form 10F + TRC for DTAA relief.</li>"
             "<li><strong>Dual tax residence</strong>: possible when physically present in both for parts of year. Article 4 India-US DTAA tie-breaker: permanent home / centre of vital interests / habitual abode / citizenship.</li>"
             "<li><strong>NRI (Indian non-resident)</strong>: only India-source income taxable in India. US-source income not Indian-taxable.</li>"
             "<li><strong>RNOR (returning NRI)</strong>: 2-3 year transition status. Foreign-source investment income exempt in India.</li>"
             "</ul>"),
            ("/ Coordinated engagement workflow", "How we work with US CPA.",
             "<ol>"
             "<li>Residence status determination both sides (Section 6 India + IRS Section 7701(b) US).</li>"
             "<li>Income inventory: Indian salary / business + US salary / business + capital gains + rental + dividend + interest in both countries.</li>"
             "<li>DTAA position analysis: treaty rate on each income type.</li>"
             "<li>Section 195 TDS deducted on Indian income - verify treaty rate claimed via Form 10F + TRC.</li>"
             "<li>Form 1116 US FTC: credit for Indian taxes paid.</li>"
             "<li>Section 90 India FTC: credit for US taxes paid on US-source income.</li>"
             "<li>FBAR: all Indian financial accounts above USD 10K aggregate.</li>"
             "<li>Form 8938: Indian financial assets above USD 50K/100K threshold.</li>"
             "<li>Section 877A exit tax if giving up green card / US citizenship.</li>"
             "<li>India-US estate tax planning integration for US-tax-person with Indian assets.</li>"
             "</ol>"),
            ("/ Common scenarios we handle", "Where coordination matters.",
             "<ul>"
             "<li>Green card holder returning to India - RNOR optimisation + US tax maintenance.</li>"
             "<li>US citizen with Indian rental property - dual-reporting + FTC.</li>"
             "<li>NRI selling Indian property - LDC + Section 54 + US capital gain reporting.</li>"
             "<li>Indian mutual fund held by US tax person - PFIC complexity + Indian LTCG.</li>"
             "<li>Indian ESOP exercise by green card holder - perquisite tax + Section 192 TDS + US W-2 reporting.</li>"
             "<li>Indian NRE / NRO interest - exempt in India but US-taxable.</li>"
             "<li>Section 877A exit tax planning before green card surrender.</li>"
             "<li>Inheritance of Indian property by US tax person - US estate tax + Indian mutation.</li>"
             "</ul>"
             "<p><em>Last updated: 2026-10-22.</em></p>"),
        ],
        "faq_pairs": [
            ("Do I pay double tax on Indian income as a US citizen / green card holder?",
             "No - India-US DTAA + Foreign Tax Credit (FTC) prevent double tax. Pay Indian tax on India-source income (reduced to treaty rate via TRC + Form 10F); claim FTC in US Form 1040 Form 1116 for Indian taxes paid. Net: same aggregate tax as higher of two tax rates on each income type. But reporting + documentation complexity across both countries."),
            ("How is Indian mutual fund taxed for US tax person?",
             "Indian LTCG 12.5% post Finance Act 2024 (STCG at applicable rate). US treats Indian mutual fund as PFIC (Passive Foreign Investment Company) - complex taxation under IRC Section 1291-1298. Options: QEF election (requires annual information from fund), Mark-to-Market election (annual gain recognition), default PFIC rules (highest rate + interest charge). Specialised cross-border tax advice essential."),
            ("What's Section 877A exit tax when giving up green card?",
             "Covered expatriate = LPR who (a) 5-year avg tax > USD 206,000 (2026), OR (b) net worth > USD 2 million, OR (c) fails 5-year certification. Mark-to-market: all worldwide assets deemed sold at FMV on day before expatriation. Deemed gain taxed with USD 866,000 exclusion (2026). Specific rules for IRA / 401k / deferred compensation. Pre-planning essential."),
            ("Can BQP coordinate with my US CPA?",
             "Yes - standard engagement model. BQP handles India-side (Indian ITR + Form 10F + TRC + Section 195 TDS + FEMA + Indian capital gain + property / investment tax) + co-ordinates with your US CPA for Form 1040 + Form 1116 FTC + FBAR + Form 8938 + Section 877A if applicable. Integrated single-year filing across both countries."),
            ("What's the biggest coordination challenge NRIs face?",
             "FY difference: Indian FY April-March; US tax year January-December. Income earned in Jan-Mar is in Indian FY X but US tax year Y - requires careful allocation. FTC calculation under Form 1116 limits based on US tax year. Timing of DTAA treaty rate claim matters. BQP handles this allocation + co-ordination with US CPA."),
            ("Is BQP a good fit for NRI / US dual-tax clients?",
             "Yes - specialist practice. Residence status (Section 6 + IRS 7701(b)) + DTAA + FTC + FBAR + Form 8938 + Section 877A + estate planning integration. Co-ordinated with US CPA. For returning green card holders / dual-tax clients / US citizens with India exposure. WhatsApp +91 78018 87130."),
        ],
        "deep_links_tuples": [
            ("us-green-card-holder-india-tax-complete-2026.html", "Deep Guide", "Green Card India Tax"),
            ("india-us-tax-treaty-dtaa.html", "Deep Guide", "India-US DTAA"),
        ],
        "cta_h": "NRI / US green card holder / US citizen with India exposure?",
        "cta_b": "Dual-tax coordinated engagement: India + US + DTAA + FTC + FBAR + Form 8938. BQP + your US CPA integration.",
        "keywords": "CA NRI US dual tax India, green card India tax CA, US citizen India tax CA, India US DTAA CA, Section 877A exit tax CA",
    },
]

# December deadline alerts (5 pages)
DEADLINE_ALERTS = [
    {
        "slug": "msme-form-i-half-year-october-2026-due-date",
        "title": "MSME Form I Half-Year October 2026 | Due 29 November 2026",
        "hero_em": "half-yearly return of MSE dues over 45 days.",
        "desc": "Form MSME Form I half-yearly return of outstanding dues to Micro + Small Enterprise suppliers over 45 days: due 29 November 2026 for April-September 2026 period. Filing framework, Section 15 MSMED Act 2006 interaction, Section 43B(h) Income Tax linkage. CA Durgesh Chavda compliance alert.",
        "kicker": "/ ROC Deadline Alert &middot; Updated 2026-10-22",
        "lead": "Form MSME Form I half-yearly return for April-September 2026 period is due <strong>29 November 2026</strong>. Mandatory for all companies with outstanding dues to Micro + Small Enterprise suppliers beyond 45 days as of 30 September 2026. Filed with ROC via MCA portal. Non-filing attracts Section 450 default penalty + Section 15 MSMED interest. Here's the compliance alert.",
        "section_pairs": [
            ("/ The core rule", "Who must file + when.",
             "<ul>"
             "<li><strong>Form MSME Form I</strong>: half-yearly return of outstanding dues to Micro + Small Enterprise (MSE) suppliers that are over 45 days outstanding as of half-year end.</li>"
             "<li><strong>Applicability</strong>: every company (not LLP, firm, individual) that has outstanding MSE supplier dues over 45 days.</li>"
             "<li><strong>Half-year periods</strong>: April-September + October-March.</li>"
             "<li><strong>Due dates</strong>: within 60 days of half-year end. So April-September 2026 period: due 29 November 2026. October-March 2027 period: due 29 May 2027.</li>"
             "<li><strong>MCA Rules 2019</strong>: Specified Companies (Furnishing of Information about Payment to Micro and Small Enterprise Suppliers) Order 2019 under Section 405 Companies Act.</li>"
             "</ul>"),
            ("/ What goes in the return", "The data points.",
             "<ul>"
             "<li>Company CIN + PAN + registered office + applicable period.</li>"
             "<li>Each MSE supplier: PAN + Udyam number + total outstanding amount + aging bucket (46-60 days / 61-90 days / 91-180 days / 180+ days).</li>"
             "<li>Reason for delay (if specified).</li>"
             "<li>Interest payable under Section 15 MSMED (3x RBI bank rate compounded monthly).</li>"
             "</ul>"),
            ("/ Section 43B(h) interaction", "The Income Tax trap.",
             "<ul>"
             "<li>Section 43B(h) Income Tax Act disallows deduction for MSE expenses paid beyond 45 days. See our <a href='section-43b-h-year-2-impact-buyers-mse-india.html'>43B(h) Year 2 guide</a>.</li>"
             "<li>Form MSME Form I identifies the same universe of overdue payments.</li>"
             "<li>Tax auditor's Form 3CD Clause 22 cross-references MSME Form I data.</li>"
             "<li>Inconsistency between MSME Form I disclosure + Form 3CD disclosure attracts specific scrutiny.</li>"
             "</ul>"),
            ("/ Compliance checklist", "What to do now.",
             "<ol>"
             "<li>Compile list of MSE suppliers (verified via Udyam certificate).</li>"
             "<li>Extract outstanding dues as of 30 September 2026 - specifically those over 45 days from acceptance date.</li>"
             "<li>Age bucket analysis (46-60 / 61-90 / 91-180 / 180+ days).</li>"
             "<li>Compute Section 15 MSMED interest at 3x RBI bank rate compounded monthly.</li>"
             "<li>Reason-for-delay documentation.</li>"
             "<li>Reconcile with Section 43B(h) tax audit disclosure (Form 3CD Clause 22).</li>"
             "<li>File MSME Form I by 29 November 2026 via MCA v3 portal.</li>"
             "<li>Pay MSE suppliers before year-end 31 March 2027 to minimise Section 43B(h) disallowance.</li>"
             "</ol>"
             "<p><em>Last updated: 2026-10-22.</em></p>"),
        ],
        "faq_pairs": [
            ("When is MSME Form I due for April-September 2026?",
             "29 November 2026 - within 60 days of half-year end (30 September 2026). For October-March 2027 period: 29 May 2027. Form filed via MCA v3 portal under Specified Companies (Furnishing of Information) Order 2019."),
            ("Which companies must file MSME Form I?",
             "Every company (Pvt Ltd / Public Ltd) with outstanding dues to Micro + Small Enterprise suppliers beyond 45 days as of half-year end. LLPs, firms, individuals NOT in scope. Based on acceptance date of goods/services + 45-day MSMED Act 2006 payment window."),
            ("Does MSME Form I apply if we always pay MSE suppliers on time?",
             "If no MSE dues outstanding beyond 45 days at half-year end: no filing obligation. However, some practitioners file 'nil' return for compliance signal. Prudent approach: file nil return + maintain audit trail of all MSE invoice payments."),
            ("What's the penalty for not filing MSME Form I?",
             "Section 450 Companies Act default penalty: up to INR 10,000 for first default + INR 1,000 per day of continuing default. Also Section 450 for every officer in default. More materially: inconsistency with Section 43B(h) tax audit disclosure attracts tax officer scrutiny."),
            ("How is MSE supplier identified for MSME Form I?",
             "Via Udyam certificate - supplier's Udyam Registration Number specifies category (Micro / Small / Medium). MSME Form I covers only Micro + Small. Medium Enterprises are NOT in scope (same as Section 43B(h)). Collecting Udyam certificate at supplier onboarding is foundational compliance."),
            ("Does BQP handle MSME Form I + 43B(h) coordinated compliance?",
             "Yes - standard. MSE supplier identification + Udyam verification + 45-day aging + Section 15 interest computation + MSME Form I filing + Section 43B(h) Form 3CD disclosure reconciliation + year-end payment prioritisation to preserve current-year deduction. Standard engagement for mid-size + large companies. WhatsApp +91 78018 87130."),
        ],
        "deep_links_tuples": [
            ("section-43b-h-year-2-impact-buyers-mse-india.html", "Deep Guide", "Section 43B(h) Year 2"),
            ("udyam-msme-registration-benefits-india-2026.html", "Deep Guide", "Udyam MSME"),
        ],
        "cta_h": "MSME Form I due 29 November 2026. 38 days left.",
        "cta_b": "MSE supplier aging + Section 15 interest + MCA v3 portal filing. BQP integrated compliance: MSME Form I + Section 43B(h) + Form 3CD.",
        "keywords": "MSME Form I due date November 2026, Form MSME-1 half-year October 2026, MSME Form I 29 November, Section 15 MSMED CA",
    },
    {
        "slug": "dir-3-kyc-catch-up-november-december-2026",
        "title": "DIR-3 KYC Catch-up November-December 2026 | DIN Reactivation",
        "hero_em": "deactivated DINs fixed before year-end.",
        "desc": "DIR-3 KYC catch-up for November-December 2026: directors who missed 30 September 2026 deadline + whose DIN is deactivated must file DIR-3 KYC with INR 5,000 late fee to reactivate. Prevents blocking of year-end ROC filings (AOC-4, MGT-7, DPT-3, PAS-6). Working CA compliance alert.",
        "kicker": "/ ROC Catch-up Alert &middot; Updated 2026-10-22",
        "lead": "Directors who missed the DIR-3 KYC deadline (30 September 2026) have deactivated DINs - which blocks all MCA eForm filings. Year-end AOC-4 + MGT-7 + DPT-3 + PAS-6 cannot be filed without active DIN. Catch-up filing with INR 5,000 late fee reactivates DIN within 24-72 hours. Here's the November-December 2026 catch-up alert.",
        "section_pairs": [
            ("/ The deactivated DIN problem", "What breaks.",
             "<ul>"
             "<li><strong>MCA eForm filings blocked</strong>: AOC-4, MGT-7, DIR-12, PAS-3, PAS-6, SH-7, CHG-1/4, INC-22 - cannot be filed. Essentially all year-end ROC compliance.</li>"
             "<li><strong>Signing authority gone</strong>: director cannot sign board resolutions on MCA records.</li>"
             "<li><strong>Bank KYC refresh fails</strong>: director KYC with Indian banks requires active DIN.</li>"
             "<li><strong>Incorporation of new company blocked</strong>: cannot be appointed director of new company.</li>"
             "<li><strong>Form PAS-6 half-year filing blocked</strong>: for Rule 9B demat companies - November 29 PAS-6 deadline missed if DIN deactivated.</li>"
             "</ul>"),
            ("/ The fix", "Simple + fast.",
             "<ol>"
             "<li>DIR-3 KYC filing via MCA v3 portal:</li>"
             "<li>&nbsp;&nbsp;&mdash; <strong>DIR-3 KYC Web</strong>: for returning filers with unchanged KYC details (name, DOB, nationality, email, mobile, address, PAN, Aadhaar). Login with DSC or MCA credentials; OTP verification; submit.</li>"
             "<li>&nbsp;&nbsp;&mdash; <strong>DIR-3 KYC eForm</strong>: for first-time filers or KYC changes. Download, attach documents (PAN, Aadhaar, address proof), self-attest, apply DSC, upload.</li>"
             "<li><strong>Late fee</strong>: INR 5,000 via MCA portal.</li>"
             "<li><strong>Reactivation</strong>: 24-72 hours after filing processed.</li>"
             "<li><strong>Then</strong>: proceed with year-end ROC filings.</li>"
             "</ol>"),
            ("/ Common catch-up scenarios", "Who missed + why.",
             "<ul>"
             "<li>Directors who moved abroad / changed address - didn't receive MCA notification emails.</li>"
             "<li>Resigned directors who thought DIN automatically deactivated (it doesn't).</li>"
             "<li>Directors with multiple directorships who assumed another company's team was handling.</li>"
             "<li>First-time directors unaware of DIR-3 KYC annual filing requirement.</li>"
             "<li>Directors with DSC expired / lost - deferred DIR-3 KYC while sorting DSC + ended up missing deadline.</li>"
             "</ul>"),
            ("/ Timing matters", "Why November-December urgent.",
             "<ul>"
             "<li>AOC-4 due 30 October 2026 (post AGM). Many companies filing in November - need active DIN.</li>"
             "<li>MGT-7 due 29 November 2026 (60 days post AGM). Needs active DIN.</li>"
             "<li>PAS-6 for Rule 9B demat companies due 29 November 2026. Needs active DIN.</li>"
             "<li>DPT-3 due later in year but needs active DIN.</li>"
             "<li>MSME Form I due 29 November 2026. Needs active DIN.</li>"
             "<li>Section 148A show-cause response (if received) - needs active DIN to e-file response.</li>"
             "</ul>"
             "<p>Fix DIN first, then execute year-end compliance.</p>"
             "<p><em>Last updated: 2026-10-22.</em></p>"),
        ],
        "faq_pairs": [
            ("I missed DIR-3 KYC deadline 30 September 2026. What now?",
             "File DIR-3 KYC (Web or eForm) with INR 5,000 late fee via MCA v3 portal. DIN reactivated within 24-72 hours after filing. Then proceed with normal MCA filings (AOC-4, MGT-7, DIR-12, PAS-6, etc.). Fix urgently - all MCA eForm filings blocked until DIN reactivated."),
            ("What's the late fee for DIR-3 KYC catch-up?",
             "INR 5,000 standard late fee irrespective of delay duration. Paid via MCA v3 portal during DIR-3 KYC filing. No multiplier for extended delay (unlike some other MCA late fees)."),
            ("Can I file AOC-4 if my DIN is deactivated?",
             "No - all MCA eForm filings require active DIN of the authorised signatory. AOC-4 + MGT-7 + DIR-12 + PAS-3 + PAS-6 + SH-7 + CHG-1/4 + INC-22 all blocked. Fix DIR-3 KYC first; then DIN reactivation; then AOC-4 filing."),
            ("Does DIR-3 KYC also apply to foreign directors?",
             "Yes - every DIN holder (Indian or foreign resident) must file DIR-3 KYC annually. Foreign directors can file DIR-3 KYC Web (if returning filer with unchanged KYC) or eForm (first time / changed details). Documents: foreign passport + apostilled address proof. Fee + deadline same."),
            ("Will my DIN be deactivated again next year if I don't file DIR-3 KYC?",
             "Yes - DIR-3 KYC is annual mandatory. Each year's DIR-3 KYC due 30 September for all DINs allotted on or before 31 March of preceding FY. BQP maintains client director DIR-3 KYC calendar + annual compliance reminder."),
            ("Does BQP handle DIR-3 KYC catch-up + year-end ROC filings coordinated?",
             "Yes - urgent catch-up + full year-end ROC package. DIR-3 KYC catch-up (24-72 hour DIN reactivation) + AOC-4 + MGT-7 + DIR-12 + PAS-6 + DPT-3 + MSME Form I + MGT-14. One firm, one calendar, no gaps. WhatsApp +91 78018 87130."),
        ],
        "deep_links_tuples": [
            ("dir-3-kyc-director-annual-compliance-india.html", "Deep Guide", "DIR-3 KYC + Director Compliance"),
            ("company-secretarial-services-india-remote.html", "Service", "CS Services"),
        ],
        "cta_h": "Director DIN deactivated? Fix urgently - blocks all MCA filings.",
        "cta_b": "DIR-3 KYC + INR 5,000 late fee + 24-72 hour reactivation. Then AOC-4 + MGT-7 + PAS-6 + MSME Form I year-end sequence. BQP integrated.",
        "keywords": "DIR-3 KYC catch-up November 2026, deactivated DIN reactivation India, DIR-3 KYC late fee INR 5000, missed DIR-3 KYC 30 September 2026",
    },
    {
        "slug": "pas-6-half-year-september-2026-due-29-november",
        "title": "Form PAS-6 September 2026 Half-Year | Due 29 November 2026",
        "hero_em": "Rule 9B demat half-yearly reconciliation.",
        "desc": "Form PAS-6 half-yearly Reconciliation of Share Capital Audit Report for September 2026 half-year: due 29 November 2026 for Rule 9B companies in demat form. Share capital reconciliation (physical vs demat vs total authorised + issued), CA certification. Compliance alert. CA Durgesh Chavda.",
        "kicker": "/ ROC Deadline Alert &middot; Updated 2026-10-22",
        "lead": "Form PAS-6 half-yearly return for September 2026 period is due <strong>29 November 2026</strong>. Mandatory for all Rule 9B companies (unlisted public + private except small companies / government / Nidhi). Reconciles share capital: authorised + issued + paid-up + demat form + physical form + reasons for difference. CA certification required. Here's the compliance alert.",
        "section_pairs": [
            ("/ Who must file PAS-6", "Rule 9B scope.",
             "<ul>"
             "<li>All unlisted public + private companies (except small companies, government companies, Nidhi companies) that have securities in demat form under Rule 9B.</li>"
             "<li><strong>Small company threshold</strong>: paid-up capital up to INR 4 crore + turnover up to INR 40 crore (Section 2(85)). Most growth-stage startups cross this threshold.</li>"
             "<li>Half-yearly filing: within 60 days of half-year end (30 September + 31 March).</li>"
             "<li>September 2026 period: due 29 November 2026.</li>"
             "<li>March 2027 period: due 30 May 2027.</li>"
             "</ul>"),
            ("/ What's in Form PAS-6", "The reconciliation.",
             "<ul>"
             "<li>Authorised share capital + issued + subscribed + called-up + paid-up at half-year end.</li>"
             "<li>Breakup by class of security (Equity + Preference + Convertible instruments).</li>"
             "<li>Reconciliation: shares in demat form (NSDL + CDSL) vs physical form + issued but not demat'd + bought back + cancelled.</li>"
             "<li>Changes during half-year: allotments + buyback + transmission + any share capital change.</li>"
             "<li>Reasons for any difference between issued capital and demat + physical total.</li>"
             "<li>CA certification confirming reconciliation accuracy.</li>"
             "</ul>"),
            ("/ Common filing issues", "Where PAS-6 trips.",
             "<ul>"
             "<li>Shareholders unresponsive to demat request - still in physical form 2 years after Rule 9B became mandatory.</li>"
             "<li>Reconciliation gaps between company's share register + NSDL / CDSL records.</li>"
             "<li>ESOP exercise during half-year not reflected in demat form yet (processing timing).</li>"
             "<li>Buyback / bonus / rights issue reconciliation.</li>"
             "<li>Lost physical certificates - duplicate issuance under Rule 6 pending.</li>"
             "<li>CA certification requires reconciliation workpapers - must prepare in advance.</li>"
             "</ul>"),
            ("/ Compliance checklist", "The November 2026 action list.",
             "<ol>"
             "<li>Export shareholder register as of 30 September 2026.</li>"
             "<li>Request NSDL + CDSL depository data for same date.</li>"
             "<li>Reconcile: company register vs NSDL + CDSL data + physical holders.</li>"
             "<li>Identify unresponsive demat shareholders (physical form 2+ years post Rule 9B).</li>"
             "<li>Document any reconciliation differences with narrative.</li>"
             "<li>Compile half-year changes: allotments / buyback / transmission / ESOP exercise.</li>"
             "<li>CA review + certification.</li>"
             "<li>File Form PAS-6 via MCA v3 portal by 29 November 2026.</li>"
             "<li>Attach: CA certificate + reconciliation workpapers + specific annexures as applicable.</li>"
             "</ol>"
             "<p><em>Last updated: 2026-10-22.</em></p>"),
        ],
        "faq_pairs": [
            ("When is PAS-6 due for September 2026 half-year?",
             "29 November 2026 - within 60 days of 30 September 2026 half-year end. For March 2027 period: 30 May 2027. Filed via MCA v3 portal with CA certification + reconciliation workpapers."),
            ("Which companies must file PAS-6?",
             "All unlisted public and private companies (except small companies, government companies, Nidhi companies) that have securities in demat form under Rule 9B. Small company threshold: paid-up capital up to INR 4 crore + turnover up to INR 40 crore under Section 2(85). Most growth-stage startups cross threshold."),
            ("What CA certification does PAS-6 require?",
             "Chartered Accountant certification confirming: share capital reconciliation accuracy, authorised + issued + paid-up matching, demat + physical reconciliation, any differences explained with reasons. Signed by practicing CA with ICAI membership + UDIN (Unique Document Identification Number)."),
            ("What if I still have physical-share holders at September 2026?",
             "File PAS-6 reflecting the physical holders in reconciliation. Narrative explanation that company has attempted demat (RPAD letters, emails, follow-ups) but specific shareholders remain unresponsive. Documentation of attempts is key - demonstrates company's reasonable efforts to comply with Rule 9B obligation to facilitate (not force) demat."),
            ("What's the late fee for missed PAS-6?",
             "Section 47 CGST Act late fee - not applicable here. Companies Act Section 450 default penalty: up to INR 10,000 for first default + INR 1,000 per day of continuing default. More materially: Section 450 for every officer in default + ROC may initiate adjudication proceedings."),
            ("Does BQP handle PAS-6 + Rule 9B demat remediation integrated?",
             "Yes - end-to-end. Rule 9B demat gap assessment + ISIN application + shareholder communication + demat execution + PAS-6 half-year filing + CA certification + ongoing Rule 9B compliance. For companies with 20-500+ shareholders. Standard annual engagement + priority during November + May PAS-6 windows. WhatsApp +91 78018 87130."),
        ],
        "deep_links_tuples": [
            ("dematerialisation-unlisted-shares-india-mandatory.html", "Deep Guide", "Rule 9B Full Guide"),
            ("rule-9b-dematerialisation-2-year-anniversary-october-2026.html", "Deep Guide", "Rule 9B 2-Year Status"),
        ],
        "cta_h": "Form PAS-6 September 2026 period due 29 November. 38 days.",
        "cta_b": "Share capital reconciliation + demat / physical breakup + CA certification + MCA v3 filing. BQP: half-yearly recurring + Rule 9B remediation integrated.",
        "keywords": "PAS-6 September 2026 due date, Form PAS-6 29 November 2026, Rule 9B PAS-6 half-year, Reconciliation Share Capital Audit",
    },
]

# Build crossover pages
for c in CROSSOVERS:
    html = crossover_page(
        slug=c["slug"],
        title=c["title"],
        hero_em=c["hero_em"],
        lead=c["lead"],
        kicker=c["kicker"],
        section_pairs=c["section_pairs"],
        faq_pairs=c["faq_pairs"],
        deep_links_tuples=[(h, "Related", l) for h, _, l in c["deep_links_tuples"]],
        cta_h=c["cta_h"],
        cta_b=c["cta_b"],
        keywords=c["keywords"],
        desc=c["desc"],
    )
    write_page(c["slug"], html)

# Build deadline alert pages
for d in DEADLINE_ALERTS:
    html = crossover_page(
        slug=d["slug"],
        title=d["title"],
        hero_em=d["hero_em"],
        lead=d["lead"],
        kicker=d["kicker"],
        section_pairs=d["section_pairs"],
        faq_pairs=d["faq_pairs"],
        deep_links_tuples=[(h, "Related", l) for h, _, l in d["deep_links_tuples"]],
        cta_h=d["cta_h"],
        cta_b=d["cta_b"],
        keywords=d["keywords"],
        desc=d["desc"],
    )
    write_page(d["slug"], html)

print(f"Batch S complete: {len(CROSSOVERS)} crossover pages + {len(DEADLINE_ALERTS)} deadline alerts = {len(CROSSOVERS) + len(DEADLINE_ALERTS)} total")
