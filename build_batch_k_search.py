# -*- coding: utf-8 -*-
"""Batch K: 10 search-intent-driven pages (verifiable high-volume Google patterns).

Targets gaps where (a) search volume is high per Google Trends / Autosuggest
observed patterns, (b) BQP currently has no content, (c) commercial intent
is clear (people search when they need help).
"""
from build_lib import page, write_page

# 1. Section 143(1) Intimation Response
write_page("section-143-1-intimation-response-india-2026", page(
    slug="section-143-1-intimation-response-india-2026",
    title="Section 143(1) Intimation Response Guide 2026 | Agree, Disagree, Rectification - BQP",
    description="Section 143(1) intimation received after ITR filing: understand the three outcomes (refund, demand, nil), reconcile with return, respond via rectification Section 154 if disagree. Step-by-step response guide by CA Durgesh Chavda.",
    keywords="Section 143(1) intimation response, Section 143(1) notice reply, income tax 143(1) intimation India, 143(1) refund demand nil, Section 154 rectification",
    hero_kicker="/ Blog &middot; Section 143(1) Intimation &middot; Updated 2026-10-10",
    hero_title_html="Section 143(1) intimation, <em>how to read it and respond.</em>",
    hero_lead="Every ITR filer gets a Section 143(1) intimation after processing &mdash; usually within 60-90 days of filing. It shows one of three outcomes: refund due, demand payable, or nil (return accepted as filed). Most people glance at it and move on. If the number does not match your ITR, you have 30 days under Section 154 to rectify. Here is the practitioner's response guide.",
    sections=[
        ("/ What Section 143(1) actually is", "Automated return processing, not scrutiny.",
         "<p>Section 143(1) of the Income Tax Act authorises the Centralised Processing Centre (CPC) at Bengaluru to process ITRs automatically. The system runs arithmetic checks, matches TDS claimed against Form 26AS, verifies tax paid against liability computed, and issues an intimation with one of three outcomes:</p>"
         "<ul>"
         "<li><strong>Refund due</strong> &mdash; TDS or advance tax exceeded final liability; refund credited to pre-validated bank account.</li>"
         "<li><strong>Demand payable</strong> &mdash; final liability exceeded tax paid; pay within 30 days or interest + penalty.</li>"
         "<li><strong>Nil &mdash; return accepted as filed</strong>.</li>"
         "</ul>"
         "<p>Section 143(1) is NOT scrutiny. It is automated reconciliation. If you receive a 143(1), the Department has not questioned your return &mdash; it has just processed it. Scrutiny is a separate notice under Section 143(2).</p>"
         "<p>Timeline: issued typically 60-90 days post-filing; must be issued within 9 months from the end of the FY in which the return is filed.</p>"),
        ("/ Three outcomes - what to do with each", "Response per outcome.",
         "<p><strong>If refund due:</strong> no action needed unless the amount is wrong. Refund credits to your pre-validated bank account (ensure PAN-Aadhaar + bank account validation is current on the e-filing portal) within 15-45 days. If no credit after 60 days, raise Refund Reissue on the portal.</p>"
         "<p><strong>If demand payable:</strong></p>"
         "<ul>"
         "<li>Compare the Department's computation (right column of 143(1)) with your ITR computation (left column). Find the difference.</li>"
         "<li>Common causes: TDS not matched (claimed in ITR but not in Form 26AS); deduction disallowed (e.g., Section 80C claimed but PF/LIC not reflected); interest under Section 234A/B/C added; standard deduction mismatch; HRA computed differently.</li>"
         "<li>If demand is correct &mdash; pay within 30 days via Challan 280 using the specific Section Code mentioned in the intimation.</li>"
         "<li>If demand is wrong &mdash; file Rectification under Section 154 within 4 years from end of the FY in which the intimation was passed.</li>"
         "</ul>"
         "<p><strong>If nil (return accepted):</strong> no action needed. Save the intimation PDF for your records; it is the official closure of return processing.</p>"),
        ("/ Rectification under Section 154", "When you disagree with the demand.",
         "<p>Section 154 allows the taxpayer (or the Department) to rectify a mistake apparent from record. Three common Section 154 rectifications for 143(1) demands:</p>"
         "<ol>"
         "<li><strong>TDS mismatch</strong> &mdash; TDS claimed in ITR not reflected in Form 26AS. Verify Form 26AS; if TDS is missing, chase the deductor (employer / bank / client) to file corrected Form 24Q/26Q. Once reflected, file Section 154 rectification online.</li>"
         "<li><strong>Deduction disallowed</strong> &mdash; e.g., Section 80C claim rejected because the deductor did not report the LIC/ELSS/NPS contribution. Collect the proof document (LIC premium receipt, ELSS statement, NPS annual statement) and file Section 154 with the proof.</li>"
         "<li><strong>Arithmetic error</strong> &mdash; CPC computed something differently (standard deduction, slab, surcharge). Prepare the correct computation and file Section 154 referencing the specific line item.</li>"
         "</ol>"
         "<p>Filing route: Login to incometax.gov.in &rarr; e-File &rarr; Rectification &rarr; Request Type: 'Reprocess the return' or 'Tax Credit Mismatch Correction' or 'Return Data Correction'. Attach supporting documents. CPC responds within 60-90 days typically.</p>"),
        ("/ Common 143(1) mistakes to avoid", "What we see in practice.",
         "<ul>"
         "<li><strong>Ignoring the demand for 30 days &mdash; interest under Section 220(2) at 1% per month starts.</strong> Even if you plan to rectify, respond or pay within the window.</li>"
         "<li><strong>Paying the demand without checking</strong> &mdash; many 143(1) demands are reversible via Section 154. Pay only after verifying the Department's computation is correct.</li>"
         "<li><strong>Not updating bank account</strong> &mdash; refund fails if the bank account on the e-filing portal is not pre-validated. Check Profile &rarr; My Bank Account before filing ITR each year.</li>"
         "<li><strong>Missing Form 26AS reconciliation</strong> &mdash; if TDS deductors have not reported, the TDS does not appear in Form 26AS even if you have Form 16A. Reconcile before filing to avoid 143(1) mismatch.</li>"
         "<li><strong>Mistaking 143(1) for scrutiny</strong> &mdash; 143(1) is automated. 143(2) is scrutiny with 6-month response window and specific document calls.</li>"
         "</ul>"
         "<p>Full ITR context: <a href=\"itr-filing-ay-2026-27-deadlines-changes-india.html\">ITR Filing AY 2026-27</a>. <em>Last updated: 2026-10-10.</em></p>"),
    ],
    faqs=[
        ("What is Section 143(1) intimation?",
         "Automated return-processing intimation from CPC Bengaluru showing one of three outcomes: refund due, demand payable, or nil (return accepted). Issued typically 60-90 days after ITR filing. Not scrutiny - just reconciliation of your return against TDS records and tax paid."),
        ("I received a 143(1) demand but I think it is wrong. What do I do?",
         "File Section 154 rectification online within 4 years from end of the FY in which the intimation was passed. Compare the Department's computation (right column) with your ITR (left column), identify the specific line of mismatch, attach supporting documents (Form 16, LIC receipt, PF statement, etc.), submit via incometax.gov.in. Response typically within 60-90 days."),
        ("Can I ignore a 143(1) demand?",
         "No. Interest under Section 220(2) at 1% per month accrues from the 31st day post-intimation. Even if you plan to rectify, respond or pay within 30 days. Ignoring compounds the penalty."),
        ("How long after ITR filing does 143(1) come?",
         "Typically 60-90 days after filing. Legally, CPC can issue within 9 months from the end of the FY in which the return is filed. If more than 9 months pass without a 143(1), the return is deemed accepted (no demand or refund action)."),
        ("What is the difference between Section 143(1) and 143(2)?",
         "143(1) is automated return-processing intimation - just reconciliation. 143(2) is scrutiny notice - the Department wants to examine your return in detail, request documents, and may add income or disallow deductions. 143(2) has specific 6-month response window and is much more serious."),
        ("Does BQP help with Section 143(1) rectification?",
         "Yes - common one-off engagement. We reconcile the Department computation vs your ITR, identify the mismatch line item, prepare the Section 154 filing with supporting documents, submit via portal, and track CPC response. WhatsApp +91 78018 87130."),
    ],
    related=[
        ("itr-filing-ay-2026-27-deadlines-changes-india.html", "Blog", "ITR AY 2026-27"),
        ("nri-taxation-india-complete-guide.html", "Guide", "NRI Taxation"),
    ],
    cta_headline="Received a 143(1) demand or confused by the intimation?",
    cta_body="Working-CA one-off engagement: reconcile the computation, identify the specific mismatch, file Section 154 rectification with supporting documents. Typical resolution: 60-90 days. WhatsApp Durgesh.",
))

# 2. Section 143(2) Scrutiny Notice Response
write_page("section-143-2-scrutiny-notice-response-india", page(
    slug="section-143-2-scrutiny-notice-response-india",
    title="Section 143(2) Scrutiny Notice Response 2026 | Documents, Timeline, CA Help - BQP",
    description="Section 143(2) scrutiny notice received: understand limited vs complete scrutiny, 6-month response window, documents to prepare, personal appearance protocol, Section 143(3) assessment order. Working CA guide by Durgesh Chavda.",
    keywords="Section 143(2) scrutiny notice, 143(2) response India, income tax scrutiny notice reply, Section 143(3) assessment, limited scrutiny vs complete scrutiny",
    hero_kicker="/ Blog &middot; Section 143(2) Scrutiny &middot; Updated 2026-10-10",
    hero_title_html="Section 143(2) scrutiny notice, <em>what to do in the first 48 hours.</em>",
    hero_lead="Section 143(2) is the Department's formal scrutiny notice. Unlike 143(1) which is automated reconciliation, 143(2) means an Assessing Officer wants to examine your return in detail, request documents, and may add income or disallow deductions. Response window: 6 months. Mistakes in the first 48 hours (ignoring, over-sharing, or responding without a CA) can turn a routine query into a tax demand. Here is the practitioner's playbook.",
    sections=[
        ("/ What triggers 143(2) scrutiny", "Who gets picked.",
         "<p>CPC Bengaluru uses algorithmic selection parameters to flag returns for scrutiny. Common triggers:</p>"
         "<ul>"
         "<li><strong>Large deductions / exemptions</strong> relative to total income &mdash; Section 80C maxed, HRA at ceiling, 80G claims, Section 54 property reinvestment.</li>"
         "<li><strong>Mismatch between ITR and Form 26AS / AIS</strong> &mdash; interest income not reported, TDS claimed higher than reported, capital-gains transactions not matching.</li>"
         "<li><strong>High-value transactions</strong> &mdash; cash deposits, property purchases, foreign remittances, mutual fund transactions above thresholds reported via SFT (Specified Financial Transactions).</li>"
         "<li><strong>Business income with low profit margin</strong> &mdash; turnover reported but net profit is suspiciously low.</li>"
         "<li><strong>Foreign assets / income</strong> &mdash; Schedule FA entries, foreign remittances, foreign bank accounts.</li>"
         "<li><strong>Random statistical selection</strong> &mdash; CBDT publishes annual scrutiny selection parameters; some returns are picked at random.</li>"
         "</ul>"
         "<p>Two types of scrutiny:</p>"
         "<ul>"
         "<li><strong>Limited scrutiny</strong> &mdash; AO examines specific issues flagged in the notice (e.g., only HRA, or only capital gains). Faster, narrower.</li>"
         "<li><strong>Complete scrutiny</strong> &mdash; AO examines the entire return. Longer, broader document calls.</li>"
         "</ul>"),
        ("/ Timeline + response window", "What the law says.",
         "<p><strong>Section 143(2) notice must be served</strong> within 3 months from the end of the FY in which the return was furnished.</p>"
         "<p><strong>Assessment under Section 143(3) completed</strong> within 12 months from the end of the FY in which the return was furnished (longer for complex / cross-border cases).</p>"
         "<p><strong>Response window after 143(2) notice</strong>: specified in the notice, typically 15-30 days for initial response. Additional document calls follow. The Department has discretion to extend the overall assessment timeline.</p>"
         "<p><strong>Faceless Assessment Scheme</strong>: since 2020, most individual scrutiny is conducted via the Faceless Assessment Scheme (National Faceless Assessment Centre, Delhi). All communication via e-filing portal; no physical appearance in most cases. The AO is not disclosed to the taxpayer.</p>"),
        ("/ First 48 hours after receiving 143(2)", "The response checklist.",
         "<ol>"
         "<li><strong>Do NOT ignore.</strong> Non-response is treated as acceptance of the Department's view; best-judgment assessment under Section 144 follows, typically unfavorable.</li>"
         "<li><strong>Read the notice carefully.</strong> Identify (a) notice type: limited or complete scrutiny, (b) specific issues flagged, (c) response deadline, (d) e-filing portal reference number.</li>"
         "<li><strong>Pull together initial documents</strong>: original ITR filing acknowledgement, Form 16, Form 26AS, Form AIS, bank statements for the AY, all deductions-supporting proofs.</li>"
         "<li><strong>Engage a CA before responding</strong>. The first response sets the tone of the proceeding. Over-sharing creates new areas of inquiry; under-sharing invites adverse inference.</li>"
         "<li><strong>Draft a measured first response</strong> addressing only the specific flagged issues (for limited scrutiny) with the exact documents requested. Do not volunteer additional information.</li>"
         "<li><strong>File the response via e-filing portal</strong> within the deadline (or request extension if genuinely needed; granted judiciously).</li>"
         "<li><strong>Prepare for follow-up queries</strong>. First response rarely closes the matter &mdash; AO typically asks 1-3 rounds of further queries.</li>"
         "</ol>"),
        ("/ Common scrutiny outcomes", "What AOs typically do.",
         "<p><strong>Accept the return as filed</strong> &mdash; happens in a meaningful minority of scrutiny cases where documentation is clean.</p>"
         "<p><strong>Minor additions</strong> &mdash; small disallowances of specific expenses, interest additions, small refunds reduced. Common and settled via acceptance.</p>"
         "<p><strong>Material additions</strong> &mdash; AO disallows large deductions, adds unreported income, imputes business profit margins. Resulting demand can be material. Response: appeal via CIT(A) within 30 days.</p>"
         "<p><strong>Section 68/69/69A additions</strong> &mdash; AO classifies unexplained cash, investment, or expenditure as income. These are harder to defend; strong documentation + logical commercial narrative essential.</p>"
         "<p><strong>Penalty under Section 270A</strong> &mdash; if AO concludes under-reporting (50% penalty) or misreporting (200% penalty). Appealable.</p>"),
        ("/ Appeals framework", "If assessment is adverse.",
         "<p>If the Section 143(3) order adds material income or imposes penalty, you have:</p>"
         "<ol>"
         "<li><strong>Rectification under Section 154</strong> if there is a mistake apparent from record. 4-year window.</li>"
         "<li><strong>Appeal to CIT(A) under Section 246A</strong> within 30 days of the order. First appellate level.</li>"
         "<li><strong>Appeal to ITAT (Tribunal) under Section 253</strong> if CIT(A) order unfavorable, within 60 days.</li>"
         "<li><strong>Appeal to High Court under Section 260A</strong> on substantial questions of law. Narrow scope.</li>"
         "</ol>"
         "<p>Each stage requires different legal support. BQP handles up to CIT(A); for ITAT and above, we co-ordinate with tax counsel. <em>Last updated: 2026-10-10.</em></p>"),
    ],
    faqs=[
        ("What is Section 143(2) notice?",
         "Formal scrutiny notice from the Assessing Officer under Income Tax Act. Means the Department wants to examine your return in detail - request documents, verify deductions, potentially add income. Different from Section 143(1) (automated reconciliation). Scrutiny response window typically 15-30 days initial; overall assessment completed within 12 months from end of FY of filing."),
        ("Can I handle Section 143(2) response myself without a CA?",
         "Technically yes. Practically risky. The first response sets the tone of the proceeding, and over-sharing or under-sharing can turn a routine query into a tax demand. Documents must be organised, computations defensible, and the AO's framing addressed precisely. Most taxpayers facing material-amount scrutiny engage a CA."),
        ("What is Faceless Assessment Scheme?",
         "Since 2020, most individual scrutiny is conducted via the Faceless Assessment Scheme - all communication through the e-filing portal; no physical appearance in most cases. The AO is not disclosed. A separate review unit, verification unit, and technical unit may be involved. The scheme aims to reduce discretion and corruption at the AO level."),
        ("What happens if I ignore a 143(2) notice?",
         "Non-response is treated as implicit acceptance of the Department's view. Best-judgment assessment under Section 144 follows - typically unfavorable, with maximum additions and penalties. Even if you cannot fully respond in time, filing an interim response acknowledging the notice and requesting extension is far better than silence."),
        ("How long does a Section 143(3) assessment take?",
         "By law, within 12 months from the end of the FY in which the return was furnished (longer for cross-border or transfer-pricing cases). In practice, limited scrutiny closes faster (3-6 months); complete scrutiny takes 6-12 months with 2-4 rounds of document calls."),
        ("Does BQP handle Section 143(2) scrutiny?",
         "Yes - response drafting, document pack preparation, follow-up query responses, appeal to CIT(A) if 143(3) order is adverse. For ITAT and above we co-ordinate with tax counsel. Standard engagement scoped per complexity. WhatsApp +91 78018 87130 or email durgesh@bharatquantumprospera.com."),
    ],
    related=[
        ("section-143-1-intimation-response-india-2026.html", "Blog", "Section 143(1) Response"),
        ("itr-filing-ay-2026-27-deadlines-changes-india.html", "Blog", "ITR AY 2026-27"),
    ],
    cta_headline="Scrutiny notice received? First 48 hours matter.",
    cta_body="Working-CA engagement: initial response drafting, document pack, follow-up query responses, CIT(A) appeal if 143(3) is adverse. The first response sets the tone - do not go in alone on a material scrutiny.",
))

# 3. Section 139(9) Defective Return
write_page("section-139-9-defective-return-response-india", page(
    slug="section-139-9-defective-return-response-india",
    title="Section 139(9) Defective Return Notice Response 2026 | 15-Day Fix - BQP",
    description="Section 139(9) defective return notice received: 15-day window to rectify, common defects (TDS mismatch, Schedule missing, wrong ITR form), rectification process via e-filing portal, consequence if ignored. Working CA guide by Durgesh Chavda.",
    keywords="Section 139(9) defective return, 139(9) response India, defective return notice reply, income tax defective return fix, how to respond to 139(9)",
    hero_kicker="/ Blog &middot; Section 139(9) Defective Return &middot; Updated 2026-10-10",
    hero_title_html="Section 139(9) defective return, <em>fix within 15 days.</em>",
    hero_lead="Section 139(9) notice means CPC Bengaluru found a defect in your ITR that must be rectified within 15 days. Common defects: wrong ITR form, Schedule missing, TDS mismatch, incomplete figures. If not rectified within 15 days (extendable to 30), the return is treated as invalid &mdash; and you may lose tax-paid credit, refund, or carry-forward of losses. Fast response matters.",
    sections=[
        ("/ What triggers 139(9) notice", "Common defects.",
         "<p>Common defects CPC flags:</p>"
         "<ul>"
         "<li><strong>Wrong ITR form</strong> &mdash; filed ITR-1 but had business income (needs ITR-3) or capital gains (needs ITR-2 or 3).</li>"
         "<li><strong>Schedule missing</strong> &mdash; Schedule CG for capital gains, Schedule FA for foreign assets, Schedule FSI for foreign source income, Schedule BP for business profits.</li>"
         "<li><strong>TDS mismatch</strong> &mdash; TDS claimed in ITR exceeds amount in Form 26AS by material margin.</li>"
         "<li><strong>Advance tax / self-assessment tax not reflected</strong> &mdash; Challan details missing from Form 26AS.</li>"
         "<li><strong>Mandatory field blank</strong> &mdash; email, address, bank details, PAN of deductor, etc.</li>"
         "<li><strong>Negative figure where not permitted</strong> &mdash; e.g., gross receipts cannot be negative.</li>"
         "<li><strong>Section 44AB (tax audit) applicable but no audit report filed</strong>.</li>"
         "<li><strong>Audit report not matched</strong> with the ITR filed.</li>"
         "</ul>"),
        ("/ The 15-day window", "What happens if you miss it.",
         "<p>Section 139(9) notice specifies a response deadline, typically 15 days from receipt. The AO can extend by up to 15 days on request.</p>"
         "<p><strong>If you rectify within 15 days (or extended period):</strong> the rectified return is treated as filed on the original filing date. All consequences (TDS credit, refund, carry-forward of losses) preserved.</p>"
         "<p><strong>If you do NOT rectify within the window:</strong> the original return is treated as invalid under Section 139(9). Consequences:</p>"
         "<ul>"
         "<li>You lose the right to claim refund if any.</li>"
         "<li>Losses that could have been carried forward are lost.</li>"
         "<li>You must file a belated return under Section 139(4) if still possible (available only until 31 December of the AY).</li>"
         "<li>Section 234F late-filing fee applies.</li>"
         "<li>Section 234A interest on unpaid tax from the original due date.</li>"
         "</ul>"
         "<p>Treat 15 days as a hard deadline.</p>"),
        ("/ How to rectify", "Step-by-step.",
         "<ol>"
         "<li><strong>Log in to incometax.gov.in</strong> with your PAN credentials.</li>"
         "<li><strong>Pending Actions &rarr; e-Proceedings</strong> or <strong>Pending Actions &rarr; Response to Outstanding Demand</strong>. The 139(9) notice appears here.</li>"
         "<li><strong>Read the notice.</strong> Identify the specific defect (notice body lists it).</li>"
         "<li><strong>Decide response path:</strong></li>"
         "<li>&nbsp;&nbsp;a. <strong>Agree &mdash; file revised return</strong>: prepare a corrected ITR fixing the defect (right form, missing schedule, correct TDS). File as 'Revised Return' with the Section 139(9) acknowledgement number. Submit via e-filing.</li>"
         "<li>&nbsp;&nbsp;b. <strong>Disagree &mdash; explain to the AO</strong>: if you believe no defect exists, submit a written response via the portal explaining why. Rare but possible when CPC's automated check misread something.</li>"
         "<li><strong>If filing revised return</strong>: ensure the revised return reflects everything correctly &mdash; wrong fixing of defect can trigger another 139(9).</li>"
         "<li><strong>Save the submission acknowledgement</strong>.</li>"
         "<li><strong>Follow up</strong> via e-filing portal after 30-45 days to confirm the revised return has been accepted and processed under 143(1).</li>"
         "</ol>"),
        ("/ Common mistakes in 139(9) response", "What we see.",
         "<ul>"
         "<li><strong>Not reading the notice carefully</strong> &mdash; and fixing the wrong thing. CPC flags a specific defect; address that specific defect, not a general refile.</li>"
         "<li><strong>Filing original ITR again instead of revised</strong> &mdash; this does not satisfy 139(9). The response must be marked as revised return with the 139(9) acknowledgement.</li>"
         "<li><strong>Missing the 15-day window</strong> &mdash; most costly mistake. Even if you cannot fully respond in 15 days, file a provisional response acknowledging the notice and requesting extension.</li>"
         "<li><strong>Not updating Form 26AS first</strong> if the defect is TDS mismatch. If you file revised return before 26AS is updated by the deductor, you will get another 139(9).</li>"
         "<li><strong>Over-fixing</strong> &mdash; changing fields the defect notice did not flag. This can trigger new scrutiny inquiries.</li>"
         "</ul>"
         "<p><em>Last updated: 2026-10-10.</em></p>"),
    ],
    faqs=[
        ("What is Section 139(9)?",
         "Defective return notice from CPC Bengaluru. Means your ITR has a defect that must be rectified within 15 days (extendable to 30 by AO). Common defects: wrong ITR form, missing schedule, TDS mismatch, incomplete fields, Section 44AB audit report mismatch."),
        ("What happens if I don't respond to 139(9) in 15 days?",
         "Original return is treated as INVALID under Section 139(9). Consequences: lose right to claim refund, lose carry-forward of losses, must file belated return under Section 139(4) if still eligible (until 31 December of AY), Section 234F late-filing fee + Section 234A interest apply. Treat 15 days as a hard deadline."),
        ("Can I extend the 15-day deadline?",
         "Yes - AO can extend by up to 15 days on written request made before the original deadline expires. Request via e-filing portal with specific reason. Grants typically depend on validity of reason. Do not assume grant; file within original window where possible."),
        ("How do I rectify a 139(9) defective return?",
         "Log in to incometax.gov.in → Pending Actions → e-Proceedings. Read the notice to identify the specific defect. Prepare a REVISED return fixing that specific defect (right ITR form, missing schedule, correct TDS). File as 'Revised Return' with the 139(9) acknowledgement number. Save submission acknowledgement. Follow up after 30-45 days."),
        ("Can I file the same original ITR again?",
         "No. The response must be a REVISED return marked specifically with the 139(9) acknowledgement number. Just re-filing the original ITR without changes will not satisfy 139(9) and will likely trigger another defective return notice."),
        ("Does BQP help with Section 139(9) response?",
         "Yes - common urgent engagement given the 15-day deadline. We analyze the specific defect, prepare the correct revised ITR, file via portal within the window, track CPC confirmation. Typical turnaround 2-5 business days. WhatsApp +91 78018 87130."),
    ],
    related=[
        ("section-143-1-intimation-response-india-2026.html", "Blog", "Section 143(1) Response"),
        ("itr-filing-ay-2026-27-deadlines-changes-india.html", "Blog", "ITR AY 2026-27"),
    ],
    cta_headline="139(9) notice received? 15-day window is tight.",
    cta_body="Working-CA urgent engagement: analyze the specific defect, prepare revised ITR, file via portal within the window. Typical turnaround 2-5 business days. WhatsApp Durgesh now.",
))

# 4. GST Notice Response
write_page("gst-notice-response-india-asmt-drc-gstr", page(
    slug="gst-notice-response-india-asmt-drc-gstr",
    title="GST Notice Response India 2026 | ASMT, DRC, GSTR Mismatch - BQP",
    description="GST notice received: ASMT-10 (discrepancy), DRC-01 / DRC-01A (SCN with proposed demand), GSTR-2A/2B vs GSTR-3B mismatch, Section 73 vs 74 notices. Response timelines, documents, GSTR-9 reconciliation. Working CA guide by Durgesh Chavda.",
    keywords="GST notice response India, ASMT-10 notice reply, DRC-01 notice response, GSTR-3B vs 2A mismatch, Section 73 GST notice, Section 74 GST notice, GST SCN response",
    hero_kicker="/ Blog &middot; GST Notice Response &middot; Updated 2026-10-10",
    hero_title_html="GST notice received, <em>which form and what to do.</em>",
    hero_lead="GST notices in India come in multiple forms &mdash; ASMT-10, DRC-01, DRC-01A, GSTR-3A, mismatch alerts &mdash; each with different response windows and consequences. Non-response or wrong response can convert a routine query into a tax demand plus 100% penalty. Here is the practitioner's response map.",
    sections=[
        ("/ Common GST notice types + response window", "The map.",
         "<p><strong>ASMT-10 (Notice of Discrepancy):</strong> issued by proper officer under Section 61 if return filed differs from information available. Response window: typically 30 days. Response via ASMT-11. Non-response: officer proceeds with audit under Section 65 or scrutiny.</p>"
         "<p><strong>DRC-01A (Pre-SCN Intimation):</strong> issued under Section 73(5) or 74(5) before formal SCN. Specifies proposed demand + reasons. Response window: typically 15 days. Response via DRC-03 (paying tax + interest voluntarily to close) or DRC-06 (contesting). Advantage of DRC-03: reduced penalty if voluntarily paid before SCN.</p>"
         "<p><strong>DRC-01 (Show Cause Notice under Section 73/74):</strong> formal SCN proposing tax demand. Section 73 (bona fide errors): penalty 10% or INR 10,000 whichever higher; 3-year time limit. Section 74 (fraud / wilful misstatement): penalty 100%; 5-year time limit. Response window: typically 30 days. Response via DRC-06.</p>"
         "<p><strong>GSTR-3A (Notice for Non-filing of Return):</strong> issued to taxpayer who has not filed GSTR-3B / GSTR-1 for one or more months. Response: file pending returns within 15 days or face Section 62 best-judgment assessment.</p>"
         "<p><strong>GSTR-2A / 2B vs GSTR-3B mismatch alerts:</strong> auto-generated by portal when ITC claimed in 3B exceeds reconciled 2B figures. Response: reconcile vendor-wise, chase vendors for missing invoices, reverse ineligible ITC.</p>"
         "<p><strong>Audit notice under Section 65 (ADT-01):</strong> formal audit of records. Response: provide records; audit completed within 3 months (extendable to 6).</p>"),
        ("/ GSTR-2A / 2B vs GSTR-3B mismatch", "The most common GST headache.",
         "<p>Mechanism: ITC can be claimed in GSTR-3B only if the vendor has filed GSTR-1 showing the supply to you. GSTR-2A (dynamic) and GSTR-2B (static month-close snapshot) reflect what vendors have reported.</p>"
         "<p>Mismatch types:</p>"
         "<ul>"
         "<li><strong>Vendor has not filed GSTR-1</strong> &mdash; invoice does not appear in your 2B. Your 3B ITC is excess vs 2B. Portal flags mismatch.</li>"
         "<li><strong>Vendor filed GSTR-1 but with wrong GSTIN</strong> &mdash; invoice shows against someone else.</li>"
         "<li><strong>Vendor filed GSTR-1 but delayed</strong> &mdash; invoice appears in a later month's 2B than when you claimed ITC.</li>"
         "<li><strong>You claimed ITC on exempt / blocked supplies</strong> &mdash; e.g., personal use, Section 17(5) blocks (motor vehicles, construction materials for own buildings).</li>"
         "</ul>"
         "<p>Response path:</p>"
         "<ol>"
         "<li>Download GSTR-2B for the mismatch period. Match line-by-line with your purchase register.</li>"
         "<li>Identify vendors who have not reported. Chase for GSTR-1 filing.</li>"
         "<li>If vendor is unresponsive, reverse the ITC in next GSTR-3B (reversal with interest under Section 50).</li>"
         "<li>If ITC was wrongly claimed on blocked / exempt supplies, reverse via GSTR-3B Table 4(B).</li>"
         "<li>If mismatch is timing (vendor filed in later month), no action needed &mdash; ITC will match in the later period.</li>"
         "<li>Document the reconciliation in GSTR-9 annual return.</li>"
         "</ol>"),
        ("/ Section 73 vs Section 74", "The crucial distinction.",
         "<p><strong>Section 73</strong>: applies to bona fide errors, oversight, interpretation differences. No fraud alleged.</p>"
         "<ul>"
         "<li>Time limit: SCN within 3 years of due date of annual return (so for FY 2024-25, within 31 December 2028).</li>"
         "<li>Penalty: 10% of tax or INR 10,000, whichever higher.</li>"
         "<li>Voluntary payment via DRC-03 before SCN: nil penalty.</li>"
         "<li>Payment within 30 days of SCN: no penalty (interest only).</li>"
         "</ul>"
         "<p><strong>Section 74</strong>: applies to fraud, wilful misstatement, suppression of facts.</p>"
         "<ul>"
         "<li>Time limit: SCN within 5 years of due date of annual return.</li>"
         "<li>Penalty: 100% of tax.</li>"
         "<li>Voluntary payment via DRC-03 before SCN: 15% penalty.</li>"
         "<li>Payment within 30 days of SCN: 25% penalty.</li>"
         "<li>Beyond 30 days: full 100% penalty.</li>"
         "</ul>"
         "<p>Section 73 vs 74 classification is often the key battle. Convert a 74 to 73 and penalty drops from 100% to 10%. Response strategy focuses on establishing bona fide error (interpretation, no suppression) and challenging the fraud allegation.</p>"),
        ("/ Response workflow", "Standard engagement.",
         "<ol>"
         "<li><strong>Read the notice carefully</strong>: identify form (ASMT, DRC-01A, DRC-01), the specific issue, response window, proposed demand amount, Section 73 or 74.</li>"
         "<li><strong>Pull GST records</strong>: GSTR-1 filed, GSTR-3B filed, GSTR-2A / 2B for the period, purchase register, sales register, GSTR-9 annual return.</li>"
         "<li><strong>Analyze the discrepancy</strong>: identify where the Department's view differs from yours.</li>"
         "<li><strong>Decide response strategy</strong>: pay-and-close (via DRC-03) if demand is correct, or contest (via DRC-06) with documents.</li>"
         "<li><strong>Draft response</strong> addressing each issue in the notice with supporting evidence.</li>"
         "<li><strong>File response via GST portal</strong> within the deadline.</li>"
         "<li><strong>Attend personal hearing</strong> if called (physical or virtual depending on jurisdiction).</li>"
         "<li><strong>Appeal to CGST Appellate Authority</strong> within 3 months if adjudication order is adverse.</li>"
         "</ol>"
         "<p><em>Last updated: 2026-10-10.</em></p>"),
    ],
    faqs=[
        ("What is ASMT-10 notice?",
         "Notice of discrepancy under Section 61 issued by proper officer when return filed shows discrepancies with information available (e.g., GSTR-3B vs 2B mismatch, turnover mismatch with e-way bill). Response window typically 30 days via ASMT-11. Non-response can lead to audit under Section 65."),
        ("What is DRC-01 notice?",
         "Formal Show Cause Notice (SCN) under Section 73 or 74 of CGST Act proposing a tax demand. Section 73 = bona fide error (10% penalty); Section 74 = fraud / wilful misstatement (100% penalty). Response window typically 30 days via DRC-06. The Section 73 vs 74 classification is often the key battleground."),
        ("What is the GSTR-2A / 2B vs 3B mismatch problem?",
         "ITC claimed in GSTR-3B must match ITC reported by your vendors in their GSTR-1 (reflected in your 2B). When vendors do not file GSTR-1 timely or you claim ITC on blocked/exempt supplies, the mismatch triggers portal alerts. Response: reconcile vendor-wise, chase vendor filings, reverse ineligible ITC with interest under Section 50."),
        ("Can I voluntarily pay to close a GST notice?",
         "Yes via DRC-03. For Section 73 notices: voluntary payment before SCN = nil penalty. For Section 74 notices: voluntary payment before SCN = 15% penalty (vs 100% at full adjudication). DRC-03 is often strategically used to close small or clearly-correct demands at reduced penalty."),
        ("What is the time limit for GST notices?",
         "Section 73 SCN: within 3 years of the due date of the annual return (GSTR-9) for the relevant period. Section 74 SCN: within 5 years. For FY 2024-25, GSTR-9 due date is 31 December 2025, so Section 73 limitation runs until 31 December 2028 and Section 74 until 31 December 2030."),
        ("Does BQP handle GST notice responses?",
         "Yes - ASMT-10 reconciliation, DRC-01A pre-SCN response, DRC-01 SCN defence, GSTR-2A/2B/3B mismatch cleanup, Section 65 audit co-ordination, Section 73/74 classification challenges, CGST Appellate Authority appeals. WhatsApp +91 78018 87130 or email durgesh@bharatquantumprospera.com."),
    ],
    related=[
        ("itr-filing-ay-2026-27-deadlines-changes-india.html", "Blog", "ITR AY 2026-27"),
        ("section-143-2-scrutiny-notice-response-india.html", "Blog", "Section 143(2) Scrutiny"),
    ],
    cta_headline="GST notice received? Form matters, time matters.",
    cta_body="Working-CA engagement: identify form (ASMT / DRC-01A / DRC-01), analyze the specific issue, decide pay-and-close vs contest strategy, file response within deadline. For Section 74 notices, converting to Section 73 can drop penalty from 100% to 10%.",
))

# 5. Freelancer Consultant Tax India
write_page("freelancer-consultant-tax-india-2026-complete", page(
    slug="freelancer-consultant-tax-india-2026-complete",
    title="Freelancer / Consultant Tax India 2026 | Upwork, Fiverr, Toptal, Direct Clients - BQP",
    description="Freelancer / consultant tax in India 2026: Section 44ADA presumptive scheme (50% deemed profit), ITR-4 vs ITR-3, GST registration threshold, foreign client income + GST LUT, Section 80C + 80D deductions. Working CA guide by Durgesh Chavda.",
    keywords="freelancer tax India 2026, consultant tax India, Upwork tax India, Fiverr tax India, Section 44ADA presumptive, freelancer GST India, foreign income freelancer tax",
    hero_kicker="/ Blog &middot; Freelancer / Consultant Tax &middot; Updated 2026-10-10",
    hero_title_html="Freelancer tax India 2026, <em>the practitioner's playbook.</em>",
    hero_lead="Indian freelancers and consultants &mdash; software developers, designers, writers, marketing consultants, translators, YouTubers, Instagram influencers &mdash; face a specific tax regime: Section 44ADA presumptive taxation, GST threshold at INR 20 lakh, special rules for foreign-client income (LUT bond), and the choice between ITR-3 and ITR-4. This is the complete working guide for FY 2025-26 / AY 2026-27.",
    sections=[
        ("/ Section 44ADA - the presumptive scheme", "Half your income is deemed profit.",
         "<p>Section 44ADA is the game-changer for Indian freelancers and consultants. Available to:</p>"
         "<ul>"
         "<li>Resident Individuals and HUFs.</li>"
         "<li>Professions specified: legal, medical, engineering, architectural, accountancy, technical consultancy, interior decoration, authorized representative, film artist, company secretary, information technology.</li>"
         "<li>Annual gross receipts up to INR 75 lakh (raised from INR 50 lakh via Finance Act 2023).</li>"
         "</ul>"
         "<p><strong>Deemed profit:</strong> 50% of gross receipts. You pay tax on 50% of what you invoice, regardless of actual expenses. No need to maintain books of accounts or get them audited.</p>"
         "<p><strong>Example:</strong> freelance software developer invoices INR 60 lakh in FY 2025-26.</p>"
         "<ul>"
         "<li>Deemed profit: INR 30 lakh (50% of INR 60 lakh).</li>"
         "<li>Tax on INR 30 lakh under new regime (default): slab calculation applies.</li>"
         "<li>No audit required (even though gross receipts are above INR 50 lakh professional threshold).</li>"
         "<li>No books of accounts required.</li>"
         "</ul>"
         "<p><strong>When to NOT use 44ADA:</strong></p>"
         "<ul>"
         "<li>Actual expenses exceed 50% of gross receipts (large office rent, employees, equipment). Then regular Section 28/29 business income computation wins.</li>"
         "<li>Gross receipts exceed INR 75 lakh. Then standard business income rules apply with Section 44AB audit if above threshold.</li>"
         "<li>You want to carry forward business losses. 44ADA does not allow loss setoff.</li>"
         "</ul>"),
        ("/ ITR-4 vs ITR-3", "Which form to file.",
         "<p><strong>ITR-4 (Sugam):</strong> for taxpayers using Section 44AD / 44ADA / 44AE presumptive schemes. Simplified return. Preferred form for 44ADA freelancers.</p>"
         "<p><strong>ITR-3:</strong> for taxpayers with business or professional income NOT using presumptive scheme, or where presumptive opt-out triggers audit. Full business income schedule required.</p>"
         "<p><strong>Switching between 44ADA and regular</strong>: Section 44ADA has a lock-in &mdash; if you opt out in any year, you cannot opt back in for the next 5 years. Think carefully before switching.</p>"
         "<p><strong>Due date:</strong></p>"
         "<ul>"
         "<li>ITR-4 (non-audit): 31 July 2026 for AY 2026-27.</li>"
         "<li>ITR-3 (audit case): 31 October 2026.</li>"
         "<li>Belated: 31 December 2026 with Section 234F fee.</li>"
         "</ul>"),
        ("/ GST registration for freelancers", "The thresholds.",
         "<p><strong>GST registration mandatory when:</strong></p>"
         "<ul>"
         "<li>Aggregate turnover in a financial year exceeds <strong>INR 20 lakh</strong> for services (INR 10 lakh in special category states: Mizoram, Tripura, Manipur, Nagaland).</li>"
         "<li>Inter-state supply of services (regardless of turnover).</li>"
         "<li>E-commerce operator (Fiverr, Upwork via platform payment).</li>"
         "</ul>"
         "<p><strong>Freelancer GST compliance:</strong></p>"
         "<ul>"
         "<li>18% GST on most freelance services (lower for specific categories).</li>"
         "<li>GSTR-1 (sales) monthly or quarterly.</li>"
         "<li>GSTR-3B (summary + tax payment) monthly or quarterly.</li>"
         "<li>GSTR-9 (annual) if turnover above INR 2 crore.</li>"
         "<li>Services to foreign clients: Export of Services, GST zero-rated under Section 16 of IGST Act. Options: (a) Pay GST and claim refund, or (b) Supply under LUT (Letter of Undertaking) bond without paying GST.</li>"
         "</ul>"
         "<p><strong>LUT bond:</strong> annual filing on GST portal (Form GST RFD-11). Enables tax-free export of services. Must be filed before 31 March each year for the next FY.</p>"),
        ("/ Foreign client income - the specific setup", "Upwork, Fiverr, Toptal, direct clients abroad.",
         "<p>For Indian freelancer invoicing foreign clients:</p>"
         "<ul>"
         "<li><strong>Income tax</strong>: fully taxable in India as business/professional income. Section 44ADA (50% deemed profit) applies if under INR 75 lakh.</li>"
         "<li><strong>GST</strong>: export of services, zero-rated. File LUT bond to avoid paying GST + claiming refund.</li>"
         "<li><strong>FEMA</strong>: receipts must come through authorised dealer bank (any scheduled bank's forex account). Not through PayPal consumer or crypto. Allowed channels: direct wire transfer, Wise Business, Payoneer (with FIRC generation), Stripe (if your business is incorporated).</li>"
         "<li><strong>FIRC (Foreign Inward Remittance Certificate)</strong>: proof of foreign-currency receipt. Required for GST LUT compliance and ITR disclosure.</li>"
         "<li><strong>Platform-specific</strong>:</li>"
         "<li>&nbsp;&nbsp;- <strong>Upwork</strong>: direct bank transfer or Payoneer; FIRC available.</li>"
         "<li>&nbsp;&nbsp;- <strong>Fiverr</strong>: Payoneer, direct bank transfer, PayPal (business). FIRC via Payoneer.</li>"
         "<li>&nbsp;&nbsp;- <strong>Toptal</strong>: direct wire transfer; FIRC available.</li>"
         "<li>&nbsp;&nbsp;- <strong>Direct clients (contracts you negotiate)</strong>: typically direct wire or Wise Business.</li>"
         "</ul>"
         "<p><strong>Common foreign-client income mistake</strong>: receiving via PayPal consumer account (not business) or Western Union &mdash; these are not GST / FEMA compliant channels. Switch to bank wire / Wise Business / Payoneer business for compliance.</p>"),
        ("/ Deductions available to freelancers", "Under old regime (not new default).",
         "<p>Under the OLD regime (requires explicit election via Form 10IEA, due by ITR filing deadline):</p>"
         "<ul>"
         "<li><strong>Section 80C</strong>: INR 1.5 lakh (LIC, ELSS, PPF, NSC, 5-year FD, PF).</li>"
         "<li><strong>Section 80CCD(1B)</strong>: additional INR 50,000 for NPS Tier 1 contributions.</li>"
         "<li><strong>Section 80D</strong>: INR 25,000 for health insurance (INR 50,000 if senior citizen parents).</li>"
         "<li><strong>Section 80E</strong>: full education loan interest deduction.</li>"
         "<li><strong>Section 80G</strong>: donations.</li>"
         "<li><strong>Section 24(b)</strong>: INR 2 lakh home loan interest (if own-use property).</li>"
         "<li><strong>HRA</strong>: if you pay rent (even to parents with proper paperwork). Freelancers can claim HRA only under Section 10(13A) if receiving HRA as part of salary &mdash; most freelancers claim under Section 80GG instead (up to INR 60,000/year or 25% of total income, whichever lower).</li>"
         "</ul>"
         "<p>Under NEW regime (default FY 2024-25 onwards): only standard deduction (INR 75,000 if salaried; freelancers get Section 44ADA 50% deemed deduction instead) + NPS employer contribution. No Section 80C etc.</p>"
         "<p>For most freelancers with large 80C + 80D + home loan interest, OLD regime wins. Use our calculator: <a href=\"new-vs-old-tax-regime-calculator.html\">New vs Old Regime Calculator</a>.</p>"
         "<p><em>Last updated: 2026-10-10.</em></p>"),
    ],
    faqs=[
        ("Is Section 44ADA presumptive scheme good for freelancers?",
         "Usually yes if actual expenses are below 50% of gross receipts. Pay tax on 50% of gross receipts regardless of actual expenses, no books of accounts, no audit. Available for specified professions (legal, medical, engineering, accountancy, IT consultancy, etc.) up to INR 75 lakh annual gross receipts. 5-year lock-in once opted out."),
        ("Do I need GST registration as a freelancer?",
         "Mandatory if aggregate annual turnover exceeds INR 20 lakh for services (INR 10 lakh in special category states), or if you supply inter-state services (regardless of turnover), or if you use an e-commerce platform (Fiverr, Upwork). Below the threshold with intra-state only: voluntary registration available."),
        ("Which ITR form should a freelancer file?",
         "ITR-4 if using Section 44ADA presumptive (most common choice). ITR-3 if not using presumptive scheme or if presumptive opt-out triggers tax audit. ITR-1 is NOT applicable for business/professional income."),
        ("How do I handle foreign client income from Upwork / Fiverr?",
         "Income tax: fully taxable in India under Section 44ADA presumptive. GST: export of services, zero-rated, file LUT bond annually (Form GST RFD-11) to avoid paying GST on exports. FEMA: receive via authorised dealer bank (direct wire, Wise Business, Payoneer business). Obtain FIRC for each inward remittance."),
        ("Can freelancers claim home office expenses?",
         "Under Section 44ADA (presumptive), expenses are deemed - cannot claim additional. Under regular business computation (not using 44ADA), yes - home office rent, electricity, internet, equipment depreciation can be claimed under Section 37. Books of accounts required."),
        ("Does BQP handle freelancer tax filings?",
         "Yes - annual ITR filing (ITR-4 for 44ADA, ITR-3 for regular), GST registration + monthly / quarterly filings, LUT bond filing, FIRC co-ordination, foreign client contract review. Specific plans for Upwork / Fiverr / Toptal freelancers and direct-client consultants. WhatsApp +91 78018 87130."),
    ],
    related=[
        ("itr-filing-ay-2026-27-deadlines-changes-india.html", "Blog", "ITR AY 2026-27"),
        ("new-vs-old-tax-regime-calculator.html", "Tool", "New vs Old Regime Calculator"),
    ],
    cta_headline="Indian freelancer with multi-platform income + foreign clients?",
    cta_body="Section 44ADA + GST LUT + FEMA FIRC setup = clean compliance stack. Annual ITR-4 + GST filings + LUT renewal under one engagement. Standard freelancer package scoped per receipt profile.",
))

# 6. YouTube / Instagram Influencer Tax
write_page("youtube-instagram-influencer-tax-india-2026", page(
    slug="youtube-instagram-influencer-tax-india-2026",
    title="YouTube / Instagram Influencer Tax India 2026 | AdSense, Brand Deals, Gifts - BQP",
    description="Content creator / influencer tax India 2026: YouTube AdSense income, Instagram brand deals, Section 194R TDS on free products, GST 18% on brand collaborations, Section 44ADA for creators, foreign-client AdSense income + LUT. CA Durgesh Chavda guide.",
    keywords="YouTube tax India 2026, Instagram influencer tax India, content creator tax India, AdSense income tax India, brand collaboration GST, Section 194R influencer",
    hero_kicker="/ Blog &middot; Content Creator Tax &middot; Updated 2026-10-10",
    hero_title_html="YouTube / Instagram influencer tax, <em>complete India 2026 framework.</em>",
    hero_lead="Indian content creators &mdash; YouTubers, Instagram influencers, podcasters, TikTok (now Lemon8), newsletter writers &mdash; have specific tax exposure: AdSense income from Google (foreign source), Indian brand deal GST at 18%, Section 194R TDS on free products from brands, FEMA for foreign-currency receipts, and the Section 44ADA 50% presumptive option. This is the practitioner's complete map for FY 2025-26.",
    sections=[
        ("/ Income sources + tax treatment", "What creators actually earn.",
         "<p><strong>1. YouTube AdSense revenue</strong> &mdash; Google pays Indian creators from Singapore / US. Treatment:</p>"
         "<ul>"
         "<li>Business/professional income under head 'Profits and Gains of Business or Profession'.</li>"
         "<li>Section 44ADA presumptive: if creator qualifies as 'profession' (treated as creative professional) &mdash; 50% deemed profit if annual receipts under INR 75 lakh.</li>"
         "<li>FEMA: receive via authorised dealer bank with FIRC.</li>"
         "<li>GST: export of services, zero-rated. File LUT bond annually.</li>"
         "</ul>"
         "<p><strong>2. Instagram / YouTube brand deals</strong> &mdash; Indian brands paying for sponsored posts, Reels, videos:</p>"
         "<ul>"
         "<li>Business income. Taxable at slab rate (or 50% under 44ADA).</li>"
         "<li>GST 18% on brand collaboration fee. Mandatory registration if annual turnover exceeds INR 20 lakh.</li>"
         "<li>Section 194R TDS by brand at 10% if non-cash perquisite + cash together exceed INR 20K per year per influencer.</li>"
         "<li>Section 194C TDS by brand at 1% on cash fee (contract-based deal).</li>"
         "</ul>"
         "<p><strong>3. Free products from brands (unboxing, review deals)</strong> &mdash; this is where creators get caught:</p>"
         "<ul>"
         "<li>Free product provided in exchange for a review / mention is a <strong>business perquisite under Section 17(2)(vi)</strong> read with Section 28(iv).</li>"
         "<li>Taxable at the FMV of the product in the creator's hands.</li>"
         "<li>Brand must deduct TDS at 10% under Section 194R if aggregate value exceeds INR 20K per year per creator.</li>"
         "<li>Creator declares this as business income on ITR.</li>"
         "</ul>"
         "<p><strong>4. Affiliate commissions</strong> (Amazon Associates, platform referrals) &mdash; business income; GST at 18% if above threshold; Section 194H TDS if above INR 15K / year.</p>"
         "<p><strong>5. Platform tips / Super Chats / YouTube Memberships / Patreon</strong> &mdash; business income; FEMA via authorised dealer bank if foreign; GST export of services if foreign-origin.</p>"
         "<p><strong>6. Merchandise / courses / newsletter subscriptions</strong> &mdash; business income; GST 18% on domestic; export zero-rated.</p>"),
        ("/ Section 194R - the brand perquisite TDS", "Covered specifically for creators.",
         "<p>CBDT Circular 12 of 2022 specifically clarified that free product samples given to social media influencers in exchange for reviews / content are perquisites under Section 194R.</p>"
         "<p><strong>Mechanics:</strong></p>"
         "<ul>"
         "<li>Brand provides free product to influencer worth, say, INR 50,000.</li>"
         "<li>Brand deducts 10% TDS = INR 5,000. Since the brand cannot deduct from a non-cash perquisite, either (a) influencer deposits INR 5,000 cash with brand, or (b) brand grosses up (treats the perquisite as INR 55,555, after 10% TDS = INR 50,000 net value).</li>"
         "<li>Brand deposits INR 5,000 with government, issues Form 16A to influencer.</li>"
         "<li>Influencer declares INR 50,000 as business income (or INR 55,555 if grossed up), claims INR 5,000 TDS credit on ITR.</li>"
         "</ul>"
         "<p>Full Section 194R guide: <a href=\"section-194r-tds-business-perquisites-india.html\">Section 194R TDS on Business Perquisites</a>.</p>"),
        ("/ Section 44ADA for creators", "Does it apply?",
         "<p>Section 44ADA applies to specified professions including 'authorized representative' and 'company secretary' and historical practice extends to creative professionals (film artist is specifically listed; by analogy content creators have been treated as creative professionals in multiple ITAT decisions).</p>"
         "<p>For creators under INR 75 lakh annual receipts:</p>"
         "<ul>"
         "<li>Opt for 44ADA presumptive: pay tax on 50% of gross receipts.</li>"
         "<li>No books of accounts required.</li>"
         "<li>No tax audit required (even if receipts exceed INR 50 lakh since 44ADA ceiling is INR 75 lakh for professions).</li>"
         "<li>Simple ITR-4 filing.</li>"
         "</ul>"
         "<p>For creators above INR 75 lakh: regular business income computation (ITR-3) with books of accounts, Section 44AB audit mandatory if turnover > INR 1 crore (or INR 10 crore under cash-receipts carve-out).</p>"
         "<p>For creators receiving large free-product value making actual-expense deduction attractive: standard business income computation may win over 44ADA.</p>"),
        ("/ GST + LUT bond for creator exports", "The specific setup.",
         "<p>Services to foreign brands + YouTube AdSense + Patreon / Substack international subscribers all qualify as <strong>Export of Services</strong> under IGST Section 2(6):</p>"
         "<ul>"
         "<li>Supplier (creator) in India.</li>"
         "<li>Recipient outside India.</li>"
         "<li>Place of supply outside India.</li>"
         "<li>Payment in convertible foreign exchange.</li>"
         "<li>Supplier and recipient are not merely establishments of same person.</li>"
         "</ul>"
         "<p>Export is <strong>zero-rated</strong> under IGST Section 16. Two routes:</p>"
         "<ul>"
         "<li>(a) <strong>Pay GST and claim refund</strong> &mdash; working capital drag.</li>"
         "<li>(b) <strong>Supply under LUT bond without paying GST</strong> &mdash; preferred by creators. Annual filing of Form GST RFD-11 before 31 March for next FY.</li>"
         "</ul>"
         "<p>LUT bond is a one-page electronic filing. Simple to execute, significant working-capital advantage.</p>"),
        ("/ FEMA + FIRC for creator foreign income", "Compliance basics.",
         "<p>Creator foreign income (AdSense, Patreon, international brand deals, Substack / Beehiiv / newsletter paid subscriptions) must flow through FEMA-compliant channels:</p>"
         "<ul>"
         "<li><strong>Direct wire to Indian bank account</strong>: standard channel. Bank issues FIRC on request.</li>"
         "<li><strong>Wise Business / Payoneer business account</strong>: supported. FIRC generation available (verify your account type).</li>"
         "<li><strong>Stripe Atlas / Delaware entity</strong>: if the creator has incorporated abroad (Delaware LLC or C-Corp) and uses Stripe, Stripe pays the US entity. The creator then transfers to India via FEMA ODI dividend / salary. See <a href=\"us-incorporation.html\">US Incorporation</a> for the structure.</li>"
         "<li><strong>PayPal consumer account</strong>: NOT FEMA-compliant for business income. Switch to PayPal Business.</li>"
         "<li><strong>Crypto / stablecoin</strong>: NOT FEMA-compliant for business receipts. Avoid.</li>"
         "</ul>"
         "<p>FIRC (Foreign Inward Remittance Certificate) is proof of foreign-currency receipt. Required for GST LUT compliance (demonstrating export) and ITR disclosure. Retain for 6 years.</p>"
         "<p><em>Last updated: 2026-10-10.</em></p>"),
    ],
    faqs=[
        ("Is YouTube AdSense income taxable in India?",
         "Yes. Fully taxable as business/professional income. Section 44ADA 50% presumptive scheme available if annual receipts under INR 75 lakh. GST: export of services, zero-rated with LUT bond. FEMA: receive via authorised dealer bank with FIRC. Google AdSense pays from Singapore or US entity depending on your region."),
        ("Do Instagram influencers need GST registration?",
         "Mandatory if aggregate annual turnover (brand deals + affiliate + sponsorships + products / courses) exceeds INR 20 lakh. 18% GST on domestic brand collaborations. Export (foreign brand) is zero-rated with LUT bond. Inter-state service supply triggers registration regardless of turnover."),
        ("Is a free product from a brand taxable for influencers?",
         "Yes. Section 17(2)(vi) read with Section 28(iv) + Section 194R. Brand deducts 10% TDS on FMV of the product if aggregate value exceeds INR 20K per year per influencer. Influencer declares the FMV as business income on ITR and claims the TDS credit. CBDT Circular 12 of 2022 specifically covers influencer samples."),
        ("Can YouTubers use Section 44ADA?",
         "Yes - creators are generally treated as creative professionals and 44ADA extends to them. 50% deemed profit if annual receipts under INR 75 lakh. No books of accounts, no tax audit, ITR-4 filing. For creators above INR 75 lakh or with heavy actual expenses, regular business computation (ITR-3) may be preferred."),
        ("How do I set up LUT bond for YouTube AdSense GST?",
         "Login to GST portal → Services → User Services → Furnish Letter of Undertaking → Form GST RFD-11. Fill details, submit electronically with DSC or EVC. Valid for one financial year; renew annually before 31 March. Enables tax-free export of services (AdSense, foreign brand deals, Patreon, international subscribers)."),
        ("Does BQP handle content creator tax filings?",
         "Yes - annual ITR filing (ITR-4 for 44ADA or ITR-3 for regular), GST registration + filings + LUT bond, Section 194R brand perquisite reconciliation, FEMA / FIRC co-ordination for foreign receipts, cross-border structuring for creators with US entity (Delaware for high-income creators). WhatsApp +91 78018 87130."),
    ],
    related=[
        ("freelancer-consultant-tax-india-2026-complete.html", "Blog", "Freelancer / Consultant Tax"),
        ("section-194r-tds-business-perquisites-india.html", "Blog", "Section 194R"),
    ],
    cta_headline="YouTuber / Instagram creator with brand deals + AdSense + products?",
    cta_body="Standard creator package: Section 44ADA ITR-4 + GST registration with LUT bond + Section 194R reconciliation + FEMA FIRC flow. For creators above INR 50 lakh annual, structuring consultation (direct vs Delaware LLC) adds value.",
))

# 7. How to Buy US Stocks from India
write_page("how-to-buy-us-stocks-from-india-2026", page(
    slug="how-to-buy-us-stocks-from-india-2026",
    title="How to Buy US Stocks from India 2026 | Vested, INDmoney, Angel One Global - BQP",
    description="Buy US stocks from India 2026: compare Vested, INDmoney, Angel One Global, HDFC Securities Global; LRS USD 250K / year limit; Section 206C(1G) 20% TCS; tax on dividend 25% US withholding; FTC under India-US DTAA. Working CA guide by Durgesh Chavda.",
    keywords="how to buy US stocks from India 2026, Vested vs INDmoney, Angel One Global US stocks, buy Apple Google Amazon from India, LRS US stocks, US stock tax India NRI",
    hero_kicker="/ Blog &middot; US Stocks from India &middot; Updated 2026-10-10",
    hero_title_html="How to buy US stocks from India, <em>complete 2026 guide.</em>",
    hero_lead="Indian retail investors can legally buy US stocks (Apple, Google, Microsoft, Amazon, Tesla, Nvidia) using the Liberalised Remittance Scheme (LRS). Multiple Indian platforms (Vested, INDmoney, Angel One Global, HDFC Securities Global) have simplified the setup to under 30 minutes. The platform choice matters less than understanding LRS limit, 20% TCS, dividend tax, and FTC. Here is the full map.",
    sections=[
        ("/ The regulatory framework", "LRS + FEMA + US side.",
         "<p>Indian resident individual can invest in US stocks via <strong>LRS (Liberalised Remittance Scheme)</strong> under FEMA:</p>"
         "<ul>"
         "<li>Annual limit: <strong>USD 250,000</strong> (~INR 2.08 crore at INR 83/USD) per financial year per individual.</li>"
         "<li>Combined limit for all overseas remittances (investment + travel + education + maintenance).</li>"
         "<li>No RBI pre-approval needed for LRS investments.</li>"
         "</ul>"
         "<p><strong>Section 206C(1G) TCS:</strong> 20% TCS on LRS remittance above INR 10 lakh per FY (cumulative across all 'other' category remittances including stock investment). TCS is advance tax credit, refundable via ITR. Use our <a href=\"lrs-tcs-calculator.html\">LRS TCS Calculator</a>.</p>"
         "<p><strong>US side:</strong> Indian individual investing in US stocks is a Non-Resident Alien for US tax. US tax treatment:</p>"
         "<ul>"
         "<li>Capital gains on US stocks: generally NOT taxable in US for Non-Resident Alien (unless US real property interests under FIRPTA).</li>"
         "<li>Dividend from US stocks: 30% US withholding tax at source, REDUCED to <strong>25%</strong> under India-US DTAA Article 10 (portfolio dividend rate) &mdash; some brokers correctly apply 25%, others incorrectly apply 30%.</li>"
         "<li>Form W-8BEN required (filed with the broker at account opening) to claim 25% treaty rate.</li>"
         "</ul>"),
        ("/ Platform comparison", "Vested vs INDmoney vs Angel One vs HDFC vs others.",
         "<p><strong>Vested</strong> (vested.co.in):</p>"
         "<ul>"
         "<li>Partnered with Drivewealth (US broker).</li>"
         "<li>Fractional shares supported.</li>"
         "<li>Account opening: ~24 hours with PAN + Aadhaar + bank proof.</li>"
         "<li>Fees: USD 1 per transaction (varies by plan). No account maintenance fee on basic plan.</li>"
         "<li>Dividend handling: 25% US withholding (W-8BEN auto-filed).</li>"
         "<li>FIRC: generated for repatriation.</li>"
         "</ul>"
         "<p><strong>INDmoney</strong> (indmoney.com):</p>"
         "<ul>"
         "<li>Partnered with Drivewealth.</li>"
         "<li>Fractional shares supported.</li>"
         "<li>Integrates with Indian portfolio view across stocks, MFs, insurance.</li>"
         "<li>Fees: no commission on US stock trades (free). Spread on currency conversion.</li>"
         "<li>Dividend handling: 25% US withholding.</li>"
         "</ul>"
         "<p><strong>Angel One Global</strong>:</p>"
         "<li>Major Indian broker-backed. Integrated with Angel One Indian broking.</li>"
         "<li>Partnered with Vested in the back-end.</li>"
         "<li>Preferred for existing Angel One customers.</li>"
         "<p><strong>HDFC Securities Global Investment</strong>:</p>"
         "<ul>"
         "<li>Full-service broker route. Partnered with Stockal / Vested.</li>"
         "<li>Higher fees but integrated with HDFC Bank KYC and remittance workflow.</li>"
         "<li>Preferred for HNIs who already bank with HDFC.</li>"
         "</ul>"
         "<p><strong>Interactive Brokers (IBKR)</strong>:</p>"
         "<ul>"
         "<li>Direct US broker; not India-platform-wrapped.</li>"
         "<li>Account opening is more involved (W-8BEN filed directly).</li>"
         "<li>Lower fees for large portfolios; wider product range (options, futures, international markets).</li>"
         "<li>LRS compliance still applies on the Indian side.</li>"
         "</ul>"
         "<p>Platform choice drivers: fractional shares needed? (all support), fees matter? (INDmoney / IBKR win), existing broker relationship? (Angel One / HDFC), international market access? (IBKR).</p>"),
        ("/ Dividend tax + Foreign Tax Credit", "Avoiding double taxation.",
         "<p>US dividend from your US stocks: <strong>25% US withholding at source</strong> (under India-US DTAA Article 10, with properly filed W-8BEN). You receive the dividend net of withholding.</p>"
         "<p>On Indian side: dividend from foreign company is taxable in India as 'Income from Other Sources' at your slab rate.</p>"
         "<p>To avoid double taxation, claim <strong>Foreign Tax Credit (FTC)</strong> under Section 90 read with India-US DTAA Article 25:</p>"
         "<ul>"
         "<li>FTC = lower of (actual US tax paid) or (Indian tax on the same income).</li>"
         "<li>Claim via <strong>Form 67</strong> filed before ITR filing deadline.</li>"
         "<li>Retain US broker's Form 1099-DIV or equivalent as proof of US tax paid.</li>"
         "</ul>"
         "<p>Example: Indian investor receives USD 100 dividend from Apple Inc.</p>"
         "<ul>"
         "<li>Apple pays USD 100. US tax at 25% = USD 25. Net received = USD 75.</li>"
         "<li>Indian investor reports USD 100 as foreign income on ITR. Indian tax at (say) 30% slab = USD 30.</li>"
         "<li>FTC claimed = lower of USD 25 (US tax paid) or USD 30 (Indian tax) = USD 25.</li>"
         "<li>Net Indian tax after FTC = USD 30 - USD 25 = USD 5.</li>"
         "<li>Total tax paid: USD 25 (US) + USD 5 (India) = USD 30 (effectively Indian 30% rate, no double taxation).</li>"
         "</ul>"),
        ("/ Capital gains on US stock sale", "India + US side.",
         "<p><strong>US side:</strong> Non-Resident Alien capital gains on US stocks (not US real property) are generally NOT taxable in US. No US tax on sale.</p>"
         "<p><strong>India side:</strong> capital gains on foreign stocks are taxable in India:</p>"
         "<ul>"
         "<li><strong>LTCG (held 24+ months)</strong>: 12.5% without indexation under current Finance Act 2024 framework.</li>"
         "<li><strong>STCG (held under 24 months)</strong>: slab rate.</li>"
         "<li>Reported in Schedule CG of ITR (ITR-2 for salary + CG; ITR-3 if also business income).</li>"
         "<li>Schedule FA mandatory disclosure of foreign stock holdings if you are Resident and Ordinarily Resident.</li>"
         "</ul>"
         "<p>No treaty-based reduction on India-side capital gains (Article 13 of India-US DTAA assigns taxing right to India for the Indian resident).</p>"),
        ("/ Common mistakes", "What investors trip on.",
         "<ul>"
         "<li><strong>Not filing W-8BEN with broker</strong> &mdash; broker withholds dividend at 30% instead of DTAA 25%. 5-percentage-point extra on every dividend. Fix: ensure W-8BEN is on file; re-sign every 3 years.</li>"
         "<li><strong>Not claiming Form 67 FTC</strong> &mdash; leaves US tax paid as sunk cost. Indian taxpayer pays slab tax on top of US 25%. Form 67 before ITR deadline recovers the FTC.</li>"
         "<li><strong>Missing Schedule FA disclosure</strong> &mdash; mandatory for ROR taxpayers. Non-disclosure penalty under Black Money Act up to INR 10 lakh per undisclosed asset. US brokerage holdings always on Schedule FA.</li>"
         "<li><strong>Exceeding LRS limit</strong> &mdash; USD 250K per FY per individual. Family office structures use multiple individuals' separate limits. Keep running tally of all overseas remittances.</li>"
         "<li><strong>Breaking FEMA by using PayPal / crypto</strong> &mdash; investment remittance must flow through authorised dealer bank (not consumer PayPal, not crypto). Only broker-approved LRS channels.</li>"
         "<li><strong>Missing TCS credit on ITR</strong> &mdash; Section 206C(1G) TCS is deposited to your account; must be claimed as credit on ITR via Form 26AS reconciliation.</li>"
         "</ul>"
         "<p><em>Last updated: 2026-10-10.</em></p>"),
    ],
    faqs=[
        ("Can Indian residents legally buy US stocks?",
         "Yes. Under FEMA Liberalised Remittance Scheme (LRS), Indian resident individual can remit up to USD 250,000 per financial year for overseas investment including US stocks. Multiple SEBI-registered Indian platforms (Vested, INDmoney, Angel One Global, HDFC Securities Global) wrap the compliance into a simple account-opening flow."),
        ("What is the TCS on buying US stocks from India?",
         "20% TCS under Section 206C(1G) on LRS remittance above INR 10 lakh per financial year (cumulative across 'other' category remittances including investment). The 20% TCS is NOT a tax - it is advance tax credit, refundable via ITR. Use our LRS TCS Calculator for exact numbers."),
        ("What tax do I pay on US dividend?",
         "25% US withholding at source (under India-US DTAA Article 10 portfolio dividend rate, if W-8BEN is filed). On Indian side, dividend is taxable at your slab rate as 'Income from Other Sources'. Foreign Tax Credit under Form 67 recovers the US tax paid - net Indian tax is slab rate minus FTC. Final effective tax = your slab rate (no double taxation if correctly handled)."),
        ("Can I keep US stocks after moving to US / becoming NRI?",
         "Yes. On becoming US tax resident, you become US-side taxable on worldwide investment income (including on US stocks). Indian-side you become NRI - no longer need to disclose on Schedule FA, US stocks no longer Indian-taxable. The holding continues at your broker. For returning NRIs, the RNOR window post-return allows selling without Indian tax on capital gains."),
        ("Which platform is best for buying US stocks from India?",
         "Depends on priorities. INDmoney = free trades, integrated with Indian portfolio view, Drivewealth backend. Vested = similar + established since 2018. Angel One Global = integrated with Angel One Indian account. HDFC Securities = full-service for HDFC Bank customers. IBKR = lowest fees + widest product range, but more complex onboarding."),
        ("Does BQP handle US stock investment tax for Indian investors?",
         "Yes - annual ITR filing with foreign dividend + capital gains + Schedule FA disclosure + Form 67 FTC + TCS credit reconciliation. For HNIs with large US portfolios, pre-remittance LRS planning + spouse / family LRS stacking + eventual estate planning if moving to US. WhatsApp +91 78018 87130."),
    ],
    related=[
        ("lrs-tcs-calculator.html", "Tool", "LRS TCS Calculator"),
        ("india-us-dtaa-withholding-rates.html", "Guide", "India-US DTAA"),
        ("nri-taxation-india-complete-guide.html", "Guide", "NRI Taxation"),
    ],
    cta_headline="Building a US stock portfolio from India? Compliance stack matters.",
    cta_body="Annual ITR with Form 67 FTC claim, Schedule FA disclosure, TCS credit reconciliation. For HNIs with large portfolios, LRS stacking across family + pre-remittance planning + eventual estate planning if US move is on the horizon.",
))

# 8. Form 26AS vs AIS vs TIS
write_page("form-26as-vs-ais-vs-tis-india-2026", page(
    slug="form-26as-vs-ais-vs-tis-india-2026",
    title="Form 26AS vs AIS vs TIS 2026 | Which to Use for ITR Filing - BQP",
    description="Form 26AS vs AIS (Annual Information Statement) vs TIS (Taxpayer Information Summary) 2026: differences, which to download for ITR filing, reconciliation workflow, feedback mechanism, SFT (Specified Financial Transactions) reporting. CA Durgesh Chavda guide.",
    keywords="Form 26AS vs AIS 2026, AIS vs TIS difference, Annual Information Statement India, Taxpayer Information Summary, Form 26AS AIS reconciliation",
    hero_kicker="/ Blog &middot; Form 26AS vs AIS vs TIS &middot; Updated 2026-10-10",
    hero_title_html="Form 26AS vs AIS vs TIS, <em>what to use when filing ITR.</em>",
    hero_lead="Three statements. Overlapping data. Different granularity. Form 26AS (traditional), AIS (introduced November 2021), TIS (summary layer on top of AIS). For AY 2026-27 ITR filing, understanding which statement to use and how to reconcile between them is the single biggest cause of ITR errors + 139(9) notices. This is the practitioner's reconciliation guide.",
    sections=[
        ("/ What each statement is", "Scope and source.",
         "<p><strong>Form 26AS</strong> (traditional, pre-2021):</p>"
         "<ul>"
         "<li>Annual Tax Statement showing tax deducted / collected at source (TDS / TCS), tax paid, and refunds.</li>"
         "<li>Sourced from: deductors filing TDS returns (24Q / 26Q / 27Q), banks reporting high-value transactions, Challan payment records.</li>"
         "<li>Downloaded from TRACES portal (traces.gov.in).</li>"
         "<li>Scope: narrower &mdash; TDS, TCS, advance tax, self-assessment tax, refunds.</li>"
         "</ul>"
         "<p><strong>AIS (Annual Information Statement)</strong>:</p>"
         "<ul>"
         "<li>Introduced November 2021 under Section 285BB.</li>"
         "<li>Comprehensive statement covering all information from third parties (banks, brokers, mutual funds, insurance, employers, GST returns, SFT reports).</li>"
         "<li>Sourced from: multiple reporting entities under Specified Financial Transactions (SFT) reporting rules.</li>"
         "<li>Downloaded from e-filing portal (incometax.gov.in) &rarr; Services &rarr; Annual Information Statement.</li>"
         "<li>Scope: much broader &mdash; includes TDS/TCS plus savings interest, FD interest, mutual fund transactions, demat holdings, stock trades, property purchases, foreign remittances (LRS), credit card payments above INR 1 lakh.</li>"
         "</ul>"
         "<p><strong>TIS (Taxpayer Information Summary)</strong>:</p>"
         "<ul>"
         "<li>Summary of AIS - the Department's view of each income category after processing AIS data.</li>"
         "<li>Shows two values per category: 'Information Processed' (what the Department sees) and 'Taxpayer Feedback' (what you have agreed/disagreed with).</li>"
         "<li>Available on e-filing portal alongside AIS.</li>"
         "<li>Scope: same categories as AIS, but summarised and processed.</li>"
         "</ul>"),
        ("/ Which to use for ITR filing", "The practical answer.",
         "<p><strong>For AY 2026-27 ITR filing (FY 2025-26 income), download and review ALL THREE:</strong></p>"
         "<ol>"
         "<li><strong>AIS</strong>: comprehensive baseline. Review line-by-line each category (TDS, interest, dividend, capital gains, mutual fund transactions, property). This is what the Department knows.</li>"
         "<li><strong>TIS</strong>: see how Department processed the AIS data. Spot differences between raw AIS entries and processed TIS summary (occasional AI errors).</li>"
         "<li><strong>Form 26AS</strong>: specifically verify TDS / TCS entries (which flow into your tax credit on ITR). Must match the TDS claimed in ITR.</li>"
         "</ol>"
         "<p><strong>Primary reference</strong>: AIS. TIS is derived. Form 26AS is subset.</p>"
         "<p><strong>Golden rule</strong>: your ITR must match AIS at the aggregate level per income category. Mismatches trigger either 139(9) defective return or 143(1) demand with mismatch adjustment.</p>"),
        ("/ Common AIS entries to reconcile", "What to check line-by-line.",
         "<ul>"
         "<li><strong>Salary (Form 16 TDS):</strong> matches Form 26AS Part A. Any difference = ask employer to file revised 24Q.</li>"
         "<li><strong>Bank savings interest</strong>: all your savings accounts' interest reported here. Compare with bank statements. If missing, bank has not reported &mdash; check and update.</li>"
         "<li><strong>FD / RD interest</strong>: separate entry per deposit. TDS at 10% if above INR 40K / year (INR 50K for senior citizens).</li>"
         "<li><strong>Dividend income</strong>: all Indian equity and MF dividends. Section 194 TDS at 10% applies above INR 5,000.</li>"
         "<li><strong>Mutual fund transactions</strong>: all redemptions reported. Compare with your MF statements for FY. Capital gains computation feeds ITR Schedule CG.</li>"
         "<li><strong>Equity trades</strong>: all demat transactions from brokers. Reconcile with broker Capital Gains statement.</li>"
         "<li><strong>Property transactions</strong>: purchases above INR 30 lakh and sales above INR 50 lakh reported by Sub-Registrar.</li>"
         "<li><strong>Credit card payments above INR 1 lakh in a month or INR 10 lakh in a year</strong>: reported under SFT.</li>"
         "<li><strong>LRS foreign remittance</strong>: reported by AD banks. Includes US stock investments, overseas education, overseas gifts.</li>"
         "<li><strong>Foreign asset income</strong> (TCS on LRS, Section 206C(1G)): reflected as TCS credit.</li>"
         "<li><strong>Interest from P2P lending platforms</strong>: reported.</li>"
         "<li><strong>Crypto / VDA transactions</strong>: reported by Indian exchanges.</li>"
         "</ul>"),
        ("/ Feedback mechanism in AIS", "When Department has wrong info.",
         "<p>AIS has a feedback mechanism: for each entry, you can mark:</p>"
         "<ul>"
         "<li><strong>Information is correct</strong> (default assumption).</li>"
         "<li><strong>Information is partially correct</strong> &mdash; provide reason.</li>"
         "<li><strong>Information is incorrect</strong> &mdash; e.g., you did not have that bank account or did not make that purchase. Report via AIS feedback.</li>"
         "<li><strong>Information relates to other PAN</strong> &mdash; e.g., misreported against your PAN but belongs to another person.</li>"
         "</ul>"
         "<p>Feedback submitted via portal is processed; TIS updates after processing. If AIS entry is wrong, feedback must be submitted BEFORE ITR filing to avoid mismatch.</p>"
         "<p>Common feedback scenarios:</p>"
         "<ul>"
         "<li>Joint bank account interest fully reported against your PAN though actual holder is spouse &rarr; feedback 'partially correct' + split.</li>"
         "<li>Property purchase reported but you were a co-buyer with specified share &rarr; feedback 'partially correct' + share.</li>"
         "<li>Mutual fund redemption reported but with wrong cost basis &rarr; feedback 'partially correct' + correct cost.</li>"
         "<li>Transaction reported against your PAN but actually belongs to your HUF or other PAN &rarr; feedback 'other PAN' with correct PAN.</li>"
         "</ul>"
         "<p><em>Last updated: 2026-10-10.</em></p>"),
    ],
    faqs=[
        ("What is the difference between Form 26AS and AIS?",
         "Form 26AS (traditional) shows tax deducted / collected at source (TDS / TCS), tax paid, refunds. Narrower scope. AIS (Annual Information Statement, from November 2021) is comprehensive - includes all third-party reported transactions: savings interest, FD interest, dividend, MF transactions, demat trades, property purchases, credit card spending above INR 10 lakh, LRS foreign remittance, crypto transactions. AIS is the broader view."),
        ("Which should I use for ITR filing - 26AS or AIS?",
         "Both. AIS is the primary reference for comprehensive income reconciliation. Form 26AS specifically for TDS / TCS reconciliation (feeds into tax credit on ITR). Your ITR aggregate per category must match AIS. Mismatches trigger 139(9) defective return or 143(1) demand."),
        ("What is TIS (Taxpayer Information Summary)?",
         "A summary layer on top of AIS - shows the Department's processed view of each income category. Available on e-filing portal alongside AIS. Shows 'Information Processed' and 'Taxpayer Feedback' columns. Useful to spot where Department's processed view differs from raw AIS entries."),
        ("Can I disagree with an AIS entry?",
         "Yes - AIS has feedback mechanism. For each entry you can mark 'incorrect', 'partially correct', 'relates to other PAN'. Submit feedback via e-filing portal BEFORE ITR filing. Processed feedback updates TIS. Common scenarios: joint account interest misattributed, co-owner property purchase, wrong cost basis for MF redemption."),
        ("How do I download AIS?",
         "Login to incometax.gov.in → Services → Annual Information Statement → select the FY. Download the AIS PDF and TIS PDF. Form 26AS is downloaded from TRACES (traces.gov.in) or via the AIS portal link."),
        ("Does BQP help with Form 26AS / AIS reconciliation for ITR?",
         "Yes - standard pre-ITR reconciliation engagement. Download your Form 26AS + AIS + TIS, line-by-line reconciliation with your bank / broker / employer records, submit AIS feedback for incorrect entries, align ITR with reconciled AIS to avoid 139(9) or 143(1) mismatch. WhatsApp +91 78018 87130."),
    ],
    related=[
        ("itr-filing-ay-2026-27-deadlines-changes-india.html", "Blog", "ITR AY 2026-27"),
        ("section-143-1-intimation-response-india-2026.html", "Blog", "Section 143(1) Response"),
    ],
    cta_headline="ITR AY 2026-27 - AIS reconciliation prevents 139(9) notices.",
    cta_body="Pre-ITR reconciliation engagement: download Form 26AS + AIS + TIS, line-by-line match with your records, submit AIS feedback for errors, align ITR aggregates. Prevents the most common cause of defective return notices.",
))

# 9. PAN-Aadhaar Linking
write_page("pan-aadhaar-linking-status-fix-india-2026", page(
    slug="pan-aadhaar-linking-status-fix-india-2026",
    title="PAN-Aadhaar Linking Status Check + Fix 2026 | Deactivated PAN - BQP",
    description="PAN-Aadhaar linking status check 2026: deactivated PAN consequences (higher TDS, no ITR, no refund), reactivation via INR 1,000 Section 234H fee, NRI exemption, name mismatch fix, step-by-step linking process. CA Durgesh Chavda guide.",
    keywords="PAN Aadhaar linking status 2026, PAN Aadhaar link check, deactivated PAN fix, Section 234H fee, PAN not linked with Aadhaar, how to link PAN Aadhaar",
    hero_kicker="/ Blog &middot; PAN-Aadhaar Linking &middot; Updated 2026-10-10",
    hero_title_html="PAN-Aadhaar linking, <em>status, consequences, fix.</em>",
    hero_lead="PAN that is not linked with Aadhaar becomes INOPERATIVE under Section 139AA(2) from the deadline date. Consequences: higher TDS rate (20% under Section 206AA / 206CC), ITR cannot be processed, refund cannot be issued, GST registration linked to PAN affected, bank KYC frozen. The link can be restored by paying INR 1,000 Section 234H fee. NRIs and some categories are exempt. Here is the current state and the fix.",
    sections=[
        ("/ Current linking status requirement", "Where things stand.",
         "<p>Section 139AA of the Income Tax Act requires every PAN holder (except specified categories) to link PAN with Aadhaar. The latest linking deadline is specified by CBDT notification. For PANs that remain unlinked past the deadline:</p>"
         "<ul>"
         "<li>PAN becomes <strong>INOPERATIVE</strong> under Section 139AA(2).</li>"
         "<li>Can be made operative again by paying <strong>INR 1,000 fee under Section 234H</strong> and completing the linking.</li>"
         "</ul>"
         "<p><strong>Exempt categories (do NOT need to link):</strong></p>"
         "<ul>"
         "<li>Non-Resident Indians (NRI).</li>"
         "<li>Not a citizen of India.</li>"
         "<li>Residents of Assam, Jammu and Kashmir, Meghalaya.</li>"
         "<li>Super senior citizens (above 80 years of age).</li>"
         "</ul>"
         "<p>If you fall in any exempt category, update your PAN record on the e-filing portal to reflect the exemption.</p>"),
        ("/ Consequences of inoperative PAN", "What breaks.",
         "<ul>"
         "<li><strong>Higher TDS rate under Section 206AA</strong>: deductor must deduct at 20% (or applicable rate if higher) instead of the normal rate. For salary / interest / rent / professional fees, this is punitive.</li>"
         "<li><strong>Higher TCS rate under Section 206CC</strong>: 5% or applicable rate on sale of goods / LRS remittances / overseas tour packages.</li>"
         "<li><strong>ITR filing allowed but not processed</strong>: Centralised Processing Centre (CPC) will not process your return, no 143(1) intimation, no refund issued.</li>"
         "<li><strong>Refund of past years frozen</strong>: pending refunds not credited while PAN is inoperative.</li>"
         "<li><strong>Specified transactions blocked</strong>: Section 139AA(2) proviso disables PAN for specified transactions (bank account opening, FD above threshold, property purchase, mutual fund investment, share purchase above threshold).</li>"
         "<li><strong>GST registration linked to PAN</strong>: GST portal access may be affected depending on registration state.</li>"
         "<li><strong>DIN / company compliance</strong>: Director Identification Number linked to PAN; MCA filings affected.</li>"
         "</ul>"),
        ("/ Step-by-step linking process", "How to link and reactivate.",
         "<ol>"
         "<li><strong>Check status first</strong>: login to incometax.gov.in &rarr; Services &rarr; Link Aadhaar &rarr; Link Aadhaar Status. Shows 'Linked', 'Not Linked', or 'Linked but Inoperative'.</li>"
         "<li><strong>If 'Not Linked' and before deadline</strong>: simply link via Link Aadhaar section. Enter Aadhaar number and name as per Aadhaar. If names match (even partially), link completes immediately.</li>"
         "<li><strong>If 'Linked but Inoperative' (post-deadline)</strong>:</li>"
         "<li>&nbsp;&nbsp;a. Pay <strong>INR 1,000 Section 234H fee</strong> via Challan 280 on tds.tin.nsdl.com. Select 'Fee for Linking Aadhaar with PAN' as the type.</li>"
         "<li>&nbsp;&nbsp;b. Wait 24-48 hours for payment to reflect in the e-filing portal.</li>"
         "<li>&nbsp;&nbsp;c. Submit the Link Aadhaar request on the portal with the Challan reference.</li>"
         "<li>&nbsp;&nbsp;d. PAN becomes operative within 7-30 days typically (sometimes faster).</li>"
         "<li><strong>If name mismatch</strong>: either correct name on PAN (via NSDL / UTI PAN services) or correct name on Aadhaar (UIDAI update process). Smaller mismatches (minor spelling) often auto-resolve during linking.</li>"
         "<li><strong>If date of birth mismatch</strong>: more serious. Must correct one of the two (usually easier to correct Aadhaar) before linking.</li>"
         "</ol>"),
        ("/ Common linking failures and fixes", "Troubleshooting.",
         "<ul>"
         "<li><strong>Error: Name mismatch</strong> &mdash; Aadhaar name is 'Mr Durgesh Chavda' but PAN name is 'Durgesh K. Chavda'. Fix: update PAN name via NSDL / UTI PAN application (processing 15-30 days).</li>"
         "<li><strong>Error: DOB mismatch</strong> &mdash; different birth dates on PAN and Aadhaar. Fix: typically easier to correct Aadhaar (UIDAI online or at Aadhaar Seva Kendra).</li>"
         "<li><strong>Error: Aadhaar not generated</strong> &mdash; Aadhaar enrolment ID exists but final Aadhaar number not generated. Fix: check UIDAI status; may need to re-enrol.</li>"
         "<li><strong>Error: PAN already linked with different Aadhaar</strong> &mdash; indicates fraud or data entry error. Raise grievance on incometax.gov.in.</li>"
         "<li><strong>Error: Fee payment not reflected</strong> &mdash; wait 48 hours; if still not reflected, raise grievance with Challan proof.</li>"
         "<li><strong>Linking submitted but PAN still inoperative after 30 days</strong> &mdash; raise grievance on portal with linking acknowledgement.</li>"
         "</ul>"
         "<p><em>Last updated: 2026-10-10.</em></p>"),
    ],
    faqs=[
        ("How do I check my PAN-Aadhaar linking status?",
         "Login to incometax.gov.in → Services → Link Aadhaar → Link Aadhaar Status. Enter PAN. Status shows: 'Linked', 'Not Linked', or 'Linked but Inoperative' (post-deadline unlinked PANs that have been formally linked but marked inoperative pending Section 234H fee)."),
        ("What is the fee to reactivate inoperative PAN?",
         "INR 1,000 under Section 234H via Challan 280 (type: 'Fee for Linking Aadhaar with PAN'). Payment reflected in e-filing portal within 24-48 hours. After submission with Challan reference, PAN becomes operative within 7-30 days typically."),
        ("Who is exempt from PAN-Aadhaar linking?",
         "Non-Resident Indians (NRI), non-citizens of India, residents of Assam / Jammu and Kashmir / Meghalaya, and super senior citizens (above 80 years of age). If you fall in any of these categories, update your e-filing portal profile to reflect exemption - no linking required."),
        ("What are the consequences of inoperative PAN?",
         "Higher TDS rate under Section 206AA (20% or applicable, whichever higher), higher TCS under Section 206CC, ITR filed but not processed (no 143(1), no refund), specified transactions blocked (bank account opening, large FDs, property purchase, share purchases), GST registration affected, DIN / MCA filings affected."),
        ("Can I file ITR with inoperative PAN?",
         "You can file ITR but it will not be processed by CPC. No 143(1) intimation, no refund issued, no closure of return. Essentially useless until PAN is made operative. Reactivate PAN first (INR 1,000 Section 234H fee + link completion), then file ITR."),
        ("What if name on PAN and Aadhaar don't match?",
         "Minor spelling mismatches often auto-resolve during linking. Material mismatches require correction. Updating PAN name (via NSDL / UTI PAN application) takes 15-30 days. Updating Aadhaar name (UIDAI online or Aadhaar Seva Kendra) is typically faster. Easier to correct Aadhaar in most cases."),
    ],
    related=[
        ("itr-filing-ay-2026-27-deadlines-changes-india.html", "Blog", "ITR AY 2026-27"),
        ("form-26as-vs-ais-vs-tis-india-2026.html", "Blog", "Form 26AS vs AIS vs TIS"),
    ],
    cta_headline="PAN marked inoperative? Reactivation is INR 1,000 + 7-30 days.",
    cta_body="Working-CA engagement if your PAN is inoperative and you have pending refund / blocked transactions. Fee payment, linking submission, grievance resolution if linking fails. Routine but time-sensitive if refund is held up.",
))

# 10. Section 80C Full Guide
write_page("section-80c-complete-list-india-2026", page(
    slug="section-80c-complete-list-india-2026",
    title="Section 80C Complete Deduction List 2026 | INR 1.5 Lakh + All Eligible Investments - BQP",
    description="Section 80C full list of eligible deductions FY 2025-26: EPF, PPF, ELSS, NSC, LIC, ULIP, Sukanya Samriddhi, NPS Tier 1, home loan principal, children education fees, 5-year tax-saver FD. Working CA guide by Durgesh Chavda.",
    keywords="Section 80C complete list 2026, Section 80C deduction eligible investments, 80C 1.5 lakh limit, ELSS vs PPF vs NSC 80C, home loan principal 80C",
    hero_kicker="/ Blog &middot; Section 80C Complete List &middot; Updated 2026-10-10",
    hero_title_html="Section 80C, <em>the complete INR 1.5 lakh deduction list.</em>",
    hero_lead="Section 80C of the Income Tax Act allows up to INR 1,50,000 deduction per financial year across a specific list of investments and payments. For FY 2025-26 (AY 2026-27), the limit remains INR 1.5 lakh. Available only under OLD regime (opt-in via Form 10IEA). This is the complete practitioner's list of what qualifies, limits per category, and lock-in periods.",
    sections=[
        ("/ The INR 1.5 lakh overall limit", "How to think about it.",
         "<p>Section 80C provides a <strong>combined INR 1,50,000 deduction</strong> per financial year across all eligible categories. If you invest INR 1.5 lakh in one category, you have exhausted the limit; no further 80C deduction available in that FY.</p>"
         "<p>Related sections stacking:</p>"
         "<ul>"
         "<li><strong>Section 80CCD(1B)</strong>: additional INR 50,000 for NPS Tier 1 contributions (beyond 80C limit).</li>"
         "<li><strong>Section 80CCD(2)</strong>: employer NPS contribution deduction (14% of salary for government, 10% for private &mdash; above 80C limit).</li>"
         "<li>Combined 80C + 80CCD(1B) + 80CCD(2): can effectively provide INR 2 lakh+ in retirement-oriented deductions.</li>"
         "</ul>"
         "<p><strong>Available only under OLD regime</strong>: must explicitly elect Old regime via Form 10IEA before ITR due date. Under New regime (default from AY 2024-25), Section 80C is NOT available.</p>"),
        ("/ Complete eligible list - investments", "Where you can park money.",
         "<p><strong>1. EPF (Employee Provident Fund)</strong>:</p>"
         "<ul>"
         "<li>Mandatory employee contribution to EPF (12% of basic + DA).</li>"
         "<li>Full employee contribution qualifies for 80C.</li>"
         "<li>Lock-in: until retirement / resignation / specific premature withdrawal grounds.</li>"
         "<li>Current rate ~8.25% (FY 2024-25); announced annually by EPFO.</li>"
         "</ul>"
         "<p><strong>2. VPF (Voluntary Provident Fund)</strong>:</p>"
         "<ul>"
         "<li>Additional voluntary contribution to EPF above mandatory 12%.</li>"
         "<li>Same rate and treatment as EPF.</li>"
         "<li>Full contribution qualifies for 80C.</li>"
         "</ul>"
         "<p><strong>3. PPF (Public Provident Fund)</strong>:</p>"
         "<ul>"
         "<li>Government-backed deposit scheme, open at post office / banks.</li>"
         "<li>Contribution: minimum INR 500, maximum INR 1,50,000 per FY per account.</li>"
         "<li>Lock-in: 15 years; partial withdrawal allowed from 7th year.</li>"
         "<li>Current rate 7.1% (announced quarterly).</li>"
         "<li>Interest tax-free; EEE (exempt-exempt-exempt) status.</li>"
         "</ul>"
         "<p><strong>4. ELSS (Equity Linked Savings Scheme)</strong>:</p>"
         "<ul>"
         "<li>Tax-saver mutual fund with 3-year lock-in.</li>"
         "<li>Equity-oriented; returns are market-linked.</li>"
         "<li>Investment up to INR 1.5 lakh / FY qualifies.</li>"
         "<li>LTCG on redemption after 3-year lock-in: 12.5% (post-July 2024) on gains above INR 1.25 lakh / FY.</li>"
         "</ul>"
         "<p><strong>5. NSC (National Savings Certificate)</strong>:</p>"
         "<ul>"
         "<li>Government savings certificate from post office.</li>"
         "<li>5-year tenure.</li>"
         "<li>Current rate ~7.7%.</li>"
         "<li>Interest reinvested year-on-year is also eligible for 80C (cumulative benefit).</li>"
         "</ul>"
         "<p><strong>6. 5-Year Tax-Saver Fixed Deposit (bank FD)</strong>:</p>"
         "<ul>"
         "<li>Specific tax-saver FD scheme at banks and post office.</li>"
         "<li>5-year lock-in.</li>"
         "<li>Current rates ~6.5-7.5%.</li>"
         "<li>Interest fully taxable (not EEE like PPF).</li>"
         "</ul>"
         "<p><strong>7. Sukanya Samriddhi Yojana (SSY)</strong>:</p>"
         "<ul>"
         "<li>For girl children up to 10 years of age.</li>"
         "<li>Account opened in girl child's name by parent / guardian.</li>"
         "<li>Current rate 8.2% (highest among government schemes).</li>"
         "<li>Lock-in: until girl's marriage or 21-year maturity.</li>"
         "<li>EEE tax status.</li>"
         "</ul>"
         "<p><strong>8. Senior Citizen Savings Scheme (SCSS)</strong>:</p>"
         "<ul>"
         "<li>For individuals above 60 years (55 for retired government employees).</li>"
         "<li>Current rate 8.2%.</li>"
         "<li>5-year lock-in (extendable).</li>"
         "<li>Interest fully taxable.</li>"
         "</ul>"
         "<p><strong>9. NPS Tier 1</strong>:</p>"
         "<ul>"
         "<li>National Pension System retirement account.</li>"
         "<li>Up to 10% of salary (14% for government) qualifies under 80CCD(1) within 80C limit.</li>"
         "<li>Additional INR 50K under Section 80CCD(1B) BEYOND 80C limit.</li>"
         "<li>Market-linked returns.</li>"
         "</ul>"
         "<p><strong>10. ULIP (Unit Linked Insurance Plan)</strong>:</p>"
         "<ul>"
         "<li>Insurance + investment hybrid product.</li>"
         "<li>Premium qualifies for 80C up to INR 2.5 lakh / FY (if ULIP issued after 1 Feb 2021, Section 10(10D) exemption on maturity withdrawn for premium above INR 2.5 lakh).</li>"
         "<li>5-year lock-in.</li>"
         "</ul>"),
        ("/ Complete eligible list - payments", "Expenses that qualify.",
         "<p><strong>11. LIC premium / Term insurance premium</strong>:</p>"
         "<ul>"
         "<li>Premium paid for life insurance policies on self, spouse, children.</li>"
         "<li>Maximum premium qualifying for 80C: 10% of sum assured (20% if policy issued before 1 April 2012).</li>"
         "<li>Premium above the 10%/20% threshold does NOT qualify.</li>"
         "<li>Section 10(10D) exemption on maturity payout available if premium limits respected and sum assured above INR 2.5 lakh.</li>"
         "</ul>"
         "<p><strong>12. Children's tuition fees</strong>:</p>"
         "<ul>"
         "<li>Full-time education fees for maximum 2 children.</li>"
         "<li>Includes school, college, university tuition.</li>"
         "<li>Does NOT include: donations, hostel fees, transport fees, extracurricular fees, coaching/private tuition fees.</li>"
         "<li>Maximum: 2 children per taxpayer.</li>"
         "</ul>"
         "<p><strong>13. Home loan principal repayment</strong>:</p>"
         "<ul>"
         "<li>Principal portion of home loan EMI for self-occupied / let-out residential property.</li>"
         "<li>Also includes stamp duty + registration charges in the year of purchase.</li>"
         "<li>Section 24(b) separately covers interest (not in 80C) up to INR 2 lakh.</li>"
         "<li>Lock-in: 5 years from the year of claim; if property sold before 5 years, principal claimed is reversed to income.</li>"
         "</ul>"
         "<p><strong>14. Stamp duty + registration charges</strong>:</p>"
         "<ul>"
         "<li>Paid at the time of residential property purchase.</li>"
         "<li>Deductible under 80C in the year of purchase (part of the overall INR 1.5 lakh limit).</li>"
         "</ul>"
         "<p><strong>15. Mutual Fund Pension Plans</strong>:</p>"
         "<ul>"
         "<li>Specific retirement-oriented MF schemes qualifying under Section 80CCC (within 80C limit).</li>"
         "</ul>"),
        ("/ What does NOT qualify under 80C", "Common misunderstandings.",
         "<ul>"
         "<li>Investment in direct equity shares (listed or unlisted).</li>"
         "<li>Non-tax-saver mutual funds (equity funds other than ELSS, debt funds, hybrid funds).</li>"
         "<li>Non-5-year tax-saver fixed deposits.</li>"
         "<li>Recurring deposits (RD).</li>"
         "<li>Second home loan EMI principal (allowed under 80C only for self-occupied / let-out of specified house; restriction on multiple properties).</li>"
         "<li>Children's hostel / transport fees.</li>"
         "<li>Life insurance premium beyond 10%/20% of sum assured.</li>"
         "<li>Health insurance premium (covered under Section 80D separately).</li>"
         "<li>Donations (covered under Section 80G separately).</li>"
         "<li>Education loan interest (covered under Section 80E separately).</li>"
         "</ul>"),
        ("/ Which 80C instrument to pick", "Decision framework.",
         "<p>For MOST taxpayers, the optimal 80C mix:</p>"
         "<ol>"
         "<li>EPF (mandatory 12%) typically covers INR 70K-1 lakh of the 80C limit for salaried taxpayers.</li>"
         "<li>Remaining limit (INR 50K-80K): split between ELSS (equity returns, 3-year lock-in) and PPF (safe, 15-year lock-in, EEE).</li>"
         "</ol>"
         "<p>For risk-averse / older taxpayers: NSC + 5-year tax saver FD + PPF.</p>"
         "<p>For girl-child families: Sukanya Samriddhi + ELSS + home loan.</p>"
         "<p>For senior citizens: SCSS + 5-year FD.</p>"
         "<p>Compare New vs Old regime first using our <a href=\"new-vs-old-tax-regime-calculator.html\">New vs Old Tax Regime Calculator</a> &mdash; if your 80C + 80D + HRA + home loan interest don't exceed INR 4-5 lakh at income above INR 10 lakh, New regime typically wins (no 80C needed).</p>"
         "<p><em>Last updated: 2026-10-10.</em></p>"),
    ],
    faqs=[
        ("What is the Section 80C deduction limit for FY 2025-26?",
         "INR 1,50,000 combined across all eligible categories. Section 80CCD(1B) adds additional INR 50,000 for NPS Tier 1 contributions beyond the 80C limit. Only available under OLD tax regime (opt-in via Form 10IEA before ITR filing deadline). Not available under default new regime."),
        ("Which Section 80C investment has the highest return?",
         "Sukanya Samriddhi Yojana currently offers 8.2% (highest among government schemes). Senior Citizen Savings Scheme also 8.2% for senior citizens. ELSS can produce higher but market-linked (12-15% long-term historical). PPF 7.1%. NSC ~7.7%. Choose based on lock-in tolerance and risk appetite, not just rate."),
        ("Does home loan principal repayment qualify for 80C?",
         "Yes - principal portion of home loan EMI for residential property (self-occupied or let-out). Also stamp duty + registration charges in the year of purchase. Lock-in: 5 years - if property sold before 5 years, principal claimed in prior years is reversed. Section 24(b) separately covers interest up to INR 2 lakh (not in 80C)."),
        ("Can I claim 80C under New Tax Regime?",
         "No. Section 80C is available only under OLD regime. New regime (default from AY 2024-25) has lower slabs but no 80C / 80D / HRA / home loan interest deductions. Only standard deduction (INR 75K salaried) and employer NPS contribution. If your 80C + 80D + HRA + home loan interest total above INR 4-5 lakh at income above INR 10 lakh, Old regime typically wins."),
        ("Do children's hostel and transport fees qualify under 80C?",
         "No. Only tuition fees for full-time education of maximum 2 children qualify. Hostel fees, transport fees, uniform, books, extracurricular activity fees, private tuition / coaching fees are NOT eligible under 80C."),
        ("Does BQP help with tax planning under Section 80C?",
         "Yes - as part of annual ITR engagement we review Old vs New regime, suggest 80C investment mix matched to your risk profile and lock-in tolerance, co-ordinate with your financial advisor on ELSS / PPF / Sukanya / NPS allocations, and file ITR under the chosen regime. WhatsApp +91 78018 87130."),
    ],
    related=[
        ("itr-filing-ay-2026-27-deadlines-changes-india.html", "Blog", "ITR AY 2026-27"),
        ("new-vs-old-tax-regime-calculator.html", "Tool", "New vs Old Regime Calculator"),
    ],
    cta_headline="80C limit maxed? Then check 80CCD(1B) NPS and 80D health insurance.",
    cta_body="Annual tax planning + ITR engagement: Old vs New regime election, 80C investment mix review, 80CCD(1B) NPS stacking, 80D health insurance, home loan interest planning. Standard individual tax engagement scoped per profile.",
))

print("Batch K complete: 10 search-intent-driven pages written")
