# -*- coding: utf-8 -*-
"""Batch EY (21 Nov 2026): REPLACES budget-2027-india-startup-founder-preparation.html and turns two mislabelled October
pages into redirects to it:
  budget-2026-expectations-startups-nri-foreign-companies.html
  pre-budget-2026-startup-foreign-company-actions-window.html
Why: the October pages called the February 2027 Budget 'Budget 2026', said a 'Direct Tax Code 2026' might replace the
Income-tax Act 1961 (the Income-tax Act, 2025 has applied since 1 April 2026), floated an extension of section 115BAB
(closed) and said the DPDP Rules were still awaited (notified 13 November 2025). They read as forecasts.
This page makes no forecasts. It states where the law stands today, from facts already verified on this site:
Income-tax Act, 2025 from 1 April 2026; companies 25.168% under 115BAA, 115BAB closed; LTCG 12.5% without indexation,
resident individuals / HUFs may choose 20% with indexation on land or buildings bought before 23 July 2024; angel tax
abolished from FY 2024-25; buybacks taxed as capital gains from 1 April 2026; TCS on LRS nil / 2% / 20% above INR 10
lakh; RBI INR 50 lakh LRS sub-limit proposal not notified; India has not enacted Pillar Two; DPDP main duties about
13 May 2027; deemed residence at Indian income above INR 15 lakh; year-end deadlines 31 December 2026 (belated / revised
ITR, FAST-DS, GSTR-9). The Union Budget is by convention presented on 1 February."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 21 November 2026."
SLUG = "budget-2027-india-startup-founder-preparation"
REDIRECTS = ["budget-2026-expectations-startups-nri-foreign-companies", "pre-budget-2026-startup-foreign-company-actions-window"]

C = contact("whether you are an NRI, a founder or a foreign company, any sale, buyback, remittance or restructuring you plan before 31 March 2027, and your country of residence")
PAGES = [dict(
    slug=SLUG,
    title="Union Budget 2027 (1 February 2027): What NRIs, Founders and Foreign Companies Should Do Before It - Where the Law Stands Today",
    em="no forecasts: the current rules and a sensible checklist.",
    kicker="/ Budget 2027 &middot; Planning &middot; NRIs, founders, foreign companies &middot; Updated 2026-11-21",
    lead=("The <strong>Union Budget for FY 2027-28</strong> is expected on <strong>1 February 2027</strong>. Nobody outside the government knows what it will contain, and this page does not guess. "
          "What helps is knowing <strong>where the law stands today</strong>, so that you can judge any change on the day, and finishing the things that have fixed deadlines before then. "
          "The main baselines are these. The <strong>Income-tax Act, 2025</strong> has applied since 1 April 2026. Companies pay <strong>25.17%</strong>. Long-term capital gains are taxed at <strong>12.5%</strong>. Buybacks are taxed as capital gains. Remittances above INR 10 lakh carry <strong>TCS</strong> of up to 20%. India has <strong>not enacted the global minimum tax</strong>. "
          "Changes announced in a Budget usually apply from 1 April, but some apply from Budget day or midnight, so if you already plan a sale, buyback or large remittance, decide the timing deliberately. Do not rush a transaction on a rumour."),
    sections=[
        ("/ Where the law stands today", "Read the Budget against these.",
         table(["Area", "Current position (November 2026)", "Guide"], [
             ["Income-tax law", "Income-tax Act, 2025 applies from 1 April 2026; old section and form numbers have changed", "<a href=\"old-vs-new-income-tax-form-numbers-2026-15ca-145-15cb-146-10f-41.html\">old vs new form numbers</a>"],
             ["Company tax", "25.168% for companies under the concessional regime; the 15% rate for new manufacturers is closed to new entrants", "<a href=\"branch-vs-subsidiary-india-tax-calculator-foreign-company-35-percent-vs-25-percent-dividend-treaty-2026.html\">branch vs subsidiary calculator</a>"],
             ["Capital gains", "Long-term gains 12.5% without indexation; resident individuals and HUFs may choose 20% with indexation on land or buildings bought before 23 July 2024; NRIs cannot", "<a href=\"is-nri-eligible-87a-rebate-indexation-nps-ppf-scss-sukanya-post-office-schemes-2026.html\">NRI eligibility</a>"],
             ["Share issues and buybacks", "Angel tax abolished from FY 2024-25; buyback proceeds taxed as capital gains from 1 April 2026", "<a href=\"get-capital-back-from-indian-subsidiary-dividend-buyback-capital-reduction-tax-2026.html\">getting capital back</a>"],
             ["Money sent abroad", "TCS nil on loan-funded education, 2% on self-funded education, 20% above INR 10 lakh for other purposes; an RBI sub-limit of INR 50 lakh has been reported but not notified", "<a href=\"rbi-lrs-50-lakh-sub-limit-proposal-2026-overseas-remittance-what-it-means.html\">LRS proposal</a>"],
             ["Global minimum tax", "India has not enacted Pillar Two; a domestic top-up tax could be introduced in a Budget", "<a href=\"beps-pillar-2-india-implementation-october-2026-update.html\">Pillar Two in India</a>"],
             ["NRI residence", "Day-count tests, with deemed residence where Indian income exceeds INR 15 lakh and no tax is paid elsewhere", "<a href=\"residential-status-calculator-india-nri-rnor-section-6.html\">residential status calculator</a>"]])
         + call_box("Planning before Budget 2027", ["Transactions you already plan before 31 March 2027 and their tax today",
                                                    "Whether timing before or after 1 February matters for you",
                                                    "Year-end deadlines still open: belated return, FAST-DS, GSTR-9",
                                                    "Documents and certificates to get in place now",
                                                    "A review after the Budget of what actually changed"],
                    "a short note of the planned transaction, amounts and dates, and your residential status.")),
        ("/ What to do before 1 February 2027", "A checklist that holds whatever the Budget says.",
         ul("<strong>Close the fixed deadlines first:</strong> belated or revised return, FAST-DS declaration and GSTR-9 by 31 December 2026; see the <a href=\"deadline-desk-20-november-2026-to-31-january-2027-income-tax-gst-roc-nri-foreign-companies.html\">deadline desk</a>.",
            "<strong>Property or share sales already planned:</strong> work out today&rsquo;s tax, apply early for a lower deduction certificate if you are an NRI, and choose the completion date knowingly.",
            "<strong>Buybacks, dividends and restructurings:</strong> board approvals, valuations and filings take weeks; start now if you want the choice of completing before the Budget.",
            "<strong>Large remittances:</strong> use the right purpose code and remember TCS is creditable; see <a href=\"tcs-20-foreign-remittance-lrs-india-2026.html\">TCS on foreign remittances</a>.",
            "<strong>Foreign companies:</strong> keep transfer pricing, FEMA filings and payroll current, so a Budget change is the only new item on your list; see the <a href=\"foreign-owned-indian-subsidiary-annual-compliance-calendar-fy-2026-27.html\">compliance calendar</a>.",
            "<strong>On Budget day:</strong> check the effective date of each change before acting. We will publish what changed for NRIs, founders and foreign companies.")
         + sources("Positions stated are those in force in November 2026 as set out in the linked guides (Income-tax Act, 2025; Finance Acts 2024 to 2026; RBI and CBDT material cited there). The Union Budget is by convention presented on 1 February; the date and contents are for the government to announce. This page replaces two earlier pre-Budget pages that contained forecasts and outdated statements.")),
    ],
    faqs=[("When is Union Budget 2027?", "By convention the Union Budget is presented on 1 February, so the Budget for FY 2027-28 is expected on 1 February 2027. The government announces the date."),
          ("What will Budget 2027 change for NRIs and startups?", "Nobody outside the government knows before Budget day. It is more useful to know the current rules, such as the 12.5% long-term capital gains rate, TCS on remittances and the residence tests, and to judge any change against them."),
          ("Should I sell property or shares before the Budget?", "Only if the sale makes sense anyway. Budget changes usually apply from 1 April, but some apply from Budget day, so decide the timing deliberately and do not rush on rumours."),
          ("Has India replaced the Income-tax Act, 1961?", "Yes. The Income-tax Act, 2025 has applied since 1 April 2026, with new section and form numbers."),
          ("Is the global minimum tax in force in India?", "No. India has not enacted Pillar Two. A domestic top-up tax could be introduced in a future Budget."),
          ("Can BQP review my position before and after the Budget?", "Yes. " + C)],
    related=[("deadline-desk-20-november-2026-to-31-january-2027-income-tax-gst-roc-nri-foreign-companies.html", "Deadline desk to 31 January 2027"),
             ("nri-year-end-tax-checklist-before-31-december-2026-refund-belated-itr-fast-ds-residency.html", "NRI year-end checklist"),
             ("india-tax-nri-cross-border-news-november-2026.html", "November 2026 news roundup")],
    cta_h="Planning a transaction before 31 March 2027?", cta_b=C,
    keywords="Union Budget 2027 date, Budget 2027 NRI, Budget 2027 startups, pre-Budget planning India 2027, Budget 2027 capital gains, Budget 2027 foreign companies India",
    desc="Union Budget 2027 is expected on 1 February 2027. No forecasts here: where Indian tax law stands today (Income-tax Act 2025, 25.17% company tax, 12.5% LTCG, buyback and TCS rules, no Pillar Two) and a checklist for NRIs, founders and foreign companies before it.",
    howto={"name": "How to prepare for Union Budget 2027", "description": "Steps that hold whatever the Budget contains.", "steps": [
        {"name": "Finish fixed deadlines", "text": "Belated return, FAST-DS and GSTR-9 by 31 December 2026."},
        {"name": "List planned transactions", "text": "Sales, buybacks, remittances and restructurings before 31 March 2027."},
        {"name": "Work out today's tax", "text": "Know the cost under the current rules."},
        {"name": "Prepare documents early", "text": "Valuations, approvals and lower deduction certificates."},
        {"name": "Check effective dates on Budget day", "text": "Act only after reading when each change applies."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)

for old in REDIRECTS:
    with open(old + ".html", "w", encoding="utf-8", newline="") as fh:
        fh.write(f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Union Budget 2027: What to Do Before It - BQP</title>
<link rel="canonical" href="https://bharatquantumprospera.com/{SLUG}.html">
<meta name="robots" content="noindex, follow">
<meta http-equiv="refresh" content="0; url={SLUG}.html">
</head><body><p>This page has been replaced by <a href="{SLUG}.html">Union Budget 2027: what NRIs, founders and foreign companies should do before it</a>.</p></body></html>
""")
print("Batch EY complete: 1 page rewritten,", len(REDIRECTS), "redirects")
