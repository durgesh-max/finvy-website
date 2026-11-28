# -*- coding: utf-8 -*-
"""Batch MG (29 Nov 2026): Deemed exports under GST - section 147, the four notified supplies (Notification 48/2017-Central Tax),
GST is paid (not zero-rated), who can claim the refund (recipient, or supplier where the recipient does not take credit),
documents (Notification 49/2017-Central Tax), the two-year time limit, how deemed exports differ from SEZ supplies and from the
0.1% concessional rate on supplies to merchant exporters (Notifications 40/2017-Central Tax (Rate) and 41/2017-Integrated Tax
(Rate)), and the link to Advance Authorisation, EPCG and EOUs.
Demand: sweep ac268 (29 Nov 2026), all 7 markets: 'deemed export gst', 'deemed export under gst', 'deemed export gst rate',
'... rate 0.1', 'deemed export gst refund', 'deemed export gst notification', 'deemed export gst percentage' (coverage
0.50); EOU / Advance Authorisation queries (0.20-0.50). Only passing mentions on the site. Exporters and suppliers to EOUs /
Advance Authorisation holders need refund and documentation help. User steer 26 Nov 2026: more call bookings.
Facts: section 147 CGST Act lets the government notify supplies of goods manufactured in India that do not leave India as
deemed exports; Notification 48/2017-Central Tax notifies (1) supply of goods against an Advance Authorisation, (2) supply of
capital goods against an EPCG authorisation, (3) supply of goods to an Export Oriented Unit (EOU), and (4) supply of gold by a
bank or specified public sector undertaking against an Advance Authorisation; tax is charged and paid on deemed exports; refund
of the tax paid can be claimed by the recipient or, where the recipient does not avail input tax credit and undertakes not to
claim refund, by the supplier (rule 89(1)); evidence under Notification 49/2017-Central Tax; relevant date for the two-year
limit is the date of furnishing the return relating to the deemed exports (section 54); supplies to SEZ units / developers are
zero-rated under section 16 IGST Act, not deemed exports; the 0.1% concessional rate applies to supplies by a registered supplier
to a registered merchant exporter subject to conditions including export within 90 days of the invoice - a separate concession,
not deemed exports. No duty-credit rates, no fees, no portal menu paths. advisory_lib.contact() is not used."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources
from build_lib import page, write_page

A.UPDATED = "Last updated: 29 November 2026."
SLUG = "deemed-exports-under-gst-notification-48-2017-refund-advance-authorisation-eou-epcg-0-1-percent-merchant-export-2026"

C = ("WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with whether you are the supplier or the recipient, "
     "the scheme involved (Advance Authorisation, EPCG, EOU or merchant export), the invoices and periods, whether the recipient "
     "has taken input tax credit, and any deficiency memo received. Or book a call directly.")
PAGES = [dict(
    slug=SLUG,
    title="Deemed Exports Under GST (2026): Notified Supplies Under Notification 48/2017, Who Claims the Refund, Documents, and the 0.1% Rate for Merchant Exporters",
    em="tax is paid first, then refunded - by the right party.",
    kicker="/ Manufacturers supplying EOUs and Advance Authorisation or EPCG holders, merchant exporters &middot; GST deemed exports &middot; Updated 2026-11-29",
    lead=("<strong>Deemed exports are notified supplies of goods made in India that never leave India - supplies against an Advance Authorisation, capital goods against an EPCG authorisation, supplies to an Export Oriented Unit, and gold supplied by banks against an Advance Authorisation. "
          "Unlike real exports they are not zero-rated: GST is charged and paid, and the recipient - or the supplier, if the recipient does not take the credit - claims a refund. "
          "The 0.1% rate on supplies to merchant exporters is a separate concession.</strong>"),
    sections=[
        ("/ What counts and how it works", "Section 147 and Notification 48/2017-Central Tax.",
         table(["Point", "Position"], [
             ["Notified deemed exports", "Goods against Advance Authorisation; capital goods against EPCG; goods to an EOU; gold by a bank or specified PSU against Advance Authorisation"],
             ["Tax on the supply", "GST is charged and paid - not zero-rated"],
             ["Who claims refund", "The recipient; or the supplier where the recipient does not take input tax credit and undertakes not to claim refund"],
             ["Documents", "Evidence under Notification 49/2017-Central Tax, including acknowledgment of receipt and undertakings on credit and refund"],
             ["Time limit", "Two years from the date of filing the return relating to the deemed export supplies"],
             ["Supplies to SEZ units", "Zero-rated under section 16 IGST Act - not deemed exports"]])
         + ul("<strong>Choose who claims early:</strong> supplier and recipient should agree in writing who will take the refund, so credit is not taken twice or lost.",
              "<strong>Scheme records:</strong> the Advance Authorisation, EPCG authorisation or EOU approval details should appear on the invoice and match the recipient&rsquo;s records.")),
        ("/ The 0.1% merchant export rate", "A concession, not deemed exports.",
         ul("<strong>What it is:</strong> a registered supplier can charge a concessional 0.1% GST on goods supplied to a registered merchant exporter (Notifications 40/2017-Central Tax (Rate) and 41/2017-Integrated Tax (Rate)).",
            "<strong>Key condition:</strong> the merchant exporter must export the goods within 90 days of the tax invoice, with the other conditions in the notifications (purchase order copy to the supplier&rsquo;s officer, goods moved to the port or warehouse, shipping bill details shared).",
            "<strong>If export does not happen in time:</strong> the concession is lost and tax at the normal rate becomes payable.",
            "<strong>DGFT schemes:</strong> Advance Authorisation, EPCG and EOU status come from the foreign trade policy; export incentives such as RoDTEP run separately from GST refunds.",
            "<strong>Refund problems:</strong> mismatched invoices, missing acknowledgments and credit taken by both parties are the usual reasons for deficiency memos.")
         + call_box("deemed exports and merchant exports", ["Checking whether a supply is a deemed export",
                                                           "Agreeing who claims the refund",
                                                           "Refund application and documents",
                                                           "0.1% merchant export conditions",
                                                           "Deficiency memo and RFD-08 replies"],
                    "Supplier or recipient, scheme, invoices and periods, credit position, any notice.")
         + sources("CGST Act, 2017 (sections 54 and 147); CGST Rules, 2017 (rule 89); Notifications 48/2017-Central Tax and 49/2017-Central Tax; Notifications 40/2017-Central Tax (Rate) and 41/2017-Integrated Tax (Rate); IGST Act, 2017 (section 16); site GST export refund, LUT and export business pages.")),
    ],
    faqs=[("What is a deemed export under GST?", "A notified supply of goods manufactured in India that does not leave India but is treated like an export for refund purposes: goods supplied against an Advance Authorisation, capital goods against an EPCG authorisation, goods supplied to an Export Oriented Unit, and gold supplied by a bank or specified PSU against an Advance Authorisation (Notification 48/2017-Central Tax)."),
          ("Is GST charged on deemed exports?", "Yes. Deemed exports are not zero-rated, so the supplier charges GST at the normal rate. The tax is then refunded to the recipient, or to the supplier if the recipient does not take the input tax credit."),
          ("Who can claim the refund on deemed exports?", "The recipient can claim it. The supplier can claim it instead where the recipient does not avail input tax credit on the supply and undertakes not to claim the refund. The claim must be made within two years of filing the return for the supplies."),
          ("What is the 0.1% GST rate for exports?", "It is a concessional rate a registered supplier can charge on goods supplied to a registered merchant exporter, provided the merchant exporter exports the goods within 90 days of the invoice and meets the other conditions. It is a separate concession, not a deemed export."),
          ("Are supplies to SEZ units deemed exports?", "No. Supplies to SEZ units and developers are zero-rated supplies under section 16 of the IGST Act, made under an LUT or with IGST paid and refunded, which is different from deemed exports."),
          ("What should I send to start?", "WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with whether you are supplier or recipient, the scheme, invoices and periods, the credit position and any deficiency memo. Or book a call directly.")],
    related=[("gst-refund-for-exporters-igst-paid-or-lut-unused-itc-rfd-01-shipping-bill-time-limit-documents-2026.html", "GST refund for exporters"),
             ("how-to-start-export-business-india-iec-gst-lut-rcmc-ad-code-documents-payment-realisation-2026.html", "How to start an export business"),
             ("gst-on-export-of-services-lut-without-lut-invoice-format-refund-freelancer-startup-2026.html", "GST on export of services and LUT"),
             ("gst-inverted-duty-structure-refund-rule-89-5-formula-inputs-only-2-years-rfd-01-90-percent-provisional-2026.html", "Inverted duty structure refund")],
    cta_h="Supplying an EOU, an Advance Authorisation holder or a merchant exporter?", cta_b=C,
    keywords="deemed export gst, deemed export under gst, deemed export gst rate, deemed export gst rate 0.1, deemed export gst refund, deemed export gst notification, notification 48/2017 central tax, merchant export 0.1 gst, supply to eou gst, advance authorisation gst",
    desc="Deemed exports under GST: the four supplies notified by Notification 48/2017 (Advance Authorisation, EPCG, EOU, gold by banks), GST paid then refunded, who claims the refund, documents, two-year limit, SEZ difference, and the separate 0.1% merchant export rate.",
    howto={"name": "How to handle a deemed export under GST", "description": "Check, agree, document, claim.", "steps": [
        {"name": "Check the supply", "text": "Is it one of the four notified deemed exports?"},
        {"name": "Agree who claims", "text": "Recipient or supplier - and the credit position on each side."},
        {"name": "Collect documents", "text": "Acknowledgment and undertakings under Notification 49/2017-Central Tax."},
        {"name": "File the refund", "text": "Within two years of the return for the supplies; answer any deficiency memo."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch MG complete")
