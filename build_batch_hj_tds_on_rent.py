# -*- coding: utf-8 -*-
"""Batch HJ (25 Nov 2026): TDS on rent and on property purchase for tax year 2026-27 under section 393 of the
Income-tax Act, 2025: Table Sl. No. 2(i) (was 194-IB, individuals/HUFs not under audit, 2% above Rs 50,000 a month,
deducted once, capped at last month's rent), Sl. No. 2(ii) (was 194-I, 10% land/building/furniture, 2% plant and
machinery, above Rs 50,000 a month), Sl. No. 3(i) (was 194-IA, 1% on property of Rs 50 lakh or more), NRI landlord under
section 393(2) (was 195).
Demand: sweep ac96 (25 Nov 2026), all 7 markets: "tds on rent limit for fy 2026-27", "tds on rent limit fy 26 27",
"tds on rent limit for fy 2025-26", "section 194ia and 194ib", "section 194ia".
Facts (checked 25 Nov 2026): Income Tax Department FAQs on TDS on rent and TDS (10% land/building/furniture, threshold
Rs 50,000 for a month or part); incometaxindia section 393 page (1% of higher of consideration or stamp duty value,
Rs 50 lakh); Taxmann 'TDS on rent under Income-tax Act 2025' (Sl. No. 2(i) = 194-IB, 2(ii) = 194-I); Taxguru mapping table
(194-IA = 393(1) Sl. No. 3(i)); CAclubindia FY 26-27 rent TDS article (2%, Rs 50,000 a month, cap at last month's rent)."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 25 November 2026."
SLUG = "tds-on-rent-limit-fy-2026-27-section-393-194ib-194i-194ia-property-purchase-1-percent-nri-landlord"

C = contact("whether you are the tenant, landlord, buyer or seller, the monthly rent or property value, whether the other party is resident or NRI, and whether you are under tax audit")
L = lambda h, t: f'<a href="{h}">{t}</a>'
PAGES = [dict(
    slug=SLUG,
    title="TDS on Rent Limit for FY 2026-27: Section 393 (Old 194-IB, 194-I and 194-IA), Rs 50,000 a Month, Rates and Property Purchase TDS",
    em="new section numbers, same Rs 50,000 test.",
    kicker="/ Tenants, landlords and property buyers &middot; TDS &middot; Updated 2026-11-25",
    lead=("<strong>From 1 April 2026, TDS on rent and on property purchases is deducted under section 393 of the Income-tax Act, 2025, which replaced sections 194-IB, 194-I and 194-IA.</strong> "
          "For tax year 2026-27, a tenant deducts TDS when rent exceeds &#8377;50,000 for a month or part of a month. "
          "Individuals and HUFs not under tax audit deduct 2% (old 194-IB, now Table Sl. No. 2(i)). Other payers deduct 10% on land, buildings and furniture and 2% on plant and machinery (old 194-I, now Sl. No. 2(ii)). "
          "A buyer of property worth &#8377;50 lakh or more deducts 1% (old 194-IA, now Sl. No. 3(i)). If the landlord or seller is an NRI, different, higher rates apply under section 393(2)."),
    sections=[
        ("/ Quick answers", "The questions behind the searches.",
         ul("<strong>What is the TDS on rent limit for FY 2026-27?</strong> &#8377;50,000 for a month or part of a month, for both individual tenants and businesses.",
            "<strong>What replaced 194-IB?</strong> Section 393(1), Table Sl. No. 2(i): 2% on rent above &#8377;50,000 a month, paid by individuals and HUFs not under tax audit, deducted once in the year.",
            "<strong>What replaced 194-I?</strong> Section 393(1), Table Sl. No. 2(ii): 10% on land, building, furniture or fittings and 2% on plant, machinery or equipment.",
            "<strong>What replaced 194-IA?</strong> Section 393(1), Table Sl. No. 3(i): 1% of the sale price or stamp duty value, whichever is higher, where it is &#8377;50 lakh or more.",
            "<strong>My landlord is an NRI. Which rule applies?</strong> Neither of the resident-rent entries. TDS falls under section 393(2) (old 195), with no &#8377;50,000 threshold and higher rates; see " + L("nri-rental-income-india-tenant-tds-31-2-percent-tan-form-144-2026.html", "TDS on rent paid to an NRI") + ".",
            "<strong>Is a refundable security deposit subject to TDS?</strong> A genuinely refundable deposit is generally not rent, so TDS is not deducted on it; an adjustable or non-refundable amount can be.")),
        ("/ Old vs new sections at a glance", "Tax year 2026-27 onwards.",
         table(["Payment", "Old section (1961 Act)", "New (2025 Act)", "Rate", "Threshold"], [
             ["Rent paid by individuals / HUFs not under audit", "194-IB", "393(1) Sl. No. 2(i)", "2%", "&#8377;50,000 a month"],
             ["Rent for land, building, furniture (others)", "194-I(b)", "393(1) Sl. No. 2(ii)", "10%", "&#8377;50,000 a month"],
             ["Rent for plant, machinery, equipment", "194-I(a)", "393(1) Sl. No. 2(ii)", "2%", "&#8377;50,000 a month"],
             ["Purchase of property from a resident", "194-IA", "393(1) Sl. No. 3(i)", "1% of higher of price or stamp value", "&#8377;50 lakh or more"],
             ["Rent or property price paid to an NRI", "195", "393(2)", "Rates for non-residents (with surcharge and cess)", "No threshold"]])
         + '<p>The rules apply to amounts paid or credited on or after 1 April 2026. Old section numbers still apply to earlier payments. Full mapping: ' + L("income-tax-act-2025-section-mapping-old-vs-new-54-is-82-80c-is-123-nri.html", "old vs new section numbers") + ' and ' + L("old-vs-new-income-tax-form-numbers-2026-15ca-145-15cb-146-10f-41.html", "old vs new form numbers") + '.</p>'),
        ("/ How it works in practice", "Tenants, landlords and buyers.",
         ul("<strong>Salaried tenant paying over &#8377;50,000 a month:</strong> deduct 2% once, with the last month&rsquo;s rent of the tax year or of the tenancy, and the TDS cannot exceed that last month&rsquo;s rent. No TAN is needed; pay through the challan-cum-statement on the e-filing portal and give the landlord the TDS certificate.",
            "<strong>Company, firm or audited business paying office rent:</strong> deduct 10% when rent is credited or paid, whichever is earlier, deposit monthly and report in the quarterly TDS statement.",
            "<strong>House rent allowance:</strong> a tenant claiming HRA who pays over &#8377;1 lakh a year should also have the landlord&rsquo;s PAN; deducting TDS where required protects the claim.",
            "<strong>Landlord without PAN:</strong> higher TDS can apply, up to the rent for the last month in the individual-tenant case.",
            "<strong>Property buyer:</strong> deduct 1% from each payment where the value is &#8377;50 lakh or more, pay through the property challan-cum-statement and issue the certificate to the seller. Buying from an NRI? See " + L("nri-selling-indian-property-capital-gains.html", "NRI property sale tax") + " and " + L("nri-property-sale-tds-calculator-lower-deduction-certificate-savings.html", "the property TDS calculator") + ".")
         + call_box("TDS on rent or property", ["Which section and rate applies",
                                                "TDS for NRI landlords and sellers",
                                                "Lower TDS certificate (Form 128)",
                                                "Correcting missed or short TDS",
                                                "Landlord&rsquo;s return and refund"],
                    "who pays whom, the amount and residential status.")
         + sources("Income-tax Act, 2025, section 393 (Income Tax Department section and TDS rate pages); Income Tax Department FAQs on TDS on rent and on TDS; Taxmann, TDS on rent under the Income-tax Act, 2025; Taxguru TDS mapping table; CAclubindia, TDS on rent for FY 2026-27. Checked 25 November 2026.")),
    ],
    faqs=[("What is the TDS on rent limit for FY 2026-27?", "TDS applies when rent exceeds Rs 50,000 for a month or part of a month. Individuals and HUFs not under tax audit deduct 2%; other payers deduct 10% on land, buildings and furniture and 2% on plant and machinery."),
          ("Which section replaced 194-IB under the Income-tax Act, 2025?", "Section 393(1), Table Sl. No. 2(i), from 1 April 2026. It keeps the 2% rate on rent above Rs 50,000 a month paid by individuals and HUFs not under audit, deducted once with the last month's rent of the year or tenancy."),
          ("Which section replaced 194-I?", "Section 393(1), Table Sl. No. 2(ii): 10% on rent for land, buildings, furniture or fittings and 2% on plant, machinery or equipment, where rent exceeds Rs 50,000 for a month or part of a month."),
          ("What is the new section for 194-IA TDS on property purchase?", "Section 393(1), Table Sl. No. 3(i): the buyer deducts 1% of the price or stamp duty value, whichever is higher, where it is Rs 50 lakh or more and the seller is resident."),
          ("How much TDS is deducted on rent paid to an NRI landlord?", "Rent paid to an NRI falls under section 393(2) (old 195), not the resident rent entries. There is no Rs 50,000 threshold, the tenant needs a TAN, and TDS is at the rates for non-residents plus surcharge and cess unless a lower certificate applies."),
          ("Can BQP help with TDS on rent or property?", "Yes. CA Durgesh Chavda can confirm the section and rate, handle TDS for NRI landlords and sellers, apply for lower TDS certificates and fix missed TDS. " + C)],
    related=[("nri-rental-income-india-tenant-tds-31-2-percent-tan-form-144-2026.html", "TDS on rent paid to an NRI"),
             ("nri-rental-income-tds-refund-calculator-31-2-percent-vs-actual-tax-2026.html", "NRI rent TDS refund calculator"),
             ("nil-lower-tds-certificate-form-128-formerly-form-13-section-395-how-to-apply-2026.html", "Lower TDS certificate"),
             ("income-tax-act-2025-section-mapping-old-vs-new-54-is-82-80c-is-123-nri.html", "Old vs new section numbers"),
             ("tax-rates-in-india-2026-27-income-tax-slabs-percentage-corporate-gst-capital-gains-nri.html", "Tax rates 2026-27")],
    cta_h="Paying or receiving rent, or buying property?", cta_b=C,
    keywords="TDS on rent limit FY 2026-27, TDS on rent section 393, 194IB new section, 194I new section, 194IA new section, section 194IA and 194IB, TDS on rent 50000 per month, TDS on property purchase 1 percent, TDS on rent NRI landlord",
    desc="TDS on rent for FY 2026-27 under section 393: Rs 50,000 a month limit, 2% for individual tenants (old 194-IB), 10% / 2% for others (old 194-I), 1% on property of Rs 50 lakh+ (old 194-IA), NRI landlords under 393(2).",
    howto={"name": "How to deduct TDS on rent in 2026-27", "description": "For a tenant paying more than Rs 50,000 a month.", "steps": [
        {"name": "Check the landlord's status", "text": "Resident or NRI; NRI rent falls under section 393(2)."},
        {"name": "Check your category", "text": "Individual or HUF not under audit (2%, once a year) or other payer (10% / 2%)."},
        {"name": "Deduct at the right time", "text": "Last month's rent for individual tenants; on credit or payment for others."},
        {"name": "Deposit and report", "text": "Challan-cum-statement for individuals; monthly deposit and quarterly statement for others."},
        {"name": "Issue the TDS certificate", "text": "So the landlord can claim credit in the return."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch HJ complete")
