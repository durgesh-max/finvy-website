# -*- coding: utf-8 -*-
"""Batch EF (20 Nov 2026): GST registration for a non-resident taxable person (foreign company or individual supplying in
India occasionally without a fixed place: exhibitions, events, short projects). Call-first page.
Demand: sweep 20 Nov 2026 (ac20), all 7 markets: "gst registration for non resident taxable person", "non resident
taxable person gst", "gstr 5 return for non resident taxable person", "difference between casual taxable person and non
resident taxable person", "gst registration non resident company".
Facts (checked 20 Nov 2026; Taxscan, ICSI GST newsletters, West Bengal CT FAQ, Tally, Legaldev): registration in Form GST
REG-09 at least five days before starting business, with an advance deposit of estimated tax for the period; supplies
only after the certificate is issued; validity the shorter of the period sought and 90 days, extendable once for up to
90 days via REG-11 with a further deposit; an authorised signatory resident in India with a PAN; GSTR-5 by the 13th of
the following month or within 7 days after registration expires, if earlier; input tax credit blocked except IGST on
goods imported by the NRTP (section 17(5)); balance of advance deposit refunded after the final return; OIDAR suppliers
register separately (REG-10); casual taxable persons are Indian businesses supplying occasionally in another state;
late fees and interest apply."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 20 November 2026."
SLUG = "gst-registration-non-resident-taxable-person-india-foreign-company-reg-09-gstr-5-2026"
HUB = "foreign-company-india-advisor-market-research-entity-due-diligence-m-and-a-joint-venture-2026"

C = contact("your country, what you will supply in India (goods, services, exhibition sales, a project), where and for how long")
PAGES = [dict(
    slug=SLUG,
    title="GST Registration for a Foreign Company in India (2026): Non-Resident Taxable Person (REG-09) for Exhibitions, Events and Short Projects, OIDAR, Reverse Charge, Advance Deposit, GSTR-5",
    em="for foreign businesses supplying in India without an Indian office.",
    kicker="/ Foreign companies &middot; GST &middot; Non-resident taxable person &middot; Updated 2026-11-20",
    lead=("A foreign company or individual that occasionally supplies goods or services in India without a fixed place of business, for example selling at a trade exhibition, running an event or delivering a short project, must register under GST as a <strong>non-resident taxable person (NRTP)</strong>. "
          "The application goes in <strong>Form GST REG-09</strong> at least <strong>five days before</strong> business starts. It needs an <strong>authorised signatory resident in India</strong> with a PAN and an <strong>advance deposit</strong> of the estimated GST for the period. Registration lasts up to <strong>90 days</strong> and can be extended once for another 90. "
          "Returns are filed in <strong>GSTR-5</strong> by the 13th of the following month, or within seven days after registration ends. Input tax credit is generally <strong>not available</strong> on purchases in India, except IGST on goods you import. Any unused deposit is refunded after the final return. "
          "For a continuing business in India, a subsidiary or branch is usually more efficient than repeated NRTP registrations."),
    sections=[
        ("/ NRTP vs other GST registrations", "Which one applies to you.",
         table(["Registration", "Who", "Key features"], [
             ["Non-resident taxable person (REG-09)", "Foreign business supplying occasionally in India with no fixed place", "Advance deposit; up to 90 days, extendable once; GSTR-5; credit only on imported goods"],
             ["OIDAR (REG-10)", "Foreign supplier of online services to Indian consumers", "Separate simplified scheme; see the OIDAR guide"],
             ["Casual taxable person", "Indian business supplying occasionally in another state", "Advance deposit; regular returns"],
             ["Regular registration", "Indian subsidiary or branch with a place of business", "Normal returns and full input tax credit"]])
         + call_box("GST for our India event or project", ["Whether you need NRTP, OIDAR or regular registration",
                                                            "The advance deposit estimate and timeline",
                                                            "Authorised signatory and documents",
                                                            "GSTR-5 filing and getting the deposit refunded",
                                                            "Customs, temporary imports and income-tax exposure of the event"],
                    "your country, what you will supply, the event or project dates and expected sales in India.")),
        ("/ Steps and timeline", "From application to refund.",
         ul("<strong>Documents:</strong> passport or incorporation documents, tax identification from your home country, authorised signatory's PAN and Aadhaar or other KYC, details of the supply and place in India.",
            "<strong>Apply:</strong> Form GST REG-09 at least five days before starting; pay the advance deposit of estimated tax; supplies begin only after the certificate is issued.",
            "<strong>Invoice and collect GST:</strong> charge IGST or CGST and SGST as applicable on Indian sales.",
            "<strong>File GSTR-5:</strong> by the 13th of the following month, or within seven days after registration expires; late fees and interest apply for delays.",
            "<strong>Extend if needed:</strong> once, for up to 90 days, in Form REG-11 with an additional deposit.",
            "<strong>Close and refund:</strong> after the final return, claim the balance of the advance deposit.",
            "<strong>Income tax:</strong> sales at an event can create Indian tax exposure; check your treaty and permanent establishment position; see the <a href=\"permanent-establishment-risk-checker-india-foreign-company-2026.html\">PE risk checker</a>.")
         + f'<p>Related: <a href="oidar-gst-foreign-saas-ecommerce-india.html">OIDAR GST for foreign SaaS</a> &middot; <a href="india-iec-gst-customs-foreign-exporter-importer-2026.html">IEC, GST and customs</a> &middot; <a href="india-entry-structure-chooser-subsidiary-llp-branch-liaison-eor-foreign-company-2026.html">India entry structure chooser</a> &middot; <a href="{HUB}.html">working with an Indian CA</a>.</p>'
         + sources("CGST Act, 2017 (sections 24, 27, 17(5)) and CGST Rules (REG-09, REG-11, GSTR-5); IGST Act, 2017. Guides checked 20 November 2026: Taxscan (GSTR-5 for non-resident taxable persons), ICSI GST newsletters (March and April 2026), West Bengal Commercial Taxes FAQ on non-resident taxpayers, Tally, Legaldev. Confirm deposit and timelines on the GST portal before applying.")),
    ],
    faqs=[("Who is a non-resident taxable person under GST?", "A person outside India who occasionally supplies goods or services in India, as principal or agent, without a fixed place of business or residence in India, such as a foreign company selling at a trade show."),
        ("Does a foreign company need GST registration in India?", "It depends on what it supplies and to whom. A foreign company that occasionally makes taxable supplies in India without a fixed place of business - for example selling at an exhibition or carrying out a short project - must register as a non-resident taxable person (REG-09, with an advance deposit). A foreign provider of online services (OIDAR) supplying Indian consumers or other non-business recipients registers under the simplified scheme in REG-10 and pays IGST - see our OIDAR guide. Services supplied to GST-registered Indian businesses are usually taxed under reverse charge in the hands of the Indian recipient, so the foreign supplier does not register for them, and goods shipped to India bear IGST at customs paid by the importer."),
        ("What should a foreign company send to check its GST position in India?", "WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with what you sell into India (goods, services or digital services), who your Indian customers are (registered businesses or consumers), whether you have any office, staff or event in India, and sample invoices or contracts. We confirm whether you need NRTP or OIDAR registration, or whether reverse charge by your customers covers it, and handle the registration and returns if needed."),
          ("How does a foreign company register for GST as an NRTP?", "By filing Form GST REG-09 at least five days before starting business, with an Indian-resident authorised signatory holding a PAN and an advance deposit of the estimated tax."),
          ("How long is NRTP registration valid?", "For the period applied for, up to 90 days, extendable once for up to another 90 days with an additional deposit."),
          ("What return does an NRTP file?", "GSTR-5, by the 13th of the following month or within seven days after the registration expires, whichever is earlier."),
          ("Can an NRTP claim input tax credit?", "Generally not on purchases in India; credit is available on IGST paid on goods the NRTP imports."),
          ("Can BQP handle our NRTP registration?", "Yes. " + C)],
    related=[("oidar-gst-foreign-saas-ecommerce-india.html", "OIDAR GST for foreign SaaS"), ("india-iec-gst-customs-foreign-exporter-importer-2026.html", "IEC, GST and customs"),
             (HUB + ".html", "Working with an Indian CA")],
    cta_h="Selling at an event or running a project in India?", cta_b=C,
    keywords="non resident taxable person GST registration, GST registration for non resident India, GST REG-09, GSTR-5 due date, NRTP advance deposit 90 days, casual vs non resident taxable person, GST for foreign company exhibition India",
    desc="GST for a non-resident taxable person in India (2026): foreign businesses at exhibitions, events or short projects register in REG-09 five days before, with an Indian authorised signatory and advance deposit; 90-day validity, GSTR-5 by the 13th, limited input tax credit, deposit refund.",
    howto={"name": "How a foreign company registers as a non-resident taxable person under GST", "description": "From application to refund.", "steps": [
        {"name": "Confirm the registration type", "text": "NRTP, OIDAR or regular registration."},
        {"name": "Appoint an authorised signatory", "text": "An India-resident person with a PAN."},
        {"name": "Apply in REG-09 with deposit", "text": "At least five days before starting, with the estimated tax deposited."},
        {"name": "Invoice and file GSTR-5", "text": "Charge GST and file by the 13th of the following month."},
        {"name": "Close and claim refund", "text": "File the final return and claim the unused deposit."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch EF complete")
