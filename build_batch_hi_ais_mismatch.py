# -*- coding: utf-8 -*-
"""Batch HI (25 Nov 2026): AIS mismatch - what to do when the Annual Information Statement does not match your ITR:
AIS feedback options, when to revise (free until 31 December 2026 for FY 2025-26), belated return, ITR-U for older years,
e-campaign / e-verification communications, 143(1) adjustments, NRI cases.
Demand: sweep ac96 (25 Nov 2026), all 7 markets: "ais mismatch", "ais mismatch communication itd", "itr ais mismatch high
value", "ais mismatch tax filing corrections", "ais mismatch advisory compliance", "is itr mismatch explanation/resolution".
Facts (checked 25 Nov 2026): Income Tax Department AIS pages and FAQs (feedback options: information is correct, not fully
correct, relates to other PAN/year, duplicate, denied; 'income is not taxable' as a custom option for income items; feedback
may be confirmed with the reporting source); Taxmann AIS FAQs; PIB / CBDT e-campaign of 17 December 2024 under the
e-Verification Scheme, 2021 (SMS and email on AIS-ITR mismatches; revise or file belated return by 31 December); site pages
on revised ITR (free to 31 Dec 2026, then fee to 31 Mar 2027), belated ITR and ITR-U."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 25 November 2026."
SLUG = "ais-mismatch-itr-what-to-do-feedback-revised-return-31-december-2026-e-campaign-nri"

C = contact("the tax year, a copy of the AIS entry or the message you received, what you reported in your return, and whether you are resident or NRI")
L = lambda h, t: f'<a href="{h}">{t}</a>'
PAGES = [dict(
    slug=SLUG,
    title="AIS Mismatch With Your ITR (2026): What to Do, AIS Feedback Options, Revised Return by 31 December and Tax Department Messages",
    em="fix the return, not just the statement.",
    kicker="/ Taxpayers and NRIs &middot; Income tax &middot; Updated 2026-11-25",
    lead=("<strong>An AIS mismatch means the Annual Information Statement on the income tax portal shows income or transactions that your return does not.</strong> "
          "Banks, brokers, employers, registrars and buyers of property report to the tax department, and its systems compare that data with your ITR. "
          "A gap can lead to an SMS or email, a reduced refund, an adjustment under section 143(1) or a notice. "
          "If the AIS entry is wrong, give feedback on the portal. If your return is wrong, correct the return: for FY 2025-26 you can revise it without a fee until 31 December 2026."),
    sections=[
        ("/ Quick answers", "What people ask after seeing a mismatch.",
         ul("<strong>Is an AIS mismatch a notice?</strong> Not by itself. It is information the department holds. It can lead to an e-campaign message, a refund adjustment, a section 143(1) intimation or, for large gaps, scrutiny or reassessment.",
            "<strong>The AIS entry is wrong. What do I do?</strong> Open AIS on the e-filing portal and submit feedback on that entry, for example that it is duplicate, belongs to another PAN or year, or is not fully correct. Keep evidence.",
            "<strong>I missed income in my return. What now?</strong> For FY 2025-26, file a revised return; it is free until 31 December 2026 and allowed with a fee until 31 March 2027. For older years, an updated return (ITR-U) with additional tax may be the route.",
            "<strong>Does feedback fix my return?</strong> No. Feedback corrects the information trail; your return must still show the right income.",
            "<strong>I got an SMS or email about a mismatch.</strong> Log in to the e-filing portal and check the compliance section. Do not click links in messages; go to the portal directly.")),
        ("/ AIS feedback options", "Choose the one that matches the facts.",
         table(["Feedback option", "When to use it"], [
             ["Information is correct", "The entry is right and is in your return"],
             ["Information is not fully correct", "The amount or details are partly wrong; enter the correct value"],
             ["Information relates to other PAN or year", "The transaction is not yours, or belongs to another tax year"],
             ["Information is duplicate", "The same transaction appears twice (check records first: two similar entries can be genuine)"],
             ["Information is denied", "You did not undertake the transaction at all"],
             ["Income is not taxable", "Shown for income items, for example exempt income such as NRE interest"]])
         + '<p>The department may confirm your feedback with the bank, broker or other reporting source. See ' + L("form-26as-vs-ais-vs-tis-india-2026.html", "Form 26AS vs AIS vs TIS") + ' for how the statements fit together.</p>'),
        ("/ Fixing the return", "Which route fits which year.",
         table(["Situation", "Route", "Timing"], [
             ["FY 2025-26 return filed, income missed or wrong", L("revised-itr-section-139-5-deadline-31-december-2026-india.html", "Revised return"), "Free until 31 December 2026; with a fee until 31 March 2027"],
             ["FY 2025-26 return not filed", L("belated-itr-31-december-2026-section-139-4-india.html", "Belated return"), "By 31 December 2026, with late fee"],
             ["Earlier years, income missed", L("itr-u-updated-return-48-months-section-139-8a-india.html", "Updated return (ITR-U)"), "Within the updated return window, with additional tax"],
             ["Undisclosed foreign assets or income", L("fast-ds-vs-revised-return-vs-updated-return-itr-u.html", "FAST-DS or revised / updated return"), "FAST-DS declarations by 31 December 2026"],
             ["Adjustment already made in a 143(1) intimation", L("section-143-1-intimation-response-india-2026.html", "Rectification or response"), "As stated in the intimation"]])),
        ("/ Common mismatches", "Where the gaps usually come from.",
         ul("<strong>Savings and deposit interest</strong> left out of the return, or reported on a cash basis while the bank reports on accrual.",
            "<strong>Share and mutual fund sales</strong> where the AIS shows sale value but not cost; the return should show the gain worked out from cost.",
            "<strong>Property sale</strong>: the buyer reports the sale and TDS; NRIs often miss reporting the gain or claiming the exemption.",
            "<strong>NRIs:</strong> NRE interest appearing in AIS (exempt; use 'income is not taxable'), NRO interest and TDS, and income of a family member shown against your PAN.",
            "<strong>Rent, dividends and foreign remittances</strong> reported by tenants, companies and banks.",
            "<strong>Duplicate entries</strong> when one transaction is reported by two sources.")
         + call_box("AIS mismatch or tax department message", ["Line-by-line AIS vs return reconciliation",
                                                               "AIS feedback with evidence",
                                                               "Revised, belated or updated return",
                                                               "Reply on the compliance portal",
                                                               "143(1) rectification and refunds"],
                    "the tax year, the AIS entry or message and your return.")
         + sources("Income Tax Department: Annual Information Statement pages and FAQs (feedback options and processing); Taxmann AIS FAQs; PIB release on the CBDT e-campaign of 17 December 2024 under the e-Verification Scheme, 2021; Income-tax Act provisions on revised, belated and updated returns. Checked 25 November 2026.")),
    ],
    faqs=[("What should I do if my AIS does not match my ITR?", "Find out which side is wrong. If the AIS entry is wrong, submit feedback on it on the e-filing portal with evidence. If your return left out income, correct the return: for FY 2025-26 a revised return is free until 31 December 2026."),
          ("What are the AIS feedback options?", "Information is correct; information is not fully correct; information relates to other PAN or year; information is duplicate; information is denied; and, for income items, income is not taxable."),
          ("Does AIS feedback correct my income tax return?", "No. Feedback corrects the information the department holds, and it may be checked with the reporting source. Your return must still show the correct income, so revise it if it is wrong."),
          ("Can an AIS mismatch lead to a notice?", "Yes. Unresolved mismatches can lead to e-campaign messages, adjustments in a section 143(1) intimation, a reduced refund, or for large or unexplained gaps, scrutiny or reassessment."),
          ("NRE interest shows in my AIS. Is it taxable?", "NRE interest is exempt for an NRI. Choose the feedback 'income is not taxable' for that entry and do not include it as taxable income in the return, but keep account statements as proof."),
          ("Can BQP help resolve an AIS mismatch?", "Yes. CA Durgesh Chavda can reconcile your AIS with your return, file feedback, prepare a revised or updated return and reply on the compliance portal. " + C)],
    related=[("form-26as-vs-ais-vs-tis-india-2026.html", "Form 26AS vs AIS vs TIS"),
             ("revised-itr-section-139-5-deadline-31-december-2026-india.html", "Revised ITR deadline"),
             ("section-143-1-intimation-response-india-2026.html", "Section 143(1) intimation"),
             ("itr-u-updated-return-48-months-section-139-8a-india.html", "ITR-U updated return"),
             ("how-to-respond-to-income-tax-notice-india.html", "Responding to an income tax notice")],
    cta_h="Seen a mismatch or got a message from the tax department?", cta_b=C,
    keywords="AIS mismatch, AIS mismatch with ITR, AIS feedback options, AIS mismatch communication, AIS mismatch revised return, income tax mismatch email, AIS mismatch NRI, NRE interest in AIS",
    desc="AIS mismatch with your ITR (2026): what it means, the six AIS feedback options, when to revise (free until 31 December 2026 for FY 2025-26), belated and updated returns, tax department messages, common NRI mismatches.",
    howto={"name": "How to resolve an AIS mismatch", "description": "When the AIS and your ITR do not agree.", "steps": [
        {"name": "Download AIS and your return", "text": "From the e-filing portal, for the same tax year."},
        {"name": "Reconcile line by line", "text": "Match each AIS entry to bank, broker and employer records."},
        {"name": "Give feedback on wrong entries", "text": "Pick the matching option and keep evidence."},
        {"name": "Correct your return if needed", "text": "Revised return (free until 31 December 2026 for FY 2025-26), belated or updated return."},
        {"name": "Respond to any message", "text": "On the portal's compliance section, within the time given."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch HI complete")
