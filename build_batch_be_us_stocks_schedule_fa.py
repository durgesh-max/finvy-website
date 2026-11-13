# -*- coding: utf-8 -*-
"""Batch BE (10 Nov 2026): US stocks bought from India through investment apps (LRS) - Schedule FA and FAST-DS.
Facts: Schedule FA applies to residents and ordinarily residents; for AY 2026-27 it follows the calendar year ending
31 December 2025; holdings must be reported even with no sale; uninvested wallet cash is reported too; dividends go in
Schedule FSI with foreign tax credit in Schedule TR and Form 67; unreported holdings bought from income taxed in India
-> FAST-DS Category 2 (INR 1 lakh, asset up to INR 5 crore, Finance Act 2026 s.133 Table item 2(b)); unreported dividends
or gains taxable in India -> undisclosed foreign income, Category 1 at 60%; declarations close 31 December 2026;
INR 10 lakh Black Money Act penalty for non-disclosure where foreign assets other than immovable property exceed INR 20 lakh."""
from urllib.parse import quote
from build_lib import page, write_page

UPDATED = "Last updated: 12 November 2026."
CK = ("fast-ds-2026-eligibility-checker.html?kind=asset&then=yes&src=taxedIndia&fa=no&inc=yes&val=500000")
CK_INC = "fast-ds-2026-eligibility-checker.html?kind=income&then=yes&inc=no&val=50000"


def wa(t):
    return "https://wa.me/917801887130?text=" + quote(t)


def ul(*x):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in x) + "</ul>"


def ol(*x):
    return "<ol>" + "".join(f"<li>{i}</li>" for i in x) + "</ol>"


def table(head, rows):
    return ("<table><thead><tr>" + "".join(f"<th>{h}</th>" for h in head) + "</tr></thead><tbody>"
            + "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows) + "</tbody></table>")


CONTACT = ("WhatsApp +91 78018 87130 or email durgesh@bharatquantumprospera.com with your app statements and the years you invested. "
           "We reply the same working day with what is needed and a fixed-scope quote.")
SLUG = "us-stocks-bought-from-india-not-in-schedule-fa-fast-ds-vested-indmoney"
BOX = (f'<div style="border:1px solid var(--line);border-left:4px solid #C2312A;border-radius:10px;padding:16px 18px;margin:18px 0;background:var(--bg-soft)">'
       f'<p style="margin:0 0 8px;font-weight:600">Check your own case in one minute</p>'
       f'<p style="margin:0">Open the <a href="{CK}"><strong>FAST-DS checker pre-filled for US stocks bought from taxed income</strong></a> and change the value to yours, '
       f'or check <a href="{CK_INC}">unreported dividends</a>. Or message CA Durgesh Chavda on <a href="{wa("Hi Durgesh, I bought US stocks from India and did not report them in Schedule FA.")}" target="_blank" rel="noopener"><strong>WhatsApp</strong></a>.</p></div>')

PAGES = [dict(
    slug=SLUG,
    title="Bought US Stocks From India but Never Reported Them in Schedule FA? What to Do Before 31 December 2026 (FAST-DS)",
    em="the app made buying easy; the return did not.",
    kicker="/ US stocks via LRS &middot; Schedule FA &middot; Updated 2026-11-10",
    lead=("If you are resident and ordinarily resident in India and hold US shares or ETFs bought through an investment app, every holding belongs in Schedule FA of your return, even if you never sold anything, and so does uninvested cash in the app's US wallet. "
          "For the return for FY 2025-26 (AY 2026-27), Schedule FA follows the calendar year ending 31 December 2025. "
          "Missed it? Shares bought with income already taxed in India usually fall in FAST-DS Category 2: a flat INR 1 lakh for assets up to INR 5 crore, if you declare by 31 December 2026. Dividends or gains that were never offered to tax are a separate Category 1 item at 60%."),
    sections=[
        ("/ What goes where", "In your Indian return.",
         table(["Item", "Where it is reported", "Tax point"], [
             ["US shares and ETFs you hold (sold or not)", "Schedule FA, calendar-year basis", "Reporting only; no tax just for holding"],
             ["Cash left in the app's US wallet", "Schedule FA (foreign custodial or depository account)", "Reporting only"],
             ["Dividends (usually with 25% US tax withheld after a W-8BEN)", "Schedule FSI, with credit in Schedule TR", "Taxable in India; file Form 67 to claim the US tax as credit"],
             ["Sale of shares", "Capital gains schedule (and FSI)", "Long-term after 24 months for foreign shares"]])
         + BOX),
        ("/ If you missed Schedule FA", "Your options before 31 December 2026.",
         ul("<strong>FAST-DS Category 2, INR 1 lakh:</strong> for shares bought from income already taxed in India (salary, business income, savings) and not shown in Schedule FA. One fee covers foreign assets worth up to INR 5 crore in total, and it brings immunity under the Black Money Act for what you declare.",
            "<strong>FAST-DS Category 1, 60%:</strong> for dividends or gains that were taxable in India but never offered to tax, within the INR 1 crore aggregate.",
            "<strong>Revised return:</strong> fixes the FY 2025-26 return only (free until 31 December 2026, with a fee until 31 March 2027). It does not cover earlier years or give Black Money Act immunity for them.",
            "<strong>Small holdings:</strong> if the money was taxed and your foreign assets other than property never exceeded INR 20 lakh in total, the INR 10 lakh Black Money Act penalty for non-disclosure does not apply. A revised return for FY 2025-26 and correct reporting from now on may then be enough; FAST-DS mainly buys certainty for earlier years. Check the totals year by year before paying INR 1 lakh.",
            "<strong>Doing nothing:</strong> the Black Money Act allows a penalty of INR 10 lakh for not disclosing foreign assets in a return where they exceed INR 20 lakh (other than immovable property), apart from tax on undisclosed income.")
         + '<p>Compare routes: <a href="fast-ds-vs-revised-return-vs-updated-return-itr-u.html">FAST-DS vs revised return vs ITR-U</a> &middot; cost: <a href="fast-ds-2026-calculator-foreign-asset-disclosure-cost.html">FAST-DS calculator</a> &middot; dates: <a href="fast-ds-payment-due-date-interest-calculator-itns-289-form-3-form-4.html">payment calculator</a>.</p>'),
        ("/ Before you declare", "Collect these.",
         ol("Your app's tax documents: the Schedule FA report (calendar year) and the dividend and tax statement.",
            "The value of each holding as on 31 March 2026, the valuation date for FAST-DS.",
            "Proof the money came from taxed income: LRS remittance records (Form A2, bank debit) and your returns for those years.",
            "Whether dividends and any sales were reported in each year's return.",
            "Your residential status for each year: in RNOR or NRI years Schedule FA was not required.")
         + '<p>Related: <a href="how-to-buy-us-stocks-from-india-2026.html">how to buy US stocks from India</a> &middot; <a href="what-is-form-w-8ben.html">Form W-8BEN</a> &middot; <a href="nri-us-estate-tax-indian-assets.html">US estate tax exposure on US shares</a> &middot; <a href="fast-ds-rsu-espp-us-shares-401k-which-category.html">RSUs and ESPP</a>.</p>'
         f'<p><strong>Sources:</strong> Income-tax return instructions for Schedule FA, FSI and TR; Finance Act, 2026, Chapter IV (FAST-DS), section 133; Black Money (Undisclosed Foreign Income and Assets) and Imposition of Tax Act, 2015, section 43. <em>{UPDATED}</em> General information, not advice for your situation.</p>'),
    ],
    faqs=[("Do I need to report US stocks in Schedule FA if I never sold them?", "Yes, if you are resident and ordinarily resident. Holdings are reported whether or not you sold, along with any uninvested cash in the US wallet."),
          ("Which period does Schedule FA cover for AY 2026-27?", "The calendar year ending 31 December 2025, not the April to March financial year."),
          ("I bought US stocks through an app and missed Schedule FA. Is FAST-DS Category 1 or 2?", "Usually Category 2, a flat INR 1 lakh, if the money came from income already taxed in India. Unreported dividends or gains are a separate Category 1 item at 60%."),
          ("My US portfolio is small. Is FAST-DS worth INR 1 lakh?", "Not always. If the money was taxed and your foreign assets other than property stayed within INR 20 lakh in total, the INR 10 lakh Black Money Act penalty does not apply, and a revised return for FY 2025-26 with correct reporting going forward may be enough. Larger holdings or several missed years usually favour FAST-DS."),
          ("Where do I report dividends from US stocks?", "In Schedule FSI, with the US tax withheld claimed as credit in Schedule TR. File Form 67 to claim the credit."),
          ("What is the deadline to fix it under FAST-DS?", "Declarations close on 31 December 2026. The payment follows the Form 2 order."),
          ("Can BQP check my app statements and file?", "Yes. " + CONTACT)],
    related=[("fast-ds-2026-eligibility-checker.html", "FAST-DS eligibility checker"), ("fast-ds-rsu-espp-us-shares-401k-which-category.html", "FAST-DS for RSUs and US shares"),
             ("how-to-buy-us-stocks-from-india-2026.html", "How to buy US stocks from India")],
    cta_h="US stocks missing from your return?", cta_b=CONTACT,
    keywords="US stocks Schedule FA, report US stocks in ITR, Vested Schedule FA, INDmoney Schedule FA, US stocks not reported FAST-DS, LRS US stocks foreign asset disclosure, Schedule FA calendar year 2025, US dividend Schedule FSI Form 67",
    desc="Resident in India with US stocks bought through an app (LRS) but missing from Schedule FA? What to report (calendar-year basis, wallet cash, dividends in FSI and Form 67) and how FAST-DS Category 2 (INR 1 lakh) fixes it before 31 December 2026.",
    howto={"name": "How to fix unreported US stocks with FAST-DS", "description": "Steps for a resident who bought US shares through an investment app and missed Schedule FA.", "steps": [
        {"name": "Download app tax documents", "text": "Get the Schedule FA and dividend reports from your investment app."},
        {"name": "Value holdings on 31 March 2026", "text": "Note the value of each holding as on 31 March 2026."},
        {"name": "Check the category", "text": "Shares from taxed income missing from Schedule FA are usually Category 2; unreported dividends or gains are Category 1."},
        {"name": "File Form 1 by 31 December 2026", "text": "Declare on the e-Filing portal, then pay after the Form 2 order and file Form 3."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch BE complete")
