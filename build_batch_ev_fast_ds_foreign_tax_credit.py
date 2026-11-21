# -*- coding: utf-8 -*-
"""Batch EV (21 Nov 2026): FAST-DS 2026 and foreign tax already paid - no foreign tax credit under Category 1; when an
updated return can cost less, and what it does not give. Call-first page for RSU / US-stock holders and returning NRIs.
Facts (checked 21 Nov 2026):
- TaxGuru, 'FAST-DS 2026: Foreign Tax Credit Gap, Double Taxation and Updated Returns' (CA Usha Gayathri K and CA
  Aishwariya K Rajagopal, 20 November 2026): the scheme is Chapter IV of the Finance Act, 2026 (sections 130-144); rules
  notified 14 August 2026 with effect from 16 August 2026; neither the Act, the Rules nor the CBDT FAQ provide credit for
  foreign tax on income declared under the first category (60%); an updated return under section 139(8A) taxes the
  income at normal rates with interest and additional tax of 25% to 70%, foreign tax credit remains available with
  Form 67, but it gives no Black Money Act immunity; under the India-US treaty the US may tax dividends up to 25% for an
  individual; uncertainty on combining an updated return with the second category; CBDT clarification awaited.
- Site pages: Category 1 / Category 2 rules, 31 December 2026, Form 67 (Form 44 for tax years from 2026-27), updated
  return window 48 months, barred after certain notices, cannot reduce tax or claim a refund.
Worked example is our own arithmetic: dividend INR 2,00,000, US tax 25% = INR 50,000; Indian tax at 30% slab plus 4% cess
= INR 62,400; credit INR 50,000; balance INR 12,400. FAST-DS Category 1 = 60% of INR 2,00,000 = INR 1,20,000."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 21 November 2026."
SLUG = "fast-ds-2026-no-foreign-tax-credit-category-1-us-dividends-rsu-updated-return-comparison"

C = contact("the foreign income involved (dividends, interest, sale gains), the years, tax already paid abroad, and whether the shares or accounts were reported in your Indian returns")
PAGES = [dict(
    slug=SLUG,
    title="FAST-DS 2026 Gives No Credit for Tax Paid Abroad: US Dividends, RSUs and When an Updated Return Costs Less",
    em="check this before you pay 60% on income already taxed overseas.",
    kicker="/ FAST-DS 2026 &middot; Foreign tax credit &middot; RSUs and US stocks &middot; Updated 2026-11-21",
    lead=("Foreign income declared under <strong>Category 1 of FAST-DS 2026</strong> is charged at a flat <strong>60%</strong>, and the scheme gives <strong>no credit for tax already paid abroad</strong> on that income. Neither the Finance Act, the rules nor the official FAQ provide for it. "
          "This matters most for <strong>dividends on US shares and RSUs</strong>, where the US has usually withheld up to 25% already. "
          "An <strong>updated return</strong> taxes the same income at normal rates with interest and an additional 25% to 70%, and it <strong>does allow the foreign tax credit</strong> through Form 67. For small amounts of already-taxed income it can cost far less. "
          "The trade-off is that an updated return gives <strong>no Black Money Act immunity</strong>, is not available for every year or after certain notices, and does not by itself fix a foreign asset that was never reported. "
          "The shares themselves usually fall under <strong>Category 2</strong> (flat INR 1 lakh). The last date for a FAST-DS declaration is <strong>31 December 2026</strong>."),
    sections=[
        ("/ Worked example", "A US dividend of INR 2,00,000 with 25% US tax withheld.",
         table(["Route", "Indian amount payable", "US tax already paid", "Black Money Act immunity"], [
             ["Reported on time, with foreign tax credit", "About INR 12,400 (30% slab plus cess = INR 62,400, less credit of INR 50,000)", "INR 50,000", "Not needed"],
             ["Updated return, with foreign tax credit", "About INR 12,400 plus interest and an additional 25% to 70% of the tax and interest", "INR 50,000", "No"],
             ["FAST-DS Category 1", "INR 1,20,000 (60% of INR 2,00,000); no credit", "INR 50,000", "Yes, for what is declared"]])
         + "<p>Figures assume the 30% slab, 4% cess and no surcharge. Your own numbers depend on the slab, the years involved and the treaty.</p>"
         + call_box("FAST-DS or updated return for my foreign income", ["Which income is Category 1 and which assets are Category 2",
                                                                       "Foreign tax already paid and whether credit can still be claimed",
                                                                       "Years still open for an updated return, and notices that block it",
                                                                       "The Black Money Act exposure each route leaves",
                                                                       "Filing before 31 December 2026 and correcting future returns"],
                    "broker or RSU statements, Form 1042-S or other foreign tax records, your Indian returns for the years involved and any email from the Department.")),
        ("/ How to decide", "Cost against protection.",
         ul("<strong>Split the problem:</strong> shares taxed through payroll but missing from the foreign-assets schedule are usually Category 2 (INR 1 lakh in total). Unreported dividends, interest and sale gains are income, and that is where the 60% applies.",
            "<strong>Where FAST-DS still wins:</strong> income never taxed anywhere, older years that an updated return cannot reach, cases where a notice has blocked the updated return, and anyone who wants the certainty of immunity.",
            "<strong>Where an updated return may be cheaper:</strong> small amounts of dividend or interest already taxed abroad, in years still open, where you can show the foreign tax paid.",
            "<strong>What an updated return does not do:</strong> it gives no Black Money Act immunity, cannot be used only to add an asset, and cannot reduce tax or claim a refund; see <a href=\"itr-u-updated-return-48-months-section-139-8a-india.html\">updated returns</a>.",
            "<strong>Open question:</strong> practitioners have flagged uncertainty about using an updated return for the income together with Category 2 for the asset. There is no clarification from the CBDT yet, so take advice on your facts before choosing.",
            "<strong>Payment is final:</strong> amounts paid under FAST-DS are not refundable, so settle the route before filing Form 1.")
         + '<p>Related: <a href="fast-ds-2026-faq-full-form-last-date-eligibility-cost-form-1-nri-founders.html">FAST-DS 2026 FAQ</a> &middot; <a href="fast-ds-rsu-espp-us-shares-401k-which-category.html">RSUs, ESPP and 401(k)</a> &middot; <a href="fast-ds-vs-revised-return-vs-updated-return-itr-u.html">FAST-DS vs revised or updated return</a> &middot; <a href="form-67-foreign-tax-credit-india-2026.html">Form 67 foreign tax credit</a> &middot; <a href="rsu-taxation-india-us-stocks-vesting-perquisite-capital-gains-schedule-fa-2026.html">RSU taxation in India</a>.</p>'
         + sources("Finance Act, 2026, Chapter IV (Foreign Assets of Small Taxpayers Disclosure Scheme, 2026) and the FAST-DS Rules, 2026 (notified 14 August 2026); section 139(8A) on updated returns; section 90, Rule 128 and Form 67 on foreign tax credit; India-US tax treaty, Articles 10 and 25; analysis by CA Usha Gayathri K and CA Aishwariya K Rajagopal, TaxGuru, 20 November 2026. The CBDT has not clarified the foreign tax credit point; check for updates before filing.")),
    ],
    faqs=[("Does FAST-DS 2026 allow foreign tax credit?", "No. Income declared under Category 1 is charged at a flat 60%, and neither the Finance Act, the rules nor the official FAQ provide credit for tax already paid abroad on that income."),
          ("I paid 25% US tax on my dividends. Do I still pay 60% under FAST-DS?", "Yes, if you declare those dividends under Category 1. The US tax is not credited, so the combined cost can exceed the income's normal Indian tax many times over."),
          ("Can I use an updated return instead for foreign dividends?", "For years still open, yes: the income is taxed at normal rates with interest and an additional 25% to 70%, and foreign tax credit can be claimed with Form 67. It gives no Black Money Act immunity and is barred after certain notices."),
          ("Which FAST-DS category applies to RSU shares?", "Shares taxed as a perquisite through Indian payroll but not reported in the foreign-assets schedule are usually Category 2, with a flat fee of INR 1 lakh. Unreported dividends and sale gains are Category 1."),
          ("Can I combine an updated return with FAST-DS Category 2?", "Practitioners have raised this as an open question and the CBDT has not clarified it. Take advice on your facts before choosing a route."),
          ("Can BQP compare the routes for me?", "Yes. " + C)],
    related=[("fast-ds-2026-faq-full-form-last-date-eligibility-cost-form-1-nri-founders.html", "FAST-DS 2026 FAQ"),
             ("fast-ds-rsu-espp-us-shares-401k-which-category.html", "FAST-DS for RSUs, ESPP and 401(k)"),
             ("fast-ds-vs-revised-return-vs-updated-return-itr-u.html", "FAST-DS vs revised or updated return")],
    cta_h="Foreign dividends or RSU income missed in your Indian return?", cta_b=C,
    keywords="FAST-DS foreign tax credit, FAST-DS Category 1 60% US dividends, FAST-DS RSU dividends tax paid abroad, FAST-DS vs updated return foreign tax credit, Form 67 updated return, FAST-DS double taxation",
    desc="FAST-DS 2026 Category 1 charges 60% with no credit for tax paid abroad. Example: a US dividend of INR 2 lakh with 25% US tax costs INR 1.2 lakh under FAST-DS vs about INR 12,400 plus interest and additional tax in an updated return with Form 67 credit, but without immunity.",
    howto={"name": "How to choose between FAST-DS and an updated return for foreign income", "description": "Before 31 December 2026.", "steps": [
        {"name": "Separate assets from income", "text": "Unreported shares are usually Category 2; unreported dividends and gains are income."},
        {"name": "Collect foreign tax proof", "text": "Broker statements and foreign tax certificates for each year."},
        {"name": "Check which years are open", "text": "Updated returns have a time limit and are barred after certain notices."},
        {"name": "Compare cost and protection", "text": "60% with immunity against normal tax, interest and additional tax with credit but no immunity."},
        {"name": "File the chosen route", "text": "FAST-DS Form 1 by 31 December 2026, or the updated return with Form 67."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch EV complete")
