# -*- coding: utf-8 -*-
"""Batch IF (25 Nov 2026): ESOP taxation in India 2026 - two-stage tax: perquisite at exercise (FMV on exercise date
minus exercise price, taxed as salary with TDS by the employer), capital gains on sale (cost = FMV used for the
perquisite; holding period from allotment / exercise; listed equity long-term after 12 months, 12.5% above Rs 1.25 lakh,
short-term 20%; unlisted and foreign shares long-term after 24 months at 12.5%, else slab). Eligible-startup deferral
(DPIIT-recognised + IMB-certified eligible startup): under the 1961 Act (section 192(1C)) TDS / tax deferred to the
earliest of 48 months from the end of the assessment year of allotment, sale, or leaving employment; under the 2025 Act
(section 392(3) read with section 289(3) per commentary) expressed as 60 months from the end of the tax year of
allotment - the same span restated because the 2025 Act has no assessment year (commentary calling it an 'extension' is
noted). TDS within 14 days of the trigger. Foreign-parent ESOPs / RSUs: perquisite taxed in India; LRS for exercise
payments; Schedule FA reporting; foreign tax credit with Form 67 / Form 44.
Demand: sweep ac108 (25 Nov 2026), all 7 markets: "esop taxation", "esop taxation in india", "esop taxation for
employees", "esop taxation for nri", "esop taxation in hands of employee", "esop taxation example", "esop foreign company
indian employee taxation", "do i have to pay taxes on esop".
Facts (checked 25 Nov 2026): Income Tax Department page 'Taxation of ESOP'; CAclubindia (ESOP taxation under Income Tax
Act 2025, 7 Sept 2026; ESOP deferral article, 30 June 2026); KSK; Taxguru; site pages (ESOP perquisite calculator, ESOP
buyback, RSU taxation)."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 25 November 2026."
SLUG = "esop-taxation-india-2026-perquisite-at-exercise-capital-gains-startup-deferral-foreign-esop-rsu"

C = contact("your employer (Indian company, eligible startup or foreign parent), grant and exercise dates, exercise price and fair market value, and whether you are resident or NRI")
L = lambda h, t: f'<a href="{h}">{t}</a>'
PAGES = [dict(
    slug=SLUG,
    title="ESOP Taxation in India 2026: Tax at Exercise and on Sale, Startup Deferral, NRIs and Foreign Company ESOPs",
    em="two tax points, and the first one comes before you have any cash.",
    kicker="/ Employees with stock options &middot; Income tax &middot; Updated 2026-11-25",
    lead=("<strong>ESOPs are taxed twice in India: first when you exercise the option, on the difference between the share&rsquo;s fair market value on the exercise date and the price you pay, which is taxed as salary; and again when you sell the shares, as capital gains on the rise above that fair market value.</strong> "
          "Your employer deducts TDS on the exercise-date perquisite. Employees of eligible startups (DPIIT-recognised and certified by the Inter-Ministerial Board) can defer that tax until they sell, leave the company or the time limit runs out. "
          "ESOPs and RSUs from a foreign parent company are taxed the same way in India, and the shares must also be reported in Schedule FA."),
    sections=[
        ("/ Quick answers", "What people search for.",
         ul("<strong>Do I have to pay tax on ESOPs?</strong> Not at grant or vesting of an option. Tax arises at exercise (perquisite) and at sale (capital gains).",
            "<strong>How is the perquisite calculated?</strong> (Fair market value on the exercise date &minus; exercise price) &times; number of shares, added to salary and taxed at your slab rate; see the " + L("esop-perquisite-tax-calculator.html", "ESOP perquisite tax calculator") + ".",
            "<strong>How are gains on sale taxed?</strong> The cost is the fair market value used for the perquisite. Listed Indian shares: long-term after 12 months, 12.5% above &#8377;1.25 lakh a year; short-term 20%. Unlisted and foreign shares: long-term after 24 months at 12.5%, otherwise slab rates.",
            "<strong>What is the startup ESOP tax deferral?</strong> For eligible startups, tax on the perquisite is deferred to the earliest of: the time limit, the sale of the shares, or leaving the employer; the employer then deducts TDS within 14 days of that event.",
            "<strong>Is the deferral 48 or 60 months?</strong> Under the 1961 Act it ran 48 months from the end of the assessment year of allotment; the Income-tax Act, 2025 has no assessment year and states it as 60 months from the end of the tax year of allotment, which is the same span. Some commentary describes this as an extension.",
            "<strong>Are NRIs taxed on Indian ESOPs?</strong> The perquisite relates to Indian employment, so it is generally taxable in India, apportioned by days worked in India where the employee moved abroad between grant and vesting; treaty relief may apply.")),
        ("/ Example (illustrative)", "Exercise, then sale.",
         table(["Step", "Figure", "Tax treatment"], [
             ["Exercise 1,000 options at &#8377;10", "FMV on exercise &#8377;210", "Perquisite &#8377;2,00,000 taxed as salary, TDS by employer"],
             ["Sell 30 months later at &#8377;510 (unlisted)", "Gain &#8377;300 &times; 1,000 = &#8377;3,00,000", "Long-term capital gain at 12.5%"],
             ["Sell 12 months later instead", "Same gain", "Short-term, taxed at slab rates"]])
         + '<p>Figures are illustrative only. Valuation of unlisted shares for the perquisite uses a merchant banker valuation; see ' + L("best-ca-esop-valuation-409a-rule-11ua-india.html", "ESOP valuation") + '.</p>'),
        ("/ Foreign company ESOPs and RSUs", "For Indian employees of global groups.",
         ul("<strong>Taxed in India:</strong> the perquisite at exercise (ESOP) or vesting (RSU) is salary income, with TDS by the Indian employer; see " + L("rsu-taxation-india-us-stocks-vesting-perquisite-capital-gains-schedule-fa-2026.html", "RSU taxation for US stocks") + ".",
            "<strong>Paying the exercise price:</strong> remitting money abroad to exercise options is under the Liberalised Remittance Scheme, with TCS where applicable; see the " + L("lrs-tcs-calculator.html", "LRS TCS calculator") + ".",
            "<strong>Report every year:</strong> shares held abroad go in Schedule FA of the ITR even if not sold.",
            "<strong>Foreign tax:</strong> if the shares are taxed abroad too, claim foreign tax credit with Form 67 (Form 44 from tax year 2026-27).",
            "<strong>Comparing instruments:</strong> see " + L("esop-vs-rsu-vs-phantom-stock-india-us.html", "ESOP vs RSU vs phantom stock") + " and, for buybacks, " + L("esop-buyback-taxation-india-2026-capital-gains-vested-options-salary-employees-founders.html", "ESOP buyback taxation") + ".")
         + call_box("ESOP tax", ["Perquisite and TDS on exercise",
                                  "Startup deferral eligibility",
                                  "Capital gains on sale and reinvestment",
                                  "Foreign parent ESOPs and RSUs",
                                  "Schedule FA and foreign tax credit"],
                    "the grant, exercise and sale details.")
         + sources("Income Tax Department page on taxation of ESOPs; Income-tax Act, 1961 sections 17(2)(vi), 192(1C) and 80-IAC and their counterparts in the Income-tax Act, 2025 (deferral reported as section 392(3) read with section 289(3)); CAclubindia commentary (7 September 2026 and 30 June 2026); KSK and Taxguru guides. Checked 25 November 2026.")),
    ],
    faqs=[("How are ESOPs taxed in India?", "At two points: at exercise, the difference between the fair market value on the exercise date and the exercise price is a salary perquisite taxed at slab rates with TDS; at sale, the gain over that fair market value is a capital gain, long-term or short-term depending on the holding period and whether the shares are listed."),
          ("Do I pay tax when ESOPs vest?", "Not for options. Tax arises when you exercise the option and again when you sell the shares. RSUs, which are shares rather than options, are taxed at vesting."),
          ("What is the ESOP tax deferral for startups?", "Employees of eligible startups (DPIIT-recognised and IMB-certified) can defer tax on the ESOP perquisite until the earliest of the time limit, sale of the shares or leaving the employer. Under the 1961 Act the limit was 48 months from the end of the assessment year of allotment; under the 2025 Act it is stated as 60 months from the end of the tax year of allotment."),
          ("How are ESOPs from a foreign parent company taxed in India?", "The perquisite at exercise is taxed in India as salary, with TDS by the Indian employer. The foreign shares must be reported in Schedule FA every year, and gains on sale are taxed as capital gains, long-term after 24 months at 12.5%."),
          ("Are NRIs taxed on ESOPs in India?", "Generally yes, for the part of the benefit that relates to employment in India, often apportioned by days worked in India between grant and vesting, subject to the relevant tax treaty."),
          ("Can BQP help with ESOP taxation?", "Yes. CA Durgesh Chavda can compute the perquisite and TDS, check startup deferral eligibility, plan the sale and handle foreign ESOP reporting. " + C)],
    related=[("esop-perquisite-tax-calculator.html", "ESOP perquisite tax calculator"),
             ("rsu-taxation-india-us-stocks-vesting-perquisite-capital-gains-schedule-fa-2026.html", "RSU taxation for US stocks"),
             ("esop-buyback-taxation-india-2026-capital-gains-vested-options-salary-employees-founders.html", "ESOP buyback taxation"),
             ("esop-vs-rsu-vs-phantom-stock-india-us.html", "ESOP vs RSU vs phantom stock"),
             ("how-to-issue-esops-india.html", "How to issue ESOPs in India")],
    cta_h="Exercising or selling ESOPs?", cta_b=C,
    keywords="ESOP taxation India, ESOP taxation for employees, ESOP tax at exercise, ESOP perquisite tax, ESOP capital gains, startup ESOP tax deferral, ESOP taxation for NRI, foreign company ESOP India, do I have to pay tax on ESOP",
    desc="ESOP taxation in India 2026: perquisite at exercise (FMV minus exercise price) taxed as salary with TDS, capital gains on sale, startup deferral (48 months from end of AY / 60 months from end of tax year), NRIs, and foreign parent ESOPs and RSUs.",
    howto={"name": "How ESOP tax is worked out", "description": "From exercise to sale.", "steps": [
        {"name": "Note the exercise-date FMV", "text": "Market price for listed shares; merchant banker valuation for unlisted."},
        {"name": "Compute the perquisite", "text": "FMV minus exercise price, times shares exercised."},
        {"name": "Check startup deferral", "text": "Only for DPIIT-recognised, IMB-certified eligible startups."},
        {"name": "Track the holding period", "text": "12 months listed; 24 months unlisted or foreign."},
        {"name": "Compute capital gains on sale", "text": "Sale price minus the exercise-date FMV."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch IF complete")
