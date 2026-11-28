# -*- coding: utf-8 -*-
"""Batch KX (28 Nov 2026): Income tax outstanding demand - what it means, how to respond (agree, partly agree, disagree),
section 245 refund adjustment, interest, rectification, appeal and stay.
Demand: 'outstanding demand income tax', 'income tax demand notice what to do', 'section 245 notice', 'refund adjusted against
demand' - on the site only as lines inside the refund-delayed, notice-reply and 143(1) pages; no dedicated page. High hire intent
(a demand must be answered and often needs rectification or appeal). User steer 26 Nov 2026: more call bookings / WhatsApp.
Facts: a demand is raised by an intimation (143(1)), an assessment or penalty order, with a notice of demand (section 156);
unpaid demand after the time in the notice carries interest at 1% per month (section 220(2)); before setting a refund off
against a demand, the department sends an intimation under section 245 (1961 Act; corresponding provisions in the 2025 Act)
and the taxpayer can respond on the e-filing portal saying the demand is correct, partly correct or disputed, with reasons
(already paid, rectification filed, appeal filed, stay granted, TDS credit not given); wrong demands are corrected by
rectification (section 154, now section 287) or appeal to CIT(A) within 30 days of service of the order; stay of demand
pending appeal on payment of a part (CBDT guideline 20%, Budget 2026-27 announced 10% of core tax - matched to the site
stay page). Interest is a statutory charge (allowed by the user's 27 Nov rule); no fees, no portal menu paths.
advisory_lib.contact() is not used."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources
from build_lib import page, write_page

A.UPDATED = "Last updated: 28 November 2026."
SLUG = "income-tax-outstanding-demand-what-to-do-section-245-refund-adjustment-disagree-rectification-2026"

C = ("WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with the outstanding demand details (assessment year, "
     "section and amount shown), the intimation or order that raised it, challans for any tax already paid, Form 26AS / AIS "
     "for that year, and any section 245 intimation. Or book a call directly.")
PAGES = [dict(
    slug=SLUG,
    title="Income Tax Outstanding Demand (2026): What It Means, How to Respond (Agree, Partly Agree, Disagree), Section 245 Refund Adjustment, Interest, Rectification and Appeal",
    em="answer it, don&rsquo;t ignore it.",
    kicker="/ Salaried, self-employed, NRIs and companies &middot; Outstanding demand and section 245 intimations &middot; Updated 2026-11-28",
    lead=("<strong>An outstanding demand is tax the department says you still owe for a past year - raised by a 143(1) intimation, an assessment or a penalty order. "
          "Left alone, it carries interest at 1% per month and can be recovered from your future refunds under section 245. "
          "Many demands are wrong - tax already paid, TDS credit missed, a processing error - and can be disputed online, rectified or appealed.</strong>"),
    sections=[
        ("/ Where the demand comes from, and what fixes it", "Cause first, remedy second.",
         table(["Common cause", "Usual remedy"], [
             ["Tax already paid but challan not matched", "Respond that the demand is paid, with challan details; rectification if needed"],
             ["TDS / TCS credit not given (missing in Form 26AS or claimed in wrong year)", "Get the deductor to correct the TDS return; then rectification"],
             ["Arithmetic or processing error in the 143(1) intimation", "Rectification (section 154, now section 287)"],
             ["Disallowance or addition in an assessment order", "Appeal to CIT(A) within 30 days of service; seek stay of demand"],
             ["Demand already reduced by an appeal or rectification order", "Respond with the order so the record is updated"],
             ["Demand is correct", "Pay it (to stop 1% per month interest) or seek instalments"]])
         + ul("<strong>Find the source:</strong> every demand has an assessment year, a section and a reference to the intimation or order that raised it - get that document before replying.",
              "<strong>Old demands:</strong> legacy demands from years ago often relate to processing errors or TDS mismatches and can still be disputed with evidence.")),
        ("/ Responding, refund adjustment, interest and stay", "Sections 156, 220(2) and 245.",
         ul("<strong>Respond online:</strong> on the e-filing portal you can say the demand is correct, partly correct or disputed, and give the reason (paid, rectification filed, appeal filed, stay granted, credit not given) with supporting details.",
            "<strong>Section 245 intimation:</strong> before setting a refund off against a demand, the department sends an intimation; reply within the time stated, or the refund can be adjusted.",
            "<strong>Interest:</strong> a demand not paid within the time in the notice of demand (section 156) carries interest at 1% per month under section 220(2).",
            "<strong>Pending appeal:</strong> apply for a stay of demand; under CBDT guidelines a stay is generally granted on payment of a part of the disputed demand.",
            "<strong>Don&rsquo;t just agree to clear the screen:</strong> agreeing to a wrong demand allows adjustment of your refunds and makes later correction harder.")
         + call_box("an outstanding income tax demand", ["Tracing the source of the demand",
                                                         "Online response: agree, partly agree or disagree",
                                                         "Rectification for processing and credit errors",
                                                         "Appeal to CIT(A) and stay of demand",
                                                         "Section 245 refund adjustment replies"],
                    "Demand details, the intimation or order, challans, Form 26AS / AIS, any section 245 intimation.")
         + sources("Income-tax Act, 1961 (sections 143(1), 154, 156, 220, 245 and 246A) and the corresponding provisions of the Income-tax Act, 2025; CBDT guidelines on stay of demand; site refund delayed, 143(1), rectification, appeal and stay pages.")),
    ],
    faqs=[("What does outstanding demand mean in income tax?", "It is tax, interest or penalty the department says you still owe for a past year, raised by a 143(1) intimation, an assessment order or a penalty order. It shows against your PAN until it is paid, reduced by rectification or appeal, or recorded as disputed."),
          ("What should I do if I get an outstanding demand notice?", "Find the intimation or order that raised it and check the cause. If it is correct, pay it to stop interest. If it is wrong, respond online saying it is disputed with the reason, then file a rectification for processing or credit errors or an appeal against an assessment order."),
          ("Can the department adjust my refund against an old demand?", "Yes. Under section 245 it can set off a refund against a demand for another year after sending you an intimation. Reply to the intimation within the time given if the demand is wrong, already paid or under appeal."),
          ("Is there interest on an unpaid income tax demand?", "Yes. If the demand is not paid within the time in the notice of demand, interest at 1% per month runs under section 220(2) until it is paid or reduced."),
          ("I already paid the tax but it still shows as outstanding. What now?", "Respond that the demand is paid, with the challan details (BSR code, date, serial number). If the payment was made under the wrong year or head, a correction or rectification is needed."),
          ("What should I send to start?", "WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with the demand details, the intimation or order, challans for tax paid, Form 26AS / AIS for that year and any section 245 intimation. Or book a call directly.")],
    related=[("itr-refund-delayed-2026-why-and-what-to-do.html", "Income tax refund delayed"),
             ("rectification-under-section-154-income-tax-now-section-287-time-limit-online-request-format-2026.html", "Rectification under section 154 / 287"),
             ("stay-of-income-tax-demand-20-percent-rule-budget-2026-10-percent-how-to-apply-format-2026.html", "Stay of income tax demand"),
             ("income-tax-appeal-cit-appeals-form-35-form-99-time-limit-30-days-fee-20-percent-pre-deposit-2026.html", "Appeal to CIT(A)")],
    cta_h="Outstanding demand showing against your PAN?", cta_b=C,
    keywords="income tax outstanding demand, outstanding demand what to do, response to outstanding demand, section 245 notice, refund adjusted against demand, disagree with income tax demand, interest on income tax demand 220(2)",
    desc="Income tax outstanding demand: where it comes from (143(1), assessment, penalty), how to respond online (correct, partly correct, disputed), section 245 refund adjustment, 1% per month interest under 220(2), rectification, appeal to CIT(A) and stay.",
    howto={"name": "How to handle an income tax outstanding demand", "description": "Trace, decide, respond.", "steps": [
        {"name": "Trace the source", "text": "Get the intimation or order for that assessment year and section."},
        {"name": "Check the cause", "text": "Paid tax, missing TDS credit, processing error or a real addition."},
        {"name": "Respond online", "text": "Agree, partly agree or disagree, with reasons and evidence."},
        {"name": "Fix or contest", "text": "Pay if correct; rectify errors; appeal and seek stay for additions."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch KX complete")
