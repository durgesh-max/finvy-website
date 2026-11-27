# -*- coding: utf-8 -*-
"""Batch KC (27 Nov 2026): Do I need to report foreign assets in my ITR? Schedule FA - who must report, what to report,
the calendar-year period, the Black Money Act penalty, and fixing a missed disclosure before 31 December 2026.
Demand: sweep ac151 (27 Nov 2026), all 7 markets: "do i need to report foreign assets"; the site had FAST-DS pages and
asset-specific Schedule FA pages (RSU, US stocks, pensions, insurance, property, Wise / PayPal) but no general page on
who must fill Schedule FA.
User steer 26 Nov 2026: more call bookings / WhatsApp enquiries - Schedule FA omissions are fixed through a revised return
or FAST-DS before 31 December 2026, which people hand to a CA.
Facts (verified 27 Nov 2026): Schedule FA is filled only by individuals who are resident and ordinarily resident (ROR); NRIs
and RNORs do not fill it; it covers foreign assets held at any time during the calendar year ending 31 December of the
previous year (for AY 2026-27, 1 January to 31 December 2025); items: foreign bank and custodial accounts, equity and debt
interests (shares, ESOP / RSU), cash-value insurance and annuity contracts, financial interest in entities, immovable
property, other capital assets, trusts, accounts with signing authority, and foreign-source income; a resident holding a
foreign asset or with signing authority must file a return even below the basic exemption limit (proviso to section 139(1)
and the corresponding provision of the Income-tax Act, 2025); Black Money Act sections 42 / 43 penalty Rs 10 lakh for failure to
report, not applied (from 1 October 2024) where the aggregate value of foreign assets other than immovable property is up to
Rs 20 lakh; Schedule AL is separate and applies above Rs 1 crore total income; revised return for AY 2026-27 by 31 December
2026; FAST-DS 2026 closes 31 December 2026. No fees, no office claims, no statistics, no portal menu paths."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 27 November 2026."
SLUG = "do-i-need-to-report-foreign-assets-itr-schedule-fa-who-must-file-penalty-2026"

C = contact("a list of every foreign bank account, brokerage account, ESOP / RSU plan, insurance policy, pension and property you held at any time in the calendar year (with the country and an approximate peak balance), the dates you lived in India over the last ten years, your ITR acknowledgement for the year and any income tax email or notice about foreign assets")
PAGES = [dict(
    slug=SLUG,
    title="Do I Need to Report Foreign Assets in My ITR? Schedule FA (2026): Who Must Report, What to Include, Penalty and How to Fix a Missed Disclosure",
    em="residents must, even with no tax due.",
    kicker="/ Residents with foreign accounts, shares, RSUs or property &middot; Returning NRIs &middot; Updated 2026-11-27",
    lead=("<strong>Yes, if you are resident and ordinarily resident in India for the year: every foreign asset you held at any time in the calendar year goes in Schedule FA of your ITR, even if it earned nothing and even if your income is below the taxable limit.</strong> "
          "NRIs and RNORs do not fill Schedule FA. "
          "Leaving an asset out can attract a Rs 10 lakh penalty under the Black Money Act, so a missed disclosure for AY 2026-27 should be fixed through a revised return or FAST-DS 2026 before 31 December 2026."),
    sections=[
        ("/ Who must report", "Your residential status decides it.",
         table(["Status for the year", "Schedule FA?", "Why"], [
             ["Resident and ordinarily resident (ROR)", "Yes - every foreign asset", "Taxed on worldwide income, so foreign holdings must be disclosed"],
             ["Resident but not ordinarily resident (RNOR)", "No", "Usually the first two or so years after a long stay abroad"],
             ["Non-resident (NRI)", "No", "Only Indian income is reported"]])
         + ul("<strong>Returning NRIs:</strong> Schedule FA starts in the first year you become ROR - this is where most omissions happen.",
              "<strong>Even with no tax due:</strong> a resident who holds a foreign asset or has signing authority over a foreign account must file a return, even if income is below the basic exemption limit.",
              "<strong>Joint holders and signatories:</strong> each resident holder reports the account; a parent added to a child's foreign account reports it too.")),
        ("/ What to include", "More than bank accounts.",
         ul("<strong>Foreign bank and custodial accounts</strong> - savings, current, fixed deposits and brokerage accounts, including closed ones held at any time in the year.",
            "<strong>Shares and securities</strong> - US stocks bought from India, ESOPs and RSUs (vested and held), mutual funds and bonds.",
            "<strong>Cash-value insurance and annuities, pensions and retirement accounts</strong> - for example 401(k), IRA, UK pension, RRSP, superannuation.",
            "<strong>Immovable property abroad</strong> - a house or flat, even if it is let out or self-used.",
            "<strong>Financial interest in a foreign entity, trust interests and other capital assets.</strong>",
            "<strong>Accounts with only signing authority</strong> - for example an employer's or relative's account you can operate.",
            "<strong>Period:</strong> the calendar year ending 31 December before the assessment year (for AY 2026-27, 1 January to 31 December 2025), with values converted to rupees as the form's instructions require.")),
        ("/ If you missed it", "Fix it before 31 December 2026.",
         ul("<strong>Penalty:</strong> sections 42 and 43 of the Black Money Act provide for a Rs 10 lakh penalty for not reporting a foreign asset; from 1 October 2024 it does not apply where the total value of foreign assets other than immovable property is up to Rs 20 lakh.",
            "<strong>Revised return:</strong> for AY 2026-27, add Schedule FA (and any foreign income) in a revised return by 31 December 2026.",
            "<strong>Earlier years or larger amounts:</strong> FAST-DS 2026 closes on 31 December 2026 and covers assets left out of earlier returns, within its limits.",
            "<strong>Got an income tax email about foreign assets?</strong> It usually means foreign reporting data does not match your return - act on it before the deadline rather than ignoring it.",
            "<strong>Schedule AL is different:</strong> it lists all assets (Indian and foreign) and applies only above Rs 1 crore of total income.")
         + call_box("Foreign asset reporting", ["Residential status check (ROR / RNOR / NRI)",
                                                "Schedule FA preparation and rupee conversion",
                                                "Revised return by 31 December 2026",
                                                "FAST-DS 2026 declarations",
                                                "Replies to foreign-asset emails and notices"],
                    "A list of foreign holdings, your stay dates and your ITR acknowledgement.")
         + sources("Income-tax Act, 1961 (section 139(1) provisos, section 6 residential status) and the corresponding provisions of the Income-tax Act, 2025; ITR Schedule FA instructions; Black Money (Undisclosed Foreign Income and Assets) and Imposition of Tax Act, 2015, sections 42 and 43 as amended by the Finance (No. 2) Act, 2024; FAST-DS 2026; site FAST-DS, revised return and returning-NRI guides. Checked 27 November 2026.")),
    ],
    faqs=[("Do I need to report foreign assets in my ITR?", "Yes, if you are resident and ordinarily resident in India for the year. Every foreign asset held at any time in the calendar year - bank and brokerage accounts, shares, ESOPs and RSUs, insurance, pensions, property and accounts you can sign on - goes in Schedule FA, even if it earned no income and even if your income is below the taxable limit."),
          ("Do NRIs have to fill Schedule FA?", "No. Non-residents and residents who are not ordinarily resident (RNOR) do not fill Schedule FA. It starts in the first year you become resident and ordinarily resident, which for returning NRIs is often two or three years after moving back."),
          ("Which period does Schedule FA cover?", "The calendar year ending 31 December before the assessment year. For the return for AY 2026-27 (financial year 2025-26), that is 1 January to 31 December 2025. Assets held at any time in that period are reported, including accounts closed during the year."),
          ("What is the penalty for not reporting foreign assets?", "Sections 42 and 43 of the Black Money Act provide for a penalty of Rs 10 lakh for failing to report a foreign asset in the return. From 1 October 2024 the penalty does not apply where the total value of foreign assets other than immovable property is up to Rs 20 lakh. Undisclosed foreign income or assets can also be taxed under that Act, so omissions are best fixed before the department acts."),
          ("I forgot to add my foreign account in Schedule FA. What should I do?", "For AY 2026-27, file a revised return with Schedule FA and any foreign income by 31 December 2026. For earlier years, or where the asset was never declared, FAST-DS 2026 - open until 31 December 2026 - may be the route. WhatsApp +91 78018 87130 with the list of foreign accounts and holdings and your ITR acknowledgement, and we tell you which route fits."),
          ("Do I report a foreign account if it has only a small balance?", "Yes. Schedule FA has no minimum balance - every account held at any time in the calendar year is reported. The Rs 20 lakh relief only affects whether the Black Money Act penalty applies, not whether the asset has to be shown."),
          ("What should I send to get Schedule FA done?", "WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with " + "a list of every foreign bank account, brokerage account, ESOP / RSU plan, insurance policy, pension and property you held in the calendar year, the dates you lived in India over the last ten years, and your ITR acknowledgement. We confirm your residential status, prepare Schedule FA and file the revised return or FAST-DS declaration. You keep your own e-filing login.")],
    related=[("fast-ds-2026-foreign-asset-disclosure-scheme-31-december-deadline.html", "FAST-DS 2026 by 31 December"),
             ("revised-itr-section-139-5-deadline-31-december-2026-india.html", "Revised ITR by 31 December 2026"),
             ("fast-ds-what-happens-if-i-do-not-declare-black-money-act.html", "If you do not declare: Black Money Act"),
             ("nri-returning-india-tax-rnor-transition.html", "Returning NRI: RNOR and Schedule FA"),
             ("rsu-taxation-india-us-stocks-vesting-perquisite-capital-gains-schedule-fa-2026.html", "RSUs and US stocks in Schedule FA"),
             ("fast-ds-2026-supplementary-faqs-november-2026-20-lakh-bank-account-joint-accounts-one-fee-returning-nri.html", "FAST-DS November FAQs")],
    cta_h="Foreign assets to report?", cta_b=C,
    keywords="do i need to report foreign assets, schedule fa itr, who needs to fill schedule fa, foreign assets in itr, schedule fa penalty, schedule fa nri, schedule fa calendar year, forgot schedule fa, foreign bank account itr india",
    desc="Do you need to report foreign assets in your ITR? Schedule FA for residents (ROR) only - not NRIs or RNORs; calendar-year period; what to include; Rs 10 lakh Black Money Act penalty and the Rs 20 lakh relief; fixing a miss by 31 December 2026.",
    howto={"name": "How to fix a missed Schedule FA disclosure", "description": "From checking status to filing.", "steps": [
        {"name": "Check residential status", "text": "Schedule FA applies only if you were resident and ordinarily resident for the year."},
        {"name": "List every foreign asset", "text": "Accounts, shares, RSUs, insurance, pensions and property held at any time in the calendar year."},
        {"name": "Pick the route", "text": "Revised return for AY 2026-27, or FAST-DS 2026 for earlier years."},
        {"name": "File before 31 December 2026", "text": "Both the revised return and FAST-DS close on 31 December 2026."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch KC complete")
