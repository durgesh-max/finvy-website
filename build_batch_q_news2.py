# -*- coding: utf-8 -*-
"""Batch Q part 2: remaining 5 news pages + 7 city pages + news hub."""
from build_lib import page, write_page

# 11. India AI regulation
write_page("india-ai-regulation-framework-meity-dia-2026", page(
    slug="india-ai-regulation-framework-meity-dia-2026",
    title="India AI Regulation Framework 2026 | MeitY + DIA Status - BQP",
    description="India AI regulation framework October 2026: MeitY (Ministry of Electronics and IT) advisories on AI deployment, Digital India Act (DIA) draft progress, sector-specific AI rules (RBI AI, SEBI AI, IRDAI AI), DPDP Act interaction with AI data processing, deepfake regulation, foundation model + GenAI governance. Working CA guide by Durgesh Chavda.",
    keywords="India AI regulation 2026, MeitY AI advisory India, Digital India Act AI, India AI governance foreign company, India GenAI regulation 2026",
    hero_kicker="/ AI Regulation Status &middot; Updated 2026-10-22",
    hero_title_html="India AI regulation, <em>principles-based + sector-specific.</em>",
    hero_lead="India has NOT yet enacted a comprehensive AI-specific law (unlike EU AI Act). Instead, the framework is layered: MeitY advisories (soft regulation), DPDP Act 2023 (data processing), sector-specific regulators' AI frameworks (RBI, SEBI, IRDAI), and pending Digital India Act (DIA) consolidation. For foreign AI / GenAI companies in India, this means navigating multiple parallel rules. Here's the complete 2026 practitioner's framework.",
    sections=[
        ("/ Current regulatory layers", "Five parallel rules.",
         "<ul>"
         "<li><strong>MeitY (Ministry of Electronics and Information Technology) advisories</strong>: periodic AI advisories (March 2024, December 2024, 2025 advisories) addressing deepfake labelling, GenAI output moderation, AI model registration (for specified large models), accountability.</li>"
         "<li><strong>DPDP Act 2023</strong>: applies to AI processing of personal data of Indian residents. Consent, data principal rights, Data Fiduciary / Significant Data Fiduciary tier, cross-border transfer blocklist.</li>"
         "<li><strong>Digital India Act (DIA) draft</strong>: consolidation of IT Act 2000 + specific AI provisions pending. Expected to be comprehensive digital governance law covering AI, intermediary liability, online gaming, deepfake, etc. Draft under consultation.</li>"
         "<li><strong>Sector-specific AI frameworks</strong>:</li>"
         "<li>&nbsp;&nbsp;&mdash; <strong>RBI</strong>: AI/ML use in financial services - specific caution advisories; model risk management expectations.</li>"
         "<li>&nbsp;&nbsp;&mdash; <strong>SEBI</strong>: AI in securities markets - framework for AI-based advisory, algorithmic trading approval.</li>"
         "<li>&nbsp;&nbsp;&mdash; <strong>IRDAI</strong>: AI in insurance underwriting + claims - specific explainability requirements.</li>"
         "<li>&nbsp;&nbsp;&mdash; <strong>IndiaAI Mission (2024)</strong>: INR 10,372 crore outlay for compute infrastructure, model development, startup ecosystem. Mix of policy + capacity-building.</li>"
         "<li><strong>Copyright Act interaction</strong>: AI training on copyrighted data, output copyrightability - ongoing judicial consideration.</li>"
         "</ul>"),
        ("/ Specific obligations in 2026", "What's enforceable now.",
         "<ul>"
         "<li><strong>Deepfake labelling (MeitY March 2024)</strong>: AI-generated or AI-modified content must be labelled by intermediary platforms. Automated detection + removal mechanism required.</li>"
         "<li><strong>Large model registration (MeitY)</strong>: Specific generative AI models at defined threshold may require MeitY intimation / registration before deployment to Indian users.</li>"
         "<li><strong>Content moderation (IT Rules 2021 Amendment)</strong>: Intermediary rules require Indian representative appointment + content moderation framework + grievance redressal.</li>"
         "<li><strong>DPDP consent for AI training</strong>: using Indian user data for AI model training requires explicit consent under DPDP (purpose limitation + consent granularity).</li>"
         "<li><strong>Children's data (DPDP + MeitY advisories)</strong>: no behavioural monitoring + no targeted advertising + verifiable parental consent for AI products aimed at children.</li>"
         "<li><strong>Harmful content</strong>: AI-generated content causing harm (hate speech, misinformation, sexual content involving minors) attracts intermediary liability + IPC criminal consequences.</li>"
         "</ul>"),
        ("/ For foreign AI / GenAI companies in India", "The compliance stack.",
         "<ul>"
         "<li>Indian intermediary status under IT Act + Rules - likely applies to foreign AI product offering services to Indian users.</li>"
         "<li>Indian representative appointment (per IT Rules 2021 Amendment).</li>"
         "<li>DPDP compliance for processing Indian user data in training + inference.</li>"
         "<li>Content moderation framework compliant with Indian intermediary rules.</li>"
         "<li>Deepfake labelling on AI-generated / AI-modified content.</li>"
         "<li>Grievance redressal mechanism for Indian users.</li>"
         "<li>Sector-specific compliance if AI product deployed in regulated sectors (financial, insurance, securities, healthcare).</li>"
         "<li>Data localisation where applicable (RBI payment data, SEBI records).</li>"
         "<li>OIDAR GST if B2C paying Indian customers.</li>"
         "</ul>"),
        ("/ Looking ahead to DIA + comprehensive AI law", "What's coming.",
         "<ul>"
         "<li>Digital India Act (DIA) is expected to consolidate IT Act + specific AI/digital provisions. Draft under consultation; final enactment timeline uncertain (likely 2026-2027).</li>"
         "<li>Comprehensive AI-specific law (analogous to EU AI Act): under policy discussion. Likely risk-tiered (low / medium / high / unacceptable risk) similar to EU framework.</li>"
         "<li>Likely obligations in future comprehensive AI law: AI system registration, risk classification, impact assessment, transparency, accountability, red-teaming for high-risk AI, human oversight.</li>"
         "<li>Prudent approach for foreign AI companies: build on top of DPDP + MeitY + sector-specific frameworks now; expand to meet future comprehensive AI law when enacted.</li>"
         "</ul>"
         "<p><em>Last updated: 2026-10-22.</em></p>"),
    ],
    faqs=[
        ("Does India have a comprehensive AI-specific law?",
         "Not yet (October 2026). India's AI regulation is layered via multiple existing frameworks: MeitY advisories, DPDP Act 2023, sector-specific regulators (RBI, SEBI, IRDAI), IT Act 2000 + Intermediary Rules 2021. Comprehensive AI-specific law under policy discussion but no draft legislation yet. Digital India Act (DIA) draft would consolidate IT Act + specific AI provisions; enactment pending."),
        ("Does MeitY's deepfake advisory apply to foreign AI companies?",
         "Yes - intermediaries offering services to Indian users (including foreign AI companies) must label AI-generated / AI-modified content, provide automated detection + removal mechanism. MeitY March 2024 advisory remains in effect; subsequent advisories build on this framework. Non-compliance intermediary consequences under IT Act / IT Rules."),
        ("Can I use Indian user data to train my AI model without DPDP consent?",
         "No - DPDP Act requires lawful basis (consent or legitimate uses per Section 7) for processing personal data of Indian residents. AI model training on Indian user data = processing requiring either explicit consent (preferable) or justified legitimate use. Purpose limitation + consent granularity apply. Training on scraped Indian personal data without consent = DPDP breach + up to INR 250 crore penalty."),
        ("Is my foreign GenAI product deployment regulated in India?",
         "Depends on activity type + user base. Pure B2B API offering to Indian enterprise customers (who themselves handle end-user compliance) - lighter touch. B2C deployment to Indian consumers (chatbot, image generation, voice synthesis for Indian users): intermediary rules + DPDP + MeitY advisories + sector-specific if deployed in regulated sector. Appoint Indian representative + grievance officer; align content moderation."),
        ("How does India's AI regulation compare to EU AI Act?",
         "India: layered / sector-specific / principles-based (as of 2026). EU: comprehensive risk-tiered legislation. Convergence likely over time as India moves toward comprehensive AI law (via DIA + separate AI legislation). Prudent approach: EU AI Act-compliant foreign AI companies have strong foundation for India; India-specific adjustments needed for DPDP, intermediary rules, sector-specific frameworks."),
        ("Does BQP help foreign AI / GenAI companies with India compliance?",
         "Yes - DPDP applicability + consent flow + Data Protection Officer appointment, MeitY advisory compliance (deepfake labelling, large model registration), intermediary rules compliance (Indian representative + grievance officer + content moderation), sector-specific framework compliance (RBI / SEBI / IRDAI if applicable), OIDAR GST registration, data localisation architecture advisory. Integrated compliance stack. WhatsApp +91 78018 87130."),
    ],
    related=[
        ("dpdp-act-india-foreign-company-compliance-2026.html", "Guide", "DPDP Act"),
        ("india-data-localisation-rbi-dpdp-foreign-saas.html", "Guide", "Data Localisation"),
    ],
    cta_headline="Foreign AI / GenAI product serving Indian users?",
    cta_body="Layered compliance: DPDP + MeitY + intermediary rules + sector-specific. BQP integrated AI compliance stack. Scope-based engagement + co-ordinated with foreign AI counsel.",
))

# 12. Rule 9B anniversary
write_page("rule-9b-dematerialisation-2-year-anniversary-october-2026", page(
    slug="rule-9b-dematerialisation-2-year-anniversary-october-2026",
    title="Rule 9B Demat Unlisted Shares 2-Year Anniversary October 2026 - BQP",
    description="MCA Rule 9B mandatory dematerialisation of unlisted shares 2-year anniversary October 2026: current compliance state across private limited companies, pending demat count estimate, enforcement actions seen, Form PAS-6 half-yearly compliance maturity, M&A impact. Status update + remediation framework. Working CA guide by Durgesh Chavda.",
    keywords="Rule 9B anniversary October 2026, demat unlisted shares status, Rule 9B enforcement India 2026, Form PAS-6 compliance maturity",
    hero_kicker="/ Rule 9B Status Update &middot; Updated 2026-10-22",
    hero_title_html="Rule 9B 2 years on, <em>where private companies actually are.</em>",
    hero_lead="MCA Rule 9B (mandatory dematerialisation of unlisted company shares) became effective for private limited companies from October 2024 (post extensions). October 2026 marks 2-year anniversary. Significant number of private limited companies still non-compliant - creating transaction / fundraising / M&A friction. Here's the current state as of October 2026 and the remediation path.",
    sections=[
        ("/ Current compliance state", "What we're seeing on the ground.",
         "<ul>"
         "<li><strong>Fully compliant private companies</strong>: well-funded startups + mid-size companies with institutional investors - typically 100% complete.</li>"
         "<li><strong>Partially compliant</strong>: shares of founders / core team demat; angel investor shares still physical (because investor non-responsive to demat request).</li>"
         "<li><strong>Entirely non-compliant</strong>: smaller family-held private limited companies, older companies with scattered small shareholders - likely 30-40% of eligible companies still have non-demat shares.</li>"
         "<li><strong>Enforcement</strong>: ROC filing blocks (DIR-12, PAS-3) + Section 450 default penalty + inability to complete share transfer / allotment / buyback / transmission.</li>"
         "<li><strong>Transaction friction</strong>: M&A deals delayed by 30-60 days when target hasn't demat'd pre-closing. Fundraising rounds blocked when new allotment can't be made in physical form.</li>"
         "</ul>"),
        ("/ Who's exempt (recap)", "The scope.",
         "<ul>"
         "<li><strong>Small companies</strong>: paid-up capital up to INR 4 crore + turnover up to INR 40 crore (Section 2(85)). Growth-stage startups cross this threshold quickly.</li>"
         "<li><strong>Government companies</strong>.</li>"
         "<li><strong>Nidhi companies</strong>.</li>"
         "<li>Everyone else: in scope under Rule 9B.</li>"
         "</ul>"),
        ("/ Form PAS-6 half-yearly compliance", "The ongoing filing.",
         "<ul>"
         "<li><strong>Form PAS-6</strong>: Reconciliation of Share Capital Audit Report. Half-yearly filing within 60 days of each half-year end (30 September + 31 March).</li>"
         "<li>For companies in demat form, Form PAS-6 is now mandatory. Many companies have missed FY 2024-25 + 2025-26 PAS-6 filings - creating late fee exposure under Section 47.</li>"
         "<li>CA certification of PAS-6 as prescribed in the form.</li>"
         "<li>October 2026: September 2026 half-year PAS-6 due by 29 November 2026.</li>"
         "</ul>"),
        ("/ Remediation path for non-compliant companies", "90-day execution plan.",
         "<ol>"
         "<li><strong>Compliance gap assessment</strong>: review existing shareholder list; identify physical-share holders.</li>"
         "<li><strong>ISIN application</strong>: via Registrar &amp; Transfer Agent (RTA) to NSDL / CDSL. 15-30 day approval.</li>"
         "<li><strong>Depository Participant (DP) appointment</strong>: company's DP for facilitating demat.</li>"
         "<li><strong>Shareholder communication</strong>: formal letter + email + phone follow-up to all physical-share holders. Standard templates + repeat follow-ups.</li>"
         "<li><strong>Shareholder's demat account opening + DRF submission</strong>: shareholders open demat with their respective DPs; submit Dematerialisation Request Form + physical share certificate.</li>"
         "<li><strong>Company RTA verification + demat confirmation</strong>: RTA matches share certificate + confirms demat.</li>"
         "<li><strong>Physical certificates cancellation</strong>.</li>"
         "<li><strong>Form PAS-6 half-yearly filing</strong> catching up on missed periods.</li>"
         "<li><strong>Lost certificate issuance under Rule 6</strong>: for lost / destroyed certificates - public notice + indemnity bond + Rule 6 cert.</li>"
         "<li><strong>Unresponsive shareholder documentation</strong>: RPAD letters + emails + newspaper notice attempts documented.</li>"
         "</ol>"
         "<p>Typical remediation timeline: 60-120 days depending on shareholder count + responsiveness.</p>"),
        ("/ M&A + fundraising-specific attention", "Pre-closing clean-up.",
         "<ul>"
         "<li><strong>Target company pre-M&A diligence</strong>: buyer's DD will surface Rule 9B non-compliance. Deal pauses until target completes demat (30-60 day delay).</li>"
         "<li><strong>Series A / B / C pre-money</strong>: new allotment to investor must be in demat form (Rule 9B). If company isn't demat'd, round delays.</li>"
         "<li><strong>IPO pre-filing</strong>: Rule 9B + SEBI pre-IPO demat required. Must be fully demat before DRHP.</li>"
         "<li><strong>Secondary sale</strong>: founder / angel exit cannot complete via physical share transfer. Buyer insists on demat first.</li>"
         "<li>Pre-emptive demat is the easy path; reactive demat under transaction time pressure is the hard path.</li>"
         "</ul>"
         "<p><em>Last updated: 2026-10-22.</em></p>"),
    ],
    faqs=[
        ("What's the current state of Rule 9B compliance in October 2026?",
         "Mixed. Well-funded startups + mid-size institutional-backed companies typically fully compliant. Smaller family-held + older private companies with scattered shareholders - still 30-40% non-compliant. Form PAS-6 half-yearly filing has caught up for compliant companies; non-compliant companies face late fee + Section 450 default penalty exposure."),
        ("What transactions does Rule 9B block for non-compliant companies?",
         "New share allotment (fundraising, ESOP exercise), share transfer (M&A, secondary sale, founder exit), buyback, transmission (on shareholder death), bonus / rights issue. Essentially every cap table change. Also: Form PAS-6 half-yearly filing mandatory for companies in demat scope - non-filing attracts Section 47 late fee + Section 450 continuing default penalty."),
        ("Can a Series A investor insist on target company demat before investing?",
         "Yes - standard practice now in 2026. Series A term sheet typically includes closing condition: 'Target to complete dematerialisation of all outstanding shares under Rule 9B before Closing'. Target company must execute demat (30-60 days) before investor's funds flow. Material deal timing impact if left to last minute."),
        ("What if a shareholder refuses to demat?",
         "Company documents attempts (RPAD letters, emails, newspaper notice, phone follow-ups). Share remains physical in that shareholder's name but company's Rule 9B obligation is to facilitate demat, not force it. For future share transfer / allotment: that specific shareholder's shares will not be transferable until they demat. Compliance posture: company has demonstrated reasonable efforts."),
        ("Does BQP help with Rule 9B remediation + PAS-6?",
         "Yes - compliance gap assessment, ISIN application via RTA, DP appointment, shareholder communication (standard templates + follow-ups), demat execution co-ordination, Form PAS-6 half-yearly filing + catch-up on missed periods, lost certificate Rule 6 handling, unresponsive shareholder documentation. Standard engagement for private companies with 20-500+ shareholders. WhatsApp +91 78018 87130."),
    ],
    related=[
        ("dematerialisation-unlisted-shares-india-mandatory.html", "Guide", "Rule 9B Full Guide"),
        ("company-secretarial-services-india-remote.html", "Guide", "CS Services"),
    ],
    cta_headline="Rule 9B 2 years on. Still have physical-share holders?",
    cta_body="Blocks every cap table change: allotment, transfer, buyback, transmission. BQP 60-120 day remediation + ongoing PAS-6 compliance.",
))

# 13. GIFT City expansion
write_page("gift-city-expansion-2026-new-tenants-ifsca-reforms", page(
    slug="gift-city-expansion-2026-new-tenants-ifsca-reforms",
    title="GIFT City Expansion 2026 | New Tenants + IFSCA Reforms - BQP",
    description="GIFT City IFSC expansion October 2026 update: new tenant arrivals (major Indian + international AIFs, foreign banks, insurance), IFSCA regulatory reforms (expanded AIF framework, new product categories, bullion exchange), Section 10(4D) tax regime maturity, Dholera semiconductor cluster complementing GIFT City finance. Working CA guide by Durgesh Chavda.",
    keywords="GIFT City expansion 2026, IFSCA reforms India, GIFT City new AIF 2026, Dholera GIFT City complementarity, Section 10(4D) GIFT City",
    hero_kicker="/ GIFT City Status &middot; Updated 2026-10-22",
    hero_title_html="GIFT City 2026, <em>new tenants + IFSCA reforms.</em>",
    hero_lead="GIFT City (Gujarat International Finance Tec-City) IFSC has grown substantially since 2022-2023 initial scaling. As of October 2026: 500+ IFSC entities (AIFs, banks, insurance, broking, reinsurance), several hundred-billion dollar AUM, new product categories operational via IFSCA regulations. Here's the current state + what new foreign + Indian financial-sector entrants should know.",
    sections=[
        ("/ Current state in Q4 2026", "The ecosystem.",
         "<ul>"
         "<li><strong>500+ IFSC entities operational</strong>: alternative investment funds, foreign bank branches, insurance intermediaries, broker-dealers, re-insurers, finance companies, aircraft leasing, ship leasing, bullion exchange.</li>"
         "<li><strong>Several hundred billion USD AUM</strong> across IFSC AIFs + banks + related products.</li>"
         "<li><strong>Resident entity cost base</strong>: office space + manpower materially cheaper than Mumbai / Bengaluru / Singapore equivalent. Tax regime (Section 10(4D)) adds further advantage.</li>"
         "<li><strong>Infrastructure</strong>: fully operational since early 2020s; now mature.</li>"
         "<li><strong>Regulatory stability</strong>: IFSCA (International Financial Services Centres Authority) established 2020; now mature with specific regulations for each product.</li>"
         "</ul>"),
        ("/ Key IFSCA regulatory reforms 2024-2026", "What's changed.",
         "<ul>"
         "<li><strong>Expanded AIF framework</strong>: new fund categories permitted; retail AIF discussions; INR-INR AIF framework (previously limited to foreign currency denomination).</li>"
         "<li><strong>Family office framework</strong>: specific IFSCA rules for family offices operating from GIFT City.</li>"
         "<li><strong>IBU (IFSC Banking Unit) expansion</strong>: more Indian + foreign banks setting up IBU - cross-border lending, treasury, trade finance.</li>"
         "<li><strong>Insurance + re-insurance</strong>: expanded IRDAI-IFSCA framework for cross-border insurance; Indian re-insurer and foreign re-insurer presence.</li>"
         "<li><strong>Fintech sandbox</strong>: specific IFSCA fintech sandbox for cross-border fintech experimentation.</li>"
         "<li><strong>Aircraft + ship leasing</strong>: dedicated regulatory framework; several lessors operational.</li>"
         "<li><strong>Bullion Exchange</strong>: IIBX operational; foreign bullion inflows + Indian jewellery sector integration.</li>"
         "<li><strong>Ancillary services</strong>: expanded scope for law firm presence, accounting / consulting firm presence, R&amp;D centre presence.</li>"
         "</ul>"),
        ("/ Tax regime maturity", "Section 10(4D) + related.",
         "<ul>"
         "<li><strong>Section 10(4D)</strong>: specified income of specified fund (including Category III AIF) in IFSC - exempt. Covers capital gain, dividend, interest - subject to conditions.</li>"
         "<li><strong>Section 115U / 115UA</strong>: pass-through for Category I + II AIFs.</li>"
         "<li><strong>Dividend from Indian company</strong>: specific carve-outs for IFSC fund.</li>"
         "<li><strong>GST</strong>: specific exemptions for IFSC services; co-ordinated with CGST Act.</li>"
         "<li><strong>Stamp duty</strong>: Gujarat state exemption for IFSC entities on specific instruments.</li>"
         "<li><strong>BEPS Pillar 2 interaction</strong>: Section 10(4D) exemption creates low Pillar 2 ETR risk for in-scope groups; QDMTT top-up may apply. See <a href='beps-pillar-2-india-implementation-october-2026-update.html'>Pillar 2 guide</a>.</li>"
         "</ul>"),
        ("/ For foreign + Indian entrants", "Decision factors.",
         "<ul>"
         "<li><strong>Foreign asset manager</strong>: IFSC AIF structure provides LP-friendly tax regime + regulatory arbitrage vs Mumbai AIF.</li>"
         "<li><strong>Indian family office</strong>: specific IFSCA family office framework + cross-border investment flexibility.</li>"
         "<li><strong>Indian reinsurer</strong>: cross-border insurance via IFSC with specific regulatory + tax regime.</li>"
         "<li><strong>Foreign fintech</strong>: fintech sandbox for cross-border experimentation + eventual full IFSC licence.</li>"
         "<li><strong>Aircraft lessor</strong>: dedicated regulatory framework + Indian + foreign airline customer base.</li>"
         "<li><strong>Bullion dealer</strong>: IIBX membership + import channel optimisation.</li>"
         "<li><strong>Service provider (law / consulting / audit)</strong>: ancillary services licence to serve IFSC entities.</li>"
         "</ul>"
         "<p><em>Last updated: 2026-10-22.</em></p>"),
    ],
    faqs=[
        ("What's the current state of GIFT City IFSC in October 2026?",
         "Mature ecosystem - 500+ IFSC entities operational across AIFs, foreign banks, insurance, broker-dealers, reinsurance, bullion exchange, aircraft/ship leasing. Several hundred billion USD AUM. IFSCA regulatory framework mature with specific rules for each product category. Resident entity cost base + tax regime (Section 10(4D)) remains advantageous vs Mumbai / Bengaluru / Singapore equivalents."),
        ("What recent IFSCA reforms affect foreign entrants?",
         "Expanded AIF framework (new fund categories + INR denomination), family office framework, IBU (IFSC Banking Unit) expansion for Indian + foreign banks, insurance + reinsurance expansion, fintech sandbox for cross-border experimentation, aircraft + ship leasing frameworks, Bullion Exchange (IIBX) operational, ancillary services (law + consulting) expanded scope."),
        ("How does Section 10(4D) interact with BEPS Pillar 2?",
         "Section 10(4D) provides tax exemption for specified income of IFSC fund - resulting in low Pillar 2 ETR for groups using IFSC. For in-scope MNC groups (consolidated revenue EUR 750M+), QDMTT (Qualified Domestic Minimum Top-up Tax) may apply to raise Indian ETR to 15% minimum. Impact: GIFT City tax advantage preserved for small/mid groups; large groups face Pillar 2 top-up."),
        ("Can a foreign asset manager run an IFSC AIF without Indian presence?",
         "No - IFSC AIF must have Indian-incorporated AMC / Investment Manager + Indian trustee + Indian fund as the SPV. Foreign asset manager typically owns 100% of Indian AMC (which is IFSC-registered). Combined with offshore feeder fund (Mauritius / Singapore) for international LPs, full cross-border structure operational."),
        ("What's the fastest way to enter GIFT City for a foreign entity?",
         "Depends on activity: Fintech sandbox (6-12 months to first product launch); IFSC AIF (3-6 months for fund formation + SEBI AIF + IFSCA approvals); Aircraft lessor (3-6 months); Family office (2-4 months); IBU (bank branch - 6-12 months). BQP coordinates incorporation + licensing + ongoing compliance."),
        ("Does BQP handle GIFT City IFSC entity setup?",
         "Yes - specialist IFSC practice. Entity structure selection + incorporation (SPICe+ + IFSCA registration) + sector-specific licence application + Section 10(4D) optimisation + Pillar 2 QDMTT impact analysis + ongoing fund accounting + regulatory reporting. Co-ordinated with Indian regulatory counsel + Gujarat state liaison. WhatsApp +91 78018 87130."),
    ],
    related=[
        ("gift-city.html", "Service", "GIFT City Service"),
        ("gift-city-section-10-4d-2026-update.html", "Guide", "Section 10(4D) Guide"),
    ],
    cta_headline="GIFT City IFSC - mature ecosystem, multiple product frameworks live.",
    cta_body="AIF / family office / IBU / insurance / fintech sandbox / aircraft lessor / bullion / ancillary services. BQP end-to-end: structure + licence + Section 10(4D) + Pillar 2 integration + ongoing.",
))

# 14. Section 148 season
write_page("section-148-reassessment-season-november-december-2026", page(
    slug="section-148-reassessment-season-november-december-2026",
    title="Section 148 Reassessment Season November-December 2026 - BQP",
    description="Section 148 / 148A reassessment season November-December 2026: AO sending Section 148A(b) show-cause notices for AY 2019-20 / 2020-21 before March 2027 limitation, 10-year lookback for asset-form escaped income above INR 50 lakh, response strategy, writ in High Court if 148A defective, Section 270A under vs mis reporting defence. Working CA guide by Durgesh Chavda.",
    keywords="Section 148 reassessment season November 2026, 148A show cause notice AY 2019-20, Section 148 limitation March 2027, 10 year reassessment India 2026",
    hero_kicker="/ Reassessment Season Alert &middot; Updated 2026-10-22",
    hero_title_html="Section 148 reassessment season, <em>Nov-Dec 2026 wave is here.</em>",
    hero_lead="November-December is India's traditional reassessment-notice season. AOs rushing to issue Section 148A(b) show-cause notices for AY 2019-20 (standard 4-year window closing March 2027) and AY 2015-16 / 2016-17 (10-year window for asset-form escaped income above INR 50 lakh). If you've received a Section 148A(b) notice, the response window is 7-30 days. Here's exactly what to do.",
    sections=[
        ("/ The current season context", "Why November-December.",
         "<ul>"
         "<li><strong>AY 2019-20 standard 4-year limit</strong>: closing on 31 March 2027. AOs issuing 148A(b) before year-end to preserve option to proceed to Section 148 before limitation.</li>"
         "<li><strong>AY 2015-16 / 2016-17 10-year extended limit</strong>: applicable where escaped income is INR 50 lakh+ in asset form. AOs reviewing CBDT risk-based selection + FTA (Foreign Tax Authority) exchange data + search cases.</li>"
         "<li><strong>Data sources driving notices</strong>: SFT (Statement of Financial Transactions), AIS / TIS mismatches, international tax exchange, specific industry audits, informant reports.</li>"
         "<li><strong>Volume</strong>: significant volume of 148A(b) notices issued each November-December season. Many are mechanical and quashable.</li>"
         "</ul>"),
        ("/ Section 148A procedure recap", "Finance Act 2021 framework.",
         "<ol>"
         "<li><strong>AO has information</strong> suggesting income escaping assessment (SFT, AIS mismatch, international exchange, search output).</li>"
         "<li><strong>Section 148A(a) enquiry</strong>: optional - AO may make preliminary enquiry.</li>"
         "<li><strong>Section 148A(b) show-cause notice</strong>: AO issues formal show-cause with the 'information' it relies on + proposed grounds. Response window 7-30 days.</li>"
         "<li><strong>Taxpayer's response</strong>: can refute information, present mitigating facts, argue jurisdictional defects.</li>"
         "<li><strong>Section 148A(d) order</strong>: AO decides whether to proceed. Must consider taxpayer's response.</li>"
         "<li><strong>Section 148 formal notice</strong>: if AO proceeds, formal reassessment notice issued. Taxpayer must file return.</li>"
         "<li><strong>Section 147 reassessment</strong>: regular assessment follows.</li>"
         "<li><strong>Section 147 order appealable</strong> to CIT(A) within 30 days.</li>"
         "</ol>"),
        ("/ Response strategy", "Step-by-step playbook.",
         "<ol>"
         "<li><strong>Immediate action (Day 1)</strong>: acknowledge notice; note exact response deadline; preserve all records relevant to the year in question.</li>"
         "<li><strong>Information review (Day 1-3)</strong>: analyse exactly what information AO relies on. RTI request for complete file if needed.</li>"
         "<li><strong>Classification review (Day 3-5)</strong>: is this a mechanical notice (easy to quash) or substantive issue (need defence)?</li>"
         "<li><strong>Legal grounds assessment</strong>:</li>"
         "<li>&nbsp;&nbsp;&mdash; Jurisdictional: 4-year vs 10-year limit, Section 148A procedure defects.</li>"
         "<li>&nbsp;&nbsp;&mdash; Substantive: income was already disclosed, SFT misreporting, duplicate counting, non-taxable receipt (gift, inheritance, exempt).</li>"
         "<li>&nbsp;&nbsp;&mdash; Treaty: DTAA relief available, foreign tax credit, treaty-residence tie-breaker.</li>"
         "<li><strong>Documentary refutation</strong>: ITR extract showing disclosed income, bank statements, agreements, Section 50C compliance docs, Section 56(2)(x) relative gift docs.</li>"
         "<li><strong>Section 148A(b) response drafting</strong>: comprehensive written response with annexures.</li>"
         "<li><strong>Submission on income tax portal</strong>: electronic filing before deadline.</li>"
         "<li><strong>Follow-up</strong>: await Section 148A(d) order. If favourable: closure. If adverse: Section 148 notice follows.</li>"
         "<li><strong>Writ in High Court</strong>: if Section 148A procedure fundamentally defective, consider writ petition.</li>"
         "</ol>"),
        ("/ Specific issues this season", "What AOs are focused on.",
         "<ul>"
         "<li><strong>Foreign asset disclosure gaps</strong>: FTA exchange data + Schedule FA mismatches. US + UK + Singapore + UAE financial institutions sharing with Indian tax authority under CRS / FATCA.</li>"
         "<li><strong>Real estate transactions</strong>: SFT reports of large property purchases / sales (Form 61A) not reflected in ITR capital gain.</li>"
         "<li><strong>Share transactions</strong>: Form 61A reports of large securities transactions not reflected in capital gain disclosure.</li>"
         "<li><strong>Cash deposits</strong>: large cash deposits reported via SFT.</li>"
         "<li><strong>Business receipt gaps</strong>: TDS / TCS discrepancy with ITR revenue.</li>"
         "<li><strong>Trust / family structures</strong>: foreign trust distributions, private trust income allocation.</li>"
         "</ul>"
         "<p><em>Last updated: 2026-10-22.</em></p>"),
    ],
    faqs=[
        ("Why is November-December reassessment-notice season in India?",
         "AO's 4-year standard reassessment limitation closes on 31 March for the AY that becomes 4 years old. For AY 2019-20, limitation closes 31 March 2027. AOs issue Section 148A(b) show-cause notices in late Q4 2026 and Q1 2027 to preserve the option to proceed to Section 148 within the window. Same pattern applies to 10-year extended limit for high-value asset-form escaped income cases."),
        ("What's the response window for Section 148A(b)?",
         "Typically 7-30 days from receipt of show-cause notice. Specific days specified in notice. Extensions sometimes granted on reasoned request. Critical to respond within window - no response = AO proceeds to Section 148A(d) order with only AO's version considered."),
        ("Can Section 148A(b) notice be quashed?",
         "Yes - via writ in High Court if procedure fundamentally defective (no proper 'information', mechanical satisfaction, pre-decided outcome, no genuine opportunity to respond). Several High Court rulings have struck down defective 148A proceedings. For substantive but weak notices, Section 148A(b) response itself can achieve dismissal at 148A(d) stage without High Court involvement."),
        ("What if the 'escaped income' is actually already disclosed?",
         "This is one of the most common defences. Produce ITR Schedule showing the income reported. Cross-reference with Form 26AS / AIS / TIS. Documentary proof of disclosure in prior year ITR. If AO's SFT data duplicates already-disclosed income, response conclusively establishes no escape."),
        ("What's the penalty if Section 148 reassessment confirms escaped income?",
         "Section 270A: 50% penalty for under-reporting (good faith) OR 200% penalty for misreporting (fraud / wilful concealment). Classification is a key battle in reassessment. Section 270AA voluntary disclosure provision can avoid 200% rate. CIT(A) + ITAT appeal paths available."),
        ("Does BQP handle Section 148 / 148A response urgently?",
         "Yes - specialised urgent service during November-December reassessment season. Immediate response team: notice review + information analysis + documentary refutation + legal grounds assessment + Section 148A(b) response drafting + e-filing + Section 148A(d) order follow-up + Section 148 reassessment representation if proceeds + CIT(A) appeal if adverse. 7-30 day response windows handled urgently. WhatsApp +91 78018 87130."),
    ],
    related=[
        ("section-148-148a-reassessment-notice-response-india.html", "Guide", "Section 148 / 148A Full Guide"),
        ("best-ca-section-148-reassessment-notice-response.html", "Guide", "Best CA for 148 Response"),
    ],
    cta_headline="Received Section 148A(b) show-cause notice?",
    cta_body="7-30 day window. First response often decides the proceeding. BQP urgent response team: notice analysis + refutation + e-filing within window. Scope-based engagement.",
))

# 15. Tax audit followups
write_page("tax-audit-season-november-2026-post-filing-followups", page(
    slug="tax-audit-season-november-2026-post-filing-followups",
    title="Tax Audit Season November 2026 Post-Filing Follow-ups - BQP",
    description="Post Tax Audit filing (31 October 2026 deadline) November follow-ups: Form 3CA/3CB + 3CD common issues, Section 43B(h) MSE reporting Year 2, Clause 44 GST + Income Tax reconciliation, specified financial transactions reconciliation, Form 3CEB TP audit (30 November deadline), AY 2026-27 ITR Nov-Dec filing coordination. CA Durgesh Chavda complete 2026 guide.",
    keywords="tax audit season November 2026 followups, Form 3CA 3CD common issues 2026, Section 43B(h) tax audit, Form 3CEB TP audit November, AY 2026-27 ITR tax audit",
    hero_kicker="/ Tax Audit Post-Filing &middot; Updated 2026-10-22",
    hero_title_html="Tax audit filed, <em>November follow-ups to execute.</em>",
    hero_lead="Tax audit (Section 44AB) for AY 2026-27 was due 31 October 2026 for most assessees + 30 November 2026 for Form 3CEB TP audit cases. Post-filing, several follow-up actions are critical: ITR coordination (ITR-3 / ITR-5 / ITR-6 due 31 October / 30 November / 31 December), 43B(h) Year 2 handling, Clause 44 reconciliation review, specified financial transaction documentation. Here's the November-December follow-up playbook.",
    sections=[
        ("/ Post-Filing Reconciliation", "What to verify.",
         "<ul>"
         "<li><strong>Form 3CA/3CB signed + e-filed</strong>: tax auditor's audit report signed and e-filed on income tax portal.</li>"
         "<li><strong>Form 3CD + 44 Clauses verification</strong>: specific Clause 20 (Section 40(a) / 40A payments), Clause 22 (43B / 43B(h) MSE), Clause 32 (specified financial transactions), Clause 34 (Chapter XVII-B TDS), Clause 44 (GST reconciliation).</li>"
         "<li><strong>CA signature + membership verification</strong>: ICAI UDIN (Unique Document Identification Number) generated for the audit report.</li>"
         "<li><strong>Supporting workpapers</strong>: in audit firm's file (preserved 8 years).</li>"
         "</ul>"),
        ("/ Clause 22 Section 43B(h) specific review", "The year-2 critical clause.",
         "<ul>"
         "<li><strong>Clause 22 expanded (post Finance Act 2023)</strong>: specific line items for Section 43B(h) MSE disallowance + amounts paid in subsequent FY (reversal from prior year).</li>"
         "<li>Common error: not identifying Micro + Small enterprise suppliers; treating all suppliers as outside 43B(h) scope. Udyam certificate collection becomes compliance signal.</li>"
         "<li>Reconciliation: 43B(h) disallowance in current year + 43B(h) reversal from prior year payment = net 43B(h) impact on current-year taxable income.</li>"
         "<li>Documentation: Udyam certificates for each MSE supplier + payment date tracking + 45-day calculation per invoice.</li>"
         "</ul>"),
        ("/ Clause 44 GST reconciliation", "The GST-Income Tax interface.",
         "<ul>"
         "<li>Clause 44 requires reconciliation of Income Tax turnover with GST turnover (as per GSTR-1 + GSTR-9).</li>"
         "<li>Common differences: credit notes / debit notes timing, year-end sales returns, GSTR-1 vs 3B gaps, exempt supplies not in Income Tax but in GST, specific adjustments like discounts.</li>"
         "<li>Narrative explanation for each unreconciled item.</li>"
         "<li>Feeds into GSTR-9 Reconciliation (31 December 2026) + GSTR-9C Part II / III.</li>"
         "</ul>"),
        ("/ Form 3CEB TP audit (30 November 2026)", "The next deadline.",
         "<ul>"
         "<li>Form 3CEB applicable for any Indian company with international transactions above INR 1 crore (effectively every foreign-subsidiary subsidiary of Indian group).</li>"
         "<li>Deadline: 30 November 2026 for AY 2026-27.</li>"
         "<li>Content: all international transactions listed with each AE + nature + value + arm's-length method + benchmarking.</li>"
         "<li>Underlying documentation (Section 92D): entity profile + industry analysis + functional analysis + economic analysis + benchmarking study. Not filed but produced on scrutiny.</li>"
         "<li>Master File (Form 3CEAA) for groups above INR 500 crore + CbCR (Form 3CEAD) for ultimate parent of groups above EUR 750M.</li>"
         "</ul>"),
        ("/ ITR filing coordination", "The November-December window.",
         "<ul>"
         "<li><strong>ITR-5 / ITR-6 / ITR-3</strong> (tax audit cases): due 31 October 2026 (standard) or 30 November 2026 if TP audit applicable.</li>"
         "<li>ITR must reflect Form 3CD disclosures (43B(h), Section 40(a), Chapter XVII-B TDS, specified financial transactions).</li>"
         "<li>Advance tax Q3 (15 December 2026) coordination.</li>"
         "<li>Belated return window: 31 December 2026.</li>"
         "<li>Updated return window (Section 139(8A)): up to 31 March 2027 for AY 2026-27, with additional tax.</li>"
         "</ul>"),
        ("/ Common November post-filing attention", "What to check.",
         "<ul>"
         "<li>Form 3CA/3CB status on portal: accepted / rejected / pending.</li>"
         "<li>UDIN verification against ICAI records.</li>"
         "<li>Form 3CD Clause 22 (43B(h)) + Clause 44 (GST reconciliation) + Clause 34 (TDS) coherence.</li>"
         "<li>Specified financial transaction disclosure (Clause 32) matching Form 61A reports.</li>"
         "<li>Pending Section 148A(b) notices from November-December 2026 reassessment season - urgent response.</li>"
         "<li>Advance tax Q3 (15 December) computation based on finalised audited financials.</li>"
         "<li>GSTR-9 FY 2025-26 preparation (due 31 December 2026).</li>"
         "<li><em>Last updated: 2026-10-22.</em></p>"),
    ],
    faqs=[
        ("What follow-ups are critical after tax audit filing on 31 October?",
         "Form 3CA/3CB status verification on portal, UDIN check against ICAI records, Form 3CD Clause-by-Clause coherence (especially 22, 32, 34, 44), coordination with ITR filing (30 November TP cases, 31 October standard), 43B(h) MSE reversal tracking, Clause 44 GST reconciliation feeding into GSTR-9 (December 2026), advance tax Q3 (15 December), Form 3CEB TP audit (30 November)."),
        ("Is Form 3CEB TP audit also due on 31 October?",
         "No - Form 3CEB has its own deadline: 30 November 2026 for AY 2026-27 (one month after standard tax audit). Mandatory for any Indian subsidiary / company with international transactions above INR 1 crore. Benchmarking study + comparability analysis underlying + Master File + CbCR for in-scope groups."),
        ("What's Clause 44 of Form 3CD?",
         "Clause 44 requires reconciliation of Income Tax turnover with GST turnover (as per GSTR-1 + GSTR-9). Line-by-line explanation of differences: credit notes timing, exempt supplies, year-end adjustments, discounts. Feeds into GSTR-9 reconciliation (December 2026). Common area of discrepancy requiring narrative."),
        ("How does Section 43B(h) show up in Form 3CD?",
         "Clause 22 (expanded post Finance Act 2023): specific line items for amounts disallowed under 43B(h) in current year (MSE payment beyond 45 days) + amounts paid in current year where disallowance was reversed from prior year. Documented with Udyam certificates + invoice-level 45-day calculation."),
        ("What happens if Form 3CA/3CB wasn't filed by 31 October?",
         "ITR filing blocked - cannot e-file ITR without Form 3CA/3CB linked on portal. Late filing fee under Section 234F: INR 5,000 (reduced to INR 1,000 for small income). Section 271B penalty for late tax audit: 0.5% of turnover or INR 1,50,000 whichever less. Belated filing possible but with penalties."),
        ("Does BQP handle tax audit + ITR + TP audit integrated engagement?",
         "Yes - integrated November-December engagement. Tax audit Form 3CA/3CB/3CD + ITR filing + Form 3CEB TP audit + Master File + CbCR + GSTR-9 preparation + advance tax Q3 + Section 148 response if any notice received. Priority turnaround through November-December 2026 deadline cluster. WhatsApp +91 78018 87130."),
    ],
    related=[
        ("ay-2026-27-itr-forms-new-disclosures-india.html", "Guide", "AY 2026-27 ITR"),
        ("transfer-pricing-india-foreign-mnc.html", "Guide", "TP Form 3CEB"),
    ],
    cta_headline="Tax audit filed. November-December follow-ups now.",
    cta_body="Form 3CEB TP (30 Nov) + ITR (31 Oct/30 Nov) + Advance Tax Q3 (15 Dec) + GSTR-9 (31 Dec). BQP integrated engagement + priority turnaround.",
))

# ============ 7 CITY SEO PAGES ============

def city_page(slug, city, specialty, title_specialty, desc_specialty, keywords):
    return page(
        slug=slug,
        title=f"Best CA Firm in {city} for {title_specialty} 2026 - BQP",
        description=f"Best CA firm in {city} for {desc_specialty}: Bharat Quantum Prospera (CA Durgesh Chavda, ICAI) delivers specialist services from Ahmedabad, Mumbai, Bengaluru, Rajkot, Dubai offices + remote delivery for {city}-based clients. Scope-based engagement. WhatsApp +91 78018 87130.",
        keywords=keywords,
        hero_kicker=f"/ {city} CA Firm &middot; {specialty} &middot; Updated 2026-10-22",
        hero_title_html=f"Best CA firm in {city} for <em>{title_specialty.lower()}.</em>",
        hero_lead=f"<strong>Short answer</strong>: Bharat Quantum Prospera (BQP). CA Durgesh Chavda-led, ICAI-qualified. 5 offices (Ahmedabad, Mumbai, Bengaluru, Rajkot, Dubai) + remote delivery for {city}-based clients. Specialist practice in {desc_specialty}. 300+ working guides. Scope-based transparent engagement. Here's why we're the practical answer for {city} clients needing this specific advisory.",
        sections=[
            ("/ Why BQP for {city}".replace("{city}", city), "Our value for this geography.",
             f"<ul>"
             f"<li><strong>Specialist practice</strong> in {desc_specialty} &mdash; not a generalist CA firm with many service lines spread thin.</li>"
             f"<li><strong>Remote delivery</strong> &mdash; {city}-based client doesn't need to visit any BQP office; all engagement via Zoom + cloud-shared workspace.</li>"
             f"<li><strong>CA Durgesh Chavda personally runs mandates</strong> &mdash; not handed off to junior staff. ICAI-qualified Chartered Accountant.</li>"
             f"<li><strong>Transparent scoped engagement</strong> &mdash; fixed-scope + fixed-fee letter upfront; no hourly billing surprises.</li>"
             f"<li><strong>Integrated firm</strong> &mdash; CA + CS + tax + legal + strategy under one firm. No coordination overhead across multiple firms.</li>"
             f"<li><strong>Multi-standard competence</strong> &mdash; US GAAP + IFRS + Ind AS + Australian AASB + UK FRS. Cross-standard reconciliation standard.</li>"
             f"</ul>"),
            ("/ What we deliver for {city} clients".replace("{city}", city), f"Scope of {specialty.lower()} engagement.",
             f"<p>Our standard {specialty.lower()} engagement for {city}-based clients covers:</p>"
             f"<ul>"
             f"<li>Scoping call (30-min, Zoom, no obligation) to understand your specific situation.</li>"
             f"<li>Scoped quote within 48 hours.</li>"
             f"<li>Signed engagement letter remotely.</li>"
             f"<li>Weekly status call during delivery.</li>"
             f"<li>Deliverables in your preferred format (PDF / Word / Excel / Google Workspace / Microsoft 365).</li>"
             f"<li>Post-delivery 30-day Q&amp;A window.</li>"
             f"<li>Ongoing retainer available where applicable.</li>"
             f"</ul>"
             f"<p>For {city} clients specifically: all engagement runs remotely. We service clients across India + 20+ foreign countries without geographic constraint.</p>"),
            ("/ Why not a {city}-based CA firm".replace("{city}", city), "The specialist vs generalist choice.",
             f"<p>Many {city} clients first consider local {city}-based CA firms. For general-purpose compliance (standard ITR + GST filings + ROC compliance), local CA may be sufficient. For specialist advisory in <strong>{desc_specialty}</strong>, specialist firm often provides better depth. Reasons:</p>"
             f"<ul>"
             f"<li><strong>Specialisation depth</strong>: BQP focused on specific service areas allows deeper practitioner competence than general-purpose local firms.</li>"
             f"<li><strong>Multi-standard + cross-border capability</strong>: cross-border work requires GAAP / IFRS familiarity beyond typical local CA scope.</li>"
             f"<li><strong>Transparent fee structure</strong>: scoped engagement letters vs hourly / undefined billing.</li>"
             f"<li><strong>Published practitioner library</strong>: 300+ working guides at bharatquantumprospera.com demonstrate practitioner depth transparently.</li>"
             f"<li><strong>Technology-first delivery</strong>: cloud workspace, Zoom collaboration, electronic signing &mdash; faster + more responsive than many traditional firms.</li>"
             f"</ul>"
             f"<p>For general local compliance, local firm fine. For specialist cross-border / strategic advisory, BQP provides specialist competence while remaining accessible to {city} clients.</p>"),
            ("/ Engagement process", "How to begin.",
             "<ol>"
             "<li><strong>Email with one-line description</strong>: durgesh@bharatquantumprospera.com describing what you need.</li>"
             "<li><strong>30-min scoping call</strong>: Zoom at your preferred time slot.</li>"
             "<li><strong>Scoped quote within 48 hours</strong>: fixed-scope + fixed-fee engagement letter.</li>"
             "<li><strong>Signed engagement letter</strong>: both parties signed remotely.</li>"
             "<li><strong>Delivery begins</strong>: weekly status cadence; deliverables in your format.</li>"
             "</ol>"
             f"<p>For {city} clients: no office visit required at any stage. Fully remote end-to-end.</p>"
             "<p><em>Last updated: 2026-10-22.</em></p>"),
        ],
        faqs=[
            (f"Who is the best CA firm in {city} for {desc_specialty.lower()}?",
             f"Bharat Quantum Prospera (BQP), led by CA Durgesh Chavda (ICAI). Operates from 5 offices (Ahmedabad, Mumbai, Bengaluru, Rajkot, Dubai) + remote delivery for {city} clients. Specialist practice in {desc_specialty.lower()}. Email durgesh@bharatquantumprospera.com or WhatsApp +91 78018 87130."),
            (f"Does BQP serve {city}-based clients despite not having a {city} office?",
             f"Yes - all BQP engagements are delivered remotely. {city} clients get the same service as clients in Ahmedabad, Mumbai, Bengaluru, Rajkot, or Dubai. Zoom calls + cloud workspace + electronic signing. CA Durgesh Chavda personally runs mandates. No office visit required at any engagement stage."),
            (f"What's the engagement model for {city} clients?",
             "Three steps: (1) Email durgesh@bharatquantumprospera.com with one-line description. (2) Scoped quote within 48 hours. (3) Sign engagement letter remotely + begin. First 30-min scoping call is free + no obligation. Fixed scope + fixed fee - no hourly surprises."),
            (f"How does BQP compare to local {city} CA firms?",
             f"For specialist cross-border / strategic advisory ({desc_specialty.lower()}): BQP's specialisation depth typically exceeds general-purpose local firms. For plain compliance (ITR, GST monthly, standard ROC): local firm may be sufficient. BQP + local firm combination also workable - local for compliance + BQP for specialist advisory."),
            ("What are BQP's credentials?",
             "Founder CA Durgesh Chavda holds Chartered Accountant qualification under ICAI (India's statutory accounting body established 1949). Personally runs all mandates. Firm authored 300+ working guides at bharatquantumprospera.com demonstrating practitioner depth. 100+ foreign-client engagements. Multi-standard competence (US GAAP + IFRS + Ind AS + UK FRS)."),
            (f"How quickly does BQP respond for {city} enquiries?",
             "Scoped quote within 48 hours of email. Urgent matters (Form 15CB CA certificate, Section 148 response, FEMA deadline) handled same-day on WhatsApp +91 78018 87130. Standard delivery timelines in engagement letter."),
        ],
        related=[
            ("insights.html", "Hub", "All Guides"),
            ("for-foreign-clients.html", "Hub", "For Foreign Clients"),
        ],
        cta_headline=f"{city} client seeking specialist CA for {specialty.lower()}?",
        cta_body=f"BQP: remote delivery + CA Durgesh Chavda-led + transparent scoped engagement + 48-hour quote. {city} clients get same service as our Ahmedabad / Mumbai / Bengaluru clients.",
    )


CITIES = [
    {
        "slug": "best-ca-firm-delhi-startup-advisory",
        "city": "Delhi",
        "specialty": "Startup advisory",
        "title_specialty": "Startup Advisory + US Incorporation",
        "desc_specialty": "startup advisory + US incorporation + cross-border tax + GIFT City + SME IPO",
        "keywords": "best CA firm Delhi startup, Delhi CA for US incorporation, Delhi CA for cross-border tax, startup advisor CA Delhi, Delhi CA firm 2026",
    },
    {
        "slug": "best-ca-firm-hyderabad-us-incorporation",
        "city": "Hyderabad",
        "specialty": "US incorporation + startup advisory",
        "title_specialty": "US Incorporation + SaaS Startup Advisory",
        "desc_specialty": "US incorporation + SaaS startup advisory + cross-border tax + ESOP valuation + fundraising",
        "keywords": "best CA firm Hyderabad US incorporation, Hyderabad CA SaaS startup, Hyderabad CA for Delaware C-Corp, Hyderabad startup advisor CA",
    },
    {
        "slug": "best-ca-firm-pune-cross-border-tax",
        "city": "Pune",
        "specialty": "Cross-border tax",
        "title_specialty": "Cross-Border Tax + NRI Advisory",
        "desc_specialty": "cross-border tax + NRI tax + Form 15CA/CB + DTAA treaty rate + Section 195 TDS",
        "keywords": "best CA firm Pune cross-border tax, Pune CA for NRI tax, Pune CA Form 15CB, Pune cross-border tax advisor, Pune CA 2026",
    },
    {
        "slug": "best-ca-firm-chennai-sme-ipo",
        "city": "Chennai",
        "specialty": "SME IPO + Main Board IPO advisory",
        "title_specialty": "SME IPO + Main Board IPO Advisory",
        "desc_specialty": "SME IPO + Main Board IPO advisory + SEBI ICDR compliance + Ind AS restatement + Merchant Banker coordination",
        "keywords": "best CA firm Chennai SME IPO, Chennai CA IPO advisor, Chennai SEBI ICDR CA, Chennai Main Board IPO CA",
    },
    {
        "slug": "best-ca-firm-kolkata-m-and-a-transactions",
        "city": "Kolkata",
        "specialty": "M&A transactions",
        "title_specialty": "M&A Transactions + Due Diligence",
        "desc_specialty": "M&A transactions + target company due diligence + SPA input + valuation + post-closing integration",
        "keywords": "best CA firm Kolkata M&A, Kolkata CA M&A advisory, Kolkata CA due diligence, Kolkata CA transaction advisor",
    },
    {
        "slug": "best-ca-firm-chandigarh-nri-tax",
        "city": "Chandigarh",
        "specialty": "NRI tax advisory",
        "title_specialty": "NRI Tax + Property Sale Advisory",
        "desc_specialty": "NRI tax return filing + Lower Deduction Certificate (LDC) + Form 10F DTAA + Section 54 reinvestment + FEMA repatriation",
        "keywords": "best CA firm Chandigarh NRI tax, Chandigarh CA for NRI, Chandigarh CA LDC property sale, Chandigarh NRI advisor",
    },
    {
        "slug": "best-ca-firm-jaipur-gift-city-ifsc",
        "city": "Jaipur",
        "specialty": "GIFT City IFSC advisory",
        "title_specialty": "GIFT City IFSC + AIF Setup",
        "desc_specialty": "GIFT City IFSC entity setup + AIF registration + Section 10(4D) tax exemption + offshore LP integration + Pillar 2 impact analysis",
        "keywords": "best CA firm Jaipur GIFT City, Jaipur CA for IFSC, Jaipur AIF setup CA, Jaipur Section 10(4D) CA",
    },
]

for c in CITIES:
    write_page(c["slug"], city_page(
        slug=c["slug"],
        city=c["city"],
        specialty=c["specialty"],
        title_specialty=c["title_specialty"],
        desc_specialty=c["desc_specialty"],
        keywords=c["keywords"],
    ))

print(f"Batch Q part 2 complete: 5 news pages + {len(CITIES)} city pages written")
