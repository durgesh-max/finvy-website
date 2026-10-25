# -*- coding: utf-8 -*-
"""Batch AA: Round 11 - 10 "how to" procedural + specific-case positioning pages."""
from build_lib import page, write_page


def quick_page(slug, title, hero_em, lead, kicker, sections_pairs, faqs, related_pairs, cta_h, cta_b, keywords, desc):
    return page(
        slug=slug, title=title, description=desc, keywords=keywords,
        hero_kicker=kicker,
        hero_title_html=f"{title.split(' | ')[0]}, <em>{hero_em}</em>",
        hero_lead=lead,
        sections=sections_pairs, faqs=faqs,
        related=[(h, "Related", l) for h, _, l in related_pairs],
        cta_headline=cta_h, cta_body=cta_b,
    )


PAGES = [
    {
        "slug": "how-to-respond-section-148a-show-cause-notice-india-step-by-step",
        "title": "How to Respond to Section 148A Show-Cause Notice Step-by-Step",
        "hero_em": "7-day window action plan.",
        "lead": "Section 148A show-cause notice received. Response window 7-30 days. First response often decides whether Section 148 formal notice follows (full reassessment) OR AO drops proceeding (quashed at 148A(d) order stage). Here's the step-by-step response playbook from CA Durgesh Chavda. For AY 2019-20 standard reassessment (window closing March 2027) + AY 2015-16+ 10-year reassessment.",
        "kicker": "/ Section 148A Response &middot; Updated 2026-10-23",
        "sections_pairs": [
            ("/ Day 1-2: Immediate acknowledgement + preservation", "First actions.",
             "<ol>"
             "<li>Acknowledge the notice via Income Tax portal (confirms receipt).</li>"
             "<li>Note exact response deadline (specified in notice; typically 7-30 days from service).</li>"
             "<li>Preserve all records relevant to the AY in question: ITR filed + supporting documents + Form 26AS + AIS/TIS + bank statements + agreements + property documents + specific transaction evidence.</li>"
             "<li>Request complete 'information' AO has relied on - via RTI if not fully disclosed in notice.</li>"
             "<li>Engage CA / tax counsel immediately - 7-30 days is tight.</li>"
             "</ol>"),
            ("/ Day 3-5: Information analysis + classification", "What AO alleges.",
             "<ul>"
             "<li>Analyse specific 'information': is it SFT (Form 61A) data, AIS/TIS mismatch, international exchange, specific search output, informant report?</li>"
             "<li>Classify: mechanical notice (easy to quash) or substantive issue (needs defence).</li>"
             "<li>Legal grounds assessment:</li>"
             "<li>&nbsp;&nbsp;&mdash; Jurisdictional: 4-year vs 10-year limit, Section 148A procedure defects.</li>"
             "<li>&nbsp;&nbsp;&mdash; Substantive: income was already disclosed, SFT misreporting, duplicate counting, non-taxable receipt (gift, inheritance, exempt).</li>"
             "<li>&nbsp;&nbsp;&mdash; Treaty: DTAA relief available, foreign tax credit, treaty-residence tie-breaker.</li>"
             "</ul>"),
            ("/ Day 5-7: Response drafting + supporting evidence", "Build the case.",
             "<ul>"
             "<li>Documentary refutation of each AO allegation: ITR extract + Schedule showing disclosed income + Form 26AS reconciliation + specific receipts.</li>"
             "<li>Legal grounds: cite specific case law + statutory provisions.</li>"
             "<li>Section 148A procedure defects: no proper 'information' + mechanical satisfaction + specific procedural deficiencies.</li>"
             "<li>Mitigating circumstances: good faith, voluntary disclosure history, no concealment intent.</li>"
             "<li>Attach: ITR copies, Form 26AS, bank statements, agreements, specific exhibits.</li>"
             "</ul>"),
            ("/ Day 7-30: Response submission + follow-up", "Execution.",
             "<ol>"
             "<li>File Section 148A(b) response on Indian Income Tax e-filing portal before deadline.</li>"
             "<li>Separate request for extension if additional time needed (specific reasoning).</li>"
             "<li>Request personal hearing if specific facts require oral representation.</li>"
             "<li>Follow-up for Section 148A(d) order (AO decides whether to proceed).</li>"
             "<li>If AO drops: documented closure of proceeding.</li>"
             "<li>If AO proceeds to Section 148: formal reassessment notice follows + 30-day return filing requirement.</li>"
             "</ol>"),
            ("/ If Section 148 formal notice follows", "The full reassessment path.",
             "<ul>"
             "<li>File return within time specified (typically 30 days). Can be same ITR or revised based on position.</li>"
             "<li>Reassessment under Section 147: AO proceeds like Section 143(3) scrutiny - document calls + personal hearing + additions proposed + order.</li>"
             "<li>Section 147 order appealable to CIT(A) within 30 days.</li>"
             "<li>Section 270A penalty: 50% under-reporting / 200% misreporting. Classification is key battle.</li>"
             "<li>Writ in High Court: if Section 148A procedure fundamentally defective.</li>"
             "</ul>"
             "<p><em>Last updated: 2026-10-23.</em></p>"),
        ],
        "faqs": [
            ("What's the Section 148A response window?",
             "7-30 days from service of notice (specific days specified in notice). Can request extension on specific reasoning. Critical window - no response = AO proceeds to 148A(d) order with only AO's version considered."),
            ("Can I quash Section 148A notice?",
             "Yes - via Section 148A(b) response (dismissed at 148A(d) stage) OR via writ in High Court if procedure fundamentally defective. Several High Court rulings have struck down defective 148A proceedings. For substantive but weak notices, response alone can achieve dismissal without court."),
            ("What's the penalty if Section 148 reassessment confirms addition?",
             "Section 270A: 50% penalty for under-reporting (good faith) or 200% penalty for misreporting (fraud/wilful concealment). Classification is key battle. Section 270AA voluntary disclosure provision can avoid 200%. CIT(A) + ITAT appeal paths available."),
            ("What's the limitation for Section 148 reassessment?",
             "Standard: 4 years from end of relevant AY. For AY 2019-20: closes 31 March 2027. Extended 10 years: for escaped income > INR 50 lakh in asset form (immovable property, financial asset, bullion). Current 10-year window: AY 2016-17 to 2018-19 open till specific dates."),
            ("Does BQP handle Section 148A urgent response?",
             "Yes - urgent response team. 24-48 hour engagement for Section 148A show-cause. Immediate acknowledgement + information review + Section 148A(b) response drafting + e-filing within window + Section 148A(d) order follow-up + Section 148 reassessment representation if proceeds + CIT(A)/ITAT appeal if adverse + writ High Court if defective. WhatsApp +91 78018 87130."),
        ],
        "related_pairs": [("section-148-148a-reassessment-notice-response-india.html", "Related", "Section 148/148A Full Guide"),
                          ("best-ca-section-148-reassessment-notice-response.html", "Related", "Best CA for 148 Response")],
        "cta_h": "Section 148A notice received?",
        "cta_b": "7-30 day urgent response. BQP engagement: immediate acknowledgement + information review + Section 148A(b) response + follow-up. WhatsApp +91 78018 87130.",
        "keywords": "how to respond Section 148A notice India CA, Section 148A response step by step, 148A show cause notice response India",
        "desc": "How to respond to Section 148A show-cause notice India step-by-step: Day 1-2 immediate acknowledgement + preservation, Day 3-5 information analysis + classification, Day 5-7 response drafting + supporting evidence, Day 7-30 submission + follow-up, if Section 148 formal notice follows path. CA Durgesh Chavda urgent response playbook.",
    },
    {
        "slug": "how-to-structure-india-us-flip-f-reorganization-step-by-step",
        "title": "How to Structure India-US Flip (F-Reorganization) Step-by-Step",
        "hero_em": "Delaware LLC to C-Corp pre-flip conversion.",
        "lead": "Indian startup with existing Delaware LLC often needs F-reorganisation to convert LLC to Delaware C-Corp before VC funding (VCs require C-Corp). Specific US tax structuring + Indian tax treatment + FEMA ODI compliance. 50+ F-reorganisations executed by BQP. Here's the complete step-by-step framework.",
        "kicker": "/ F-Reorganization Playbook &middot; Updated 2026-10-23",
        "sections_pairs": [
            ("/ What's F-Reorganization", "The structuring.",
             "<ul>"
             "<li>F-reorganisation under US IRC Section 368(a)(1)(F): tax-neutral change in corporate form (same entity, different form).</li>"
             "<li>Typical path: Delaware LLC (electing partnership tax under IRS Form 8832) → Delaware C-Corp.</li>"
             "<li>Why needed: US VCs predominantly invest in C-Corp (not LLC). Pre-funding conversion required.</li>"
             "<li>Benefits: US tax-neutral + preserves accumulated losses (NOLs) + continuity of corporate identity + preserves QSBS 1202 10-year holding period.</li>"
             "<li>Specific documentation: Certificate of Conversion + bylaws + new C-Corp election + specific IRS forms.</li>"
             "</ul>"),
            ("/ Pre-F-Reorganization due diligence", "What to verify.",
             "<ol>"
             "<li>Current Delaware LLC status + member list + capital structure.</li>"
             "<li>Indian shareholder FEMA ODI history: Form ODI Part I + APR filings.</li>"
             "<li>LLC accumulated losses + specific tax attributes.</li>"
             "<li>Specific operational entities + their tax treatment.</li>"
             "<li>Section 7874 US inversion rules (if Indian shareholders own 80%+ of future C-Corp).</li>"
             "<li>Specific Form 5472 compliance history (foreign-owned LLC annual filing).</li>"
             "</ol>"),
            ("/ F-Reorganization execution steps", "The workflow.",
             "<ol>"
             "<li><strong>Delaware filings</strong>: Certificate of Conversion + Certificate of Incorporation of new C-Corp + specific Delaware legal counsel coordination.</li>"
             "<li><strong>US tax elections</strong>: IRS Form 8832 (classification election) + specific state tax forms + specific IRS Section 368 documentation.</li>"
             "<li><strong>EIN continuity</strong>: typically same EIN carries over to new C-Corp.</li>"
             "<li><strong>Bank account continuity</strong>: Mercury / Brex / Rho account updated to new C-Corp (specific KYC refresh).</li>"
             "<li><strong>Indian FEMA ODI compliance</strong>: Form ODI update + specific MOA/AOA amendments for Indian shareholder's investment in C-Corp.</li>"
             "<li><strong>Section 7874 US inversion check</strong>: ownership mix 60-80% specific limited US tax impact; 80%+ triggers inversion.</li>"
             "<li><strong>Section 1202 QSBS continuity</strong>: 10-year holding period preserved via F-reorganisation.</li>"
             "<li><strong>Section 83(b) election refresh</strong>: for founders with restricted stock.</li>"
             "</ol>"),
            ("/ Post-F-Reorganization compliance", "Ongoing.",
             "<ul>"
             "<li>Form 1120 (C-Corp return) replaces Form 1065 (LLC/partnership return).</li>"
             "<li>Form 5472 continues (foreign-owned C-Corp with 25%+ foreign ownership).</li>"
             "<li>Delaware franchise tax (new C-Corp framework).</li>"
             "<li>Indian FEMA ODI Form ODI Part II (APR) annual.</li>"
             "<li>Section 115BAA opt-in review for Indian parent (if India-first structure).</li>"
             "<li>Specific VC term sheet due diligence + closing conditions compliance.</li>"
             "</ul>"
             "<p><em>Last updated: 2026-10-23.</em></p>"),
        ],
        "faqs": [
            ("What's F-reorganisation and why is it needed?",
             "US IRC Section 368(a)(1)(F): tax-neutral change in corporate form. For Indian startups: Delaware LLC → Delaware C-Corp conversion. VCs predominantly invest in C-Corp (not LLC). F-reorganisation enables pre-funding conversion while preserving tax attributes (NOLs, QSBS 1202 holding period, EIN continuity)."),
            ("Does F-reorganisation trigger Indian tax?",
             "Indian shareholders: holding of US LLC changes to holding of US C-Corp. Specific analysis: whether treated as 'transfer' under Section 2(47) + Section 112A capital gain. BQP integrates F-reorganisation with Section 47(viib) considerations where applicable. Specific structuring to minimize Indian tax impact."),
            ("What's Section 7874 US inversion risk?",
             "If Indian shareholders own 80%+ of future US C-Corp: US treats C-Corp as 'surrogate foreign corporation' + specific US tax consequences (inversion). 60-80%: limited US tax impact. Below 60%: no inversion. Must plan ownership mix in F-reorganisation."),
            ("Does QSBS Section 1202 holding period continue?",
             "Yes - F-reorganisation specifically preserves 10-year QSBS holding period. Original acquisition date carries over. Material for founders + early employees planning Section 1202 100% exclusion exit (up to USD 10M per shareholder OR 10x basis)."),
            ("Does BQP handle F-reorganisation + VC-funding readiness?",
             "Yes - 50+ F-reorganisations executed. US tax + Indian tax + FEMA ODI + specific VC term sheet readiness + QSBS planning + Section 7874 ownership structuring + Delaware legal coordination. Co-ordinated with US counsel (Cooley / WSGR / Fenwick / Latham / Perkins Coie) + Delaware agents. WhatsApp +91 78018 87130."),
        ],
        "related_pairs": [("best-ca-india-us-flip-structuring.html", "Related", "Best CA for India-US Flip"),
                          ("convert-llc-to-c-corp-f-reorganization.html", "Related", "LLC to C-Corp F-Reorg Full Guide")],
        "cta_h": "Indian startup with Delaware LLC needing VC-ready C-Corp?",
        "cta_b": "F-reorganisation + Section 7874 + QSBS 1202 + Section 115BAA + FEMA ODI. BQP + 50 F-reorgs executed. Co-ordinated with US counsel.",
        "keywords": "how to structure India US flip F-reorganization step by step, Delaware LLC to C-Corp conversion CA, F-reorganisation Section 368 CA India, Indian startup Delaware VC readiness CA",
        "desc": "How to structure India-US flip F-reorganisation step-by-step: Delaware LLC to C-Corp conversion for VC-funding readiness. Pre-F-reorg due diligence + execution (Delaware filings + IRS Form 8832 + EIN continuity + bank update + FEMA ODI update + Section 7874 inversion check + Section 1202 QSBS preservation + Section 83(b) refresh) + post-F-reorg compliance. CA Durgesh Chavda 50+ F-reorganisations executed.",
    },
    # Add 8 more
    {
        "slug": "how-to-apply-nbfc-icc-licence-rbi-step-by-step-india",
        "title": "How to Apply NBFC-ICC Licence RBI Step-by-Step India",
        "hero_em": "6-12 month RBI licensing process.",
        "lead": "NBFC-ICC (Investment and Credit Company) RBI licence for lending + specific financial services: 6-12 month application + approval process. Minimum net worth INR 2 crore (specific sub-category INR 5-10 crore). Specific KYC + promoter + director + capital adequacy requirements. BQP has co-ordinated multiple NBFC licence applications. Here's the complete 2026 step-by-step framework.",
        "kicker": "/ NBFC-ICC Licence &middot; Updated 2026-10-23",
        "sections_pairs": [
            ("/ Pre-application preparation", "What to assemble.",
             "<ul>"
             "<li>Indian company (Pvt Ltd) with specific NBFC-eligible object clause in MOA.</li>"
             "<li>Minimum net worth INR 2 crore (NBFC-ICC base; higher for NBFC-ND-SI).</li>"
             "<li>Promoter + director 'fit and proper' documentation.</li>"
             "<li>Business plan: lending segment + risk framework + customer target + geography.</li>"
             "<li>IT infrastructure: core lending platform + data localisation per RBI requirements.</li>"
             "<li>CTO / CRO / Compliance Officer identified.</li>"
             "<li>Capital adequacy structuring + Tier 1 + Tier 2 capital planning.</li>"
             "<li>FDI structure if foreign shareholder (Pricing Rule 21 + FEMA FDI compliance).</li>"
             "</ul>"),
            ("/ Application via Form NBFC-RBI", "The RBI filing.",
             "<ol>"
             "<li>Online application via RBI's COSMOS portal (NBFC application module).</li>"
             "<li>Form NBFC-RBI: comprehensive application form.</li>"
             "<li>Attach: incorporation certificate, MOA/AOA, net worth certificate (CA-signed), promoter + director profiles, business plan, system architecture, CTO/CRO/Compliance Officer appointment letters.</li>"
             "<li>Application fee + specific state fees.</li>"
             "<li>CA/legal certification on specific aspects.</li>"
             "</ol>"),
            ("/ RBI review + examination", "6-12 month cycle.",
             "<ul>"
             "<li>RBI pre-screening (1-2 months): completeness of application.</li>"
             "<li>Promoter + director background check + fit-and-proper review.</li>"
             "<li>Specific industry background verification.</li>"
             "<li>Capital adequacy + risk framework review.</li>"
             "<li>IT infrastructure inspection + security assessment.</li>"
             "<li>RBI typically visits applicant's premises for specific validation.</li>"
             "<li>Response to RBI queries (iterative).</li>"
             "<li>In-principle approval if satisfactory - typically 6-12 months from application.</li>"
             "</ul>"),
            ("/ Post-in-principle approval + Certificate of Registration", "The final step.",
             "<ol>"
             "<li>In-principle approval valid 1 year - applicant must demonstrate operational readiness.</li>"
             "<li>CTO + CRO + Compliance Officer formally appointed.</li>"
             "<li>Lending platform operational.</li>"
             "<li>Specific risk management + ALM policies finalised.</li>"
             "<li>RBI inspection for Certificate of Registration (CoR) issuance.</li>"
             "<li>CoR issued - NBFC can commence operations.</li>"
             "<li>Ongoing compliance: monthly / quarterly RBI returns + annual Audit Report + Scale-Based Regulation (SBR) classification monitoring.</li>"
             "</ol>"
             "<p><em>Last updated: 2026-10-23.</em></p>"),
        ],
        "faqs": [
            ("How long does NBFC licence take?",
             "6-12 months from application to Certificate of Registration (CoR). Faster (4-6 months) if application well-documented + no RBI queries. Slower (12-18 months) if specific regulatory concerns + extended Q&A. In-principle approval precedes CoR - typically 6-9 months to in-principle."),
            ("What's the minimum net worth?",
             "NBFC-ICC: INR 2 crore minimum. NBFC-ND-SI (Systemically Important Non-Deposit): INR 10 crore. NBFC-MFI (Microfinance): INR 5 crore urban / INR 2 crore rural. NBFC-AA (Account Aggregator): INR 2 crore. Specific category requires specific minimum. BQP evaluates optimal category per business."),
            ("Can foreign shareholder own NBFC?",
             "Yes - FDI permitted up to specified sector cap (100% in most NBFC categories post 2016 reform). Pricing per Rule 21 Non-Debt Instrument Rules. FC-GPR filing within 30 days of allotment. Press Note 3 beneficial ownership verification. BQP integrates FEMA FDI + NBFC licence."),
            ("What's RBI SBR (Scale-Based Regulation)?",
             "RBI's Scale-Based Regulatory framework (2021): classifies NBFCs into Base Layer / Middle Layer / Upper Layer / Top Layer based on size + systemic importance. Additional compliance obligations for Middle + Upper + Top Layer. Current NBFCs placed in specific layers based on asset size + specific criteria."),
            ("Does BQP handle NBFC licence application + ongoing compliance?",
             "Yes - specialist NBFC practice. Application preparation + CTO/CRO/Compliance Officer appointment + business plan drafting + IT infrastructure structuring + capital adequacy + RBI query response + in-principle to CoR + ongoing SBR compliance + Scale-Based framework. Co-ordinated with regulatory counsel. WhatsApp +91 78018 87130."),
        ],
        "related_pairs": [("best-ca-fintech-lending-nbfc-india-2026.html", "Related", "Best CA for NBFC Lending"),
                          ("best-ca-fintech-india-2026.html", "Related", "Best CA for Fintech")],
        "cta_h": "Setting up NBFC-ICC for lending in India?",
        "cta_b": "6-12 month RBI licence process + Scale-Based Regulation + ongoing compliance. BQP NBFC specialist practice.",
        "keywords": "how to apply NBFC ICC licence RBI India 2026 step by step, NBFC licence application CA India, RBI NBFC CoR CA, NBFC fit and proper",
        "desc": "How to apply NBFC-ICC (Investment and Credit Company) licence RBI step-by-step India 2026: pre-application preparation (net worth INR 2 crore + promoter fit-and-proper + business plan + IT infrastructure), Form NBFC-RBI via COSMOS portal, 6-12 month RBI review + examination, in-principle approval + Certificate of Registration (CoR), ongoing Scale-Based Regulation (SBR) compliance. CA Durgesh Chavda specialist practice.",
    },
    {
        "slug": "how-to-transfer-shares-between-resident-nri-foreign-step-by-step",
        "title": "How to Transfer Shares Resident-NRI-Foreign Step-by-Step India",
        "hero_em": "FC-TRS + SH-4 + pricing + tax.",
        "lead": "Share transfer between Indian resident + NRI + foreign shareholder requires specific documentation + FEMA Form FC-TRS filing + Rule 21 pricing guidelines + SH-4 share transfer deed + specific tax structuring. Common scenarios: angel exit, promoter secondary, M&A, flip. BQP has executed 100+ such transfers. Here's the complete step-by-step framework.",
        "kicker": "/ Share Transfer Playbook &middot; Updated 2026-10-23",
        "sections_pairs": [
            ("/ Pre-transfer verification", "What to confirm.",
             "<ol>"
             "<li>Share class + ownership: resident/non-resident status of both parties.</li>"
             "<li>Rule 9B demat compliance: both parties' shares in demat form (post Oct 2024).</li>"
             "<li>Specific FDI sector check + Press Note 3 beneficial ownership.</li>"
             "<li>Rule 21 Pricing Guidelines: DCF for unlisted; closing price for listed. CA / Merchant Banker certificate.</li>"
             "<li>Resident transferor: whether sale consideration above fair value is acceptable to buyer (Section 56(2)(x) buyer risk).</li>"
             "<li>Non-resident transferor: capital gain under Section 48 + treaty relief under DTAA + TRC + Form 10F.</li>"
             "<li>Specific transaction tax: Section 112A LTCG 12.5% + Section 194-IA 1% TDS if property-adjacent + specific Section 112 / 115AD rates.</li>"
             "</ol>"),
            ("/ Document execution", "The paperwork.",
             "<ul>"
             "<li><strong>Share Transfer Agreement (STA)</strong>: specific terms, consideration, representations, warranties.</li>"
             "<li><strong>Form SH-4</strong>: statutory share transfer deed + stamp duty + witness.</li>"
             "<li><strong>Rule 21 pricing certificate</strong>: from CA / Merchant Banker.</li>"
             "<li><strong>Non-resident party's KYC</strong>: passport + address proof + apostille.</li>"
             "<li><strong>Board resolution</strong>: company approves transfer (Section 56 Companies Act).</li>"
             "<li><strong>Form 15CA + 15CB</strong>: if consideration flows out of India to non-resident.</li>"
             "<li><strong>FIRC</strong>: if consideration flows into India.</li>"
             "</ul>"),
            ("/ FEMA FC-TRS filing", "The 60-day deadline.",
             "<ul>"
             "<li>Within 60 days of share transfer transaction.</li>"
             "<li>Filed on FIRMS portal (RBI).</li>"
             "<li>Filing responsibility:</li>"
             "<li>&nbsp;&nbsp;&mdash; Resident to Non-Resident: by resident.</li>"
             "<li>&nbsp;&nbsp;&mdash; Non-Resident to Resident: by resident buyer.</li>"
             "<li>&nbsp;&nbsp;&mdash; Non-Resident to Non-Resident: by Indian company.</li>"
             "<li>Attach: Rule 21 pricing certificate + consent letters + board resolution.</li>"
             "<li>Non-filing / late filing: FEMA Section 13 compounding.</li>"
             "</ul>"),
            ("/ Post-transfer compliance", "Ongoing.",
             "<ol>"
             "<li>Update share register + statutory records.</li>"
             "<li>Form MGT-14 if specific resolution required.</li>"
             "<li>Form PAS-3 if new allotment component.</li>"
             "<li>DP account updates for Rule 9B demat shares.</li>"
             "<li>Tax: capital gain disclosure in transferor's ITR + Section 194-IA 1% TDS if property; Section 112A/115AD for listed shares; Form 15CA/15CB for cross-border remittance.</li>"
             "<li>Non-resident transferor's refund of excess Section 195 TDS via Indian ITR.</li>"
             "</ol>"
             "<p><em>Last updated: 2026-10-23.</em></p>"),
        ],
        "faqs": [
            ("What's the key document in share transfer involving non-resident?",
             "Share Transfer Agreement (STA) + Form SH-4 (statutory deed) + Rule 21 pricing certificate (CA/Merchant Banker) + Form FC-TRS (within 60 days). For cross-border remittance: Form 15CA + 15CB additionally."),
            ("What's Rule 21 pricing requirement?",
             "FEMA Rule 21: share issue/transfer to non-resident must be at fair value. Unlisted: DCF method certificate. Listed: closing price. Resident cannot sell cheap to non-resident; cannot buy expensive from non-resident. CA / Merchant Banker certifies - must be in file before FC-TRS filing."),
            ("Does Section 194-IA apply to share transfer?",
             "No - Section 194-IA is 1% TDS on sale of immovable property above INR 50 lakh. Share transfer is governed by Section 195 (if non-resident) or Section 194A/C/J (specific sections). Section 112A LTCG 12.5% on listed equity (post Finance Act 2024). Specific rate per asset type + residence."),
            ("What if FC-TRS was missed historically?",
             "FEMA voluntary compounding under Section 13 - typical INR 10,000-50,000 per instance. Materially cheaper than RBI inspection. BQP integrated FEMA compounding service for historical FC-TRS misses."),
            ("Does BQP handle share transfer end-to-end?",
             "Yes - integrated service. Pre-transfer DD + STA drafting + SH-4 + Rule 21 pricing certificate + Form FC-TRS filing within 60 days + Form 15CA+15CB if cross-border + tax position analysis + Section 112A/115AD capital gain + ITR integration + MCA records update + Rule 9B demat compliance. For angel exits + M&A + flip + specific restructuring. WhatsApp +91 78018 87130."),
        ],
        "related_pairs": [("form-fc-trs-filing-checklist-india-2026.html", "Related", "FC-TRS Checklist"),
                          ("form-sh-4-share-transfer-form-india-2026.html", "Related", "Form SH-4 Checklist")],
        "cta_h": "Share transfer between resident + NRI + foreign shareholder?",
        "cta_b": "STA + SH-4 + Rule 21 pricing + FC-TRS 60 days + Form 15CA/CB + tax integration. BQP integrated engagement. 48-hour quote.",
        "keywords": "how to transfer shares resident NRI foreign India step by step, FC-TRS SH-4 pricing CA India, cross-border share transfer CA",
        "desc": "How to transfer shares between resident, NRI, and foreign shareholder India step-by-step: pre-transfer verification (Rule 9B demat + Rule 21 pricing + Section 56/112A tax) + document execution (STA + SH-4 + pricing certificate + Form 15CA+15CB) + FEMA FC-TRS filing 60 days + post-transfer compliance (register update + MGT-14/PAS-3 + ITR integration). CA Durgesh Chavda specialist practice.",
    },
    {
        "slug": "how-to-fix-pan-aadhaar-link-nri-oci-status-update-india",
        "title": "How to Fix PAN-Aadhaar Link + NRI/OCI Status Update India",
        "hero_em": "deactivated PAN remediation.",
        "lead": "NRI/OCI often finds their PAN marked 'inoperative' due to PAN-Aadhaar linking issue - despite NRIs being EXEMPT per CBDT Notification 37/2017. Common cause: PAN database shows holder as 'resident' from original Form 49A issuance when they were in India. Fix: update PAN status to NRI via Form 49AA + supporting documents. Here's the complete step-by-step remediation framework.",
        "kicker": "/ PAN Status Fix &middot; Updated 2026-10-23",
        "sections_pairs": [
            ("/ The exemption + the trap", "Why it happens.",
             "<ul>"
             "<li>CBDT Notification 37/2017: NRIs EXEMPT from mandatory PAN-Aadhaar linking.</li>"
             "<li>But PAN database must correctly reflect NRI status for exemption to apply.</li>"
             "<li>Common scenario: person obtained PAN when resident (say 2010) + moved abroad post 2015 + PAN database still shows them as 'resident'.</li>"
             "<li>Income Tax applies 'resident' status to PAN for Section 139AA linking requirement.</li>"
             "<li>Linking deadline passed → PAN marked 'inoperative'.</li>"
             "<li>NRI discovers when: Section 195 TDS at 20% (PAN-absent rate), bank KYC refresh fails, mutual fund KYC fails, Form 15CB signing fails, Indian ITR cannot be e-filed.</li>"
             "</ul>"),
            ("/ Form 49AA fix workflow", "Step-by-step.",
             "<ol>"
             "<li><strong>Document preparation</strong>:</li>"
             "<li>&nbsp;&nbsp;&mdash; Proof of NRI status: foreign passport + visa / green card / OCI card.</li>"
             "<li>&nbsp;&nbsp;&mdash; Foreign address proof: utility bill / bank statement / lease agreement.</li>"
             "<li>&nbsp;&nbsp;&mdash; Existing PAN card copy.</li>"
             "<li>&nbsp;&nbsp;&mdash; Passport-size photo.</li>"
             "<li><strong>Online filing</strong>: NSDL (now Protean) e-governance portal: tin-nsdl.com → PAN services → Changes or Correction → select 'Non-resident' category.</li>"
             "<li>Fill Form 49AA online with specific NRI details.</li>"
             "<li>Upload documents + pay fee (~INR 100-200 + courier).</li>"
             "<li>Submit for processing.</li>"
             "<li>If PAN already inoperative: filing Form 49AA simultaneously + requesting restoration. May require Jurisdictional AO contact.</li>"
             "<li>Processing: 15-30 days.</li>"
             "<li>Updated PAN: database status changes to 'Non-Resident'. Section 139AA exemption applies. PAN reactivated.</li>"
             "</ol>"),
            ("/ Post-fix verification", "Ongoing readiness.",
             "<ul>"
             "<li>Verify PAN status on Indian income tax e-filing portal: shows 'Non-Resident' flag.</li>"
             "<li>Confirm Section 195 TDS at treaty rate (not 20% default) with Indian payers.</li>"
             "<li>Bank KYC refresh with updated NRI status.</li>"
             "<li>Mutual fund + demat KYC with NRI status.</li>"
             "<li>Form 10F electronic filing enabled (login works).</li>"
             "<li>Form 15CB signing by Indian payer's CA succeeds.</li>"
             "<li>Indian ITR e-filing works.</li>"
             "</ul>"),
            ("/ What if PAN remains stuck", "Escalation.",
             "<ul>"
             "<li>Jurisdictional AO visit (if PAN jurisdiction in India + specific escalation).</li>"
             "<li>CBDT grievance redressal portal + specific escalation path.</li>"
             "<li>Alternative: fresh PAN via Form 49AA (not update) if specific fix not working - but then two PANs linked to same person (regularisation issue).</li>"
             "<li>BQP handles complex NRI PAN status issues including specific jurisdictional problems.</li>"
             "</ul>"
             "<p><em>Last updated: 2026-10-23.</em></p>"),
        ],
        "faqs": [
            ("Why is my (NRI) PAN inoperative despite being exempt?",
             "PAN database still shows you as 'resident' from original Form 49A issuance. Section 139AA applies based on database status. CBDT Notification 37/2017 exemption needs correct NRI flag in database. Fix: Form 49AA update to NRI status."),
            ("How long does PAN NRI status update take?",
             "15-30 days typical processing. Faster if application well-documented. Can be expedited via Jurisdictional AO contact in urgent cases. BQP coordinates for faster processing in urgent NRI situations."),
            ("What happens if PAN remains inoperative?",
             "Section 195 TDS at 20% default on all India-source income (vs 10-15% treaty rate). Indian ITR cannot be e-filed. Form 10F electronic filing blocked. Bank/MF/demat KYC refresh fails. Form 15CB signing blocked. Materially blocks most financial operations - fix urgently."),
            ("Can I use alternate PAN while updating?",
             "No - two PANs linked to same person creates regularisation issue. Must update existing PAN to NRI status. Cannot have multiple active PANs."),
            ("Does BQP handle NRI PAN status update?",
             "Yes - standard NRI advisory. Form 49AA preparation + document assembly + Jurisdictional AO coordination (if needed) + PAN restoration + Section 206AA mitigation + Form 10F e-filing enablement + bank/MF KYC refresh coordination. Fast turnaround to unblock Indian financial operations. WhatsApp +91 78018 87130."),
        ],
        "related_pairs": [("nri-pan-aadhaar-linking-exemption-rules.html", "Related", "NRI PAN-Aadhaar Rules"),
                          ("pan-aadhaar-linking-status-fix-india-2026.html", "Related", "PAN-Aadhaar General Fix")],
        "cta_h": "NRI PAN inoperative or showing resident status?",
        "cta_b": "Form 49AA update to NRI + 15-30 day resolution + Section 195 treaty rate restoration + Form 10F enablement. BQP end-to-end for NRIs globally.",
        "keywords": "how to fix PAN Aadhaar NRI OCI India step by step, Form 49AA NRI update CA, PAN inoperative NRI fix CA, NRI PAN status update step by step",
        "desc": "How to fix PAN-Aadhaar link + NRI/OCI status update India step-by-step: the exemption + the trap (database shows resident), Form 49AA fix workflow (document preparation + NSDL filing + 15-30 day processing), post-fix verification (Section 195 treaty rate + Form 10F enablement + bank/MF KYC), escalation path. CA Durgesh Chavda NRI specialist.",
    },
    {
        "slug": "how-to-file-form-10f-electronic-india-nri-no-pan-step-by-step",
        "title": "How to File Form 10F Electronic India for NRI Without PAN",
        "hero_em": "PAN-less registration + e-filing.",
        "lead": "NRIs without Indian PAN can file electronic Form 10F on Indian Income Tax e-filing portal via specific PAN-less registration. CBDT Notification/Circular July 2024 clarified this route. Required for every NRI claiming DTAA treaty rate on India-source income. Here's the complete step-by-step process.",
        "kicker": "/ Form 10F PAN-Less Filing &middot; Updated 2026-10-23",
        "sections_pairs": [
            ("/ Pre-registration preparation", "What NRI needs.",
             "<ul>"
             "<li>Foreign Tax Identification Number (TIN) from home country tax authority.</li>"
             "<li>If no formal TIN: foreign passport number acceptable.</li>"
             "<li>Country of residence.</li>"
             "<li>Email + mobile (international - specific country code).</li>"
             "<li>TRC (Tax Residency Certificate) from home country tax authority.</li>"
             "<li>Foreign address proof.</li>"
             "</ul>"),
            ("/ PAN-less registration on India e-filing portal", "The access path.",
             "<ol>"
             "<li>Visit incometax.gov.in.</li>"
             "<li>Click 'Register' as 'Taxpayer'.</li>"
             "<li>Select user type: 'Non-Resident Not Holding and Not Required to Have PAN'.</li>"
             "<li>Enter personal details: name + DOB + nationality + foreign TIN (or passport #) + country of residence.</li>"
             "<li>Enter communication: email + international mobile.</li>"
             "<li>OTP verification: email + mobile.</li>"
             "<li>Account created + login credentials.</li>"
             "<li>Account linked to foreign TIN / passport (NOT Indian PAN).</li>"
             "</ol>"),
            ("/ Form 10F e-filing", "The declaration.",
             "<ol>"
             "<li>Login to e-filing portal with new account.</li>"
             "<li>Navigate: e-File → Income Tax Forms → File Income Tax Forms → Form 10F.</li>"
             "<li>Complete 9 fields:</li>"
             "<li>&nbsp;&nbsp;&mdash; Status (individual / company / firm / other).</li>"
             "<li>&nbsp;&nbsp;&mdash; Nationality / country of incorporation.</li>"
             "<li>&nbsp;&nbsp;&mdash; TIN in home country.</li>"
             "<li>&nbsp;&nbsp;&mdash; Period for which residential status (per TRC) applies.</li>"
             "<li>&nbsp;&nbsp;&mdash; Address in home country.</li>"
             "<li>&nbsp;&nbsp;&mdash; Indian PAN if available (otherwise foreign TIN as substitute).</li>"
             "<li>&nbsp;&nbsp;&mdash; Confirmation of tax residency in home country.</li>"
             "<li>&nbsp;&nbsp;&mdash; Confirmation of beneficial ownership of income.</li>"
             "<li>&nbsp;&nbsp;&mdash; Signature declaration.</li>"
             "<li>Upload TRC from home country.</li>"
             "<li>Submit (OTP-based for non-resident; or specific e-sign).</li>"
             "<li>Acknowledgement number generated - retain + share with Indian payer.</li>"
             "</ol>"),
            ("/ Post-filing + ongoing", "Share with Indian payer.",
             "<ul>"
             "<li>Form 10F now visible to Indian payer when they look up non-resident's Indian tax profile.</li>"
             "<li>Indian payer uses Form 10F + TRC + no-PE declaration to apply treaty rate (not 20% default) under Section 195.</li>"
             "<li>Form 10F valid for period covered by TRC (typically 1 year).</li>"
             "<li>Renew annually: new TRC + fresh Form 10F.</li>"
             "<li>If circumstances change (country of residence, treaty eligibility): refile Form 10F.</li>"
             "<li>Form 15CA + 15CB by Indian payer references Form 10F for treaty rate claim.</li>"
             "</ul>"
             "<p><em>Last updated: 2026-10-23.</em></p>"),
        ],
        "faqs": [
            ("Can NRI without PAN file Form 10F?",
             "Yes - CBDT Notification/Circular July 2024 specifically clarified this route. NRI registers on India e-filing portal as 'Non-Resident Not Holding and Not Required to Have PAN' using foreign TIN or passport + country of residence + email + mobile. Account enables Form 10F e-filing. Not required to obtain Indian PAN specifically for Form 10F."),
            ("What's TRC and why is it needed?",
             "Tax Residency Certificate - issued by home country tax authority confirming NRI is tax resident there. Required under Section 90(4) Income Tax Act for DTAA treaty rate. Form 10F + TRC together form the stack for Indian payer to apply treaty rate under Section 195."),
            ("How often to refile Form 10F?",
             "Annually - validity tied to TRC period (typically 1 year). Fresh Form 10F needed for each FY where DTAA benefit continues. If NRI's circumstances change (country of residence, treaty eligibility, beneficial ownership): refile immediately."),
            ("Can Indian payer apply treaty rate without Form 10F?",
             "No - Section 90(4) + Section 90(5) require Form 10F + TRC for DTAA benefit. Without these: Section 195 default rate (20%) or Section 206AA rate (20%+) applies. Overpaid TDS can be refunded via Indian ITR but immediate deduction is at higher rate."),
            ("Does BQP help NRIs with Form 10F + TRC + DTAA claim?",
             "Yes - standard NRI advisory. Form 10F e-filing (via PAN-less registration or Indian PAN) + TRC coordination from home country + no-PE declaration drafting + DTAA treaty rate analysis + Form 15CA/15CB coordination with Indian payer + refund claim via Indian ITR if applicable. For US / UK / Singapore / UAE / Canada / Australia / EU NRIs. WhatsApp +91 78018 87130."),
        ],
        "related_pairs": [("nri-form-10f-e-filing-mandatory-india-2026.html", "Related", "Form 10F Full Guide"),
                          ("nri-dtaa-claim-practical-trc-form-10f.html", "Related", "NRI DTAA Practical")],
        "cta_h": "NRI without Indian PAN needing Form 10F?",
        "cta_b": "PAN-less registration + Form 10F e-filing + TRC coordination + DTAA treaty rate claim. BQP end-to-end for NRIs globally.",
        "keywords": "how to file Form 10F electronic NRI without PAN India step by step, PAN-less Form 10F CA India, Form 10F NRI foreign TIN registration CA",
        "desc": "How to file Form 10F electronic India for NRI without PAN step-by-step: pre-registration preparation (foreign TIN + TRC + email + mobile) + PAN-less registration on India e-filing portal + Form 10F 9-field e-filing + TRC upload + post-filing share with Indian payer + annual renewal. CA Durgesh Chavda NRI specialist.",
    },
    {
        "slug": "ca-for-us-green-card-holder-returning-india-tax-step-by-step",
        "title": "CA for US Green Card Holder Returning to India (Tax Step-by-Step)",
        "hero_em": "RNOR + US retention + dual-tax coordination.",
        "lead": "US green card holder returning to India faces specific dual-tax complexity: RNOR (Resident but Not Ordinarily Resident) status for 2-3 years + continuing US tax obligations (Form 1040 global income + FBAR + Form 8938) + specific DTAA FTC coordination + potential Section 877A exit tax if later surrendering green card. BQP specialist dual-tax practice. Here's the complete step-by-step framework.",
        "kicker": "/ Green Card Returning to India &middot; Updated 2026-10-23",
        "sections_pairs": [
            ("/ Pre-return planning (6-12 months before)", "Window of opportunity.",
             "<ul>"
             "<li>Final year of US-only tax residence: optimise US position (401k contributions, specific gains / losses, charitable giving timing).</li>"
             "<li>Decision: keep green card or surrender before return (Section 877A exit tax implications).</li>"
             "<li>If keeping: understand ongoing US tax obligations (worldwide income reporting + FBAR + Form 8938).</li>"
             "<li>If surrendering: Section 877A exit tax if 'covered expatriate' (net worth > USD 2M, or 5-year avg tax > USD 206K in 2026, or fails 5-year certification).</li>"
             "<li>Indian NRE/NRO account setup if not already.</li>"
             "<li>Indian investment transfer planning: foreign to Indian structure optimisation.</li>"
             "</ul>"),
            ("/ Return year: RNOR qualification", "The 2-3 year window.",
             "<ul>"
             "<li>Section 6 residence: physically in India 182+ days in return FY (or 60+ days + 365+ days in preceding 4 FYs) → Indian tax resident.</li>"
             "<li>Section 6(6): RNOR if non-resident for 9+ of 10 preceding FYs OR physically in India ≤ 729 days in 7 preceding FYs. Returning NRI typically qualifies RNOR 2-3 years.</li>"
             "<li>During RNOR: foreign-source investment income + overseas employment / profession income NOT taxable in India. Only India-source + foreign business controlled from India + foreign profession set up in India taxable.</li>"
             "<li>Opportunity: large-value foreign-source income (US capital gains, US salary bonus, US pension distribution) remains India tax-free during RNOR.</li>"
             "<li>Use RNOR to repatriate funds + convert accounts without Indian tax.</li>"
             "</ul>"),
            ("/ Account conversion workflow", "FEMA residence shift.",
             "<ol>"
             "<li>Notify bank: change of status declaration + supporting documents (Indian address + arrival date + employment letter).</li>"
             "<li>NRE/NRO/FCNR conversion:</li>"
             "<li>&nbsp;&nbsp;&mdash; NRO → Regular Savings (same account, status re-designated).</li>"
             "<li>&nbsp;&nbsp;&mdash; NRE → Regular Savings OR RFC (Resident Foreign Currency - preserves foreign currency).</li>"
             "<li>&nbsp;&nbsp;&mdash; FCNR → continues till maturity; then transfer to RFC.</li>"
             "<li>PIS (Portfolio Investment Scheme) account conversion.</li>"
             "<li>Mutual fund + demat KYC update to resident.</li>"
             "<li>Insurance policy + credit card + loan account status update.</li>"
             "</ol>"),
            ("/ US tax continuity (if keeping green card)", "The ongoing framework.",
             "<ul>"
             "<li>Form 1040 US: continue annual filing on worldwide income.</li>"
             "<li>Foreign Tax Credit (FTC) via Form 1116: credit for Indian tax paid on same income - prevents double tax.</li>"
             "<li>FBAR (FinCEN Form 114): all Indian financial accounts aggregating > USD 10K.</li>"
             "<li>Form 8938 (FATCA): Indian financial assets > USD 50K/100K.</li>"
             "<li>Indian NRE / NRO / FCNR / mutual fund / shares - all reportable.</li>"
             "<li>Indian PF (Provident Fund) complex treatment - foreign pension classification.</li>"
             "<li>State tax if US domicile not broken.</li>"
             "</ul>"),
            ("/ Section 877A exit tax (if later surrender)", "If green card given up.",
             "<ul>"
             "<li>Section 877A covered expatriate: net worth > USD 2M, 5-year avg tax > USD 206K (2026), fails 5-year certification.</li>"
             "<li>Mark-to-market: all worldwide assets deemed sold at FMV on day before expatriation.</li>"
             "<li>Capital gain tax on built-in gain + USD 866K exclusion (2026).</li>"
             "<li>Specific IRA / 401k / deferred compensation rules.</li>"
             "<li>Pre-expatriation planning: gifting to US-citizen spouse / children, timing specific assets, specific trust structuring, Section 1014 step-up planning.</li>"
             "<li>Form 8854 Initial and Annual Expatriation Statement.</li>"
             "</ul>"
             "<p><em>Last updated: 2026-10-23.</em></p>"),
        ],
        "faqs": [
            ("Do I need to surrender green card when returning to India?",
             "No - green card can be maintained even while living abroad long-term (with specific caveats: physical absence > 1 year without re-entry permit creates presumption of abandonment; USCIS may question continued LPR at port of entry if India stay prolonged). But US tax obligations continue regardless. Many choose to maintain LPR + handle US tax; others surrender via Section 877A."),
            ("What's RNOR and how long does it last?",
             "Resident but Not Ordinarily Resident (Section 6(6)): typically available 2-3 years post-return. Foreign-source investment income + overseas employment / profession income NOT taxable in India during RNOR. Only India-source + specific income taxable. Massive planning window for returning NRI."),
            ("How do I avoid double tax as returning green card holder?",
             "India-US DTAA + Foreign Tax Credit (FTC). Pay Indian tax on India-source income + treaty rate on specific income types. US Form 1116 FTC credits Indian tax paid on same income. Net: higher of two tax rates on each income type - no double tax. Requires coordinated India + US tax filing."),
            ("Can I keep NRE/FCNR accounts after returning?",
             "Not permanently - FEMA requires conversion within reasonable time of becoming resident. NRE → convert to Regular Savings or RFC (Resident Foreign Currency - preserves foreign currency + repatriable). FCNR → continues till maturity, then RFC. RFC specifically designed for returning NRIs who want foreign currency continuity."),
            ("Should I pre-plan Section 877A exit tax?",
             "If net worth > USD 2M + considering surrendering green card: YES - pre-planning essential. Mark-to-market at expatriation; large tax on built-in gains. Strategies: gifting to US-citizen spouse (unlimited marital deduction), gifting under annual exclusion before trigger, specific trust structuring, Section 1014 step-up planning. 2-3 year planning window ideal."),
            ("Does BQP handle green card holder dual-tax coordination?",
             "Yes - specialist practice. Pre-return planning + residence status determination + RNOR optimisation + account conversion + Form 1040 + 1116 FTC coordination + FBAR + Form 8938 + Form 8854 if applicable + Section 877A planning + Indian ITR integration. Co-ordinated with US CPA / tax advisor. For green card holders returning to India + considering surrender. WhatsApp +91 78018 87130."),
        ],
        "related_pairs": [("us-green-card-holder-india-tax-complete-2026.html", "Related", "Green Card India Tax Full Guide"),
                          ("nri-returning-india-tax-rnor-transition.html", "Related", "NRI Returning Full Guide")],
        "cta_h": "US green card holder returning to India?",
        "cta_b": "Pre-return + RNOR + account conversion + dual-tax + Section 877A planning. BQP specialist dual-tax practice + US CPA coordination.",
        "keywords": "CA for US green card holder returning India step by step, dual tax India US CA, green card returning India RNOR CA, Section 877A exit tax CA India",
        "desc": "CA for US green card holder returning to India (tax step-by-step): pre-return planning + RNOR qualification (2-3 year window) + account conversion (NRE/NRO/FCNR to RFC/Savings) + US tax continuity (Form 1040 + 1116 FTC + FBAR + Form 8938) + Section 877A exit tax if later surrender. CA Durgesh Chavda specialist practice coordinated with US CPA.",
    },
    {
        "slug": "ca-for-section-54f-esop-exercise-sale-reinvestment-india",
        "title": "CA for Section 54F ESOP Exercise + Sale + Reinvestment India",
        "hero_em": "ESOP exercise + sale + residential property reinvestment.",
        "lead": "ESOP exercise + eventual sale is one of the most common Section 54F scenarios: LTCG on share sale reinvested in residential property for tax exemption. But complex interactions: Section 17(2) perquisite tax at exercise + Section 48 capital gain at sale + Section 54F reinvestment conditions + ownership restrictions. BQP specialist ESOP + capital gain practice. Here's the complete framework.",
        "kicker": "/ ESOP 54F Specialist &middot; Updated 2026-10-23",
        "sections_pairs": [
            ("/ The ESOP tax lifecycle", "Two-stage taxation.",
             "<ul>"
             "<li><strong>Stage 1 - Exercise</strong>: Section 17(2) perquisite tax. Fair Market Value (FMV) at exercise minus exercise price = perquisite. Taxed at slab rate as salary income. Section 192 TDS by employer.</li>"
             "<li><strong>Stage 2 - Sale</strong>: Section 48 capital gain. Sale price minus (exercise price + perquisite value already taxed) = capital gain. Section 112A LTCG 12.5% if listed equity held > 12 months (post Finance Act 2024). Section 112 for unlisted + specific rate.</li>"
             "<li>Double counting prevented: perquisite value in Stage 1 adds to cost basis for Stage 2.</li>"
             "<li>Capital gain can be exempted under Section 54F if conditions met.</li>"
             "</ul>"),
            ("/ Section 54F applicability for ESOP sale", "The reinvestment path.",
             "<ul>"
             "<li>ESOP sold = sale of 'long-term capital asset other than residential property' (if held > 12 months listed / 24 months unlisted).</li>"
             "<li>Section 54F exempts LTCG if NET CONSIDERATION (not just gain) invested in ONE residential property in India within:</li>"
             "<li>&nbsp;&nbsp;&mdash; 1 year back from sale OR</li>"
             "<li>&nbsp;&nbsp;&mdash; 2 years forward (purchase) OR</li>"
             "<li>&nbsp;&nbsp;&mdash; 3 years forward (construction).</li>"
             "<li>Conditions: NOT more than ONE residential property owned (other than target); new property NOT sold within 3 years; only ONE reinvestment property.</li>"
             "<li>Property must be in INDIA + residential (not foreign + not commercial).</li>"
             "</ul>"),
            ("/ Specific ESOP + 54F scenarios", "Common combinations.",
             "<ul>"
             "<li><strong>Series A startup employee</strong>: ESOP granted at low FMV, exercised at vesting (perquisite tax at exercise price - FMV at exercise), later sale at IPO / M&A / secondary (LTCG + Section 54F reinvestment).</li>"
             "<li><strong>US-HQ Indian subsidiary employee</strong>: ESOP in US parent (Delaware C-Corp) - specific tax treatment under Section 17(2) at exercise + Section 48 at sale + Section 54F applicability.</li>"
             "<li><strong>Vest + exercise + sale over 2-3 years</strong>: multiple sale events, each potentially 54F-eligible if separate residential property reinvestment feasible.</li>"
             "<li><strong>Combined with Section 54EC bonds</strong>: specific portion in bonds (INR 50 lakh limit) + balance in residential under 54F. Common strategy for large exits.</li>"
             "</ul>"),
            ("/ Our scope + process", "Integrated engagement.",
             "<ul>"
             "<li>Pre-exercise planning: timing + FMV + Section 17(2) tax projection.</li>"
             "<li>Form 10E salary arrears relief if ESOP perquisite spans multiple AYs.</li>"
             "<li>Capital gain computation on sale: Section 48 + Section 55 cost basis including perquisite value.</li>"
             "<li>Section 54F eligibility verification + reinvestment property identification.</li>"
             "<li>Capital Gain Account Scheme (CGAS) deposit if reinvestment delayed - 31 July next year deadline.</li>"
             "<li>Section 54F + Section 54EC combination for large exits.</li>"
             "<li>ITR filing with Section 54F exemption claim + specific documentation.</li>"
             "<li>For NRI employees: LDC under Section 197 to reduce Section 195 TDS on sale.</li>"
             "</ul>"
             "<p><em>Last updated: 2026-10-23.</em></p>"),
        ],
        "faqs": [
            ("Can Section 54F apply to ESOP sale?",
             "Yes - ESOP (listed or unlisted shares) is 'long-term capital asset other than residential property'. If held > 12 months (listed) or 24 months (unlisted) + sold: LTCG qualifies for Section 54F reinvestment exemption. Net consideration (not just gain) must be invested in ONE residential property in India within 2/3 year window."),
            ("What's taxed at ESOP exercise vs sale?",
             "Exercise: Section 17(2) perquisite - FMV at exercise minus exercise price = perquisite value, taxed at slab rate as salary. Employer deducts Section 192 TDS. Sale: Section 48 capital gain - sale price minus (exercise price + perquisite value) = capital gain. LTCG 12.5% (listed) or specific rate (unlisted). Section 54F reinvestment can exempt the capital gain portion."),
            ("Can Section 54F + Section 54EC be combined for large ESOP exit?",
             "Yes - common strategy. Example: INR 2 crore LTCG from ESOP sale → INR 50 lakh in Section 54EC bonds (max limit) + balance INR 1.5 crore invested in residential property under Section 54F. Both exemptions can be claimed simultaneously. Significantly reduces tax on large ESOP exit."),
            ("Does ESOP in US parent qualify for Section 54F?",
             "Specific analysis needed. If employee is Indian tax resident + sells US parent shares: Section 48 capital gain + treaty relief under India-US DTAA. Section 54F requires reinvestment in INDIAN residential property - foreign residential property doesn't qualify. For dual-tax situation (US tax person): coordinated with US capital gain + Form 1116 FTC."),
            ("Does BQP handle ESOP + Section 54F end-to-end?",
             "Yes - specialist practice. Pre-exercise planning + Section 17(2) perquisite computation + Section 192 TDS structuring + Section 48 capital gain computation + Section 54F eligibility + reinvestment property identification + CGAS deposit coordination + Section 54F + 54EC combination + ITR filing + Form 10E salary arrears relief + NRI LDC coordination. Standard engagement for ESOP exercise + sale events. WhatsApp +91 78018 87130."),
        ],
        "related_pairs": [("best-ca-section-54f-capital-gain-reinvestment-india.html", "Related", "Section 54F Full Guide"),
                          ("best-ca-esop-valuation-409a-rule-11ua-india.html", "Related", "ESOP Valuation CA")],
        "cta_h": "ESOP exercise + sale with Section 54F reinvestment planning?",
        "cta_b": "Section 17(2) perquisite + Section 48 capital gain + Section 54F reinvestment + Section 54EC combination + ITR. BQP integrated engagement.",
        "keywords": "CA Section 54F ESOP exercise sale reinvestment India, ESOP capital gain reinvestment CA, Section 17 2 perquisite ESOP CA, Section 54F ESOP CA India",
        "desc": "CA for Section 54F ESOP exercise + sale + reinvestment India: two-stage ESOP taxation (Section 17(2) perquisite at exercise + Section 48 capital gain at sale), Section 54F applicability for ESOP sale LTCG, specific combinations (Section 54F + 54EC bonds for large exits), common scenarios (Series A employee + US-HQ Indian employee + multi-year vest). CA Durgesh Chavda ESOP + capital gain specialist.",
    },
    {
        "slug": "ca-for-india-dividend-repatriation-foreign-parent-step-by-step",
        "title": "CA for India Dividend Repatriation to Foreign Parent (Step-by-Step)",
        "hero_em": "post-DDT dividend tax + treaty rate execution.",
        "lead": "Indian subsidiary paying dividend to foreign parent: post Dividend Distribution Tax (DDT) abolition April 2020, dividend taxed in shareholder's hands via Section 195 TDS. Default 20% + surcharge + cess; 10-15% under DTAA with TRC + Form 10F. Form 15CA + 15CB mandatory. Here's the complete step-by-step execution framework.",
        "kicker": "/ Dividend Repatriation Playbook &middot; Updated 2026-10-23",
        "sections_pairs": [
            ("/ Pre-dividend declaration", "Preparation.",
             "<ol>"
             "<li>Verify distributable profits: Section 123 Companies Act 2013 - dividend can only be declared out of current profit or accumulated past profit; must pass solvency test.</li>"
             "<li>Board resolution (final dividend requires shareholder approval; interim dividend board-only).</li>"
             "<li>Section 115QA buyback vs dividend decision for large repatriation.</li>"
             "<li>Specific Section 180 Companies Act compliance if dividend > specific threshold.</li>"
             "<li>Transfer Pricing + arm's-length verification for related-party context.</li>"
             "<li>Beneficial ownership of foreign parent + Press Note 3 compliance.</li>"
             "</ol>"),
            ("/ Foreign parent documents", "What to collect.",
             "<ul>"
             "<li><strong>TRC (Tax Residency Certificate)</strong>: from foreign parent's home country tax authority - annual.</li>"
             "<li><strong>Form 10F</strong>: electronic filing on India e-filing portal.</li>"
             "<li><strong>No-PE declaration</strong>: foreign parent confirms no Permanent Establishment in India.</li>"
             "<li><strong>Foreign PAN</strong>: if available (not strictly required; Section 206AA 20% applies if missing).</li>"
             "<li><strong>Beneficial ownership declaration</strong>: anti-GAAR / PPT compliance.</li>"
             "</ul>"),
            ("/ Form 15CA + 15CB execution", "The CA certification.",
             "<ol>"
             "<li>Form 15CA Part C (standard for dividend above INR 5 lakh): e-filed on Indian income tax portal by Indian subsidiary.</li>"
             "<li>Form 15CB: Chartered Accountant certificate stating: chargeability under Section 195, DTAA applicable, treaty rate, TDS deducted.</li>"
             "<li>CA (ICAI member) signs with UDIN.</li>"
             "<li>Treaty rate verification: country-specific DTAA + beneficial ownership + PPT.</li>"
             "<li>Standard DTAA dividend rates:</li>"
             "<li>&nbsp;&nbsp;&mdash; USA: 15% (25% ownership) / 25% (otherwise).</li>"
             "<li>&nbsp;&nbsp;&mdash; UK: 10% (10% ownership) / 15% (otherwise).</li>"
             "<li>&nbsp;&nbsp;&mdash; Singapore: 10% (25% ownership) / 15% (otherwise).</li>"
             "<li>&nbsp;&nbsp;&mdash; UAE: 10%.</li>"
             "<li>&nbsp;&nbsp;&mdash; Mauritius: 5% (10% ownership) / 15% (otherwise).</li>"
             "<li>&nbsp;&nbsp;&mdash; Netherlands / Germany / France: 10%.</li>"
             "</ol>"),
            ("/ TDS deposit + filing + remittance", "The execution.",
             "<ol>"
             "<li>TDS deposit by 7th of next month via Challan ITNS 281 under Section 195.</li>"
             "<li>Form 27Q quarterly return by 31 July / 31 October / 31 January / 31 May.</li>"
             "<li>Form 16A issued to foreign payee within quarterly timeline.</li>"
             "<li>Remittance via AD-I category bank: Form A2 + Form 15CA acknowledgement + Form 15CB attached.</li>"
             "<li>Bank releases SWIFT after documents verified.</li>"
             "<li>Foreign parent receives dividend net of TDS.</li>"
             "<li>Foreign parent claims FTC in home country tax return for Indian TDS paid.</li>"
             "</ol>"),
            ("/ Common dividend repatriation mistakes", "Where companies trip.",
             "<ul>"
             "<li>Section 206AA 20% rate when foreign parent PAN missing + TRC/Form 10F also missing.</li>"
             "<li>Over-withholding at 20% default when treaty rate (10-15%) applies with proper documentation.</li>"
             "<li>Section 194 (resident dividend TDS) confused with Section 195 (non-resident). Different rates + specific sections.</li>"
             "<li>Form 10F expired - TRC + Form 10F must be current for FY of dividend.</li>"
             "<li>Section 194 10% TDS on dividend to Indian shareholder confused with Section 195 for non-resident shareholder.</li>"
             "<li>Form MGT-14 if specific threshold crossed - specific resolution filing.</li>"
             "<li>Specific Section 123 Companies Act compliance missed - solvency + distributable profit verification.</li>"
             "</ul>"
             "<p><em>Last updated: 2026-10-23.</em></p>"),
        ],
        "faqs": [
            ("Is dividend from Indian subsidiary to foreign parent taxable in India?",
             "Yes - post DDT abolition April 2020, dividend taxable in foreign parent's hands. Section 195 TDS at 20% default + 10-15% treaty rate under DTAA with TRC + Form 10F. Indian subsidiary deducts TDS + deposits + Form 27Q + Form 16A to foreign parent."),
            ("What's the typical DTAA dividend rate?",
             "Varies by country: USA 15% (25% ownership) / 25% otherwise; UK 10% (10% ownership) / 15% otherwise; Singapore 10% (25% ownership) / 15% otherwise; UAE 10%; Mauritius 5% (10% ownership) / 15% otherwise; Netherlands/Germany/France 10%. TRC + Form 10F + beneficial ownership required to claim treaty rate."),
            ("Can we use buyback instead of dividend?",
             "Yes - alternative for large one-time repatriation. Section 115QA buyback tax 20% + surcharge on distributed income paid by Indian subsidiary. Receipt in parent's hands = capital gain but Section 10(34A) exempts buyback-related income. Materially different cash flow + tax position. Max 10-25% buyback per Companies Act + 2-year gap between buybacks."),
            ("What if TRC/Form 10F is missing?",
             "Section 206AA + Section 195 default: 20% + applicable surcharge + 4% cess. Treaty rate denied. Foreign parent can later claim refund via Indian ITR but immediate TDS at higher rate. Best practice: TRC + Form 10F obtained before dividend declaration."),
            ("Does BQP handle dividend repatriation for Indian subsidiary of foreign parent?",
             "Yes - standard engagement. Section 123 Companies Act compliance + board/shareholder resolution + Transfer Pricing arm's-length verification + TRC coordination with foreign parent + Form 10F e-filing + Form 15CA + 15CB preparation + Section 195 TDS deposit + Form 27Q + Form 16A + AD bank coordination + remittance. For Indian subsidiaries of US / UK / EU / Singapore / UAE parents making regular dividends. WhatsApp +91 78018 87130."),
        ],
        "related_pairs": [("repatriate-profits-india-foreign-parent.html", "Related", "Profit Repatriation Full Guide"),
                          ("form-15ca-15cb-foreign-remittance-india.html", "Related", "Form 15CA/15CB")],
        "cta_h": "Indian subsidiary paying dividend to foreign parent?",
        "cta_b": "Section 195 + TRC + Form 10F + Form 15CA/15CB + treaty rate + Form 27Q + AD bank. BQP integrated engagement for foreign-shareholder Indian subsidiaries.",
        "keywords": "CA India dividend repatriation foreign parent step by step, Section 195 dividend TDS CA India, Form 15CB dividend CA, DTAA dividend treaty rate CA India",
        "desc": "CA for India dividend repatriation to foreign parent step-by-step: pre-declaration (Section 123 distributable profits + solvency + resolution + TP arm's-length) + foreign parent documents (TRC + Form 10F + no-PE + beneficial ownership) + Form 15CA + 15CB execution (treaty rate verification + CA UDIN) + TDS deposit + Form 27Q + Form 16A + AD bank remittance. CA Durgesh Chavda specialist practice.",
    },
    {
        "slug": "ca-for-india-foreign-director-nominee-service-step-by-step",
        "title": "CA for India Resident Director Nominee Service (Step-by-Step)",
        "hero_em": "Section 149(3) nominee director arrangement.",
        "lead": "Foreign-owned Indian subsidiary requires at least one resident director (Section 149(3) Companies Act 2013). If foreign parent has no India-resident person, BQP provides CA-qualified nominee resident director as standard governance service. 100+ nominee director arrangements executed. Here's the complete step-by-step framework.",
        "kicker": "/ Nominee Director Service &middot; Updated 2026-10-23",
        "sections_pairs": [
            ("/ Section 149(3) requirement", "The statutory rule.",
             "<ul>"
             "<li>Every Indian company (Pvt Ltd + Public Ltd) must have minimum directors (2 for Pvt Ltd; 3 for Public Ltd).</li>"
             "<li>At least ONE director must be <strong>resident of India</strong> - stayed in India 182+ days in preceding FY.</li>"
             "<li>Non-resident Indians (NRIs) with Indian passport but non-resident status: do NOT qualify.</li>"
             "<li>Foreign citizens who are tax-residents of India (182+ days physical): qualify.</li>"
             "<li>Non-compliance: Section 164 director disqualification risk + ROC filing blockage + Section 450 default penalty.</li>"
             "</ul>"),
            ("/ When nominee director needed", "Common scenarios.",
             "<ul>"
             "<li>Foreign parent incorporating Indian WOS: 2 foreign directors appointed; need 1 India-resident nominee.</li>"
             "<li>India-resident director resigns: company left without resident director; 30 days to appoint replacement.</li>"
             "<li>Expat executive relocates out of India: director who was India-resident loses that status after 180+ days abroad.</li>"
             "<li>Dormant Indian subsidiary: not actively operated but still needs 1 resident director for compliance.</li>"
             "</ul>"),
            ("/ BQP nominee director service workflow", "Step-by-step.",
             "<ol>"
             "<li><strong>Nominee Director Agreement</strong>: signed between foreign parent + BQP nominee partner. Defines scope + fee + indemnity.</li>"
             "<li><strong>Pre-signed resignation</strong>: nominee signs undated DIR-11 resignation form; held in escrow (can be used immediately if nominee needs to be replaced).</li>"
             "<li><strong>DIN application</strong>: nominee's Director Identification Number if not already (BQP partners have DIN).</li>"
             "<li><strong>DSC</strong>: Digital Signature Certificate for ROC filings.</li>"
             "<li><strong>Board resolution</strong>: company's board appoints nominee as director + specific disclosure of nominee relationship.</li>"
             "<li><strong>Form DIR-12</strong>: filed with ROC within 30 days of appointment.</li>"
             "<li><strong>Indemnity</strong>: foreign parent indemnifies nominee against claims arising from acts of other directors / company's operations. Standard legal protection.</li>"
             "<li><strong>D&amp;O insurance (optional)</strong>: foreign parent may purchase D&amp;O insurance covering Indian subsidiary directors.</li>"
             "</ol>"),
            ("/ Nominee director's scope + what they do NOT do", "Clear boundaries.",
             "<p><strong>Nominee DOES</strong>:</p>"
             "<ul>"
             "<li>Named as director in Indian company's records (MCA / ROC filings).</li>"
             "<li>Holds valid DIN + DSC.</li>"
             "<li>Signs required ROC filings: AOC-4, MGT-7, DIR-12, PAS-3, MGT-14 as applicable.</li>"
             "<li>Attends board meetings (video / telephonic) when quorum needs resident director.</li>"
             "<li>Signs resolutions requiring resident director signature.</li>"
             "<li>Files annual DIR-3 KYC.</li>"
             "<li>Signs required bank KYC / banking documents.</li>"
             "</ul>"
             "<p><strong>Nominee does NOT</strong>:</p>"
             "<ul>"
             "<li>Participate in business operations / strategy / commercial decisions.</li>"
             "<li>Sign commercial contracts / customer agreements / vendor contracts.</li>"
             "<li>Represent the company publicly.</li>"
             "<li>Access operational funds / treasury / payroll.</li>"
             "<li>Make day-to-day business judgments.</li>"
             "</ul>"
             "<p>Role is purely statutory governance - satisfying Section 149(3), not running the business.</p>"),
            ("/ Replacement + transition workflow", "If nominee changes.",
             "<ol>"
             "<li>Reasons for replacement: nominee's own change of circumstances; foreign parent prefers different nominee; appointment of new India-resident director from parent group.</li>"
             "<li>Pre-signed resignation (DIR-11) activated - specific date entered.</li>"
             "<li>Successor nominee's DIR-12 (within 30 days of appointment).</li>"
             "<li>Section 164 disqualification check: successor must not be disqualified.</li>"
             "<li>Bank KYC refresh: new signatory authorisation.</li>"
             "<li>MCA records updated: company's director list updated.</li>"
             "<li>Updated Nominee Director Agreement with new nominee.</li>"
             "<li>Standard replacement timeline: 30-45 days end-to-end.</li>"
             "</ol>"
             "<p><em>Last updated: 2026-10-23.</em></p>"),
        ],
        "faqs": [
            ("Why do foreign-owned Indian subsidiaries need nominee director?",
             "Section 149(3) Companies Act 2013: every Indian company must have at least one director resident in India (stayed 182+ days in preceding FY). If foreign parent has no India-resident person on leadership team: nominee resident director required. Standard arrangement for 90%+ of foreign WOS incorporations."),
            ("What's the legal risk of being a nominee director?",
             "Directors owe fiduciary duties (Section 166) + liable for non-compliance by company (Section 164 disqualification, Section 450 default penalties). Mitigated by: scope restriction (nominee doesn't participate in operational decisions), foreign parent's indemnity, regular DIR-3 KYC + DIR-8 + MBP-1 compliance, D&O insurance (optional). BQP structuring includes standard protective framework."),
            ("Can my Indian employee be the resident director instead?",
             "Yes if they are tax-resident in India + willing. However: directors have personal liability under Companies Act; many employees refuse. Also creates employer-director conflict in HR matters. External CA-qualified nominee (like BQP partners) is cleaner structurally. Many foreign parents choose BQP nominee specifically for professional separation."),
            ("How does BQP's nominee director arrangement work commercially?",
             "Nominee Director Agreement (annual) + specific scope + indemnity + pre-signed resignation (undated) + replacement workflow. Scope-based annual fee. CA-qualified nominee + specific statutory governance + no operational participation. Standard engagement for foreign WOS incorporations + ongoing arrangements."),
            ("Does BQP provide nominee director service for foreign companies?",
             "Yes - 100+ nominee director arrangements executed. For foreign WOS incorporations + replacement scenarios + dormant subsidiary maintenance. CA-qualified partner nominee + full Nominee Director Agreement + indemnity + pre-signed resignation + replacement workflow + annual DIR-3 KYC + required ROC filings. Standard service for foreign parents in US / UK / EU / Singapore / UAE. WhatsApp +91 78018 87130."),
        ],
        "related_pairs": [("nominee-resident-director-india-foreign-company.html", "Related", "Nominee Director Full Guide"),
                          ("foreign-company-setup-indian-subsidiary-wos.html", "Related", "Foreign WOS Setup")],
        "cta_h": "Foreign parent needing Section 149(3) resident director?",
        "cta_b": "BQP CA-qualified nominee + Nominee Director Agreement + indemnity + pre-signed resignation + replacement workflow + annual DIR-3 KYC. Standard engagement for foreign WOS.",
        "keywords": "CA India resident director nominee service step by step, Section 149(3) nominee director foreign company India CA, nominee director Section 149 CA India",
        "desc": "CA for India resident director nominee service (step-by-step): Section 149(3) requirement + when nominee needed + BQP workflow (Nominee Director Agreement + pre-signed resignation + DIN/DSC + board resolution + Form DIR-12 + indemnity + optional D&O insurance) + nominee's scope boundaries (statutory governance yes; operational decisions no) + replacement workflow. 100+ nominee arrangements executed. CA Durgesh Chavda specialist practice.",
    },
]

for p in PAGES:
    html = quick_page(
        slug=p["slug"], title=p["title"], hero_em=p["hero_em"], lead=p["lead"],
        kicker=p["kicker"], sections_pairs=p["sections_pairs"],
        faqs=p["faqs"], related_pairs=p["related_pairs"],
        cta_h=p["cta_h"], cta_b=p["cta_b"],
        keywords=p["keywords"], desc=p["desc"],
    )
    write_page(p["slug"], html)

print(f"Batch AA complete: {len(PAGES)} pages")
