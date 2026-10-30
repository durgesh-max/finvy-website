# -*- coding: utf-8 -*-
"""Batch AM: Round 24 - LLP Form 8 (no extension) and November 2026 compliance calendar."""
from build_lib import page, write_page

CONTACT = "Email durgesh@bharatquantumprospera.com or WhatsApp +91 78018 87130. Fixed-scope quote within 48 hours."


def ul(*items):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


def src(*pairs):
    return "<p><strong>Sources:</strong> " + "; ".join(f'<a href="{u}" rel="nofollow noopener" target="_blank">{t}</a>' for t, u in pairs) + ".</p>"


PAGES = [
    dict(
        slug="llp-form-8-due-30-october-2026-no-extension-late-fee",
        title="LLP Form 8 Due 30 October 2026: No Extension, and How the Late Fee Works",
        em="the company extension does not cover LLPs.",
        kicker="/ MCA &middot; LLP &middot; Updated 2026-10-30",
        lead="Every LLP must file Form 8, the Statement of Account and Solvency for FY 2025-26, by 30 October 2026. MCA General Circular 05/2026 of 24 October 2026 extended only company filings (AOC-4 to 31 December 2026 and MGT-7 to 31 January 2027); it does not cover LLP Form 8 or Form 11. Late filing attracts an additional fee that multiplies with the delay.",
        sections=[
            ("/ The two LLP annual forms", "What is due when.",
             "<table><thead><tr><th>Form</th><th>What it is</th><th>Due</th></tr></thead><tbody>"
             "<tr><td>Form 11</td><td>Annual return: partners, contributions, changes</td><td>30 May (within 60 days of year-end)</td></tr>"
             "<tr><td>Form 8</td><td>Statement of Account and Solvency</td><td>30 October (within 30 days of six months from year-end)</td></tr></tbody></table>"
             "<p>Form 8 is signed by two designated partners with digital signatures and certified by a practising chartered accountant, company secretary or cost accountant. There is no simplified Form 8 for small LLPs.</p>"),
            ("/ If you file late", "Additional fee, as a multiple of the normal fee.",
             "<table><thead><tr><th>Delay after 30 October</th><th>Small LLP</th><th>Other LLP</th></tr></thead><tbody>"
             "<tr><td>Up to 15 days</td><td>1x</td><td>1x</td></tr><tr><td>15 to 30 days</td><td>2x</td><td>4x</td></tr>"
             "<tr><td>30 to 60 days</td><td>4x</td><td>8x</td></tr><tr><td>60 to 90 days</td><td>6x</td><td>12x</td></tr>"
             "<tr><td>90 to 180 days</td><td>10x</td><td>20x</td></tr><tr><td>180 to 360 days</td><td>15x</td><td>30x</td></tr>"
             "<tr><td>Beyond 360 days</td><td>15x plus INR 10 a day</td><td>30x plus INR 20 a day</td></tr></tbody></table>"
             + ul("The normal fee depends on the LLP's contribution; the multiples apply on top of it (LLP Rules, 2009, as amended by G.S.R. 109(E) of 11 February 2022).",
                  "Separately, Section 34(5) of the LLP Act provides a penalty of INR 100 a day while the default continues, capped at INR 1 lakh for the LLP and INR 50,000 for each designated partner; small LLPs and start-up LLPs pay half.",
                  "Fees run only on the form that is late; a late Form 8 does not add fees to a Form 11 filed on time.")),
            ("/ Checklist for today", "If you are filing now.",
             ul("Signed financial statements for FY 2025-26 (audited if turnover exceeds INR 40 lakh or contribution exceeds INR 25 lakh).",
                "Solvency declaration by designated partners.",
                "Active DINs and valid DSCs for two designated partners; a deactivated DIN must be reactivated first.",
                "Certification by a practising CA, CS or CMA.") +
             src(("TaxAJ: LLP Form 8 FY 2025-26", "https://www.taxaj.com/learn/?p=90969"), ("CAclubindia: General Circular 05/2026", "https://www.caclubindia.com/articles/mca-general-circular-05-2026-additional-fee-relaxation-for-fy-2025-26-annual-filings-56490.asp")) +
             "<p><em>Last updated: 30 October 2026. Confirm fee amounts on the MCA portal before filing.</em></p>"),
        ],
        faqs=[
            ("What is the due date for LLP Form 8 for FY 2025-26?", "30 October 2026."),
            ("Has LLP Form 8 been extended in 2026?", "No. MCA General Circular 05/2026 of 24 October 2026 extended only company filings (AOC-4 and MGT-7). It does not cover LLP Form 8 or Form 11."),
            ("What is the late fee for LLP Form 8?", "An additional fee that is a multiple of the normal fee: 1x for up to 15 days, rising to 15x (small LLPs) or 30x (others) after 180 days, plus a per-day amount beyond 360 days. A separate penalty under Section 34(5) can also apply."),
            ("Who certifies LLP Form 8?", "A practising chartered accountant, company secretary or cost accountant, with two designated partners signing using digital signatures."),
            ("Can BQP file our LLP Form 8 and Form 11?", "Yes, including foreign-owned LLPs and overdue years. " + CONTACT),
        ],
        related=[("aoc-4-filing-deadline-30-october-2026-late-fee-india.html", "Companies: AOC-4 fee waiver to 31 December"), ("which-is-better-llp-vs-private-limited-india.html", "LLP vs Private Limited")],
        cta_h="LLP Form 8 due today?", cta_b=CONTACT,
        keywords="LLP Form 8 due date 2026, LLP Form 8 extension 2026, LLP Form 8 late fee, LLP Form 8 30 October 2026, LLP annual filing FY 2025-26, General Circular 05/2026 LLP",
        desc="LLP Form 8 (Statement of Account and Solvency) for FY 2025-26 is due 30 October 2026, with no extension: MCA General Circular 05/2026 covers only company AOC-4 and MGT-7. Late-fee multiples, Section 34(5) penalty and filing checklist.",
    ),
    dict(
        slug="november-2026-compliance-calendar-india-tax-gst-mca",
        title="November 2026 Compliance Calendar: Every Indian Tax, GST and MCA Deadline",
        em="for companies, NRIs, exporters and pensioners.",
        kicker="/ Calendar &middot; November 2026 &middot; Updated 2026-10-30",
        lead="The deadlines falling in November 2026, with the latest extensions applied: GST changes from 1 November, audit-case ITRs on 21 November, the MCA annual return (with the additional fee waived until 31 January 2027), the last date to claim FY 2025-26 GST input tax credit, and pensioners' life certificates by 30 November.",
        sections=[
            ("/ Date by date", "November 2026.",
             "<table><thead><tr><th>Date</th><th>What</th><th>Who</th></tr></thead><tbody>"
             "<tr><td>1 Nov</td><td>GST changes take effect: 90% provisional inverted-duty refunds, reverse charge and GST TDS on scrap and e-waste</td><td>GST-registered businesses</td></tr>"
             "<tr><td>1 Nov</td><td>Life certificate window opens for pensioners below 80 (80+ from 1 October)</td><td>Pensioners, including NRIs</td></tr>"
             "<tr><td>7 Nov</td><td>TDS and TCS deposit for October</td><td>All deductors</td></tr>"
             "<tr><td>11 Nov</td><td>GSTR-1 for October (monthly filers)</td><td>GST-registered businesses</td></tr>"
             "<tr><td>15 Nov</td><td>TDS certificates for July-September (non-salary)</td><td>Deductors</td></tr>"
             "<tr><td>20 Nov</td><td>GSTR-3B for October (monthly filers)</td><td>GST-registered businesses</td></tr>"
             "<tr><td>21 Nov</td><td>Income tax return for audit cases, AY 2026-27 (CBDT Circular 07/2026)</td><td>Companies, audited firms and individuals</td></tr>"
             "<tr><td>29 Nov</td><td>MGT-7 / MGT-7A annual return (additional fee waived if filed by 31 January 2027); PAS-6 for April-September</td><td>Companies</td></tr>"
             "<tr><td>30 Nov</td><td>ITR for transfer pricing cases; Master File (Form 3CEAA) where applicable</td><td>Companies with international group transactions</td></tr>"
             "<tr><td>30 Nov</td><td>Last date to claim FY 2025-26 GST input tax credit (or the GSTR-9 filing date, if earlier)</td><td>GST-registered businesses</td></tr>"
             "<tr><td>30 Nov</td><td>Life certificate deadline; pension may pause from December if not submitted</td><td>Pensioners</td></tr>"
             "<tr><td>30 Nov</td><td>UAE top-up tax registration for in-scope multinational groups</td><td>UAE entities of large groups</td></tr>"
             "</tbody></table>"),
            ("/ Already passed or extended", "So you do not panic.",
             ul("AOC-4 (FY 2025-26): due 30 October, but the additional fee is waived if filed by 31 December 2026 (MCA General Circular 05/2026).",
                "LLP Form 8: due 30 October 2026, no extension.",
                "Form 3CEB and MSME Form I: due 31 October 2026.",
                "DIR-3 KYC: no longer annual; once every three years by 30 June.")),
            ("/ Coming in December", "Plan now.",
             ul("15 December: third advance tax instalment (75%).",
                "31 December: belated and revised ITRs for FY 2025-26; FAST-DS foreign asset disclosure; GSTR-9/9C for FY 2025-26; AOC-4 fee waiver ends.") +
             src(("CAclubindia: General Circular 05/2026", "https://www.caclubindia.com/articles/mca-general-circular-05-2026-additional-fee-relaxation-for-fy-2025-26-annual-filings-56490.asp"),
                 ("India Briefing: CBDT Circular 07/2026", "https://www.india-briefing.com/news/india-cbdt-extends-itr-due-date-tax-audit-cases-ay-2026-27-47142.html/"),
                 ("Business Today: Jeevan Pramaan 2026", "https://www.businesstoday.in/personal-finance/story/jeevan-pramaan-2026-who-can-submit-digital-life-certificate-from-october-1-and-who-must-wait-559868-2026-10-07")) +
             "<p><em>Last updated: 30 October 2026. Quarterly GST filers and TDS form names under the Income-tax Act, 2025 have their own schedules; check the portals for your case.</em></p>"),
        ],
        faqs=[
            ("What are the main compliance deadlines in November 2026?", "21 November: ITR for audit cases. 29 November: MGT-7/MGT-7A and PAS-6. 30 November: ITR for transfer pricing cases, last date to claim FY 2025-26 GST input tax credit, and pensioners' life certificates. GST changes from the 57th GST Council take effect on 1 November."),
            ("Is the MGT-7 deadline extended?", "The due date stays 29 November 2026, but MCA General Circular 05/2026 waives the additional fee for FY 2025-26 returns filed by 31 January 2027."),
            ("What is the last date to claim GST input tax credit for FY 2025-26?", "30 November 2026, or the date you file the FY 2025-26 annual return if that is earlier."),
            ("When must pensioners submit the life certificate in 2026?", "By 30 November 2026. Pensioners aged 80 and above could submit from 1 October; others from 1 November."),
            ("Can BQP handle November filings?", "Yes: ITRs, MGT-7, GST and transfer pricing filings, for Indian and foreign-owned companies and NRIs. " + CONTACT),
        ],
        related=[("india-tax-nri-cross-border-news-october-2026.html", "October 2026 news roundup"), ("india-tax-compliance-calendar-fy-2026-27-complete.html", "Full FY 2026-27 compliance calendar")],
        cta_h="Too many November deadlines?", cta_b=CONTACT,
        keywords="November 2026 compliance calendar, tax due dates November 2026 India, GST due dates November 2026, MGT-7 due date 2026, ITC claim last date FY 2025-26, life certificate November 2026",
        desc="November 2026 compliance calendar for India: GST changes from 1 November, TDS and GST returns, audit-case ITR on 21 November, MGT-7 (fee waived to 31 January 2027), FY 2025-26 ITC claim and life certificates by 30 November.",
    ),
]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"],
                hero_kicker=p["kicker"], hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>',
                hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]],
                cta_headline=p["cta_h"], cta_body=p["cta_b"])
    write_page(p["slug"], html)
print(f"Batch AM complete: {len(PAGES)} pages")
