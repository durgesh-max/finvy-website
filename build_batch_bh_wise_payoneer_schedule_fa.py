# -*- coding: utf-8 -*-
"""Batch BH (11 Nov 2026): Wise, Payoneer, PayPal or Revolut balances of residents (freelancers) - Schedule FA and FAST-DS.
Facts: residents and ordinarily residents report foreign depository/custodial accounts held at any time in the calendar
year in Schedule FA (peak and closing balance, income); not needed in NRI or RNOR years. Income earned through them is
reported in the normal schedules. Black Money Act ss.42/43 proviso (from 1 October 2024): no INR 10 lakh penalty where the
aggregate value of foreign assets other than immovable property does not exceed INR 20 lakh. FAST-DS Category 2: INR 1 lakh
for foreign assets from taxed income missing from Schedule FA (up to INR 5 crore); declarations close 31 December 2026.
Revised return for FY 2025-26: free until 31 December 2026, with the s.234-I fee until 31 March 2027."""
from urllib.parse import quote
from build_lib import page, write_page

UPDATED = "Last updated: 11 November 2026."
CK = "fast-ds-2026-eligibility-checker.html?kind=asset&then=yes&src=taxedIndia&fa=no&inc=yes&val=800000"


def wa(t):
    return "https://wa.me/917801887130?text=" + quote(t)


def ul(*x):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in x) + "</ul>"


def table(head, rows):
    return ("<table><thead><tr>" + "".join(f"<th>{h}</th>" for h in head) + "</tr></thead><tbody>"
            + "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows) + "</tbody></table>")


CONTACT = ("WhatsApp +91 78018 87130 or email durgesh@bharatquantumprospera.com with your account statements and the years you held them. "
           "We reply the same working day with what is needed and a fixed-scope quote.")
SLUG = "wise-payoneer-paypal-revolut-balance-schedule-fa-freelancer-fast-ds"
BOX = (f'<div style="border:1px solid var(--line);border-left:4px solid #C2312A;border-radius:10px;padding:16px 18px;margin:18px 0;background:var(--bg-soft)">'
       f'<p style="margin:0 0 8px;font-weight:600">Small balances: weigh the INR 20 lakh rule before paying INR 1 lakh</p>'
       f'<p style="margin:0">If the income was taxed and your foreign assets other than property never exceeded INR 20 lakh in total, the Black Money Act&rsquo;s INR 10 lakh non-disclosure penalty does not apply. '
       f'Then a revised return and correct reporting from now on may be enough, and FAST-DS mainly buys certainty. Above that, or with several years missed, FAST-DS Category 2 is usually the cleaner fix. '
       f'<a href="{CK}"><strong>Check your case in the FAST-DS checker</strong></a> or message CA Durgesh Chavda on '
       f'<a href="{wa("Hi Durgesh, I am a freelancer with a Wise/Payoneer balance abroad and want to check Schedule FA.")}" target="_blank" rel="noopener"><strong>WhatsApp</strong></a>.</p></div>')

PAGES = [dict(
    slug=SLUG,
    title="Wise, Payoneer, PayPal or Revolut Balance Abroad: Does It Go in Schedule FA? (Freelancers, 2026)",
    em="the income is in your return; is the account?",
    kicker="/ Freelancers &middot; Foreign wallets &middot; Schedule FA &middot; Updated 2026-11-11",
    lead=("If you are resident and ordinarily resident in India and hold money in an account with a foreign provider, such as a Wise, Payoneer or Revolut account opened abroad or a USD balance kept with a foreign entity, that account belongs in Schedule FA for every calendar year you held it, with its peak and closing balance. "
          "Showing the freelance income in your return does not cover the account. "
          "A service that pays straight into your Indian bank and never holds a foreign balance usually leaves nothing to report. "
          "Missed it? Because the income was taxed, it is usually FAST-DS Category 2 (INR 1 lakh), but for small balances the INR 20 lakh rule may make a revised return enough."),
    sections=[
        ("/ Report it or not", "Look at where the money sits.",
         table(["Your account", "Schedule FA?"], [
             ["Account with a foreign provider holding a balance at any time in the calendar year (for example opened while you lived abroad, or a USD balance held with a foreign entity)", "Yes: foreign depository or custodial account, peak and closing balance, interest if any"],
             ["Service that only converts and pays into your Indian bank account, holding no foreign balance in your name", "Usually no foreign account to report; check the statement and the provider's terms"],
             ["Any of the above in a year you were NRI or RNOR", "No Schedule FA for that year"],
             ["Foreign shares or funds bought through the same app", "Yes, separately, as foreign equity"]])
         + BOX),
        ("/ What else applies", "Tax and FEMA, briefly.",
         ul("<strong>The income:</strong> freelance receipts are taxable as business or professional income (presumptive taxation under the 44ADA equivalent if you qualify), whether or not they reach India. See <a href=\"freelancer-consultant-tax-india-2026-complete.html\">freelancer and consultant tax in India</a>.",
            "<strong>FEMA:</strong> export of services proceeds have to be realised and repatriated within the time the RBI allows; a balance parked abroad indefinitely can raise a FEMA question. See <a href=\"fema-export-rules-1-october-2026-nine-month-realisation-edf-services.html\">the export realisation rules</a>.",
            "<strong>GST:</strong> exports of services are zero-rated under conditions, including receipt in convertible foreign exchange; registered freelancers need an LUT or pay IGST and claim a refund.",
            "<strong>Fees and exchange:</strong> keep the provider's statements; they support both the income figure and the Schedule FA peak balance."))
        ,
        ("/ If you missed it", "Your options before 31 December 2026.",
         ul("<strong>FAST-DS Category 2, INR 1 lakh:</strong> for a foreign account funded by income already taxed in India and missing from Schedule FA; immunity for what you declare, up to 2025-26.",
            "<strong>Revised return:</strong> corrects the FY 2025-26 return (free until 31 December 2026, with a fee until 31 March 2027). It does not reach earlier years.",
            "<strong>Untaxed receipts:</strong> payments that never made it into any return are undisclosed income: Category 1 at 60% within INR 1 crore, or an updated return where it is allowed.")
         + '<p>Compare: <a href="fast-ds-vs-revised-return-vs-updated-return-itr-u.html">FAST-DS vs revised return vs ITR-U</a> &middot; <a href="fast-ds-what-happens-if-i-do-not-declare-black-money-act.html">what happens if you do not declare</a> &middot; <a href="fast-ds-2026-calculator-foreign-asset-disclosure-cost.html">FAST-DS calculator</a>.</p>'
         f'<p><strong>Sources:</strong> Income-tax return instructions for Schedule FA; Finance Act, 2026, Chapter IV (FAST-DS); Black Money (Undisclosed Foreign Income and Assets) and Imposition of Tax Act, 2015, sections 42 and 43 as amended from 1 October 2024; RBI Master Direction on Export of Goods and Services. <em>{UPDATED}</em> General information, not advice for your situation.</p>'),
    ],
    faqs=[("Do I need to report my Wise or Payoneer account in Schedule FA?", "Yes, if you are resident and ordinarily resident and the account is held with a foreign provider and had a balance during the calendar year. Report the peak and closing balance. A service that only pays into your Indian bank account and holds no foreign balance usually leaves nothing to report."),
          ("I already show my freelance income. Is that not enough?", "No. The income goes in the income schedules; the foreign account itself goes in Schedule FA. They are separate requirements."),
          ("Does PayPal count?", "Only if a balance is held for you abroad. Where payments are converted and sent to your Indian bank account without a foreign balance, there is usually no foreign account to report. Check your statements."),
          ("Is FAST-DS worth INR 1 lakh for a small balance?", "Not always. If the income was taxed and your foreign assets other than property stayed within INR 20 lakh in total, the INR 10 lakh Black Money Act penalty does not apply, and a revised return with correct reporting going forward may be enough. Larger balances or several missed years usually favour FAST-DS."),
          ("What is the deadline?", "FAST-DS declarations close on 31 December 2026. The revised return for FY 2025-26 is free until 31 December 2026."),
          ("Can BQP sort this out for me?", "Yes. " + CONTACT)],
    related=[("freelancer-consultant-tax-india-2026-complete.html", "Freelancer and consultant tax in India"),
             ("fast-ds-vs-revised-return-vs-updated-return-itr-u.html", "FAST-DS vs revised return vs ITR-U"),
             ("fast-ds-2026-eligibility-checker.html", "FAST-DS eligibility checker")],
    cta_h="Foreign wallet missing from your return?", cta_b=CONTACT,
    keywords="Wise account Schedule FA, Payoneer Schedule FA, PayPal balance foreign asset India, Revolut account India tax, freelancer foreign account Schedule FA, FAST-DS freelancer, Wise USD balance India tax",
    desc="Freelancer resident in India with a Wise, Payoneer, PayPal or Revolut balance held abroad? When it goes in Schedule FA (peak and closing balance), when there is nothing to report, and whether FAST-DS (INR 1 lakh) or a revised return fits if you missed it.",
    howto={"name": "How to check if a foreign wallet goes in Schedule FA", "description": "Steps for a freelancer resident in India.", "steps": [
        {"name": "Check where the balance is held", "text": "A balance held with a foreign provider is a foreign account; a service that pays straight into your Indian bank usually is not."},
        {"name": "Check your residential status", "text": "Schedule FA applies only in years you are resident and ordinarily resident."},
        {"name": "Note the peak and closing balance", "text": "Take them from the provider's statements for the calendar year."},
        {"name": "Fix missed years", "text": "Use a revised return for FY 2025-26 or FAST-DS by 31 December 2026, depending on the amounts and years."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch BH complete")
