# -*- coding: utf-8 -*-
"""Batch IQ (25 Nov 2026): tax on lottery winnings in India 2026 - winnings from lotteries, crossword puzzles, card games,
game shows, races and other games of any sort taxed at a flat 30% (section 115BB of the 1961 Act) plus surcharge where
applicable and 4% cess (31.2% before surcharge); no deduction of expenses, no use of the basic exemption limit or the
87A rebate against it; TDS at 30% under section 194B where a single winning exceeds Rs 10,000 (horse races 194BB);
prizes in kind taxed on market value with tax paid before release; online game winnings taxed separately (115BBJ /
194BA, net winnings); report under income from other sources at the special rate; renumbered provisions in the
Income-tax Act, 2025 from tax year 2026-27 (section numbers per commentary, not quoted).
Demand: sweep ac112 (25 Nov 2026), 5-7 markets: "tax on lottery winnings", "tax on lottery", "tax on lottery winnings
in india", "tax on lottery in india".
Facts (checked 25 Nov 2026): Income Tax Department pages on sections 115BB, 194B and 194BA; Aditya Birla Capital;
Bajaj Finserv (20 July 2026); Taxtmi notes."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 25 November 2026."
SLUG = "tax-on-lottery-winnings-india-2026-30-percent-section-115bb-tds-194b-10000-game-show-prize"

C = contact("what you won (lottery, game show, contest, prize in kind), the amount and date, the TDS deducted, your other income, and whether you are resident or NRI")
L = lambda h, t: f'<a href="{h}">{t}</a>'
PAGES = [dict(
    slug=SLUG,
    title="Tax on Lottery Winnings in India 2026: Flat 30% (31.2% With Cess), TDS Above Rs 10,000, Game Show Prizes and Prizes in Kind",
    em="a flat 30%, whatever your slab.",
    kicker="/ Winners of lotteries, contests and game shows &middot; Income tax &middot; Updated 2026-11-25",
    lead=("<strong>Lottery, game show, crossword, card game and similar winnings in India are taxed at a flat 30%, plus 4% cess (31.2%) and surcharge where your income is high, regardless of your tax slab or regime.</strong> "
          "The payer deducts 30% TDS when a single winning exceeds &#8377;10,000. No expenses can be deducted, and the basic exemption limit and the section 87A rebate cannot be used to reduce this tax."),
    sections=[
        ("/ Key rules", "What applies to winnings.",
         table(["Point", "Rule"], [
             ["Tax rate", "30% flat (section 115BB of the 1961 Act), plus surcharge if applicable and 4% cess"],
             ["TDS", "30% under section 194B when a single winning exceeds &#8377;10,000 (horse races under 194BB)"],
             ["Deductions", "None: no expenses, no Chapter VI-A deductions, no basic exemption limit or 87A rebate against it"],
             ["Prizes in kind (car, flat, gold)", "Taxed on market value; the winner must pay the tax before the prize is released"],
             ["Online game winnings", "Taxed separately on net winnings (section 115BBJ, TDS under 194BA)"],
             ["Regime", "Same 30% in the old and new regimes"],
             ["Return", "Report under income from other sources at the special rate; claim the TDS shown in your " + L("form-26as-vs-ais-vs-tis-india-2026.html", "AIS and Form 26AS")]])
         + '<p>From tax year 2026-27 these provisions continue in the Income-tax Act, 2025 under new section numbers.</p>'),
        ("/ Worked example (illustrative)", "Lottery prize of Rs 10 lakh, no surcharge.",
         table(["Step", "Amount"], [
             ["Prize", "&#8377;10,00,000"],
             ["TDS by the payer at 30%", "&#8377;3,00,000"],
             ["Tax at 30% plus 4% cess", "&#8377;3,12,000"],
             ["Balance payable with the return", "&#8377;12,000"]])
         + '<p>If your total income is above &#8377;50 lakh, surcharge applies on top. See ' + L("tax-rates-in-india-2026-27-income-tax-slabs-percentage-corporate-gst-capital-gains-nri.html", "tax rates 2026-27") + '.</p>'),
        ("/ Practical points", "Before you collect the prize.",
         ul("<strong>Prize in kind:</strong> agree the market value and pay the 30% tax (or give the payer the TDS amount) before taking delivery; keep the payer&rsquo;s certificate.",
            "<strong>Advance tax:</strong> pay any balance (cess, surcharge) in the next advance tax instalment; see " + L("advance-tax-q3-december-15-2026-india.html", "advance tax dates") + ".",
            "<strong>No set-off:</strong> lottery ticket costs or losses cannot be set off against winnings.",
            "<strong>Gifts are different:</strong> money received from relatives is exempt; gifts from others above &#8377;50,000 are taxed at slab rates; see " + L("section-56-2-x-gift-tax-india-2026.html", "gift tax rules") + ".",
            "<strong>Crypto and other income:</strong> virtual digital assets have their own 30% regime; see " + L("crypto-vda-tax-india-2026-complete.html", "crypto tax in India") + ".",
            "<strong>NRIs:</strong> TDS on winnings paid to NRIs is also deducted at 30% plus applicable surcharge and cess; check your residence country&rsquo;s rules on foreign tax credit.")
         + call_box("Winnings", ["Tax on lottery and game show prizes",
                                  "Prizes in kind and valuation",
                                  "TDS credit and refunds",
                                  "Advance tax on the balance",
                                  "ITR filing"],
                    "the prize details and TDS certificate.")
         + sources("Income-tax Act, 1961 sections 115BB, 115BBJ, 194B, 194BA and 194BB, carried into the Income-tax Act, 2025 from tax year 2026-27; Income Tax Department section pages; Aditya Birla Capital and Bajaj Finserv explainers; Taxtmi notes. Checked 25 November 2026.")),
    ],
    faqs=[("How much tax is charged on lottery winnings in India?", "A flat 30% plus 4% cess, which is 31.2%, plus surcharge if your total income is high. The rate is the same whatever your tax slab or regime."),
          ("Is TDS deducted on lottery winnings?", "Yes. The payer deducts 30% TDS under section 194B when a single winning exceeds Rs 10,000. Any balance, such as cess or surcharge, is paid with advance tax or your return."),
          ("Can I use the basic exemption limit against lottery winnings?", "No. Lottery and game show winnings are taxed at 30% from the first rupee; the basic exemption limit, deductions and the section 87A rebate cannot reduce this tax."),
          ("How is a prize in kind like a car taxed?", "On its market value at 30% plus cess. The winner must pay the tax (or give the payer the TDS amount) before the prize is released."),
          ("Are online game winnings taxed like lottery winnings?", "They are taxed at 30% too, but under a separate provision on net winnings (section 115BBJ, with TDS under 194BA)."),
          ("Can BQP help me with tax on a prize?", "Yes. CA Durgesh Chavda can compute the tax, value a prize in kind, reconcile TDS and file your return. " + C)],
    related=[("tax-rates-in-india-2026-27-income-tax-slabs-percentage-corporate-gst-capital-gains-nri.html", "Tax rates 2026-27"),
             ("section-56-2-x-gift-tax-india-2026.html", "Gift tax rules"),
             ("crypto-vda-tax-india-2026-complete.html", "Crypto tax in India"),
             ("form-26as-vs-ais-vs-tis-india-2026.html", "AIS and Form 26AS"),
             ("advance-tax-q3-december-15-2026-india.html", "Advance tax dates")],
    cta_h="Won a prize?", cta_b=C,
    keywords="tax on lottery winnings in india, lottery tax india, tax on lottery, section 115BB 30 percent, TDS 194B 10000, game show prize tax, prize in kind tax, lottery winnings tax 2026",
    desc="Tax on lottery winnings in India 2026: flat 30% (31.2% with cess) under section 115BB whatever your slab, 30% TDS under 194B above Rs 10,000, no deductions or basic exemption, prizes in kind, online games, worked example.",
    howto={"name": "How to handle tax on lottery winnings", "description": "For resident winners.", "steps": [
        {"name": "Check the TDS", "text": "30% deducted on winnings above Rs 10,000."},
        {"name": "Value prizes in kind", "text": "Pay the tax on market value before release."},
        {"name": "Compute the full tax", "text": "30% plus cess and any surcharge."},
        {"name": "Pay the balance", "text": "Through advance tax or self-assessment tax."},
        {"name": "Report in the return", "text": "Income from other sources at the special rate, claim TDS."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch IQ complete")
