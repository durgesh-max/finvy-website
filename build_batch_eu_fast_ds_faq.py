# -*- coding: utf-8 -*-
"""Batch EU (21 Nov 2026): FAST-DS 2026 FAQ - one page answering the questions people search (full form, start date, last
date, who can file, cost, forms, payment, NRIs, founders with foreign company shares, crypto, what if above the limits).
Demand: sweep 21 Nov 2026 (ac33), all 7 markets: "fast ds 2026 scheme faq", "fast ds scheme full form", "fast ds 2026
scheme start date", "fast ds scheme form 1", "fast ds for nri", "fast ds eligibility", "fast ds 2026 scheme details".
Clarity (first night of data, 20-21 Nov 2026): the FAST-DS filing-help page was the top landing page, from Google.
Facts: taken only from the site's existing, already-verified FAST-DS pages (main scheme page checked 13 Nov 2026;
filing-help, payment, above-limits, returning-NRI, do-not-declare pages): Foreign Assets of Small Taxpayers Disclosure
Scheme, 2026 (Finance Act, 2026, sections 131-140); window 16 August to 31 December 2026 for Form 1; values as on
31 March 2026; Category 1 - 30% tax plus equal amount = 60%, aggregate up to INR 1 crore; Category 2 - flat INR 1 lakh,
aggregate foreign assets up to INR 5 crore; Form 2 order, pay by challan ITNS 289 within two months from the end of the
month of receipt, or two more months with 1% simple interest a month; Form 3 intimation; Form 4 certificate; no refund
(section 138); immunity for years up to 2025-26 (section 139); current NRIs can file if resident when the income arose
or asset was acquired (section 131(1)(a)(ii)); RNOR years outside Schedule FA; Black Money Act outside the scheme: 30%
tax, penalty three times the tax, INR 10 lakh non-disclosure penalty (not for non-immovable assets up to INR 20 lakh in
aggregate), prosecution; updated return cannot be used only to add an asset. New, hedged items: founders' shares in
a foreign company follow the same category logic; crypto on a foreign exchange is fact-specific."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 21 November 2026."
SLUG = "fast-ds-2026-faq-full-form-last-date-eligibility-cost-form-1-nri-founders"

C = contact("a short note of your foreign accounts, shares or property, their approximate values, and the years you were resident in India")
FAQS = [
    ("What is the full form of FAST-DS?", "Foreign Assets of Small Taxpayers Disclosure Scheme, 2026. It is a one-time scheme in the Finance Act, 2026 that lets small taxpayers declare foreign income or assets missed in their Indian returns and get immunity under the Black Money Act."),
    ("When did FAST-DS 2026 start and what is the last date?", "Declarations opened on 16 August 2026 and close on 31 December 2026. That date is for filing the declaration in Form 1; payment comes later, after the Department's order in Form 2."),
    ("Who can file under FAST-DS 2026?", "People who were resident in India when foreign income arose or a foreign asset was acquired, and who did not report it: returning students and professionals, employees with foreign shares or RSUs, former NRIs with overseas accounts, and current NRIs for the years they were resident."),
    ("How much does FAST-DS cost?", "Category 1, for foreign income never taxed in India or assets bought from it: 30% tax plus an equal amount, 60% in total, where the aggregate is up to INR 1 crore. Category 2, for foreign assets bought from taxed income or while non-resident but missing from the foreign-assets schedule: a flat INR 1 lakh, where the aggregate value is up to INR 5 crore."),
    ("How are foreign assets valued under FAST-DS?", "At fair market value as on 31 March 2026. The INR 1 crore and INR 5 crore limits apply to the aggregate, so assets cannot be split to stay under a limit."),
    ("What are Form 1, Form 2, Form 3 and Form 4 under FAST-DS?", "Form 1 is your declaration, due by 31 December 2026. Form 2 is the Department's order of the amount payable. Form 3 is your intimation of payment with proof. Form 4 is the certificate issued after the payment is verified."),
    ("When and how is the FAST-DS amount paid?", "Through challan ITNS 289 on the e-Filing portal, within two months from the end of the month in which you receive Form 2, or within two further months with simple interest of 1% a month."),
    ("Is the amount paid under FAST-DS refundable?", "No. The scheme says no amount paid is refundable, and the portal warns that a wrong ITNS 289 payment cannot be corrected, so check the category and amount before filing and paying."),
    ("What immunity does FAST-DS give?", "A valid declaration with payment gives immunity from further tax, penalty and prosecution under the Black Money Act for the declared income or asset, for years up to 2025-26. The declared amount is not taxed again."),
    ("Can an NRI file FAST-DS?", "Yes, if he or she was resident in India in the year the income arose or the asset was acquired. Assets built while non-resident and missed after returning are usually Category 2."),
    ("Do I need FAST-DS for RNOR years?", "Generally no. The foreign-assets schedule applies to residents who are ordinarily resident, so years in which you were resident but not ordinarily resident are generally outside it."),
    ("I hold RSUs or shares of my US employer. Which category?", "Shares taxed through Indian payroll but missing from the foreign-assets schedule are usually Category 2. Dividends or sale gains that were never taxed in India are Category 1."),
    ("I am a founder with shares in my own US or other foreign company. Do I need FAST-DS?", "Shares in a foreign company belong in the foreign-assets schedule of a resident's return. If they were bought with taxed money and only the reporting was missed, the logic of Category 2 applies; income from the company that was never taxed in India is Category 1. Valuing unlisted shares as on 31 March 2026 is the difficult part, so get it reviewed."),
    ("Does FAST-DS cover crypto held abroad?", "The scheme covers foreign assets and foreign income. Whether crypto counts as a foreign asset depends on where the account or wallet is held, and crypto gains have their own tax rules, so the category needs checking on your facts."),
    ("What if my foreign assets are above the FAST-DS limits?", "The scheme cannot be used above INR 1 crore for Category 1 or INR 5 crore for Category 2. The options are a revised return for FY 2025-26, updated returns for earlier years where additional income is involved, documenting the source of funds and reporting correctly from now on."),
    ("Can I just file an updated return instead of FAST-DS?", "Not to add an asset. An updated return must report additional income and increase tax; it cannot be used only to add a foreign asset to the schedule, and it is barred after certain notices."),
    ("What happens if I do not declare by 31 December 2026?", "Undisclosed foreign income or assets found later fall under the Black Money Act: 30% tax, a penalty of three times that tax, a separate INR 10 lakh penalty for non-disclosure where the threshold is crossed, and possible prosecution."),
    ("Is there a penalty for a small foreign bank account?", "The INR 10 lakh non-disclosure penalty does not apply where the aggregate value of foreign assets other than immovable property is INR 20 lakh or less. Tax on any undisclosed income still applies."),
    ("I received an email from the Income Tax Department about foreign assets. What should I do?", "Check the assets listed against your returns for each year you were resident, work out whether Category 1 or Category 2 applies, and file Form 1 before 31 December 2026 if a declaration is needed."),
    ("Can BQP file my FAST-DS declaration?", "Yes. " + C),
]
PAGES = [dict(
    slug=SLUG,
    title="FAST-DS 2026 FAQ: 20 Questions Answered - Full Form, Last Date 31 December 2026, Who Can File, Cost, Form 1 to Form 4, NRIs and Founders",
    em="short answers before the window closes.",
    kicker="/ FAST-DS 2026 &middot; FAQ &middot; Closes 31 December 2026 &middot; Updated 2026-11-21",
    lead=("<strong>FAST-DS</strong> stands for the <strong>Foreign Assets of Small Taxpayers Disclosure Scheme, 2026</strong>. It lets a person who was resident in India declare foreign income or assets left out of Indian returns and get immunity under the Black Money Act. "
          "The window opened on <strong>16 August 2026</strong> and the declaration (Form 1) must be filed by <strong>31 December 2026</strong>. "
          "<strong>Category 1</strong> costs <strong>60%</strong> (30% tax plus an equal amount) for untaxed foreign income or assets up to INR 1 crore in total. <strong>Category 2</strong> costs a flat <strong>INR 1 lakh</strong> for foreign assets bought from taxed income, or while non-resident, that were only missing from the return, up to INR 5 crore in total. "
          "Assets are valued as on 31 March 2026, the amount paid is not refundable, and current NRIs can file for the years they were resident. The questions people ask most are answered below."),
    sections=[
        ("/ Key facts", "FAST-DS 2026 in one table.",
         table(["Point", "Answer"], [
             ["Full form", "Foreign Assets of Small Taxpayers Disclosure Scheme, 2026"],
             ["Window", "16 August 2026 to 31 December 2026 (Form 1)"],
             ["Category 1", "Untaxed foreign income or assets: 60% of the value, aggregate up to INR 1 crore"],
             ["Category 2", "Taxed or non-resident-era assets not reported: flat INR 1 lakh, aggregate up to INR 5 crore"],
             ["Valuation date", "31 March 2026, fair market value"],
             ["Forms", "Form 1 declaration; Form 2 order; Form 3 payment intimation; Form 4 certificate"],
             ["Payment", "Challan ITNS 289, within two months from the end of the month of Form 2; two more months with 1% a month interest"],
             ["Immunity", "From further tax, penalty and prosecution under the Black Money Act for what is declared, for years up to 2025-26"],
             ["Refund", "None"]])
         + call_box("My FAST-DS declaration", ["Whether you need to declare at all, year by year",
                                             "Category 1 or Category 2 for each account, share or property",
                                             "Valuation as on 31 March 2026",
                                             "Filing Form 1 before 31 December and handling Form 2 to Form 4",
                                             "Fixing the foreign-assets schedule in future returns"],
                    "a list of foreign accounts, shares, retirement plans or property, and the years you lived in India.")),
        ("/ Tools and detailed guides", "Go deeper on your case.",
         ul("<a href=\"fast-ds-2026-eligibility-checker.html\">Eligibility checker</a> and <a href=\"fast-ds-2026-calculator-foreign-asset-disclosure-cost.html\">cost calculator</a>",
            "<a href=\"fast-ds-2026-filing-help-chartered-accountant.html\">Getting it filed by a chartered accountant</a>",
            "<a href=\"fast-ds-rsu-espp-us-shares-401k-which-category.html\">RSUs, ESPP shares and 401(k)</a> &middot; <a href=\"us-stocks-bought-from-india-not-in-schedule-fa-fast-ds-vested-indmoney.html\">US stocks bought from India</a>",
            "<a href=\"fast-ds-returning-nri-foreign-accounts-not-reported.html\">Returning NRIs</a> &middot; <a href=\"fast-ds-uk-pension-isa-canada-rrsp-australia-super-schedule-fa.html\">UK, Canada and Australia retirement accounts</a>",
            "<a href=\"fast-ds-payment-due-date-interest-calculator-itns-289-form-3-form-4.html\">Payment dates, ITNS 289, Form 3 and Form 4</a>",
            "<a href=\"fast-ds-not-eligible-above-1-crore-5-crore-limit-what-are-the-options.html\">Above the limits</a> &middot; <a href=\"fast-ds-vs-revised-return-vs-updated-return-itr-u.html\">FAST-DS vs revised or updated return</a>",
            "<a href=\"income-tax-email-foreign-assets-fast-ds-what-to-do.html\">The Department's email about foreign assets</a> &middot; <a href=\"fast-ds-what-happens-if-i-do-not-declare-black-money-act.html\">if you do not declare</a>")
         + sources("Finance Act, 2026 (Foreign Assets of Small Taxpayers Disclosure Scheme, 2026, sections 131 to 140), the scheme rules and forms, the e-Filing portal's FAST-DS pages and official FAQ, and the Black Money (Undisclosed Foreign Income and Assets) and Imposition of Tax Act, 2015, as set out in the detailed guides linked above. Check your own facts before filing; the amount paid is not refundable.")),
    ],
    faqs=FAQS,
    related=[("fast-ds-2026-foreign-asset-disclosure-scheme-31-december-deadline.html", "FAST-DS 2026 explained"),
             ("fast-ds-2026-eligibility-checker.html", "FAST-DS eligibility checker"),
             ("fast-ds-2026-filing-help-chartered-accountant.html", "FAST-DS filing help")],
    cta_h="Foreign assets missing from your Indian return?", cta_b=C,
    keywords="FAST-DS 2026 FAQ, FAST-DS full form, FAST-DS last date 31 December 2026, FAST-DS scheme start date, FAST-DS Form 1, FAST-DS eligibility, FAST-DS for NRI, FAST-DS Category 1 Category 2, FAST-DS founders foreign company shares",
    desc="FAST-DS 2026 FAQ: full form (Foreign Assets of Small Taxpayers Disclosure Scheme), window 16 August to 31 December 2026, Category 1 at 60% up to INR 1 crore, Category 2 flat INR 1 lakh up to INR 5 crore, Forms 1 to 4, ITNS 289, NRIs, RSUs, founders and crypto.")]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"])
    write_page(p["slug"], html)
print("Batch EU complete")
