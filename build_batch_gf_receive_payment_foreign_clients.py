# -*- coding: utf-8 -*-
"""Batch GF (24 Nov 2026): how freelancers, agencies and startups in India receive payments from foreign clients -
channels, RBI purpose codes, FIRA/FIRC, the 2026 export declaration (EDF) rules, realisation period, GST and income tax.
Call-first page.
Demand: sweep ac54 (24 Nov 2026), all 7 markets: "how to receive payment from international clients in india", "how to
receive international payments in india", "how to get payment from foreign client in india", "purpose code for export of
services", "purpose code for export of software services", "firc for freelancers".
Facts (checked 24 Nov 2026):
- RBI purpose codes for receipts: P0802 software implementation/consultancy (other than those covered by the software
  export form), P0807 off-site software exports, P1006 business and management consultancy and PR (RBI list; HDFC;
  Cashfree; Razorpay). Other service codes in the RBI list include P1005 accounting/auditing/tax, P1007 advertising, P1008
  research and development, P1009 architectural, engineering and other technical services. Bank confirms the code.
- FEMA (Export and Import of Goods and Services) Regulations, 2026 from 1 October 2026: service exports declared in the EDF;
  deemed filed for individuals and for companies up to INR 10 lakh per service (Second Amendment, 2 November 2026);
  realisation within nine months (site page).
- GST: export of services zero-rated with LUT; payment in convertible foreign exchange is a condition; bank advice / FIRA
  is the proof (site GST export page). Income tax: export income taxable as business/professional income."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 24 November 2026."
SLUG = "how-to-receive-payment-from-foreign-clients-in-india-purpose-code-fira-firc-gst-2026"

C = contact("what you sell, where your clients are, how you are paid today (bank, PayPal, Wise or another platform), your annual receipts, and whether you are an individual or a company")
L = lambda h, t: f'<a href="{h}">{t}</a>'
PAGES = [dict(
    slug=SLUG,
    title="How to Receive Payment From Foreign Clients in India (2026): Bank or Platform, Purpose Codes, FIRA/FIRC, GST and Tax",
    em="get paid properly once, and GST, FEMA and tax line up.",
    kicker="/ Freelancers and startups &middot; Export of services &middot; Updated 2026-11-24",
    lead=("<strong>Freelancers, agencies and startups in India can receive foreign client payments by SWIFT wire into a bank account or through a payment platform that pays out to an Indian bank; either way the money must arrive as an export receipt with the right RBI purpose code.</strong> "
          "Common codes are <strong>P0802</strong> (software implementation or consultancy), <strong>P0807</strong> (off-site software exports) and <strong>P1006</strong> (business and management consultancy); your bank confirms the code. "
          "Keep the <strong>FIRA</strong> (foreign inward remittance advice) or FIRC for each payment: it proves the export for GST and the bank. "
          "Under the 2026 FEMA export rules, service exports are declared in an <strong>EDF</strong>, which is <strong>deemed filed for individuals</strong> and for companies up to INR 10 lakh per service, and money should come in within <strong>nine months</strong>. "
          "No GST is charged on exports under an LUT, but the income is taxable."),
    sections=[
        ("/ Quick answers", "What people starting to bill abroad ask.",
         ul("<strong>How do I receive payment from a foreign client in India?</strong> Give the client your bank&rsquo;s SWIFT details and account, or use a payment platform that collects in foreign currency and pays out to your Indian account. Tell the bank or platform the purpose of the payment.",
            "<strong>Which purpose code for export of services?</strong> It depends on the service: P0802 for software implementation or consultancy, P0807 for off-site software exports, P1006 for business and management consultancy, P1005 for accounting and tax services, P1009 for engineering and technical services. Confirm with your bank.",
            "<strong>What is FIRC or FIRA?</strong> The bank&rsquo;s record that foreign currency came in for a stated purpose: FIRA is the per-transaction advice; a FIRC is the certificate some banks issue on request. Platforms issue their own equivalent. Keep them for GST and audits.",
            "<strong>Do I pay GST on foreign client payments?</strong> No GST on a valid export of services: register (if above the threshold) and file an LUT to invoice without GST. Below INR 20 lakh a year you need not register.",
            "<strong>Is the income taxable?</strong> Yes, as business or professional income in your Indian return; freelancers may use presumptive taxation where eligible.")),
        ("/ Purpose codes", "Common RBI codes for service receipts.",
         table(["Code", "Use it for"], [
             ["P0802", "Software implementation or consultancy (other than work declared as software exports)"],
             ["P0807", "Off-site software exports: development, SaaS, maintenance delivered remotely"],
             ["P0803", "Database and data processing charges"],
             ["P1005", "Accounting, auditing, bookkeeping and tax consulting"],
             ["P1006", "Business and management consultancy and public relations"],
             ["P1007", "Advertising and market research"],
             ["P1008", "Research and development services"],
             ["P1009", "Architectural, engineering and other technical services"]])
         + '<p>The wrong code can make the bank treat a payment as something else (a gift or a loan), which causes trouble with GST refunds and tax. Ask the bank to correct it promptly if the code is wrong.</p>'),
        ("/ Bank or platform", "Choosing how to get paid.",
         ul("<strong>Bank wire (SWIFT):</strong> best for larger invoices and companies; the bank issues FIRA and applies the purpose code; watch correspondent bank charges.",
            "<strong>Payment platforms:</strong> convenient for freelancers and card payments from clients; they convert and pay out to your Indian account and issue an inward remittance advice. Money held in a platform balance abroad can be a foreign asset to report in Schedule FA; see " + L("wise-payoneer-paypal-revolut-balance-schedule-fa-freelancer-fast-ds.html", "platform balances and Schedule FA") + ".",
            "<strong>Invoice in foreign currency</strong> with the client&rsquo;s name, country and the service; for GST, include the export endorsement under LUT; see " + L("gst-on-export-of-services-lut-without-lut-invoice-format-refund-freelancer-startup-2026.html", "GST on export of services") + ".",
            "<strong>FEMA:</strong> realise payment within nine months; the EDF is deemed filed for individuals and small receipts; see " + L("fema-services-export-edf-relief-freelancers-10-lakh-rbi-amendment-2-november-2026.html", "the EDF relief") + ".",
            "<strong>US clients</strong> usually ask for Form W-8BEN; see " + L("us-company-paying-indian-contractor-w-8ben-no-1099-gst-lut-pe-risk-2026.html", "US company paying an Indian contractor") + ".")
         + call_box("receiving payments from foreign clients", ["Purpose codes and bank documentation",
                                                                 "GST registration and LUT",
                                                                 "FEMA realisation and EDF",
                                                                 "Income tax and presumptive scheme",
                                                                 "Platform balances and Schedule FA"],
                    "what you sell, your clients' countries, how you are paid and your annual receipts.")
         + sources("RBI purpose codes for reporting foreign exchange transactions (receipts), as published by banks including HDFC and DBS; Cashfree and Razorpay guides to purpose codes; Foreign Exchange Management (Export and Import of Goods and Services) Regulations, 2026 and Second Amendment Regulations (FEMA 23(R)/(2)/2026-RB, 2 November 2026); IGST Act section 2(6) and LUT rules; Income-tax Act provisions on business and professional income. Checked 24 November 2026.")),
    ],
    faqs=[("How do I receive payment from international clients in India?", "Through a SWIFT wire into your Indian bank account or a payment platform that collects in foreign currency and pays out to your Indian account. Make sure the payment is tagged with the correct RBI purpose code and keep the FIRA for each payment."),
          ("What is the purpose code for export of services?", "It depends on the service: P0802 for software implementation or consultancy, P0807 for off-site software exports, P1006 for business and management consultancy, P1005 for accounting and tax services and P1009 for engineering and technical services. Your bank confirms the code."),
          ("What is the purpose code for software export?", "P0807 is used for off-site software exports such as remotely delivered development and SaaS; P0802 is used for software implementation or consultancy. Ask your bank which applies to your invoice."),
          ("Do freelancers need a FIRC?", "Freelancers should keep the bank's FIRA (foreign inward remittance advice) or a FIRC for each foreign payment. It proves the export for GST, supports zero-rating and is useful for income tax and audits."),
          ("What is a foreign inward remittance certificate (FIRC), and how is it different from a FIRA?", "Both are bank documents that prove foreign currency reached your Indian account. A FIRA (foreign inward remittance advice) is the credit advice most banks and payment platforms issue for each incoming payment, showing the sender, the amount in foreign currency, the rupee amount credited, the date and usually the purpose code. A FIRC (foreign inward remittance certificate) is a signed certificate the bank issues on request, often covering one or several remittances. For a freelancer or exporter of services, either is evidence that the payment came in convertible foreign exchange - which is what GST zero-rating and an export refund rely on - and it also supports the income tax return and any bank or audit query. Ask your bank or platform for it each month rather than at year-end, and check that the purpose code matches the service on your invoice. WhatsApp +91 78018 87130 with how you are paid (bank wire, PayPal, Wise or another platform), a sample FIRA and your GST status, or book a call."),
          ("Is GST payable on payments from foreign clients?", "Not on a valid export of services. Below INR 20 lakh of turnover a year you need not register; above it, register and file an LUT to invoice without GST."),
          ("Can BQP set up my foreign payments, GST and tax?", "Yes. " + C)],
    related=[("gst-on-export-of-services-lut-without-lut-invoice-format-refund-freelancer-startup-2026.html", "GST on export of services"),
             ("fema-services-export-edf-relief-freelancers-10-lakh-rbi-amendment-2-november-2026.html", "FEMA EDF relief for service exports"),
             ("wise-payoneer-paypal-revolut-balance-schedule-fa-freelancer-fast-ds.html", "Platform balances and Schedule FA"),
             ("freelancer-consultant-tax-india-2026-complete.html", "Tax for freelancers and consultants"),
             ("us-company-paying-indian-contractor-w-8ben-no-1099-gst-lut-pe-risk-2026.html", "US company paying an Indian contractor")],
    cta_h="Getting paid by clients abroad?", cta_b=C,
    keywords="how to receive payment from foreign clients in India, how to receive international payments in India, purpose code for export of services, purpose code for software export P0807, P0802 purpose code, FIRC for freelancers, FIRA, EDF service export 2026",
    desc="How to receive payment from foreign clients in India (2026): bank wire or payment platform, RBI purpose codes (P0802, P0807, P1006 and others), FIRA/FIRC, the 2026 EDF rules and nine-month realisation, GST with LUT and income tax for freelancers and startups.",
    howto={"name": "How to receive a payment from a foreign client in India", "description": "Steps from invoice to tax.", "steps": [
        {"name": "Invoice in foreign currency", "text": "Client name, country, service; GST export endorsement under LUT if registered."},
        {"name": "Share bank or platform details", "text": "SWIFT details or a platform that pays out to your Indian account."},
        {"name": "Confirm the purpose code", "text": "For example P0802, P0807 or P1006, with your bank."},
        {"name": "Keep the FIRA", "text": "For each payment, as export proof."},
        {"name": "Report correctly", "text": "GST returns as zero-rated supply; income in your Indian return."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch GF complete")
