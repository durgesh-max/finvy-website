# -*- coding: utf-8 -*-
"""Batch HL (25 Nov 2026): income tax notice reply letter format - there is no prescribed format; structure of a reply,
sample skeleton, annexures, how to submit through e-Proceedings, adjournment, authorised representative, DIN check.
Demand: sweep ac96 (25 Nov 2026), all 7 markets: "income tax notice reply letter format in word pdf", "income tax notice
reply letter format in word", "income tax notice reply format in word", "income tax notice reply time limit", "income tax
notice reply ai tool".
Facts (checked 25 Nov 2026): e-Filing portal help 'Respond to e-Proceedings' and FAQs (Pending Actions > e-Proceedings >
Self > View Notice > Submit Response; attachments; response cannot be edited once submitted; adjournment / extension
request; authorised representative); 'Comply to Notice' FAQ (enter DIN from the notice); CBDT Circular 19/2019 (DIN on
communications from 1 October 2019; communications without DIN treated as invalid)."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 25 November 2026."
SLUG = "income-tax-notice-reply-letter-format-sample-how-to-submit-e-proceedings-2026"

C = contact("a copy of the notice (section, tax year, DIN and due date), what it asks for, and your return for that year")
L = lambda h, t: f'<a href="{h}">{t}</a>'
SKELETON = ('<div style="border:1px solid var(--line,#ddd);border-radius:6px;padding:18px 20px;font-family:ui-monospace,Menlo,Consolas,monospace;font-size:13px;line-height:1.7;white-space:pre-wrap">'
            'To,\nThe Assessing Officer / National Faceless Assessment Centre\n\n'
            'Subject: Reply to notice under section [__] for Assessment Year / Tax Year [____]\n'
            'Name: [__________]   PAN: [__________]\n'
            'Notice DIN: [__________]   Dated: [__/__/____]\n\n'
            'Respected Sir / Madam,\n\n'
            '1. With reference to the above notice, I submit my reply below.\n'
            '2. Point-wise reply:\n'
            '   (a) [Query 1 as worded in the notice] - [Reply, with figures] - Annexure A\n'
            '   (b) [Query 2] - [Reply] - Annexure B\n'
            '3. [Reconciliation of the amount in question, if any]\n'
            '4. I request that the above be considered and the proceedings closed / no adjustment be made. '
            'I may be given an opportunity of being heard by video conference before any adverse view is taken.\n\n'
            'Annexures: A - [__]; B - [__]; C - [__]\n\n'
            'I declare that the information given above is true and correct.\n\n'
            'Place: [____]   Date: [__/__/____]\n'
            '[Name]  [Signature]</div>'
            '<p><em>This skeleton is a starting point, not legal advice. The right reply depends on the section, the query and the evidence.</em></p>')
PAGES = [dict(
    slug=SLUG,
    title="Income Tax Notice Reply Letter Format (2026): Sample Structure, Annexures and How to Submit Through e-Proceedings",
    em="answer each point, attach the proof, submit before the due date.",
    kicker="/ Taxpayers, NRIs and companies &middot; Income tax &middot; Updated 2026-11-25",
    lead=("<strong>There is no official format for replying to an income tax notice.</strong> "
          "A good reply quotes the notice (section, tax year, DIN and date), answers every query point by point, reconciles any figures in question, attaches evidence as numbered annexures, and is submitted online through e-Proceedings on the e-filing portal before the due date. "
          "Once submitted, a reply cannot be edited, so check it carefully, and ask for an adjournment on the portal if you need more time."),
    sections=[
        ("/ Quick answers", "What people search for.",
         ul("<strong>Is there a prescribed format?</strong> No. Write a clear letter or statement and attach it as a PDF with your supporting documents.",
            "<strong>Where do I submit it?</strong> Log in to the e-filing portal, go to Pending Actions, then e-Proceedings, open the notice and use Submit Response. Upload the reply and annexures.",
            "<strong>What is the time limit?</strong> The date given in the notice. If you need more time, request an adjournment on the portal before the due date and give a reason.",
            "<strong>Can I edit a reply after submitting?</strong> No. You can make a further submission, but the first one stays on record.",
            "<strong>How do I know the notice is genuine?</strong> Check the Document Identification Number (DIN) using the portal&rsquo;s authenticate notice service. Under CBDT Circular 19/2019, a communication without a DIN is treated as invalid.",
            "<strong>Can someone reply for me?</strong> Yes. You can add an authorised representative, such as a chartered accountant, to respond through e-Proceedings.")),
        ("/ Sample reply structure", "Fill in the brackets.", SKELETON),
        ("/ What to say for common notices", "Match the reply to the section.",
         table(["Notice", "What the reply should cover"], [
             ["Intimation under 143(1) (adjustment)", "Agree or disagree with each adjustment; if wrong, file rectification. See " + L("section-143-1-intimation-response-india-2026.html", "143(1) guide")],
             ["Defective return 139(9)", "Correct the defect and file the corrected return within the time given"],
             ["Scrutiny 143(2) / questionnaire 142(1)", "Point-wise answers, ledgers, bank statements, reconciliations. See " + L("section-143-2-scrutiny-notice-response-india.html", "scrutiny guide")],
             ["Reassessment 148A show cause", "Why income has not escaped assessment, with evidence; ask for the material relied on. See " + L("how-to-respond-section-148a-show-cause-notice-india-step-by-step.html", "148A guide")],
             ["AIS / high-value transaction mismatch", "Explain the transaction, give AIS feedback, revise the return if needed. See " + L("ais-mismatch-itr-what-to-do-feedback-revised-return-31-december-2026-e-campaign-nri.html", "AIS mismatch guide")],
             ["Foreign assets or income not disclosed", "Disclosure route (revised return, ITR-U or FAST-DS) and reply. See " + L("income-tax-email-foreign-assets-fast-ds-what-to-do.html", "foreign assets email")]])
         + '<p>Notices for years before tax year 2026-27 cite sections of the Income-tax Act, 1961; see ' + L("income-tax-act-2025-section-mapping-old-vs-new-54-is-82-80c-is-123-nri.html", "old vs new section numbers") + '.</p>'),
        ("/ Mistakes to avoid", "Where replies go wrong.",
         ul("<strong>Missing the due date</strong> and getting a best-judgment assessment or penalty; ask for an adjournment instead.",
            "<strong>Answering a different question</strong>: quote each query exactly and answer it.",
            "<strong>Unlabelled attachments</strong>: number annexures and refer to them in the reply.",
            "<strong>Admitting income without working it out</strong>: reconcile first; an unexplained admission is hard to undo.",
            "<strong>Using generic or AI-generated text</strong> that does not match the facts; officers see many identical replies.",
            "<strong>Ignoring a request to be heard</strong>: if an adverse view is likely, ask for a personal hearing by video conference.")
         + call_box("Replying to an income tax notice", ["Reading the notice and deadline",
                                                          "Point-wise reply and reconciliations",
                                                          "Annexures and evidence",
                                                          "Adjournment and hearing requests",
                                                          "Filing as authorised representative"],
                    "the notice, the tax year and your return.")
         + sources("Income Tax e-Filing portal help: Respond to e-Proceedings, e-Proceedings FAQs and Comply to Notice FAQs; CBDT Circular 19/2019 on the Document Identification Number; Income Tax Department faceless scheme pages. Checked 25 November 2026.")),
    ],
    faqs=[("Is there a format for replying to an income tax notice?", "No format is prescribed. Quote the notice (section, tax year, DIN, date), answer each query point by point, reconcile any figures, list numbered annexures, add a declaration, and submit it as a PDF through e-Proceedings."),
          ("How do I submit a reply to an income tax notice online?", "Log in to the e-filing portal, open Pending Actions and then e-Proceedings, choose the notice, click Submit Response, and upload the reply and annexures before the due date."),
          ("What if I cannot reply by the due date?", "Request an adjournment or extension on the portal before the due date, giving a reason. Not replying can lead to an assessment on the information available and penalties."),
          ("Can I edit my reply after submission?", "No. A submitted response cannot be edited, though you can make a further submission. Check the reply and attachments before submitting."),
          ("How can I check whether an income tax notice is genuine?", "Use the portal's authenticate notice service with the DIN on the notice. Under CBDT Circular 19/2019, a communication without a DIN is treated as invalid."),
          ("Can BQP reply to an income tax notice for me?", "Yes. CA Durgesh Chavda can act as authorised representative, draft the point-wise reply with annexures and handle hearings. " + C)],
    related=[("how-to-respond-to-income-tax-notice-india.html", "How to respond to an income tax notice"),
             ("section-143-1-intimation-response-india-2026.html", "Section 143(1) intimation"),
             ("section-143-2-scrutiny-notice-response-india.html", "Section 143(2) scrutiny"),
             ("section-148-148a-reassessment-notice-response-india.html", "Section 148 / 148A reassessment"),
             ("ais-mismatch-itr-what-to-do-feedback-revised-return-31-december-2026-e-campaign-nri.html", "AIS mismatch")],
    cta_h="Received an income tax notice?", cta_b=C,
    keywords="income tax notice reply letter format, income tax notice reply format in word, reply to income tax notice sample, income tax notice reply time limit, how to reply income tax notice online, e-proceedings response, income tax notice DIN",
    desc="Income tax notice reply letter format (2026): no prescribed format; sample structure with notice details, point-wise reply, annexures and declaration; how to submit through e-Proceedings, adjournment, DIN check, common notices.",
    howto={"name": "How to reply to an income tax notice", "description": "Through the e-filing portal.", "steps": [
        {"name": "Verify the notice", "text": "Check the DIN, section, tax year and due date."},
        {"name": "Gather evidence", "text": "Return, AIS, bank statements, ledgers, agreements."},
        {"name": "Draft the reply", "text": "Quote each query and answer it point by point, with numbered annexures."},
        {"name": "Submit on e-Proceedings", "text": "Pending Actions, e-Proceedings, Submit Response; upload PDFs."},
        {"name": "Track and follow up", "text": "Watch for further queries; request a hearing if needed."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch HL complete")
