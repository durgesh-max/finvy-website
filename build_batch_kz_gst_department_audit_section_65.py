# -*- coding: utf-8 -*-
"""Batch KZ (28 Nov 2026): GST audit by the department under section 65 - ADT-01 notice, documents, timelines, ADT-02 findings,
paying before a show cause notice, and special audit under section 66.
Demand: 'gst audit notice', 'adt-01 notice', 'gst department audit section 65', 'adt-02', 'gst audit by tax authorities' - on the
site only as a line in the GST notice response page; no dedicated page. High hire intent (a department audit needs a CA to
prepare reconciliations and replies). User steer 26 Nov 2026: more call bookings / WhatsApp enquiries.
Facts (CGST Act section 65 and 66; CGST Rules rule 101 and 102): Commissioner or authorised officer may audit a registered person
at the place of business or in the tax office; notice in Form GST ADT-01 at least fifteen working days before the audit; audit to
be completed within three months from commencement, extendable by the Commissioner for up to six months more; commencement is the
date records are made available or the audit actually begins at the place of business, whichever is later; the registered person
must provide facilities, records and answers; discrepancies are informed and the person may reply; findings in Form GST ADT-02
within thirty days of completion; tax found short leads to proceedings under section 73 / 74 (section 74A from FY 2024-25), and
paying tax and interest before the show cause notice avoids penalty in non-fraud cases (matched to the site DRC-03 page); special
audit under section 66 by a chartered accountant or cost accountant nominated by the Commissioner (ADT-03 / ADT-04), report within
ninety days, extendable by ninety days. No fees, no portal menu paths. advisory_lib.contact() is not used."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources
from build_lib import page, write_page

A.UPDATED = "Last updated: 28 November 2026."
SLUG = "gst-audit-by-department-section-65-adt-01-notice-documents-timeline-adt-02-findings-2026"

C = ("WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with the ADT-01 notice (or ADT-02 findings), the "
     "financial years covered, your GSTR-1, GSTR-3B and GSTR-9 / 9C for those years, and your books. Or book a call directly.")
PAGES = [dict(
    slug=SLUG,
    title="GST Audit by the Department Under Section 65 (2026): ADT-01 Notice, Documents to Keep Ready, Three-Month Timeline, ADT-02 Findings and Paying Before a Notice",
    em="reconcile before they do.",
    kicker="/ GST-registered businesses &middot; Department audit (section 65) and special audit (section 66) &middot; Updated 2026-11-28",
    lead=("<strong>A GST audit under section 65 starts with a notice in Form ADT-01, given at least fifteen working days in advance. "
          "The officer examines your returns, books and tax payments for the years named, must normally finish within three months, and reports findings in Form ADT-02. "
          "Short payments found can be paid with interest before a show cause notice to avoid penalty in non-fraud cases - otherwise they move into demand proceedings.</strong>"),
    sections=[
        ("/ How the audit runs", "Section 65 and rule 101.",
         table(["Step", "Rule"], [
             ["Notice", "Form GST ADT-01, at least fifteen working days before the audit"],
             ["Where", "Your place of business or the tax office"],
             ["Period", "One or more financial years, or part of a year, named in the notice"],
             ["Duration", "Three months from commencement; the Commissioner can extend by up to six months"],
             ["Commencement", "Date records are made available or the audit begins at your premises, whichever is later"],
             ["Discrepancies", "Communicated to you; you can reply with explanations and evidence"],
             ["Findings", "Form GST ADT-02, within thirty days of completion"]])
         + ul("<strong>Special audit (section 66):</strong> where the value or credit is complex, a chartered accountant or cost accountant nominated by the Commissioner can be directed to audit (ADT-03), reporting within ninety days, extendable by ninety days; findings in ADT-04.",
              "<strong>You must cooperate:</strong> provide facilities, records and answers to the officer&rsquo;s questions within the time given.")),
        ("/ Preparing, replying and paying", "Before the findings harden into a demand.",
         ul("<strong>Reconcile first:</strong> GSTR-1 vs GSTR-3B, GSTR-3B vs GSTR-2B input tax credit, books vs returns, e-way bills and e-invoices vs sales, and RCM liabilities - the usual audit points.",
            "<strong>Keep ready:</strong> returns and annual returns, ledgers, invoices, credit and debit notes, contracts, export and LUT documents, and ITC reversal workings.",
            "<strong>Reply to each discrepancy:</strong> agree where it is right, explain with documents where it is not.",
            "<strong>Paying before a notice:</strong> tax and interest paid on an accepted observation before a show cause notice avoids penalty in non-fraud cases (section 73(5) up to FY 2023-24; section 74A from FY 2024-25).",
            "<strong>After ADT-02:</strong> disputed amounts lead to a show cause notice; reply on time and, if a demand order follows, appeal.")
         + call_box("a GST department audit", ["Pre-audit reconciliations",
                                               "Document set for the audit",
                                               "Replies to discrepancies",
                                               "Paying accepted points before a notice",
                                               "Show cause notice and appeal after ADT-02"],
                    "ADT-01 or ADT-02, years covered, returns, annual returns and books.")
         + sources("CGST Act, 2017 (sections 65, 66, 73, 74 and 74A); CGST Rules, 2017 (rules 101 and 102; Forms GST ADT-01 to ADT-04); site GST notice response, DRC-03 voluntary payment, DRC-01B / 01C and GST appeal pages.")),
    ],
    faqs=[("What is a GST audit under section 65?", "An audit of a records of a registered person by the GST department, at the business premises or the tax office, to check that tax, input tax credit and refunds are correct. It starts with a Form ADT-01 notice at least fifteen working days in advance."),
          ("How long does a GST department audit take?", "It must be completed within three months from commencement, and the Commissioner can extend it by up to six months more. Findings are communicated in Form ADT-02 within thirty days of completion."),
          ("What documents are needed for a GST audit?", "Returns and annual returns for the years covered, books of account, invoices, credit and debit notes, contracts, input tax credit records and reversals, export and LUT papers, and e-way bill and e-invoice data, with reconciliations between them."),
          ("What happens after the ADT-02 findings?", "Accepted short payments can be paid with interest before a show cause notice. Points you dispute lead to a show cause notice under section 73, 74 or 74A, which must be answered; a demand order can then be appealed."),
          ("What is a special audit under section 66?", "Where the case is complex, the department can direct a chartered accountant or cost accountant nominated by the Commissioner to audit the records. The report is due within ninety days, extendable by ninety days, and findings are shared in Form ADT-04."),
          ("What should I send to start?", "WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with the ADT-01 or ADT-02, the years covered, your returns and annual returns for those years, and your books. Or book a call directly.")],
    related=[("gst-notice-response-india-asmt-drc-gstr.html", "GST notice reply"),
             ("discovered-gstr-9-shortfall-voluntary-disclosure-urgent-india.html", "Pay GST shortfall through DRC-03 before a notice"),
             ("gst-summons-section-70-inspection-search-section-67-drc-07-gstr-3a-what-to-do-2026.html", "GST summons, inspection and search"),
             ("gst-appeal-apl-01-section-107-time-limit-pre-deposit-format-appellate-authority-2026.html", "GST appeal (APL-01)")],
    cta_h="Received a GST audit notice?", cta_b=C,
    keywords="gst audit notice, adt-01 notice, gst audit section 65, gst department audit, adt-02 findings, gst special audit section 66, documents for gst audit",
    desc="GST audit by the department under section 65: ADT-01 notice fifteen working days ahead, documents to keep ready, three months to complete (extendable six months), ADT-02 findings within thirty days, paying before a notice, special audit under section 66.",
    howto={"name": "How to handle a GST department audit", "description": "From ADT-01 to ADT-02.", "steps": [
        {"name": "Read the ADT-01", "text": "Note the years, place and date of the audit."},
        {"name": "Reconcile", "text": "GSTR-1 vs 3B, 3B vs 2B, books vs returns, e-way bills and e-invoices."},
        {"name": "Answer discrepancies", "text": "Agree what is right; explain the rest with documents."},
        {"name": "Close it out", "text": "Pay accepted points before a notice; contest the rest after ADT-02."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch KZ complete")
