# -*- coding: utf-8 -*-
"""Batch HV (25 Nov 2026): GST composition scheme - turnover limits (Rs 1.5 crore; Rs 75 lakh in specified states;
service providers Rs 50 lakh), rates (1% manufacturers and traders, 5% restaurants, 6% services), conditions (no ITC, no
tax collected from customers, bill of supply, no inter-state outward supply of goods, excluded categories), compliance
(CMP-02 before the year, CMP-08 by the 18th after each quarter, annual GSTR-4, CMP-04 to exit), pros and cons.
Demand: sweep ac105 (25 Nov 2026), all 7 markets: "gst composition scheme", "turnover limit", "limit", "rules", "rate",
"for service providers", "check", "gst on services in composition scheme".
Facts (checked 25 Nov 2026): CAclubindia 'Composition scheme under GST ... FY 2026-27'; ClearTax, Taxguru, IndiaFilings
(CMP-02 deadline), Busy, Paytm composition guides; Taxscan on GSTAT order (scheme ends on crossing Rs 1.5 crore).
GSTR-4 due date: rule 62 amended in 2024 to 30 June (some guides still say 30 April) - stated with that caveat.
E-commerce eligibility reported inconsistently - flagged, not stated."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 25 November 2026."
SLUG = "gst-composition-scheme-turnover-limit-1-5-crore-rates-service-providers-6-percent-rules-2026"

C = contact("your state, whether you trade, manufacture, run a restaurant or provide services, your turnover, whether you sell to other states or online, and your input costs")
L = lambda h, t: f'<a href="{h}">{t}</a>'
PAGES = [dict(
    slug=SLUG,
    title="GST Composition Scheme (2026): Turnover Limit Rs 1.5 Crore, Rates, Service Providers at 6%, Rules, Returns and Who Should Opt In",
    em="lower tax and fewer returns, at the cost of input tax credit.",
    kicker="/ Small businesses &middot; GST &middot; Updated 2026-11-25",
    lead=("<strong>The GST composition scheme lets small businesses pay tax at a flat rate on turnover instead of charging regular GST: 1% for traders and manufacturers, 5% for restaurants and 6% for service providers.</strong> "
          "It is open to businesses with turnover up to &#8377;1.5 crore in the previous year (&#8377;75 lakh in some special category states), and up to &#8377;50 lakh for service providers. "
          "In return, a composition taxpayer cannot claim input tax credit, cannot collect GST from customers, issues a bill of supply instead of a tax invoice and cannot make inter-state outward supplies of goods. "
          "It files a quarterly payment statement (CMP-08) and one annual return (GSTR-4)."),
    sections=[
        ("/ Quick answers", "What small businesses search for.",
         ul("<strong>What is the composition scheme turnover limit?</strong> &#8377;1.5 crore aggregate turnover in the previous financial year for traders, manufacturers and restaurants (&#8377;75 lakh in some special category states); &#8377;50 lakh for service providers under the separate services composition.",
            "<strong>What are the composition rates?</strong> 1% (0.5% CGST + 0.5% SGST) for manufacturers and traders, 5% for restaurants not serving alcohol, and 6% (3% + 3%) for other service providers.",
            "<strong>Can service providers opt in?</strong> Yes, under the services composition at 6% if turnover was up to &#8377;50 lakh. Restaurants use the main scheme.",
            "<strong>How do I opt in?</strong> File Form CMP-02 on the GST portal before the start of the financial year (for a new registration, choose composition in the registration application).",
            "<strong>What returns are due?</strong> CMP-08 to pay tax by the 18th of the month after each quarter, and the annual GSTR-4. The GSTR-4 due date was moved to 30 June after the year in 2024; some guides still show 30 April, so check the portal.",
            "<strong>How do I check if a supplier is under composition?</strong> Search the GSTIN on the GST portal; the taxpayer type shows Composition.")),
        ("/ Composition vs regular GST", "Which suits you.",
         table(["Point", "Composition", "Regular"], [
             ["Tax", "Flat 1% / 5% / 6% of turnover, paid by you", "Rate on each supply, collected from customers"],
             ["Input tax credit", "Not available", "Available"],
             ["Invoice", "Bill of supply, no GST shown", "Tax invoice"],
             ["Inter-state outward supply of goods", "Not allowed", "Allowed"],
             ["Returns", "CMP-08 quarterly + GSTR-4 annual", "GSTR-1, GSTR-3B (monthly or quarterly) + annual return"],
             ["Best for", "B2C businesses with low input costs and local customers", "B2B suppliers whose customers want credit, exporters, inter-state sellers"]])
         + '<p>Thresholds for registering at all are explained in ' + L("is-gst-registration-mandatory-for-startup-new-small-business-threshold-2026.html", "is GST registration mandatory?") + '.</p>'),
        ("/ Who cannot opt in", "Exclusions and exits.",
         ul("<strong>Excluded:</strong> businesses making inter-state outward supplies of goods, non-resident and casual taxable persons, and manufacturers of notified goods such as ice cream, pan masala and tobacco products.",
            "<strong>E-commerce:</strong> eligibility for sellers supplying through e-commerce operators is reported inconsistently and has changed over time; confirm before opting in.",
            "<strong>All or nothing:</strong> every registration under the same PAN must opt for composition together.",
            "<strong>Crossing the limit:</strong> once turnover crosses the limit during the year, the scheme ends and regular GST applies; file CMP-04 to leave voluntarily.",
            "<strong>Sole proprietors and small firms:</strong> see " + L("sole-proprietorship-registration-india-documents-gst-udyam-shop-licence-online-2026.html", "proprietorship registration") + " and " + L("partnership-firm-registration-india-online-documents-certificate-form-1-registrar-of-firms-2026.html", "partnership firm registration") + ".")
         + call_box("GST composition or regular?", ["Eligibility and turnover test",
                                                    "Composition vs regular tax comparison",
                                                    "CMP-02, CMP-08 and GSTR-4",
                                                    "Moving out of composition",
                                                    "Rent and reverse charge for composition dealers"],
                    "your state, activity, turnover and customers.")
         + sources("Central Goods and Services Tax Act, 2017, section 10 and Notification 2/2019-CT(Rate) (services composition); CGST Rules 3 to 7 and rule 62; CAclubindia composition scheme guide for FY 2026-27; ClearTax, Taxguru, IndiaFilings, Busy and Paytm guides; Taxscan report on a GSTAT order. Checked 25 November 2026.")),
    ],
    faqs=[("What is the turnover limit for the GST composition scheme?", "Rs 1.5 crore aggregate turnover in the previous financial year for traders, manufacturers and restaurants (Rs 75 lakh in some special category states), and Rs 50 lakh for service providers under the services composition scheme."),
          ("What are the GST composition scheme rates?", "1% of turnover for manufacturers and traders, 5% for restaurants not serving alcohol, and 6% for other service providers, split equally between CGST and SGST."),
          ("Can a service provider opt for the composition scheme?", "Yes. A service provider with turnover up to Rs 50 lakh in the previous year can pay 6% under the services composition scheme, without input tax credit and without charging GST to customers."),
          ("What returns does a composition taxpayer file?", "CMP-08 by the 18th of the month after each quarter to pay tax, and the annual GSTR-4. The GSTR-4 due date was moved to 30 June after the year in 2024; confirm the current date on the GST portal."),
          ("Can a composition dealer claim input tax credit?", "No. Composition taxpayers cannot claim input tax credit or collect GST from customers; they issue a bill of supply instead of a tax invoice."),
          ("Can BQP help decide between composition and regular GST?", "Yes. CA Durgesh Chavda can compare the two for your turnover and customers, file CMP-02 and handle CMP-08 and GSTR-4. " + C)],
    related=[("is-gst-registration-mandatory-for-startup-new-small-business-threshold-2026.html", "GST registration threshold"),
             ("gst-on-rent-residential-commercial-property-reverse-charge-18-percent-registered-tenant-landlord-2026.html", "GST on rent"),
             ("what-is-input-tax-credit-and-how-to-claim-india-gst.html", "Input tax credit"),
             ("sole-proprietorship-registration-india-documents-gst-udyam-shop-licence-online-2026.html", "Sole proprietorship registration"),
             ("gst-notice-response-india-asmt-drc-gstr.html", "GST notice response")],
    cta_h="Choosing between composition and regular GST?", cta_b=C,
    keywords="GST composition scheme, GST composition scheme turnover limit, composition scheme limit 1.5 crore, GST composition scheme rate, composition scheme for service providers, GST composition scheme rules, CMP-08, GSTR-4, CMP-02",
    desc="GST composition scheme (2026): turnover limit Rs 1.5 crore (Rs 75 lakh special states), Rs 50 lakh for services; rates 1% / 5% / 6%; no ITC, bill of supply, no inter-state goods; CMP-02, CMP-08, GSTR-4; who should opt in.",
    howto={"name": "How to opt for the GST composition scheme", "description": "For an existing GST registration.", "steps": [
        {"name": "Check eligibility", "text": "Turnover limit, no inter-state goods supply, not an excluded category."},
        {"name": "Compare with regular GST", "text": "Input credit lost versus lower tax and fewer returns."},
        {"name": "File CMP-02", "text": "On the GST portal before the financial year starts."},
        {"name": "Switch to bills of supply", "text": "No GST charged; display composition status."},
        {"name": "File CMP-08 and GSTR-4", "text": "Quarterly payment and annual return."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch HV complete")
