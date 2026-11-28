# -*- coding: utf-8 -*-
"""Batch LE (28 Nov 2026): GST interest on late payment under section 50 - 18% on delayed tax, interest only on the net cash
liability for late returns, 18% on input tax credit wrongly availed and utilised (rule 88B), how it is computed and paid.
Demand: 'gst interest on late payment', 'gst interest calculation', 'interest on net cash liability', 'interest on wrongly
availed itc' - no dedicated page; mentioned in passing on DRC-03 and return pages. Businesses receive interest demands and
DRC-01 notices. User steer 26 Nov 2026: more call bookings / WhatsApp enquiries.
Facts (CGST Act section 50; CGST Rules rule 88B): interest at 18% a year on tax not paid by the due date, from the day after the
due date until payment; for a return filed late (other than after a section 73 / 74 proceeding), interest is charged only on the
part of tax paid by debiting the electronic cash ledger (net cash liability) - retrospective from 1 July 2017; rule 88B as amended
in 2024 excludes tax deposited in the cash ledger by the due date and used when the late return is filed; interest at 18% on input
tax credit wrongly availed and utilised - utilised when the credit ledger balance falls below the wrongly availed amount - from
1 July 2017; interest is paid in cash, not from the credit ledger; interest (a statutory charge) is separate from the late fee.
No fees, no portal menu paths. advisory_lib.contact() is not used."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources
from build_lib import page, write_page

A.UPDATED = "Last updated: 28 November 2026."
SLUG = "gst-interest-on-late-payment-section-50-18-percent-net-cash-liability-wrong-itc-rule-88b-2026"

C = ("WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with the periods involved, return filing and payment "
     "dates, your cash and credit ledger statements, and any interest demand, DRC-01 or audit observation. Or book a call directly.")
PAGES = [dict(
    slug=SLUG,
    title="GST Interest on Late Payment Under Section 50 (2026): 18% Rate, Interest Only on Net Cash Liability, Wrongly Availed ITC Under Rule 88B, and How to Compute It",
    em="18%, but only on what is really owed.",
    kicker="/ GST-registered businesses and accountants &middot; Interest on delayed tax and wrong credit &middot; Updated 2026-11-28",
    lead=("<strong>Under section 50 of the CGST Act, tax paid after the due date carries interest at 18% a year from the day after the due date until payment. "
          "For a late return, interest is charged only on the part of tax paid in cash (the net cash liability), not on tax set off from input tax credit. "
          "Input tax credit that is wrongly availed attracts 18% interest only if it is utilised.</strong>"),
    sections=[
        ("/ When interest applies, and on what", "Section 50 and rule 88B.",
         table(["Situation", "Interest", "Computed on"], [
             ["Tax paid after the due date (late GSTR-3B)", "18% a year", "Net cash liability only - tax paid by debiting the cash ledger"],
             ["Cash deposited in the cash ledger by the due date, return filed late", "None on that amount", "Excluded under rule 88B as amended in 2024"],
             ["Tax found short in a proceeding under section 73 / 74 / 74A", "18% a year", "The full tax found short"],
             ["Input tax credit wrongly availed but not utilised", "None", "-"],
             ["Input tax credit wrongly availed and utilised", "18% a year", "From utilisation until reversal; utilised when the credit ledger falls below the wrong credit"]])
         + ul("<strong>Period:</strong> from the day after the due date (or date of utilisation) to the date of payment or reversal.",
              "<strong>Paid in cash:</strong> interest cannot be paid from the electronic credit ledger.",
              "<strong>Late fee is separate:</strong> a late fee for the late return applies in addition to interest.")),
        ("/ Computing, paying and disputing", "Getting the figure right.",
         ul("<strong>Compute period by period:</strong> tax paid in cash x 18% x days of delay / 365, for each return filed late.",
            "<strong>Check system-computed figures:</strong> interest suggested in GSTR-3B is based on the data available; verify it against your own working before paying.",
            "<strong>Wrong credit:</strong> reverse wrongly availed credit promptly; compute interest only for the days the credit ledger balance stayed below the wrong credit.",
            "<strong>Interest demands:</strong> where a notice demands interest on gross tax, reply with the net cash and rule 88B working; pay the correct amount through DRC-03.",
            "<strong>Annual reconciliation:</strong> short payments found in GSTR-9 / 9C work also carry interest - pay with the tax to avoid a larger demand later.")
         + call_box("GST interest", ["Period-wise interest computation",
                                     "Net cash and rule 88B working",
                                     "Interest on wrongly availed credit",
                                     "Replies to interest demands and DRC-01",
                                     "Payment through DRC-03"],
                    "Periods, filing and payment dates, ledgers, any demand or notice.")
         + sources("CGST Act, 2017 (section 50, as amended by the Finance Acts, 2021 and 2022); CGST Rules, 2017 (rule 88B, as amended in 2024); site DRC-03, DRC-01B / 01C, GST return filing and GST notice reply pages.")),
    ],
    faqs=[("What is the interest rate on late payment of GST?", "18% a year under section 50 of the CGST Act, from the day after the due date until the tax is paid."),
          ("Is GST interest charged on gross tax or net cash liability?", "For a return filed late, interest is charged only on the tax paid by debiting the electronic cash ledger (the net cash liability), not on tax set off from input tax credit. This applies retrospectively from 1 July 2017, except where tax is paid after a proceeding under section 73 or 74."),
          ("Is there interest if cash was deposited before the due date but the return was filed late?", "Under rule 88B as amended in 2024, tax deposited in the electronic cash ledger by the due date and used when the late return is filed is excluded from interest."),
          ("What is the interest on wrongly availed input tax credit?", "18% a year, but only if the credit is utilised. It is treated as utilised when the electronic credit ledger balance falls below the wrongly availed amount, and interest runs until the credit is reversed."),
          ("Can GST interest be paid from input tax credit?", "No. Interest is paid in cash from the electronic cash ledger, separately from the late fee."),
          ("What should I send to start?", "WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with the periods involved, filing and payment dates, your cash and credit ledger statements, and any interest demand or notice. Or book a call directly.")],
    related=[("discovered-gstr-9-shortfall-voluntary-disclosure-urgent-india.html", "Pay GST shortfall through DRC-03 before a notice"),
             ("gst-return-filing-2026-due-dates-gstr-1-gstr-3b-qrmp-cmp-08-gstr-9-process-late-fee.html", "GST return filing, due dates and late fee"),
             ("gst-blocked-credits-section-17-5-itc-on-car-food-insurance-construction-csr-gifts-exceptions-2026.html", "GST blocked credits under section 17(5)"),
             ("gst-notice-response-india-asmt-drc-gstr.html", "GST notice reply")],
    cta_h="GST interest demand or late returns?", cta_b=C,
    keywords="gst interest on late payment, gst interest calculation, gst interest 18 percent, interest on net cash liability gst, interest on wrongly availed itc, rule 88b gst, section 50 cgst",
    desc="GST interest under section 50: 18% a year on late tax from the day after the due date; only on net cash liability for late returns (retrospective from 1 July 2017); cash deposited by the due date excluded under rule 88B; 18% on wrongly availed ITC only if utilised; paid in cash; separate from late fee.",
    howto={"name": "How to compute GST interest", "description": "Period by period.", "steps": [
        {"name": "List late periods", "text": "Due date, filing date and payment date for each return."},
        {"name": "Take the cash portion", "text": "Tax paid by debiting the cash ledger; exclude cash deposited by the due date."},
        {"name": "Apply 18%", "text": "Cash tax x 18% x days of delay / 365."},
        {"name": "Pay or dispute", "text": "Pay through DRC-03; reply to gross-tax demands with the net cash working."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch LE complete")
