# -*- coding: utf-8 -*-
"""Batch LC (28 Nov 2026): GST blocked credits under section 17(5) - cars, food, insurance, club membership, construction and works
contract, CSR, gifts and free samples, and the exceptions that allow credit.
Demand: 'blocked credit under gst', 'section 17(5) gst', 'itc on car gst', 'itc on food gst', 'itc on construction of building' -
mentioned in about five pages but no dedicated page. Business owners and accountants regularly need advice; wrong claims lead to
DRC-01 notices. User steer 26 Nov 2026: more call bookings / WhatsApp enquiries.
Facts (CGST Act section 17(5)): (a) motor vehicles for transport of persons with seating capacity of not more than 13 including
the driver - credit allowed when used for further supply of such vehicles, transport of passengers or imparting training on
driving; (ab) general insurance, servicing, repair and maintenance of such vehicles - credit where the vehicle itself qualifies,
or when received by a manufacturer or insurer as specified; (b) food and beverages, outdoor catering, beauty treatment, health
services, cosmetic and plastic surgery, leasing or renting of such vehicles, life and health insurance - credit where used for an
outward taxable supply of the same category or as part of a composite or mixed supply; membership of a club, health and fitness
centre; travel benefits to employees on vacation; with credit allowed where the law obliges the employer to provide the item to
employees; (c) works contract services for construction of immovable property (other than plant and machinery), except for a
further supply of works contract; (d) goods or services for construction of immovable property on own account (other than plant
and machinery) even if used in business - the words 'plant or machinery' were replaced by 'plant and machinery' retrospectively
from 1 July 2017 by the Finance Act, 2025, after the Supreme Court Safari Retreats judgment (October 2024); (e) supplies where tax
is paid under composition; (fa) goods or services used for CSR obligations (from 1 October 2023); (g) personal consumption;
(h) goods lost, stolen, destroyed, written off, or given as gifts or free samples; (i) tax paid on demands involving fraud or
suppression, detention or confiscation. No fees, no portal menu paths. advisory_lib.contact() is not used."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources
from build_lib import page, write_page

A.UPDATED = "Last updated: 28 November 2026."
SLUG = "gst-blocked-credits-section-17-5-itc-on-car-food-insurance-construction-csr-gifts-exceptions-2026"

C = ("WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with the type of purchase (vehicle, food, insurance, "
     "construction, gifts, CSR), how it is used in your business, the invoices or ITC amounts involved, and any DRC-01, "
     "DRC-01C or audit observation received. Or book a call directly.")
PAGES = [dict(
    slug=SLUG,
    title="GST Blocked Credits Under Section 17(5) (2026): ITC on Cars, Food, Insurance, Club Membership, Construction, CSR, Gifts and Free Samples - and the Exceptions",
    em="know the exceptions before you claim.",
    kicker="/ GST-registered businesses, accountants and CFOs &middot; Input tax credit restrictions &middot; Updated 2026-11-28",
    lead=("<strong>Section 17(5) of the CGST Act blocks input tax credit on certain purchases even when they are used in business - cars, food and beverages, insurance, club memberships, construction of buildings, CSR spending, and gifts or free samples, among others. "
          "Each block has its own exceptions, and claiming blocked credit is one of the most common reasons for GST notices and audit objections.</strong>"),
    sections=[
        ("/ What is blocked, and when credit is still allowed", "Section 17(5) item by item.",
         table(["Blocked item", "Credit still allowed when"], [
             ["Motor vehicles for carrying persons, seating up to 13 including driver", "Used for further supply of such vehicles, transport of passengers, or driving training"],
             ["Insurance, servicing, repair and maintenance of those vehicles", "The vehicle itself qualifies, or as specified for manufacturers and insurers"],
             ["Food and beverages, outdoor catering, beauty treatment, health services, cosmetic surgery", "Used for an outward taxable supply of the same category, or as part of a composite or mixed supply"],
             ["Renting of such vehicles, life and health insurance", "Same-category outward supply, or the law obliges the employer to provide it to employees"],
             ["Club, health and fitness centre membership; employee holiday travel", "The law obliges the employer to provide it to employees"],
             ["Works contract for constructing immovable property", "Used for a further supply of works contract service; or for plant and machinery"],
             ["Goods and services for constructing immovable property on own account", "Plant and machinery (not buildings or civil structures)"],
             ["Goods or services used for CSR obligations (from 1 October 2023)", "No exception"],
             ["Gifts, free samples, goods lost, stolen, destroyed or written off", "No exception"],
             ["Personal consumption", "No exception"],
             ["Tax paid on fraud or suppression demands, detention or confiscation", "No exception"]])
         + ul("<strong>Construction after Safari Retreats:</strong> the Supreme Court read &lsquo;plant or machinery&rsquo; broadly in October 2024, but the Finance Act, 2025 replaced it with &lsquo;plant and machinery&rsquo; retrospectively from 1 July 2017 - credit on buildings let out on rent remains blocked.",
              "<strong>Goods transport vehicles</strong> and vehicles seating more than 13 are not covered by the motor vehicle block.")),
        ("/ Getting it right", "Claims, reversals and notices.",
         ul("<strong>Tag purchases at entry:</strong> classify vehicle, food, insurance, construction, gift and CSR purchases so blocked credit is not claimed in GSTR-3B.",
            "<strong>Already claimed?</strong> Reverse the blocked credit with interest where it was used; paying before a show cause notice avoids penalty in non-fraud cases.",
            "<strong>Free samples and gifts:</strong> credit on inputs used for them must be reversed.",
            "<strong>Mixed use:</strong> where an item is partly for exempt or non-business use, proportionate reversal rules also apply.",
            "<strong>Notices and audits:</strong> 17(5) claims are routinely checked in GSTR-9 / 9C reviews, scrutiny and department audits - keep a working of every exception you rely on.")
         + call_box("GST blocked credits", ["Reviewing ITC claims against section 17(5)",
                                            "Exceptions for vehicles, food, insurance and construction",
                                            "Reversal with interest before a notice",
                                            "Replies to DRC-01 / DRC-01C and audit observations",
                                            "Annual return (GSTR-9 / 9C) credit review"],
                    "Purchase type, business use, invoices or ITC amounts, any notice or observation.")
         + sources("CGST Act, 2017 (section 17(5), as amended including by the Finance Act, 2023 and the Finance Act, 2025); Supreme Court, Chief Commissioner of CGST v. Safari Retreats (October 2024); site input tax credit, DRC-03, GST audit and GST notice reply pages.")),
    ],
    faqs=[("What are blocked credits under GST section 17(5)?", "Purchases on which input tax credit cannot be claimed even if used in business, such as cars seating up to 13, food and beverages, life and health insurance, club memberships, construction of buildings, CSR spending, gifts, free samples and personal consumption, each subject to specific exceptions."),
          ("Can I claim GST input tax credit on a car?", "Not on a motor vehicle for carrying persons with seating capacity of 13 or less including the driver, unless it is used for further supply of such vehicles, transport of passengers or driving training. Goods vehicles and vehicles seating more than 13 are not blocked."),
          ("Is GST credit available on food and staff welfare?", "Generally no for food and beverages, outdoor catering, health services, club memberships and holiday travel, unless they are used for an outward supply of the same kind or the law obliges the employer to provide them to employees."),
          ("Can I claim ITC on construction of a building used for business?", "No. Credit on goods, services and works contracts for constructing immovable property on your own account is blocked, except for plant and machinery. The Finance Act, 2025 confirmed this retrospectively from 1 July 2017 after the Safari Retreats judgment."),
          ("What if I have already claimed blocked credit?", "Reverse it with interest where it was used. Paying before a show cause notice avoids penalty in non-fraud cases; if a notice has already come, reply with the working of any exception you rely on."),
          ("What should I send to start?", "WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with the type of purchase, how it is used, the invoices or ITC amounts and any notice or audit observation. Or book a call directly.")],
    related=[("what-is-input-tax-credit-and-how-to-claim-india-gst.html", "What is input tax credit"),
             ("discovered-gstr-9-shortfall-voluntary-disclosure-urgent-india.html", "Pay GST shortfall through DRC-03 before a notice"),
             ("gst-audit-by-department-section-65-adt-01-notice-documents-timeline-adt-02-findings-2026.html", "GST audit by the department"),
             ("gst-drc-01c-drc-01b-notice-reply-itc-mismatch-gstr-2b-3b-liability-mismatch-gstr-1-3b-rule-88c-88d-2026.html", "DRC-01B / DRC-01C notice reply")],
    cta_h="Not sure if your GST credit is blocked?", cta_b=C,
    keywords="blocked credit under gst, section 17(5) gst, itc on car gst, itc on food gst, itc on construction of building, itc on csr expenses, itc on gifts free samples, safari retreats plant and machinery",
    desc="GST blocked credits under section 17(5): cars seating up to 13, vehicle insurance and repairs, food and beverages, health and life insurance, club membership, construction and works contract (plant and machinery, Finance Act 2025 after Safari Retreats), CSR, gifts and free samples - with the exceptions.",
    howto={"name": "How to avoid claiming blocked GST credit", "description": "Classify, check, reverse.", "steps": [
        {"name": "Classify purchases", "text": "Tag vehicle, food, insurance, construction, gift and CSR purchases."},
        {"name": "Check the exception", "text": "Same-category supply, legal obligation, plant and machinery, seating above 13."},
        {"name": "Reverse what is blocked", "text": "Reverse with interest before a notice where already used."},
        {"name": "Document", "text": "Keep a working for every exception relied on, for audit and notices."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch LC complete")
