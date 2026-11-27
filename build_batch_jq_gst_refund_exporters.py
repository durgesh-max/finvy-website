# -*- coding: utf-8 -*-
"""Batch JQ (27 Nov 2026): GST refund for exporters - goods and services, with payment of IGST or under LUT.
Demand: sweep ac130 (27 Nov 2026), all 7 markets: "gst refund for exporters", "gst refund for export of services",
"gst refund for export of goods (with / without payment of tax)", "gst refund form for exporters", "lut gst export";
no page title covered export refunds as a whole (the export-of-services page and the rule 96(10) page exist).
User steer 26 Nov 2026: more call bookings / WhatsApp enquiries - refunds usually need a CA.
Facts (verified 27 Nov 2026): exports are zero-rated (section 16 IGST Act); two routes - (1) export with payment of IGST
and claim a refund of the IGST (for goods the shipping bill is treated as the refund application once GSTR-1 export
details and GSTR-3B are filed - rule 96; for services file RFD-01), (2) export under a letter of undertaking (LUT, Form
GST RFD-11, furnished for each financial year) without paying IGST and claim a refund of unused ITC in RFD-01 (rule 89(4)
formula); refund application within two years of the relevant date (section 54(1)); 90% provisional refund for
zero-rated supplies (section 54(6)); order within 60 days of a complete application (section 54(7)); export of services
needs payment in convertible foreign exchange (or INR where RBI permits); rule 96(10) omitted retrospectively (site
page). No fees, no timings beyond the statutory ones, no office claims."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 27 November 2026."
SLUG = "gst-refund-for-exporters-igst-paid-or-lut-unused-itc-rfd-01-shipping-bill-time-limit-documents-2026"

C = contact("your GSTIN, the period, export invoices, shipping bills or service contracts, foreign inward remittance proof (FIRC / e-BRC), GSTR-1, GSTR-3B and GSTR-2B for the period, your LUT acknowledgement if you export without paying IGST, and any refund deficiency memo or notice you have received")
PAGES = [dict(
    slug=SLUG,
    title="GST Refund for Exporters (2026): Refund of IGST Paid on Exports or Unused ITC Under LUT - RFD-01, Shipping Bill Route, Time Limit, Documents and How to Reply to an RFD-08 Show Cause Notice",
    em="pick the route, file in time, match every document.",
    kicker="/ Exporters of goods and services, freelancers and SaaS &middot; Zero-rated supplies &middot; Updated 2026-11-27",
    lead=("<strong>Exports are zero-rated under GST, so an exporter should not end up bearing GST: either you pay IGST on the export and get it refunded, or you export under a letter of undertaking (LUT) without paying IGST and get the unused input tax credit refunded.</strong> "
          "Most refund delays come from mismatches between invoices, shipping bills, GSTR-1 and GSTR-3B, or from missing proof of foreign payment for services. "
          "The application must be made within two years of the relevant date."),
    sections=[
        ("/ The two routes", "With payment of IGST, or under LUT.",
         table(["Route", "How the refund works", "Form"], [
             ["Export of goods with payment of IGST", "The shipping bill is treated as the refund application once the export details are in GSTR-1 and GSTR-3B is filed; mismatches stop it", "Shipping bill (via customs)"],
             ["Export of services with payment of IGST", "Apply for a refund of the IGST paid on the export invoices", "RFD-01"],
             ["Export (goods or services) under LUT", "No IGST is paid; claim a refund of the input tax credit used for the exports, worked out with the rule 89(4) formula", "LUT in RFD-11, refund in RFD-01"]])),
        ("/ Time limits and rules", "What the law says.",
         ul("<strong>Two years:</strong> the refund application must be filed within two years of the relevant date (section 54(1)).",
            "<strong>Provisional refund:</strong> for zero-rated supplies, 90% of the claim can be refunded provisionally (section 54(6)), with the balance after verification.",
            "<strong>Order:</strong> the officer should pass the order within 60 days of a complete application (section 54(7)).",
            "<strong>LUT every year:</strong> the LUT in Form RFD-11 is furnished for each financial year, before exporting without IGST.",
            "<strong>Services:</strong> an export of services needs the payment received in convertible foreign exchange (or in rupees where the RBI permits); keep the FIRC or e-BRC for each invoice.",
            "<strong>Old demands:</strong> rule 96(10) was omitted retrospectively, which helps exporters fighting old IGST refund demands - see our " + '<a href="rule-96-10-omitted-retrospectively-exporters-igst-refund-circular-264-2026.html">rule 96(10) guide</a>' + ".")),
        ("/ Why refunds get stuck", "The usual mismatches.",
         ul("Export invoice values or numbers in GSTR-1 Table 6A not matching the shipping bill.",
            "GSTR-3B not filed, or IGST paid shown differently from GSTR-1.",
            "Missing FIRC / e-BRC for services, or payment received in a way that does not count as export proceeds.",
            "Unused ITC claim not reconciled with GSTR-2B, or turnover figures in the rule 89(4) formula inconsistent with returns.",
            "Deficiency memo (RFD-03) not answered with a corrected fresh application.")
         + call_box("GST export refunds", ["Choosing IGST or LUT for your exports",
                                           "Reconciling GSTR-1, GSTR-3B, shipping bills and 2B",
                                           "Preparing and filing RFD-01 with the statements",
                                           "Replying to deficiency memos and show cause notices",
                                           "Old IGST refund demands after rule 96(10)"],
                    "GSTIN, period, invoices, shipping bills or FIRCs.")
         + sources("CGST Act, 2017 (section 54); IGST Act, 2017 (section 16); CGST Rules (rules 89, 91, 96, RFD-01 / RFD-11); site export-of-services, rule 96(10) and IEC guides. Checked 27 November 2026.")),
    ],
    faqs=[("How do exporters get a GST refund?", "Either export with payment of IGST and claim it back (for goods the shipping bill works as the refund application once GSTR-1 and GSTR-3B are filed; for services file RFD-01), or export under an LUT without paying IGST and claim a refund of the unused input tax credit in RFD-01."),
          ("Is there GST on exports?", "Exports are zero-rated: you either pay IGST and get it refunded, or export under an LUT without paying IGST. Either way the exporter should not finally bear GST, provided the conditions and paperwork are in order."),
          ("What is the time limit for a GST export refund?", "The refund application must be filed within two years of the relevant date under section 54(1) of the CGST Act. For zero-rated supplies, 90% can be refunded provisionally, and the officer should pass the order within 60 days of a complete application."),
          ("How do I file an LUT for exports under GST?", "File Form GST RFD-11 on the GST portal for each financial year before exporting without paying IGST. With an LUT you then claim a refund of the unused input tax credit, not of IGST."),
          ("Why is my GST export refund stuck?", "Usually a mismatch: invoice details in GSTR-1 not matching the shipping bill, GSTR-3B not filed or inconsistent, missing FIRC / e-BRC for services, or ITC figures not matching GSTR-2B. A deficiency memo needs a corrected fresh application."),
        ("How do I reply to a GST refund show cause notice in Form RFD-08?", "Under rule 92(3) of the CGST Rules, an officer who thinks all or part of a refund is not admissible must first issue a notice in Form RFD-08, and you reply in Form RFD-09 within fifteen days of receiving it (or any other period the notice allows). Answer each ground point by point with the supporting documents - shipping bills, export invoices, bank realisation, the LUT, the ITC working - and ask for a personal hearing. The officer then passes a reasoned order in RFD-06, and a refund cannot be rejected without giving you a hearing. File the reply before the order is issued, as the portal does not accept an RFD-09 once an RFD-06 has been passed; if the claim is still rejected, the remedy is an appeal in APL-01."),
        ("What should I send to reply to an RFD-08 refund notice?", "WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with the RFD-08 notice, the refund application (RFD-01) and its acknowledgement, the shipping bills and export invoices, bank realisation or FIRC records, your LUT, and the ITC or turnover working you used. We draft the RFD-09 reply ground by ground, attend the hearing and, if needed, file the appeal. You keep your own GST login."),
          ("What should I send to claim a GST export refund?", "WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with your GSTIN and period, export invoices, shipping bills or service contracts, FIRCs / e-BRCs, GSTR-1, GSTR-3B and GSTR-2B, your LUT acknowledgement if you export without IGST, and any deficiency memo or notice. We reconcile the figures, pick the route and prepare the refund claim."),
          ("Can BQP handle GST refunds for my export business?", "Yes. CA Durgesh Chavda works online with exporters of goods and services, freelancers and SaaS companies. " + C)],
    related=[("gst-on-export-of-services-lut-without-lut-invoice-format-refund-freelancer-startup-2026.html", "GST on export of services and LUT"),
             ("rule-96-10-omitted-retrospectively-exporters-igst-refund-circular-264-2026.html", "Rule 96(10) omitted: old IGST refund demands"),
             ("india-iec-gst-customs-foreign-exporter-importer-2026.html", "IEC registration and customs"),
             ("gst-intermediary-services-export-section-13-8-b-omitted-30-march-2026.html", "Intermediary services now exports"),
             ("gst-notice-response-india-asmt-drc-gstr.html", "GST notice reply")],
    cta_h="Export refund stuck or not yet filed?", cta_b=C,
    keywords="gst refund for exporters, gst refund for export of services, gst refund for export of goods, gst refund with payment of igst, gst refund without payment of tax lut, rfd-01 export refund, lut gst export, gst export refund time limit",
    desc="GST refund for exporters: the two routes (refund of IGST paid on exports, or unused ITC under an LUT), RFD-01 and the shipping bill route, the two-year time limit, 90% provisional refund, the 60-day order rule, and why refunds get stuck.",
    howto={"name": "How to claim a GST refund on exports", "description": "From choosing the route to the refund order.", "steps": [
        {"name": "Choose the route", "text": "Pay IGST on exports, or file an LUT (RFD-11) for the year and export without IGST."},
        {"name": "Match the returns", "text": "Report exports in GSTR-1 and file GSTR-3B so they match invoices and shipping bills."},
        {"name": "File the refund", "text": "Goods with IGST: shipping bill route; services or LUT: file RFD-01 with the statements."},
        {"name": "Follow up", "text": "Answer any deficiency memo or notice within the time given."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch JQ complete")
