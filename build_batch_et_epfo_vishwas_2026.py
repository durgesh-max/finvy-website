# -*- coding: utf-8 -*-
"""Batch ET (21 Nov 2026): EPFO VISHWAS 2026 - one-time window to settle damages for delayed provident fund payments at
reduced rates, closing 28 December 2026. Deadline-led, call-first page for employers and foreign-owned subsidiaries.
Facts (checked 21 Nov 2026; Angel One news, 11 Nov 2026; corroborated by search summaries of Ujjivan SFB, IncorpX and
CorpLawUpdates): VISHWAS 2026 opened 29 June 2026 for six months; applications until 28 December 2026 (some EPFO
communications cite 29 December); EPFO has said the deadline will not be extended; Ministry of Labour notice of
3 September 2026; covers delays in PF payments made before 14 June 2024; regular damages can go up to 37% a year;
scheme rates - 0.25% a month for delays up to two months, 0.50% a month for two to four months, 1% a month beyond four
months; covered - damages proceedings pending before a court or tribunal, damages order passed but not (fully)
recovered, notice issued without final order, delayed payments on EPFO record without a notice; apply on the EPFO
Employer Portal after clearing outstanding interest on the delayed contributions; portal computes the amount; 15 days
to pay with an automatic further 15 days; digitally signed settlement certificate; pending proceedings closed; VISHWAS
cells at 153 regional offices. Employees' Enrolment Campaign 2026 (left-out employees, 1 April 2009 to 31 March 2026,
INR 100 lump-sum damages) ran 1 July to 31 October 2026 and is closed (PIB release; search summaries)."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 21 November 2026."
SLUG = "epfo-vishwas-2026-pf-damages-settlement-reduced-rates-last-date-28-december-2026"
EPF = "epf-scheme-2026-changes-employers-foreign-subsidiaries-nri-withdrawal-12-months-wages-definition"

C = contact("your establishment's PF code, the months paid late and when, any damages notice or order received, and whether a case is pending")
PAGES = [dict(
    slug=SLUG,
    title="EPFO VISHWAS 2026: Settle Old Provident Fund Damages at Reduced Rates - Last Date 28 December 2026",
    em="a one-time window for employers with late PF payments before 14 June 2024.",
    kicker="/ Payroll &middot; Provident fund &middot; Deadline 28 December 2026 &middot; Updated 2026-11-21",
    lead=("<strong>VISHWAS 2026</strong> is a one-time EPFO scheme that lets employers settle <strong>damages for provident fund contributions paid late before 14 June 2024</strong> at much lower rates. "
          "Applications close on <strong>28 December 2026</strong>, and EPFO has said the date will not be extended. "
          "Regular damages can run up to 37% a year. Under the scheme they are <strong>0.25% a month</strong> for delays of up to two months, <strong>0.50% a month</strong> for two to four months and <strong>1% a month</strong> beyond four months. "
          "It covers cases pending in a court or tribunal, damages orders not yet recovered, notices without a final order, and late payments on EPFO&rsquo;s record where no notice has been issued. "
          "You apply on the <strong>EPFO Employer Portal</strong> after paying the interest due on the late contributions, pay the computed amount within 15 days and receive a settlement certificate. Pending proceedings are then closed. "
          "The separate enrolment campaign for left-out employees closed on 31 October 2026."),
    sections=[
        ("/ The scheme at a glance", "Rates, coverage and dates.",
         table(["Point", "VISHWAS 2026"], [
             ["Who", "Employers with provident fund contributions paid late where the delayed payment was made before 14 June 2024"],
             ["Reduced damages", "0.25% a month (delay up to 2 months); 0.50% a month (2 to 4 months); 1% a month (over 4 months)"],
             ["Compared with", "Regular damages of up to 37% a year"],
             ["Cases covered", "Proceedings pending in a court or tribunal; damages order passed but not fully recovered; notice issued without a final order; late payments on EPFO record with no notice yet"],
             ["Condition", "Pay the outstanding interest on the late contributions first"],
             ["How", "EPFO Employer Portal: choose the category, upload documents, authenticate; the portal computes the amount"],
             ["Payment", "Within 15 days, with an automatic further 15 days"],
             ["Result", "Digitally signed settlement certificate; pending proceedings closed"],
             ["Last date", "28 December 2026 (some EPFO communications say 29 December); no extension expected"]])
         + call_box("Settling old PF damages before 28 December", ["Whether your late payments fall within the scheme",
                                                                  "The interest to clear first and the reduced damages to pay",
                                                                  "Pending notices, orders or tribunal cases and how settlement closes them",
                                                                  "Payroll changes under the EPF Scheme 2026 so delays do not recur",
                                                                  "For foreign-owned subsidiaries: reporting the exposure to the parent"],
                    "your PF code, challan history or EPFO damages statement, and any notices or orders.")),
        ("/ What to do before 28 December", "Steps for employers.",
         ul("<strong>List the delays:</strong> download the challan history and identify months paid after the due date where payment was made before 14 June 2024.",
            "<strong>Check for notices:</strong> gather any damages notices, orders, recovery letters and case papers.",
            "<strong>Clear interest:</strong> pay the outstanding interest on the delayed contributions; the scheme module opens only after that.",
            "<strong>Apply online:</strong> pick the right category on the Employer Portal and upload the documents; do not leave it to the last week.",
            "<strong>Pay and keep the certificate:</strong> pay within the 15-day window and file the settlement certificate with your statutory records.",
            "<strong>Fix the cause:</strong> review payroll and due dates under the new scheme; see <a href=\"" + EPF + ".html\">what the EPF Scheme 2026 changed</a>.")
         + '<p>Related: <a href="foreign-company-india-subsidiary-employee-benefits-payroll-epf-esic-gratuity-2026.html">payroll and benefits for an Indian subsidiary</a> &middot; <a href="foreign-owned-indian-subsidiary-annual-compliance-calendar-fy-2026-27.html">compliance calendar for foreign-owned subsidiaries</a> &middot; <a href="deadline-desk-20-november-2026-to-31-january-2027-income-tax-gst-roc-nri-foreign-companies.html">deadline desk to 31 January 2027</a>.</p>'
         + sources("EPFO VISHWAS 2026 scheme (notified with the EPF Scheme, 2026 on 29 June 2026) and the Ministry of Labour and Employment notice of 3 September 2026, as reported by Angel One (11 November 2026) and other summaries; PIB release on the Employees' Enrolment Campaign 2026 (closed 31 October 2026). Confirm the closing date and your eligible periods on the EPFO Employer Portal.")),
    ],
    faqs=[("What is the last date for EPFO VISHWAS 2026?", "28 December 2026 (some EPFO communications mention 29 December). EPFO has said the deadline will not be extended."),
          ("What are the reduced damages under VISHWAS 2026?", "0.25% a month for delays of up to two months, 0.50% a month for delays of two to four months and 1% a month for longer delays, against regular damages of up to 37% a year."),
          ("Which PF defaults are covered by VISHWAS 2026?", "Delayed provident fund payments made before 14 June 2024, whether a case is pending in a court or tribunal, an order is unrecovered, a notice has been issued, or the delay is only on EPFO's record."),
          ("How does an employer apply for VISHWAS 2026?", "On the EPFO Employer Portal, after paying the outstanding interest on the late contributions: choose the category, upload documents, authenticate, pay the computed amount within 15 days and download the settlement certificate."),
          ("Is the Employees' Enrolment Campaign 2026 still open?", "No. The campaign for enrolling left-out employees ran from 1 July to 31 October 2026 and has closed."),
          ("Can BQP help with a VISHWAS 2026 application?", "Yes. " + C)],
    related=[(EPF + ".html", "EPF Scheme 2026: what changed"),
             ("foreign-company-india-subsidiary-employee-benefits-payroll-epf-esic-gratuity-2026.html", "Payroll and benefits for an Indian subsidiary"),
             ("deadline-desk-20-november-2026-to-31-january-2027-income-tax-gst-roc-nri-foreign-companies.html", "Deadline desk to 31 January 2027")],
    cta_h="Late PF payments in past years?", cta_b=C,
    keywords="EPFO VISHWAS 2026, VISHWAS 2026 last date, PF damages reduced rate, section 14B damages settlement, EPFO damages 0.25% 0.5% 1% per month, PF late payment penalty settlement 2026, EPFO employer portal VISHWAS",
    desc="EPFO VISHWAS 2026: settle damages for PF paid late before 14 June 2024 at 0.25%, 0.50% or 1% a month instead of up to 37% a year. Covers pending cases, orders and notices. Apply on the Employer Portal by 28 December 2026; no extension expected.",
    howto={"name": "How to settle PF damages under VISHWAS 2026", "description": "Before 28 December 2026.", "steps": [
        {"name": "Identify late payments", "text": "Months paid late where payment was made before 14 June 2024."},
        {"name": "Collect notices and orders", "text": "Damages notices, orders and any case papers."},
        {"name": "Pay outstanding interest", "text": "Clear interest on the delayed contributions."},
        {"name": "Apply on the Employer Portal", "text": "Choose the category, upload documents and authenticate."},
        {"name": "Pay and download the certificate", "text": "Pay within 15 days and keep the settlement certificate."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch ET complete")
