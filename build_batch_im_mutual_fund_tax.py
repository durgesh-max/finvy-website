# -*- coding: utf-8 -*-
"""Batch IM (25 Nov 2026): mutual fund taxation in India 2026 with examples - equity-oriented funds (65%+ equity): STCG
(12 months or less) 20%, LTCG 12.5% on gains above Rs 1.25 lakh a year; specified mutual funds (more than 65% in debt
and money market instruments; section 50AA as amended by the Finance (No. 2) Act, 2024, section 76 of the 2025 Act):
units bought on or after 1 April 2023 taxed at slab rates whatever the holding period; debt units bought before
1 April 2023 long-term after 24 months at 12.5% without indexation; other funds (hybrids between, international /
gold funds not over 65% debt): long-term after 24 months at 12.5% without the Rs 1.25 lakh exemption, else slab;
dividends taxed at slab with TDS above the yearly threshold; equity units bought before 1 February 2018 grandfathered
at 31 January 2018 value.
Demand: sweep ac111 (25 Nov 2026), 6 markets: "mutual fund tax", "mutual fund taxation with example".
Facts (checked 25 Nov 2026): ICICI Prudential and Mirae Asset tax reckoners 2026-27; Income Tax Department section 50AA
pages; Freefincal, Finnovate and Taxguru notes; site NRI mutual fund tax page (same rate structure)."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 25 November 2026."
SLUG = "mutual-fund-taxation-india-2026-equity-debt-hybrid-ltcg-12-5-stcg-20-examples"

C = contact("the funds you hold (equity, debt, hybrid, international), purchase dates and amounts, and planned redemptions")
L = lambda h, t: f'<a href="{h}">{t}</a>'
PAGES = [dict(
    slug=SLUG,
    title="Mutual Fund Taxation in India 2026 With Examples: Equity, Debt and Hybrid Funds, 12.5% LTCG, 20% STCG and Dividends",
    em="the fund type decides the rate, not just how long you hold it.",
    kicker="/ Mutual fund investors &middot; Capital gains &middot; Updated 2026-11-25",
    lead=("<strong>Gains on equity mutual funds held for more than 12 months are taxed at 12.5% on the amount above &#8377;1.25 lakh a year, and at 20% if held for 12 months or less.</strong> "
          "Debt funds that invest more than 65% in debt and money market instruments, bought on or after 1 April 2023, are taxed at your slab rate however long you hold them. "
          "Funds in between, such as many hybrid, international and gold funds, become long-term after 24 months and are taxed at 12.5% without the &#8377;1.25 lakh exemption. Dividends from any fund are taxed at your slab rate."),
    sections=[
        ("/ Rates at a glance", "By fund type.",
         table(["Fund type", "Short-term", "Long-term"], [
             ["Equity-oriented (65%+ equity)", "12 months or less: 20%", "Over 12 months: 12.5% above Rs 1.25 lakh a year"],
             ["Specified (over 65% debt), bought from 1 April 2023", "Slab rate, any holding period", "Not applicable"],
             ["Debt units bought before 1 April 2023", "24 months or less: slab", "Over 24 months: 12.5%, no indexation"],
             ["Other funds (hybrid in between, international, gold)", "24 months or less: slab", "Over 24 months: 12.5%"],
             ["Dividends (IDCW) from any fund", "Slab rate", "Slab rate"]])
         + '<p>Under the Income-tax Act, 2025 the specified-fund definition sits in section 76. NRIs: see ' + L("nri-mutual-funds-india-tax.html", "NRI mutual fund tax") + '.</p>'),
        ("/ Worked examples (illustrative)", "Before cess and surcharge.",
         ul("<strong>Equity fund, held 3 years:</strong> invested &#8377;5 lakh, redeemed &#8377;8 lakh. Gain &#8377;3 lakh; first &#8377;1.25 lakh exempt; tax 12.5% of &#8377;1.75 lakh = &#8377;21,875.",
            "<strong>Equity fund, held 8 months:</strong> gain &#8377;1 lakh, taxed at 20% = &#8377;20,000.",
            "<strong>Debt fund bought in 2024, held 3 years:</strong> gain &#8377;1 lakh added to income and taxed at your slab rate (for example 30% = &#8377;30,000).",
            "<strong>Hybrid fund with 50% equity, held 30 months:</strong> gain &#8377;1 lakh taxed at 12.5% = &#8377;12,500, with no &#8377;1.25 lakh exemption.",
            "<strong>Dividends:</strong> &#8377;20,000 of IDCW is added to income at your slab rate; TDS applies above the yearly threshold.")),
        ("/ Planning points", "Ways to reduce the tax.",
         ul("<strong>Use the &#8377;1.25 lakh exemption each year:</strong> booking equity gains up to the limit and reinvesting resets the cost.",
            "<strong>Set off losses:</strong> short-term losses can offset short- or long-term gains; long-term losses only long-term gains; carry forward eight years if the return is filed on time.",
            "<strong>Growth over IDCW:</strong> dividends are taxed every year at slab; growth options defer tax until redemption.",
            "<strong>Reinvest in a house:</strong> long-term gains can qualify for section 54F if the net sale proceeds go into a residential house; see " + L("which-section-54-vs-54f-vs-54ec-decision-tree-india.html", "54 vs 54F vs 54EC") + ".",
            "<strong>Report correctly:</strong> capital gains statements from the registrar feed Schedule CG of the return; see " + L("form-26as-vs-ais-vs-tis-india-2026.html", "AIS and Form 26AS") + ".")
         + call_box("Mutual fund tax", ["Capital gains computation",
                                         "Tax-loss harvesting",
                                         "Debt vs equity vs hybrid choice",
                                         "54F reinvestment",
                                         "ITR Schedule CG"],
                    "your fund statements.")
         + sources("Income-tax Act, 1961 sections 50AA, 111A and 112A (as amended by the Finance (No. 2) Act, 2024) and section 76 of the Income-tax Act, 2025; ICICI Prudential and Mirae Asset tax reckoners 2026-27; Income Tax Department section 50AA pages; Freefincal, Finnovate and Taxguru commentary. Checked 25 November 2026.")),
    ],
    faqs=[("How are equity mutual funds taxed in India?", "Held for more than 12 months, gains are taxed at 12.5% on the amount above Rs 1.25 lakh a year; held for 12 months or less, at 20%. Equity-oriented means at least 65% in Indian equity."),
          ("How are debt mutual funds taxed after 2023?", "Units of funds investing more than 65% in debt and money market instruments bought on or after 1 April 2023 are taxed at your slab rate regardless of holding period. Units bought before 1 April 2023 held over 24 months are taxed at 12.5% without indexation."),
          ("How are hybrid funds taxed?", "Funds with 65% or more equity are taxed like equity funds. Funds that are neither equity-oriented nor more than 65% debt become long-term after 24 months and are taxed at 12.5% without the Rs 1.25 lakh exemption; short-term gains are taxed at slab."),
          ("Are mutual fund dividends taxable?", "Yes. Dividends (IDCW) are added to your income and taxed at your slab rate, with TDS deducted by the fund above the yearly threshold."),
        ("How are dividends from shares taxed in India?", "Dividends from Indian companies are added to your income and taxed at your slab rate under both regimes. The company deducts 10% TDS when dividends it pays you exceed Rs 10,000 in a year (raised from Rs 5,000 from 1 April 2025; 20% if PAN is not provided); the threshold applies company by company. You claim the TDS in your return, and Form 15G or 15H can stop TDS if your total income is below the taxable limit. From tax year 2026-27 dividend TDS sits in section 393 of the Income-tax Act, 2025."),
          ("Can I set off mutual fund losses?", "Short-term capital losses can be set off against short- or long-term gains, and long-term losses only against long-term gains; unused losses carry forward for eight years if the return is filed on time."),
          ("Can BQP compute my mutual fund capital gains?", "Yes. CA Durgesh Chavda can compute gains from your statements, plan harvesting and reinvestment, and file your return. " + C)],
    related=[("nri-mutual-funds-india-tax.html", "NRI mutual fund tax"),
             ("which-section-54-vs-54f-vs-54ec-decision-tree-india.html", "54 vs 54F vs 54EC"),
             ("form-26as-vs-ais-vs-tis-india-2026.html", "AIS and Form 26AS"),
             ("tax-rates-in-india-2026-27-income-tax-slabs-percentage-corporate-gst-capital-gains-nri.html", "Tax rates 2026-27"),
             ("new-vs-old-tax-regime-calculator.html", "New vs old regime calculator")],
    cta_h="Redeeming mutual funds?", cta_b=C,
    keywords="mutual fund taxation India, mutual fund tax 2026, equity mutual fund LTCG 12.5%, mutual fund STCG 20%, debt mutual fund tax slab, hybrid fund tax, mutual fund taxation with example, mutual fund dividend tax, section 50AA",
    desc="Mutual fund taxation in India 2026 with examples: equity funds 12.5% LTCG above Rs 1.25 lakh / 20% STCG, debt funds (over 65% debt, bought from April 2023) at slab, hybrids 12.5% after 24 months, dividends at slab, loss set-off.",
    howto={"name": "How to work out tax on a mutual fund redemption", "description": "For resident investors.", "steps": [
        {"name": "Identify the fund type", "text": "Equity-oriented, specified debt, or other."},
        {"name": "Check the holding period", "text": "12 months for equity; 24 months for others."},
        {"name": "Compute the gain", "text": "Redemption value minus cost (grandfathered value for pre-2018 equity)."},
        {"name": "Apply the rate", "text": "20% / 12.5% for equity, slab for specified debt, 12.5% or slab for others."},
        {"name": "Use exemptions and losses", "text": "Rs 1.25 lakh equity exemption, set-off and carry forward."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch IM complete")
