# -*- coding: utf-8 -*-
"""Batch GM (24 Nov 2026): Tax rates in India at a glance for tax year 2026-27 - income tax slabs (new and old regime),
surcharge and cess, NRI points, capital gains, company tax (domestic and foreign), GST rates, common TDS on NRIs.
Call-first hub page for "tax in india percentage" searchers in India and abroad.
Demand: sweep ac62 (24 Nov 2026): "tax in india percentage" in all 7 markets; "india gst rate" in 6.
Facts (checked 24 Nov 2026): Budget 2026 left individual slabs unchanged for tax year 2026-27 (Business Today 1 Feb 2026,
Asianet, Bajaj Finserv): new regime nil to INR 4 lakh, 5% 4-8, 10% 8-12, 15% 12-16, 20% 16-20, 25% 20-24, 30% above 24;
rebate up to INR 60,000 for residents with income up to INR 12 lakh; standard deduction INR 75,000 (new) / 50,000 (old);
old regime nil to 2.5 lakh, 5% 2.5-5, 20% 5-10, 30% above 10. Surcharge and cess, capital gains, company and GST rates as
already stated on site pages (branch-vs-subsidiary calculator, 115BAA page, GST pages: 5%, 18%, 40% since 22 September 2025)."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 24 November 2026."
SLUG = "tax-rates-in-india-2026-27-income-tax-slabs-percentage-corporate-gst-capital-gains-nri"

C = contact("whether you are resident, NRI or a foreign company, your main income types (salary, business, rent, capital gains, dividends) and the year in question")
L = lambda h, t: f'<a href="{h}">{t}</a>'
PAGES = [dict(
    slug=SLUG,
    title="Tax Rates in India 2026-27: Income Tax Slabs, Company Tax, Capital Gains, GST and NRI Rates",
    em="every main percentage on one page.",
    kicker="/ Tax rates &middot; India &middot; Updated 2026-11-24",
    lead=("<strong>For tax year 2026-27, individuals in India pay income tax at 0% to 30%: under the default new regime, nil up to INR 4 lakh, then 5%, 10%, 15%, 20% and 25% in INR 4 lakh steps, and 30% above INR 24 lakh, plus 4% cess.</strong> "
          "Residents with taxable income up to INR 12 lakh pay nothing after the rebate (INR 12.75 lakh for salaried people after the INR 75,000 standard deduction). "
          "Domestic companies pay about <strong>25.17%</strong> under the concessional regime, foreign companies' Indian branches <strong>35%</strong> plus surcharge and cess, and GST is mostly <strong>5% or 18%</strong>, with <strong>40%</strong> on luxury and sin goods. "
          "Long-term gains on listed shares are taxed at <strong>12.5%</strong> above INR 1.25 lakh a year and short-term at <strong>20%</strong>. Budget 2026 did not change the individual slabs."),
    sections=[
        ("/ Individuals", "Income tax slabs for tax year 2026-27 (FY 2026-27).",
         table(["Taxable income (INR)", "New regime (default)", "Old regime (opt in)"], [
             ["Up to 2.5 lakh", "Nil", "Nil"],
             ["2.5 to 4 lakh", "Nil", "5%"],
             ["4 to 5 lakh", "5%", "5%"],
             ["5 to 8 lakh", "5%", "20%"],
             ["8 to 10 lakh", "10%", "20%"],
             ["10 to 12 lakh", "10%", "30%"],
             ["12 to 16 lakh", "15%", "30%"],
             ["16 to 20 lakh", "20%", "30%"],
             ["20 to 24 lakh", "25%", "30%"],
             ["Above 24 lakh", "30%", "30%"]])
         + ul("<strong>Rebate:</strong> residents with taxable income up to INR 12 lakh (new regime) or INR 5 lakh (old regime) pay no tax; NRIs do not get the rebate.",
              "<strong>Standard deduction</strong> for salary and pension: INR 75,000 (new) or INR 50,000 (old).",
              "<strong>Cess:</strong> 4% on tax plus surcharge.",
              "<strong>Surcharge</strong> on high incomes: 10% above INR 50 lakh, 15% above INR 1 crore, 25% above INR 2 crore (the old regime adds 37% above INR 5 crore); capped at 15% on dividends and capital gains on shares.",
              "<strong>Old regime</strong> keeps deductions such as investments, health insurance and home loan interest. Compare with the " + L("new-vs-old-tax-regime-calculator.html", "new vs old regime calculator") + ".")),
        ("/ Capital gains, companies and GST", "The other rates people ask about.",
         table(["Item", "Rate"], [
             ["Listed shares and equity funds, long term (over 12 months)", "12.5% above INR 1.25 lakh a year"],
             ["Listed shares and equity funds, short term", "20%"],
             ["Property and other assets, long term (property over 24 months)", "12.5% without indexation (resident individuals can choose 20% with indexation for land or buildings bought before 23 July 2024)"],
             ["Debt funds bought from 1 April 2023", "Slab rate"],
             ["Domestic company, concessional regime", "22% plus 10% surcharge and 4% cess = about 25.17%"],
             ["Domestic company, regular regime", "25% (turnover up to INR 400 crore) or 30%, plus surcharge and cess"],
             ["Foreign company (branch or project office)", "35% plus surcharge (2% above INR 1 crore, 5% above INR 10 crore) and 4% cess"],
             ["GST", "0%, 5% or 18% for most goods and services, 40% on luxury and sin goods (since 22 September 2025)"]])
         + '<p>More detail: ' + L("section-115baa-115bab-corporate-tax-regime-india.html", "company tax regimes") + ' and ' + L("branch-vs-subsidiary-india-tax-calculator-foreign-company-35-percent-vs-25-percent-dividend-treaty-2026.html", "branch vs subsidiary for foreign companies") + '.</p>'),
        ("/ NRIs and foreign investors", "Rates that apply when you live abroad.",
         ul("<strong>Same slabs</strong> as residents for Indian income, but no rebate, so tax starts above INR 4 lakh (new regime) or INR 2.5 lakh (old).",
            "<strong>Tax deducted on NRO interest and rent</strong> paid to an NRI: 30% plus cess (about 31.2%), which a return can bring down to your actual tax.",
            "<strong>Dividends</strong> to non-residents: 20% under Indian law, often lower under a tax treaty with a residency certificate.",
            "<strong>NRE and FCNR interest</strong> is tax-free for NRIs.",
            "<strong>Property sale by an NRI:</strong> the buyer deducts tax on the gain at 12.5% (long term) plus surcharge and cess; see " + L("nri-selling-indian-property-capital-gains.html", "NRI property sale") + ".")
         + call_box("Indian tax rates for your situation", ["Which regime suits your income",
                                                             "NRI rates, refunds and treaty relief",
                                                             "Capital gains on shares or property",
                                                             "Company tax for a new Indian entity",
                                                             "GST rate on your product or service"],
                    "whether you are resident, NRI or a company, and your main income types.")
         + sources("Union Budget 2026 coverage of unchanged individual slabs for tax year 2026-27 (Business Today, 1 February 2026; Asianet Newsable; Bajaj Finserv); Income-tax Act, 2025 (in force 1 April 2026) and Finance Act 2026; GST rate rationalisation from 22 September 2025 (56th GST Council). Rates are general and may differ for special income; checked 24 November 2026.")),
    ],
    faqs=[("What is the income tax percentage in India?", "0% to 30% for individuals, plus 4% cess. Under the default new regime for tax year 2026-27: nil up to INR 4 lakh, 5% up to 8 lakh, 10% up to 12 lakh, 15% up to 16 lakh, 20% up to 20 lakh, 25% up to 24 lakh and 30% above. Residents with taxable income up to INR 12 lakh pay nothing after the rebate."),
          ("Did Budget 2026 change the income tax slabs?", "No. Budget 2026 kept the individual slabs for tax year 2026-27 the same as the year before under both regimes."),
          ("What is the corporate tax rate in India?", "About 25.17% for domestic companies under the concessional regime (22% plus surcharge and cess), 25% or 30% under the regular regime, and 35% plus surcharge and cess for a foreign company's branch."),
          ("What are the GST rates in India?", "Since 22 September 2025, most goods and services are taxed at 5% or 18%, with 40% on luxury and sin goods and some items exempt or at 0%."),
          ("Do NRIs pay the same tax rates as residents?", "The slabs are the same, but NRIs do not get the rebate up to INR 12 lakh, banks and tenants deduct about 31.2% on NRO interest and rent, and NRE and FCNR interest is tax-free."),
          ("Can BQP work out my Indian tax?", "Yes. " + C)],
    related=[("new-vs-old-tax-regime-calculator.html", "New vs old regime calculator"),
             ("which-regime-new-vs-old-tax-regime-decision-india-2026-27.html", "Which regime to choose"),
             ("section-115baa-115bab-corporate-tax-regime-india.html", "Company tax regimes"),
             ("branch-vs-subsidiary-india-tax-calculator-foreign-company-35-percent-vs-25-percent-dividend-treaty-2026.html", "Branch vs subsidiary tax"),
             ("nre-nro-fcnr-account-tax-rules.html", "NRE, NRO and FCNR tax rules")],
    cta_h="Need your actual tax worked out?", cta_b=C,
    keywords="tax in India percentage, income tax slab 2026-27, income tax rates India 2026, new regime slabs, old regime slabs, corporate tax rate India, GST rates India 2026, capital gains tax India rate, NRI tax rates India",
    desc="Tax rates in India for 2026-27: income tax slabs 0% to 30% (new regime nil to INR 4 lakh, rebate to INR 12 lakh for residents; old regime), surcharge and cess, capital gains 12.5% / 20%, company tax about 25.17% or 35% for foreign branches, GST 5% / 18% / 40%, and NRI rates.",
    howto={"name": "How to work out your Indian tax rate", "description": "Quick steps for tax year 2026-27.", "steps": [
        {"name": "Check your residential status", "text": "Resident or NRI changes the rebate and deductions."},
        {"name": "Pick the regime", "text": "New regime by default; old regime if your deductions are large."},
        {"name": "Apply the slabs", "text": "Add 4% cess and any surcharge."},
        {"name": "Tax special income separately", "text": "Capital gains and some other income have their own rates."},
        {"name": "Credit tax already deducted", "text": "Claim TDS and file a return for any refund."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch GM complete")
