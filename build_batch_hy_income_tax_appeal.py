# -*- coding: utf-8 -*-
"""Batch HY (25 Nov 2026): income tax appeal to CIT(A) / JCIT(A) - 30 days from service of the order, Form 35 under the
1961 Act and Form 99 under the 2025 Act (rule 167 of the Income-tax Rules, 2026, appeals against orders under sections 356 /
357; time limit in section 358), fee Rs 250 / 500 / 1,000 by assessed income, condonation of delay, faceless appeals,
stay of demand with a 20% pre-deposit under CBDT instructions, ITAT as the next forum, status tracking.
Demand: sweep ac106 (25 Nov 2026), all 7 markets: "income tax appeal time limit", "income tax appeal pre deposit", "income
tax appeal procedure", "income tax appeal status", "cit appeals fees", "commissioner of income tax appeals case status".
Facts (checked 25 Nov 2026): Income Tax Department pages (appeal to CIT(A); appeals and revision; section 358; Form 99
FAQs and Form 99 notification); Taxguru, TaxHeal (manner of filing appeal to CIT(A) AY 2026-27), Patron Accounting on
faceless appeals under the 2025 Act. 20% pre-deposit from CBDT Office Memoranda of 29 February 2016 and 31 July 2017
(settled practice)."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 25 November 2026."
SLUG = "income-tax-appeal-cit-appeals-form-35-form-99-time-limit-30-days-fee-20-percent-pre-deposit-2026"

C = contact("the order you want to challenge (section, assessment year, date of service, DIN), the demand raised, and the points you disagree with")
L = lambda h, t: f'<a href="{h}">{t}</a>'
PAGES = [dict(
    slug=SLUG,
    title="Income Tax Appeal to CIT(A) (2026): Time Limit 30 Days, Form 35 / Form 99, Fees, 20% Pre-Deposit for Stay and Appeal Status",
    em="file within 30 days, then deal with the demand.",
    kicker="/ Taxpayers disputing an assessment &middot; Income tax &middot; Updated 2026-11-25",
    lead=("<strong>The first appeal against an income tax assessment or penalty order goes to the Commissioner of Income Tax (Appeals) or the Joint Commissioner (Appeals), and must be filed online within 30 days of receiving the order.</strong> "
          "Under the Income-tax Act, 1961 the appeal is filed in Form 35; under the Income-tax Act, 2025 the form is Form 99 (rule 167 of the Income-tax Rules, 2026), so use the form that applies to the year of the order. "
          "The fee is &#8377;250, &#8377;500 or &#8377;1,000 depending on assessed income. Filing an appeal does not stop the demand: to keep recovery on hold while the appeal is pending, taxpayers usually pay 20% of the disputed demand and apply for a stay, under CBDT instructions."),
    sections=[
        ("/ Quick answers", "What people search for.",
         ul("<strong>What is the time limit for an income tax appeal?</strong> 30 days from the date the order is served. A late appeal can be admitted if you show sufficient cause for the delay, with a condonation request.",
            "<strong>Which form?</strong> Form 35 for orders under the 1961 Act; Form 99 for appeals against orders under sections 356 or 357 of the 2025 Act. Both are filed on the e-filing portal with a digital signature or EVC.",
            "<strong>What are the CIT(A) appeal fees?</strong> A small statutory fee that rises with the assessed income band, with a flat fee for appeals not about assessed income. Check the current amount on the portal and pay it by challan before filing.",
            "<strong>Do I need to pay a pre-deposit?</strong> There is no statutory pre-deposit to file. To stay recovery of the demand while the appeal is pending, CBDT instructions generally expect 20% of the disputed demand to be paid, with the rest stayed.",
            "<strong>How do I check appeal status?</strong> In the e-filing portal under the appeals section of pending actions and e-proceedings; appeals are heard in a faceless manner through notices on the portal.",
            "<strong>What if I lose at CIT(A)?</strong> The next appeal is to the Income Tax Appellate Tribunal (ITAT), generally within 60 days of the appellate order.")),
        ("/ Appeal vs other remedies", "Pick the right route.",
         table(["Situation", "Remedy"], [
             ["Disagreement on facts, law or additions in an assessment or penalty order", "Appeal to CIT(A) / JCIT(A)"],
             ["Obvious arithmetic error or credit not given", L("rectification-under-section-154-income-tax-now-section-287-time-limit-online-request-format-2026.html", "Rectification (section 154 / 287)")],
             ["You missed income in your return", L("itr-u-updated-return-48-months-section-139-8a-india.html", "Updated return (ITR-U)") + " where available"],
             ["Reassessment notice", L("section-148-148a-reassessment-notice-response-india.html", "Reply to the 148A notice") + ", then appeal against the final order"],
             ["Order of CIT(A) still adverse", "Appeal to ITAT"]])),
        ("/ Filing a strong appeal", "What to prepare.",
         ul("<strong>Grounds of appeal:</strong> short, specific grounds against each addition or disallowance, plus a statement of facts.",
            "<strong>Evidence:</strong> documents filed before the assessing officer; new evidence is admitted only in limited circumstances, so explain why it was not filed earlier.",
            "<strong>Demand:</strong> request a stay from the assessing officer, paying the expected pre-deposit, so refunds are not adjusted and recovery does not start.",
            "<strong>Hearings:</strong> appeals are handled faceless; reply to each portal notice by the date given and ask for a video hearing if needed; see " + L("income-tax-notice-reply-letter-format-sample-how-to-submit-e-proceedings-2026.html", "notice reply format") + ".",
            "<strong>Scrutiny background:</strong> see " + L("section-143-2-scrutiny-notice-response-india.html", "scrutiny notices") + ".")
         + call_box("Income tax appeals", ["Grounds and statement of facts",
                                           "Form 35 / Form 99 filing",
                                           "Stay of demand and pre-deposit",
                                           "Condonation of delay",
                                           "Faceless hearings and ITAT appeals"],
                    "the order, the demand and the dates.")
         + sources("Income-tax Act, 1961, sections 246A to 251; Income-tax Act, 2025, sections 356 to 358 and Income-tax Rules, 2026, rule 167 (Form 99); Income Tax Department pages on appeals to CIT(A), Form 99 FAQs and section 358; CBDT Office Memoranda of 29 February 2016 and 31 July 2017 on stay of demand; Taxguru, TaxHeal and Patron Accounting commentary. Fee bands are reported slightly differently; confirm on the portal. Checked 25 November 2026.")),
    ],
    faqs=[("What is the time limit to file an income tax appeal?", "30 days from the date the assessment or penalty order is served. A delayed appeal can still be admitted if the Commissioner (Appeals) is satisfied there was sufficient cause, so file a condonation request with reasons."),
          ("Which form is used for an income tax appeal in 2026?", "Form 35 for orders under the Income-tax Act, 1961, and Form 99 under the Income-tax Act, 2025 (rule 167 of the Income-tax Rules, 2026) for appeals against orders under sections 356 or 357. Both are filed on the e-filing portal."),
          ("What is the fee for an appeal to CIT(A)?", "A small statutory fee that rises with the assessed income band (with a flat fee for appeals not about assessed income), paid by challan before filing. Check the current amount on the portal. Confirm the band on the portal."),
          ("Is a 20% pre-deposit required to file an income tax appeal?", "No pre-deposit is needed to file. To stay recovery of the disputed demand while the first appeal is pending, CBDT instructions generally expect 20% of the disputed demand to be paid, with the balance stayed."),
          ("Where does the next appeal go after CIT(A)?", "To the Income Tax Appellate Tribunal, generally within 60 days of receiving the CIT(A) order."),
          ("Can BQP file and argue my income tax appeal?", "Yes. CA Durgesh Chavda can draft grounds and the statement of facts, file the appeal, seek a stay of demand and handle faceless hearings. " + C)],
    related=[("rectification-under-section-154-income-tax-now-section-287-time-limit-online-request-format-2026.html", "Rectification under section 154"),
             ("section-143-2-scrutiny-notice-response-india.html", "Scrutiny notice response"),
             ("section-148-148a-reassessment-notice-response-india.html", "Reassessment notice response"),
             ("income-tax-notice-reply-letter-format-sample-how-to-submit-e-proceedings-2026.html", "Notice reply letter format"),
             ("how-to-respond-to-income-tax-notice-india.html", "Responding to an income tax notice")],
    cta_h="Received an assessment order you disagree with?", cta_b=C,
    keywords="income tax appeal, income tax appeal time limit, CIT appeals fees, Form 35 appeal, Form 99 appeal, income tax appeal pre deposit 20 percent, stay of demand, income tax appeal status, commissioner of income tax appeals, ITAT appeal",
    desc="Income tax appeal to CIT(A) (2026): file within 30 days in Form 35 (1961 Act) or Form 99 (2025 Act), statutory fee by challan, 20% pre-deposit to stay the demand, condonation of delay, faceless hearings, appeal status, ITAT next.",
    howto={"name": "How to file an income tax appeal to CIT(A)", "description": "On the e-filing portal.", "steps": [
        {"name": "Note the service date", "text": "The 30-day limit runs from when the order was served."},
        {"name": "Pay the appeal fee", "text": "Pay the statutory appeal fee (it depends on the assessed income) by challan before filing."},
        {"name": "Draft grounds and facts", "text": "Specific grounds against each addition, with documents."},
        {"name": "File Form 35 or Form 99", "text": "Online, verified with DSC or EVC."},
        {"name": "Seek a stay of demand", "text": "Pay the expected 20% and apply to the assessing officer."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch HY complete")
