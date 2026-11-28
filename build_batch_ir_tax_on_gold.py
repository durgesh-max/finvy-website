# -*- coding: utf-8 -*-
"""Batch IR (25 Nov 2026): tax on gold in India 2026 - physical gold, jewellery, coins, bars and digital gold:
long-term after 24 months, LTCG 12.5% without indexation (Finance (No. 2) Act, 2024), short-term at slab; gold ETFs
(listed units): long-term after 12 months at 12.5%, short-term at slab; gold mutual funds / fund of funds: treated as
'other' funds (not over 65% debt) - 12.5% after 24 months, with purchase-date nuances; sovereign gold bonds: 2.5%
interest taxable at slab; redemption gain exempt only for individuals who subscribed at original issue and hold to
maturity (Budget 2026, from 1 April 2026); SGBs bought on the exchange taxed on redemption; listed SGB sale on exchange
12.5% after 12 months; inheritance not taxed, gifts per 56(2)(x); section 54F for LTCG reinvested in a house.
Demand: sweep ac113 (25 Nov 2026), all 7 markets: "tax on gold", "tax on gold etf".
Facts (checked 25 Nov 2026): Kotak Neo (post-Budget 2026 gold / silver tax), Business Today (1-2 Feb 2026), Angel One,
Taxscan, NISM, Freefincal (SGB exemption only for original subscribers held to maturity), Finnovate; site NRI gold page
and mutual fund taxation page."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 25 November 2026."
SLUG = "tax-on-gold-india-2026-jewellery-digital-gold-etf-sovereign-gold-bond-ltcg-12-5-percent"

C = contact("the form of gold (jewellery, coins, digital gold, ETF, gold fund, SGB), purchase dates and cost, sale value, and whether it was bought, inherited or gifted")
L = lambda h, t: f'<a href="{h}">{t}</a>'
PAGES = [dict(
    slug=SLUG,
    title="Tax on Gold in India 2026: Jewellery, Digital Gold, Gold ETF and Sovereign Gold Bonds - 12.5% LTCG, Holding Periods and SGB Rule Change",
    em="the form you hold decides the holding period.",
    kicker="/ Gold investors and families &middot; Capital gains &middot; Updated 2026-11-25",
    lead=("<strong>Profit on selling physical gold, jewellery or digital gold held for more than 24 months is taxed at 12.5% without indexation; if sold sooner, it is added to your income and taxed at your slab rate.</strong> "
          "Gold ETFs become long-term after just 12 months, also at 12.5%. Sovereign gold bond redemptions stay tax-free only for individuals who subscribed at the original issue and hold to maturity; from 1 April 2026 bonds bought on the exchange are taxed on redemption."),
    sections=[
        ("/ Rates by form of gold", "Resident individuals.",
         table(["Form", "Long-term after", "Long-term tax", "Short-term tax"], [
             ["Jewellery, coins, bars, digital gold", "24 months", "12.5%, no indexation", "Slab rate"],
             ["Gold ETF (listed units)", "12 months", "12.5%", "Slab rate"],
             ["Gold mutual fund / fund of funds", "24 months", "12.5%", "Slab rate"],
             ["SGB held from original issue to maturity", "-", "Exempt on redemption", "-"],
             ["SGB bought on the exchange, held to redemption", "12 months", "Taxable on redemption (from 1 April 2026)", "Slab rate"],
             ["SGB interest (2.5% a year)", "-", "Slab rate every year", "Slab rate"]])
         + '<p>Gold fund units bought between 1 April 2023 and 31 March 2025 can be treated differently; see ' + L("mutual-fund-taxation-india-2026-equity-debt-hybrid-ltcg-12-5-stcg-20-examples.html", "mutual fund taxation") + '. NRIs: see ' + L("can-nri-buy-gold-in-india-physical-digital-gold-etf-sgb-tax-repatriation-2026.html", "NRIs and gold") + '.</p>'),
        ("/ Worked example (illustrative)", "Jewellery bought in 2019, sold in November 2026.",
         table(["Item", "Amount"], [
             ["Sale value", "&#8377;7,50,000"],
             ["Cost (2019 purchase bill)", "&#8377;3,00,000"],
             ["Long-term capital gain", "&#8377;4,50,000"],
             ["Tax at 12.5% plus 4% cess", "&#8377;58,500"]])
         + '<p>Making charges and GST paid at purchase form part of cost if supported by the bill. Reinvesting the full net sale proceeds in a residential house can make the gain exempt under section 54F; see ' + L("which-section-54-vs-54f-vs-54ec-decision-tree-india.html", "54 vs 54F vs 54EC") + '.</p>'),
        ("/ Practical points", "Inherited, gifted and old gold.",
         ul("<strong>Inherited jewellery:</strong> no tax on inheriting; on sale, the previous owner&rsquo;s cost and holding period count.",
            "<strong>Gifts:</strong> gold from relatives is exempt; gifts from others worth over &#8377;50,000 in a year are taxed at slab; see " + L("section-56-2-x-gift-tax-india-2026.html", "gift tax rules") + ".",
            "<strong>No bills:</strong> keep purchase invoices or a valuation report; without proof of cost the whole sale value can be questioned.",
            "<strong>Exchanging old jewellery for new:</strong> it is still a sale of the old gold for tax purposes.",
            "<strong>Sale of high-value jewellery:</strong> jewellers report large cash and card transactions, so the sale can appear in your " + L("form-26as-vs-ais-vs-tis-india-2026.html", "AIS") + "; report the gain in your return.",
            "<strong>Rates:</strong> see " + L("tax-rates-in-india-2026-27-income-tax-slabs-percentage-corporate-gst-capital-gains-nri.html", "tax rates 2026-27") + " for slabs and surcharge.")
         + call_box("Gold tax", ["Capital gains on jewellery and digital gold",
                                  "Gold ETF and gold fund redemptions",
                                  "SGB redemption after the 2026 change",
                                  "Section 54F reinvestment",
                                  "ITR Schedule CG"],
                    "your purchase and sale details.")
         + sources("Income-tax Act, 1961 sections 2(42A), 10, 54F and 112 as amended by the Finance (No. 2) Act, 2024 and Finance Act, 2026, carried into the Income-tax Act, 2025; Kotak Neo, Business Today, Angel One, Taxscan, NISM, Freefincal and Finnovate commentary on gold and SGB taxation after Budget 2026. Checked 25 November 2026.")),
    ],
    faqs=[("How is gold taxed in India in 2026?", "Physical gold, jewellery and digital gold held for more than 24 months are taxed at 12.5% without indexation; if sold earlier, the gain is taxed at your slab rate. Gold ETFs are long-term after 12 months, also at 12.5%."),
          ("How are gold ETFs taxed?", "Listed gold ETF units held for more than 12 months are taxed at 12.5% on the gain; units sold within 12 months are taxed at your slab rate."),
          ("Is SGB taxable on maturity - are sovereign gold bonds still tax-free?", "Redemption at maturity is exempt only for individuals who subscribed at the original issue and held the bond until maturity. From 1 April 2026, bonds bought on the stock exchange are taxed on the gain at redemption. The 2.5% interest is always taxable at slab."),
          ("Is interest on sovereign gold bonds taxable?", "Yes. The fixed annual interest on sovereign gold bonds is taxable at your slab rate as income from other sources in the year it is received, under both tax regimes. No TDS is deducted on it, so include it in your return and in advance tax if needed."),
          ("Is selling inherited gold jewellery taxable?", "Inheriting is not taxed, but selling is. The previous owner's purchase cost and holding period are used, so jewellery held for decades usually gives a long-term gain at 12.5%."),
          ("Can I save tax on gold sale profit?", "Yes. Investing the full net sale proceeds of a long-term gold sale in a residential house can make the gain exempt under section 54F, subject to its conditions."),
          ("Can BQP compute tax on my gold sale?", "Yes. CA Durgesh Chavda can compute the gain, check SGB treatment, plan 54F reinvestment and file your return. " + C)],
    related=[("mutual-fund-taxation-india-2026-equity-debt-hybrid-ltcg-12-5-stcg-20-examples.html", "Mutual fund taxation"),
             ("can-nri-buy-gold-in-india-physical-digital-gold-etf-sgb-tax-repatriation-2026.html", "NRIs and gold"),
             ("which-section-54-vs-54f-vs-54ec-decision-tree-india.html", "54 vs 54F vs 54EC"),
             ("section-56-2-x-gift-tax-india-2026.html", "Gift tax rules"),
             ("tax-rates-in-india-2026-27-income-tax-slabs-percentage-corporate-gst-capital-gains-nri.html", "Tax rates 2026-27")],
    cta_h="Selling gold?", cta_b=C,
    keywords="tax on gold india, tax on gold etf, gold capital gains tax 2026, jewellery sale tax, digital gold tax, sovereign gold bond tax budget 2026, gold LTCG 12.5%, gold holding period 24 months",
    desc="Tax on gold in India 2026: jewellery, coins and digital gold 12.5% LTCG after 24 months, gold ETFs after 12 months, gold funds, SGB exemption only for original subscribers held to maturity from April 2026, inherited gold, 54F, worked example.",
    howto={"name": "How to work out tax on selling gold", "description": "For resident individuals.", "steps": [
        {"name": "Identify the form", "text": "Physical / digital gold, ETF, gold fund or SGB."},
        {"name": "Check the holding period", "text": "24 months for physical and funds, 12 months for ETFs and listed SGBs."},
        {"name": "Compute the gain", "text": "Sale value minus documented cost (previous owner's cost if inherited)."},
        {"name": "Apply the rate", "text": "12.5% long-term or slab rate short-term; SGB exemption only if conditions met."},
        {"name": "Consider 54F", "text": "Reinvest in a residential house to exempt long-term gains."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch IR complete")
