# -*- coding: utf-8 -*-
"""Batch M: 12 inbound-India SEO pages for foreign clients + /for-foreign-clients hub.

Target searcher: foreign company / foreign founder / foreign VC / foreign CFO
who needs an Indian CA while staying outside India. Each page addresses a specific
high-intent query that is severely underserved on bqp today.
"""
from build_lib import page, write_page

# 1. Foreign company setting up Indian WOS
write_page("foreign-company-setup-indian-subsidiary-wos", page(
    slug="foreign-company-setup-indian-subsidiary-wos",
    title="Set Up Indian Subsidiary (WOS) from USA / UK / Singapore 2026 - BQP",
    description="Complete guide for foreign companies setting up a Wholly-Owned Subsidiary in India: FDI automatic route, Pvt Ltd incorporation, resident director, FEMA FC-GPR, PAN TAN, FDI sector caps. Done remotely by Indian CA from India for USA / UK / EU / Singapore / UAE parent companies. Working CA guide by Durgesh Chavda.",
    keywords="Indian subsidiary from USA, WOS India foreign parent, set up Pvt Ltd India remotely, India company incorporation foreign company, FDI automatic route India, foreign-owned Indian subsidiary setup",
    hero_kicker="/ Foreign Clients &middot; India WOS Setup &middot; Updated 2026-10-13",
    hero_title_html="Set up an Indian WOS <em>without ever landing in India.</em>",
    hero_lead="Foreign company (USA Delaware C-Corp, UK Ltd, Singapore Pte Ltd, UAE FZ-LLC, etc.) wanting to incorporate a Wholly-Owned Subsidiary in India: fully remote execution from India. Automatic FDI route for most sectors. 30-45 day timeline. Resident director arranged. Bank account, FDI reporting (FC-GPR), PAN, TAN, GST — one engagement, one firm. Here's the complete playbook.",
    sections=[
        ("/ The default structure", "WOS as Pvt Ltd.",
         "<p>For most foreign companies entering India, the right structure is a <strong>Private Limited Company (Pvt Ltd)</strong> with 100% foreign shareholding (Wholly-Owned Subsidiary, 'WOS'). Benefits:</p>"
         "<ul>"
         "<li>FDI permitted via <strong>automatic route</strong> in most sectors (no prior approval needed).</li>"
         "<li>Separate legal entity &mdash; limited liability.</li>"
         "<li>Easy to operate commercially (sign contracts, hire employees, invoice customers).</li>"
         "<li>Standard tax rates (25% / 22% under Section 115BAA).</li>"
         "<li>Easy to repatriate profits via dividend (subject to Section 195 TDS + DTAA).</li>"
         "</ul>"
         "<p>Alternatives (less common): Branch Office, Liaison Office, Project Office, LLP (foreign investment restricted). See our separate guide on <a href='branch-office-vs-liaison-vs-wos-india-foreign.html'>Branch vs Liaison vs WOS</a>.</p>"),
        ("/ Pre-incorporation requirements", "What foreign parent must have.",
         "<ul>"
         "<li><strong>Minimum 2 shareholders</strong>: foreign parent company + 1 nominee (nominal 1-share holder; can be another entity or individual).</li>"
         "<li><strong>Minimum 2 directors</strong>: at least ONE must be an <strong>Indian resident</strong> (physically present in India &gt;120 days in the FY). BQP arranges resident director if parent has no India-resident person.</li>"
         "<li><strong>Foreign director's documents</strong>: passport + address proof (utility bill/bank statement, apostilled or Hague Convention authenticated).</li>"
         "<li><strong>Foreign parent documents</strong>: Certificate of Incorporation + Board resolution authorising India subsidiary + apostille/authentication.</li>"
         "<li><strong>Registered office in India</strong>: can be virtual office / co-working / BQP office address initially; must be updated to actual within 30 days.</li>"
         "<li><strong>FDI sector check</strong>: verify the proposed business falls under automatic route (default for most IT/SaaS/trading/manufacturing). Prohibited sectors: lottery, chit funds, real estate dealing, atomic energy. Press Note 3 (2020): any investment from countries sharing land border with India (China, Pakistan, Bangladesh, Nepal, Bhutan, Myanmar, Afghanistan) requires prior government approval.</li>"
         "</ul>"),
        ("/ Incorporation workflow", "30-45 day execution.",
         "<ol>"
         "<li><strong>DSC (Digital Signature Certificate)</strong> for all proposed directors &mdash; 2-3 days; foreign directors can obtain via online KYC + apostilled passport.</li>"
         "<li><strong>DIN (Director Identification Number)</strong> applied through SPICe+ Part B &mdash; approved along with incorporation.</li>"
         "<li><strong>Name reservation</strong> via SPICe+ Part A &mdash; propose 2 names; MCA approves within 1-2 days.</li>"
         "<li><strong>SPICe+ Part B incorporation</strong>: MOA, AOA, declarations, consent forms, apostilled documents. Filing fee + stamp duty vary by state and authorised capital.</li>"
         "<li><strong>Certificate of Incorporation + PAN + TAN</strong>: issued together by MCA / Income Tax Department. 5-10 working days.</li>"
         "<li><strong>Bank account</strong>: open current account with HDFC / ICICI / Kotak / Axis. Resident director typically signs; foreign director KYC can be remote. 7-14 days.</li>"
         "<li><strong>Share capital remittance</strong>: foreign parent wires subscription money to India bank account. AD bank issues FIRC (Foreign Inward Remittance Certificate).</li>"
         "<li><strong>FC-GPR filing</strong> within 30 days of receiving remittance &mdash; mandatory FEMA compliance. Non-filing attracts compounding penalty.</li>"
         "<li><strong>Post-incorporation</strong>: GST registration (if applicable), Professional Tax (state-specific), Shops &amp; Establishment, PF &amp; ESI (once headcount triggers).</li>"
         "</ol>"),
        ("/ Ongoing compliance (year 1 onwards)", "The India compliance calendar.",
         "<ul>"
         "<li><strong>Statutory audit</strong>: mandatory for all Pvt Ltd regardless of size. Signed by an Indian CA. Done remotely for foreign-owned companies &mdash; BQP delivers audit from India.</li>"
         "<li><strong>Income tax return</strong>: Form ITR-6 by 31 October (if TP applicable: 30 November).</li>"
         "<li><strong>Tax audit</strong>: if turnover &gt; INR 1 crore.</li>"
         "<li><strong>Transfer pricing audit (Form 3CEB)</strong>: mandatory for any transaction with foreign parent (always &gt; INR 1 crore threshold triggered immediately). Form 3CEB by 31 October.</li>"
         "<li><strong>ROC annual filings</strong>: AOC-4 (financials), MGT-7 (annual return).</li>"
         "<li><strong>FLA Return (RBI)</strong>: annual filing of foreign liabilities &amp; assets &mdash; <a href='fla-return-foreign-liabilities-assets-rbi-india.html'>our FLA guide</a>.</li>"
         "<li><strong>GST monthly / quarterly returns</strong>: GSTR-1 + GSTR-3B.</li>"
         "<li><strong>TDS quarterly returns</strong>: Form 26Q / 24Q.</li>"
         "<li><strong>Board meetings</strong>: minimum 4 per year (quarterly).</li>"
         "<li><strong>AGM</strong>: within 6 months of FY end (30 September).</li>"
         "</ul>"
         "<p>BQP runs this entire calendar remotely. Foreign parent gets quarterly MIS + annual audited financials.</p>"),
        ("/ What foreign clients often get wrong", "Avoidable mistakes.",
         "<ul>"
         "<li><strong>Press Note 3 trap</strong>: investor based in China / Hong Kong routing via Singapore holdco. Beneficial ownership check applies &mdash; prior government approval needed. Must disclose BO.</li>"
         "<li><strong>FDI sector cap violation</strong>: assuming 100% FDI permitted when sector cap is lower (e.g., multi-brand retail trading 51%, print media 26%, defence 74%). Pre-check.</li>"
         "<li><strong>No resident director</strong>: trying to incorporate with only foreign directors. Section 149(3) Companies Act requires at least 1 director to be resident in India (&gt;120 days in FY).</li>"
         "<li><strong>FC-GPR missed deadline</strong>: 30-day window from receipt of remittance. Late filing requires compounding under FEMA Section 13 &mdash; INR 10,000-50,000 per instance.</li>"
         "<li><strong>Apostille vs attestation confusion</strong>: Hague Convention member countries (USA, UK, EU, Singapore, UAE, etc.) use apostille. Non-Hague countries need embassy attestation + MEA attestation chain. Different docs; different timelines.</li>"
         "<li><strong>Missing Form 3CEB</strong>: thinking TP audit doesn't apply because 'it's just a subsidiary of my own company'. Any transaction with foreign parent is Associated Enterprise &mdash; Form 3CEB mandatory. See <a href='transfer-pricing-india-foreign-mnc.html'>our TP guide</a>.</li>"
         "</ul>"
         "<p><em>Last updated: 2026-10-13.</em></p>"),
    ],
    faqs=[
        ("Can a US / UK / Singapore company own 100% of an Indian subsidiary?",
         "Yes - via FDI automatic route in most sectors. 100% foreign ownership of a Pvt Ltd WOS is standard. Exceptions: prohibited sectors (lottery, chit funds, real estate dealing, atomic energy) and sector-cap limited sectors (multi-brand retail, print media, defence). Press Note 3 restriction applies for countries sharing land border with India (China, Pakistan, Bangladesh, Nepal, Bhutan, Myanmar, Afghanistan) requiring prior government approval."),
        ("Do I need to visit India to incorporate my Indian subsidiary?",
         "No. Full remote execution. Foreign directors can obtain DSC + DIN remotely via online KYC with apostilled passport. Documents (MOA/AOA/consents) signed digitally. Bank account can be opened with foreign director KYC (video or in-person at bank's foreign branch). BQP has handled 100+ foreign-WOS incorporations without the foreign parent ever landing in India."),
        ("Why is a resident director mandatory in India?",
         "Section 149(3) Companies Act 2013: every Indian company must have at least one director who has stayed in India for 182 days in the preceding FY (effectively a resident). This is to ensure accountable local presence. BQP arranges resident director nominee if the parent has no India-resident person - typical fee USD 1,500-3,000/year scope-based."),
        ("How long does Indian WOS incorporation take?",
         "30-45 days end-to-end: DSC (3 days) + name reservation (2 days) + SPICe+ incorporation (10 days) + bank account (14 days) + FC-GPR filing after capital remittance (variable). The longest step is foreign document apostille which can take 7-21 days depending on the issuing country."),
        ("What is Form FC-GPR?",
         "Foreign Currency - Gross Provisional Return. Mandatory FEMA filing to RBI within 30 days of receiving foreign share subscription money. Reports: shareholder details, remittance amount, equity issued, pricing method. Non-filing attracts FEMA compounding fee under Section 13. Core service we deliver as part of standard WOS setup engagement."),
        ("Does BQP handle Indian WOS setup for foreign companies?",
         "Yes - this is a core service. Full remote execution from India: DSC/DIN, SPICe+ incorporation, resident director arrangement, bank account coordination, FC-GPR filing, PAN/TAN/GST, FLA Return, annual audit + ROC compliance, TP documentation (Form 3CEB). Standard engagement for US / UK / EU / Singapore / UAE parents. WhatsApp +91 78018 87130."),
    ],
    related=[
        ("branch-office-vs-liaison-vs-wos-india-foreign.html", "Guide", "Branch vs Liaison vs WOS"),
        ("transfer-pricing-india-foreign-mnc.html", "Guide", "TP for Foreign MNC"),
    ],
    cta_headline="US / UK / Singapore / UAE company planning Indian WOS?",
    cta_body="Full remote execution from India. DSC + SPICe+ + resident director + bank account + FC-GPR + GST + annual compliance under one firm. Standard 30-45 day timeline. Scope-based engagement.",
))

# 2. Due diligence of Indian company for foreign buyer
write_page("due-diligence-indian-company-foreign-buyer", page(
    slug="due-diligence-indian-company-foreign-buyer",
    title="Due Diligence of Indian Company for Foreign Buyer | M&A VC Fund - BQP",
    description="Comprehensive due diligence on Indian target company for foreign M&A buyer / VC / PE investor: financial DD, tax DD (GST / TDS / FEMA / Income Tax), legal DD (ROC / contracts / IP), compliance DD, QoE (quality of earnings). Delivered remotely by Indian CA from India for US / UK / EU / Singapore / UAE acquirers. Working CA guide by Durgesh Chavda.",
    keywords="due diligence Indian company foreign buyer, India M&A due diligence CA, tax due diligence India, financial DD India target, India target company diligence",
    hero_kicker="/ Foreign Clients &middot; India DD &middot; Updated 2026-10-13",
    hero_title_html="India target due diligence, <em>end to end from India.</em>",
    hero_lead="Foreign M&amp;A buyer, VC fund, PE firm or strategic acquirer evaluating an Indian target: comprehensive remote due diligence delivered from India. Financial, tax, legal, FEMA, compliance, HR, IT, data room review. 3-6 week turnaround. Red-flag report + working-paper file + buyer counsel coordination. Here's what proper India DD looks like.",
    sections=[
        ("/ The India DD stack", "Six workstreams.",
         "<p><strong>Standard India target DD covers six workstreams</strong>:</p>"
         "<ol>"
         "<li><strong>Financial DD</strong>: historical P&amp;L normalisation, revenue recognition quality (ASC 606 / Ind AS 115 adjustments), working capital bridge, debt + cash position, QoE (quality of earnings), key customer concentration, AR aging, inventory valuation.</li>"
         "<li><strong>Tax DD</strong>: Income Tax exposure (open years, outstanding scrutiny notices, pending appeals, Section 143(2) / 148 risks), GST exposure (unmatched 2A/2B, Section 17(5) blocked ITC taken, pending demand notices), TDS exposure (Section 201 interest, 234E late fee, unmatched Form 26AS), FEMA exposure (missed FC-GPR / FLA / APR, compounding risk), Transfer Pricing exposure (Form 3CEB arm's-length defensibility).</li>"
         "<li><strong>Legal DD</strong>: incorporation docs + MOA/AOA, share capital history, cap table + dilution, shareholder agreements, employment contracts, customer/vendor contracts, IP ownership (patents, trademarks, copyrights, software licensing), litigation (pending + threatened), regulatory licences (RBI, SEBI, sector-specific).</li>"
         "<li><strong>Compliance DD</strong>: ROC filings status (AOC-4, MGT-7, PAS-6 for Rule 9B companies, DPT-3, MSME Form 1), board + AGM resolutions, statutory registers, DIR-3 KYC status.</li>"
         "<li><strong>HR + payroll DD</strong>: employee contracts, PF/ESI compliance, gratuity + leave encashment provisions, labour law compliance (CLRA, Factories Act, Shops &amp; Establishment), ESOP + sweat equity history.</li>"
         "<li><strong>IT / cybersecurity DD</strong> (if scope): data protection compliance (DPDP Act 2023), security certifications, source code escrow, software licensing.</li>"
         "</ol>"),
        ("/ India-specific red flags foreign buyers miss", "What's not in a US / UK DD template.",
         "<ul>"
         "<li><strong>Pending Income Tax reassessment under Section 148 / 148A</strong>: can resurrect old years. Even if current year is clean, prior-year reassessment can create INR crore exposure. Review Section 148A show-cause notices + any pending appeals.</li>"
         "<li><strong>GST demand under Section 73 / 74</strong>: assessment of unpaid tax within 3 years (73) or 5 years (74) with 100% penalty under 74. Check for ASMT-10, DRC-01, DRC-03 history.</li>"
         "<li><strong>Section 17(5) GST blocked ITC taken</strong>: many Indian companies routinely claim ITC on motor vehicles, construction materials, employee insurance which is specifically blocked. Reverses with interest.</li>"
         "<li><strong>Form 26AS vs TDS claimed mismatch</strong>: TDS claimed in ITR but not reflected in Form 26AS (because deductor didn't file 26Q) &mdash; tax department has disallowed. Common issue.</li>"
         "<li><strong>FEMA non-compliance</strong>: missed FC-GPR / FLA Return / APR filings. Compounding penalty under Section 13.</li>"
         "<li><strong>Transfer pricing weakness</strong>: Form 3CEB filed but benchmarks weak / incomparables used. Scrutiny risk + addition exposure.</li>"
         "<li><strong>Section 56(2)(viib) angel tax</strong>: if target raised equity above FMV from non-residents in the past, Section 56(2)(viib) was applicable until Finance Act 2024 abolished it. Historical liability may remain.</li>"
         "<li><strong>Dematerialisation of unlisted shares (Rule 9B)</strong>: since Oct 2024, mandatory. Non-compliance blocks share transfer in M&amp;A &mdash; see our <a href='dematerialisation-unlisted-shares-india-mandatory.html'>demat guide</a>. Fix pre-closing.</li>"
         "<li><strong>Pending Companies Act notices (ROC)</strong>: AOC-4 / MGT-7 non-filing, Section 164 director disqualification, DIR-3 KYC lapses.</li>"
         "<li><strong>IP ownership gap</strong>: Indian subsidiary developed IP but no written assignment to parent. Patents / trademarks sitting with employees as inventors.</li>"
         "</ul>"),
        ("/ Timeline + deliverables", "What a 4-week DD looks like.",
         "<p><strong>Week 1</strong>: data room access, document request list issued, initial review of financials (Ind AS or IFRS). First management session (Q&amp;A).</p>"
         "<p><strong>Week 2</strong>: deep-dive into tax position (Income Tax + GST + TDS + FEMA + TP). Site visit / plant audit if operational business. Second management session.</p>"
         "<p><strong>Week 3</strong>: legal review, contract review, IP review, HR review, compliance log review. Third management session (clarifications).</p>"
         "<p><strong>Week 4</strong>: drafting of final report. Red-flag summary. Quantified tax / FEMA / compliance exposure. Working-paper file. Draft report shared with buyer counsel.</p>"
         "<p><strong>Deliverables</strong>:</p>"
         "<ul>"
         "<li>Executive summary (3-5 pages) &mdash; red flags, quantified exposure, go/no-go on key issues, SPA points.</li>"
         "<li>Full DD report (40-80 pages) &mdash; workstream by workstream findings.</li>"
         "<li>Working-paper file &mdash; schedules, computations, supporting docs.</li>"
         "<li>SPA input list &mdash; representations, warranties, indemnities, specific escrow asks.</li>"
         "<li>Open-items list &mdash; residual questions not resolved during DD.</li>"
         "<li>Post-closing integration list &mdash; items to be fixed in first 90 days of ownership.</li>"
         "</ul>"
         "<p><em>Last updated: 2026-10-13.</em></p>"),
        ("/ Scope and fee framework", "How we scope.",
         "<p>India DD scope depends on target size + complexity:</p>"
         "<ul>"
         "<li><strong>Small target (revenue &lt; INR 10 crore)</strong>: ~2-3 week turnaround. Financial + tax DD only. Scope-based pricing.</li>"
         "<li><strong>Mid-market target (INR 10-100 crore)</strong>: 3-5 week turnaround. Full six-workstream DD. QoE build. Site visit if manufacturing/retail.</li>"
         "<li><strong>Large target (INR 100 crore+)</strong>: 6-8 week turnaround. Full DD + QoE + synergy analysis + post-closing integration plan.</li>"
         "<li><strong>Follow-on diligence</strong>: for additional rounds / expansions. Standard retainer basis.</li>"
         "</ul>"
         "<p>BQP coordinates with buyer counsel (US / UK / Singapore counsel) + buyer internal finance team. Weekly status calls. Final report delivered in buyer's preferred format (PDF + Excel + Word for SPA input).</p>"),
    ],
    faqs=[
        ("Can an Indian CA firm do remote due diligence for a US / UK acquirer?",
         "Yes - this is standard for cross-border M&A. Target data room is accessed online, management calls happen on Zoom, site visit (if operational business) is done by India team and reported with photos / videos. Final deliverables (report + schedules) are in English, formatted for US / UK / Singapore counsel's SPA integration. BQP has run DDs for US VC, UK PE, Singapore family office, UAE strategic buyers."),
        ("How long does India DD take?",
         "4 weeks for mid-market target (INR 10-100 crore). 2-3 weeks for small target. 6-8 weeks for large / complex target. Timeline depends on data room completeness, management responsiveness, and whether a site visit is required. Weekly status call keeps buyer informed."),
        ("What specific India tax risks do foreign buyers often miss?",
         "Section 148/148A reassessment of prior years, GST Section 73/74 demand exposure, Section 17(5) blocked ITC routinely claimed, Form 26AS vs TDS mismatch, FEMA compounding exposure for missed FC-GPR / FLA / APR, Transfer Pricing weakness on Form 3CEB benchmarks, Section 56(2)(viib) legacy angel tax, dematerialisation (Rule 9B) non-compliance blocking share transfer."),
        ("Can the DD report be used for SPA negotiations?",
         "Yes - DD report feeds directly into SPA. Each identified risk becomes a specific indemnity / escrow / price adjustment. BQP delivers an SPA input list: representations needed, warranty exceptions, specific escrow asks (e.g., INR X lakh for pending Section 143(2) notice outcome), tax indemnity period."),
        ("What is QoE (Quality of Earnings) for India target?",
         "Normalised EBITDA calculation adjusted for one-time items, revenue recognition quality, working capital normalisation, promoter-related expenses (owner's compensation, related-party rent), accounting policy adjustments. Essential for valuation negotiation. Standard output alongside financial DD."),
        ("Does BQP handle M&A due diligence for foreign buyers of Indian targets?",
         "Yes - this is a core service. Full six-workstream DD, QoE, SPA input, buyer counsel coordination. Mid-market deals (INR 10-100 crore) are our sweet spot but we handle larger. Standard engagement scoped per target size + complexity. WhatsApp +91 78018 87130."),
    ],
    related=[
        ("foreign-company-setup-indian-subsidiary-wos.html", "Guide", "India WOS Setup"),
        ("ma-transactions.html", "Service", "M&A Transactions"),
    ],
    cta_headline="Foreign buyer evaluating an Indian target?",
    cta_body="4-week remote DD from India covering financial / tax / legal / FEMA / compliance / HR / IT. Red-flag report + SPA input + buyer counsel coordination. Standard mid-market engagement scope-based.",
))

# 3. Form 15CA / 15CB
write_page("form-15ca-15cb-foreign-remittance-india", page(
    slug="form-15ca-15cb-foreign-remittance-india",
    title="Form 15CA / 15CB for Foreign Remittance from India 2026 - BQP",
    description="Form 15CA (self-declaration) + 15CB (CA certificate) mandatory for foreign remittance from India under Section 195 + Rule 37BB. Thresholds (INR 5 lakh), DTAA relief, Tax Residency Certificate (TRC) + Form 10F, PE analysis. CA certificate issued remotely from India for any foreign payee globally. Working CA guide by Durgesh Chavda.",
    keywords="Form 15CA 15CB CA certificate India, foreign remittance 15CB CA, Section 195 TDS 15CA 15CB, Rule 37BB 15CA 15CB, 15CB CA India remote",
    hero_kicker="/ Foreign Clients &middot; 15CA / 15CB &middot; Updated 2026-10-13",
    hero_title_html="Form 15CA / 15CB, <em>the CA certificate that unlocks the wire.</em>",
    hero_lead="Every foreign remittance from India above the threshold needs Form 15CA (payer's self-declaration) + Form 15CB (Chartered Accountant's certificate). The AD bank won't release the SWIFT without them. BQP delivers 15CB remotely for any foreign payee &mdash; dividend to US holdco, royalty to UK licensor, service fee to Singapore vendor, salary to Dubai consultant. 24-48 hour turnaround. Here's the complete framework.",
    sections=[
        ("/ Why 15CA + 15CB exist", "Section 195 + Rule 37BB.",
         "<p>Section 195 Income Tax Act: any person making payment to a non-resident that is chargeable to tax in India must deduct TDS. Rule 37BB (introduced 2013, revised repeatedly) operationalises this via Form 15CA (payer declaration) and Form 15CB (CA certificate on taxability and rate).</p>"
         "<p>The AD bank processing the SWIFT asks for 15CA acknowledgement AND (where applicable) 15CB before releasing foreign exchange. No 15CA/15CB &rarr; no wire.</p>"
         "<p><strong>The four Parts of Form 15CA</strong>:</p>"
         "<ul>"
         "<li><strong>Part A</strong>: for remittances up to <strong>INR 5 lakh in a FY</strong>, aggregate per payee. No 15CB needed; only self-declaration.</li>"
         "<li><strong>Part B</strong>: for remittances above INR 5 lakh where an order under Section 195(2)/(3) or 197 has been obtained (NIL / lower deduction certificate).</li>"
         "<li><strong>Part C</strong>: for remittances above INR 5 lakh where Form 15CB (CA certificate) is attached. <strong>This is the standard case.</strong></li>"
         "<li><strong>Part D</strong>: for remittances not chargeable to tax under the Act (list of 33 specified categories).</li>"
         "</ul>"),
        ("/ When Form 15CB is mandatory", "The core use case.",
         "<p>Form 15CB (CA certificate) is required when:</p>"
         "<ul>"
         "<li>Remittance is &gt; INR 5 lakh aggregate per payee per FY, AND</li>"
         "<li>The remittance is chargeable to tax in India, AND</li>"
         "<li>No Section 195(2)/(3) / 197 order has been obtained.</li>"
         "</ul>"
         "<p>Standard scenarios needing 15CB:</p>"
         "<ul>"
         "<li>Dividend from Indian subsidiary to foreign parent &mdash; Section 195 TDS 20% (10% under treaty with TRC).</li>"
         "<li>Royalty / FTS (Fees for Technical Services) to foreign licensor &mdash; Section 115A 20% (10% under treaty).</li>"
         "<li>Interest on ECB / NCD to foreign lender &mdash; Section 195 20% (treaty rate may apply).</li>"
         "<li>Capital gains on Indian securities to foreign investor &mdash; Section 112A / 115AD rates.</li>"
         "<li>Branch office remittance to head office.</li>"
         "<li>Service fee to foreign vendor &mdash; nature-dependent (FTS vs business income under treaty).</li>"
         "<li>Salary to foreign consultant / independent contractor &mdash; Section 192 vs Section 194R / 195 depending on employment vs independent.</li>"
         "<li>Reimbursement of expenses &mdash; chargeability depends on facts.</li>"
         "</ul>"),
        ("/ Form 15CB mechanics", "What the CA certifies.",
         "<p>Form 15CB is a CA certificate stating:</p>"
         "<ul>"
         "<li>Nature of remittance (dividend / royalty / FTS / interest / capital gain / business income / salary / reimbursement, etc.).</li>"
         "<li>Chargeability under the Act (Section 9, Section 115A, Section 195, specific sections).</li>"
         "<li>Applicable DTAA, if any, and treaty rate.</li>"
         "<li>TDS deducted at applicable rate.</li>"
         "<li>Reasons supporting the taxability / non-taxability conclusion.</li>"
         "</ul>"
         "<p>Key documents needed:</p>"
         "<ul>"
         "<li>Invoice / agreement supporting the remittance.</li>"
         "<li>Payee's <strong>Tax Residency Certificate (TRC)</strong> &mdash; mandatory for claiming DTAA benefit.</li>"
         "<li>Payee's <strong>Form 10F</strong> &mdash; electronic Form 10F now mandatory via e-filing portal (post Oct 2023). Even if TRC provides most info, Form 10F additional.</li>"
         "<li>Payee's PAN (if available) &mdash; without PAN, Section 206AA kicks in: rate = higher of (a) treaty rate, (b) 20%.</li>"
         "<li>No-PE declaration from payee (if claiming business income exemption under treaty).</li>"
         "</ul>"),
        ("/ Common 15CA / 15CB mistakes", "What foreign payees should push back on.",
         "<ul>"
         "<li><strong>Payer withholding at 20% ignoring treaty</strong>: when TRC + Form 10F are available, treaty rate (usually 10-15%) applies. Over-withholding delays payee's refund / clog in Indian tax system.</li>"
         "<li><strong>Payer claiming 'reimbursement' without substance</strong>: reimbursement must be bare cost, no mark-up, documented back-to-back. Else chargeable as business income / FTS.</li>"
         "<li><strong>Missing Form 10F</strong>: post Oct 2023, electronic Form 10F mandatory. Even non-residents without Indian PAN must obtain India e-filing PAN temporarily to file Form 10F. CBDT clarifications ongoing.</li>"
         "<li><strong>Service classification errors</strong>: payer calls it 'consultancy' (FTS 10% treaty), CA re-classifies as 'business income' (nil if no PE). Taxability can shift by INR 10 lakh+ on INR 1 crore remittance.</li>"
         "<li><strong>PE / fixed-place analysis skipped</strong>: foreign vendor rendering services remotely but has frequent India presence (frequent travel, demo deployment, long on-site engagement) &rarr; service PE / fixed-place PE &rarr; business income taxable.</li>"
         "</ul>"
         "<p><em>Last updated: 2026-10-13.</em></p>"),
    ],
    faqs=[
        ("When is Form 15CB mandatory?",
         "When remittance exceeds INR 5 lakh aggregate per payee per FY AND the remittance is chargeable to tax in India AND no Section 195(2)/(3)/197 order has been obtained. For smaller amounts (up to INR 5 lakh in FY), only Form 15CA Part A (self-declaration) is required; no CA certificate."),
        ("What is Form 10F and is it still required?",
         "Yes - Form 10F is a declaration by the non-resident payee confirming details (name, country of residence, PAN or substitute, treaty eligibility, no PE). Post October 2023, electronic Form 10F is mandatory via Indian e-filing portal. Even non-residents without Indian PAN must obtain temporary India e-filing registration to file Form 10F. Required alongside TRC for DTAA benefit."),
        ("What is TRC and why is it needed?",
         "Tax Residency Certificate - issued by the tax authority of the payee's country of residence confirming the payee is a tax resident there. Mandatory for claiming DTAA benefit (treaty rate) under Section 90(4). Without TRC, no treaty rate - standard Section 195 rate (20%) applies."),
        ("What's the TDS rate if payee doesn't have PAN?",
         "Section 206AA kicks in - rate is higher of: (a) rate under the Act / applicable Section 195, (b) rate under treaty (if TRC + Form 10F available), (c) 20%. Effectively 20% for most remittances. Payee should obtain PAN or at minimum file Form 10F even temporarily."),
        ("How quickly can BQP issue Form 15CB?",
         "24-48 hours standard turnaround once we have the documents (invoice, agreement, TRC, Form 10F, payee PAN if available). Rush turnaround possible for same-day if urgent. We can issue 15CB for any foreign payee globally - the certificate is based on Indian tax law and Indian CA certification; the payee's location doesn't matter."),
        ("Does BQP handle 15CA / 15CB for recurring remittances?",
         "Yes - standard engagement includes annual retainer for recurring remittances (monthly dividend, quarterly royalty, service fees). We maintain TRC + Form 10F file, update annually, pre-stage 15CBs for scheduled remittances. Standard engagement for Indian subsidiaries of foreign parents making regular remittances. WhatsApp +91 78018 87130."),
    ],
    related=[
        ("repatriate-profits-india-foreign-parent.html", "Guide", "Profit Repatriation"),
        ("section-195-tds-foreign-payer-indian-vendor.html", "Guide", "Section 195 TDS"),
    ],
    cta_headline="Need Form 15CB to release a wire from India?",
    cta_body="24-48 hour turnaround. We handle any payee globally &mdash; dividend, royalty, FTS, interest, capital gain, service fee. TRC + Form 10F guidance for payee. Also recurring remittance retainers. WhatsApp +91 78018 87130.",
))

# 4. OIDAR GST
write_page("oidar-gst-foreign-saas-ecommerce-india", page(
    slug="oidar-gst-foreign-saas-ecommerce-india",
    title="OIDAR GST for Foreign SaaS & E-commerce 2026 | Registration + Compliance - BQP",
    description="OIDAR (Online Information Database Access & Retrieval) GST for foreign SaaS / e-commerce companies selling to Indian consumers: Section 2(17) + 2(118), mandatory registration, 18% IGST, invoice requirements, OIDAR-9 return, representative appointment. Done remotely from India for foreign-based SaaS / digital companies. Working CA guide by Durgesh Chavda.",
    keywords="OIDAR GST foreign SaaS India, OIDAR registration process India, OIDAR 18% IGST, foreign e-commerce GST India B2C, Section 2(17) OIDAR services",
    hero_kicker="/ Foreign Clients &middot; OIDAR GST &middot; Updated 2026-10-13",
    hero_title_html="OIDAR GST, <em>what every foreign SaaS selling to India needs.</em>",
    hero_lead="If you're a US / UK / EU / Singapore SaaS company and you have paying Indian B2C customers (individuals, not GST-registered businesses), you likely need an OIDAR GST registration. 18% IGST on every rupee. Netflix, Spotify, Zoom, Adobe, Microsoft, Shopify &mdash; all registered. Many smaller SaaS companies miss this and accumulate liability. Here's the complete OIDAR framework.",
    sections=[
        ("/ What is OIDAR", "Section 2(17) + 2(118).",
         "<p><strong>OIDAR = Online Information Database Access and Retrieval services</strong>. Defined under Section 2(17) of the IGST Act:</p>"
         "<ul>"
         "<li>Services whose delivery is mediated by information technology over the internet or electronic network.</li>"
         "<li>Essentially automated with minimal human intervention.</li>"
         "<li>Impossible to supply without information technology.</li>"
         "</ul>"
         "<p><strong>Examples of OIDAR services</strong>:</p>"
         "<ul>"
         "<li>SaaS subscriptions (Zoom, Dropbox, Figma, Notion, Slack).</li>"
         "<li>Online advertising (Google Ads, Meta Ads, LinkedIn Ads purchased by Indian B2C customer).</li>"
         "<li>Cloud storage + computing (AWS, GCP, Azure B2C).</li>"
         "<li>E-books, music, video streaming (Spotify, Netflix, YouTube Premium).</li>"
         "<li>Mobile app subscriptions (gaming, productivity).</li>"
         "<li>Online learning platforms (Coursera, Udemy B2C).</li>"
         "<li>Digital advertising services, website hosting, online data retrieval.</li>"
         "</ul>"
         "<p><strong>NOT OIDAR</strong>: online consultancy with real human CA / consultant on the other end (that's regular Section 2(118) service), remote training with live instructor, physical goods shipped internationally, B2B services where the Indian recipient is GST-registered (reverse charge applies &mdash; no OIDAR obligation on foreign supplier).</p>"),
        ("/ Who must register", "B2C to Indian customers.",
         "<p>OIDAR GST registration is <strong>mandatory</strong> (no threshold) if ALL of these are true:</p>"
         "<ul>"
         "<li>You are a foreign supplier (incorporated / based outside India).</li>"
         "<li>Services qualify as OIDAR under Section 2(17).</li>"
         "<li>Recipient is a <strong>non-taxable online recipient</strong> &mdash; i.e., an Indian B2C customer (individual not registered for GST, or Indian entity not registered for GST, or Indian government body).</li>"
         "</ul>"
         "<p><strong>B2B exception</strong>: if your Indian customer is GST-registered (business), they are deemed to self-assess under reverse charge mechanism (Section 5(3) IGST). No GST obligation on foreign supplier for B2B. But <strong>practically</strong>, most SaaS companies have mix of B2B + B2C &mdash; and must register once any B2C paying customer exists.</p>"
         "<p>Finance Act 2023 broadened OIDAR definition (removed 'essentially automated' requirement for some sub-categories) &mdash; even more foreign suppliers now in scope.</p>"),
        ("/ Registration + compliance workflow", "What foreign SaaS must do.",
         "<ol>"
         "<li><strong>Appoint representative in India</strong> (recommended, not mandatory): a GST-registered Indian consultant / CA firm as 'authorised representative' for the OIDAR registration. BQP handles this role.</li>"
         "<li><strong>Register under OIDAR</strong>: online via GST portal (ggsp.gst.gov.in or regular GST portal, specific OIDAR category). Documents: company incorporation, passport of directors, bank account, business address proof.</li>"
         "<li><strong>GSTIN issued</strong>: specific format for OIDAR registrants (begins with '9900' or similar).</li>"
         "<li><strong>Charge 18% IGST</strong> on every invoice to Indian B2C customer. Shown on customer invoice; collected via payment gateway.</li>"
         "<li><strong>Monthly / quarterly return</strong>: Form GSTR-9A (OIDAR annual return) + monthly statement. Pay collected IGST to Indian government by 20th of next month.</li>"
         "<li><strong>IGST payment</strong>: via NEFT/RTGS to designated government account. In practice, Indian representative handles payment on behalf of foreign supplier.</li>"
         "</ol>"),
        ("/ Common OIDAR mistakes + risks", "What foreign SaaS gets wrong.",
         "<ul>"
         "<li><strong>Not registering at all</strong>: assuming 'we don't have an Indian entity, so no GST applies'. Wrong &mdash; OIDAR applies even without Indian presence. Non-registration = tax demand under Section 74 (fraud / wilful suppression) up to 5 years back + 100% penalty.</li>"
         "<li><strong>Not distinguishing B2B vs B2C</strong>: Indian B2B customer should provide their GSTIN for self-assessment (reverse charge). Foreign supplier should capture GSTIN at checkout. Without GSTIN capture, every sale defaults to B2C &rarr; 18% OIDAR GST obligation.</li>"
         "<li><strong>Charging INR-denominated vs USD-denominated</strong>: GST is on supply value. If invoice is in USD, convert at RBI reference rate for the day. Document FX conversion rate.</li>"
         "<li><strong>Credit note / refund processing errors</strong>: refunds reduce taxable supply but need proper credit-note documentation under GST invoice rules.</li>"
         "<li><strong>Missed Form OIDAR-9 / GSTR-9A filing</strong>: annual return separate from monthly compliance. Late fee + penalty.</li>"
         "<li><strong>No Indian representative</strong>: makes tax officer communication / notice response very difficult. Appointment of Indian authorised representative is standard best practice.</li>"
         "</ul>"
         "<p><em>Last updated: 2026-10-13.</em></p>"),
    ],
    faqs=[
        ("What is OIDAR GST?",
         "Online Information Database Access and Retrieval service tax under GST. Foreign suppliers of digital services (SaaS, streaming, cloud, online ads, e-books) to Indian B2C customers (non-GST-registered individuals / businesses) must register, charge 18% IGST, and remit to Indian government. Introduced under Section 2(17) IGST Act. Netflix, Spotify, Zoom, Adobe are all OIDAR-registered."),
        ("Is there a threshold for OIDAR registration?",
         "No threshold - mandatory registration for every foreign supplier of OIDAR services to Indian B2C customers from the first rupee. Unlike regular GST which has INR 20 lakh / 40 lakh thresholds, OIDAR has zero threshold for foreign suppliers."),
        ("Does OIDAR apply to B2B sales to Indian businesses?",
         "No - if the Indian customer is GST-registered (business), reverse charge mechanism applies (Section 5(3) IGST Act). Indian recipient self-assesses GST; no obligation on foreign supplier. BUT: foreign supplier must capture Indian customer's GSTIN at checkout to prove B2B status. Without GSTIN, every sale defaults to B2C and attracts OIDAR GST obligation."),
        ("Do I need an Indian representative for OIDAR?",
         "Not strictly mandatory, but highly recommended. The Indian authorised representative handles: representation with tax officer, monthly return filing, IGST payment execution, response to notices, annual return (GSTR-9A). Without an Indian representative, every compliance step is harder for foreign supplier. BQP acts as authorised representative for several foreign SaaS clients."),
        ("What happens if I don't register for OIDAR?",
         "Section 74 GST demand (fraud / wilful suppression) can go back 5 years with 100% penalty. Section 73 (non-fraud) 3 years back with 10% penalty / INR 10,000 whichever higher. Payment gateway blocking is also possible (RBI can direct). Reputational risk if major customer tax audit surfaces the issue."),
        ("Does BQP handle OIDAR registration + ongoing compliance?",
         "Yes - full stack: OIDAR registration, Indian authorised representative service, monthly IGST computation + payment, GSTR-9A annual return, notice response, tax audit coordination. Standard annual engagement for foreign SaaS / e-commerce selling to Indian consumers. WhatsApp +91 78018 87130."),
    ],
    related=[
        ("foreign-company-setup-indian-subsidiary-wos.html", "Guide", "India WOS Setup"),
        ("gstr-9-gstr-9c-annual-return-india-2026.html", "Guide", "GSTR-9"),
    ],
    cta_headline="Foreign SaaS / e-commerce with Indian B2C paying customers?",
    cta_body="OIDAR registration is from the first rupee. Non-registration = tax demand up to 5 years back with 100% penalty. BQP: registration + Indian representative + monthly compliance + GSTR-9A. Standard annual engagement.",
))

# 5. Transfer pricing India for foreign MNC
write_page("transfer-pricing-india-foreign-mnc", page(
    slug="transfer-pricing-india-foreign-mnc",
    title="Transfer Pricing India for Foreign MNC 2026 | Form 3CEB, APA, Master File - BQP",
    description="Transfer pricing compliance for Indian subsidiary of foreign MNC: Form 3CEB mandatory, benchmarking study, Master File + CbCR for groups above threshold, APA (Advance Pricing Agreement), BEPS Pillar 2 India implementation. Delivered remotely from India for US / UK / EU / Singapore / UAE MNC groups. Working CA guide by Durgesh Chavda.",
    keywords="transfer pricing India foreign MNC, Form 3CEB India foreign company, APA India advance pricing agreement, Master File CbCR India, BEPS Pillar 2 India MNC",
    hero_kicker="/ Foreign Clients &middot; Transfer Pricing &middot; Updated 2026-10-13",
    hero_title_html="Transfer pricing India, <em>when parent is foreign.</em>",
    hero_lead="Any Indian subsidiary of a foreign MNC with cross-border related-party transactions is in India's transfer pricing regime: Section 92 to 92F, Rules 10 to 10TE. Form 3CEB mandatory. Benchmarking study required. Scrutiny likelihood is high &mdash; India is one of the most TP-active jurisdictions globally with ~INR 50,000 crore+ in adjustments annually. For groups above the threshold, Master File + CbCR + BEPS Pillar 2. Here's the practitioner's framework.",
    sections=[
        ("/ When Indian TP applies", "Associated Enterprise + International Transaction.",
         "<p>India's TP applies when:</p>"
         "<ul>"
         "<li>An <strong>Indian company has transactions with an Associated Enterprise</strong> (AE), AND</li>"
         "<li>The transaction qualifies as an <strong>International Transaction</strong> or <strong>Specified Domestic Transaction</strong>.</li>"
         "</ul>"
         "<p><strong>Associated Enterprise (Section 92A)</strong>:</p>"
         "<ul>"
         "<li>Direct or indirect participation in management, control, or capital (26%+ shareholding, 26%+ voting, etc.).</li>"
         "<li>Common management / control of both enterprises.</li>"
         "<li>Guarantee / loan providing &gt; 51% total.</li>"
         "<li>Appointment of &gt; 50% of board members.</li>"
         "</ul>"
         "<p>Indian subsidiary of US parent: AE. Indian subsidiary of UK parent via Singapore holdco: both US / UK / Singapore are AE.</p>"
         "<p><strong>International Transaction (Section 92B)</strong>: any transaction between AEs that affects profits, income, losses, or assets &mdash; purchase/sale of goods, services, intangibles, lending/borrowing, guarantees, cost sharing, business restructuring.</p>"
         "<p><strong>Threshold for TP documentation</strong>: aggregate international transactions &gt; INR 1 crore in the FY &rarr; Section 92D documentation required.</p>"),
        ("/ Form 3CEB (annual audit)", "The core compliance.",
         "<p>Form 3CEB is a transfer pricing audit certificate issued by a Chartered Accountant, filed as part of the Indian company's annual tax return. Required for:</p>"
         "<ul>"
         "<li>Every taxpayer with international transactions above INR 1 crore in the FY (effectively every foreign-subsidiary).</li>"
         "<li>Due date: 31 October of the AY (vs 31 July for non-TP taxpayers).</li>"
         "</ul>"
         "<p>Form 3CEB covers:</p>"
         "<ul>"
         "<li>List of all international transactions with each AE &mdash; by nature (goods, services, intangibles, financing, cost allocation, business restructuring).</li>"
         "<li>Transaction value in INR + description.</li>"
         "<li>Arm's-length method chosen (CUP, Resale Price Method, Cost Plus Method, TNMM, PSM, Other Method).</li>"
         "<li>Benchmarking analysis supporting arm's-length conclusion.</li>"
         "<li>Material facts and specific adjustments / documentation.</li>"
         "</ul>"
         "<p><strong>Underlying documentation</strong>: Section 92D requires detailed TP documentation to be maintained (not filed, but produced if asked): entity profile, industry analysis, functional analysis, economic analysis / benchmarking study. Must be contemporaneous (prepared by the time of filing Form 3CEB, not after a scrutiny notice).</p>"),
        ("/ Master File + CbCR (for large groups)", "BEPS compliance.",
         "<p>Finance Act 2016 introduced BEPS-aligned <strong>Master File</strong> and <strong>Country-by-Country Report</strong> (CbCR) requirements.</p>"
         "<p><strong>Master File (Form 3CEAA)</strong>: required for any Indian entity which is part of an international group where:</p>"
         "<ul>"
         "<li>Consolidated group revenue in preceding year &gt; INR 500 crore (~USD 60 million), AND</li>"
         "<li>Aggregate value of international transactions &gt; INR 50 crore OR international transactions pertaining to intangibles &gt; INR 10 crore.</li>"
         "</ul>"
         "<p>Contents: group overview, business strategy, group's intangibles, group's intercompany financing, group's financial + tax position.</p>"
         "<p><strong>CbCR (Form 3CEAD)</strong>: required for any ultimate parent of an international group with consolidated revenue &gt; INR 6,400 crore (~EUR 750 million, aligned with BEPS Action 13).</p>"
         "<ul>"
         "<li>Primary filing obligation on the ultimate parent (if India).</li>"
         "<li>Secondary filing (Form 3CEAC &amp; 3CEAD) on Indian subsidiary of foreign parent if parent country has no CbCR regime or no information-sharing MoU.</li>"
         "</ul>"
         "<p>Contents: country-by-country breakdown of revenue, profit, tax paid, employees, tangible assets.</p>"
         "<p><strong>BEPS Pillar 2 (Global Minimum Tax, 15%)</strong>: India implementing from FY 2025-26 for groups with consolidated revenue &gt; EUR 750M. Separate GloBE compliance alongside TP. See our <a href='pillar-2-global-minimum-tax-india-startups-2026.html'>Pillar 2 guide</a>.</p>"),
        ("/ APA (Advance Pricing Agreement)", "Certainty for 5+5 years.",
         "<p>For taxpayers wanting certainty on TP position: Section 92CC Advance Pricing Agreement with CBDT.</p>"
         "<ul>"
         "<li><strong>Unilateral APA</strong>: with CBDT only.</li>"
         "<li><strong>Bilateral APA</strong>: between CBDT and competent authority of the other country (US, UK, Japan, Singapore &mdash; most useful).</li>"
         "<li><strong>Multilateral APA</strong>: three or more jurisdictions.</li>"
         "</ul>"
         "<p><strong>Duration</strong>: 5 years prospective + 4 years rollback = up to 9 years of certainty.</p>"
         "<p><strong>Benefits</strong>:</p>"
         "<ul>"
         "<li>No TP scrutiny for covered transactions during APA period.</li>"
         "<li>Removes double-taxation risk (bilateral APA).</li>"
         "<li>Reduces litigation cost / management time.</li>"
         "</ul>"
         "<p><strong>Timeline</strong>: typically 24-36 months from filing to signing. Expensive upfront but valuable for groups with large recurring intercompany transactions.</p>"),
        ("/ Common TP mistakes foreign MNCs make in India", "What triggers assessment.",
         "<ul>"
         "<li><strong>Low operating margin on contract services</strong>: Indian subsidiary providing IT / BPO services to foreign parent at 10% net margin. Indian comparables typically show 15-18%. Addition likely at ~5% of cost base.</li>"
         "<li><strong>Royalty rate on licensed brand / technology</strong>: too low (parent extracting value) or too high (shifting profit to parent). Benchmarking against royalty databases (e.g., RoyaltyStat, ktMINE) + comparability adjustments.</li>"
         "<li><strong>Guarantee fee for parent's bank guarantee</strong>: Indian subsidiary paying nil or symbolic guarantee fee to parent for parent-provided guarantee. CBDT expects fee at ~0.5-1.5% of guaranteed amount.</li>"
         "<li><strong>Marketing intangibles (AMP / brand building)</strong>: Indian subsidiary spending significantly on brand marketing in India but not getting marketing-service fee / IP reward from parent. 'Bright Line' test ADPCO cases &rarr; adjustment risk.</li>"
         "<li><strong>Cost allocation without substance</strong>: parent allocating group HQ costs to Indian subsidiary without proper allocation key / benefit test. CBDT typically disallows allocations lacking benefit test.</li>"
         "<li><strong>Weak benchmarking</strong>: using too few comparables, including non-comparable sized companies, cherry-picking inter-quartile range.</li>"
         "<li><strong>Not filing Master File / CbCR when applicable</strong>: group revenue above threshold but local Indian team not aware of global filing status.</li>"
         "</ul>"
         "<p><em>Last updated: 2026-10-13.</em></p>"),
    ],
    faqs=[
        ("Is Form 3CEB mandatory for every foreign-subsidiary in India?",
         "Effectively yes - any Indian subsidiary of a foreign parent that has international transactions (parent charges management fee, royalty, interest, service fee, or buys/sells goods to Indian subsidiary) crosses the INR 1 crore threshold quickly. Form 3CEB mandatory alongside Form 3CD and ITR-6. Due 31 October of the AY."),
        ("What is Master File and when do I need it?",
         "Form 3CEAA - detailed documentation of the entire international group (business, intangibles, intercompany financing, tax position). Required if (a) group consolidated revenue > INR 500 crore in preceding year AND (b) aggregate international transactions > INR 50 crore OR intangible-related > INR 10 crore. Filed by Indian subsidiary; prepared based on group data from parent."),
        ("What is CbCR and when does India require it?",
         "Country-by-Country Report (Form 3CEAD) under BEPS Action 13 - country-wise breakdown of revenue, profit, tax paid, headcount, tangible assets for the whole international group. Required for groups with consolidated revenue > INR 6,400 crore (~EUR 750M). Primary filing by ultimate parent; secondary filing by Indian subsidiary if parent country has no CbCR regime."),
        ("Is APA worth the cost for a foreign MNC in India?",
         "For groups with large recurring intercompany transactions (e.g., annual royalty > USD 5M, or IT services engagement with 1000+ Indian headcount), yes - 5+4 years of certainty + removal of double-taxation risk + reduced litigation outweigh the 24-36 month filing process + professional fees. For smaller / variable transactions, standard annual Form 3CEB may suffice."),
        ("How much is a typical TP adjustment in India?",
         "Varies widely by industry and transaction type. For IT services with low Indian margin: adjustment at 2-8% of cost base. For royalty: often 100% disallowance if not benchmarked. For guarantee fee: 0.5-1.5% of guaranteed amount addition. Across India, CBDT makes ~INR 50,000 crore+ in TP adjustments annually across all taxpayers."),
        ("Does BQP handle Indian TP for foreign MNC subsidiaries?",
         "Yes - full stack: Form 3CEB preparation + filing, benchmarking study (TNMM / RPM / CUP method), Master File + CbCR filing, APA application if valuable, TP scrutiny / assessment representation. We work with group tax / treasury of foreign parent and coordinate with group-level TP advisors. Standard annual engagement scoped per transaction count + complexity. WhatsApp +91 78018 87130."),
    ],
    related=[
        ("transfer-pricing.html", "Service", "Transfer Pricing Hub"),
        ("pillar-2-global-minimum-tax-india-startups-2026.html", "Guide", "Pillar 2"),
    ],
    cta_headline="Foreign MNC with Indian subsidiary - is your TP position defensible?",
    cta_body="India is one of the most TP-active jurisdictions globally. Form 3CEB + benchmarking + Master File / CbCR / APA scope varies. BQP full stack from India for US / UK / EU / Singapore / UAE MNC groups.",
))

# 6. India market entry
write_page("india-market-entry-foreign-company-guide", page(
    slug="india-market-entry-foreign-company-guide",
    title="India Market Entry for Foreign Companies 2026 | Regulatory + Strategy Guide - BQP",
    description="Complete India market entry guide for foreign companies: entity structure (WOS vs branch vs liaison), FDI sector check, Press Note 3, GST + IGST + customs, hiring + payroll, IP registration, data compliance (DPDP Act), banking + repatriation. Executed from India for US / UK / EU / Singapore / UAE companies. Working CA guide by Durgesh Chavda.",
    keywords="India market entry foreign company, India business setup foreign, how to enter India market, India FDI entry route, India market entry consultant",
    hero_kicker="/ Foreign Clients &middot; India Market Entry &middot; Updated 2026-10-13",
    hero_title_html="India market entry, <em>a foreign company's complete playbook.</em>",
    hero_lead="Foreign company evaluating India market entry: this is the complete decision + execution framework. Entity structure, FDI regulatory path, GST / tax regime, hiring, IP protection, banking, repatriation, DPDP data law. 12-24 week typical setup. Here's the full practitioner's map &mdash; everything a US / UK / EU / Singapore / UAE company's board needs to know before committing to the India plan.",
    sections=[
        ("/ Entity structure decision tree", "Six options.",
         "<p>Six legal entity options for foreign company in India:</p>"
         "<ol>"
         "<li><strong>Wholly-Owned Subsidiary (Pvt Ltd)</strong> &mdash; the default. Separate legal entity, 100% foreign ownership, limited liability, standard corporate tax, easy to operate. <strong>Choose if</strong>: you'll have Indian employees, invoice Indian customers, build material India business. See <a href='foreign-company-setup-indian-subsidiary-wos.html'>WOS guide</a>.</li>"
         "<li><strong>Joint Venture (Pvt Ltd with Indian partner)</strong> &mdash; same as WOS but with Indian equity partner. <strong>Choose if</strong>: regulated sector with FDI cap (defence 74%, insurance 74%, print media 26%), or local market knowledge / government relationship is essential.</li>"
         "<li><strong>Branch Office</strong> &mdash; extension of foreign parent, not a separate entity. Requires RBI prior approval. Limited to specified activities (export/import, consultancy, representation, R&amp;D). <strong>Choose if</strong>: narrow operational scope, parent wants direct accountability.</li>"
         "<li><strong>Liaison Office</strong> &mdash; representative office only; cannot do business. RBI prior approval. Cannot invoice; expenses funded by parent remittance. <strong>Choose if</strong>: exploratory presence, market research, no revenue plan.</li>"
         "<li><strong>Project Office</strong> &mdash; for a specific project (government contract, infrastructure). Time-bound.</li>"
         "<li><strong>LLP</strong> &mdash; foreign investment permitted only in specific sectors + under automatic route. Less common for foreign parents; chosen occasionally for small operations.</li>"
         "</ol>"
         "<p>For 90%+ of foreign companies entering India for business, the answer is WOS (Pvt Ltd). See the full comparison in our <a href='branch-office-vs-liaison-vs-wos-india-foreign.html'>Branch vs Liaison vs WOS guide</a>.</p>"),
        ("/ FDI regulatory check", "Automatic vs Approval route.",
         "<p>India's FDI policy:</p>"
         "<ul>"
         "<li><strong>Automatic route</strong>: 100% FDI allowed, no prior government approval. Applies to most sectors: IT/SaaS, trading, manufacturing, services, retail trading (single-brand under conditions).</li>"
         "<li><strong>Approval route</strong>: FDI capped (e.g., multi-brand retail 51%, print media 26%, broadcasting 49%, insurance 74%, defence 74%, telecom under conditions). Requires prior Government approval via FDI portal (DPIIT).</li>"
         "<li><strong>Prohibited sectors</strong>: lottery, gambling, chit funds, Nidhi companies, trading in transferable development rights, real estate business (not construction), atomic energy, railway operations (certain areas), tobacco manufacturing.</li>"
         "<li><strong>Press Note 3 (April 2020)</strong>: for countries sharing land border with India (China, Pakistan, Bangladesh, Nepal, Bhutan, Myanmar, Afghanistan) OR beneficial ownership from such countries, prior government approval mandatory regardless of sector / FDI cap.</li>"
         "</ul>"
         "<p>Pre-check your sector + beneficial ownership before incorporation.</p>"),
        ("/ GST + tax regime", "The compliance stack.",
         "<ul>"
         "<li><strong>Corporate tax</strong>: 25% / 22% (Section 115BAA) / 15% (Section 115BAB new manufacturing). See <a href='section-115baa-115bab-corporate-tax-regime-india.html'>corporate tax guide</a>.</li>"
         "<li><strong>Minimum Alternate Tax (MAT)</strong>: 15% on book profit (does not apply if 115BAA / 115BAB opted).</li>"
         "<li><strong>Dividend Distribution Tax (DDT)</strong>: abolished from April 2020. Dividend taxable in shareholder's hands (foreign parent &rarr; Section 195 TDS at treaty rate).</li>"
         "<li><strong>GST</strong>: 18% standard; 5% / 12% reduced; 28% luxury. Monthly GSTR-1 + 3B. Annual GSTR-9 if turnover &gt; INR 2 crore.</li>"
         "<li><strong>IGST on imports</strong>: paid on customs value + Basic Customs Duty; credit available if used for GST-taxable supply.</li>"
         "<li><strong>Customs duty</strong>: Basic Customs Duty + Social Welfare Surcharge + IGST. HSN-wise rates. Free Trade Agreement countries (ASEAN, Japan, Korea, UAE post-CEPA, UK post-CETA 2026) have preferential rates.</li>"
         "<li><strong>Transfer pricing</strong>: Form 3CEB + benchmarking study. See <a href='transfer-pricing-india-foreign-mnc.html'>TP guide</a>.</li>"
         "<li><strong>Equalisation Levy</strong>: 2% on digital services payments to non-residents (though under BEPS Pillar 1 phase-out).</li>"
         "</ul>"),
        ("/ Hiring Indian talent + payroll", "People side.",
         "<ul>"
         "<li><strong>Employment contracts</strong>: Indian subsidiary hires Indian employees directly. Standard offer letter + employment agreement + leave + termination terms. Governed by Shops &amp; Establishment Act (state-specific) + Industrial Employment (Standing Orders) Act.</li>"
         "<li><strong>PF (Provident Fund)</strong>: 12% employer + 12% employee contribution. Mandatory if headcount &gt;= 20.</li>"
         "<li><strong>ESI (Employee State Insurance)</strong>: 3.25% employer + 0.75% employee. Mandatory if gross salary &lt;= INR 21,000/month.</li>"
         "<li><strong>Professional Tax</strong>: state-specific, max INR 2,500/year per employee.</li>"
         "<li><strong>Gratuity</strong>: 15 days salary per completed year of service, payable on exit after 5 years. Provision required in books.</li>"
         "<li><strong>Section 192 TDS</strong>: employer deducts income tax on employee salary monthly.</li>"
         "<li><strong>Alternative - EOR</strong>: if you don't yet have Indian subsidiary, use Employer of Record. See <a href='employer-of-record-india-hire-from-abroad.html'>EOR guide</a>.</li>"
         "</ul>"),
        ("/ Data protection + IP + banking", "Three must-check items.",
         "<ul>"
         "<li><strong>DPDP Act 2023</strong>: India's data protection law (effective FY 2024-25 onwards). Covers 'personal data' of Indian residents. Consent-based processing, data principal rights, breach notification, cross-border transfer restrictions (specific countries approved by govt). Fines up to INR 250 crore for violation.</li>"
         "<li><strong>IP registration</strong>: trademark + copyright + patent + design &mdash; foreign company can register directly or via Madrid Protocol (trademark) / PCT national phase (patent). See <a href='india-trademark-patent-ip-foreign-company.html'>India IP guide</a>.</li>"
         "<li><strong>Banking</strong>: current account for Indian subsidiary with HDFC / ICICI / Kotak / Axis / foreign bank Indian branch (Citi, DBS, HSBC). AD-I category banks handle FEMA remittance.</li>"
         "<li><strong>Repatriation</strong>: dividend / royalty / FTS / interest to foreign parent. See <a href='repatriate-profits-india-foreign-parent.html'>repatriation guide</a>.</li>"
         "</ul>"
         "<p><em>Last updated: 2026-10-13.</em></p>"),
    ],
    faqs=[
        ("What's the standard entity for foreign company entering India?",
         "Private Limited Company (Pvt Ltd) as 100% Wholly-Owned Subsidiary (WOS) of foreign parent. Chosen in ~90% of foreign market entries. Alternatives (Branch, Liaison, Project Office, LLP, JV) chosen in specific scenarios - sector restrictions, exploratory presence, time-bound projects."),
        ("Does my FDI need government approval?",
         "Depends on sector + source. Automatic route for most sectors (IT, SaaS, trading, manufacturing, services) - no prior approval. Approval route for sector-capped (multi-brand retail 51%, defence 74%, print media 26%, insurance 74%). Press Note 3: any investment from countries sharing land border with India (China, Pakistan, Bangladesh, etc.) requires prior approval regardless of sector."),
        ("How long does India market entry take?",
         "12-24 weeks typical: FDI sector verification + beneficial ownership check (2 weeks), apostille of parent docs (3-4 weeks), DSC/DIN + incorporation (3-4 weeks), bank account + capital remittance + FC-GPR (4 weeks), GST + professional tax + Shops & Establishment (2-4 weeks), DPDP + IP registrations (ongoing)."),
        ("What are India's typical tax rates for a foreign subsidiary?",
         "Corporate tax: 22% + surcharge + cess = ~25.17% effective under Section 115BAA (opted by most foreign subsidiaries). Dividend from subsidiary to foreign parent: Section 195 TDS at 20% (standard) or treaty rate (typically 10-15% under DTAA with TRC + Form 10F). GST 18% on most B2B services + goods."),
        ("Can I hire Indian employees without an Indian entity?",
         "Yes - via Employer of Record (EOR). The EOR is the legal employer in India (handles payroll, PF, ESI, taxes); you pay EOR a monthly fee + employee cost. Useful for 1-10 Indian hires + exploratory presence. For 10+ hires or long-term India plan, incorporating your own Indian subsidiary is more cost-effective."),
        ("Does BQP handle India market entry for foreign companies?",
         "Yes - this is a core service. Entity structure advisory + FDI sector check + incorporation + apostille coordination + bank account + GST + Shops & Establishment + hiring setup + IP registration + DPDP compliance + ongoing annual compliance + repatriation + TP. One firm, one engagement, one point of accountability. Standard engagement for US / UK / EU / Singapore / UAE companies. WhatsApp +91 78018 87130."),
    ],
    related=[
        ("foreign-company-setup-indian-subsidiary-wos.html", "Guide", "WOS Setup"),
        ("branch-office-vs-liaison-vs-wos-india-foreign.html", "Guide", "Entity Comparison"),
    ],
    cta_headline="Foreign company planning India market entry?",
    cta_body="12-24 week full execution from India: entity + FDI + GST + hiring + IP + DPDP + ongoing compliance. BQP runs the whole stack under one engagement. Scope-based pricing by sector + complexity.",
))

# 7. EOR
write_page("employer-of-record-india-hire-from-abroad", page(
    slug="employer-of-record-india-hire-from-abroad",
    title="Employer of Record (EOR) India 2026 | Hire Indian Talent from USA UK EU - BQP",
    description="EOR India for foreign companies hiring Indian talent without an Indian entity: EOR vs own subsidiary comparison, PF / ESI / PT / gratuity compliance, Section 192 TDS, independent contractor vs employee classification, PE risk for foreign hirer. Standard EOR scope-based. BQP acts as EOR partner. Working CA guide by Durgesh Chavda.",
    keywords="employer of record India, EOR India from USA, hire Indian talent without Indian entity, EOR vs Indian subsidiary, EOR India payroll compliance, PEO India foreign company",
    hero_kicker="/ Foreign Clients &middot; EOR India &middot; Updated 2026-10-13",
    hero_title_html="Employer of Record India, <em>hire from abroad without an Indian entity.</em>",
    hero_lead="Foreign company (US / UK / EU / Singapore / UAE) wanting to hire Indian engineers / sales / operations talent &mdash; but not yet ready to set up an Indian entity. Employer of Record (EOR) is the fast path: EOR is the legal employer in India (handles payroll, PF, ESI, taxes), you pay EOR a monthly fee + employee cost. 2-week hire cycle. Here's when EOR works, when it breaks, and the PE risk you need to manage.",
    sections=[
        ("/ EOR vs own Indian subsidiary", "The decision.",
         "<p><strong>EOR is right if</strong>:</p>"
         "<ul>"
         "<li>1-15 Indian hires over next 12-24 months.</li>"
         "<li>Early market exploration; India is one of several hiring geographies.</li>"
         "<li>Need to onboard a specific candidate quickly (1-3 weeks).</li>"
         "<li>Don't want to deal with Indian compliance (payroll, PF, ESI, PT, gratuity, labour law).</li>"
         "</ul>"
         "<p><strong>Own Indian subsidiary (Pvt Ltd WOS) is right if</strong>:</p>"
         "<ul>"
         "<li>15+ Indian hires or multi-year India plan.</li>"
         "<li>Need to invoice Indian customers (EOR doesn't give you an invoicing entity).</li>"
         "<li>Want direct ESOP grants to Indian employees (easier via Indian subsidiary).</li>"
         "<li>Want to control the brand presence / IP / data residency in India.</li>"
         "<li>Need to amortise setup cost over longer horizon.</li>"
         "</ul>"
         "<p><strong>Cost comparison</strong> (rough):</p>"
         "<ul>"
         "<li>EOR: ~USD 100-300/employee/month fee + employee cost. For 10 engineers at USD 20K/year each, EOR cost ~USD 15-30K/year.</li>"
         "<li>Own subsidiary: setup USD 2-5K one-time + annual compliance USD 5-10K/year + optional resident director nominee USD 2-3K/year. Break-even vs EOR around 8-12 Indian hires.</li>"
         "</ul>"),
        ("/ What EOR handles", "The compliance stack.",
         "<ul>"
         "<li><strong>Employment contract</strong>: EOR issues to employee; mirrors foreign hirer's commercial terms. India-compliant (Shops &amp; Establishment, applicable state's labour laws).</li>"
         "<li><strong>Monthly payroll</strong>: compute gross &rarr; deductions (PF 12% + ESI 0.75% if applicable + PT state-specific) &rarr; TDS Section 192 &rarr; net pay. Credit on 1st of month.</li>"
         "<li><strong>PF (Provident Fund)</strong>: 12% employer + 12% employee contribution. EOR files Form 5 (new employee) + ECR (electronic challan return) monthly.</li>"
         "<li><strong>ESI</strong>: if applicable (gross salary &lt;= INR 21,000/month, often not applicable for mid-senior roles).</li>"
         "<li><strong>Professional Tax</strong>: state-specific, max INR 2,500/year.</li>"
         "<li><strong>TDS Section 192</strong>: monthly deduction + quarterly Form 24Q filing.</li>"
         "<li><strong>Gratuity</strong>: provision in books; payable on exit after 5 years of continuous service.</li>"
         "<li><strong>Form 16</strong>: issued to employee annually (by 15 June).</li>"
         "<li><strong>Statutory compliance</strong>: labour welfare fund, bonus, leave encashment, maternity benefit, Shops &amp; Establishment renewal, labour returns.</li>"
         "</ul>"),
        ("/ PE risk - the critical issue", "What breaks the model.",
         "<p>EOR assumes the Indian employee works 'for' the foreign company. The foreign company pays, directs work, provides tools. India's tax authority can argue:</p>"
         "<ul>"
         "<li><strong>Dependent Agent PE</strong>: Indian employee habitually concludes contracts in India on behalf of foreign company &rarr; Dependent Agent PE under Article 5 of most DTAAs &rarr; foreign company has Indian taxable presence &rarr; profit attribution + Indian corporate tax.</li>"
         "<li><strong>Service PE</strong>: Indian employees provide services in India to foreign group companies for &gt; specified days per 12-month period (varies by treaty, 90 days in India-US DTAA, 183 days in some others) &rarr; Service PE &rarr; same consequence.</li>"
         "<li><strong>Fixed Place PE</strong>: if Indian employee works from a specific premises (foreign company's leased office, cowork) and this is held at foreign company's disposal &rarr; Fixed Place PE.</li>"
         "</ul>"
         "<p><strong>Risk mitigation</strong>:</p>"
         "<ul>"
         "<li>Keep Indian employees in support / development roles, not sales / contract-signing.</li>"
         "<li>Decision-making authority stays with foreign HQ.</li>"
         "<li>Avoid giving Indian employees authority to bind foreign company contractually.</li>"
         "<li>Document role as 'back-office support' / 'development'.</li>"
         "<li>Review PE risk annually with tax advisor.</li>"
         "</ul>"
         "<p>For sales / client-facing / contract-authority roles, own Indian subsidiary is safer than EOR (because invoicing is through the Indian entity).</p>"),
        ("/ Independent contractor alternative", "The 1099 / Form 16A path.",
         "<p>Instead of EOR, foreign company can engage Indian individuals as <strong>independent contractors</strong>:</p>"
         "<ul>"
         "<li>Contract directly with Indian individual as consultant / freelancer.</li>"
         "<li>Pay via wire / wire aggregator / PayPal / Deel / Wise.</li>"
         "<li>Contractor is self-employed; files own Indian ITR, pays own tax + GST (if applicable).</li>"
         "<li>No PF / ESI / Section 192 TDS obligation on foreign company.</li>"
         "</ul>"
         "<p><strong>But</strong>:</p>"
         "<ul>"
         "<li><strong>Mis-classification risk</strong>: if the arrangement is really an employment (regular hours, exclusive, directed work, tools provided), labour authority can re-characterise as employment &rarr; back-dated PF + ESI + gratuity + Section 192 TDS.</li>"
         "<li><strong>GST risk</strong>: if contractor's turnover exceeds INR 20 lakh / 40 lakh threshold, they must register for GST + charge GST on invoice. If export of service under GST rules (place of supply outside India, payment in foreign currency, zero-rated), LUT bond + no IGST charged.</li>"
         "<li><strong>No employee benefits</strong>: contractor has no gratuity, no PF, no leave encashment, no bonus &mdash; may limit ability to hire mid-senior talent.</li>"
         "</ul>"),
        ("/ Who to pick as EOR", "What matters.",
         "<ul>"
         "<li><strong>Compliance track record</strong>: PF / ESI / Section 192 TDS on time, Form 24Q filed quarterly without defaults.</li>"
         "<li><strong>Transparency</strong>: itemised monthly invoice (base pay / PF / ESI / PT / TDS / fee).</li>"
         "<li><strong>Payroll portal</strong>: employee can see payslip + Form 16 + PF balance.</li>"
         "<li><strong>HR support</strong>: offer letters, onboarding, policy drafts, exit handling.</li>"
         "<li><strong>Legal support</strong>: labour law notice handling, PE-risk analysis, specific-event advisory (maternity, resignation, PIP).</li>"
         "<li><strong>Scale</strong>: can grow with you from 1 to 50+ Indian hires without renegotiation.</li>"
         "</ul>"
         "<p>BQP offers EOR + CA + tax integrated: one firm handling India payroll, India tax compliance, India ROC compliance, and ready to transition to own-subsidiary when scale justifies it.</p>"
         "<p><em>Last updated: 2026-10-13.</em></p>"),
    ],
    faqs=[
        ("What is an Employer of Record (EOR) in India?",
         "EOR is a third-party entity that becomes the legal employer of your Indian hires. EOR handles Indian employment contract, monthly payroll, PF, ESI, Professional Tax, Section 192 TDS, Form 24Q, Form 16, gratuity, labour law compliance. You pay EOR a monthly fee + the employee's cost; the employee effectively works for your company. Fast path to hire Indian talent without setting up your own Indian entity."),
        ("When should I use EOR vs own Indian subsidiary?",
         "EOR for 1-15 Indian hires + short/medium-term India plan + no need to invoice Indian customers. Own subsidiary for 15+ hires + long-term plan + Indian customer invoicing + direct ESOP grants + brand/IP presence. Break-even cost around 8-12 Indian hires: EOR cost ~USD 100-300/employee/month scales linearly; own subsidiary has fixed setup + annual compliance that amortises."),
        ("What is PE (Permanent Establishment) risk with EOR?",
         "If Indian employees working through EOR take decisions / sign contracts / provide client-facing services on behalf of the foreign company, India's tax authority can argue the foreign company has a Dependent Agent PE / Service PE / Fixed Place PE in India - creating Indian taxable presence + profit attribution. Mitigation: keep EOR employees in support/development roles, decision authority at foreign HQ, no contract-signing authority."),
        ("Can I hire Indian contractors directly instead of using EOR?",
         "Yes - as independent contractor / consultant. Contract directly, pay via wire. No PF / ESI / Section 192 TDS on foreign company. But risk of mis-classification: if arrangement is really employment (regular hours, exclusive, directed), labour authority can re-characterise with back-dated obligations. Appropriate for genuine freelancers / consultants, not for exclusive full-time workers."),
        ("How quickly can I onboard someone via EOR in India?",
         "1-3 weeks from offer acceptance: EOR drafts employment contract (India-compliant), employee signs, PF registration + bank account linkage, payroll setup, Section 192 TDS registration if first employee. First salary credit on 1st or 7th of next month depending on cycle. Much faster than setting up your own entity (which takes 30-45 days before you can start payroll)."),
        ("Does BQP act as EOR for foreign companies hiring in India?",
         "Yes - integrated EOR + CA + tax engagement. We hold the Indian employment, run payroll + PF + ESI + Section 192 TDS + Form 24Q + Form 16, offer HR + legal support, and advise on PE risk + transition to own-subsidiary when scale justifies. Standard engagement for US / UK / EU / Singapore / UAE companies hiring 1-20 Indian employees. WhatsApp +91 78018 87130."),
    ],
    related=[
        ("foreign-company-setup-indian-subsidiary-wos.html", "Guide", "Own Subsidiary"),
        ("india-market-entry-foreign-company-guide.html", "Guide", "India Entry"),
    ],
    cta_headline="US / UK / EU company wanting to hire Indian talent fast?",
    cta_body="EOR via BQP: 1-3 week onboarding, full compliance stack, PE-risk advisory, transition to own-subsidiary when ready. Scope-based pricing. WhatsApp +91 78018 87130.",
))

# 8. Remote audit of Indian company
write_page("india-audit-services-foreign-shareholder-remote", page(
    slug="india-audit-services-foreign-shareholder-remote",
    title="India Audit Services for Foreign Shareholder 2026 | Remote CA Audit - BQP",
    description="Statutory audit + tax audit + TP audit of Indian subsidiary / company for foreign shareholder: fully remote execution, IFRS to Ind AS reconciliation, Form 3CD + Form 3CEB signing, group-reporting-package delivery to foreign parent in parent's format. Standard annual engagement for US / UK / EU / Singapore / UAE parent companies. Working CA guide by Durgesh Chavda.",
    keywords="India company audit foreign shareholder, remote audit India CA, statutory audit Indian subsidiary foreign parent, tax audit India foreign company, Ind AS to IFRS reconciliation",
    hero_kicker="/ Foreign Clients &middot; Remote India Audit &middot; Updated 2026-10-13",
    hero_title_html="India audit for foreign shareholder, <em>fully remote delivery.</em>",
    hero_lead="Foreign parent (US Delaware C-Corp, UK Ltd, Singapore Pte Ltd, Dutch BV) with Indian subsidiary needs annual audit under Companies Act 2013. Must be signed by Indian CA. Everything can be done remotely from India &mdash; data room access, management calls, draft audit opinion, final signing. Group reporting package delivered to parent in parent's format (US GAAP / IFRS / consolidation pack). Here's how it works.",
    sections=[
        ("/ India audit requirements", "Three audits.",
         "<p>Indian subsidiary of foreign parent faces three concurrent audits:</p>"
         "<p><strong>1. Statutory Audit (Companies Act 2013)</strong></p>"
         "<ul>"
         "<li>Mandatory for every Indian company (Pvt Ltd and Public Ltd) regardless of size.</li>"
         "<li>Appointment of statutory auditor at first board meeting (first year) and at AGM (ongoing).</li>"
         "<li>Signed by Indian Chartered Accountant (member of ICAI).</li>"
         "<li>Audit report under Companies Act 2013 + ICAI auditing standards (SA 700 series).</li>"
         "<li>Includes CARO 2020 reporting (Companies Auditor's Report Order) with 20+ specific matters.</li>"
         "<li>Deliverable: audited financial statements + audit report + CARO + Board's report.</li>"
         "<li>Deadline: before AGM (within 6 months of FY end &mdash; typically September).</li>"
         "</ul>"
         "<p><strong>2. Tax Audit (Section 44AB Income Tax)</strong></p>"
         "<ul>"
         "<li>Mandatory if turnover &gt; INR 1 crore (or 10 crore for digital transactions-dominated businesses).</li>"
         "<li>Signed by Indian CA.</li>"
         "<li>Form 3CA + Form 3CD (46-clause detailed questionnaire).</li>"
         "<li>Deadline: 31 October of AY (vs 31 July for non-tax-audit).</li>"
         "</ul>"
         "<p><strong>3. Transfer Pricing Audit (Section 92E / Rule 10E)</strong></p>"
         "<ul>"
         "<li>Mandatory for any company with international transactions &gt; INR 1 crore (nearly every foreign-subsidiary triggers).</li>"
         "<li>Form 3CEB signed by Indian CA.</li>"
         "<li>Deadline: 31 October (extended once in recent years to 30 November).</li>"
         "<li>See <a href='transfer-pricing-india-foreign-mnc.html'>TP guide</a>.</li>"
         "</ul>"),
        ("/ Ind AS vs AS (Accounting Standards)", "Which applies.",
         "<p>Indian accounting framework:</p>"
         "<ul>"
         "<li><strong>Ind AS (Indian Accounting Standards)</strong> &mdash; converged with IFRS. Mandatory for:</li>"
         "<li>&nbsp;&nbsp;&mdash; Listed companies.</li>"
         "<li>&nbsp;&nbsp;&mdash; Unlisted companies with net worth &gt;= INR 250 crore.</li>"
         "<li>&nbsp;&nbsp;&mdash; Subsidiaries, JVs, associates of the above.</li>"
         "<li>&nbsp;&nbsp;&mdash; Any company that voluntarily adopts Ind AS.</li>"
         "<li><strong>AS (Accounting Standards, older)</strong> &mdash; for everyone else (small/medium unlisted companies with net worth &lt; INR 250 crore).</li>"
         "</ul>"
         "<p>For foreign subsidiaries, Ind AS adoption is often <strong>recommended</strong> even below threshold &mdash; it simplifies the IFRS consolidation pack for the foreign parent (Ind AS and IFRS are 95%+ identical post-2019 updates).</p>"),
        ("/ Remote audit workflow", "How it actually runs.",
         "<p><strong>Pre-audit (May-June)</strong>:</p>"
         "<ul>"
         "<li>Scoping call with Indian team + foreign parent finance.</li>"
         "<li>Data room setup (Google Drive / Dropbox / Box / foreign parent's SharePoint).</li>"
         "<li>Internal control walkthrough (video calls with Indian team).</li>"
         "<li>Audit plan + risk assessment memo shared with parent.</li>"
         "</ul>"
         "<p><strong>Fieldwork (June-August)</strong>:</p>"
         "<ul>"
         "<li>Trial balance review.</li>"
         "<li>Sample testing of revenue, expenses, AR, AP.</li>"
         "<li>Confirmation letters: banks, major customers, major vendors, related parties.</li>"
         "<li>Physical verification (if required): BQP team member visits Indian office / warehouse once a year with video documentation shared with parent.</li>"
         "<li>Weekly status call with Indian management + bi-weekly with parent finance.</li>"
         "</ul>"
         "<p><strong>Reporting (August-September)</strong>:</p>"
         "<ul>"
         "<li>Draft audit report + management letter.</li>"
         "<li>Discussion of findings with Indian management + parent.</li>"
         "<li>Finalisation + signing by Indian CA partner.</li>"
         "<li>CARO 2020 reporting.</li>"
         "<li>Delivery: PDF signed audit report + Word draft for parent's consolidation + Excel schedules.</li>"
         "<li>Parent-format reporting package: adjustments to IFRS / US GAAP, group reporting template (BQP fills parent's standard template).</li>"
         "</ul>"
         "<p><strong>Tax audit + TP audit (September-October)</strong>: run concurrently; Form 3CA/CD/CEB signed and filed by 31 October.</p>"),
        ("/ Common issues for foreign-shareholder audits", "Where accuracy matters.",
         "<ul>"
         "<li><strong>Related-party transaction disclosure</strong>: every transaction with foreign parent + sister companies + ultimate controlling party must be disclosed per AS-18 / Ind AS 24. Scrutinised in audit + Form 3CD + Form 3CEB.</li>"
         "<li><strong>Transfer pricing adjustments</strong>: if historical TP position weak, audit may require provision for likely addition.</li>"
         "<li><strong>Foreign currency translation</strong>: Ind AS 21 / AS 11 &mdash; closing rate for monetary items, historical for non-monetary. Mis-translation changes P&amp;L materially.</li>"
         "<li><strong>Group recharge / cost allocation</strong>: parent charges IT / HR / finance costs to Indian subsidiary. Benefit test required. Documentation of allocation key. Common audit finding + TP exposure.</li>"
         "<li><strong>Reporting-package format</strong>: parent asks for US GAAP vs Ind AS reconciliation (Rev Rec ASC 606 vs Ind AS 115, Lease ASC 842 vs Ind AS 116, Fin Instrument ASC 326 vs Ind AS 109). BQP delivers reconciliation schedule.</li>"
         "<li><strong>CARO 2020 reporting</strong>: 20+ specific matters; parent's auditor may ask about specific items (fixed asset register, loans + advances, inventory count, pending litigation, undisclosed income under IT scrutiny).</li>"
         "</ul>"
         "<p><em>Last updated: 2026-10-13.</em></p>"),
    ],
    faqs=[
        ("Can an Indian company's audit be done fully remotely?",
         "Yes - substantially. Data room access via cloud, management calls on Zoom, sample testing on scanned documents, confirmation letters sent/received electronically. Physical verification (fixed assets, inventory, if applicable) requires one annual in-person visit by BQP team member - videos + photos shared with parent. Final signing + ROC filing is India-only but doesn't require foreign parent presence."),
        ("Is Ind AS or AS applicable to my Indian subsidiary?",
         "Ind AS mandatory if net worth >= INR 250 crore OR if parent is listed OR if subsidiary of Ind AS-adopter. Below that, older AS applies. For foreign subsidiaries, Ind AS voluntary adoption is often recommended - simplifies IFRS consolidation at parent level. Ind AS and IFRS are 95%+ identical post-2019."),
        ("When are India audits due?",
         "Statutory audit: before AGM (within 6 months of FY end - so typically by late September). Tax audit (Section 44AB): 31 October of AY. Transfer pricing audit (Form 3CEB): 31 October (sometimes extended to 30 November). Non-compliance: late fees + penalties + ITR filing blockage."),
        ("Does BQP deliver audit report in parent's reporting format?",
         "Yes - standard scope includes: Indian-GAAP signed audit report (per Companies Act 2013), Ind AS to IFRS / US GAAP reconciliation schedule, group-reporting-template fill (parent's standard template), management letter + CARO 2020 for group audit team review. Monthly MIS to parent in parent's format."),
        ("Who signs the Indian audit report?",
         "Indian Chartered Accountant (ICAI member) and partner of an ICAI-registered firm (sole proprietor CA, LLP, or Partnership). Foreign auditors (US CPA, UK CA, etc.) cannot sign Indian statutory audit directly. BQP's Indian partners sign; coordination with foreign parent's auditor (Big 4 or regional) is standard."),
        ("Does BQP handle India audit for foreign-shareholder subsidiaries?",
         "Yes - full annual stack: statutory audit (Companies Act) + tax audit (Section 44AB) + TP audit (Form 3CEB) + ROC filings (AOC-4 + MGT-7; DIR-3 KYC every three years) + FLA Return (RBI) + annual ITR filing + parent reporting package. Standard annual engagement scoped per turnover + complexity. WhatsApp +91 78018 87130."),
    ],
    related=[
        ("foreign-company-setup-indian-subsidiary-wos.html", "Guide", "WOS Setup"),
        ("transfer-pricing-india-foreign-mnc.html", "Guide", "TP"),
    ],
    cta_headline="Foreign parent with Indian subsidiary - audit season approaching?",
    cta_body="Full remote delivery from India: statutory + tax + TP audit + ROC + FLA + parent-format reporting. One firm, one annual engagement. Scope by turnover + complexity.",
))

# 9. Section 195 TDS foreign payer
write_page("section-195-tds-foreign-payer-indian-vendor", page(
    slug="section-195-tds-foreign-payer-indian-vendor",
    title="Section 195 TDS by Foreign Payer to Indian Vendor 2026 - BQP",
    description="Section 195 India TDS when foreign company pays Indian service provider: when 195 applies, DTAA relief for Indian resident payee, TRC + Form 10F, PE risk analysis, representative assessee under Section 160, remitting India TDS from abroad. CA guidance from India. Working CA guide by Durgesh Chavda.",
    keywords="Section 195 TDS foreign payer India, foreign company TDS to Indian vendor, DTAA relief Indian resident, Section 160 representative assessee, Section 195 TDS from abroad",
    hero_kicker="/ Foreign Clients &middot; Section 195 &middot; Updated 2026-10-13",
    hero_title_html="Section 195 TDS, <em>when you're the foreign payer.</em>",
    hero_lead="Foreign company making payment to Indian service provider (freelancer, consultant, vendor) &mdash; does Section 195 India TDS apply? The usual answer: yes, if the payment is 'chargeable to tax in India'. But most foreign payers get this wrong, often over-withholding on simple services or under-withholding on technical services. Here's the correct framework.",
    sections=[
        ("/ When does Section 195 apply", "The chargeability test.",
         "<p>Section 195 Income Tax Act: any person (whether resident or non-resident) making payment to a non-resident that is 'chargeable to tax in India' must deduct TDS. Note: the payer can also be a non-resident &mdash; so foreign company paying Indian vendor could trigger Section 195.</p>"
         "<p>But wait &mdash; Section 195 is about payment to a non-resident. If you're paying an Indian resident (Indian individual CA / Indian company), Section 195 does NOT apply. Sections 194C / 194J / 194A would apply if the payer has an India tax presence (PE / fixed place / branch).</p>"
         "<p>So the question splits:</p>"
         "<ul>"
         "<li><strong>Foreign payer, non-resident payee</strong>: Section 195 applies IF the income is India-sourced (Section 9) or deemed to accrue in India.</li>"
         "<li><strong>Foreign payer, resident payee (Indian citizen / Indian company)</strong>: Sections 194C / 194J etc. may apply IF foreign payer has an India tax presence. If foreign payer has NO India presence &mdash; usually no TDS obligation on foreign payer; Indian resident pays own tax on receipt.</li>"
         "</ul>"
         "<p>Most foreign-payer-to-Indian-vendor scenarios are the second case: no TDS obligation on foreign payer. Indian vendor files own ITR and pays own tax.</p>"),
        ("/ The common misconception", "Foreign payer over-withholds.",
         "<p>Many foreign companies pay their Indian vendors (freelance developer in Bangalore, consultant in Mumbai, agency in Delhi) and ask 'should we withhold Indian tax?'. If the Indian vendor is an Indian resident (Indian individual or Indian company), the standard answer is <strong>No</strong>. The foreign payer has no India TDS obligation (because the foreign payer has no India tax presence that would make Sections 194C/194J/194A applicable).</p>"
         "<p>The Indian vendor:</p>"
         "<ul>"
         "<li>Receives gross payment.</li>"
         "<li>Reports it as income in their Indian ITR.</li>"
         "<li>Pays own income tax (slab rate for individuals, 25% / 22% for companies).</li>"
         "<li>Charges GST if their turnover crosses threshold (zero-rated if export of service under GST rules).</li>"
         "</ul>"
         "<p>Confirming: foreign payer's obligation is to pay the agreed invoice amount. No India TDS. No Indian compliance obligation.</p>"),
        ("/ When foreign payer DOES have Section 195 obligation", "The exceptions.",
         "<p>Foreign payer DOES have Section 195 obligation when:</p>"
         "<ul>"
         "<li><strong>Payee is a non-resident entity</strong> (not an Indian resident) and income is India-sourced. Example: US company pays UK consultant for work done in India &mdash; UK consultant is non-resident; income may be India-sourced; Section 195 applies.</li>"
         "<li><strong>Foreign payer has an Indian branch / fixed place / PE</strong>, and the payment is made through / attributable to that India presence. Section 195 then applies.</li>"
         "<li><strong>Payment is treated as 'representative assessee' matter under Section 160</strong>: if foreign payer has an Indian representative (agent, broker, Indian subsidiary), the representative can be assessed as 'representative assessee' for the foreign company's India-sourced income. Section 195 obligations shift to the Indian representative.</li>"
         "</ul>"
         "<p>For a US SaaS company paying an Indian individual CA for consulting work: Section 195 does not apply (payee is Indian resident, payer has no India presence).</p>"
         "<p>For an Indian subsidiary of a US company paying a UK consultant: Section 195 does apply (payee is non-resident; Indian subsidiary is the payer; payment chargeable to tax in India).</p>"),
        ("/ Practical scenarios + handling", "Three common cases.",
         "<p><strong>Case 1: US company pays Indian freelancer USD 10K/month for development work</strong></p>"
         "<ul>"
         "<li>Payee: Indian individual (resident).</li>"
         "<li>Foreign payer: no India presence.</li>"
         "<li>Section 195: not applicable.</li>"
         "<li>Action: pay full USD 10K via wire / Deel / Wise. Indian freelancer handles own ITR + GST.</li>"
         "</ul>"
         "<p><strong>Case 2: UK company pays Indian company (Pvt Ltd) INR 50 lakh for development project</strong></p>"
         "<ul>"
         "<li>Payee: Indian company (resident).</li>"
         "<li>Foreign payer: no India presence.</li>"
         "<li>Section 195: not applicable.</li>"
         "<li>Action: pay full INR 50 lakh. Indian company handles own corporate tax + GST (export of service under GST may apply &rarr; zero-rated with LUT bond).</li>"
         "</ul>"
         "<p><strong>Case 3: Indian subsidiary (of German parent) pays German consultant EUR 20K for technical services</strong></p>"
         "<ul>"
         "<li>Payee: German resident (non-resident of India).</li>"
         "<li>Indian subsidiary: the payer; has India tax presence.</li>"
         "<li>Section 195: applies.</li>"
         "<li>Chargeability: Fees for Technical Services (FTS) under Section 115A &rarr; chargeable in India at 20% default; 10% under India-Germany DTAA with TRC + Form 10F.</li>"
         "<li>Form 15CA + Form 15CB mandatory before remittance.</li>"
         "<li>Indian subsidiary deducts 10% TDS, deposits by 7th of next month, files Form 27Q quarterly.</li>"
         "</ul>"),
        ("/ What foreign companies should do", "Practical steps.",
         "<ul>"
         "<li><strong>Pay Indian residents gross</strong> (full invoice amount), no India TDS withholding. If you're a US company paying an Indian freelancer in Bangalore, pay USD X; the Indian freelancer handles their own India tax.</li>"
         "<li><strong>Insist on invoice + PAN</strong>: your Indian vendor should provide a GST-compliant invoice with their PAN. Keeps your audit trail clean.</li>"
         "<li><strong>GST awareness</strong>: Indian vendor's invoice may show GST at 18% (if their turnover crosses threshold AND they bill in INR) or zero (if export of service under GST rules). Either way, foreign payer pays the invoice; GST is Indian vendor's obligation.</li>"
         "<li><strong>If YOU have an Indian subsidiary</strong>: that subsidiary paying any non-resident vendor &rarr; Section 195 applies &rarr; 15CA + 15CB protocol. See <a href='form-15ca-15cb-foreign-remittance-india.html'>15CA/CB guide</a>.</li>"
         "<li><strong>Beneficial Ownership + Treaty Shopping risk</strong>: avoid routing payment through third-country intermediaries just to reduce TDS; India has GAAR + treaty-shopping provisions.</li>"
         "<li><strong>Doubt &rarr; written advisor opinion</strong>: a CA opinion letter costs little and clarifies the position; much cheaper than mistaken TDS obligations.</li>"
         "</ul>"
         "<p><em>Last updated: 2026-10-13.</em></p>"),
    ],
    faqs=[
        ("If I'm a US company paying an Indian freelancer, do I need to withhold Indian tax?",
         "No. Section 195 India TDS applies only when: (a) payee is non-resident of India AND income is India-sourced, OR (b) payer has India tax presence. Indian freelancer is Indian resident; US payer has no India presence. No Section 195 obligation. Pay full invoice amount. Indian freelancer handles own ITR + GST on their side."),
        ("What if I'm paying an Indian company (Pvt Ltd) from abroad?",
         "Same as above - Indian Pvt Ltd is Indian resident. Foreign payer with no India presence has no Section 195 TDS obligation. Pay full invoice. Indian company handles own corporate tax + GST (export of service may apply at zero rate with LUT bond)."),
        ("When does Section 195 definitely apply to a foreign payer?",
         "When payee is non-resident of India AND payment is chargeable in India (India-sourced income). Example: Indian subsidiary of foreign parent paying a non-resident consultant for FTS - Section 195 applies, Form 15CA/CB mandatory. Or: foreign payer with India branch/PE making payment through the India presence."),
        ("Can my Indian vendor charge me GST?",
         "Yes - if their Indian turnover crosses GST threshold (INR 20 lakh / 40 lakh depending on state and type). But export of service to foreign client is typically zero-rated under GST (place of supply outside India + payment in forex + LUT bond). So many Indian vendors bill foreign clients at zero GST while still being GST-registered. Verify your vendor's invoice format."),
        ("What is 'representative assessee' under Section 160?",
         "Section 160 Income Tax Act: an Indian agent, broker, trustee, or Indian subsidiary of a foreign principal can be treated as the 'representative assessee' for the foreign person's India-sourced income. The representative is liable for India tax + TDS on behalf of the foreign principal. Shifts Section 195 obligations to the Indian representative."),
        ("Does BQP help foreign payers with India tax position clarification?",
         "Yes - written tax opinion letters on specific payment scenarios (does Section 195 apply? what rate? treaty relief available? PE risk?), Form 15CA/CB execution if applicable, PE risk analysis, representative assessee clarity. Standard advisory engagement. WhatsApp +91 78018 87130."),
    ],
    related=[
        ("form-15ca-15cb-foreign-remittance-india.html", "Guide", "Form 15CA/CB"),
        ("employer-of-record-india-hire-from-abroad.html", "Guide", "EOR India"),
    ],
    cta_headline="Foreign company paying Indian vendors / contractors?",
    cta_body="Over-withholding India TDS costs vendor relationship. Under-withholding risks audit. Get a written CA opinion letter on your specific payment flow &mdash; cheap, clear, defensible.",
))

# 10. Repatriate profits
write_page("repatriate-profits-india-foreign-parent", page(
    slug="repatriate-profits-india-foreign-parent",
    title="Repatriate Profits from India to Foreign Parent 2026 | Dividend Royalty FTS - BQP",
    description="Repatriating profits from Indian subsidiary to foreign parent in 2026: dividend route (post DDT abolition, Section 195 TDS 20% / treaty rate), royalty + FTS Section 115A, buyback vs dividend, deemed dividend Section 2(22)(e), FEMA current account vs capital account. Done remotely from India by CA for US / UK / EU / Singapore / UAE parent. Working CA guide by Durgesh Chavda.",
    keywords="repatriate profits India foreign parent, dividend from India Section 195, royalty FTS Section 115A, dividend vs buyback India, FEMA repatriation current account capital account",
    hero_kicker="/ Foreign Clients &middot; Profit Repatriation &middot; Updated 2026-10-13",
    hero_title_html="Repatriate profits, <em>dividend vs royalty vs FTS vs buyback.</em>",
    hero_lead="Foreign parent with profitable Indian subsidiary &mdash; how to get the cash out. Four main routes: dividend, royalty, Fees for Technical Services (FTS), buyback. Each has different tax rate, FEMA compliance, and defensibility. Section 195 TDS applies to all; treaty rate varies by DTAA. Post DDT abolition (April 2020), tax is in the shareholder's hands &mdash; typically ~10-15% withholding under treaty vs 20% default. Here's the practitioner's decision framework.",
    sections=[
        ("/ The four repatriation routes", "Decision table.",
         "<p><strong>1. Dividend</strong></p>"
         "<ul>"
         "<li>Post April 2020: DDT abolished. Dividend taxable in foreign parent's hands &mdash; Section 195 TDS 20% default; 10-15% under DTAA with TRC + Form 10F.</li>"
         "<li>Pre-conditions: Indian subsidiary must have distributable profits (per Companies Act Section 123); must pass solvency test.</li>"
         "<li>Board resolution + sometimes AGM declaration.</li>"
         "<li>FEMA: current account transaction &mdash; permitted via AD bank without special approval.</li>"
         "<li>Form 15CA + 15CB mandatory.</li>"
         "</ul>"
         "<p><strong>2. Royalty / License Fee</strong></p>"
         "<ul>"
         "<li>Parent licenses IP (brand, patent, technology, software) to Indian subsidiary; subsidiary pays royalty.</li>"
         "<li>Section 115A: 20% TDS default; 10% under most DTAAs with TRC + Form 10F.</li>"
         "<li>Deductible in Indian subsidiary's P&amp;L (unlike dividend which is not).</li>"
         "<li>Transfer pricing scrutiny &mdash; must be benchmarked.</li>"
         "<li>FEMA: current account; subject to Reserve Bank Automatic Route limits (typically 5% of domestic sales for brand; 8% of exports for brand).</li>"
         "</ul>"
         "<p><strong>3. Fees for Technical Services (FTS) / Management Fee</strong></p>"
         "<ul>"
         "<li>Parent provides services (management, consulting, IT, HR) to Indian subsidiary.</li>"
         "<li>Section 115A: 20% TDS default; 10% under DTAA.</li>"
         "<li>Deductible in Indian subsidiary's P&amp;L subject to benefit test + TP arm's-length.</li>"
         "<li>Common adjustment target in TP scrutiny if lacking substance.</li>"
         "</ul>"
         "<p><strong>4. Buyback / Capital Reduction</strong></p>"
         "<ul>"
         "<li>Indian subsidiary buys back shares from foreign parent.</li>"
         "<li>Section 115QA: buyback tax 20% + surcharge on distributed income (effectively ~23.3%).</li>"
         "<li>Receipt in parent's hands = capital gain &mdash; often non-taxable in India for foreign parent (Section 10(34A) exempts buyback-related income).</li>"
         "<li>FEMA: subject to pricing guidelines; must be at fair value.</li>"
         "<li>Companies Act: 10%-25% maximum buyback limits + 2-year gap between buybacks.</li>"
         "<li>Complex but useful for large one-time repatriation.</li>"
         "</ul>"),
        ("/ Choosing the right route", "Decision factors.",
         "<p><strong>For small recurring repatriation (USD 100K-1M annually)</strong>:</p>"
         "<ul>"
         "<li>Dividend if India has profit history + distributable reserves. Simplest, lowest friction.</li>"
         "</ul>"
         "<p><strong>For loss-making Indian subsidiary that still needs to repatriate</strong>:</p>"
         "<ul>"
         "<li>Dividend impossible (no profits).</li>"
         "<li>Royalty / FTS acceptable &mdash; parent charges for services / IP. Must be TP-defensible.</li>"
         "<li>Capital reduction possible but one-off.</li>"
         "</ul>"
         "<p><strong>For brand / IP-heavy groups</strong>:</p>"
         "<ul>"
         "<li>Royalty is natural &mdash; parent owns brand, licensed to Indian subsidiary.</li>"
         "<li>5% of domestic sales benchmark typical; TP benchmarking supports.</li>"
         "</ul>"
         "<p><strong>For large one-time repatriation (USD 10M+)</strong>:</p>"
         "<ul>"
         "<li>Buyback / capital reduction may be more tax-efficient than dividend (buyback tax 20% on distribution amount vs 20% TDS on dividend amount &mdash; roughly similar but can be optimised).</li>"
         "<li>Also provides cap table cleanup.</li>"
         "</ul>"
         "<p><strong>Deemed dividend (Section 2(22)(e))</strong> trap:</p>"
         "<ul>"
         "<li>If Indian subsidiary gives loan / advance to parent (or shareholder with 10%+ holding), treated as deemed dividend.</li>"
         "<li>Avoids by: proper documentation (interest-bearing commercial loan, FEMA ECB compliance), repayment schedule.</li>"
         "</ul>"),
        ("/ Treaty rates for key countries", "DTAA WHT.",
         "<table style='width:100%;border-collapse:collapse;margin:12px 0;font:400 13px Inter'>"
         "<tr style='background:#f8f3e8'><th style='padding:8px;border:1px solid #ece4d5;text-align:left'>Country</th><th style='padding:8px;border:1px solid #ece4d5;text-align:left'>Dividend (DTAA)</th><th style='padding:8px;border:1px solid #ece4d5;text-align:left'>Royalty (DTAA)</th><th style='padding:8px;border:1px solid #ece4d5;text-align:left'>FTS (DTAA)</th></tr>"
         "<tr><td style='padding:8px;border:1px solid #ece4d5'><strong>USA</strong></td><td style='padding:8px;border:1px solid #ece4d5'>15% (25% hold); 25% else</td><td style='padding:8px;border:1px solid #ece4d5'>10-15%</td><td style='padding:8px;border:1px solid #ece4d5'>10-15%</td></tr>"
         "<tr><td style='padding:8px;border:1px solid #ece4d5'><strong>UK</strong></td><td style='padding:8px;border:1px solid #ece4d5'>10% (10% hold); 15% else</td><td style='padding:8px;border:1px solid #ece4d5'>10-15%</td><td style='padding:8px;border:1px solid #ece4d5'>10-15%</td></tr>"
         "<tr><td style='padding:8px;border:1px solid #ece4d5'><strong>Singapore</strong></td><td style='padding:8px;border:1px solid #ece4d5'>10% (25% hold); 15% else</td><td style='padding:8px;border:1px solid #ece4d5'>10%</td><td style='padding:8px;border:1px solid #ece4d5'>10%</td></tr>"
         "<tr><td style='padding:8px;border:1px solid #ece4d5'><strong>Mauritius</strong></td><td style='padding:8px;border:1px solid #ece4d5'>5% (10% hold); 15% else</td><td style='padding:8px;border:1px solid #ece4d5'>15%</td><td style='padding:8px;border:1px solid #ece4d5'>10%</td></tr>"
         "<tr><td style='padding:8px;border:1px solid #ece4d5'><strong>UAE</strong></td><td style='padding:8px;border:1px solid #ece4d5'>10%</td><td style='padding:8px;border:1px solid #ece4d5'>10%</td><td style='padding:8px;border:1px solid #ece4d5'>10%</td></tr>"
         "<tr><td style='padding:8px;border:1px solid #ece4d5'><strong>Netherlands</strong></td><td style='padding:8px;border:1px solid #ece4d5'>10%</td><td style='padding:8px;border:1px solid #ece4d5'>10%</td><td style='padding:8px;border:1px solid #ece4d5'>10%</td></tr>"
         "<tr><td style='padding:8px;border:1px solid #ece4d5'><strong>Germany</strong></td><td style='padding:8px;border:1px solid #ece4d5'>10%</td><td style='padding:8px;border:1px solid #ece4d5'>10%</td><td style='padding:8px;border:1px solid #ece4d5'>10%</td></tr>"
         "</table>"
         "<p><em>Rates indicative; verify specific DTAA article + beneficial ownership + GAAR implications before relying.</em></p>"
         "<p><strong>Must-haves for treaty rate</strong>: TRC from parent's country + Form 10F (electronic post Oct 2023) + No-PE declaration (where applicable).</p>"),
        ("/ Execution workflow", "What repatriation actually involves.",
         "<ol>"
         "<li><strong>Confirm distributable profits</strong> (for dividend) or arm's-length pricing (for royalty / FTS).</li>"
         "<li><strong>Board / shareholder resolution</strong>: Indian subsidiary's board/AGM declares dividend / approves royalty rate / FTS contract.</li>"
         "<li><strong>Documents from foreign parent</strong>: TRC + Form 10F + PAN (if available).</li>"
         "<li><strong>Form 15CA + 15CB</strong>: filed on Indian e-filing portal before remittance. See <a href='form-15ca-15cb-foreign-remittance-india.html'>15CA/CB guide</a>.</li>"
         "<li><strong>TDS deduction</strong>: at treaty rate (or 20% if TRC/Form 10F missing).</li>"
         "<li><strong>Section 195 TDS deposit</strong>: by 7th of next month.</li>"
         "<li><strong>Form 27Q quarterly return</strong>: by 31 Jul / 31 Oct / 31 Jan / 31 May.</li>"
         "<li><strong>AD bank processing</strong>: with 15CA acknowledgement + 15CB attached, bank releases SWIFT.</li>"
         "<li><strong>Payee receives net remittance</strong> in foreign bank account.</li>"
         "<li><strong>Form 16A</strong> issued to foreign payee for TDS credit (if payee files Indian ITR to claim refund where applicable).</li>"
         "</ol>"
         "<p><em>Last updated: 2026-10-13.</em></p>"),
    ],
    faqs=[
        ("Is dividend from Indian subsidiary taxable in India post DDT abolition?",
         "No DDT (Dividend Distribution Tax, previously ~20% in company's hands). From April 2020, dividend is taxable in shareholder's hands. For foreign shareholder: Section 195 TDS at 20% default; 10-15% under DTAA with TRC + Form 10F. Indian subsidiary deducts and deposits TDS; foreign parent receives net remittance."),
        ("What's cheaper - dividend or royalty for profit repatriation?",
         "Comparable at treaty rates (both ~10-15% WHT) but royalty is deductible in Indian subsidiary's P&L (reduces Indian corporate tax ~25%) while dividend is not. Net: royalty often more tax-efficient at group level IF supported by TP benchmarks + genuine IP ownership at parent. Risk: aggressive royalty rates trigger TP scrutiny."),
        ("What is 'deemed dividend' under Section 2(22)(e)?",
         "If Indian subsidiary gives a loan or advance to its parent (or any shareholder holding 10%+), the loan/advance is treated as deemed dividend to the extent of accumulated profits. Taxable in recipient's hands. Avoid by: (a) proper commercial loan documentation with interest + repayment schedule, (b) FEMA ECB compliance for cross-border loans, (c) using dividend/royalty route instead of informal transfers."),
        ("Do I need TRC and Form 10F every year?",
         "Yes - TRC is typically annual (year-specific). Form 10F is electronic (post Oct 2023 via India e-filing portal), also annual. Both required for every remittance claiming DTAA treaty rate. Must be in place before Form 15CB is signed. BQP maintains TRC + Form 10F file for recurring remittance clients."),
        ("Can I use buyback to repatriate from India?",
         "Yes - Indian subsidiary buys back shares from foreign parent. Buyback tax under Section 115QA: 20% + surcharge on distributed income (~23.3% effective) paid by Indian subsidiary. Receipt is capital gain in parent's hands but Section 10(34A) exempts buyback-related income - foreign parent typically pays no further India tax. Useful for large one-time repatriation + cap table cleanup. Max 10-25% buyback per Companies Act with 2-year gap."),
        ("Does BQP handle profit repatriation end-to-end?",
         "Yes - route recommendation (dividend vs royalty vs FTS vs buyback), TP support (for royalty + FTS), TRC + Form 10F coordination with parent, Form 15CA + 15CB preparation, Section 195 TDS deposit + Form 27Q quarterly filing, AD bank liaison for SWIFT, Form 16A issuance. Standard annual engagement for Indian subsidiaries of foreign parents making regular remittances. WhatsApp +91 78018 87130."),
    ],
    related=[
        ("form-15ca-15cb-foreign-remittance-india.html", "Guide", "Form 15CA/CB"),
        ("india-us-tax-treaty-dtaa.html", "Guide", "India-US DTAA"),
    ],
    cta_headline="Need to repatriate profits from Indian subsidiary to foreign parent?",
    cta_body="Dividend, royalty, FTS, buyback - each has different tax rate + TP risk + FEMA compliance. BQP: route recommendation + Form 15CA/CB + Section 195 execution + annual compliance. Scope-based.",
))

# 11. Branch vs Liaison vs WOS
write_page("branch-office-vs-liaison-vs-wos-india-foreign", page(
    slug="branch-office-vs-liaison-vs-wos-india-foreign",
    title="Branch Office vs Liaison Office vs WOS India 2026 | Foreign Company Entry - BQP",
    description="Complete comparison for foreign company India entry: Branch Office vs Liaison Office vs Project Office vs Wholly-Owned Subsidiary vs LLP. RBI approval, permitted activities, tax, FDI, repatriation, closure. Decision framework for US / UK / EU / Singapore / UAE companies. Working CA guide by Durgesh Chavda.",
    keywords="branch office vs liaison office India, WOS vs branch office India, India entity options foreign company, Pvt Ltd vs branch India, LLP India foreign",
    hero_kicker="/ Foreign Clients &middot; Entity Comparison &middot; Updated 2026-10-13",
    hero_title_html="Branch vs Liaison vs WOS, <em>which India entity fits.</em>",
    hero_lead="Foreign company evaluating India entry has five legal options. Each has different RBI approval, permitted activities, tax position, FDI treatment, and closure complexity. The right choice depends on scope + duration + revenue model + risk appetite. For 90% of companies, WOS Pvt Ltd is the answer. For the 10% exceptions, here's the detailed comparison.",
    sections=[
        ("/ The five options at a glance", "Comparison table.",
         "<table style='width:100%;border-collapse:collapse;margin:12px 0;font:400 12px Inter'>"
         "<tr style='background:#f8f3e8'><th style='padding:6px;border:1px solid #ece4d5;text-align:left'>Feature</th><th style='padding:6px;border:1px solid #ece4d5;text-align:left'>WOS Pvt Ltd</th><th style='padding:6px;border:1px solid #ece4d5;text-align:left'>Branch Office</th><th style='padding:6px;border:1px solid #ece4d5;text-align:left'>Liaison Office</th><th style='padding:6px;border:1px solid #ece4d5;text-align:left'>Project Office</th><th style='padding:6px;border:1px solid #ece4d5;text-align:left'>LLP</th></tr>"
         "<tr><td style='padding:6px;border:1px solid #ece4d5'>Legal status</td><td style='padding:6px;border:1px solid #ece4d5'>Separate entity</td><td style='padding:6px;border:1px solid #ece4d5'>Extension of parent</td><td style='padding:6px;border:1px solid #ece4d5'>Rep office only</td><td style='padding:6px;border:1px solid #ece4d5'>Time-bound</td><td style='padding:6px;border:1px solid #ece4d5'>Separate entity</td></tr>"
         "<tr><td style='padding:6px;border:1px solid #ece4d5'>Can invoice?</td><td style='padding:6px;border:1px solid #ece4d5'>Yes</td><td style='padding:6px;border:1px solid #ece4d5'>Yes (narrow)</td><td style='padding:6px;border:1px solid #ece4d5'>NO</td><td style='padding:6px;border:1px solid #ece4d5'>Project-specific</td><td style='padding:6px;border:1px solid #ece4d5'>Yes</td></tr>"
         "<tr><td style='padding:6px;border:1px solid #ece4d5'>RBI prior approval</td><td style='padding:6px;border:1px solid #ece4d5'>No (automatic FDI)</td><td style='padding:6px;border:1px solid #ece4d5'>YES</td><td style='padding:6px;border:1px solid #ece4d5'>YES</td><td style='padding:6px;border:1px solid #ece4d5'>YES</td><td style='padding:6px;border:1px solid #ece4d5'>No (automatic in specific sectors)</td></tr>"
         "<tr><td style='padding:6px;border:1px solid #ece4d5'>FDI permitted</td><td style='padding:6px;border:1px solid #ece4d5'>Most sectors 100%</td><td style='padding:6px;border:1px solid #ece4d5'>N/A (not FDI)</td><td style='padding:6px;border:1px solid #ece4d5'>N/A</td><td style='padding:6px;border:1px solid #ece4d5'>N/A</td><td style='padding:6px;border:1px solid #ece4d5'>Limited</td></tr>"
         "<tr><td style='padding:6px;border:1px solid #ece4d5'>Tax rate</td><td style='padding:6px;border:1px solid #ece4d5'>25% / 22% (115BAA)</td><td style='padding:6px;border:1px solid #ece4d5'>40%+ (branch tax)</td><td style='padding:6px;border:1px solid #ece4d5'>No tax (no income)</td><td style='padding:6px;border:1px solid #ece4d5'>40%+ branch rate</td><td style='padding:6px;border:1px solid #ece4d5'>30%+ (slab/alternate)</td></tr>"
         "<tr><td style='padding:6px;border:1px solid #ece4d5'>Resident director</td><td style='padding:6px;border:1px solid #ece4d5'>YES (min 1)</td><td style='padding:6px;border:1px solid #ece4d5'>No (authorised rep)</td><td style='padding:6px;border:1px solid #ece4d5'>No (authorised rep)</td><td style='padding:6px;border:1px solid #ece4d5'>No</td><td style='padding:6px;border:1px solid #ece4d5'>YES (1 designated partner)</td></tr>"
         "<tr><td style='padding:6px;border:1px solid #ece4d5'>Repatriation</td><td style='padding:6px;border:1px solid #ece4d5'>Dividend / royalty / buyback</td><td style='padding:6px;border:1px solid #ece4d5'>Remittance of profits (post tax)</td><td style='padding:6px;border:1px solid #ece4d5'>No profits (reimbursement)</td><td style='padding:6px;border:1px solid #ece4d5'>Project surplus</td><td style='padding:6px;border:1px solid #ece4d5'>Distribution to partners</td></tr>"
         "<tr><td style='padding:6px;border:1px solid #ece4d5'>Closure complexity</td><td style='padding:6px;border:1px solid #ece4d5'>Medium</td><td style='padding:6px;border:1px solid #ece4d5'>High (RBI approval)</td><td style='padding:6px;border:1px solid #ece4d5'>Simpler (RBI approval)</td><td style='padding:6px;border:1px solid #ece4d5'>Project-end</td><td style='padding:6px;border:1px solid #ece4d5'>Medium</td></tr>"
         "</table>"),
        ("/ When each entity makes sense", "Decision scenarios.",
         "<p><strong>WOS Pvt Ltd &mdash; the default (90% of foreign entrants)</strong>:</p>"
         "<ul>"
         "<li>Want to invoice Indian customers.</li>"
         "<li>Will hire Indian employees for operational roles.</li>"
         "<li>Long-term India plan (3+ years).</li>"
         "<li>Need brand / IP / data residency presence.</li>"
         "<li>Want flexibility in exit (M&amp;A, IPO, buyback).</li>"
         "</ul>"
         "<p><strong>Branch Office</strong>:</p>"
         "<ul>"
         "<li>Narrow operational scope (export/import, consultancy, R&amp;D, agent).</li>"
         "<li>Parent prefers direct accountability (branch's acts bind parent legally).</li>"
         "<li>Sector where branch form is traditional (banks, insurance, airlines).</li>"
         "<li>Short-medium term presence; parent OK with branch tax rate (~40% vs 25% WOS).</li>"
         "</ul>"
         "<p><strong>Liaison Office</strong>:</p>"
         "<ul>"
         "<li>Exploratory market presence; no revenue plan for next 2-3 years.</li>"
         "<li>Market research, representation, communication with Indian customers.</li>"
         "<li>Expenses funded by parent remittance (not from local income).</li>"
         "<li>Must upgrade to WOS or Branch once commercial activity begins.</li>"
         "</ul>"
         "<p><strong>Project Office</strong>:</p>"
         "<ul>"
         "<li>Specific project with Indian client (typically government infrastructure, long-duration construction).</li>"
         "<li>Project duration generally &lt; 2-3 years.</li>"
         "<li>Automatically closes at project completion.</li>"
         "</ul>"
         "<p><strong>LLP</strong>:</p>"
         "<ul>"
         "<li>Rare for foreign parents.</li>"
         "<li>FDI permitted only in automatic-route sectors (not all).</li>"
         "<li>Smaller / professional services setup where limited liability + pass-through tax desired.</li>"
         "</ul>"),
        ("/ Branch Office specifics", "Setup + operation.",
         "<p>Branch Office setup under FEMA:</p>"
         "<ul>"
         "<li>RBI prior approval via Form FNC filed through AD-I category bank.</li>"
         "<li>Timeline: 2-4 months typical approval cycle.</li>"
         "<li>Permitted activities (specified in RBI Master Direction):</li>"
         "<li>&nbsp;&nbsp;&mdash; Export/import of goods.</li>"
         "<li>&nbsp;&nbsp;&mdash; Rendering professional/consultancy services.</li>"
         "<li>&nbsp;&nbsp;&mdash; R&amp;D activities.</li>"
         "<li>&nbsp;&nbsp;&mdash; Promoting technical / financial collaboration between Indian / foreign companies.</li>"
         "<li>&nbsp;&nbsp;&mdash; Representation as buying/selling agent in India.</li>"
         "<li>&nbsp;&nbsp;&mdash; IT and software services.</li>"
         "<li>&nbsp;&nbsp;&mdash; Technical support services.</li>"
         "<li>&nbsp;&nbsp;&mdash; Foreign airline/shipping company agency.</li>"
         "<li>Tax: 40% + surcharge + cess (branch of foreign company) = ~43.68% effective. Materially higher than WOS 25%.</li>"
         "<li>No separate legal entity &mdash; branch's acts legally bind foreign parent.</li>"
         "<li>Annual filings: audit, Income Tax, Form 29B (if MAT applicable), FLA Return.</li>"
         "</ul>"),
        ("/ Why most foreign companies choose WOS", "The economics.",
         "<p>Over 95% of foreign-origin new Indian entities in 2024-25 are WOS Pvt Ltd. Reasons:</p>"
         "<ul>"
         "<li><strong>Lower tax</strong>: 25% (standard) or 22% (Section 115BAA) &mdash; vs 40%+ for Branch.</li>"
         "<li><strong>No RBI prior approval</strong>: automatic FDI route for most sectors &rarr; 30-45 day setup vs 2-4 months for Branch.</li>"
         "<li><strong>Operational flexibility</strong>: can enter any lawful business, hire employees, sign long-term customer contracts, raise local debt, IPO in India later.</li>"
         "<li><strong>Exit flexibility</strong>: sell shares to Indian / foreign buyer, buyback, voluntary winding up &mdash; all simpler than Branch closure.</li>"
         "<li><strong>Liability shield</strong>: WOS liability stays with WOS; doesn't automatically extend to foreign parent.</li>"
         "<li><strong>Lower post-closure overhead</strong>: WOS is a standalone entity; closure doesn't trigger foreign-parent tax issues.</li>"
         "</ul>"
         "<p>Exceptions where Branch/Liaison still make sense: specific regulated sectors, narrow commercial scope, short-term exploratory presence, or specific tax-treaty optimisation.</p>"
         "<p><em>Last updated: 2026-10-13.</em></p>"),
    ],
    faqs=[
        ("Why would a foreign company choose Branch Office instead of WOS?",
         "Narrow permitted scope aligns with parent's needs (consultancy, R&D, buying/selling agent, foreign airline/shipping agency). Parent prefers direct accountability (branch's acts bind parent). Some regulated sectors (banks, airlines, insurance) traditionally use branch form. However, Branch has higher tax rate (~43.7% effective vs 25% WOS) and RBI prior approval (2-4 months) - most foreign entrants prefer WOS."),
        ("What's the difference between Branch and Liaison Office?",
         "Branch Office can conduct commercial activity (invoice Indian customers for permitted activities, generate revenue). Liaison Office cannot - purely representational (market research, communication, promotion). Liaison's expenses funded by parent remittance; no local income. Both require RBI prior approval. Liaison is typically precursor to upgrading to Branch or WOS once commercial activity planned."),
        ("Can a foreign company open an LLP in India?",
         "Yes - with restrictions. FDI into LLP permitted via automatic route in sectors where 100% FDI is allowed without any performance-linked conditions. Most IT / SaaS / services sectors qualify. Not permitted in sectors with FDI conditions (defence, insurance, retail trading). For foreign-parent entrants with pure services business, LLP can be an alternative to Pvt Ltd WOS - but rare in practice."),
        ("Which entity has the lowest tax rate for a foreign company in India?",
         "WOS Pvt Ltd under Section 115BAA: 22% + 10% surcharge + 4% cess = 25.17% effective. Branch Office of foreign company: 40% + 5% surcharge + 4% cess = 43.68% effective. LLP: 30% + surcharge + cess = ~34.94% effective (plus 30% alternate minimum tax on adjusted total income). WOS Pvt Ltd is materially the most tax-efficient."),
        ("How long does Branch Office setup take?",
         "2-4 months typical: Form FNC filing to AD-I bank (1 month compilation of parent docs + apostille), RBI review + approval (1-3 months). Add 1-2 months for bank account opening + PAN + GST post-approval. End-to-end 3-6 months. Compares with 30-45 days for WOS - a key reason WOS is preferred when parent flexibility is on timeline."),
        ("Does BQP handle all five entity structures for foreign companies?",
         "Yes - WOS Pvt Ltd (default, 90% of our foreign-client work), Branch Office (RBI Form FNC coordination + ongoing compliance), Liaison Office (FNC filing + annual reporting), Project Office (specific project + closure), LLP (where appropriate). Structure recommendation + end-to-end execution + annual compliance under one engagement. WhatsApp +91 78018 87130."),
    ],
    related=[
        ("foreign-company-setup-indian-subsidiary-wos.html", "Guide", "WOS Setup"),
        ("india-market-entry-foreign-company-guide.html", "Guide", "Market Entry"),
    ],
    cta_headline="Comparing India entity options for your foreign company?",
    cta_body="90% of foreign entrants choose WOS Pvt Ltd (25% tax, 30-45 day setup, no RBI prior approval). For the 10% that fit Branch / Liaison / Project / LLP, we scope the right route and execute end-to-end.",
))

# 12. India IP for foreign company
write_page("india-trademark-patent-ip-foreign-company", page(
    slug="india-trademark-patent-ip-foreign-company",
    title="India Trademark + Patent + IP Registration for Foreign Company 2026 - BQP",
    description="India IP registration for foreign company: trademark (Madrid Protocol vs direct), patent (PCT national phase), copyright, design, geographical indication. Timeline, cost, oppositions handling, assignments. Done remotely from India for US / UK / EU / Singapore / UAE applicants. Working CA + IP guide by Durgesh Chavda.",
    keywords="India trademark registration foreign company, Madrid Protocol India trademark, India patent PCT national phase, India copyright foreign, India IP registration from USA",
    hero_kicker="/ Foreign Clients &middot; India IP &middot; Updated 2026-10-13",
    hero_title_html="India IP registration, <em>from Delaware / London / Singapore.</em>",
    hero_lead="Foreign company protecting IP in India: trademark, patent, copyright, design. Can be filed from abroad &mdash; via Madrid Protocol (trademark), PCT national phase entry (patent), or direct filing via Indian IP agent (all types). Timeline + cost + oppositions handling + enforcement. Here's the complete practitioner's framework.",
    sections=[
        ("/ Trademark India for foreign applicant", "Two routes.",
         "<p><strong>Route 1: Madrid Protocol (international registration)</strong></p>"
         "<ul>"
         "<li>File a base application in home country (USPTO / UKIPO / EUIPO / etc.) then designate India via WIPO Madrid Protocol.</li>"
         "<li>Single application covers India + other designated countries.</li>"
         "<li>Timeline: 2-4 years from Madrid filing to Indian registration (India examines designations independently).</li>"
         "<li>Benefits: simpler administration (single renewal, single modification), cost-effective for multi-country protection.</li>"
         "<li>Drawbacks: dependent on home base registration first 5 years (central attack); Indian objections handled by Indian IP agent.</li>"
         "</ul>"
         "<p><strong>Route 2: Direct Indian application</strong></p>"
         "<ul>"
         "<li>File directly at Indian Trademark Registry via Form TM-A (national application).</li>"
         "<li>Foreign applicant must appoint Indian attorney / agent.</li>"
         "<li>Timeline: 18-36 months typical from filing to registration (varies by class + opposition).</li>"
         "<li>Benefits: independent of home base, direct control, faster for Indian-specific priority.</li>"
         "<li>Drawbacks: country-by-country costs if multi-national protection needed.</li>"
         "</ul>"
         "<p><strong>Which to pick</strong>:</p>"
         "<ul>"
         "<li>Multi-country launch (India + 3+ others): Madrid.</li>"
         "<li>India-only or India-priority: Direct.</li>"
         "<li>Existing US / EU registration + want India expansion: Madrid designation if home registration is already granted.</li>"
         "</ul>"),
        ("/ Trademark workflow + cost", "India specifics.",
         "<ol>"
         "<li><strong>Trademark search</strong>: free search on Indian TM Registry database (ipindiaonline.gov.in). Identify similar marks in your Nice class(es). Essential to avoid oppositions.</li>"
         "<li><strong>Classification</strong>: pick Nice Class(es) &mdash; 45 total (34 goods + 11 services). Fee per class.</li>"
         "<li><strong>Filing</strong>: TM-A (national) or WIPO Madrid designation. Government fee ~INR 4,500-9,000 per class (varies by applicant type: startup/MSME half-fee).</li>"
         "<li><strong>Examination</strong>: Indian examiner reviews on absolute grounds (distinctiveness) + relative grounds (prior marks) in ~6-18 months.</li>"
         "<li><strong>Examination report (if raised)</strong>: respond within 1 month. If objection sustained, hearing before Trademark Hearing Officer.</li>"
         "<li><strong>Publication</strong>: approved applications published in Trademark Journal.</li>"
         "<li><strong>Opposition</strong>: 4-month window post-publication for third parties to oppose. If opposed &rarr; proceedings before Trademark Registry (can take 2-4 years).</li>"
         "<li><strong>Registration</strong>: if no opposition / opposition dismissed, certificate issued.</li>"
         "<li><strong>Validity</strong>: 10 years from filing, renewable indefinitely.</li>"
         "</ol>"),
        ("/ Patent India for foreign applicant", "PCT national phase + direct.",
         "<p><strong>Route 1: PCT National Phase Entry</strong></p>"
         "<ul>"
         "<li>File PCT international application at WIPO (claiming priority from US / UK / etc. patent).</li>"
         "<li>Enter Indian national phase within 31 months of priority date.</li>"
         "<li>Filing fee ~INR 1,600-8,000 (government) + attorney fee.</li>"
         "<li>Timeline: 4-7 years from PCT filing to Indian grant (varies by field).</li>"
         "<li>Most foreign-origin Indian patents use this route.</li>"
         "</ul>"
         "<p><strong>Route 2: Direct Indian application (Convention application)</strong></p>"
         "<ul>"
         "<li>Within 12 months of priority date in home country.</li>"
         "<li>Independent Indian prosecution.</li>"
         "<li>Faster if India is key market.</li>"
         "</ul>"
         "<p><strong>Patent workflow</strong>:</p>"
         "<ol>"
         "<li>Prior art search.</li>"
         "<li>Filing: Form 1 (Request for Patent) + Form 2 (Provisional/Complete Specification) + claims + drawings. Attorney fee significant.</li>"
         "<li>18-month publication (automatic unless secrecy direction).</li>"
         "<li>Request for Examination within 48 months (Form 18).</li>"
         "<li>First Examination Report (FER) &mdash; respond within 6-12 months.</li>"
         "<li>Hearing (if needed) before Controller.</li>"
         "<li>Grant &rarr; publication &rarr; 20-year validity from filing date.</li>"
         "<li>Annuity fees every year from 3rd year.</li>"
         "</ol>"
         "<p><strong>Section 3 restrictions</strong>: certain subject matter not patentable in India &mdash; new form of known substance (Section 3(d)), method of agriculture, business methods per se, mathematical/business methods, computer programs per se, plants/animals (except microorganisms). Section 3(d) especially important for pharma patents.</p>"),
        ("/ Copyright + design + GI", "Other IP categories.",
         "<p><strong>Copyright</strong>:</p>"
         "<ul>"
         "<li>Automatic protection on creation (no registration mandatory in India for enforceability).</li>"
         "<li>Registration optional but useful as evidence of ownership + date.</li>"
         "<li>Covers: original literary / artistic / musical / dramatic works + cinematograph films + sound recordings + software source code.</li>"
         "<li>Term: author's life + 60 years for literary/musical works.</li>"
         "<li>Foreign authors / corporations: Berne Convention + India IP agent for registration.</li>"
         "</ul>"
         "<p><strong>Design Registration</strong>:</p>"
         "<ul>"
         "<li>Protects shape, configuration, ornamentation of articles.</li>"
         "<li>Term: 10 years + 5-year renewal.</li>"
         "<li>Priority claim within 6 months of foreign filing.</li>"
         "</ul>"
         "<p><strong>Geographical Indication (GI)</strong>:</p>"
         "<ul>"
         "<li>Mostly for Indian-origin products (Darjeeling tea, Basmati rice, Mysore silk).</li>"
         "<li>Foreign GI possible for products uniquely associated with a foreign region.</li>"
         "</ul>"),
        ("/ IP enforcement + oppositions", "What happens post-registration.",
         "<ul>"
         "<li><strong>Infringement suit</strong>: civil remedy before District Court / High Court. Injunction + damages + account of profits.</li>"
         "<li><strong>Opposition (TM)</strong>: as above, 4-month post-publication window.</li>"
         "<li><strong>Rectification</strong>: cancel registered mark on grounds of non-use (5 years) or improper registration.</li>"
         "<li><strong>Pre-grant opposition (Patent)</strong>: before grant, by any person.</li>"
         "<li><strong>Post-grant opposition (Patent)</strong>: within 1 year of grant.</li>"
         "<li><strong>Customs enforcement</strong>: register IP with Indian Customs (Form IEIR) to block counterfeit imports at border.</li>"
         "<li><strong>Criminal remedy (TM)</strong>: Section 103-104 Trademarks Act &mdash; imprisonment + fine for counterfeiters.</li>"
         "</ul>"
         "<p><em>Last updated: 2026-10-13.</em></p>"),
    ],
    faqs=[
        ("Can a US / UK / Singapore company register trademark in India directly?",
         "Yes - via two routes: (a) Madrid Protocol designating India via WIPO (requires home-country base registration), or (b) Direct Indian application via Form TM-A through an Indian trademark attorney. Both work. Madrid is cost-effective for multi-country protection; Direct is faster if India is the priority."),
        ("How long does Indian trademark registration take?",
         "18-36 months typical from filing to registration if no opposition. Timeline: examination (6-18 months), publication (immediate after examination clearance), 4-month opposition window, registration certificate issuance. If opposed, add 2-4 years for opposition proceedings. Madrid Protocol designation similar - Indian examination independent."),
        ("Can a foreign company file a patent in India?",
         "Yes - via (a) PCT national phase entry within 31 months of priority date, or (b) direct Indian application (Convention route) within 12 months of priority. Both require Indian patent agent. Timeline: 4-7 years from PCT filing to Indian grant typical. Section 3 restrictions apply - new form of known substance, business methods per se, software per se all excluded."),
        ("Does Section 3(d) really block pharma patents?",
         "Yes for 'evergreening' claims. Section 3(d) prohibits patents on new forms (salts, polymorphs, isomers, etc.) of known substances unless they show significantly enhanced efficacy. Famous Novartis Glivec case - Supreme Court denied patent on imatinib mesylate crystalline form. Foreign pharma applicants should assess Section 3(d) carefully for secondary patents."),
        ("Is copyright registration mandatory in India?",
         "No - copyright is automatic on creation (per Copyright Act). Registration optional but useful: provides prima facie evidence of ownership + date of creation + nature of work. Useful if enforcement litigation is likely. Foreign works protected under Berne Convention + Universal Copyright Convention automatically."),
        ("Does BQP handle India IP registration for foreign companies?",
         "Yes - integrated engagement combining Indian IP agent partner + CA + legal support: trademark (Madrid Protocol coordination + direct TM filing), patent (PCT national phase + Indian examination), copyright, design, Customs IPR Rules registration (to block counterfeit imports), oppositions handling, infringement litigation support. Standard engagement scoped per IP type + volume. WhatsApp +91 78018 87130."),
    ],
    related=[
        ("foreign-company-setup-indian-subsidiary-wos.html", "Guide", "WOS Setup"),
        ("india-market-entry-foreign-company-guide.html", "Guide", "Market Entry"),
    ],
    cta_headline="Protecting your IP in India from abroad?",
    cta_body="Trademark (Madrid or Direct), Patent (PCT National Phase), Copyright, Design &mdash; all registrable from US / UK / EU / Singapore / UAE via Indian IP agent. BQP integrated engagement.",
))

print("Batch M complete: 12 foreign-client inbound-India SEO pages written")
