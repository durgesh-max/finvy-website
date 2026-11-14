# -*- coding: utf-8 -*-
"""Batch AU: November 2026 news roundup (add items to NEWS_ITEMS and re-run this file during November)."""
from build_lib import page, write_page

CONTACT = "Email durgesh@bharatquantumprospera.com or WhatsApp +91 78018 87130. Fixed-scope quote within 48 hours."
LEAD = "CA Durgesh Chavda, Bharat Quantum Prospera"
UPDATED = "14 November 2026"
SLUG = "india-tax-nri-cross-border-news-november-2026"


def ul(*items):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


# (date, title, text, our page, (source name, source url)) - newest first
NEWS_ITEMS = [
    ("14 Nov 2026", "Foreign digital companies: significant economic presence under the new Income-tax Act",
     "With the equalisation levy gone (2% ended 1 August 2024, 6% ended 1 April 2025), Indian revenue of foreign SaaS, app and ad businesses is tested under section 9 of the Income-tax Act, 2025: payments from India above INR 2 crore or 3 lakh users in India create a business connection. Treaty-country companies with a TRC and Form 10F (Form 41) and no PE are usually protected.",
     "significant-economic-presence-foreign-saas-app-company-india-2-crore-3-lakh-users-2026.html",
     ("Accorp Partners", "https://accorppartners.com/blogs/india-incorporation/equalisation-levy-and-significant-economic-presence-when-a-foreign-company-owes-indian-tax-without-any-india-entity")),
    ("13 Nov 2026", "FEMA: where to file compounding for ODI, overseas loans and guarantees",
     "RBI A.P. (DIR Series) Circular No. 28/2026-27 (23 October 2026) moved compounding of overseas investment, borrowing/lending and guarantee contraventions to seven Regional Offices. Overseas investment cases go by the foreign entity's UIN prefix; cases with no UIN, or mixed categories, stay with CEFA at the Central Office in Mumbai. Procedure and computation are unchanged.",
     "fema-compounding-odi-rbi-regional-office-uin-circular-28-october-2026.html",
     ("TaxGuru", "https://taxguru.in/rbi/fema-compounding-overseas-investments-loans-guarantees-delegated-regional-offices-rbi.html")),
    ("13 Nov 2026", "Company law: GIFT IFSC direct listing opened to equity instruments and loss-making companies",
     "G.S.R. 968(E) dated 3 November 2026 amends the listing rules for permissible jurisdictions: equity instruments including convertible debentures and preference shares, unlisted public companies in the IFSC, negative net worth companies with at least 75% of the net offer to QIBs, and offers for sale by eligible existing holders.",
     "direct-listing-gift-ifsc-indian-company-equity-instruments-amendment-november-2026.html",
     ("TaxGuru", "https://taxguru.in/company-law/mca-expands-ifsc-listing-rules-equity-instruments-2026.html")),
    ("11 Nov 2026", "FAST-DS: Income Tax Department nudging owners of undisclosed UAE property",
     "Business Standard reported on 26 October 2026, citing Finance Ministry sources, that the department has begun selectively contacting taxpayers who may hold undisclosed UAE residential or commercial property, with about 1,100 FAST-DS declarations filed so far. Regional committees under Principal Chief Commissioners handle queries. Declarations close on 31 December 2026.",
     "dubai-uae-property-not-disclosed-india-income-tax-nudge-fast-ds-2026.html",
     ("Business Standard", "https://www.business-standard.com/finance/news/i-t-dept-nudges-uae-property-owners-as-fast-ds-gets-1-100-declarations-126102601405_1.html")),
    ("10 Nov 2026", "Income tax: revised returns for FY 2025-26 can be filed until 31 March 2027",
     "The Finance Act, 2026 extended the Section 139(5) window from nine to twelve months. Revising until 31 December 2026 stays free; a revision from 1 January to 31 March 2027 attracts a fee under section 234-I of INR 1,000 or INR 5,000 depending on total income. Belated returns are still due by 31 December 2026.",
     "revised-itr-section-139-5-deadline-31-december-2026-india.html",
     ("LiveLaw", "https://www.livelawbiz.com/top-stories/budget-2026-proposes-12-month-window-from-assessment-year-end-to-file-revised-income-tax-returns-521417")),
    ("7 Nov 2026", "UK: second MTD for Income Tax quarterly update due",
     "Sole traders and landlords in the first Making Tax Digital for Income Tax cohort send their update for 6 July to 5 October 2026 by 7 November. No penalty points for late quarterly updates in 2026-27, but returns and payments are still penalised.",
     "mtd-income-tax-quarterly-update-7-november-2026-deadlines-uk-practices.html",
     ("Xero", "https://www.xero.com/uk/guides/mtd-for-income-tax-penalties/")),
    ("1 Nov 2026", "GST: post-supply discounts, faster inverted-duty refunds, no INR 1,000 export refund floor",
     "Notification 03/2026-Central Tax (26 October 2026) brings Sections 153 to 155 of the Finance Act, 2026 into force from today. Discounts given after a supply can be adjusted through a credit note (Sections 15(3)(b) and 34(1)), 90% of inverted-duty refund claims can be paid provisionally (Section 54(6)), and the INR 1,000 minimum no longer applies to refunds on goods exported with payment of tax.",
     "gst-changes-from-1-november-2026-57th-gst-council-cbic-circulars.html",
     ("TaxGuru", "https://taxguru.in/goods-and-service-tax/gst-post-supply-discount-refund-amendments-effective-1-november-2026.html")),
]

news_rows = "".join(
    f'<li><strong>{d}: {t}</strong><br>{x} <a href="{h}">Read more</a> &middot; <a href="{su}" rel="nofollow noopener" target="_blank">Source: {sn}</a></li>'
    for d, t, x, h, (sn, su) in NEWS_ITEMS)

sections = [
    ("/ This month's changes", "Newest first.", "<ul>" + news_rows + "</ul>"),
    ("/ Deadlines this month and next", "Put these in the calendar.",
     ul("4 November 2026: comments to SEBI on the SME IPO consultation paper.",
        "7 November 2026 (UK): second MTD for Income Tax quarterly update.",
        "15 November 2026: TDS certificates (Form 131) for July-September 2026.",
        "21 November 2026: ITR for audit cases, AY 2026-27.",
        "29 November 2026: MGT-7/MGT-7A annual return (additional fee waived until 31 January 2027).",
        "30 November 2026: ITR for transfer pricing cases; last date to claim FY 2025-26 GST input tax credit; pensioners' life certificates.",
        "15 December 2026: third advance tax instalment.",
        "31 December 2026: belated and revised ITRs for FY 2025-26; FAST-DS foreign asset declarations.") +
     '<p>Full list: <a href="november-2026-compliance-calendar-india-tax-gst-mca.html">November 2026 compliance calendar</a>. Last month: <a href="india-tax-nri-cross-border-news-october-2026.html">October 2026 roundup</a>.</p>'
     f"<p><em>Last updated: {UPDATED}.</em></p>"),
    ("/ Already in force", "Changes from earlier in 2026 that still catch people out.",
     ul('<a href="income-tax-act-2025-section-mapping-old-vs-new-54-is-82-80c-is-123-nri.html">Income-tax Act, 2025 section numbers</a> and <a href="old-vs-new-income-tax-form-numbers-2026-15ca-145-15cb-146-10f-41.html">new form numbers</a> (15CA is now Form 145).',
        '<a href="buying-property-from-nri-no-tan-form-141-from-1-october-2026.html">No TAN needed to buy property from an NRI</a> from 1 October 2026.',
        '<a href="fema-export-rules-1-october-2026-nine-month-realisation-edf-services.html">FEMA export rules</a>: nine months to realise export proceeds.',
        '<a href="press-note-2-2026-fdi-land-border-countries-china-10-percent-60-day-approval.html">Press Note 2 (2026)</a> on investment with China or other land-border links.')),
]

faqs = [
    ("What GST changes apply from 1 November 2026?", "Sections 153 to 155 of the Finance Act, 2026, notified by Notification 03/2026-Central Tax: post-supply discounts through credit notes, 90% provisional refunds for inverted duty structure claims, and removal of the INR 1,000 minimum for refunds on goods exported with payment of tax."),
    ("What are the key tax deadlines in November 2026?", "15 November for TDS certificates, 21 November for audit-case ITRs, 29 November for MGT-7, and 30 November for transfer pricing ITRs, the FY 2025-26 GST input tax credit cut-off and pensioners' life certificates."),
    ("Who can help me act on these changes?", f"{LEAD} advises NRIs, Indian founders and foreign companies. " + CONTACT),
]

html = page(slug=SLUG,
            title="India Tax, NRI and Cross-Border News: November 2026 Roundup",
            description="November 2026 India tax and NRI news: GST post-supply discounts and 90% provisional refunds from 1 November (Notification 03/2026-CT), audit-case ITR due 21 November, transfer pricing ITR and GST ITC cut-off 30 November, FAST-DS by 31 December.",
            keywords="India tax news November 2026, NRI news November 2026, GST changes 1 November 2026, Notification 03/2026 Central Tax, India compliance November 2026",
            hero_kicker=f"/ News &middot; Roundup &middot; Updated {UPDATED}",
            hero_title_html="India Tax, NRI and Cross-Border News: November 2026, <em>what changed and what to do.</em>",
            hero_lead=f"The tax and regulatory changes this month that matter to NRIs, Indian founders and foreign companies with Indian operations, each with the action to take. Compiled by {LEAD} and updated through the month.",
            sections=sections, faqs=faqs,
            related=[("india-tax-nri-cross-border-news-october-2026.html", "Related", "October 2026 roundup"),
                     ("november-2026-compliance-calendar-india-tax-gst-mca.html", "Related", "November 2026 compliance calendar")],
            cta_headline="Not sure which change affects you?", cta_body=CONTACT)
write_page(SLUG, html)
print("November roundup built")
