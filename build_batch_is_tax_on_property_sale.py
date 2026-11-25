# -*- coding: utf-8 -*-
"""Batch IS (25 Nov 2026): tax on property sale in India 2026 for residents - land / building held more than 24 months:
LTCG 12.5% without indexation; for land or buildings acquired before 23 July 2024, resident individuals and HUFs may
instead pay 20% with indexation, whichever is lower (Finance (No. 2) Act, 2024); held 24 months or less: slab; cost =
purchase price + stamp duty + registration + brokerage + improvements (FMV on 1 April 2001 for older property, capped
at stamp duty value); stamp duty value replaces consideration if it exceeds it by more than 10% (section 50C); buyer
deducts 1% TDS where consideration is Rs 50 lakh or more (194-IA); exemptions: section 54 (now 82), 54F, 54EC bonds
(now section 85: within 6 months, Rs 50 lakh, 5-year lock-in), CGAS; advance tax on the gain.
Demand: sweep ac113 (25 Nov 2026), all 7 markets: "tax on property sale", "tax on property sale profit", "tax on
property sale in india", "tax on property sale calculator".
Facts: site pages on section 54 / 82, 54EC / 85, NRI property sale and the 54 vs 54F vs 54EC decision tree; property
LTCG rules as stated across the site (12.5% / 20%-with-indexation option for resident individuals and HUFs)."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 25 November 2026."
SLUG = "tax-on-property-sale-india-2026-residents-ltcg-12-5-or-20-indexation-calculation-tds-save-tax"

C = contact("the purchase date and cost (with stamp duty and improvement bills), the sale price and stamp duty value, any reinvestment you plan, and whether you are resident or NRI")
L = lambda h, t: f'<a href="{h}">{t}</a>'
PAGES = [dict(
    slug=SLUG,
    title="Tax on Property Sale in India 2026: 12.5% LTCG or 20% With Indexation, How to Calculate the Profit, 1% TDS and How to Save Tax",
    em="hold more than two years and the rate drops to 12.5%.",
    kicker="/ Resident property sellers &middot; Capital gains &middot; Updated 2026-11-25",
    lead=("<strong>Profit on selling a house, flat or land held for more than 24 months is taxed at 12.5% without indexation; if you bought it before 23 July 2024, a resident individual or HUF can instead pay 20% with indexation, whichever is lower.</strong> "
          "Property sold within 24 months is taxed at your slab rate. The buyer deducts 1% TDS when the price is &#8377;50 lakh or more, and the gain can be saved by buying another house or investing in capital gains bonds."),
    sections=[
        ("/ Rates and rules", "Resident individuals and HUFs.",
         table(["Point", "Rule"], [
             ["Held more than 24 months", "Long-term: 12.5% without indexation"],
             ["Bought before 23 July 2024", "Option of 20% with indexation, whichever tax is lower"],
             ["Held 24 months or less", "Short-term: added to income at slab rate"],
             ["Cost of acquisition", "Price + stamp duty + registration + brokerage + improvement costs"],
             ["Bought before 1 April 2001", "Fair market value on 1 April 2001 (capped at stamp duty value) can be used as cost"],
             ["Sale below stamp duty value", "Stamp duty value is used if it exceeds the price by more than 10% (section 50C)"],
             ["TDS by buyer", "1% where the price is &#8377;50 lakh or more (section 194-IA); claim it in your return"]])
         + '<p>NRIs pay 12.5% without the indexation option and face higher TDS; see ' + L("nri-selling-indian-property-capital-gains.html", "NRI property sale tax") + '.</p>'),
        ("/ How to calculate the profit (illustrative)", "Flat bought in 2015, sold in November 2026.",
         table(["Item", "Amount"], [
             ["Sale price", "&#8377;1,00,00,000"],
             ["Cost (price, stamp duty, registration)", "&#8377;40,00,000"],
             ["Long-term gain without indexation", "&#8377;60,00,000"],
             ["Tax at 12.5% plus 4% cess", "&#8377;7,80,000"],
             ["Compare: indexed cost and 20% tax", "Use the cost inflation index for 2015-16 and the sale year; pay the lower tax"]])
         + '<p>Surcharge applies if total income is above &#8377;50 lakh. Pay advance tax on the gain in the instalment after the sale; see ' + L("advance-tax-q3-december-15-2026-india.html", "advance tax dates") + '.</p>'),
        ("/ How to save tax on property sale", "Exemptions and planning.",
         ul("<strong>Buy another house (section 54, now section 82):</strong> reinvest the long-term gain on a residential house in a new house within 1 year before or 2 years after the sale (3 years if constructing), up to &#8377;10 crore; see " + L("section-54-exemption-house-property-capital-gains-conditions-10-crore-limit-cgas-section-82-2026.html", "section 54 rules") + ".",
            "<strong>Sold land or a commercial property (section 54F):</strong> invest the full net sale proceeds in a residential house to exempt the gain proportionately.",
            "<strong>Capital gains bonds (54EC, now section 85):</strong> invest up to &#8377;50 lakh within 6 months in specified bonds with a 5-year lock-in; see " + L("54ec-bonds-section-85-capital-gains-bonds-lock-in-interest-rate-limit-nri-2026.html", "54EC bonds") + ".",
            "<strong>Not ready to buy before filing:</strong> deposit the amount in the Capital Gains Account Scheme before the return due date.",
            "<strong>Which option fits:</strong> see the " + L("which-section-54-vs-54f-vs-54ec-decision-tree-india.html", "54 vs 54F vs 54EC decision tree") + ".",
            "<strong>Keep records:</strong> purchase deed, stamp duty receipts, improvement bills and the sale deed support the cost and the gain.")
         + call_box("Property sale tax", ["Capital gain computation (12.5% vs 20% indexed)",
                                           "Section 54 / 54F / 54EC planning",
                                           "Stamp duty value disputes (50C)",
                                           "TDS credit and advance tax",
                                           "ITR Schedule CG"],
                    "your purchase and sale documents.")
         + sources("Income-tax Act, 1961 sections 45, 48, 50C, 54, 54EC, 54F, 112 and 194-IA as amended by the Finance (No. 2) Act, 2024, carried into the Income-tax Act, 2025 (sections 82 and 85 for 54 and 54EC); site guides on section 54, 54EC bonds and NRI property sales. Checked 25 November 2026.")),
    ],
    faqs=[("How much tax do I pay on selling a property in India?", "If held for more than 24 months, 12.5% of the gain without indexation; residents who bought before 23 July 2024 can choose 20% with indexation if that is lower. If held for 24 months or less, the gain is taxed at your slab rate."),
          ("How do I calculate profit on a property sale?", "Sale price (or stamp duty value, if it exceeds the price by more than 10%) minus the cost of acquisition, which includes the purchase price, stamp duty, registration, brokerage and improvement costs; for indexation, the cost is adjusted with the cost inflation index."),
          ("Is TDS deducted when I sell property?", "Yes. A resident buyer deducts 1% TDS under section 194-IA when the price is Rs 50 lakh or more and deposits it against your PAN; you claim it in your return."),
          ("How can I avoid tax on property sale?", "Reinvest the gain in a residential house under section 54 (section 82 of the 2025 Act), invest the net proceeds under 54F if you sold land or commercial property, or buy up to Rs 50 lakh of 54EC bonds within 6 months."),
          ("Is the 20% indexation option available to NRIs?", "No. The option of 20% with indexation for property bought before 23 July 2024 is available only to resident individuals and HUFs; NRIs pay 12.5% without indexation."),
          ("Can BQP compute tax on my property sale?", "Yes. CA Durgesh Chavda can compute the gain under both methods, plan reinvestment, handle TDS credit and file your return. " + C)],
    related=[("section-54-exemption-house-property-capital-gains-conditions-10-crore-limit-cgas-section-82-2026.html", "Section 54 exemption"),
             ("54ec-bonds-section-85-capital-gains-bonds-lock-in-interest-rate-limit-nri-2026.html", "54EC bonds"),
             ("which-section-54-vs-54f-vs-54ec-decision-tree-india.html", "54 vs 54F vs 54EC"),
             ("nri-selling-indian-property-capital-gains.html", "NRI property sale tax"),
             ("advance-tax-q3-december-15-2026-india.html", "Advance tax dates")],
    cta_h="Selling a property?", cta_b=C,
    keywords="tax on property sale, tax on property sale in india, tax on property sale profit, property sale capital gains tax 2026, LTCG 12.5% property, 20% indexation property, TDS 194-IA 1%, save tax on property sale",
    desc="Tax on property sale in India 2026: 12.5% LTCG after 24 months or 20% with indexation for property bought before 23 July 2024 (residents), slab rate if sooner, profit calculation, 50C, 1% TDS, sections 54 / 54F / 54EC to save tax.",
    howto={"name": "How to work out tax on a property sale", "description": "For resident individuals and HUFs.", "steps": [
        {"name": "Check the holding period", "text": "More than 24 months is long-term."},
        {"name": "Work out the cost", "text": "Price, stamp duty, registration, brokerage, improvements."},
        {"name": "Compute the gain both ways", "text": "12.5% without indexation vs 20% with indexation (pre-23 July 2024 purchases)."},
        {"name": "Plan exemptions", "text": "Section 54, 54F, 54EC bonds or the CGAS."},
        {"name": "Pay and report", "text": "Advance tax on the balance after TDS; Schedule CG in the return."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch IS complete")
