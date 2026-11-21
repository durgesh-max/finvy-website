# -*- coding: utf-8 -*-
"""Batch FJ (21 Nov 2026): FAST-DS 2026 supplementary FAQs (Q51 to Q93), published 20-21 November 2026 - what they
settle. Call-first page. Clarity (21 Nov) shows the FAST-DS guides are the site's top landing pages.
Facts (checked 21 Nov 2026) from the FAQ text as reproduced by TaxGuru, "FAST-DS 2026 Supplementary FAQs Q51-Q93"
(21 Nov 2026), cross-checked with CalcGuru (21 Nov 2026), A2Z Taxcorp and CAclubindia reports of 43 supplementary FAQs:
- The FAQs call the 60% route Category A (undisclosed foreign income or asset, limit INR 1 crore: tax 30% + additional
  amount 30%) and the INR 1 lakh route Category B (asset from taxed income not shown in Schedule FA, limit INR 5 crore).
  Earlier pages on this site call them Category 1 and Category 2.
- Q51-Q54: declare only what was not offered to tax / not shown in Schedule FA; partial declaration is valid for what is
  declared; immunity only for that.
- Q55: USD conversion INR 94.6543 (RBI reference rate of 30 March 2026, none published on 31 March 2026).
- Q56-Q59: each joint holder reports separately; a holder named on the account is covered whoever funded it; value by
  ascertainable share, else equally; the INR 5 crore ceiling is tested for each declarant.
- Q60-Q61: directors, employees and authorised signatories: reporting follows the Black Money Act conditions.
- Q62: a person now non-resident who was resident when the account should have been reported is eligible.
- Q63: assets acquired while RNOR and not reported after becoming ordinarily resident go under Category B.
- Q64-Q65: concluded Black Money Act assessment or penalty proceedings are excluded; pending notices are not.
- Q66: Black Money Act: 30% tax + 90% penalty = 120%; FAST-DS Category A: 60%.
- Q67: foreign bank accounts with aggregate balance not above INR 20 lakh at any time in the year, deposits from
  disclosed sources: no declaration needed; needed where the account has undisclosed income or unaccounted deposits.
- Q69-Q72: an asset declared under A need not be declared again under B; mixed funding goes to A; both categories can
  be in one Form 1; income and the asset bought from it are not counted twice.
- Q73: fractional shares valued pro rata. Q74-Q75: declared assets not added to income in any assessment; confidential.
- Q76-Q78: 20% tolerance applies to values based on a recognised valuer's report, including immovable property; indexed
  cost, where used, is final.
- Q80: gifted or inherited asset: cost to the donor.
- Q82-Q83: single flat fee of INR 1 lakh for all Category B assets and all years.
- Q84-Q86: one consolidated Form 1; it can be refiled before Form 2 is issued; not after.
- Q87: no DTAA or foreign tax credit under Category A.
- Q88: a search or survey does not bar the scheme unless a Black Money Act assessment is complete or PMLA applies.
- Window closes 31 December 2026; no extension announced (reports of 20-21 Nov 2026)."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 21 November 2026."
SLUG = "fast-ds-2026-supplementary-faqs-november-2026-20-lakh-bank-account-joint-accounts-one-fee-returning-nri"

C = contact("the country where the assets are, what they are (bank account, shares, RSUs, property), rough values, the years you were resident in India and whether the money behind them was taxed")
PAGES = [dict(
    slug=SLUG,
    title="FAST-DS 2026 Supplementary FAQs (November 2026): Bank Accounts up to INR 20 Lakh, Joint Accounts, One INR 1 Lakh Fee and Returning NRIs",
    em="43 new answers, and what they change for you.",
    kicker="/ FAST-DS 2026 &middot; New FAQs &middot; Updated 2026-11-21",
    lead=("<strong>The Income Tax Department has published 43 more FAQs on FAST-DS 2026 (questions 51 to 93), reported on 20 and 21 November 2026.</strong> "
          "The headline points: foreign <strong>bank accounts that together never held more than INR 20 lakh</strong> in the year, funded only from taxed money, <strong>need no declaration</strong>. "
          "<strong>Each joint holder</strong> of a foreign account must declare for themselves, even if only one person put money in. "
          "The <strong>INR 1 lakh fee is paid once</strong>, for all eligible assets and all years. "
          "An asset bought partly from untaxed money goes under the <strong>60% route</strong>. "
          "People who are <strong>now non-resident</strong> can still declare what they should have reported while resident. "
          "<strong>The last date has not moved: 31 December 2026</strong>, and only one Form 1 can stand, so it has to be right."),
    sections=[
        ("/ What the new FAQs settle", "By question.",
         table(["Your situation", "What the FAQs say", "FAQ"], [
             ["Foreign bank accounts, total balance never above INR 20 lakh in the year, all deposits from taxed money", "No FAST-DS declaration needed. Report it in Schedule FA from now on", "Q67"],
             ["Same accounts, but they hold untaxed income or unexplained deposits", "Declaration needed", "Q67"],
             ["Joint account with a spouse or parent; only one of you funded it", "Each holder declares separately. Value is split by share, or equally if shares are not fixed", "Q56 to Q58"],
             ["Several assets missed for several years, all from taxed money", "One flat fee of INR 1 lakh covers all of them and all years, up to INR 5 crore", "Q82, Q83"],
             ["Asset bought partly from taxed and partly from untaxed money", "It cannot use the INR 1 lakh route; it goes under the 60% route", "Q70"],
             ["Some assets are from taxed money and some are not", "Both routes can be used in the same Form 1", "Q71"],
             ["You are non-resident now, but were resident when the account should have been reported", "You can still use the scheme", "Q62"],
             ["Assets acquired while RNOR, not reported after you became ordinarily resident", "INR 1 lakh route", "Q63"],
             ["You want to declare only some assets", "Allowed, but immunity covers only what you declare", "Q53, Q54"],
             ["Tax already paid abroad on the income", "No credit against the 60%", "Q87"],
             ["Mistake in Form 1", "File a fresh Form 1 before Form 2 is issued. After that, no", "Q84 to Q86"],
             ["Black Money Act notice received, assessment not finished", "The scheme is still open to you", "Q64"]])
         + '<p>The FAQs name the two routes <strong>Category A</strong> (60% of the value, up to INR 1 crore) and <strong>Category B</strong> (flat INR 1 lakh, up to INR 5 crore). Our earlier pages call the same routes Category 1 and Category 2.</p>'
         + call_box("FAST-DS before 31 December: which of these applies to me?", ["Whether you need to declare at all after the INR 20 lakh clarification",
                                                                                "Which route each asset falls under, and the amount payable",
                                                                                "Joint accounts: who declares what",
                                                                                "Valuation, including the dollar rate and property valuation reports",
                                                                                "Filing Form 1 once, correctly, and paying on time"],
                    "the country and type of each asset, rough values, the years you were resident in India and whether the money was taxed.")),
        ("/ Valuation and filing", "Details that affect the amount.",
         ul("<strong>Dollar rate:</strong> values in US dollars are converted at INR 94.6543, the RBI reference rate of 30 March 2026, because none was published on 31 March 2026 (Q55).",
            "<strong>Joint accounts and the INR 5 crore limit:</strong> the limit is tested separately for each person on their own Form 1 (Q59).",
            "<strong>Property and the 20% tolerance:</strong> if you use a recognised valuer&rsquo;s report and the tax officer later arrives at a value up to 20% higher, the declaration stays valid. If you use indexed cost instead, that figure is final (Q76 to Q78).",
            "<strong>Gifted or inherited assets:</strong> the cost is what the donor paid (Q80).",
            "<strong>Fractional shares:</strong> valued in proportion to a full share (Q73).",
            "<strong>No double counting:</strong> untaxed income and the asset bought with it are not both charged (Q72).",
            "<strong>One Form 1:</strong> all assets and income go in a single consolidated form. It can be refiled only until Form 2 is issued (Q84, Q86).",
            "<strong>Company accounts:</strong> a director, employee or authorised signatory may have to declare a company&rsquo;s foreign account where the Black Money Act reporting conditions are met (Q60, Q61).",
            "<strong>Search or survey:</strong> does not bar the scheme unless a Black Money Act assessment is already complete or money-laundering proceedings apply (Q88).",
            "<strong>Confidentiality:</strong> a declaration is treated like a tax return, and declared assets are not added to income in any assessment (Q74, Q75).")),
        ("/ What to do now", "The window closes on 31 December.",
         ul("<strong>List every foreign account, share, plan and property</strong> you held while resident in India, and check each against Schedule FA of your returns.",
            "<strong>For bank accounts,</strong> find the highest balance in each year and where the money came from. That decides between no declaration, the INR 1 lakh route and the 60% route.",
            "<strong>Joint holders</strong> should each plan their own Form 1.",
            "<strong>Order valuation reports early</strong> for property and unlisted shares.",
            "<strong>Compare with the alternatives</strong> where the 60% route applies: see <a href=\"fast-ds-vs-revised-return-vs-updated-return-itr-u.html\">FAST-DS vs revised or updated return</a> and <a href=\"fast-ds-2026-no-foreign-tax-credit-category-1-us-dividends-rsu-updated-return-comparison.html\">no foreign tax credit under the 60% route</a>.",
            "<strong>File well before 31 December 2026</strong> so there is time to correct Form 1 before Form 2 is issued.")
         + '<p>Related: <a href="fast-ds-2026-filing-help-chartered-accountant.html">FAST-DS filing help</a> &middot; <a href="fast-ds-2026-eligibility-checker.html">eligibility checker</a> &middot; <a href="fast-ds-2026-calculator-foreign-asset-disclosure-cost.html">cost calculator</a> &middot; <a href="fast-ds-2026-faq-full-form-last-date-eligibility-cost-form-1-nri-founders.html">20 quick answers</a> &middot; <a href="fast-ds-returning-nri-foreign-accounts-not-reported.html">returning NRIs</a> &middot; <a href="income-tax-email-foreign-assets-fast-ds-what-to-do.html">got an email about foreign assets?</a></p>'
         + sources("Income Tax Department, FAST-DS 2026 supplementary FAQs (Q51 to Q93), as reproduced by TaxGuru on 21 November 2026 and reported by CalcGuru, A2Z Taxcorp and CAclubindia; Finance Act, 2026, Chapter IV (sections 130 to 144); FAST-DS Rules, CBDT Notification No. 114/2026 of 14 August 2026; Black Money Act, 2015, sections 42 and 43. Checked 21 November 2026. Read the FAQ on the e-filing portal for your exact case; this page is general information.")),
    ],
    faqs=[("Do I need a FAST-DS declaration for a foreign bank account below INR 20 lakh?", "Not if the aggregate balance never exceeded INR 20 lakh at any time in the year and all deposits came from disclosed, taxed sources (supplementary FAQ 67). A declaration is needed if the account holds undisclosed income or unexplained deposits."),
          ("In a joint foreign account, who has to declare under FAST-DS?", "Each joint holder who was required to report the account declares separately, even if only one of them funded it. The value is split by ascertainable share, or equally where shares are not fixed (FAQs 56 to 58)."),
          ("Is the FAST-DS fee of INR 1 lakh charged per asset or per year?", "Neither. It is a single flat fee for all eligible assets and all years in one declaration, up to an aggregate value of INR 5 crore (FAQs 82 and 83)."),
          ("Can an NRI use FAST-DS?", "Yes, if the person was resident in India in the years when the foreign asset should have been reported. A person who has since become non-resident remains eligible (FAQ 62)."),
          ("What is the dollar conversion rate for FAST-DS?", "INR 94.6543 per US dollar, the RBI reference rate of 30 March 2026, since no rate was published on 31 March 2026 (FAQ 55)."),
          ("Can I correct Form 1 after filing?", "Yes, by filing a fresh Form 1 before Form 2 is issued. Once Form 2 has been issued accepting the declaration, another Form 1 cannot be filed (FAQs 84 to 86)."),
          ("Has the FAST-DS last date been extended?", "No. Declarations close on 31 December 2026 and no extension had been announced as of 21 November 2026."),
          ("Can BQP handle my FAST-DS declaration?", "Yes. " + C)],
    related=[("fast-ds-2026-filing-help-chartered-accountant.html", "FAST-DS filing help"),
             ("fast-ds-2026-eligibility-checker.html", "FAST-DS eligibility checker"),
             ("fast-ds-vs-revised-return-vs-updated-return-itr-u.html", "FAST-DS vs revised or updated return")],
    cta_h="Not sure whether you need to declare, or under which route?", cta_b=C,
    keywords="FAST-DS supplementary FAQs, FAST-DS 2026 FAQ November 2026, FAST-DS 20 lakh bank account, FAST-DS joint account, FAST-DS 1 lakh fee per asset, FAST-DS NRI eligible, FAST-DS dollar conversion rate 94.6543, FAST-DS Form 1 revise, FAST-DS last date 31 December 2026",
    desc="FAST-DS 2026 supplementary FAQs (Q51 to Q93, November 2026): no declaration for taxed foreign bank accounts up to INR 20 lakh; each joint holder declares; one INR 1 lakh fee for all assets and years; mixed funding goes to the 60% route; NRIs eligible; USD at 94.6543; closes 31 December 2026.",
    howto={"name": "How to act on the FAST-DS supplementary FAQs", "description": "Before 31 December 2026.", "steps": [
        {"name": "List foreign assets", "text": "Accounts, shares, plans and property held while resident."},
        {"name": "Check small bank accounts", "text": "Total balance never above INR 20 lakh and fully taxed money: no declaration."},
        {"name": "Sort the rest", "text": "Taxed money: INR 1 lakh route. Any untaxed money: 60% route."},
        {"name": "Value them", "text": "As on 31 March 2026; US dollars at INR 94.6543."},
        {"name": "File one Form 1", "text": "Well before 31 December 2026, then pay within the time in Form 2."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch FJ complete")
