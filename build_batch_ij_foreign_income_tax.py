# -*- coding: utf-8 -*-
"""Batch IJ (25 Nov 2026): foreign income tax in India 2026 - scope of total income by residential status: resident and
ordinarily resident (ROR) taxed on worldwide income; resident but not ordinarily resident (RNOR) on income received /
accruing in India plus foreign income from a business controlled in or profession set up in India; non-resident (NR) on
income received / accruing / deemed to accrue in India only. Residence tests in section 6 of both Acts. Foreign income
of residents reported in Schedule FSI, foreign tax credit claimed in Schedule TR with Form 67 (Form 44 under the 2026
Rules) by the end of the assessment year (rule 128(9)); foreign assets in Schedule FA (ROR); Black Money Act penalty of
Rs 10 lakh for non-disclosure; FAST-DS 2026 window per site pages. GST: export of services by a registered supplier is
zero-rated (LUT) - not a tax on the income.
Demand: sweep ac110 (25 Nov 2026), all 7 markets: "foreign income india", "foreign income taxable in india", "foreign
income for indian resident", "foreign income received in india is taxable", "foreign income declaration india",
"foreign income tax india percentage", "foreign income tax india calculator", "foreign income taxation in india",
"gst on foreign income india".
Facts (checked 25 Nov 2026): site pages on residential status / RNOR, Form 67 (rule 128(9), Notification 100/2022),
FAST-DS and Black Money Act exposure, GST on export of services; section 5 / section 6 scope rules (1961 Act and 2025
Act counterparts)."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 25 November 2026."
SLUG = "foreign-income-tax-india-2026-taxable-for-residents-rnor-nri-schedule-fsi-fa-foreign-tax-credit"

C = contact("your residential status for the year (days in India), the foreign income and the country, foreign tax paid, and any foreign accounts or assets")
L = lambda h, t: f'<a href="{h}">{t}</a>'
PAGES = [dict(
    slug=SLUG,
    title="Foreign Income Tax in India 2026: Is Foreign Income Taxable for Residents, RNOR and NRIs, Schedule FSI / FA and Foreign Tax Credit",
    em="residential status decides whether India taxes it at all.",
    kicker="/ Residents with income from abroad &middot; Income tax &middot; Updated 2026-11-25",
    lead=("<strong>Whether India taxes your foreign income depends on your residential status for the year: a resident and ordinarily resident (ROR) is taxed on worldwide income, a resident but not ordinarily resident (RNOR) mainly on income received or earned in India, and a non-resident only on Indian income.</strong> "
          "An ROR adds foreign salary, interest, dividends, rent and capital gains to Indian income and pays tax at normal rates, then claims credit for foreign tax paid under the tax treaty or domestic relief by filing Form 67 (Form 44 under the 2026 Rules). "
          "Foreign income goes in Schedule FSI of the return and foreign assets in Schedule FA; leaving foreign assets out can attract a &#8377;10 lakh penalty under the Black Money Act."),
    sections=[
        ("/ Quick answers", "What people search for.",
         ul("<strong>Is foreign income taxable in India?</strong> For an ROR, yes, all of it. For an RNOR, only if received in India or from a business controlled or profession set up in India. For a non-resident, no, unless it is received or arises in India.",
            "<strong>Is foreign income received in India taxable?</strong> Bringing money into India is not itself taxed; what matters is whether the income was taxable when earned. For non-residents and RNORs, income first received in India can become taxable, so the place of first receipt matters.",
            "<strong>What is the tax rate on foreign income?</strong> There is no separate percentage: it is added to total income at slab rates (or special rates for capital gains), and foreign tax paid on the same income is credited up to the Indian tax on it.",
            "<strong>How do I declare foreign income?</strong> In Schedule FSI (income by country), Schedule TR (tax relief claimed) and, for RORs, Schedule FA (foreign assets held at any time in the calendar year).",
            "<strong>How do I avoid double tax?</strong> Claim foreign tax credit by filing Form 67 / Form 44 with proof of foreign tax, by the end of the assessment year if the return is filed on time or as a belated return; see " + L("form-67-foreign-tax-credit-india-2026.html", "Form 67 foreign tax credit") + ".",
            "<strong>Is GST payable on foreign income?</strong> GST is a tax on supplies, not income: exporting services from India is zero-rated, usually under an LUT; see " + L("gst-on-export-of-services-lut-without-lut-invoice-format-refund-freelancer-startup-2026.html", "GST on export of services") + ".")),
        ("/ Scope by residential status", "What India taxes.",
         table(["Status", "Indian income", "Foreign income"], [
             ["Resident and ordinarily resident (ROR)", "Taxable", "Taxable (worldwide)"],
             ["Resident but not ordinarily resident (RNOR)", "Taxable", "Only if from a business controlled or profession set up in India, or received in India"],
             ["Non-resident (NR)", "Taxable", "Not taxable unless received or arising in India"]])
         + '<p>Residence is decided by days in India under section 6 of both Acts; see ' + L("nri-residential-status-rnor-india.html", "residential status and RNOR") + ' and ' + L("best-ca-nri-returning-india-rnor-planning.html", "RNOR planning for returning NRIs") + '.</p>'),
        ("/ Getting reporting right", "Where people slip.",
         ul("<strong>Schedule FA covers assets, not just income:</strong> foreign bank accounts, shares, RSUs, insurance policies and property must be listed even with no income; see " + L("rsu-taxation-india-us-stocks-vesting-perquisite-capital-gains-schedule-fa-2026.html", "RSU taxation and Schedule FA") + ".",
            "<strong>Missed disclosures:</strong> see " + L("fast-ds-what-happens-if-i-do-not-declare-black-money-act.html", "what happens if foreign assets are not declared") + " and the " + L("fast-ds-2026-calculator-foreign-asset-disclosure-cost.html", "FAST-DS 2026 cost calculator") + ".",
            "<strong>Freelancers and consultants:</strong> foreign client receipts are business income; see " + L("freelancer-consultant-tax-india-2026-complete.html", "freelancer and consultant tax") + ".",
            "<strong>Exchange rates:</strong> convert foreign tax for the credit at the SBI telegraphic transfer buying rate on the last day of the month before it was paid or deducted.",
            "<strong>NRIs:</strong> see the " + L("nri-taxation-india-complete-guide.html", "NRI taxation guide") + ".")
         + call_box("Foreign income", ["Residential status check",
                                        "Schedule FSI, TR and FA reporting",
                                        "Form 67 / Form 44 foreign tax credit",
                                        "Missed disclosure clean-up",
                                        "Treaty relief planning"],
                    "your days in India and income sources.")
         + sources("Income-tax Act, 1961 sections 5, 6 and 90 / 91 and their counterparts in the Income-tax Act, 2025; Income-tax Rules, 1962 rule 128 (Form 67) and Income-tax Rules, 2026 (Form 44); Black Money (Undisclosed Foreign Income and Assets) and Imposition of Tax Act, 2015; site guides on residential status, Form 67, FAST-DS and GST on export of services. Checked 25 November 2026.")),
    ],
    faqs=[("Is foreign income taxable in India for residents?", "Yes for a resident and ordinarily resident, who is taxed on worldwide income at normal rates with credit for foreign tax. A resident but not ordinarily resident is taxed on foreign income only if it comes from a business controlled or profession set up in India or is received in India."),
          ("Is foreign income taxable for NRIs in India?", "No, unless it is received in India or accrues or arises in India. NRIs are taxed in India on Indian income such as rent, interest on NRO deposits and capital gains on Indian assets."),
          ("What is the tax rate on foreign income in India?", "There is no separate rate. Foreign income is added to total income and taxed at slab rates, or at the special rate for capital gains, with credit for foreign tax paid on the same income."),
          ("How do I declare foreign income in my ITR?", "Report it in Schedule FSI country by country, claim relief in Schedule TR backed by Form 67 (Form 44 under the 2026 Rules), and list foreign assets in Schedule FA if you are resident and ordinarily resident."),
          ("What happens if I do not declare foreign assets?", "Non-disclosure of foreign assets in the return can attract a penalty of Rs 10 lakh under the Black Money Act, apart from tax on undisclosed income; the site's FAST-DS guides explain the current disclosure window."),
          ("Can BQP help with foreign income tax?", "Yes. CA Durgesh Chavda can confirm your residential status, report foreign income and assets correctly and claim foreign tax credit. " + C)],
    related=[("nri-residential-status-rnor-india.html", "Residential status and RNOR"),
             ("form-67-foreign-tax-credit-india-2026.html", "Form 67 foreign tax credit"),
             ("fast-ds-what-happens-if-i-do-not-declare-black-money-act.html", "Undeclared foreign assets"),
             ("rsu-taxation-india-us-stocks-vesting-perquisite-capital-gains-schedule-fa-2026.html", "RSU taxation and Schedule FA"),
             ("nri-taxation-india-complete-guide.html", "NRI taxation guide")],
    cta_h="Earning income from abroad?", cta_b=C,
    keywords="foreign income tax India, is foreign income taxable in India, foreign income for Indian resident, foreign income received in India taxable, Schedule FSI, Schedule FA, foreign tax credit Form 67, RNOR foreign income, foreign income declaration India",
    desc="Foreign income tax in India 2026: ROR taxed on worldwide income, RNOR and NRIs only on Indian / India-received income, slab rates, Schedule FSI / TR / FA reporting, foreign tax credit with Form 67 / 44, Black Money Act penalty, GST on exports.",
    howto={"name": "How to report foreign income in India", "description": "For residents.", "steps": [
        {"name": "Fix your residential status", "text": "Count days in India for the year and the earlier years."},
        {"name": "List foreign income", "text": "Salary, interest, dividends, rent and gains, by country."},
        {"name": "Convert and add", "text": "Add to total income at slab or special rates."},
        {"name": "Claim foreign tax credit", "text": "File Form 67 / 44 and Schedule TR with proof of foreign tax."},
        {"name": "Disclose foreign assets", "text": "Schedule FA for RORs, every year."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch IJ complete")
