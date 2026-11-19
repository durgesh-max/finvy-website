# -*- coding: utf-8 -*-
"""Batch DM (19 Nov 2026): RSU taxation in India for US-listed (foreign) employer shares - employees of foreign MNCs and
the Indian subsidiaries that run payroll. Call-first page.
Demand: autocomplete sweep 19 Nov 2026 (ac16), all 7 markets: "rsu taxation india", "rsu tax india", "rsu taxation in
india for us stocks", "rsu taxation in india example", "rsu taxation in india for us stocks calculator".
Facts (checked 19 Nov 2026; secondary sources Treelife, ClearTax, EquityList, CalcGuru, The Tax Corp): two tax points -
perquisite at vesting (fair market value on vesting, taxed as salary at slab rates, TDS by the Indian employer,
including sell-to-cover), and capital gains on sale; foreign shares are unlisted for Indian purposes - long-term after
24 months at 12.5% without indexation and without the INR 1.25 lakh exemption, short-term at slab rates; cost of
acquisition = FMV taxed as perquisite; valuation of foreign-listed shares - sources differ (merchant banker under the
rules vs exchange price converted at SBI TT buying rate) so follow the employer's documented method; dividends from US
shares - US withholds (25% under the India-US treaty for portfolio holdings), credit via Form 67; Schedule FA
(calendar-year reporting) for resident and ordinarily resident employees, including unvested holdings at the broker as
applicable; Income-tax Act, 2025 recasts the perquisite provision from FY 2026-27."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

HUB = "foreign-company-india-advisor-market-research-entity-due-diligence-m-and-a-joint-venture-2026"
RSU = "rsu-taxation-india-us-stocks-vesting-perquisite-capital-gains-schedule-fa-2026"

C_RSU = contact("your employer, vesting and sale history, residential status and whether you held the shares while abroad")
PAGES = [dict(
    slug=RSU,
    title="RSU Taxation in India for US Stocks (2026): Tax at Vesting, Capital Gains on Sale, Dividends, Schedule FA and Foreign Tax Credit - With Example",
    em="for employees of foreign companies in India and the employers who run their payroll.",
    kicker="/ Employees &middot; Foreign employers &middot; RSU &middot; Updated 2026-11-19",
    lead=("RSUs of a US or other foreign employer are taxed in India <strong>twice</strong>. First, at <strong>vesting</strong>, the fair market value of the shares is a <strong>salary perquisite</strong>, taxed at your slab rate, and the Indian employer deducts TDS, often through sell-to-cover. Second, when you <strong>sell</strong>, you pay <strong>capital gains</strong> on the rise above the value already taxed at vesting. "
          "Foreign shares are treated as <strong>unlisted</strong> in India. Gains after <strong>24 months</strong> are long-term and taxed at <strong>12.5%</strong> with no indexation and no INR 1.25 lakh exemption; earlier gains are taxed at slab rates. "
          "Dividends suffer <strong>US withholding</strong> (25% under the treaty for most employees), creditable in India by filing <strong>Form 67</strong>. Resident and ordinarily resident employees must report the shares and the broker account in <strong>Schedule FA</strong> every year. Missing it is the most common and costliest mistake."),
    sections=[
        ("/ How RSUs are taxed, step by step", "With an illustrative example.",
         table(["Event", "Indian tax", "Example (illustrative)"], [
             ["Grant", "No tax", "100 RSUs granted"],
             ["Vesting", "Perquisite = fair market value on vesting x shares; salary at slab rate; employer TDS", "25 vest at USD 200 = USD 5,000, converted to INR at the applicable rate and added to salary"],
             ["Sell-to-cover", "Shares sold to fund TDS; usually little or no gain", "Some shares sold on vesting day"],
             ["Holding", "Report in Schedule FA (calendar year) if resident and ordinarily resident", "Shares and broker account shown with peak and closing values"],
             ["Dividend", "Taxable in India at slab rate; credit for US withholding via Form 67", "US withholds 25%; claim credit up to Indian tax on it"],
             ["Sale", "Capital gain = sale price minus vesting value; over 24 months 12.5%, otherwise slab rate", "Sold after 30 months at USD 260: gain of USD 60 per share at 12.5%"]])
         + call_box("RSU tax and reporting", ["Whether past vesting and sales were taxed and reported correctly",
                                               "Schedule FA and FAST-DS exposure for missed years",
                                               "Foreign tax credit on dividends and any US tax withheld",
                                               "Tax on RSUs earned partly while working abroad",
                                               "For employers: payroll TDS, valuation method and recharge from the parent"],
                    "your broker statements (vesting, sale, dividends), Form 16 and residential status for the relevant years.")),
        ("/ Where employees go wrong", "And how to fix it.",
         ul("<strong>Schedule FA left blank:</strong> foreign shares and broker accounts must be reported every year by resident and ordinarily resident individuals, even with no sale; see <a href=\"fast-ds-rsu-espp-us-shares-401k-which-category.html\">RSUs and FAST-DS</a>.",
            "<strong>Wrong cost on sale:</strong> the cost is the value already taxed at vesting, not zero; using zero overstates the gain.",
            "<strong>Treating US shares like Indian listed shares:</strong> foreign shares do not get the INR 1.25 lakh long-term exemption or the listed-share rates.",
            "<strong>Dividend credit not claimed:</strong> file Form 67 before the return to claim credit for US withholding; see <a href=\"form-67-foreign-tax-credit-india-2026.html\">Form 67</a>.",
            "<strong>Valuation method:</strong> sources differ on how vesting value is fixed for foreign-listed shares (merchant banker valuation under the rules, or exchange price converted at the SBI TT buying rate); follow and keep your employer's documented method.",
            "<strong>Moved to or from India:</strong> RSUs earned partly while working abroad may be taxed in India only for the India-service portion, depending on residency and the treaty.")),
        ("/ For foreign employers and Indian subsidiaries", "Payroll and recharge.",
         ul("The Indian employer deducts TDS on the perquisite at vesting and reports it in Form 16; sell-to-cover or cash collection must fund the TDS on time.",
            "If the foreign parent recharges the RSU cost to the Indian subsidiary, the recharge needs an agreement and transfer pricing support, and withholding may apply.",
            "Employees holding foreign employer shares is permitted under India's overseas investment rules; keep plan documents and statements for the bank and tax officer.",
            "From FY 2026-27 the perquisite provision sits in the Income-tax Act, 2025; the principles are unchanged.")
         + f'<p>Related: <a href="esop-vs-rsu-vs-phantom-stock-india-us.html">ESOP vs RSU vs phantom stock</a> &middot; <a href="esop-perquisite-tax-calculator.html">ESOP perquisite tax calculator</a> &middot; <a href="us-stocks-bought-from-india-not-in-schedule-fa-fast-ds-vested-indmoney.html">US stocks not in Schedule FA</a> &middot; <a href="expat-tax-india-foreign-employee-residency-rnor-salary-pf-dtaa-2026.html">expat tax in India</a> &middot; <a href="{HUB}.html">working with an Indian CA as a foreign company</a>.</p>'
         + sources("Income-tax Act, 1961 (section 17(2)(vi), capital gains) and Income-tax Act, 2025 from FY 2026-27; Income-tax Rules (perquisite valuation); India-US tax treaty (Article 10); Form 67 rules. Secondary guides checked 19 November 2026: Treelife, ClearTax, EquityList, CalcGuru, The Tax Corp. The example uses round illustrative numbers only.")),
    ],
    faqs=[("How are RSUs taxed in India?", "At vesting, the fair market value is taxed as salary (perquisite) with employer TDS; on sale, the increase over the vesting value is taxed as capital gains."),
          ("What is the capital gains tax on selling US RSU shares in India?", "Foreign shares are treated as unlisted: gains on shares held over 24 months are taxed at 12.5% without indexation or the INR 1.25 lakh exemption; shorter holdings are taxed at slab rates."),
          ("Do I need to report RSUs in Schedule FA?", "Yes, if you are resident and ordinarily resident: report the foreign shares and the broker account every year (calendar-year basis), even if you did not sell."),
          ("How are dividends on US RSU shares taxed?", "The US withholds tax (25% under the India-US treaty for most employees); the dividend is taxable in India and you claim credit for the US tax by filing Form 67."),
          ("What is the cost of acquisition for RSU shares?", "The fair market value on vesting that was taxed as a perquisite, so the capital gain is only the increase after vesting."),
          ("Can BQP fix past RSU reporting?", "Yes. " + C_RSU)],
    related=[("esop-vs-rsu-vs-phantom-stock-india-us.html", "ESOP vs RSU vs phantom stock"), ("form-67-foreign-tax-credit-india-2026.html", "Form 67 foreign tax credit"),
             ("fast-ds-rsu-espp-us-shares-401k-which-category.html", "RSUs and FAST-DS")],
    cta_h="RSUs from a foreign employer?", cta_b=C_RSU,
    keywords="RSU taxation India, RSU tax India US stocks, RSU taxation in India example, RSU perquisite vesting India, capital gains on US shares India 12.5 percent, RSU Schedule FA, RSU dividend foreign tax credit Form 67, sell to cover TDS India",
    desc="RSU taxation in India for US stocks (2026): perquisite at vesting with employer TDS, capital gains on sale (foreign shares unlisted: 12.5% after 24 months, no INR 1.25 lakh exemption), dividends and Form 67 credit, Schedule FA, common mistakes and employer points, with an illustrative example.",
    howto={"name": "How to handle RSU tax in India", "description": "From vesting to sale.", "steps": [
        {"name": "Record vesting values", "text": "Keep the vesting date, shares and value taxed as perquisite (Form 16)."},
        {"name": "Report holdings", "text": "Show shares and broker account in Schedule FA every year if resident and ordinarily resident."},
        {"name": "Claim dividend credit", "text": "File Form 67 for US tax withheld on dividends."},
        {"name": "Compute gains on sale", "text": "Sale price minus vesting value; 12.5% if held over 24 months."},
        {"name": "Fix past gaps", "text": "Revise or update returns, or use the disclosure route if foreign assets were missed."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch DM complete:", len(PAGES))
