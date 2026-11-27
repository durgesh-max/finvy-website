# -*- coding: utf-8 -*-
"""Batch KK (27 Nov 2026): Accounting and bookkeeping services for Indian businesses - what is done monthly and at year-end,
who needs it, and how it works online for anyone searching 'accounting and bookkeeping services near me'.
Demand: sweep ac168 (27 Nov 2026), all 7 markets: "accounting and bookkeeping services near me" (the sweep's only gap); the
site had bookkeeping outsourcing pages for foreign SMBs and overseas accountancy practices, but none for Indian businesses.
User steer 26 Nov 2026: more call bookings / WhatsApp enquiries.
Facts: companies keep books under section 128 of the Companies Act and preserve them for eight years; accounting software of
companies must keep an audit trail (edit log) from 1 April 2023; GST records are kept for 72 months from the due date of the
annual return for the year (section 36 CGST Act); GSTR-2B reconciliation drives input tax credit; TDS on payments deposited
by the 7th of the next month; audit thresholds per the site's audit applicability page. No fees, no office claims (the work
is done online), no statistics, no portal menu paths, never ask for passwords."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 27 November 2026."
SLUG = "accounting-bookkeeping-services-online-india-small-business-gst-tds-reconciliation-mis-year-end-near-me-2026"

C = contact("the business type (proprietorship, partnership, LLP or company), the accounting software you use or none, the monthly volume of sales and purchase invoices, the bank accounts, and whether GST and TDS apply")
PAGES = [dict(
    slug=SLUG,
    title="Accounting and Bookkeeping Services Online for Indian Businesses (2026): Monthly Books, GST and TDS Reconciliation, MIS and Year-End Accounts - If You Are Searching Near Me",
    em="books that match your GST, TDS and bank.",
    kicker="/ Proprietors, firms, LLPs, startups and companies &middot; Monthly bookkeeping, reconciliations and year-end accounts &middot; Updated 2026-11-27",
    lead=("<strong>Good bookkeeping means your books, GST returns, TDS and bank statements tell the same story every month - so the year-end accounts, audit and income tax return are built on numbers that already agree.</strong> "
          "A CA-led bookkeeping service records sales, purchases, expenses and bank entries, reconciles them with GSTR-2B and TDS data, and gives you a monthly picture of profit, cash and dues. "
          "It runs on shared invoices, bank statements and cloud accounting software, so it does not need to be near you."),
    sections=[
        ("/ What an accounting and bookkeeping service covers", "Monthly, quarterly and at year-end.",
         table(["When", "What is done"], [
             ["Every month", "Sales, purchase and expense entries, bank and card reconciliation, receivables and payables ageing"],
             ["Every month", "GST: matching purchase invoices with GSTR-2B so input tax credit is claimed correctly; data for GSTR-1 and GSTR-3B"],
             ["Every month", "TDS on payments identified and deposited by the 7th of the next month; quarterly TDS returns"],
             ["Monthly or quarterly", "MIS: profit and loss, cash flow, dues to and from customers and suppliers"],
             ["Year-end", "Closing entries, depreciation, provisions, trial balance and financial statements ready for audit and the income tax return"]])
         + ul("<strong>Companies:</strong> books under section 128 of the Companies Act, preserved for eight years, in accounting software that keeps an audit trail (edit log).",
              "<strong>GST records:</strong> kept for 72 months from the due date of the annual return for the year.",
              "<strong>Audit-ready:</strong> clean monthly books leave fewer open questions for the statutory or tax audit and the return.",
              "<strong>Your access stays yours:</strong> data can be shared through the software's user access; you never need to send passwords by message.")),
        ("/ How to engage one from anywhere", "Near you, or not.",
         ul("<strong>Online by design:</strong> invoices, bank statements and the accounting file are shared securely; questions are settled on a call or WhatsApp.",
            "<strong>Start with a catch-up if needed:</strong> pending months are brought up to date first, reconciled with GST and bank, before the monthly routine starts.",
            "<strong>Fix the calendar:</strong> a cut-off for sharing documents each month, then GST, TDS and MIS dates.",
            "<strong>Scope sets the cost:</strong> invoice volume, number of bank accounts and entities decide the effort - book a call and we scope it.")
         + call_box("Accounting and bookkeeping", ["Monthly bookkeeping and bank reconciliation",
                                                   "GSTR-2B and input tax credit reconciliation",
                                                   "TDS identification and returns",
                                                   "MIS and cash-flow reporting",
                                                   "Year-end accounts for audit and ITR"],
                    "Business type, software, invoice volume, bank accounts, GST / TDS status.")
         + sources("Companies Act, 2013 (section 128) and the Companies (Accounts) Rules on audit trail; CGST Act, 2017 (section 36); Income-tax Act, 2025 and Income-tax Rules, 2026 on books and TDS; site GST consultant, TDS return and audit applicability guides. Checked 27 November 2026.")),
    ],
    faqs=[("What does an accounting and bookkeeping service include?", "Recording sales, purchases, expenses and bank entries every month, reconciling bank accounts, matching purchase invoices with GSTR-2B for input tax credit, identifying and depositing TDS, preparing monthly or quarterly MIS (profit, cash flow and dues), and closing the books at year-end so the financial statements are ready for audit and the income tax return."),
          ("I am searching for accounting and bookkeeping services near me. Does location matter?", "Not for the work. Invoices, bank statements and the accounting file are shared online, and questions are settled on a call or WhatsApp, so the service works wherever the business is."),
          ("Do small businesses and proprietors need proper books?", "A business whose income or turnover crosses the limits in the income tax law must keep books of account, and any business registered for GST must keep records that support its returns. Even below the limits, monthly books make GST, TDS and the income tax return far easier and help with loans and investors."),
          ("How long must accounting records be kept?", "Companies preserve books for eight years, and GST records are kept for 72 months from the due date of the annual return for the year. Keep invoices, bank statements and the accounting file together for at least that long."),
          ("Can you bring pending months up to date?", "Yes. Pending months are entered and reconciled with GST returns and bank statements first, so any mismatch is found before the year-end, and then the monthly routine starts."),
          ("What should I send to start?", "WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with the business type, the accounting software you use (or none), the monthly volume of sales and purchase invoices, the bank accounts, and whether GST and TDS apply. We suggest the routine and scope it, or book a call.")],
    related=[("gst-consultant-online-india-registration-returns-lut-refund-notice-reply-gstr-9-near-me-2026.html", "GST consultant online"),
             ("tds-return-filing-fy-2026-27-due-dates-form-138-140-144-143-process-late-fee.html", "TDS return filing"),
             ("audit-applicability-india-company-llp-partnership-proprietorship-trust-statutory-tax-audit-limits-2026.html", "Audit applicability"),
             ("india-accounting-bookkeeping-outsourcing-foreign-smb.html", "Bookkeeping for foreign SMBs")],
    cta_h="Want your books kept right every month?", cta_b=C,
    keywords="accounting and bookkeeping services near me, accounting and bookkeeping services india, bookkeeping services online india, accounting services for small business india, gst reconciliation, tds compliance, mis reporting, year end accounts",
    desc="Accounting and bookkeeping services online for Indian businesses: monthly books, bank reconciliation, GSTR-2B and input tax credit matching, TDS by the 7th, MIS and year-end accounts for audit and ITR - for anyone searching accounting and bookkeeping services near me.",
    howto={"name": "How to set up monthly bookkeeping", "description": "From catch-up to routine.", "steps": [
        {"name": "Share the basics", "text": "Business type, software, invoice volume, bank accounts and GST / TDS status."},
        {"name": "Catch up pending months", "text": "Enter and reconcile with GST returns and bank statements."},
        {"name": "Fix the monthly cut-off", "text": "Documents by an agreed date; GST, TDS and MIS dates follow."},
        {"name": "Close the year", "text": "Year-end entries and financial statements for audit and the return."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch KK complete")
