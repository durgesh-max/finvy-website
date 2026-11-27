# -*- coding: utf-8 -*-
"""Batch IH (25 Nov 2026): section 54 exemption (section 82 of the Income-tax Act, 2025 from tax year 2026-27) - long-term
capital gain on sale of a residential house by an individual or HUF exempt if invested in a residential house in India:
purchase 1 year before or 2 years after the sale, or construction within 3 years; exemption = lower of gain and cost of
new house; cost / gain above Rs 10 crore ignored (from AY 2024-25); option to invest in two houses once in a lifetime
where the gain does not exceed Rs 2 crore; unutilised amount in the Capital Gains Account Scheme before the return due
date; new house sold within 3 years -> exemption reversed; available under the new regime (capital gains exemptions are
not among those withdrawn). Sale of land / other assets -> section 54F (net consideration), agricultural land -> 54B,
bonds -> 54EC.
Demand: sweep ac109 (25 Nov 2026), all 7 markets: "section 54 exemption", "conditions", "limit", "in new tax regime",
"chart", "calculation", "on sale of land", "capital gain", "list".
Facts (checked 25 Nov 2026): Income Tax Department section 82 pages; CAclubindia text of section 82 ('profit on sale of
property used for residence'); TMI notes; eBizFiling and AUBSP on section 82; site decision-tree page (Rs 10 crore cap
from 1 April 2023) and 54EC page."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 25 November 2026."
SLUG = "section-54-exemption-house-property-capital-gains-conditions-10-crore-limit-cgas-section-82-2026"

C = contact("sale date and price of the house, purchase date and cost, the new house (purchase or construction) and whether you are resident or NRI")
L = lambda h, t: f'<a href="{h}">{t}</a>'
PAGES = [dict(
    slug=SLUG,
    title="Section 54 of Income Tax Act (Now Section 82): Exemption on Sale of House Property - Conditions, Rs 10 Crore Limit, Two Houses, CGAS, NRIs, New Regime (2026)",
    em="reinvest in a house, on time, and keep it for three years.",
    kicker="/ Individuals and HUFs selling a house &middot; Capital gains &middot; Updated 2026-11-25",
    lead=("<strong>Section 54 exempts the long-term capital gain on selling a residential house if the gain is invested in another residential house in India: bought within one year before or two years after the sale, or constructed within three years.</strong> "
          "From tax year 2026-27 the same relief is in section 82 of the Income-tax Act, 2025. It is available to individuals and HUFs, resident or non-resident, and under both the old and the new tax regime. "
          "The exemption is the lower of the capital gain and the cost of the new house, with anything above &#8377;10 crore ignored. Money not invested by the return due date must be parked in the Capital Gains Account Scheme."),
    sections=[
        ("/ Quick answers", "What people search for.",
         ul("<strong>What are the section 54 conditions?</strong> The house sold was a residential house held for more than 24 months; the seller is an individual or HUF; the new residential house is in India and is bought or built within the time limits.",
            "<strong>What is the section 54 exemption limit?</strong> The exemption is limited to the cost of the new house, and cost or gain above &#8377;10 crore is not counted.",
            "<strong>Can I buy two houses?</strong> Once in a lifetime, if the capital gain does not exceed &#8377;2 crore, the gain can be invested in two residential houses.",
            "<strong>Is section 54 available in the new tax regime?</strong> Yes. The new regime removes deductions such as 80C and HRA, but capital gains exemptions under sections 54, 54F and 54EC remain available.",
            "<strong>What if I cannot buy before filing my return?</strong> Deposit the unused gain in the Capital Gains Account Scheme with an authorised bank before the return due date and claim the exemption; use it within the time limit or it becomes taxable.",
            "<strong>Section 54 on sale of land?</strong> Section 54 applies only to a residential house sold. For land or other assets use section 54F (invest the net sale consideration in a house) or 54EC bonds; see the " + L("which-section-54-vs-54f-vs-54ec-decision-tree-india.html", "54 vs 54F vs 54EC decision tree") + ".")),
        ("/ Calculation example (illustrative)", "Lower of gain and new house cost.",
         table(["Item", "Amount"], [
             ["Sale price of old house", "&#8377;1.5 crore"],
             ["Cost of old house", "&#8377;70 lakh"],
             ["Long-term capital gain", "&#8377;80 lakh"],
             ["New house bought within 2 years", "&#8377;60 lakh"],
             ["Exemption under section 54 / 82", "&#8377;60 lakh"],
             ["Taxable gain", "&#8377;20 lakh at 12.5%"]])
         + '<p>Figures are illustrative; surcharge and cess apply. Gains on property are taxed at 12.5% without indexation after 24 months; see ' + L("tax-rates-in-india-2026-27-income-tax-slabs-percentage-corporate-gst-capital-gains-nri.html", "tax rates 2026-27") + '.</p>'),
        ("/ Traps that cost the exemption", "Watch these.",
         ul("<strong>Selling the new house within three years:</strong> the exemption is reversed by reducing the cost of the new house, so the gain becomes taxable on that sale.",
            "<strong>House abroad:</strong> the new house must be in India.",
            "<strong>Missing the CGAS deposit:</strong> without a deposit before the return due date, the uninvested part is taxable.",
            "<strong>Over the cap:</strong> amounts above &#8377;10 crore get no exemption; consider 54EC bonds for part of the gain, see " + L("54ec-bonds-section-85-capital-gains-bonds-lock-in-interest-rate-limit-nri-2026.html", "54EC bonds") + ".",
            "<strong>NRIs:</strong> the exemption applies, but the buyer deducts TDS on the sale; a lower deduction certificate can reflect the reinvestment, see " + L("nri-selling-indian-property-capital-gains.html", "NRI capital gains on property") + ".")
         + call_box("Section 54 planning", ["Eligibility and time limits",
                                             "CGAS deposit before filing",
                                             "Two-house option check",
                                             "54 vs 54F vs 54EC choice",
                                             "NRI sales and lower TDS"],
                    "the sale and the planned reinvestment.")
         + sources("Income-tax Act, 1961, sections 54, 54B, 54EC and 54F; Income-tax Act, 2025, section 82 (Income Tax Department section pages; CAclubindia text); Capital Gains Accounts Scheme, 1988; TMI notes, eBizFiling and AUBSP commentary on section 82. Checked 25 November 2026.")),
    ],
    faqs=[("What is the section 54 exemption?", "An exemption from tax on the long-term capital gain from selling a residential house, if the gain is invested in another residential house in India within the time limits. From tax year 2026-27 it is section 82 of the Income-tax Act, 2025."),
          ("What are the conditions for section 54?", "The seller is an individual or HUF; the house sold was held for more than 24 months; the new residential house in India is bought within one year before or two years after the sale, or constructed within three years; and the new house is not sold within three years."),
        ("Is section 54 available to an NRI?", "Yes. Section 54 (now section 82) applies to any individual or HUF, whatever the residential status, so an NRI selling a house in India can claim it on the same conditions - including that the new house must be in India, not abroad. The exemption does not stop the buyer deducting TDS on the whole price under section 393 (old 195): either get a Form 128 (old Form 13) lower TDS certificate before the sale, showing the planned reinvestment, or claim the excess TDS back as a refund in your ITR-2 for the year."),
          ("What is the maximum exemption under section 54?", "The lower of the capital gain and the cost of the new house, with any cost or gain above Rs 10 crore ignored."),
          ("Is section 54 available under the new tax regime?", "Yes. Capital gains exemptions under sections 54, 54F and 54EC (and their 2025 Act counterparts) are available under both the old and new regimes."),
          ("Can I claim section 54 for two houses?", "Yes, once in a lifetime, if the long-term capital gain does not exceed Rs 2 crore. Otherwise the exemption is for one residential house."),
        ("What is the Capital Gains Account Scheme and how does it work?", "It is a 1988 government scheme run through authorised bank branches for gains you have not reinvested by the return due date. You deposit the unused amount before the due date (31 July for most individuals not needing an audit) and claim the exemption in the return. Account A works like a savings account for withdrawals as you pay for the house; Account B is a term deposit. The money must be used for the new house within two years of the sale for a purchase, or three years for construction; whatever is unused then becomes taxable as long-term capital gain in the year the period ends. Withdrawals and closure follow the forms prescribed under the scheme, and closing with an unused balance needs the Assessing Officer's approval."),
        ("Can an NRI open a Capital Gains Account Scheme account?", "Yes. The scheme is open to any taxpayer claiming exemption under sections 54, 54F and similar provisions (now sections 82 and 86), including non-residents. Open it at an authorised branch of a bank that runs the scheme (rural branches are not authorised) and deposit from the sale proceeds before the return due date; check the bank's KYC requirements for non-residents first. Keep the deposit receipt with your ITR papers, and remember the buyer's TDS on the sale is separate - a Form 128 lower TDS certificate before the sale avoids excess tax being withheld."),
          ("Can BQP help me claim section 54?", "Yes. CA Durgesh Chavda can check eligibility, plan the reinvestment and CGAS deposit, and handle NRI sales and lower TDS certificates. " + C)],
    related=[("which-section-54-vs-54f-vs-54ec-decision-tree-india.html", "54 vs 54F vs 54EC decision tree"),
             ("54ec-bonds-section-85-capital-gains-bonds-lock-in-interest-rate-limit-nri-2026.html", "54EC bonds"),
             ("nri-selling-indian-property-capital-gains.html", "NRI capital gains on property"),
             ("best-ca-nri-property-sale-section-54-reinvestment.html", "NRI property sale and section 54"),
             ("tax-rates-in-india-2026-27-income-tax-slabs-percentage-corporate-gst-capital-gains-nri.html", "Tax rates 2026-27")],
    cta_h="Selling a house and reinvesting?", cta_b=C,
    keywords="section 54 exemption, section 54 conditions, section 54 exemption limit, section 54 new tax regime, section 54 two houses, section 54 calculation, section 82 Income-tax Act 2025, capital gains account scheme, section 54 on sale of land",
    desc="Section 54 exemption (section 82 of the 2025 Act): long-term gain on a house reinvested in a house in India within 1-2 years (purchase) or 3 years (construction), Rs 10 crore limit, two-house option up to Rs 2 crore gain, CGAS, new regime, calculation, 3-year lock-in.",
    howto={"name": "How to claim section 54", "description": "After selling a residential house.", "steps": [
        {"name": "Confirm long-term", "text": "House held more than 24 months."},
        {"name": "Compute the gain", "text": "Sale price minus cost and transfer expenses."},
        {"name": "Reinvest in a house", "text": "Buy within 1 year before / 2 years after, or build within 3 years."},
        {"name": "Use CGAS if needed", "text": "Deposit unused gain before the return due date."},
        {"name": "Hold for 3 years", "text": "Selling earlier reverses the exemption."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch IH complete")
