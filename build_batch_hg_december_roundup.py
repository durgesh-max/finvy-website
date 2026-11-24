# -*- coding: utf-8 -*-
"""Batch HG: December 2026 news roundup (published 25 November with the month's scheduled changes and deadlines;
add items to the 'Newest first' list during December with scratchpad/roundup_add.py pointed at this page).
Facts are drawn from existing, sourced site pages (deadline desk 20 Nov 2026 to 31 Jan 2027, advance tax Q3, belated
ITR, revised ITR, GSTR-9 FY 2025-26, AOC-4 fee waiver, MGT-7 waiver, EPFO Vishwas, SEBI digital KYC, FAST-DS)."""
from build_lib import page, write_page

CONTACT = "Email info@bharatquantumprospera.com or WhatsApp +91 78018 87130. Fixed-scope quote within 48 hours."
LEAD = "CA Durgesh Chavda, Bharat Quantum Prospera"
UPDATED = "25 November 2026"
SLUG = "india-tax-nri-cross-border-news-december-2026"


def ul(*items):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


# (date, title, text, our page) - scheduled changes first; news added during December, newest first
ITEMS = [
    ("From 3 Dec 2026", "SEBI: NRIs and OCIs can complete market KYC from abroad",
     "Under a SEBI circular dated 4 November 2026, intermediaries can accept digital KYC and re-KYC from NRIs, OCIs and foreign nationals in FATF-compliant countries without a visit to India, using video verification, from 3 December 2026.",
     "nri-oci-demat-trading-account-digital-kyc-from-abroad-sebi-3-december-2026.html"),
    ("Scheduled", "Year-end window for NRIs: refunds, belated returns and FAST-DS",
     "December is the last month to file a belated return for FY 2025-26, to revise a return without a fee, and to make a FAST-DS declaration of undisclosed foreign assets; NRIs visiting India for the holidays should also check baggage, cash and gift rules.",
     "nri-year-end-tax-checklist-before-31-december-2026-refund-belated-itr-fast-ds-residency.html"),
]
rows = "".join(f'<li><strong>{d}: {t}</strong><br>{x} <a href="{h}">Read more</a></li>' for d, t, x, h in ITEMS)

sections = [
    ("/ This month's changes", "Newest first.", "<ul>" + rows + "</ul>"),
    ("/ Deadlines this month and next", "Put these in the calendar.",
     ul('15 December 2026: third advance tax instalment, 75% of the year&rsquo;s tax (<a href="advance-tax-q3-december-15-2026-india.html">guide</a>).',
        '28 December 2026: last date under the EPFO Vishwas scheme for PF damages settlement (<a href="epfo-vishwas-2026-pf-damages-settlement-reduced-rates-last-date-28-december-2026.html">guide</a>).',
        '31 December 2026: belated ITR for FY 2025-26 (<a href="belated-itr-31-december-2026-section-139-4-india.html">guide</a>); last date to revise a return without the new fee (<a href="revised-itr-section-139-5-deadline-31-december-2026-india.html">guide</a>).',
        '31 December 2026: GSTR-9 and GSTR-9C for FY 2025-26 (<a href="gstr-9-gstr-9c-fy-2025-26-mandatory-optional-tables-notification-05-2026-due-31-december-2026.html">guide</a>).',
        '31 December 2026: AOC-4 additional fee waiver ends (<a href="aoc-4-filing-deadline-30-october-2026-late-fee-india.html">guide</a>); FAST-DS foreign asset declarations close.',
        '31 January 2027: MGT-7/MGT-7A additional fee waiver ends; TDS statements for October-December 2026 in Forms 138, 140 and 144.') +
     '<p>Full list: <a href="deadline-desk-20-november-2026-to-31-january-2027-income-tax-gst-roc-nri-foreign-companies.html">deadline desk, 20 November 2026 to 31 January 2027</a>. Last month: <a href="india-tax-nri-cross-border-news-november-2026.html">November 2026 roundup</a>.</p>'
     f"<p><em>Last updated: {UPDATED}. Updated through December as changes are notified.</em></p>"),
    ("/ Already in force", "Changes from earlier in 2026 that still catch people out.",
     ul('<a href="income-tax-act-2025-section-mapping-old-vs-new-54-is-82-80c-is-123-nri.html">Income-tax Act, 2025 section numbers</a> and <a href="old-vs-new-income-tax-form-numbers-2026-15ca-145-15cb-146-10f-41.html">new form numbers</a>.',
        '<a href="itr-due-date-21-november-2026-audit-cases-cbdt-circular-07-2026.html">Audit-case ITR deadline moved to 21 November</a> (CBDT Circular 07/2026).',
        '<a href="gst-changes-from-1-november-2026-57th-gst-council-cbic-circulars.html">GST changes from 1 November 2026</a>: post-supply discounts and faster refunds.',
        '<a href="what-is-dtaa.html">India&rsquo;s tax treaties, country by country</a>, including the <a href="india-france-dtaa-2026-amending-protocol-dividend-5-15-capital-gains-mfn-removed-rates.html">India-France protocol</a>.')),
]

faqs = [
    ("What are the key India tax deadlines in December 2026?", "15 December for the third advance tax instalment, 28 December for the EPFO Vishwas scheme, and 31 December for belated and fee-free revised ITRs for FY 2025-26, GSTR-9 and GSTR-9C for FY 2025-26, the AOC-4 additional fee waiver and FAST-DS declarations."),
    ("What changes for NRIs in December 2026?", "From 3 December 2026, NRIs and OCIs in FATF-compliant countries can complete market KYC and re-KYC digitally from abroad under a SEBI circular, and 31 December is the last date for belated returns and FAST-DS declarations."),
    ("Who can help me act on these changes?", f"{LEAD} advises NRIs, Indian founders and foreign companies. " + CONTACT),
]

html = page(slug=SLUG,
            title="India Tax, NRI and Cross-Border News: December 2026 Roundup",
            description="December 2026 India tax and NRI news and deadlines: SEBI digital KYC for NRIs from 3 December, advance tax 15 December, EPFO Vishwas 28 December, belated and revised ITRs, GSTR-9/9C, AOC-4 waiver and FAST-DS by 31 December.",
            keywords="India tax news December 2026, NRI news December 2026, India tax deadlines December 2026, advance tax 15 December 2026, belated ITR 31 December 2026, GSTR-9 31 December 2026",
            hero_kicker=f"/ News &middot; Roundup &middot; Updated {UPDATED}",
            hero_title_html="India Tax, NRI and Cross-Border News: December 2026, <em>what changes and what is due.</em>",
            hero_lead=f"The tax and regulatory changes and deadlines this month that matter to NRIs, Indian founders and foreign companies with Indian operations, each with the action to take. Compiled by {LEAD} and updated through the month.",
            sections=sections, faqs=faqs,
            related=[("india-tax-nri-cross-border-news-november-2026.html", "Related", "November 2026 roundup"),
                     ("deadline-desk-20-november-2026-to-31-january-2027-income-tax-gst-roc-nri-foreign-companies.html", "Related", "Deadline desk to 31 January 2027")],
            cta_headline="Not sure which change affects you?", cta_body=CONTACT)
write_page(SLUG, html)
print("December roundup built")
