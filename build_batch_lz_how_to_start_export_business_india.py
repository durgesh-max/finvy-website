# -*- coding: utf-8 -*-
"""Batch LZ (28 Nov 2026): How to start an export business in India - business entity, IEC, GST registration and LUT, RCMC, AD code
and customs, export documents, receiving payment (realisation, e-BRC / FIRC), export incentives, and refunds.
Demand: sweep ac246 (28 Nov 2026), all 7 markets: 'how to start export business in india with low investment', 'how to start
business in india with low investment' (coverage 0.40-0.50) - the site's IEC page is written for foreign exporters / importers; no
page for an Indian starting to export. First-time exporters need registrations and GST set up - high hire intent. User steer 26 Nov.
Facts: Importer-Exporter Code (IEC) from DGFT is needed to export or import goods (PAN-based, updated every year between April and
June, otherwise deactivated); GST registration, and exports are zero-rated - export under a Letter of Undertaking (LUT) without IGST
and claim refund of unused credit, or pay IGST and claim refund (site exporter refund page); Registration-cum-Membership Certificate
(RCMC) from the relevant export promotion council for scheme benefits; AD code registration with customs at the port of export for
goods; shipping bill, commercial invoice, packing list, bill of lading or airway bill; payment through banking channels, realised
within nine months under FEMA from 1 October 2026 (12 months if invoiced in rupees) per the site FEMA export rules page; bank
realisation certificates (e-BRC) and FIRA / FIRC; schemes such as RoDTEP and duty drawback for eligible goods; services exporters
need GST, LUT and FEMA compliance but not IEC unless they deal in goods (the site export of services page). No fees, no investment
amounts, no portal menu paths. advisory_lib.contact() is not used."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources
from build_lib import page, write_page

A.UPDATED = "Last updated: 28 November 2026."
SLUG = "how-to-start-export-business-india-iec-gst-lut-rcmc-ad-code-documents-payment-realisation-2026"

C = ("WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with what you plan to export (goods or services, product "
     "and HS code if known), the countries, your business structure (proprietor, partnership, LLP, company), your PAN and GST "
     "status, and how buyers will pay. Or book a call directly.")
PAGES = [dict(
    slug=SLUG,
    title="How to Start an Export Business in India (2026): Entity, IEC, GST Registration and LUT, RCMC, AD Code, Export Documents, Getting Paid and Refunds",
    em="registrations first, first shipment second.",
    kicker="/ First-time exporters, manufacturers, traders and service businesses &middot; Export compliance in India &middot; Updated 2026-11-28",
    lead=("<strong>To export goods from India you need a business set up in your name, an Importer-Exporter Code (IEC) from DGFT, GST registration with a Letter of Undertaking (LUT) to export without paying IGST, and - for scheme benefits - an RCMC from the relevant export promotion council. "
          "Each shipment then moves on a shipping bill through customs, and payment must come through the banking channel within the time FEMA allows. "
          "Services exporters need GST, LUT and FEMA compliance, but not an IEC unless they also deal in goods.</strong>"),
    sections=[
        ("/ The registrations", "Before the first shipment.",
         table(["Registration", "Why", "Key point"], [
             ["Business entity", "Proprietorship, partnership, LLP or company", "Choose with tax, liability and funding in mind"],
             ["IEC (DGFT)", "Needed to export or import goods", "PAN-based; update it every year between April and June or it is deactivated"],
             ["GST registration", "Exports are zero-rated supplies", "Needed to export under LUT and claim refunds"],
             ["Letter of Undertaking (LUT)", "Export without paying IGST", "Filed for each financial year"],
             ["RCMC", "Membership of the export promotion council for your product", "Needed for many scheme benefits"],
             ["AD code with customs", "Links your bank account to the port of export", "Needed for goods shipments and incentives"]])
         + ul("<strong>Services exporters:</strong> software, consulting and other services need GST registration (above the threshold or voluntarily), an LUT and FEMA-compliant receipts - an IEC is not needed for services alone.",
              "<strong>Product rules:</strong> some goods need extra licences (food, drugs, chemicals, restricted items) - check the export policy for your HS code.")),
        ("/ Each shipment, payment and refunds", "Where new exporters slip.",
         ul("<strong>Documents:</strong> commercial invoice, packing list, shipping bill, and bill of lading or airway bill; certificate of origin where the buyer&rsquo;s country needs it.",
            "<strong>Getting paid:</strong> through banking channels into your AD bank account, realised within nine months under FEMA from 1 October 2026 (12 months if invoiced in rupees); keep e-BRC and FIRA / FIRC records.",
            "<strong>GST refunds:</strong> export under LUT and claim refund of unused input tax credit, or pay IGST and claim it back - file within the time limits.",
            "<strong>Incentives:</strong> schemes such as RoDTEP and duty drawback apply to eligible goods; they depend on correct declarations in the shipping bill.",
            "<strong>Income tax:</strong> export income is taxed like other business income; keep proof of every export for audits and notices.")
         + call_box("starting an export business", ["Choosing the business structure",
                                                    "IEC, GST registration and LUT",
                                                    "RCMC and AD code",
                                                    "FEMA realisation and e-BRC tracking",
                                                    "GST refunds and export incentives"],
                    "Product or service, countries, business structure, PAN and GST status, payment method.")
         + sources("Foreign Trade (Development and Regulation) Act, 1992 and the Foreign Trade Policy (IEC, RCMC, RoDTEP); CGST and IGST Acts (zero-rated supplies, LUT, refunds); FEMA (Export of Goods and Services) Regulations; site IEC, FEMA export rules, exporter GST refund and export of services pages.")),
    ],
    faqs=[("How do I start an export business in India?", "Set up a business entity, obtain an Importer-Exporter Code (IEC) from DGFT, register for GST and file a Letter of Undertaking to export without IGST, get an RCMC from the relevant export promotion council for scheme benefits, register your AD code with customs, and then ship on a shipping bill with payment through your bank."),
          ("Is IEC mandatory for exporting from India?", "Yes, for exporting or importing goods. It is PAN-based and must be updated every year between April and June. Exporters of services alone do not need an IEC."),
          ("Do exporters need GST registration?", "Exports are zero-rated supplies, and GST registration lets you export under a Letter of Undertaking without paying IGST and claim refund of input tax credit, or pay IGST and claim it back."),
          ("How long do I have to receive payment for exports?", "Under FEMA, export proceeds must be realised within nine months from 1 October 2026, or 12 months if the invoice is in rupees, through banking channels into your AD bank account."),
          ("What is RCMC and do I need it?", "A Registration-cum-Membership Certificate from the export promotion council for your product. It is needed to claim many Foreign Trade Policy benefits."),
          ("What should I send to start?", "WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with what you plan to export, the countries, your business structure, your PAN and GST status and how buyers will pay. Or book a call directly.")],
    related=[("india-iec-gst-customs-foreign-exporter-importer-2026.html", "IEC, GST and customs for importers and exporters"),
             ("fema-export-rules-1-october-2026-nine-month-realisation-edf-services.html", "FEMA export rules from 1 October 2026"),
             ("gst-refund-for-exporters-igst-paid-or-lut-unused-itc-rfd-01-shipping-bill-time-limit-documents-2026.html", "GST refund for exporters"),
             ("gst-on-export-of-services-lut-without-lut-invoice-format-refund-freelancer-startup-2026.html", "GST on export of services and LUT")],
    cta_h="Planning your first export?", cta_b=C,
    keywords="how to start export business in india, export business registration india, iec registration for export, gst lut for exporters, rcmc export promotion council, ad code registration customs, export payment realisation 9 months",
    desc="How to start an export business in India: business entity, IEC from DGFT (annual update April-June), GST registration and LUT for zero-rated exports, RCMC, AD code with customs, shipping documents, payment realised within nine months under FEMA, e-BRC, GST refunds and incentives.",
    howto={"name": "How to start exporting from India", "description": "Registrations, then shipments.", "steps": [
        {"name": "Set up the business", "text": "Choose the entity; get PAN and a current account."},
        {"name": "Register", "text": "IEC, GST and LUT; RCMC; AD code with customs for goods."},
        {"name": "Ship correctly", "text": "Invoice, packing list, shipping bill, bill of lading or airway bill."},
        {"name": "Get paid and refunded", "text": "Realise within nine months; track e-BRC; claim GST refunds and incentives."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch LZ complete")
