# -*- coding: utf-8 -*-
"""Batch AX: MTD for Income Tax quarterly update deadlines 2026-27 (next due 7 November 2026), for UK practices."""
from build_lib import page, write_page

CONTACT = "Email durgesh@bharatquantumprospera.com or WhatsApp +91 78018 87130. Fixed-scope quote within 48 hours."
SLUG = "mtd-income-tax-quarterly-update-7-november-2026-deadlines-uk-practices"

TABLE = ("<table><thead><tr><th>Quarterly period (2026-27)</th><th>Update due</th></tr></thead><tbody>"
         "<tr><td>6 April to 5 July 2026</td><td>7 August 2026</td></tr>"
         "<tr><td>6 July to 5 October 2026</td><td><strong>7 November 2026</strong></td></tr>"
         "<tr><td>6 October 2026 to 5 January 2027</td><td>7 February 2027</td></tr>"
         "<tr><td>6 January to 5 April 2027</td><td>7 May 2027</td></tr>"
         "<tr><td>Tax return for 2026-27</td><td>31 January 2028</td></tr></tbody></table>")


def ul(*items):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


sections = [
    ("/ The deadlines", "Standard quarterly periods.", TABLE),
    ("/ Penalties in the first year", "What is relaxed and what is not.",
     ul("For 2026-27, HMRC will not issue penalty points for late quarterly updates from the first MTD for Income Tax cohort.",
        "The easement does not cover the 2026-27 tax return or late payment of tax.",
        "Taxpayers who join from 6 April 2027 (qualifying income above GBP 30,000) get no such easement; their first quarterly update is due 7 August 2027.",
        "Under the points regime, four points trigger a GBP 200 penalty, and each further missed deadline while at the threshold adds another GBP 200.")),
    ("/ Who is in scope", "And who joins next.",
     ul("From 6 April 2026: sole traders and landlords with qualifying income (self-employment plus property) above GBP 50,000 in 2024-25.",
        "From 6 April 2027: above GBP 30,000 (tested on 2025-26). From 6 April 2028: above GBP 20,000.",
        "Partnerships are not yet in scope.")),
    ("/ For UK practices", "Four deadlines a year per client.",
     ul("Quarterly updates turn one annual job into five touchpoints per client: four updates and the tax return.",
        "Routine work (bank feeds, categorising transactions, preparing the quarterly summary in MTD-compatible software) can be handled offshore, leaving your team to review, advise and submit as agent.",
        "Plan now for the April 2027 cohort, which is larger and has no penalty easement.") +
     '<p>See <a href="outsourced-accounting-bookkeeping-for-uk-accountancy-practices-india.html">outsourced accounting for UK practices</a> and the <a href="uk-accountants-outsourcing-to-india-gdpr-idta-checklist.html">UK GDPR outsourcing checklist</a>.</p>'
     '<p><strong>Sources:</strong> <a href="https://www.xero.com/uk/guides/mtd-for-income-tax-penalties/" rel="nofollow noopener" target="_blank">Xero: MTD for Income Tax penalties</a>; '
     '<a href="https://www.taxassist.co.uk/ayr/resources/articles/making-tax-digital-for-income-tax-how-to-make-a-quarterly-update/amp" rel="nofollow noopener" target="_blank">TaxAssist: quarterly updates</a>; '
     '<a href="https://www.gov.uk/government/news/one-year-until-making-tax-digital-for-income-tax-launches" rel="nofollow noopener" target="_blank">GOV.UK: MTD for Income Tax</a>.</p>'
     "<p><em>Last updated: 2 November 2026. Some clients may use different update periods; check HMRC's guidance and your software for each client's obligations.</em></p>"),
]

faqs = [
    ("When is the next MTD for Income Tax quarterly update due?", "7 November 2026, for the period 6 July to 5 October 2026. The following updates are due on 7 February and 7 May 2027."),
    ("Are there penalties for a late MTD quarterly update in 2026-27?", "No penalty points are issued for late quarterly updates in 2026-27 for the first cohort. Late tax returns and late payments are still penalised."),
    ("Who has to use MTD for Income Tax from April 2027?", "Sole traders and landlords with qualifying income above GBP 30,000 in 2025-26."),
    ("How many points trigger an MTD penalty?", "Four points for quarterly filers, leading to a GBP 200 penalty, with GBP 200 more for each further missed deadline at the threshold."),
    ("Can BQP prepare MTD quarterly updates for our clients?", "Yes: bookkeeping and quarterly summaries in your MTD software, for your review and submission. " + CONTACT),
]

html = page(slug=SLUG,
            title="MTD for Income Tax: Quarterly Update Due 7 November 2026, All 2026-27 Deadlines",
            description="Making Tax Digital for Income Tax 2026-27: quarterly updates due 7 August and 7 November 2026, 7 February and 7 May 2027, return by 31 January 2028. No penalty points for late quarterly updates in 2026-27; the April 2027 cohort (above GBP 30,000) gets no easement.",
            keywords="MTD income tax 7 November 2026, MTD ITSA quarterly update deadlines, MTD quarterly update due dates 2026-27, MTD penalty points first year, making tax digital income tax deadlines, MTD April 2027 30000",
            hero_kicker="/ UK &middot; Making Tax Digital &middot; Updated 2026-11-02",
            hero_title_html="MTD for Income Tax: quarterly update due 7 November 2026, <em>and every 2026-27 deadline.</em>",
            hero_lead="Sole traders and landlords in the first Making Tax Digital for Income Tax cohort must send their second quarterly update, for 6 July to 5 October 2026, by 7 November 2026. HMRC will not issue penalty points for late quarterly updates in 2026-27, but the easement does not cover the tax return or payments, and it does not extend to the larger cohort joining in April 2027.",
            sections=sections, faqs=faqs,
            related=[("outsourced-accounting-bookkeeping-for-uk-accountancy-practices-india.html", "Related", "Outsourcing for UK practices"),
                     ("indian-ca-for-clients-in-uk.html", "Related", "Indian CA for clients in the UK")],
            cta_headline="MTD workload piling up?", cta_body=CONTACT)
write_page(SLUG, html)
print("Batch AX complete")
