# -*- coding: utf-8 -*-
"""Batch JZ (27 Nov 2026): GST summons under section 70, inspection and search under section 67, and the related
notices people search next (GSTR-3A under section 46, DRC-07 summary of demand) - what each means and what to do.
Demand: sweep ac146 (27 Nov 2026), all 7 markets: "gst summons section 70", "... reply format", "... procedure", "... case
id", "gst inspection search and seizure", "gst search seizure summon and arrest", "search and seizure under gst act",
"assessment order and gst drc 07 (means)", "standalone drc 07 order in gst", "gstr 3a notice under section 46", "gstr 3a
notice kya hota hai", "gst special audit section 66"; no page covered GST summons or search.
User steer 26 Nov 2026: more call bookings / WhatsApp enquiries - a GST summons or search needs a professional at once.
Facts (verified 27 Nov 2026): section 70 CGST Act - the proper officer can summon any person to give evidence or produce
documents, with the powers of a civil court, and the inquiry is a judicial proceeding; CBIC Instruction 03/2022-23
(GST-Investigation, 17 August 2022) - summons are not to be used for records already on the GST portal, and senior
management (CMD, MD, CEO, CFO) should not ordinarily be summoned in the first instance; Circular 249/06/2025-GST - a
communication carrying a reference number (RFN) need not quote a DIN; section 67 - inspection on written authorisation
(INS-01) of a Joint Commissioner or above, search and seizure where there is reason to believe, copies of seized documents,
provisional release of seized goods; arrest under section 69 only for specified offences under section 132 with the
Commissioner's authorisation (thresholds not restated); section 46 - GSTR-3A notice to a return defaulter, file within 15
days, otherwise best judgment assessment under section 62, which is withdrawn if the return is filed within 60 days (a
further 60 days with additional late fee); DRC-07 is the summary of a demand order - appeal under section 107 within three
months; special audit under section 66 by a CA / cost accountant nominated by the Commissioner. No fees, no timings, no
office claims."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 27 November 2026."
SLUG = "gst-summons-section-70-inspection-search-section-67-drc-07-gstr-3a-what-to-do-2026"

C = contact("the summons, authorisation or notice (with its reference number), the date and place you are asked to appear, the period and transactions it mentions, your GST returns for that period, and any panchnama or list of documents taken")
PAGES = [dict(
    slug=SLUG,
    title="GST Summons under Section 70, Inspection and Search under Section 67 (2026): What to Do, Your Rights, GSTR-3A, DRC-07 and E-Way Bill Penalties",
    em="prepare before you appear.",
    kicker="/ Businesses, directors and foreign-owned subsidiaries &middot; GST investigations and orders &middot; Updated 2026-11-27",
    lead=("<strong>A GST summons under section 70 requires you to appear, give a statement or produce documents before a GST officer; an inspection or search under section 67 means officers can visit your premises and take documents or goods.</strong> "
          "Both are serious: statements are recorded in a judicial proceeding and are used later in show cause notices. "
          "Respond on time, carry only what is asked, keep copies of everything, and take professional help before the first appearance."),
    sections=[
        ("/ What each notice means", "Summons, search, GSTR-3A and DRC-07.",
         table(["Notice", "What it is", "What to do"], [
             ["Summons (section 70)", "Order to appear, give evidence or produce documents; the officer has civil-court powers and the inquiry is a judicial proceeding", "Check the reference number, date and documents asked for; appear or seek a short adjournment in writing; prepare a factual statement"],
             ["Inspection / search (section 67)", "Visit on written authorisation (INS-01) of a Joint Commissioner or above; search and seizure where there is reason to believe tax was evaded", "Ask to see the authorisation, cooperate, check the panchnama and inventory, and take copies of documents seized"],
             ["GSTR-3A (section 46)", "Notice to a person who has not filed a return, asking them to file within 15 days", "File the overdue return with late fee and interest; otherwise a best judgment assessment can follow"],
             ["DRC-07", "Summary of a demand order (tax, interest, penalty) issued after adjudication", "Check the order and the date it was communicated; appeal in APL-01 within three months or pay"],
             ["Special audit (section 66)", "Audit of your records by a chartered or cost accountant nominated by the Commissioner", "Give the records asked for and answer the findings before any demand"]])),
        ("/ Your position on a summons", "Guidelines officers must follow.",
         ul("<strong>Records already online:</strong> CBIC Instruction 03/2022-23 says summons should not be used to call for records already available on the GST portal.",
            "<strong>Senior management:</strong> the same instruction says chairpersons, managing directors, CEOs and CFOs should not ordinarily be summoned in the first instance.",
            "<strong>Reference number:</strong> check the document identification or reference number on the summons; CBIC's Circular 249/06/2025-GST treats a communication with a reference number (RFN) as not needing a separate DIN.",
            "<strong>Your statement:</strong> answer factually, do not guess figures, ask to read the statement before signing, and keep a copy; retractions later carry little weight.",
            "<strong>Arrest:</strong> arrest is possible only for specified offences under section 132 with the Commissioner's authorisation - if you fear arrest, take legal advice at once.")),
        ("/ After the visit or statement", "What usually follows.",
         ul("A show cause notice (DRC-01) under section 73 or 74, often preceded by DRC-01A - reply on time with documents.",
            "Voluntary payment with interest can reduce penalty at the right stage - weigh it before the notice is issued.",
            "Seized goods can be released provisionally on a bond and security; seized documents must be returned if not relied on.",
            "If an order is passed, the DRC-07 summary starts the three-month appeal clock.")
         + call_box("GST investigations", ["Preparing for a section 70 summons",
                                           "Support during inspections and searches",
                                           "Replies to DRC-01A and DRC-01 show cause notices",
                                           "GSTR-3A and best judgment assessment fixes",
                                           "Appeals against DRC-07 demand orders"],
                    "The summons or notice and your returns.")
         + sources("CGST Act, 2017 (sections 46, 62, 66, 67, 69, 70, 73, 74, 107, 132) and CGST Rules (Forms INS-01, INS-04, GSTR-3A, ASMT-13, DRC-01A, DRC-01, DRC-07); CBIC Instruction 03/2022-23 (GST-Investigation) dated 17 August 2022; CBIC Circular 249/06/2025-GST; site GST notice reply, appeal and registration guides. Checked 27 November 2026.")),
    ],
    faqs=[("What is a GST summons under section 70?", "An order from a GST officer requiring you to appear, give evidence or produce documents. The officer has the powers of a civil court and the inquiry is treated as a judicial proceeding, so statements recorded can be used later in a show cause notice or prosecution."),
          ("How do I reply to a GST summons?", "There is no fixed reply format. Check the reference number, date and documents asked for, then either appear with those documents or write asking for a short adjournment with reasons. Prepare a factual statement with your adviser, read it before signing, and keep copies of everything submitted."),
          ("Can a GST officer summon the CEO or managing director?", "CBIC Instruction 03/2022-23 says senior management such as chairpersons, managing directors, CEOs and CFOs should not ordinarily be summoned in the first instance, and that summons should not be used to call for records already on the GST portal."),
          ("What happens during a GST inspection or search?", "Officers visit on written authorisation (INS-01) from a Joint Commissioner or above, inspect records and stock, and may seize documents or goods. Ask to see the authorisation, check the panchnama and inventory before signing, and take copies of seized documents; seized goods can be released provisionally on a bond and security."),
          ("What is a GSTR-3A notice?", "A notice under section 46 to someone who has not filed a GST return, asking them to file within 15 days. If the return is not filed, the officer can make a best judgment assessment under section 62; that order is withdrawn if the return is filed within 60 days (a further 60 days with an additional late fee)."),
          ("What does an assessment order and DRC-07 mean?", "DRC-07 is the summary of a demand order showing the tax, interest and penalty payable after a show cause notice is decided. It starts the three-month time limit to appeal in APL-01, with the pre-deposit, or the amount must be paid."),
        ("What is the penalty for moving goods without an e-way bill?", "Under section 129 the goods and vehicle can be detained. Where the owner comes forward, the penalty is 200% of the tax payable on the goods (for exempt goods, 2% of their value or Rs 25,000, whichever is less); where the owner does not come forward, a higher penalty applies. The officer issues a notice in MOV-07 and passes an order in MOV-09, and the goods are released once the penalty is paid. If the detention was wrong - for example a minor clerical error in the e-way bill - reply to the MOV-07 notice with the invoice and documents, and appeal the MOV-09 order in APL-01 if needed, with a pre-deposit of 25% of the penalty."),
        ("How do I pay an e-way bill penalty online?", "Once the officer passes the penalty order in MOV-09, its summary is uploaded as a demand in DRC-07 and appears in your electronic liability register on the GST portal. Deposit the amount into your electronic cash ledger through a GST challan and pay that demand from the cash ledger - penalties cannot be paid from input tax credit. After payment the goods and vehicle are released by a release order (MOV-05). Pay within the time allowed - section 129(6) lets the goods be sold if the penalty is not paid within 15 days of the order. If the detention or the amount is wrong, you can still pay to release the goods and challenge the order in appeal under section 107. WhatsApp +91 78018 87130 with the MOV-07 notice, the MOV-09 order and the invoice and e-way bill, and we check the penalty and whether an appeal is worth filing."),
        ("What should I send if my goods were detained for an e-way bill issue?", "WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with the MOV-07 notice or MOV-09 order, the tax invoice and e-way bill (if any), the lorry receipt or transport documents, and the detention memo. We prepare the reply to the notice, work out the penalty position and, where the order is wrong, the appeal. You keep your own GST login."),
          ("What should I send if I received a GST summons or notice?", "WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with the summons, authorisation or notice and its reference number, the date and place of appearance, the period and transactions mentioned, your GST returns for that period, and any panchnama or list of documents taken. We prepare you for the appearance, draft replies and handle what follows. You keep your own GST login.")],
    related=[("gst-notice-response-india-asmt-drc-gstr.html", "GST notice reply (ASMT-10, DRC-01)"),
             ("gst-appeal-apl-01-section-107-time-limit-pre-deposit-format-appellate-authority-2026.html", "GST appeal in APL-01"),
             ("gst-drc-01c-drc-01b-notice-reply-itc-mismatch-gstr-2b-3b-liability-mismatch-gstr-1-3b-rule-88c-88d-2026.html", "DRC-01C / DRC-01B mismatch notices"),
             ("gst-registration-rejected-or-suspended-reg-03-reg-05-rule-21a-reg-31-what-to-do-2026.html", "GST registration rejected or suspended"),
             ("gst-registration-cancellation-reg-16-reg-19-gstr-10-revocation-reg-21-certificate-download-2026.html", "GST cancellation and revocation")],
    cta_h="Received a GST summons or search?", cta_b=C,
    keywords="gst summons section 70, gst summons reply format, gst search and seizure, gst inspection section 67, gstr 3a notice, drc 07 order meaning, gst special audit section 66, gst arrest section 69, e way bill penalty section 129, goods detained without e way bill",
    desc="GST summons under section 70 and inspection or search under section 67: what each means, the CBIC guidelines on summons, your position during a statement or search, and what GSTR-3A and DRC-07 orders mean - with what to send.",
    howto={"name": "How to respond to a GST summons", "description": "From the summons to a recorded statement.", "steps": [
        {"name": "Check the summons", "text": "Confirm the reference number, date, place and documents asked for."},
        {"name": "Gather documents", "text": "Collect returns, invoices and records for the period mentioned."},
        {"name": "Prepare the statement", "text": "Agree the facts with your adviser; do not guess figures."},
        {"name": "Appear and keep copies", "text": "Read the statement before signing and keep copies of everything submitted."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch JZ complete")
