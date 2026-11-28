# -*- coding: utf-8 -*-
"""Batch LD (28 Nov 2026): GST e-invoicing - who must issue e-invoices (INR 5 crore aggregate turnover), which documents, who is
exempt, the 30-day reporting limit for AATO of INR 10 crore and above, IRN cancellation, and consequences of not complying.
Demand: 'e invoicing applicability', 'e invoice limit', 'e invoice 30 days rule', 'is e invoice mandatory', 'e invoice cancel
time limit' - mentioned on three pages but no dedicated page. Businesses crossing the threshold need setup help. User steer
26 Nov 2026: more call bookings / WhatsApp enquiries.
Facts: e-invoicing applies to registered persons whose aggregate turnover in any financial year from 2017-18 exceeded INR 5 crore
(from 1 August 2023); covers B2B tax invoices, credit and debit notes, exports, supplies to SEZs and deemed exports; exempt
classes include SEZ units, insurers, banks, NBFCs and other financial institutions, goods transport agencies, passenger transport
services, admission to multiplex cinemas, and government departments and local authorities; the invoice is reported to an
Invoice Registration Portal (IRP) to get an IRN and signed QR code; an invoice without IRN where e-invoicing applies is not a
valid invoice (rule 48(5)) and the buyer's credit is at risk; 30-day reporting limit: AATO of INR 100 crore and above from
1 November 2023, lowered to AATO of INR 10 crore and above from 1 April 2025 (GSTN advisory of 5 November 2024, verified by web
search 28 Nov 2026); IRN can be cancelled within 24 hours on the IRP (no partial cancellation); e-invoice data flows to GSTR-1
and e-way bill Part A. Penalty under section 122 for invoices not issued as required (no amounts). No fees, no portal menu paths.
advisory_lib.contact() is not used."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources
from build_lib import page, write_page

A.UPDATED = "Last updated: 28 November 2026."
SLUG = "gst-e-invoicing-applicability-5-crore-30-day-reporting-limit-irn-exemptions-cancellation-2026"

C = ("WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with your aggregate turnover for each year since 2017-18, "
     "the type of supplies you make (B2B, exports, SEZ), your billing software, and any invoices issued without IRN or rejected "
     "for being late. Or book a call directly.")
PAGES = [dict(
    slug=SLUG,
    title="GST E-Invoicing (2026): Who Must Issue E-Invoices (INR 5 Crore Turnover), Which Documents, Exemptions, the 30-Day Reporting Limit, IRN Cancellation and Penalties",
    em="once you cross the line, every B2B invoice needs an IRN.",
    kicker="/ Manufacturers, traders, service providers and exporters &middot; GST e-invoicing &middot; Updated 2026-11-28",
    lead=("<strong>If your aggregate turnover crossed INR 5 crore in any financial year since 2017-18, your B2B invoices, credit and debit notes, exports and SEZ supplies must be reported to the Invoice Registration Portal to get an IRN and QR code. "
          "An invoice without an IRN is not a valid invoice, and the buyer&rsquo;s input tax credit is at risk. "
          "If your AATO is INR 10 crore or more, invoices must be reported within 30 days of their date - late ones are rejected by the portal.</strong>"),
    sections=[
        ("/ Who and what is covered", "Applicability, documents and exemptions.",
         table(["Point", "Rule"], [
             ["Threshold", "Aggregate turnover above INR 5 crore in any financial year from 2017-18 (from 1 August 2023)"],
             ["Documents", "Tax invoices, credit notes and debit notes"],
             ["Supplies covered", "B2B, exports, supplies to SEZ units or developers, deemed exports"],
             ["Not covered", "B2C invoices (separate dynamic QR code rules apply to the largest businesses)"],
             ["Exempt classes", "SEZ units, insurers, banks, NBFCs and financial institutions, goods transport agencies, passenger transport, multiplex admission, government departments and local authorities"],
             ["30-day limit", "AATO INR 10 crore and above: report within 30 days of invoice date (from 1 April 2025; INR 100 crore and above since 1 November 2023)"],
             ["Cancellation", "IRN can be cancelled within 24 hours on the IRP; no partial cancellation"]])
         + ul("<strong>Once in, always in:</strong> the test looks at every year since 2017-18, so a single year above the threshold brings you in even if turnover later falls.",
              "<strong>Auto-flow:</strong> e-invoice data populates GSTR-1 and Part A of the e-way bill, which reduces mismatches when set up correctly.")),
        ("/ Getting compliant, and fixing gaps", "Setup, late invoices and notices.",
         ul("<strong>Check applicability now:</strong> compute aggregate turnover (all GSTINs on the same PAN, India-wide) for each year since 2017-18.",
            "<strong>Set up:</strong> generate IRNs through your billing or ERP software, a GST Suvidha Provider, or directly on the IRP, and train staff on the 30-day and 24-hour limits.",
            "<strong>Invoices issued without IRN:</strong> where e-invoicing applied, the invoice is treated as not issued - correct the position with the buyer quickly to protect their credit.",
            "<strong>Rejected for being late:</strong> plan billing so invoices reach the IRP within 30 days; get advice on how to regularise a missed invoice.",
            "<strong>Penalties and notices:</strong> invoices not issued as required attract penalty under section 122; e-invoice gaps also show up in GSTR-1, e-way bill and GSTR-2B mismatches.")
         + call_box("GST e-invoicing", ["Applicability check since 2017-18",
                                        "Exemption review for your business",
                                        "Setup with billing software or GSP",
                                        "Fixing invoices issued without IRN",
                                        "Mismatch notices and penalties"],
                    "Turnover by year, supply types, billing software, any problem invoices.")
         + sources("CGST Act, 2017 (sections 31 and 122); CGST Rules, 2017 (rule 48(4) and 48(5)); CBIC notifications on e-invoicing thresholds and exemptions; GSTN advisory of 5 November 2024 on the 30-day reporting limit; site GST return filing, e-way bill and DRC-01B / 01C pages.")),
    ],
    faqs=[("Who has to issue e-invoices under GST?", "Registered persons whose aggregate turnover exceeded INR 5 crore in any financial year from 2017-18, unless they fall in an exempt class such as SEZ units, insurers, banks and financial institutions, goods transport agencies, passenger transport and government departments."),
          ("Which documents need an e-invoice?", "Tax invoices, credit notes and debit notes for B2B supplies, exports, supplies to SEZs and deemed exports. Invoices to unregistered consumers (B2C) are not reported for IRN."),
          ("What is the 30-day rule for e-invoices?", "Businesses with annual aggregate turnover of INR 10 crore or more must report an invoice to the IRP within 30 days of its date, from 1 April 2025. Later invoices are rejected by the portal. The limit applied to INR 100 crore and above from 1 November 2023."),
          ("What happens if an e-invoice is not generated?", "Where e-invoicing applies, an invoice without an IRN is not a valid invoice, so the buyer's input tax credit is at risk and penalty under section 122 can apply. Correct it with the buyer as soon as possible."),
          ("Can an e-invoice be cancelled?", "Yes, the IRN can be cancelled on the IRP within 24 hours of generation, but only in full. After that, the correction is made through a credit note or an amendment in GSTR-1."),
          ("What should I send to start?", "WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with your turnover by year since 2017-18, your supply types, your billing software and any invoices issued without IRN or rejected as late. Or book a call directly.")],
    related=[("gst-return-filing-2026-due-dates-gstr-1-gstr-3b-qrmp-cmp-08-gstr-9-process-late-fee.html", "GST return filing and due dates"),
             ("e-way-bill-expired-extension-goods-detained-section-129-mov-07-penalty-release-2026.html", "E-way bill expired or goods detained"),
             ("gst-drc-01c-drc-01b-notice-reply-itc-mismatch-gstr-2b-3b-liability-mismatch-gstr-1-3b-rule-88c-88d-2026.html", "DRC-01B / DRC-01C notice reply"),
             ("gst-blocked-credits-section-17-5-itc-on-car-food-insurance-construction-csr-gifts-exceptions-2026.html", "GST blocked credits under section 17(5)")],
    cta_h="Crossed INR 5 crore or getting e-invoices rejected?", cta_b=C,
    keywords="e invoicing applicability, e invoice limit 5 crore, e invoice 30 days rule 10 crore, is e invoice mandatory, e invoice exemption, e invoice cancel 24 hours, irn gst, invoice without irn",
    desc="GST e-invoicing: applies above INR 5 crore aggregate turnover in any year since 2017-18 to B2B invoices, credit / debit notes, exports and SEZ supplies; exemptions; 30-day reporting limit for AATO INR 10 crore and above from 1 April 2025; IRN cancellation within 24 hours; invoices without IRN and penalties.",
    howto={"name": "How to comply with GST e-invoicing", "description": "Check, set up, report on time.", "steps": [
        {"name": "Check applicability", "text": "Aggregate turnover above INR 5 crore in any year since 2017-18, and no exemption."},
        {"name": "Set up IRN generation", "text": "Billing or ERP software, a GSP, or the IRP directly."},
        {"name": "Report on time", "text": "Within 30 days of invoice date if AATO is INR 10 crore or more."},
        {"name": "Fix gaps", "text": "Correct invoices issued without IRN; cancel wrong IRNs within 24 hours."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch LD complete")
