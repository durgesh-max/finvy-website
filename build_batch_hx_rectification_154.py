# -*- coding: utf-8 -*-
"""Batch HX (25 Nov 2026): rectification of mistakes in income tax orders - section 154 of the 1961 Act, section 287 of
the 2025 Act: mistake apparent from record; four years from end of the financial year in which the order was passed;
application to be disposed of within six months from the end of the month of receipt; online rectification request on the
e-filing portal for CPC 143(1) intimations (request types); rectification vs revised / updated return vs appeal; format.
Demand: sweep ac106 (25 Nov 2026), all 7 markets: "rectification us 154", "rectification under 154", "154 rectification order",
"154 rectification format", "rectification us 154 time limit".
Facts (checked 25 Nov 2026): Income Tax Department pages on section 287 (2025 Act) and 'rectification, assessment and
appeal'; TMI notes; Aaptaxlaw section 287 explainer; Taxscan 360 on section 154 time limits and grounds. Portal request
types (reprocess, tax credit mismatch, status correction, exemption section correction, return data correction) from the
e-filing portal's rectification service."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 25 November 2026."
SLUG = "rectification-under-section-154-income-tax-now-section-287-time-limit-online-request-format-2026"

C = contact("the order or intimation (section, assessment year, DIN), what you think is wrong, your return and any demand or refund involved")
L = lambda h, t: f'<a href="{h}">{t}</a>'
PAGES = [dict(
    slug=SLUG,
    title="Rectification Under Section 154 (Now Section 287): Time Limit, Online Request, Format and When to Appeal Instead",
    em="for mistakes that are obvious from the record.",
    kicker="/ Taxpayers with a wrong intimation or order &middot; Income tax &middot; Updated 2026-11-25",
    lead=("<strong>Rectification lets the tax department correct a mistake apparent from the record in an order or intimation, such as a TDS credit not given, an arithmetic error or a deduction ignored by the processing centre.</strong> "
          "It is section 154 of the Income-tax Act, 1961, and section 287 of the Income-tax Act, 2025. "
          "An application can be made within four years from the end of the financial year in which the order was passed, and the authority must dispose of it within six months from the end of the month in which it is received. "
          "For errors in a section 143(1) intimation from the CPC, file an online rectification request on the e-filing portal. Disputes that need argument or evidence go to appeal, not rectification."),
    sections=[
        ("/ Quick answers", "What people search for.",
         ul("<strong>What can be rectified?</strong> Only a mistake apparent from the record: something obvious from the order and return without debate, such as a wrong calculation, credit for tax paid not given, or a claim visibly ignored.",
            "<strong>What is the time limit?</strong> Four years from the end of the financial year in which the order or intimation was passed. The authority must decide an application within six months from the end of the month it is received.",
            "<strong>How do I file a 154 rectification online?</strong> Log in to the e-filing portal, open the rectification service, choose the assessment year and the order, and pick the request type; CPC handles requests on its 143(1) intimations.",
            "<strong>Is there a 154 rectification format?</strong> For CPC orders the portal form is the format. For an order passed by an assessing officer, write an application quoting the order, the DIN, the mistake, the correct position and supporting documents, and submit it on the portal.",
            "<strong>Rectification or appeal?</strong> Use rectification for obvious errors; use an appeal for disputes on facts or law, and do not miss the appeal time limit while waiting for a rectification.",
            "<strong>Rectification or revised return?</strong> If the mistake is yours in the return, revise or update the return; rectification corrects the department&rsquo;s order.")),
        ("/ Online request types (CPC intimations)", "Choose the one that fits.",
         table(["Request type", "Use it when"], [
             ["Reprocess the return", "The return should be processed again, for example after a credit is now visible"],
             ["Tax credit mismatch correction", "TDS, TCS or advance tax paid was not credited correctly"],
             ["Status correction", "Residential status or taxpayer status was applied wrongly"],
             ["Exemption section correction", "An exemption section was wrongly applied or ignored"],
             ["Return data correction (online / offline)", "Figures in the return need correcting for reprocessing"]])
         + '<p>Related: ' + L("section-143-1-intimation-response-india-2026.html", "responding to a 143(1) intimation") + ', ' + L("itr-refund-delayed-2026-why-and-what-to-do.html", "ITR refund status and delays") + ' and ' + L("income-tax-notice-reply-letter-format-sample-how-to-submit-e-proceedings-2026.html", "income tax notice reply format") + '.</p>'),
        ("/ Choosing the right route", "Rectification, appeal or a fresh return.",
         table(["Problem", "Route"], [
             ["Obvious error in the department&rsquo;s order or intimation", "Rectification (section 154 / 287)"],
             ["Disagreement on facts, evidence or interpretation", "Appeal"],
             ["Your own mistake or omission in the return, current window open", L("revised-itr-section-139-5-deadline-31-december-2026-india.html", "Revised return")],
             ["Your own omission, revised window closed", L("itr-u-updated-return-48-months-section-139-8a-india.html", "Updated return (ITR-U)")],
             ["Mismatch with AIS", L("ais-mismatch-itr-what-to-do-feedback-revised-return-31-december-2026-e-campaign-nri.html", "AIS feedback and, if needed, revised return")]])
         + call_box("Rectification and demand disputes", ["Reading the intimation or order",
                                                         "Online rectification request",
                                                         "Application to the assessing officer",
                                                         "Rectification vs appeal decision",
                                                         "Refunds and outstanding demands"],
                    "the order, the mistake and the amounts.")
         + sources("Income-tax Act, 1961, section 154; Income-tax Act, 2025, sections 287 and 288 (Income Tax Department section pages); Income Tax Department page on rectification, assessment and appeal; e-filing portal rectification service; TMI notes, Aaptaxlaw and Taxscan commentary. Checked 25 November 2026.")),
    ],
    faqs=[("What is rectification under section 154?", "A correction of a mistake apparent from the record in an income tax order or intimation, such as a calculation error or tax credit not given. From tax year 2026-27 the provision is section 287 of the Income-tax Act, 2025."),
          ("What is the time limit for rectification under section 154?", "Four years from the end of the financial year in which the order sought to be rectified was passed. Once an application is received, it must be disposed of within six months from the end of the month of receipt."),
          ("How do I file a rectification request online?", "On the income tax e-filing portal, open the rectification service, select the assessment year and the order, and choose the request type, such as reprocessing, tax credit mismatch, status or exemption correction, or return data correction."),
          ("Is there a format for a section 154 rectification application?", "For CPC intimations the portal form is used. For an order by an assessing officer, write an application quoting the order and DIN, the mistake, the correct position and supporting documents, and submit it on the portal."),
          ("Should I file rectification or an appeal?", "Rectification is only for obvious errors. If the issue needs argument on facts or law, file an appeal within its time limit; a pending rectification does not extend the appeal deadline."),
          ("Can BQP file a rectification for me?", "Yes. CA Durgesh Chavda can review the intimation or order, file the rectification or application, and advise whether an appeal is needed. " + C)],
    related=[("section-143-1-intimation-response-india-2026.html", "Section 143(1) intimation"),
             ("itr-refund-delayed-2026-why-and-what-to-do.html", "ITR refund status"),
             ("income-tax-notice-reply-letter-format-sample-how-to-submit-e-proceedings-2026.html", "Notice reply letter format"),
             ("how-to-respond-to-income-tax-notice-india.html", "Responding to an income tax notice"),
             ("income-tax-act-2025-section-mapping-old-vs-new-54-is-82-80c-is-123-nri.html", "Old vs new section numbers")],
    cta_h="Wrong intimation or order?", cta_b=C,
    keywords="rectification under section 154, rectification u/s 154, 154 rectification time limit, 154 rectification format, rectification request online income tax, section 287 Income-tax Act 2025, mistake apparent from record, reprocess return",
    desc="Rectification under section 154 (now section 287 of the 2025 Act): mistakes apparent from record, four-year time limit, six-month disposal, online request types for CPC intimations, application format, and when to appeal or revise instead.",
    howto={"name": "How to file an income tax rectification", "description": "For a mistake in a CPC intimation.", "steps": [
        {"name": "Read the intimation", "text": "Identify the exact mistake and the amount."},
        {"name": "Check it is apparent from record", "text": "Obvious from the return and order, not a dispute."},
        {"name": "Open the rectification service", "text": "On the e-filing portal, choose the assessment year and order."},
        {"name": "Pick the request type", "text": "Reprocess, tax credit mismatch, status, exemption or data correction."},
        {"name": "Track the outcome", "text": "Within six months; appeal if the issue is not rectifiable."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch HX complete")
