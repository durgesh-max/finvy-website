# -*- coding: utf-8 -*-
"""Batch GC (24 Nov 2026): ESOP buyback taxation in India - buyback of exercised shares (capital gains from 1 April 2026),
the October 2024 to March 2026 dividend window, secondary sales, and buyback of vested unexercised options (salary vs
capital gains dispute). Call-first page for startup employees, founders and HR/finance teams.
Demand: sweep ac52 (24 Nov 2026), all 7 markets: "esop buyback taxation india", "what is esop buyback", "esop buyback
meaning", "is esop taxable in india". No ESOP buyback page on the site.
Facts (checked 24 Nov 2026):
- Budget 2026 / Finance Act 2026: buybacks on or after 1 April 2026 taxed as capital gains for all shareholders, with an
  additional levy on promoters (effective 30% non-corporate, 22% corporate; promoter definition includes holders above
  10%) (Business Standard, Taxscan, Angel One; site LTCG page). From 1 October 2024 to 31 March 2026 buyback proceeds were
  taxed as deemed dividend with the cost allowed as a capital loss.
- ESOP basics: perquisite at exercise = FMV on exercise date minus exercise price, taxed as salary with employer TDS;
  later sale or buyback: gain = consideration minus FMV at exercise (Treelife, CAclubindia).
- Unlisted shares: long-term if held more than 24 months, 12.5% without indexation; short-term at slab rates. Listed: 12.5%
  above INR 1.25 lakh (over 12 months), 20% short-term.
- Buyback of vested, unexercised options: practice often treats the payment as salary with TDS; Bangalore ITAT (Pramod
  Kumar Jain, reported by EY, September 2026) held it taxable as capital gains, since the perquisite provision taxes only
  securities allotted on exercise. Position not settled."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 24 November 2026."
SLUG = "esop-buyback-taxation-india-2026-capital-gains-vested-options-salary-employees-founders"

C = contact("whether the buyback is of shares you already hold or of vested options, the grant, exercise and buyback dates, the prices, whether the company is listed, and where you are tax resident")
L = lambda h, t: f'<a href="{h}">{t}</a>'
PAGES = [dict(
    slug=SLUG,
    title="ESOP Buyback Taxation in India (2026): Shares Bought Back, Vested Options Cashed Out, and the 1 April 2026 Change",
    em="what you sell back decides how it is taxed.",
    kicker="/ Startups &middot; ESOPs &middot; Buyback tax &middot; Updated 2026-11-24",
    lead=("<strong>An ESOP buyback is taxed in one of two ways, depending on what the company buys back.</strong> "
          "If it buys back <strong>shares you already received on exercise</strong>, the gain over the share&rsquo;s fair market value on the exercise date is a <strong>capital gain</strong> for buybacks on or after <strong>1 April 2026</strong>: for unlisted shares held over 24 months, <strong>12.5%</strong> without indexation; otherwise at your slab rate. "
          "(Between 1 October 2024 and 31 March 2026, buyback money was taxed as a dividend instead.) "
          "If it pays you cash for <strong>vested options you never exercised</strong>, most employers deduct tax as <strong>salary</strong>, but a 2026 Bangalore tribunal ruling held such a payment to be a capital gain, so the position is disputed. "
          "Remember the perquisite tax you paid at exercise: that value is your cost, so it is not taxed twice."),
    sections=[
        ("/ Quick answers", "What employees ask when a buyback is announced.",
         ul("<strong>What is an ESOP buyback?</strong> The company (or an investor or ESOP trust it arranges) buys back employees&rsquo; shares or vested options for cash, giving liquidity before an IPO or sale.",
            "<strong>Is ESOP buyback money taxable in India?</strong> Yes. Shares bought back on or after 1 April 2026 give a capital gain; cash for unexercised options is usually taxed as salary by the employer, though one tribunal has held it to be a capital gain.",
            "<strong>What is my cost?</strong> For shares you exercised, the fair market value on the exercise date (the value already taxed as a perquisite), not the exercise price you paid.",
            "<strong>Long-term or short-term?</strong> Unlisted shares are long-term after 24 months from allotment (12.5%); listed shares after 12 months (12.5% above INR 1.25 lakh). Shorter holdings are short-term.",
            "<strong>Do the promoter rules apply to me?</strong> Only if you count as a promoter, which for this purpose includes holding more than 10% of the company. Ordinary employees pay normal capital gains rates.")),
        ("/ Which treatment applies", "By what is bought back and when.",
         table(["What is bought back", "When", "How it is taxed"], [
             ["Shares you received on exercise, bought back by the company", "On or after 1 April 2026", "Capital gain: buyback price minus FMV on exercise date; 12.5% long-term (unlisted over 24 months) or slab rate"],
             ["Shares you received on exercise, bought back by the company", "1 October 2024 to 31 March 2026", "Whole amount taxed as dividend at slab rate; your cost allowed as a capital loss"],
             ["Shares sold to an investor or ESOP trust (secondary sale)", "Any time", "Capital gain, as above"],
             ["Vested options cashed out without exercise", "Any time", "Usually salary with employer TDS; Bangalore tribunal (2026) held capital gain. Unsettled"],
             ["Exercise itself", "At exercise", "Perquisite (FMV minus exercise price) taxed as salary; startups eligible under the deferral rule can pay this tax later"]])
         + '<p>Work out the exercise-date value with the ' + L("esop-perquisite-tax-calculator.html", "ESOP perquisite tax calculator") + '. Exits on listed shares and reinvestment in a house are covered in ' + L("ca-for-section-54f-esop-exercise-sale-reinvestment-india.html", "ESOP sale and Section 54F") + '.</p>'),
        ("/ Practical points", "Before you accept the buyback offer.",
         ul("<strong>Ask what is being bought back:</strong> shares or options. The offer letter decides the tax treatment and whether the company deducts TDS as salary.",
            "<strong>Keep the exercise-date valuation report:</strong> it fixes your cost; without it you may be taxed on more than your real gain.",
            "<strong>Option cash-outs:</strong> if TDS is deducted as salary and you want to take the capital gains position, take advice first; it can be contested.",
            "<strong>Employees abroad:</strong> non-resident employees face TDS at non-resident rates on the capital gain and may get treaty relief; their home country may also tax the gain.",
            "<strong>Reinvestment:</strong> Section 54F can exempt a long-term gain on shares if the net consideration goes into one residential house in India; 54EC bonds do not apply to share gains.",
            "<strong>Companies running a buyback:</strong> follow the Companies Act buyback rules (or arrange a secondary purchase), value the shares properly and plan the TDS; see " + L("how-to-issue-esops-india.html", "issuing ESOPs in India") + ".")
         + call_box("an ESOP buyback", ["Shares or options: which treatment applies",
                                         "Your cost and holding period",
                                         "TDS on the payment and how to claim credit",
                                         "Section 54F reinvestment",
                                         "Non-resident employees and treaty relief"],
                    "the offer letter, grant and exercise details, valuation reports and your residence.")
         + sources("Finance Act, 2026 (buybacks taxed as capital gains from 1 April 2026; additional levy on promoters), as reported by Business Standard, Taxscan and others; Finance (No. 2) Act, 2024 (buyback as deemed dividend from 1 October 2024); Income-tax Act provisions on ESOP perquisites, cost of acquisition and capital gains rates (12.5% long-term from 23 July 2024); EY tax alert on the Bangalore ITAT ruling in Pramod Kumar Jain (September 2026) on buyback of vested options; Treelife and CAclubindia guides on ESOP taxation. Checked 24 November 2026.")),
    ],
    faqs=[("How is ESOP buyback taxed in India in 2026?", "If the company buys back shares you received on exercise, on or after 1 April 2026 the gain over the fair market value on the exercise date is a capital gain: 12.5% for unlisted shares held over 24 months, otherwise at slab rates. Cash paid for vested options never exercised is usually taxed as salary, although a 2026 Bangalore tribunal ruling treated it as a capital gain."),
          ("What is an ESOP buyback?", "A company, an investor or an ESOP trust buying back employees' shares or vested options for cash, usually to give employees liquidity before an IPO or acquisition."),
          ("Is ESOP buyback taxed as dividend?", "Only for company buybacks between 1 October 2024 and 31 March 2026. From 1 April 2026 buybacks are taxed as capital gains again."),
          ("What is the cost of ESOP shares for capital gains?", "The fair market value on the date of exercise, which was already taxed as a perquisite, not the exercise price you paid."),
          ("Is cash for unexercised ESOPs salary or capital gain?", "Disputed. Employers usually deduct tax as salary. A Bangalore tribunal held in 2026 that it is a capital gain because the perquisite rule taxes only shares allotted on exercise. Take advice before filing on that basis."),
          ("Can BQP help with an ESOP buyback?", "Yes. " + C)],
    related=[("esop-perquisite-tax-calculator.html", "ESOP perquisite tax calculator"),
             ("ca-for-section-54f-esop-exercise-sale-reinvestment-india.html", "ESOP sale and Section 54F"),
             ("ltcg-12-5-percent-new-capital-gains-india-2026.html", "LTCG at 12.5%"),
             ("how-to-issue-esops-india.html", "Issuing ESOPs in India"),
             ("esop-vs-rsu-vs-phantom-stock-india-us.html", "ESOP vs RSU vs phantom stock")],
    cta_h="ESOP buyback offer on the table?", cta_b=C,
    keywords="ESOP buyback taxation India, what is ESOP buyback, ESOP buyback meaning, is ESOP taxable in India, ESOP buyback capital gains 2026, buyback tax 1 April 2026, vested options buyback salary or capital gain, unlisted shares buyback tax",
    desc="ESOP buyback taxation in India (2026): shares bought back on or after 1 April 2026 give a capital gain (12.5% for unlisted shares held over 24 months), the October 2024 to March 2026 dividend window, secondary sales, and the salary vs capital gains dispute on cashing out vested options.",
    howto={"name": "How an employee handles an ESOP buyback for tax", "description": "Steps before and after the buyback.", "steps": [
        {"name": "Identify what is bought back", "text": "Shares received on exercise, or vested options."},
        {"name": "Find your cost", "text": "Fair market value on the exercise date, from the valuation report."},
        {"name": "Check holding period", "text": "Over 24 months for unlisted shares means long-term at 12.5%."},
        {"name": "Check TDS", "text": "Whether the company deducts as salary or on capital gains."},
        {"name": "Report in your return", "text": "Capital gains schedule or salary, and consider Section 54F."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch GC complete")
