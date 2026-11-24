# -*- coding: utf-8 -*-
"""Batch HK (25 Nov 2026): GST on rent - residential vs commercial property: residential dwelling exempt when let to an
unregistered person, reverse charge (18%) when let to a registered person (from 18 July 2022; proprietor renting for own
residence carved out); commercial property: registered landlord charges 18%, unregistered landlord to registered tenant
under reverse charge from 10 October 2024, composition tenants excluded from 16 January 2025; landlord registration
threshold; TDS on rent excluding GST; NRI landlords.
Demand: sweep ac96 (25 Nov 2026), all 7 markets: "gst on rent", "gst on rent paid on commercial property", "gst on rent
of residential property", "gst on rent of commercial property".
Facts (checked 25 Nov 2026): Notifications 04/2022 and 05/2022-CT(Rate) (entry 5AA, from 18 July 2022) as summarised by
Taxguru, Taxmann and Business Standard; Notification 09/2024 (entry 5AB, from 10 October 2024) and 07/2025-CT(Rate) (16
January 2025, composition exclusion) and Circular 245/02/2025-GST as reported by Taxscan and Studycafe; Tally / ClearTax
guides on 18% rate. No 2026 change to rent taxation found."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 25 November 2026."
SLUG = "gst-on-rent-residential-commercial-property-reverse-charge-18-percent-registered-tenant-landlord-2026"

C = contact("whether you are the landlord or tenant, residential or commercial property, who is GST-registered, the monthly rent, and whether the landlord is an NRI")
L = lambda h, t: f'<a href="{h}">{t}</a>'
PAGES = [dict(
    slug=SLUG,
    title="GST on Rent (2026): Residential vs Commercial Property, 18% Rate, Reverse Charge for Registered Tenants and Landlord Registration",
    em="who pays depends on who is registered.",
    kicker="/ Landlords, tenants and businesses &middot; GST &middot; Updated 2026-11-25",
    lead=("<strong>GST on rent is 18%, but whether it applies, and who pays it, depends on the type of property and on whether the landlord and the tenant are GST-registered.</strong> "
          "Renting a house or flat to an unregistered person for living in is exempt. Renting a residential dwelling to a GST-registered tenant is taxed under reverse charge, so the tenant pays. "
          "For commercial property, a registered landlord charges 18% on the invoice; if the landlord is unregistered and the tenant is registered, the tenant pays under reverse charge (since 10 October 2024), unless the tenant is under the composition scheme."),
    sections=[
        ("/ Quick answers", "What landlords and tenants ask.",
         ul("<strong>Is there GST on residential rent?</strong> Not when the tenant is an unregistered individual using it as a home. If the tenant is GST-registered, the tenant pays 18% under reverse charge.",
            "<strong>A proprietor rents a flat to live in. GST?</strong> Renting to a registered proprietor in a personal capacity for his or her own residence is carved out; renting in the business&rsquo;s name or for business use is under reverse charge.",
            "<strong>Is there GST on commercial rent?</strong> Yes, 18%. A registered landlord charges it; if the landlord is unregistered and the tenant is registered (and not under composition), the tenant pays under reverse charge.",
            "<strong>When must a landlord register?</strong> When aggregate turnover from taxable supplies, including commercial rent, exceeds &#8377;20 lakh in a year (&#8377;10 lakh in special category states). Exempt residential rent is part of aggregate turnover but is not taxed.",
            "<strong>Can the tenant claim input tax credit?</strong> A registered tenant using the premises for business can generally claim credit for GST paid, including under reverse charge, subject to the usual conditions.",
            "<strong>Is TDS on rent worked out on rent plus GST?</strong> No. Where GST is shown separately on the invoice, TDS on rent is deducted on the rent excluding GST; see " + L("tds-on-rent-limit-fy-2026-27-section-393-194ib-194i-194ia-property-purchase-1-percent-nri-landlord.html", "TDS on rent for FY 2026-27") + ".")),
        ("/ Who pays GST on rent", "Six combinations.",
         table(["Property", "Landlord", "Tenant", "GST"], [
             ["Residential dwelling", "Any", "Unregistered (living in it)", "Exempt"],
             ["Residential dwelling", "Any", "Registered (business use or in business name)", "18% under reverse charge, paid by tenant"],
             ["Residential dwelling", "Any", "Registered proprietor, personal residence", "Exempt (carved out)"],
             ["Commercial / non-residential", "Registered", "Any", "18% forward charge, on landlord&rsquo;s invoice"],
             ["Commercial / non-residential", "Unregistered", "Registered (regular)", "18% under reverse charge, paid by tenant (from 10 Oct 2024)"],
             ["Commercial / non-residential", "Unregistered", "Registered under composition, or unregistered", "No GST (composition tenants excluded from 16 Jan 2025)"]])
         + '<p>More on reverse charge mechanics: ' + L("gst-reverse-charge-import-of-services-india-rcm-self-invoice-itc-2026.html", "GST reverse charge, self-invoice and ITC") + '. Registration thresholds: ' + L("is-gst-registration-mandatory-for-startup-new-small-business-threshold-2026.html", "is GST registration mandatory?") + '.</p>'),
        ("/ Practical points", "Getting it right.",
         ul("<strong>Tenants paying under reverse charge</strong> issue a self-invoice, pay the GST in cash (it cannot be paid from credit) and report it in GSTR-3B; the credit can then be taken where eligible.",
            "<strong>Startups and companies</strong> renting a flat for a founder or as a guest house are registered tenants: reverse charge applies even if the flat is only lived in.",
            "<strong>NRI landlords</strong> letting commercial property: an unregistered NRI landlord&rsquo;s registered tenant pays under reverse charge; once taxable rent crosses the threshold the NRI must register. Income tax on the rent is separate; see " + L("nri-rental-income-india-tenant-tds-31-2-percent-tan-form-144-2026.html", "NRI rental income and TDS") + ".",
            "<strong>Mixed use:</strong> a residential flat used as an office is rent for non-residential use; check the arrangement and the agreement.",
            "<strong>Annual return:</strong> rent and reverse charge entries flow into the annual return; see " + L("gstr-9-gstr-9c-fy-2025-26-mandatory-optional-tables-notification-05-2026-due-31-december-2026.html", "GSTR-9 for FY 2025-26") + ".")
         + call_box("GST on rent", ["Whether reverse charge applies to your lease",
                                    "Landlord GST registration",
                                    "Self-invoice and ITC for tenants",
                                    "NRI landlords: GST and income tax",
                                    "Correcting missed reverse charge"],
                    "the property type, both parties&rsquo; GST status and the rent.")
         + sources("CBIC Notifications 04/2022 and 05/2022-Central Tax (Rate) (residential dwelling, entry 5AA), 09/2024 (non-residential property, entry 5AB) and 07/2025-Central Tax (Rate) (composition exclusion), Circular 245/02/2025-GST, as summarised by Taxguru, Taxmann, Taxscan, Studycafe and Business Standard; Tally and ClearTax GST on rent guides. Checked 25 November 2026.")),
    ],
    faqs=[("Is GST applicable on rent of residential property?", "Not when it is rented to an unregistered person as a residence. If the tenant is GST-registered and rents it for business or in the business's name, the tenant pays 18% GST under reverse charge. A registered proprietor renting in a personal capacity for his or her own home is carved out."),
          ("What is the GST rate on commercial rent?", "18%. A registered landlord charges it on the invoice. If the landlord is unregistered and the tenant is a regular registered taxpayer, the tenant pays it under reverse charge, which applies from 10 October 2024."),
          ("Do composition taxpayers pay reverse charge on commercial rent?", "No. From 16 January 2025, a tenant under the composition scheme is excluded from reverse charge on rent paid to an unregistered landlord for commercial property."),
          ("When does a landlord need GST registration?", "When aggregate turnover from taxable supplies, such as commercial rent, crosses Rs 20 lakh in a financial year (Rs 10 lakh in special category states)."),
          ("Is TDS on rent deducted on the GST amount too?", "No. Where GST is shown separately on the invoice, TDS on rent is worked out on the rent amount excluding GST."),
          ("Can BQP help with GST on rent?", "Yes. CA Durgesh Chavda can check whether GST or reverse charge applies to your lease, handle landlord registration, and set up self-invoicing and credit for tenants. " + C)],
    related=[("gst-reverse-charge-import-of-services-india-rcm-self-invoice-itc-2026.html", "GST reverse charge and ITC"),
             ("is-gst-registration-mandatory-for-startup-new-small-business-threshold-2026.html", "GST registration threshold"),
             ("tds-on-rent-limit-fy-2026-27-section-393-194ib-194i-194ia-property-purchase-1-percent-nri-landlord.html", "TDS on rent FY 2026-27"),
             ("what-is-input-tax-credit-and-how-to-claim-india-gst.html", "Input tax credit"),
             ("nri-rental-income-india-tenant-tds-31-2-percent-tan-form-144-2026.html", "NRI rental income")],
    cta_h="Renting property to or from a business?", cta_b=C,
    keywords="GST on rent, GST on rent of residential property, GST on rent paid on commercial property, GST on commercial rent 18 percent, RCM on rent, reverse charge on rent unregistered landlord, GST on rent registered tenant, GST on rent composition",
    desc="GST on rent (2026): residential rent exempt for unregistered tenants, 18% reverse charge for registered tenants; commercial rent 18%, reverse charge when the landlord is unregistered (from 10 Oct 2024), composition tenants excluded; registration and TDS.",
    howto={"name": "How to work out GST on rent", "description": "For a lease in India.", "steps": [
        {"name": "Identify the property type", "text": "Residential dwelling or commercial / non-residential."},
        {"name": "Check both parties' GST status", "text": "Registered (regular or composition) or unregistered."},
        {"name": "Find who pays", "text": "Landlord on invoice (forward charge) or tenant (reverse charge)."},
        {"name": "Pay and report", "text": "Reverse charge: self-invoice, pay in cash, report in GSTR-3B."},
        {"name": "Claim credit and deduct TDS", "text": "ITC where eligible; TDS on rent excluding GST."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch HK complete")
