# -*- coding: utf-8 -*-
"""Batch HR (25 Nov 2026): HRA exemption 2026 - formula (least of three), 50% cities extended from four to eight
(Bengaluru, Hyderabad, Pune, Ahmedabad added) under the Income-tax Rules, 2026 (rule 279, replacing rule 2A) from tax year
2026-27, 40% elsewhere; not available in the new regime; salary definition; landlord PAN; no HRA -> section 80GG.
Demand: sweep ac101 (25 Nov 2026), all 7 markets: "hra exemption", "hra exemption calculator", "hra exemption formula",
"hra exemption under which section", "hra exemption in new regime", "hra exemption conditions".
Facts (checked 25 Nov 2026): Moneylife, Siasat, BDO, Deccan Herald, Angel One, Oracle PeopleSoft notes on the Income-tax
Rules, 2026 (notified March 2026; eight cities at 50%; others 40%; rule 279 maps old rule 2A); Taxguru on section 10(13A)
of the 1961 Act. Section number in the 2025 Act not stated (sources conflict)."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 25 November 2026."
SLUG = "hra-exemption-2026-formula-calculation-8-metro-cities-50-percent-new-regime-section-10-13a"

C = contact("your city, basic salary and DA, HRA received, rent paid, the tax regime you chose and the tax year")
L = lambda h, t: f'<a href="{h}">{t}</a>'
PAGES = [dict(
    slug=SLUG,
    title="HRA Exemption 2026: Formula, Calculation, 8 Metro Cities at 50%, New Regime Rule and Which Section Applies",
    em="Bengaluru, Hyderabad, Pune and Ahmedabad now count as metros.",
    kicker="/ Salaried employees &middot; Income tax &middot; Updated 2026-11-25",
    lead=("<strong>House rent allowance (HRA) is exempt up to the least of three amounts: the HRA actually received, rent paid minus 10% of salary, and 50% of salary in a metro city or 40% elsewhere.</strong> "
          "From tax year 2026-27, the Income-tax Rules, 2026 widen the 50% list from four cities (Mumbai, Delhi, Kolkata, Chennai) to eight, adding Bengaluru, Hyderabad, Pune and Ahmedabad. "
          "The exemption is available only under the old tax regime; under the default new regime HRA is fully taxable. It was section 10(13A) of the 1961 Act and continues under the Income-tax Act, 2025."),
    sections=[
        ("/ Quick answers", "What salaried people search for.",
         ul("<strong>What is the HRA exemption formula?</strong> The least of (1) actual HRA received, (2) rent paid minus 10% of salary, and (3) 50% of salary for the eight metro cities or 40% for other cities.",
            "<strong>What counts as salary?</strong> Basic pay plus dearness allowance that forms part of retirement benefits, plus any commission fixed as a percentage of turnover, for the period you lived in rented housing.",
            "<strong>Which cities get 50%?</strong> From tax year 2026-27: Mumbai, Delhi, Kolkata, Chennai, Bengaluru, Hyderabad, Pune and Ahmedabad. For FY 2025-26 (the return filed in 2026), only the original four.",
            "<strong>Is HRA exempt in the new regime?</strong> No. The new regime does not allow the HRA exemption; compare regimes before choosing.",
            "<strong>Under which section?</strong> Section 10(13A) of the Income-tax Act, 1961, with the city list in rule 2A; from 1 April 2026 the exemption continues under the Income-tax Act, 2025, with the city list in rule 279 of the Income-tax Rules, 2026.",
            "<strong>I do not get HRA. Can I still claim rent?</strong> Under the old regime, possibly under section 80GG with Form 10BA; see " + L("form-10ba-house-rent-self-certification-section-80gg.html", "section 80GG and Form 10BA") + ".")),
        ("/ Worked example", "Tax year 2026-27, old regime.",
         table(["Item", "Bengaluru employee (metro from 2026-27)", "Same pay in a non-metro city"], [
             ["Basic + DA for the year", "&#8377;12,00,000", "&#8377;12,00,000"],
             ["HRA received", "&#8377;6,00,000", "&#8377;6,00,000"],
             ["Rent paid", "&#8377;4,80,000", "&#8377;4,80,000"],
             ["(1) Actual HRA", "&#8377;6,00,000", "&#8377;6,00,000"],
             ["(2) Rent minus 10% of salary", "&#8377;3,60,000", "&#8377;3,60,000"],
             ["(3) 50% / 40% of salary", "&#8377;6,00,000 (50%)", "&#8377;4,80,000 (40%)"],
             ["Exempt HRA (least)", "&#8377;3,60,000", "&#8377;3,60,000"]])
         + '<p>Here the rent test is the binding limit, so the new metro status does not change the answer. It helps when rent is high relative to salary, because the 50% cap then rises above the 40% cap. Illustration only; figures are hypothetical.</p>'),
        ("/ Claiming it correctly", "Proof and pitfalls.",
         ul("<strong>Rent receipts and agreement:</strong> give them to your employer for the TDS calculation, or claim in your return if the employer did not allow it.",
            "<strong>Landlord&rsquo;s PAN:</strong> needed when annual rent exceeds &#8377;1 lakh.",
            "<strong>Paying rent to parents:</strong> allowed if the arrangement is genuine, the parent owns the house and reports the rent as income.",
            "<strong>Living in your own house:</strong> no HRA exemption for a period when you live in a house you own.",
            "<strong>Rent above &#8377;50,000 a month:</strong> the tenant may have to deduct TDS; see " + L("tds-on-rent-limit-fy-2026-27-section-393-194ib-194i-194ia-property-purchase-1-percent-nri-landlord.html", "TDS on rent for FY 2026-27") + ".",
            "<strong>Choosing a regime:</strong> HRA is one of the main reasons the old regime can still win; see " + L("tax-rates-in-india-2026-27-income-tax-slabs-percentage-corporate-gst-capital-gains-nri.html", "tax rates for 2026-27") + ".")
         + call_box("HRA and salary tax", ["HRA exemption working",
                                           "Old vs new regime comparison",
                                           "Rent paid to family members",
                                           "Section 80GG where no HRA",
                                           "Correcting HRA in your return"],
                    "your city, salary, HRA, rent and regime.")
         + sources("Income-tax Act, 1961, section 10(13A) and rule 2A; Income-tax Act, 2025 and Income-tax Rules, 2026 (rule 279) as reported by Moneylife, BDO India, Deccan Herald, Siasat, Angel One and Oracle PeopleSoft payroll notes; Taxguru commentary. Section number under the 2025 Act should be confirmed against the Act text. Checked 25 November 2026.")),
    ],
    faqs=[("What is the HRA exemption formula?", "HRA is exempt up to the least of the actual HRA received, rent paid minus 10% of salary, and 50% of salary in a metro city or 40% in other cities. Salary means basic plus dearness allowance forming part of retirement benefits, plus turnover-based commission."),
          ("Which cities get 50% HRA exemption from 2026-27?", "Under the Income-tax Rules, 2026, eight cities: Mumbai, Delhi, Kolkata, Chennai, Bengaluru, Hyderabad, Pune and Ahmedabad. All other cities use 40%."),
          ("Can I claim HRA exemption in the new tax regime?", "No. The HRA exemption is available only under the old tax regime. Under the new regime HRA is fully taxable."),
          ("Under which section is HRA exempt?", "Section 10(13A) of the Income-tax Act, 1961, with the city list in rule 2A. From 1 April 2026 it continues under the Income-tax Act, 2025, with the city list in rule 279 of the Income-tax Rules, 2026."),
          ("Can I claim HRA if I pay rent to my parents?", "Yes, if the arrangement is genuine, the parent owns the property, rent is actually paid and the parent reports it as income. Keep a rent agreement and bank records."),
        ("Can I claim HRA without rent receipts?", "Only if you can still prove the rent was actually paid. HRA exemption (old regime only) is for rent you really pay for a home you live in, and your employer will usually ask for rent receipts or the rent agreement before allowing it in TDS, plus the landlord's PAN where annual rent is above INR 1 lakh. If the employer did not allow it, you can still claim it in your return, but keep the rent agreement, bank transfer records and receipts signed by the landlord; cash rent with no paper trail, or rent to a relative who does not show it as income, is exactly what the department's HRA verification campaigns question. Book a call to check the claim before you file."),
          ("Can BQP check my HRA and regime choice?", "Yes. CA Durgesh Chavda can work out your HRA exemption, compare the old and new regimes and fix HRA claims in your return. " + C)],
    related=[("form-10ba-house-rent-self-certification-section-80gg.html", "Section 80GG and Form 10BA"),
             ("tds-on-rent-limit-fy-2026-27-section-393-194ib-194i-194ia-property-purchase-1-percent-nri-landlord.html", "TDS on rent FY 2026-27"),
             ("tax-rates-in-india-2026-27-income-tax-slabs-percentage-corporate-gst-capital-gains-nri.html", "Tax rates 2026-27"),
             ("section-80c-complete-list-india-2026.html", "Section 80C list"),
             ("income-tax-act-2025-section-mapping-old-vs-new-54-is-82-80c-is-123-nri.html", "Old vs new section numbers")],
    cta_h="Not sure how much HRA is exempt?", cta_b=C,
    keywords="HRA exemption, HRA exemption calculator, HRA exemption formula, HRA exemption under which section, HRA exemption in new regime, HRA exemption conditions, HRA 50 percent cities 2026, HRA Bengaluru metro, section 10(13A)",
    desc="HRA exemption 2026: least of actual HRA, rent minus 10% of salary, and 50% (8 metros incl. Bengaluru, Hyderabad, Pune, Ahmedabad from 2026-27) or 40% of salary; not in the new regime; section 10(13A) and rule 279.",
    howto={"name": "How to calculate HRA exemption", "description": "Under the old regime.", "steps": [
        {"name": "Work out salary", "text": "Basic plus DA forming part of retirement benefits, plus turnover commission."},
        {"name": "Take actual HRA received", "text": "For the months you paid rent."},
        {"name": "Compute rent minus 10% of salary", "text": "For the same period."},
        {"name": "Apply 50% or 40% of salary", "text": "50% for the eight metro cities from 2026-27, else 40%."},
        {"name": "Exempt the lowest of the three", "text": "The rest of the HRA is taxable."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch HR complete")
