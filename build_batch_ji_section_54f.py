# -*- coding: utf-8 -*-
"""Batch JI (25 Nov 2026): Section 54F of the Income-tax Act (now section 86 of the Income-tax Act, 2025 from tax year
2026-27 per Taxguru / Taxscan) - exemption on long-term capital gains from any asset other than a residential house
(shares, mutual funds, land, plot, gold, commercial property, unlisted shares, ESOP shares) when the net sale
consideration is invested in one residential house in India: buy 1 year before or 2 years after, or construct within
3 years; proportionate exemption = gain x amount invested / net consideration; cost of the new house counted up to
Rs 10 crore (Finance Act 2023); must not own more than one other residential house on the date of sale; buying another
house within 2 years or building one within 3 years, or selling the new house within 3 years, reverses the exemption;
unused amount must go into the Capital Gains Accounts Scheme before the return due date; individuals and HUFs,
residents and NRIs (house in India); available in the new regime.
Demand: sweep ac118 (25 Nov 2026), 6 markets: "section 54f of income tax act"; 7 markets "section 54"; "capital gains".
Facts (checked 25 Nov 2026): Taxguru (section 54F -> section 86), Taxscan (54F vs 86 series), Income Tax Department
section 54F pages and capital gains exemptions tutorial; site section 54, 54EC and decision-tree pages."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 25 November 2026."
SLUG = "section-54f-of-income-tax-act-now-section-86-capital-gains-exemption-shares-land-house-conditions-10-crore-2026"

C = contact("what you sold and when, the sale price and cost, how many houses you own, and the house you plan to buy or build")
L = lambda h, t: f'<a href="{h}">{t}</a>'
PAGES = [dict(
    slug=SLUG,
    title="Section 54F of Income Tax Act (Now Section 86): Capital Gains Exemption on Shares, Land and Other Assets Reinvested in a House - Conditions, Formula, Rs 10 Crore Cap (2026)",
    em="invest the whole sale price, not just the gain.",
    kicker="/ Investors, founders, ESOP holders and NRIs &middot; Capital gains &middot; Updated 2026-11-25",
    lead=("<strong>Section 54F exempts long-term capital gains from selling any asset other than a residential house, such as shares, mutual funds, land, gold or commercial property, if you invest the net sale consideration in one residential house in India.</strong> "
          "From tax year 2026-27 the same relief sits in section 86 of the Income-tax Act, 2025. "
          "Invest the full sale price and the whole gain is exempt; invest part of it and the exemption is proportionate. The cost of the new house counts only up to &#8377;10 crore."),
    sections=[
        ("/ Section 54F at a glance", "Who can claim it and on what.",
         table(["Point", "Rule"], [
             ["Who can claim", "Individuals and HUFs, residents and NRIs"],
             ["Asset sold", "Any long-term capital asset other than a residential house: listed or unlisted shares, mutual funds, land or plot, gold, commercial property"],
             ["What to invest", "The net sale consideration (sale price minus transfer costs), not just the gain"],
             ["New asset", "One residential house in India"],
             ["Time limit", "Buy 1 year before or 2 years after the sale, or construct within 3 years"],
             ["Exemption", "Gain x amount invested / net sale consideration"],
             ["Cap", "Cost of the new house counted only up to &#8377;10 crore"],
             ["Not yet invested by the return due date", "Deposit in the Capital Gains Accounts Scheme"],
             ["Tax regime", "Available in both the new and old regimes"],
             ["2025 Act", "Section 86 from tax year 2026-27"]])
         + '<p>Selling a house instead? Use ' + L("section-54-exemption-house-property-capital-gains-conditions-10-crore-limit-cgas-section-82-2026.html", "section 54 (now section 82)") + '. Prefer bonds? See ' + L("54ec-bonds-section-85-capital-gains-bonds-lock-in-interest-rate-limit-nri-2026.html", "54EC bonds (now section 85)") + ', and compare all three in the ' + L("which-section-54-vs-54f-vs-54ec-decision-tree-india.html", "54 vs 54F vs 54EC decision tree") + '.</p>'),
        ("/ Conditions that can cost you the exemption", "Check these before you sell.",
         ul("<strong>House ownership:</strong> on the date of sale you must not own more than one residential house other than the new one.",
            "<strong>No second new house:</strong> buying another residential house within two years, or building one within three years, after the sale withdraws the exemption.",
            "<strong>Three-year hold:</strong> selling the new house within three years makes the exempted gain taxable in that year.",
            "<strong>India only:</strong> the new house must be in India; a house abroad does not qualify.",
            "<strong>Capital Gains Accounts Scheme:</strong> money not invested by the return due date must be deposited in a CGAS account before filing; any amount not used within the time limit is taxed as long-term gain in the year the period ends.",
            "<strong>Long-term only:</strong> the asset must be long-term: over 12 months for listed shares and equity funds, over 24 months for most other assets; see " + L("ltcg-12-5-percent-new-capital-gains-india-2026.html", "LTCG at 12.5%") + ".")),
        ("/ Worked example and common cases", "How the formula works.",
         ul("<strong>Example:</strong> listed shares sold for a net &#8377;80 lakh with a long-term gain of &#8377;30 lakh; you buy a house for &#8377;60 lakh. Exemption = 30 x 60 / 80 = &#8377;22.5 lakh, so &#8377;7.5 lakh stays taxable at 12.5% (above the &#8377;1.25 lakh exemption for listed equity).",
            "<strong>ESOP and startup shares:</strong> gains on selling ESOP shares (beyond the salary perquisite taxed at exercise) can use section 54F; see " + L("esop-taxation-india-2026-perquisite-at-exercise-capital-gains-startup-deferral-foreign-esop-rsu.html", "ESOP taxation") + ".",
            "<strong>NRIs:</strong> NRIs can claim section 54F on Indian assets and can apply for a lower TDS certificate to reflect it; see " + L("nri-capital-gains-tax-on-indian-shares-ltcg-12-5-stcg-20-tds-refund-2026.html", "NRI capital gains on shares") + ".",
            "<strong>Land or plot:</strong> a plot is not a residential house, so gains on selling it use section 54F (or 54EC bonds), not section 54.")
         + call_box("Capital gains planning", ["54F eligibility and house-ownership check",
                                                "Exemption calculation and CGAS deposit",
                                                "54 vs 54F vs 54EC choice",
                                                "NRI lower TDS certificate",
                                                "ITR with capital gains schedules"],
                    "the sale details and your planned house.")
         + sources("Income-tax Act, 1961, section 54F; Income-tax Act, 2025, section 86 (Taxguru and Taxscan commentary); Finance Act, 2023 (Rs 10 crore cap); Capital Gains Accounts Scheme, 1988; Income Tax Department section pages and capital gains exemptions tutorial; site section 54, 54EC and decision-tree guides. Checked 25 November 2026.")),
    ],
    faqs=[("What is section 54F of the Income Tax Act?", "It exempts long-term capital gains from selling any asset other than a residential house, such as shares, mutual funds, land or gold, when the net sale consideration is invested in one residential house in India. From tax year 2026-27 it is section 86 of the Income-tax Act, 2025."),
          ("What is the difference between section 54 and section 54F?", "Section 54 applies when you sell a residential house and reinvest the gain in another house; section 54F applies when you sell any other long-term asset and requires investing the net sale consideration, not just the gain."),
          ("How is the section 54F exemption calculated?", "Exemption = capital gain x amount invested in the new house / net sale consideration. Investing the full net consideration exempts the whole gain; the new house cost is counted only up to Rs 10 crore."),
          ("Can I claim section 54F if I already own a house?", "Yes, if you own no more than one residential house other than the new one on the date of sale. Owning two or more other houses on that date rules out the exemption."),
          ("Can I claim section 54F on sale of shares or mutual funds?", "Yes. Long-term gains on listed or unlisted shares and mutual fund units qualify if the net sale consideration is invested in a residential house in India within the time limits."),
          ("Is section 54F available in the new tax regime?", "Yes. Capital gains exemptions such as sections 54, 54F and 54EC remain available in the new regime."),
          ("Can BQP help with section 54F planning?", "Yes. CA Durgesh Chavda checks eligibility, computes the exemption, handles the Capital Gains Accounts Scheme deposit and files the return. " + C)],
    related=[("section-54-exemption-house-property-capital-gains-conditions-10-crore-limit-cgas-section-82-2026.html", "Section 54 (now section 82)"),
             ("54ec-bonds-section-85-capital-gains-bonds-lock-in-interest-rate-limit-nri-2026.html", "54EC bonds"),
             ("which-section-54-vs-54f-vs-54ec-decision-tree-india.html", "54 vs 54F vs 54EC"),
             ("ltcg-12-5-percent-new-capital-gains-india-2026.html", "LTCG at 12.5%"),
             ("esop-taxation-india-2026-perquisite-at-exercise-capital-gains-startup-deferral-foreign-esop-rsu.html", "ESOP taxation")],
    cta_h="Selling shares or land and buying a house?", cta_b=C,
    keywords="section 54f of income tax act, section 54f, section 86 income tax act 2025, 54f exemption, 54f calculation, 54f conditions, 54f on sale of shares, 54f vs 54, capital gains exemption house",
    desc="Section 54F of Income Tax Act (now section 86 of the 2025 Act): LTCG on shares, mutual funds, land or gold exempt when the net sale price is invested in one house in India; formula, time limits, Rs 10 crore cap, ownership conditions, CGAS.",
    howto={"name": "How to claim the section 54F exemption", "description": "Step by step.", "steps": [
        {"name": "Check the asset", "text": "Long-term asset other than a residential house."},
        {"name": "Check house ownership", "text": "No more than one other house on the date of sale."},
        {"name": "Invest the net sale consideration", "text": "Buy within 1 year before / 2 years after, or build within 3 years."},
        {"name": "Use CGAS if needed", "text": "Deposit unused money before the return due date."},
        {"name": "Hold and report", "text": "Keep the house 3 years; claim the exemption in the ITR."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch JI complete")
