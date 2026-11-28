# -*- coding: utf-8 -*-
"""Batch HU (25 Nov 2026): RNOR status (resident but not ordinarily resident) - the tests in section 6(6) (same in the
1961 and 2025 Acts per site pages): non-resident in 9 of the 10 preceding years, or 729 days or less in India in the 7
preceding years; also residents under the 120-day rule with Indian income above Rs 15 lakh and deemed residents; how many
years it lasts (depends on history, commonly one to three); what is taxed; no Schedule FA; planning for returning NRIs.
Demand: sweep ac102 (25 Nov 2026), all 7 markets: "rnor status for 3 years", "rnor status for how many years", "rnor status
income tax".
Facts (checked 25 Nov 2026) from settled section 6 law and site pages: expat / H-1B / returning NRI pages (RNOR commonly
one to three years; RNOR taxed on Indian income; foreign income not taxed unless received in India or from a business
controlled or profession set up in India; no Schedule FA while RNOR; section 6 tests identical in both Acts; deemed
resident page)."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 25 November 2026."
SLUG = "rnor-status-india-how-many-years-conditions-729-days-9-of-10-years-returning-nri-tax-2026"

C = contact("the date you returned (or plan to), your days in India in each of the last ten years, your residential status in those years, and your foreign income and assets")
L = lambda h, t: f'<a href="{h}">{t}</a>'
PAGES = [dict(
    slug=SLUG,
    title="RNOR (Resident but Not Ordinarily Resident) Status in India (2026): Conditions, How Many Years It Lasts, What Is Taxed and Planning for Returning NRIs",
    em="the window when foreign income stays outside Indian tax.",
    kicker="/ Returning NRIs and expats &middot; Residential status &middot; Updated 2026-11-25",
    lead=("<strong>RNOR (resident but not ordinarily resident) is a middle residential status for people who become resident in India after years abroad.</strong> "
          "You are RNOR in a year in which you are resident if you were a non-resident in at least 9 of the 10 preceding years, or you spent 729 days or less in India in the 7 preceding years; some residents under the 120-day rule and deemed residents are also RNOR. "
          "An RNOR is taxed on Indian income, but foreign income is generally not taxed unless it is received in India or comes from a business controlled or a profession set up in India. "
          "There is no fixed number of years: returning NRIs commonly get one to three years, depending on their history."),
    sections=[
        ("/ Quick answers", "What returning NRIs search for.",
         ul("<strong>How many years does RNOR status last?</strong> It is tested every year. Most returning NRIs qualify for one to three years; long-term NRIs often get three, because the 729-days-in-7-years test keeps passing until enough days in India accumulate.",
            "<strong>Is RNOR status for 3 years fixed?</strong> No. There is no automatic three-year period; each year is tested on the preceding 10 and 7 years.",
            "<strong>What is taxed when I am RNOR?</strong> Indian income (salary for work in India, rent, interest, capital gains on Indian assets), and foreign income only if received in India or from a business controlled or profession set up in India.",
            "<strong>Do I file Schedule FA as RNOR?</strong> No. Foreign assets go in Schedule FA only once you are resident and ordinarily resident (ROR).",
            "<strong>Can an NRI who visits India a lot still be RNOR?</strong> Possibly, but frequent long visits use up the 729-day allowance and can make you ROR sooner.",
            "<strong>Which section?</strong> Section 6 of the Income-tax Act, 1961, carried into section 6 of the Income-tax Act, 2025 with the same tests.")),
        ("/ The tests", "Step 1: are you resident? Step 2: are you RNOR?",
         table(["Question", "Rule"], [
             ["Resident this year?", "182 days or more in India, or 60 days plus 365 days in the preceding 4 years (the 60 days becomes 120 for citizens or PIOs visiting India with Indian income above &#8377;15 lakh; 182 for those on a visit with lower income or leaving for work)"],
             ["RNOR route 1", "Non-resident in 9 out of the 10 preceding years"],
             ["RNOR route 2", "In India for 729 days or less in the 7 preceding years"],
             ["RNOR route 3", "Citizen or PIO resident only under the 120-day rule (Indian income above &#8377;15 lakh)"],
             ["RNOR route 4", "Deemed resident: Indian citizen with Indian income above &#8377;15 lakh who is not liable to tax in any country"],
             ["Otherwise", "Resident and ordinarily resident: taxed on worldwide income, Schedule FA applies"]])
         + '<p>Deemed residence is explained in ' + L("dubai-uae-nri-indian-income-above-15-lakh-deemed-resident-india-tax-2026.html", "deemed resident for Gulf NRIs") + '.</p>'),
        ("/ Using the RNOR years well", "Planning for returning NRIs.",
         ul("<strong>Foreign salary and interest:</strong> keep foreign income received abroad during RNOR years.",
            "<strong>Retirement accounts:</strong> consider the Form 40 option for a 401(k), IRA, UK pension or super before you become ROR; see " + L("form-40-foreign-retirement-account-401k-ira-uk-pension-rrsp-super-defer-tax-india.html", "Form 40 for foreign retirement accounts") + ".",
            "<strong>Bank accounts:</strong> re-designate NRE / NRO accounts and consider an RFC account; see " + L("nri-nre-nro-conversion-returning-india-2026.html", "NRE and NRO conversion on return") + ".",
            "<strong>Selling foreign assets:</strong> timing gains in RNOR years can keep them outside Indian tax, subject to the tax in the other country.",
            "<strong>Foreign assets disclosure:</strong> plan the first ROR year&rsquo;s Schedule FA; see " + L("fast-ds-returning-nri-foreign-accounts-not-reported.html", "foreign accounts for returning NRIs") + ".",
            "<strong>US returnees:</strong> see " + L("h1b-holders-returning-to-india-tax-rnor-401k-2026.html", "H-1B holders returning to India") + ".")
         + call_box("RNOR planning for returning NRIs", ["Residential status year by year",
                                                         "Foreign income during RNOR years",
                                                         "401(k), IRA, pension and Form 40",
                                                         "Bank account re-designation",
                                                         "Schedule FA in the first ROR year"],
                    "your return date and ten-year travel history.")
         + sources("Income-tax Act, 1961, section 6(1), 6(1A) and 6(6); Income-tax Act, 2025, section 6 (same tests, per the site's section mapping); site pages on expat tax, H-1B returnees, deemed residence and foreign retirement accounts. Residential status depends on exact days; confirm with your travel records. Checked 25 November 2026.")),
    ],
    faqs=[("What is RNOR status in India?", "Resident but not ordinarily resident: a resident who was a non-resident in 9 of the 10 preceding years or spent 729 days or less in India in the 7 preceding years, plus some residents under the 120-day rule and deemed residents. An RNOR is taxed on Indian income but generally not on foreign income."),
          ("What does resident but not ordinarily resident mean?", "Resident but not ordinarily resident (RNOR) is a residential status under section 6(6) of the Income-tax Act. You are resident for the year, but not ordinarily resident if you were non-resident in 9 of the 10 preceding years or in India for 729 days or less in the 7 preceding years. Indian citizens and persons of Indian origin treated as resident under the 120-day rule for Indian income above INR 15 lakh, and deemed residents, are also RNOR. An RNOR is taxed in India on Indian income and on foreign income only if it comes from a business controlled or a profession set up in India."),
          ("How many years does RNOR status last?", "There is no fixed period; it is tested every year. Returning NRIs commonly qualify for one to three years, depending on how many years they were non-resident and how many days they spent in India."),
          ("Is foreign income taxed in India for an RNOR?", "Generally no, unless it is received in India or comes from a business controlled or a profession set up in India. Indian income is taxed as for any resident."),
          ("Does an RNOR have to report foreign assets in Schedule FA?", "No. Schedule FA applies only to residents who are ordinarily resident, so the first ROR year is when foreign assets must be reported."),
          ("Which section defines RNOR status?", "Section 6(6) of the Income-tax Act, 1961, and section 6 of the Income-tax Act, 2025, which applies the same tests."),
          ("Can BQP plan my RNOR years?", "Yes. CA Durgesh Chavda can work out your status year by year and plan foreign income, retirement accounts, bank accounts and Schedule FA. " + C)],
    related=[("h1b-holders-returning-to-india-tax-rnor-401k-2026.html", "H-1B holders returning to India"),
             ("form-40-foreign-retirement-account-401k-ira-uk-pension-rrsp-super-defer-tax-india.html", "Form 40 for 401(k) and pensions"),
             ("nri-nre-nro-conversion-returning-india-2026.html", "NRE / NRO conversion on return"),
             ("expat-tax-india-foreign-employee-residency-rnor-salary-pf-dtaa-2026.html", "Expat tax and residency"),
             ("dubai-uae-nri-indian-income-above-15-lakh-deemed-resident-india-tax-2026.html", "Deemed resident rule")],
    cta_h="Moving back to India?", cta_b=C,
    keywords="RNOR status, RNOR status for 3 years, RNOR status how many years, RNOR status income tax, resident but not ordinarily resident, returning NRI tax, 729 days rule, 9 out of 10 years non resident, RNOR Schedule FA",
    desc="RNOR status in India (2026): resident but not ordinarily resident if NRI in 9 of 10 years or 729 days or less in 7 years (plus 120-day and deemed residents); lasts one to three years typically; foreign income not taxed; no Schedule FA.",
    howto={"name": "How to check your RNOR status", "description": "For each tax year after you return.", "steps": [
        {"name": "Count days in India this year", "text": "To see whether you are resident at all."},
        {"name": "List the last 10 years' status", "text": "Non-resident in 9 of 10 years means RNOR."},
        {"name": "Count days in the last 7 years", "text": "729 days or less means RNOR."},
        {"name": "Check the 120-day and deemed rules", "text": "These residents are also RNOR."},
        {"name": "Plan income and accounts", "text": "Keep foreign income abroad; prepare for the first ROR year."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch HU complete")
