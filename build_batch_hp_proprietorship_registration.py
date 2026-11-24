# -*- coding: utf-8 -*-
"""Batch HP (25 Nov 2026): sole proprietorship registration in India - no single registration law; the business is
identified through GST, Udyam, Shops and Establishments licence, municipal trade licence and other registrations; documents;
current account (bank needs proof of the business in the proprietor's name); tax (proprietor's PAN, ITR-3 / ITR-4,
presumptive section 44AD); when to move to an LLP or company; NRIs.
Demand: sweep ac100 (25 Nov 2026), all 7 markets: "proprietorship registration", "proprietorship registration documents
required", "proprietorship registration online government website", "proprietorship registration in india", "gst
registration online for sole proprietorship".
Facts (checked 25 Nov 2026) cross-checked with site pages: GST thresholds (Rs 20 lakh services, Rs 40 lakh goods-only in
most states, lower in special category states; is-gst-registration-mandatory page), Udyam free online registration and
downloadable certificate (udyam-msme page), NRI proprietorship on a non-repatriation basis (can-nri-start-business page),
partnership registration page. No state fee figures given."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 25 November 2026."
SLUG = "sole-proprietorship-registration-india-documents-gst-udyam-shop-licence-online-2026"

C = contact("the state and city, the business activity, expected turnover, whether you sell online or across states, and whether you need a current account or GST")
L = lambda h, t: f'<a href="{h}">{t}</a>'
PAGES = [dict(
    slug=SLUG,
    title="Sole Proprietorship Registration in India (2026): Documents, GST, Udyam, Shop Licence and How to Get a Current Account",
    em="there is no single certificate, so build the right set of registrations.",
    kicker="/ Small businesses and freelancers &middot; Business registration &middot; Updated 2026-11-25",
    lead=("<strong>India has no separate law or certificate for registering a sole proprietorship: the business is simply the owner trading in their own name or a trade name, using the owner&rsquo;s PAN.</strong> "
          "It is &ldquo;registered&rdquo; by taking the registrations the business needs, most commonly Udyam (free, online), GST (once turnover crosses &#8377;20 lakh for services or &#8377;40 lakh for goods-only in most states, or earlier in compulsory cases), and the state Shops and Establishments licence or a municipal trade licence. "
          "Two of these in the business name are usually what a bank asks for to open a current account."),
    sections=[
        ("/ Quick answers", "What people search for.",
         ul("<strong>How do I register a proprietorship?</strong> There is no single government registration. Take Udyam registration, GST if required, and the state shop or trade licence, then open a current account in the business name.",
            "<strong>Is there a government website for proprietorship registration?</strong> No single one. Udyam is on the Udyam Registration portal, GST on the GST portal, and shop and trade licences on state or municipal portals.",
            "<strong>Is GST compulsory for a sole proprietor?</strong> Only once aggregate turnover crosses the threshold (&#8377;20 lakh for services, &#8377;40 lakh for goods-only in most states, lower in some special category states) or in compulsory cases such as inter-state supply of goods or selling through e-commerce platforms; see " + L("is-gst-registration-mandatory-for-startup-new-small-business-threshold-2026.html", "is GST registration mandatory?") + ".",
            "<strong>What documents are needed?</strong> The owner&rsquo;s PAN and Aadhaar, a photograph, proof of the business address (rent agreement or ownership with NOC, and a utility bill), and a bank account; GST also asks for the place-of-business proof.",
            "<strong>How is a proprietorship taxed?</strong> As the owner&rsquo;s own income, in the owner&rsquo;s return (ITR-3, or ITR-4 under the presumptive scheme for eligible small businesses).",
            "<strong>Can an NRI own one?</strong> Yes, on a non-repatriation basis, outside barred activities; see " + L("can-nri-start-business-in-india-sole-proprietorship-partnership-opc-llp-company-2026.html", "can an NRI start a business in India") + ".")),
        ("/ Registrations to consider", "Pick what your business actually needs.",
         table(["Registration", "When it is needed", "Where"], [
             ["Udyam (MSME)", "Optional but useful: government schemes, priority lending, delayed-payment protection; free", "Udyam Registration portal; see " + L("udyam-msme-registration-benefits-india-2026.html", "Udyam guide")],
             ["GST", "Turnover above the threshold or compulsory cases", "GST portal"],
             ["Shops and Establishments", "Most shops, offices and commercial premises, under state law", "State labour department portal"],
             ["Trade licence", "Many municipalities, depending on the activity", "Municipal corporation"],
             ["Professional tax", "In states that levy it, for the owner and employees", "State tax department"],
             ["Import Export Code", "Importing or exporting goods or services", "DGFT portal; see " + L("india-iec-gst-customs-foreign-exporter-importer-2026.html", "IEC guide")],
             ["Activity licences", "Food (FSSAI), drugs, and other regulated activities", "The relevant regulator"]])),
        ("/ Limits of a proprietorship", "When to choose something else.",
         ul("<strong>Unlimited liability:</strong> the owner is personally liable for all business debts.",
            "<strong>No outside equity:</strong> investors cannot take shares; bringing in a partner means a " + L("partnership-firm-registration-india-online-documents-certificate-form-1-registrar-of-firms-2026.html", "partnership firm") + ", an LLP or a company.",
            "<strong>Continuity:</strong> the business is tied to the owner and does not continue as a separate entity.",
            "<strong>Growth path:</strong> compare " + L("llp-registration-india-2026-process-documents-fillip-designated-partner-nri-foreign-partner.html", "LLP registration") + " and " + L("which-is-better-llp-vs-private-limited-india.html", "LLP vs private limited") + ".")
         + call_box("Starting as a sole proprietor", ["Which registrations you need",
                                                      "GST and Udyam registration",
                                                      "Current account documents",
                                                      "Presumptive tax and ITR",
                                                      "Moving to an LLP or company later"],
                    "the activity, location and expected turnover.")
         + sources("Central Goods and Services Tax Act, 2017 (sections 22 to 24) and notified threshold limits; MSME Udyam registration notifications; state Shops and Establishments Acts; RBI KYC directions for proprietary concerns; Income-tax provisions on presumptive taxation; FEMA (Non-Debt Instruments) Rules for NRIs. State licences and fees vary. Checked 25 November 2026.")),
    ],
    faqs=[("How do I register a sole proprietorship in India?", "There is no single proprietorship registration. The business is identified through the registrations it takes: usually Udyam (free, online), GST once turnover crosses the threshold or in compulsory cases, and the state Shops and Establishments or municipal trade licence. A current account is then opened in the business name."),
          ("What documents are required for proprietorship registration?", "The owner's PAN and Aadhaar, a photograph, proof of the business address such as a rent agreement or ownership document with an NOC plus a utility bill, and bank details. Each registration (GST, Udyam, shop licence) asks for its own set."),
          ("Is there a government website for proprietorship registration?", "No single website. Udyam registration is on the Udyam portal, GST on the GST portal, and shop or trade licences on state or municipal portals."),
          ("Do I need GST registration as a sole proprietor?", "Only when aggregate turnover exceeds the threshold (Rs 20 lakh for services, Rs 40 lakh for goods-only in most states, lower in some special category states) or in compulsory cases such as inter-state supply of goods or selling through e-commerce operators."),
          ("Which documents does a bank need for a proprietorship current account?", "Banks usually ask for two proofs of the business in the proprietor's name, such as a GST certificate, Udyam certificate, shop and establishments licence, IEC or utility bills, along with the owner's KYC."),
          ("Can BQP set up our proprietorship registrations?", "Yes. CA Durgesh Chavda can work out which registrations you need, handle GST and Udyam, and set up your tax and accounts. " + C)],
    related=[("partnership-firm-registration-india-online-documents-certificate-form-1-registrar-of-firms-2026.html", "Partnership firm registration"),
             ("is-gst-registration-mandatory-for-startup-new-small-business-threshold-2026.html", "GST registration threshold"),
             ("udyam-msme-registration-benefits-india-2026.html", "Udyam MSME registration"),
             ("can-nri-start-business-in-india-sole-proprietorship-partnership-opc-llp-company-2026.html", "Business structures for NRIs"),
             ("llp-registration-india-2026-process-documents-fillip-designated-partner-nri-foreign-partner.html", "LLP registration")],
    cta_h="Starting a business in your own name?", cta_b=C,
    keywords="proprietorship registration, sole proprietorship registration India, proprietorship registration documents required, proprietorship registration online, GST registration for sole proprietorship, proprietorship current account documents, Udyam for proprietorship",
    desc="Sole proprietorship registration in India (2026): no single certificate; register through Udyam, GST (above threshold or compulsory cases), Shops and Establishments or trade licence; documents, current account proofs, tax, NRIs.",
    howto={"name": "How to set up a sole proprietorship in India", "description": "Using the registrations the business needs.", "steps": [
        {"name": "Choose a trade name and address", "text": "Keep proof of the place of business."},
        {"name": "Register on Udyam", "text": "Free and online with Aadhaar and PAN."},
        {"name": "Take GST if required", "text": "Above the threshold or in compulsory cases."},
        {"name": "Get the shop or trade licence", "text": "Under state or municipal rules."},
        {"name": "Open a current account", "text": "With two proofs of the business in your name."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch HP complete")
