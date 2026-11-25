# -*- coding: utf-8 -*-
"""Batch IA (25 Nov 2026): condonation of delay in income tax - section 119(2)(b) of the Income-tax Act, 1961 for
belated returns claiming a refund or carry forward of loss; CBDT Circular No. 11/2024 (1 October 2024): Pr. CIT / CIT up
to Rs 1 crore per assessment year, CCIT above Rs 1 crore up to Rs 3 crore, Pr. CCIT above Rs 3 crore; no application
beyond five years from the end of the assessment year; disposal as far as possible within six months from the end of the
month of receipt; reasonable cause and genuine hardship; CIT CPC Bengaluru for delayed ITR-V verification; court time
excluded. Late appeals: CIT(A) and ITAT can admit late appeals for sufficient cause.
Demand: sweep ac106 (25 Nov 2026), all 7 markets: "condonation of delay income tax", "condonation of delay under section
119(2)(b)", "condonation of delay in filing itr", "condonation of delay application", "condonation of delay meaning".
Facts (checked 25 Nov 2026): Circular No. 11/2024 text as reproduced by CAclubindia; Taxmann summaries of Circulars
11/2024 and 07/2023; Income Tax Department circular pages (Circular 9/2015). Interest on condoned refunds is not stated
for ordinary belated refund returns in Circular 11/2024 (only 'no interest' on belated supplementary claims), so the
page does not assert it."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 25 November 2026."
SLUG = "condonation-of-delay-income-tax-section-119-2-b-itr-refund-loss-application-2026"

C = contact("the assessment year, the return or form that was late, the refund or loss involved, and the reason for the delay with any supporting documents")
L = lambda h, t: f'<a href="{h}">{t}</a>'
PAGES = [dict(
    slug=SLUG,
    title="Condonation of Delay in Income Tax Under Section 119(2)(b): Late ITR With Refund or Loss, Limits, Time Limit and Application",
    em="when a deadline has passed but the refund or loss still matters.",
    kicker="/ Taxpayers who missed a return deadline &middot; Income tax &middot; Updated 2026-11-25",
    lead=("<strong>Condonation of delay lets the income tax authorities accept a return claiming a refund or carry forward of loss even after the normal time limit, if the taxpayer shows a reasonable cause for the delay and genuine hardship.</strong> "
          "The power is in section 119(2)(b) of the Income-tax Act, 1961, and CBDT Circular No. 11/2024 (1 October 2024) says who decides: the Principal Commissioner or Commissioner for claims up to &#8377;1 crore per assessment year, the Chief Commissioner above &#8377;1 crore up to &#8377;3 crore, and the Principal Chief Commissioner above &#8377;3 crore. "
          "An application cannot be entertained beyond five years from the end of the assessment year of the claim, and should be decided, as far as possible, within six months from the end of the month in which it is received."),
    sections=[
        ("/ Quick answers", "What people search for.",
         ul("<strong>What does condonation of delay mean?</strong> Asking the authority to excuse a missed deadline so that a late return, claim or appeal can still be accepted on its merits.",
            "<strong>When is section 119(2)(b) used?</strong> Mainly when the belated or revised return window has closed and you want to claim a refund (for example excess TDS) or carry forward a loss that would otherwise lapse.",
            "<strong>Who decides?</strong> By claim size per assessment year: up to &#8377;1 crore Principal Commissioner / Commissioner; &#8377;1 crore to &#8377;3 crore Chief Commissioner; above &#8377;3 crore Principal Chief Commissioner. Delays in verifying a return (ITR-V) are handled by the Commissioner, CPC Bengaluru.",
            "<strong>What is the time limit?</strong> Five years from the end of the assessment year for which the claim is made. Time spent in court proceedings can be excluded if you apply within six months of the court order or by the end of that financial year, whichever is later.",
            "<strong>What must the application show?</strong> That a reasonable cause prevented filing on time and that refusing the claim would cause genuine hardship. The authority can ask the assessing officer to verify the facts.",
            "<strong>Is condonation guaranteed?</strong> No. It is discretionary; a clear, documented reason (illness, a death in the family, a technical failure, a pending dispute) carries weight, while plain oversight often does not.")),
        ("/ Which route for which delay", "Not every late filing goes to section 119(2)(b).",
         table(["Situation", "Route"], [
             ["Return filed late or not filed, refund or loss at stake, belated window closed", "Condonation application under section 119(2)(b)"],
             ["Return filed but not verified in time", "Condonation request for delayed verification (Commissioner, CPC)"],
             ["Belated window still open", L("belated-itr-31-december-2026-section-139-4-india.html", "Belated return") + " instead, with late fee"],
             ["Income missed, refund not claimed", L("itr-u-updated-return-48-months-section-139-8a-india.html", "Updated return (ITR-U)") + " can add income but cannot claim a refund"],
             ["Appeal filed after 30 days", L("income-tax-appeal-cit-appeals-form-35-form-99-time-limit-30-days-fee-20-percent-pre-deposit-2026.html", "Late appeal") + " with a request to condone the delay for sufficient cause"],
             ["Mistake in a processed return", L("rectification-under-section-154-income-tax-now-section-287-time-limit-online-request-format-2026.html", "Rectification") + ", not condonation"]])),
        ("/ Preparing the application", "What to include.",
         ul("<strong>Facts:</strong> the assessment year, the due date missed, when the return was or will be filed, and the refund or loss amount.",
            "<strong>Reason:</strong> a specific explanation of what prevented filing, with dates.",
            "<strong>Evidence:</strong> medical records, death certificate, proof of technical failure, correspondence, or court orders, as relevant.",
            "<strong>Hardship:</strong> why losing the refund or loss would be unfair, for example tax already deducted at source on income that is below the taxable limit.",
            "<strong>Follow-up:</strong> respond to any enquiry from the assessing officer; once condoned, file or regularise the return as directed.",
            "<strong>Related:</strong> " + L("missed-itr-due-date-21-november-2026-audit-case-what-you-lose-loss-carry-forward-10-iea-80ac.html", "missed the ITR due date") + ", " + L("itr-refund-delayed-2026-why-and-what-to-do.html", "ITR refund delays") + " and " + L("how-to-respond-to-income-tax-notice-india.html", "income tax notices") + ".")
         + call_box("Condonation of delay", ["Reviewing whether a claim is worth pursuing",
                                             "Drafting the section 119(2)(b) application",
                                             "Evidence and hardship statement",
                                             "Filing the return after condonation",
                                             "Late appeals with delay condonation"],
                    "the assessment year, the claim and the reason for delay.")
         + sources("Income-tax Act, 1961, section 119(2)(b); CBDT Circular No. 11/2024 dated 1 October 2024 (F. No. 312/63/2023-OT), as reproduced by CAclubindia, superseding earlier instructions including Circular No. 9/2015 and Circular No. 7/2023; Taxmann summaries. For tax years from 2026-27, check the corresponding power under the Income-tax Act, 2025. Checked 25 November 2026.")),
    ],
    faqs=[("What is condonation of delay under section 119(2)(b)?", "A power of the CBDT, delegated to senior income tax authorities, to admit a return claiming a refund or carry forward of loss after the time limit has passed, where there was a reasonable cause for the delay and genuine hardship."),
          ("Who can condone delay in filing an ITR with a refund claim?", "Under CBDT Circular No. 11/2024, the Principal Commissioner or Commissioner for claims up to Rs 1 crore for an assessment year, the Chief Commissioner for claims above Rs 1 crore up to Rs 3 crore, and the Principal Chief Commissioner above Rs 3 crore."),
          ("What is the time limit for a condonation of delay application?", "It cannot be entertained beyond five years from the end of the assessment year for which the claim is made. The authority should decide it, as far as possible, within six months from the end of the month in which it is received."),
          ("Can I file an ITR after the deadline to claim a TDS refund?", "If the belated return window has closed, an updated return cannot claim a refund, so the route is an application for condonation of delay under section 119(2)(b), showing reasonable cause and genuine hardship."),
          ("Can a late income tax appeal be condoned?", "Yes. The Commissioner (Appeals) and the Tribunal can admit an appeal filed after the time limit if there was sufficient cause, so file the appeal with a condonation request explaining the delay."),
          ("Can BQP prepare a condonation of delay application?", "Yes. CA Durgesh Chavda can assess whether the claim is worth pursuing, draft the application with evidence, and file the return or appeal once the delay is condoned. " + C)],
    related=[("missed-itr-due-date-21-november-2026-audit-case-what-you-lose-loss-carry-forward-10-iea-80ac.html", "Missed the ITR due date"),
             ("itr-refund-delayed-2026-why-and-what-to-do.html", "ITR refund delays"),
             ("income-tax-appeal-cit-appeals-form-35-form-99-time-limit-30-days-fee-20-percent-pre-deposit-2026.html", "Income tax appeal to CIT(A)"),
             ("itr-u-updated-return-48-months-section-139-8a-india.html", "Updated return (ITR-U)"),
             ("how-to-respond-to-income-tax-notice-india.html", "Responding to an income tax notice")],
    cta_h="Missed a deadline with a refund or loss at stake?", cta_b=C,
    keywords="condonation of delay income tax, condonation of delay section 119(2)(b), condonation of delay in filing ITR, condonation of delay application, CBDT circular 11/2024, late ITR refund claim, carry forward of loss belated return, condonation of delay meaning",
    desc="Condonation of delay under section 119(2)(b): late ITR claiming a refund or loss, CBDT Circular 11/2024 limits (Rs 1 crore / Rs 3 crore), five-year time limit, six-month disposal, reasonable cause and hardship, late appeals.",
    howto={"name": "How to seek condonation of delay for a late ITR", "description": "Under section 119(2)(b).", "steps": [
        {"name": "Confirm the route", "text": "Check that the belated window has closed and a refund or loss is at stake."},
        {"name": "Check the time limit", "text": "Within five years from the end of the assessment year."},
        {"name": "Identify the authority", "text": "By claim size: Rs 1 crore and Rs 3 crore thresholds."},
        {"name": "Draft the application", "text": "Facts, specific reason, evidence and genuine hardship."},
        {"name": "Respond and file", "text": "Answer enquiries, then file the return as directed."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch IA complete")
