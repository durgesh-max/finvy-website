# -*- coding: utf-8 -*-
"""Batch IL (25 Nov 2026): agricultural income tax India 2026 - agricultural income from land in India is exempt from
central income tax but, for individuals / HUFs / AOPs / BOIs, partial integration applies when net agricultural income
exceeds Rs 5,000 and non-agricultural income exceeds the basic exemption limit: tax on (non-agri + agri) minus tax on
(agri + basic exemption limit); applies in both regimes (Rs 4 lakh nil slab new regime; Rs 2.5 / 3 / 5 lakh old);
report in Schedule EI; rural agricultural land (outside municipal limits and beyond 2 / 6 / 8 km) is not a capital
asset; urban agricultural land sale taxed as capital gain with section 54B relief; produce sold after processing beyond
what makes it marketable, dairy, poultry etc. are not agricultural income.
Demand: sweep ac111 (25 Nov 2026), 6-7 markets: "agricultural income taxability", "agricultural income tax",
"agricultural income tax rates", "agricultural income tax punjab".
Facts (checked 25 Nov 2026): Income Tax Department 'farmer' page; Bankbazaar, Taxclue (Income-tax Act 2025), TaxHeal
(computation AY 2026-27), RTI wiki summaries; site NRI agricultural land page (partial integration, rural / urban land,
54B)."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 25 November 2026."
SLUG = "agricultural-income-tax-india-2026-exempt-partial-integration-5000-calculation-farmland-sale"

C = contact("your agricultural and non-agricultural income for the year, the land location (rural or urban), and whether you are resident or NRI")
L = lambda h, t: f'<a href="{h}">{t}</a>'
PAGES = [dict(
    slug=SLUG,
    title="Agricultural Income Tax in India 2026: Is It Taxable, Partial Integration Above Rs 5,000, Calculation and Farmland Sale",
    em="exempt itself, but it can raise the tax on everything else.",
    kicker="/ Farmers and landowners &middot; Income tax &middot; Updated 2026-11-25",
    lead=("<strong>Agricultural income from land in India, such as income from growing and selling crops, is exempt from income tax, but if it is more than &#8377;5,000 and your other income is above the basic exemption limit, it is used to push your other income into higher tax slabs through partial integration.</strong> "
          "The tax is worked out as the tax on agricultural plus non-agricultural income, minus the tax on agricultural income plus the basic exemption limit, under whichever regime you use. "
          "Selling rural agricultural land is not taxed as capital gains, but urban agricultural land is."),
    sections=[
        ("/ Quick answers", "What people search for.",
         ul("<strong>Is agricultural income taxable in India?</strong> No, it is exempt, but it is included for rate purposes when it exceeds &#8377;5,000 and other income exceeds the basic exemption limit.",
            "<strong>What counts as agricultural income?</strong> Rent or revenue from agricultural land in India, income from cultivation and the sale of produce in a form that is marketable, and income from farm buildings used for agriculture. Dairy, poultry, fisheries and processed products beyond basic marketability are generally not agricultural income.",
            "<strong>Does partial integration apply under the new regime?</strong> Yes, it applies under both regimes, using that regime&rsquo;s slabs and basic exemption (&#8377;4 lakh in the new regime).",
            "<strong>Where is it reported?</strong> In the exempt income schedule of the return; with agricultural income above &#8377;5,000, use ITR-2 or ITR-3 rather than ITR-1.",
            "<strong>Is selling agricultural land taxable?</strong> Rural agricultural land (outside municipal limits and beyond 2, 6 or 8 km depending on population) is not a capital asset, so no capital gains tax; urban agricultural land is taxed as capital gains, with relief under section 54B on reinvestment in agricultural land.",
            "<strong>NRIs:</strong> see " + L("nri-oci-agricultural-land-india-buy-inherit-sell-tax-fema-2026.html", "NRIs and agricultural land") + " for FEMA limits on buying and inheriting farmland.")),
        ("/ Partial integration example (new regime)", "Non-agricultural income Rs 15 lakh, agricultural Rs 3 lakh.",
         table(["Step", "Calculation", "Tax"], [
             ["1. Tax on Rs 18 lakh (15 + 3)", "New regime slabs", "&#8377;1,60,000"],
             ["2. Tax on Rs 7 lakh (3 + Rs 4 lakh exemption)", "New regime slabs", "&#8377;15,000"],
             ["3. Tax payable before cess", "Step 1 minus step 2", "&#8377;1,45,000"],
             ["Without agricultural income", "Tax on Rs 15 lakh", "&#8377;1,05,000"]])
         + '<p>Illustrative only; 4% cess and surcharge apply on top. Here agricultural income adds &#8377;40,000 of tax on the other income. Compare regimes with the ' + L("new-vs-old-tax-regime-calculator.html", "new vs old regime calculator") + ' and see ' + L("tax-rates-in-india-2026-27-income-tax-slabs-percentage-corporate-gst-capital-gains-nri.html", "tax rates 2026-27") + '.</p>'),
        ("/ Practical points", "Avoid the common mistakes.",
         ul("<strong>Keep evidence:</strong> land records, crop sale receipts (mandi slips or invoices) and expenses, because large agricultural income claims are scrutinised.",
            "<strong>Rent from farmland:</strong> rent from agricultural land is agricultural income; rent from a farmhouse not used for agriculture is house property income.",
            "<strong>Large claims draw notices:</strong> unusually high agricultural income compared with landholding is a common scrutiny trigger; see " + L("section-143-2-scrutiny-notice-response-india.html", "scrutiny notices") + ".",
            "<strong>State levies:</strong> agricultural income tax is a state subject; check whether your state levies any tax on plantation or agricultural income.",
            "<strong>Selling farmland:</strong> confirm rural or urban status from municipal limits and distance before the sale; see " + L("section-54-exemption-house-property-capital-gains-conditions-10-crore-limit-cgas-section-82-2026.html", "capital gains exemptions") + ".")
         + call_box("Agricultural income", ["Partial integration computation",
                                             "ITR with agricultural income",
                                             "Farmland sale and section 54B",
                                             "Scrutiny on agricultural income claims",
                                             "NRI farmland questions"],
                    "your income and land details.")
         + sources("Income-tax Act, 1961 sections 2(1A), 2(14) and 10(1) and the corresponding provisions of the Income-tax Act, 2025; Finance Act rate schedules on partial integration; Income Tax Department guidance for farmers; Bankbazaar, Taxclue, TaxHeal and RTI wiki summaries; site guide on NRIs and agricultural land. Checked 25 November 2026.")),
    ],
    faqs=[("Is agricultural income taxable in India?", "No. Agricultural income from land in India is exempt from income tax, but if it exceeds Rs 5,000 and your other income is above the basic exemption limit, it is aggregated to decide the tax rate on your other income (partial integration)."),
          ("How is tax on agricultural income calculated?", "Compute tax on non-agricultural plus agricultural income, then subtract the tax on agricultural income plus the basic exemption limit. The difference, plus cess, is the tax payable. The method applies under both the old and new regimes."),
          ("Does partial integration apply in the new tax regime?", "Yes. It uses the new regime slabs and its Rs 4 lakh basic exemption."),
          ("Is sale of agricultural land taxable?", "Rural agricultural land outside municipal limits and beyond the 2, 6 or 8 km band is not a capital asset, so its sale is not taxed as capital gains. Urban agricultural land is taxed as capital gains, with relief under section 54B for reinvestment in agricultural land."),
          ("Which ITR do I file with agricultural income?", "If agricultural income is up to Rs 5,000, ITR-1 may be used where otherwise eligible; above that, ITR-2 (or ITR-3 with business income), reporting it in the exempt income schedule."),
          ("Can BQP help with agricultural income tax?", "Yes. CA Durgesh Chavda can compute partial integration, file your return with agricultural income, and advise on farmland sales and scrutiny. " + C)],
    related=[("nri-oci-agricultural-land-india-buy-inherit-sell-tax-fema-2026.html", "NRIs and agricultural land"),
             ("new-vs-old-tax-regime-calculator.html", "New vs old regime calculator"),
             ("tax-rates-in-india-2026-27-income-tax-slabs-percentage-corporate-gst-capital-gains-nri.html", "Tax rates 2026-27"),
             ("section-143-2-scrutiny-notice-response-india.html", "Scrutiny notices"),
             ("section-54-exemption-house-property-capital-gains-conditions-10-crore-limit-cgas-section-82-2026.html", "Section 54 exemption")],
    cta_h="Earning agricultural income?", cta_b=C,
    keywords="agricultural income tax India, is agricultural income taxable, agricultural income taxability, partial integration agricultural income, agricultural income Rs 5000, agricultural land sale tax, agricultural income new regime, agricultural income ITR",
    desc="Agricultural income tax in India 2026: exempt, but partial integration applies when it exceeds Rs 5,000 and other income exceeds the basic exemption; worked example under the new regime, ITR reporting, rural vs urban farmland sale, section 54B.",
    howto={"name": "How partial integration works", "description": "When agricultural income exceeds Rs 5,000.", "steps": [
        {"name": "Check the two triggers", "text": "Agricultural income above Rs 5,000 and other income above the basic exemption."},
        {"name": "Tax on total", "text": "Compute tax on agricultural plus non-agricultural income."},
        {"name": "Tax on agri + exemption", "text": "Compute tax on agricultural income plus the basic exemption limit."},
        {"name": "Subtract", "text": "Difference is the tax payable before cess and rebates."},
        {"name": "Report correctly", "text": "Use ITR-2 / ITR-3 and the exempt income schedule."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch IL complete")
