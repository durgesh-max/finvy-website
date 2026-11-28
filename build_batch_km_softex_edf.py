# -*- coding: utf-8 -*-
"""Batch KM (28 Nov 2026): SOFTEX replaced by the EDF - how software and IT service exporters declare exports from 1 October 2026.
Demand: sweep ac229 (28 Nov 2026), all 7 markets: 'softex form', 'softex form applicability / due date / stpi / meaning / pdf',
'who is required to file softex form' - about ten variants with no page on the site (FAQ added in PR #896). User steer
26 Nov 2026: more call bookings / WhatsApp enquiries.
Facts (secondary sources - law firm and compliance publications - checked 28 Nov 2026; the RBI text is FEMA 23(R)/2026-RB):
the FEMA (Export of Goods and Services) Regulations, 2026 apply from 1 October 2026 and replace the 2015 regulations; SOFTEX is
discontinued and software is treated as a service; exports of goods, services and software are declared on a single Export
Declaration Form (EDF); for software the EDF is due within 30 days from the end of the month in which the invoice is raised,
certified by the bank or, for units in a domestic tariff area, STPI; the RBI amendment of 2 November 2026 deems resident
individuals to have filed the EDF once they give the bank the payment details, and other exporters for remittances up to
INR 10 lakh (site page fema-services-export-edf-relief...); realisation within nine months of the invoice (twelve months for
rupee invoices) per the site's FEMA services export page. No fees, no office claims, no statistics, no portal menu paths,
never ask for passwords. advisory_lib.contact() is not used (it adds a response-time / fee line awaiting owner sign-off)."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources
from build_lib import page, write_page

A.UPDATED = "Last updated: 28 November 2026."
SLUG = "softex-form-replaced-by-edf-software-it-services-export-declaration-stpi-fema-2026"

C = ("WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with whether you export as an individual, firm or company, "
     "whether you are an STPI, SEZ or domestic unit, your typical invoice sizes and currencies, your bank, and any SOFTEX forms "
     "still open from before October 2026. Or book a call directly.")
PAGES = [dict(
    slug=SLUG,
    title="SOFTEX Form Replaced by EDF (2026): How Software and IT Service Exporters Declare Exports Under the FEMA Export Regulations From 1 October 2026",
    em="one declaration for software and services.",
    kicker="/ Software, SaaS and IT service exporters &middot; STPI, SEZ and domestic units &middot; Freelancers &middot; Updated 2026-11-28",
    lead=("<strong>The SOFTEX form is gone. From 1 October 2026 the FEMA (Export of Goods and Services) Regulations, 2026 treat software as a service, "
          "and software and service exports are declared on the Export Declaration Form (EDF) instead - within 30 days from the end of the month in which the invoice is raised.</strong> "
          "Small receipts and individual exporters got relief on 2 November 2026; companies with larger invoices still run the EDF routine, and SOFTEX forms left open from earlier months still need closing."),
    sections=[
        ("/ What changed on 1 October 2026", "SOFTEX out, EDF in.",
         table(["Point", "Before (2015 regulations)", "From 1 October 2026"], [
             ["Form for software exports", "SOFTEX", "Export Declaration Form (EDF)"],
             ["Software", "Separate category", "Treated as a service"],
             ["Due date", "As set for SOFTEX", "Within 30 days from the end of the invoice month"],
             ["Certification", "STPI / SEZ authority", "Bank, or STPI for domestic tariff area units"],
             ["Individuals (freelancers)", "-", "Deemed to have filed the EDF once the bank has the payment details (2 Nov 2026)"],
             ["Other exporters, small receipts", "-", "Deemed filed for inward remittances up to INR 10 lakh (2 Nov 2026)"]])
         + ul("<strong>Realisation is unchanged in principle:</strong> export proceeds must still be realised and repatriated within the period allowed (nine months from the invoice, twelve for rupee invoices, per the current rules) - the EDF is how the bank tracks it.",
              "<strong>Open SOFTEX forms:</strong> invoices raised before 1 October 2026 under SOFTEX should be followed up with the bank or STPI so the export is shown as realised and closed.",
              "<strong>GST is separate:</strong> export of services is still zero-rated under GST with an LUT or IGST refund; the EDF does not replace GST invoices or the LUT.")),
        ("/ Who has to do what", "By type of exporter.",
         ul("<strong>Freelancers and individual consultants:</strong> give the bank complete payment details (purpose code, invoice and client) for each receipt - the EDF is then deemed filed.",
            "<strong>Companies, LLPs and firms with receipts up to INR 10 lakh:</strong> the same deemed filing applies to those remittances.",
            "<strong>Larger receipts:</strong> file the EDF within 30 days from the end of the invoice month and get it certified by the bank (or STPI for a domestic tariff area unit).",
            "<strong>STPI and SEZ units:</strong> keep the unit-level reporting your scheme requires alongside the EDF.",
            "<strong>Everyone:</strong> track realisation invoice by invoice so nothing stays outstanding past the deadline.")
         + call_box("software and IT service export compliance", ["EDF routine and bank certification for larger invoices",
                                                                  "Closing SOFTEX forms left open from before October 2026",
                                                                  "Realisation tracking and extensions",
                                                                  "GST export of services: LUT, invoices and refunds",
                                                                  "Income tax on export income"],
                    "Entity type, STPI / SEZ / domestic status, invoice sizes and currencies, bank, open SOFTEX forms.")
         + sources("FEMA (Export of Goods and Services) Regulations, 2026 (FEMA 23(R)/2026-RB), in force 1 October 2026, and the RBI amendment of 2 November 2026; FEMA (Export of Goods and Services) Regulations, 2015 (superseded); CGST and IGST Acts on zero-rated export of services; site FEMA services export, GST export of services and FEMA consultant pages. Details are drawn from published professional commentary on the 2026 Regulations; check the RBI notification and your bank's process before relying on a step.")),
    ],
    faqs=[("Is the SOFTEX form still required?", "No. The FEMA (Export of Goods and Services) Regulations, 2026, in force from 1 October 2026, discontinued SOFTEX. Software is treated as a service and software exports are declared on the Export Declaration Form (EDF)."),
          ("What is the due date for the EDF for software exports?", "Within 30 days from the end of the month in which the invoice is raised. It is certified by the bank or, for a unit in a domestic tariff area, by STPI."),
          ("Do freelancers have to file the EDF?", "Under the RBI amendment of 2 November 2026, a resident individual exporting services is deemed to have filed the EDF once they give the bank the information needed to receive and credit the payment, such as the purpose code, invoice and client details."),
          ("Is there relief for small export receipts?", "Yes. For exporters other than individuals, the EDF is deemed filed for inward remittances up to INR 10 lakh. Larger receipts follow the normal EDF process."),
          ("What happens to SOFTEX forms filed before October 2026?", "They do not disappear. Invoices declared on SOFTEX before 1 October 2026 should be followed up with the bank or STPI so the export is shown as realised and closed; an open form can lead to bank or RBI queries."),
          ("What should I send to set up export compliance?", "WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with your entity type, whether you are an STPI, SEZ or domestic unit, typical invoice sizes and currencies, your bank and any SOFTEX forms still open. Or book a call directly.")],
    related=[("fema-services-export-edf-relief-freelancers-10-lakh-rbi-amendment-2-november-2026.html", "FEMA relief for service exporters (2 Nov 2026)"),
             ("gst-on-export-of-services-lut-without-lut-invoice-format-refund-freelancer-startup-2026.html", "GST on export of services"),
             ("fema-consultant-india-fdi-odi-nri-rbi-filings-compounding-mumbai-delhi-bangalore-pune-hyderabad-chennai-2026.html", "FEMA consultant in India"),
             ("gst-consultant-online-india-registration-returns-lut-refund-notice-reply-gstr-9-near-me-2026.html", "GST consultant online")],
    cta_h="Exporting software or IT services?", cta_b=C,
    keywords="softex form, softex form replaced, softex form applicability, softex form due date, softex form stpi, edf for software exports, export declaration form services, fema export regulations 2026, edf for service exporters",
    desc="SOFTEX form replaced by the EDF from 1 October 2026: under the FEMA Export Regulations 2026 software is a service and exports are declared on the EDF within 30 days from the end of the invoice month; relief for individuals and receipts up to INR 10 lakh; close open SOFTEX forms.",
    howto={"name": "How to move from SOFTEX to the EDF", "description": "For software and IT service exporters.", "steps": [
        {"name": "Check who you are", "text": "Individual, small receipts or larger receipts; STPI, SEZ or domestic unit."},
        {"name": "Give the bank full details", "text": "Purpose code, invoice and client for every receipt."},
        {"name": "File the EDF for larger invoices", "text": "Within 30 days from the end of the invoice month, certified by the bank or STPI."},
        {"name": "Close old SOFTEX forms", "text": "Follow up pre-October invoices with the bank or STPI."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch KM complete")
