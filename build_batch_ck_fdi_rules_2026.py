# -*- coding: utf-8 -*-
"""Batch CK (14 Nov 2026): "FDI rules in India" pillar (sweep-2 demand: "new fdi rules in india", "fdi rules and
regulations in india", "fdi laws in india", "fdi in india rules", seen in all 7 markets).
Facts: FDI governed by FEMA (Non-debt Instruments) Rules, 2019 and DPIIT's Consolidated FDI Policy; automatic route
(no prior approval) for most sectors, government route for specified sectors and for any investment from countries
sharing a land border; prohibited sectors include lottery, gambling and betting, chit funds, Nidhi companies, trading in
TDRs, real estate business and farmhouses, and manufacture of tobacco cigarettes. Press Note 2 (2026) revised the
land-border framework (beneficial ownership, tiered approvals, reporting route for some cases), followed by the NDI
(Amendment) Rules, 2026 of 1 May 2026 and a DPIIT SOP of 4 May 2026. RBI released the draft Foreign Exchange Management
(Foreign Investment) Rules, 2026 in July 2026 to replace the NDI Rules, comments to 31 August 2026; DPIIT continues to
interpret FDI policy. Reporting: shares allotted within 60 days of receiving funds; Form FC-GPR within 30 days of
allotment; FC-TRS within 60 days of receipt of consideration; FLA return by 15 July; issue and transfer at or above fair
value for non-residents. Sources: Nishith Desai, Chambers, Bar and Bench, Mondaq, KS&K (checked 14 Nov 2026)."""
from urllib.parse import quote
from build_lib import page, write_page

UPDATED = "Last updated: 14 November 2026."


def wa(t):
    return "https://wa.me/917801887130?text=" + quote(t)


def ul(*x):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in x) + "</ul>"


def table(head, rows):
    return ("<table><thead><tr>" + "".join(f"<th>{h}</th>" for h in head) + "</tr></thead><tbody>"
            + "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows) + "</tbody></table>")


CONTACT = ("Email info@bharatquantumprospera.com or WhatsApp +91 78018 87130 with the investor's country, the Indian company's sector, the amount and whether shares are new or bought from existing holders. "
           "We reply within one working day with the route, the filings and a fixed-scope quote.")
SLUG = "fdi-rules-india-2026-automatic-government-route-reporting-draft-foreign-investment-rules"
BOX = (f'<div style="border:1px solid var(--line);border-left:4px solid #C2312A;border-radius:10px;padding:16px 18px;margin:18px 0;background:var(--bg-soft)">'
       f'<p style="margin:0 0 8px;font-weight:600">Most FDI problems are timing problems.</p>'
       f'<p style="margin:0">Allotting late, filing FC-GPR late or pricing below fair value leads to late fees or compounding. A short checklist before the money arrives avoids all three. '
       f'<a href="{wa("Hi Durgesh, we are bringing foreign investment into an Indian company. Can you confirm the FDI route and filings?")}" target="_blank" rel="noopener"><strong>WhatsApp CA Durgesh Chavda</strong></a>.</p></div>')

PAGES = [dict(
    slug=SLUG,
    title="FDI Rules in India (2026): Automatic vs Government Route, Prohibited Sectors, Filings and Deadlines, and What the New Rules Change",
    em="most sectors need no approval, but every rupee needs reporting.",
    kicker="/ FDI &middot; FEMA &middot; Foreign investors &middot; Updated 2026-11-14",
    lead=("Foreign direct investment into India comes under the <strong>FEMA (Non-debt Instruments) Rules, 2019</strong> and DPIIT's <strong>Consolidated FDI Policy</strong>. Most sectors are on the <strong>automatic route</strong> (no prior approval); some sectors, and <strong>any investment from a country sharing a land border with India</strong>, need <strong>government approval</strong>; a few sectors are prohibited. "
          "Every investment must be reported: shares allotted within <strong>60 days</strong> of receiving the money, <strong>Form FC-GPR within 30 days</strong> of allotment, <strong>FC-TRS within 60 days</strong> for share transfers, and the annual <strong>FLA return by 15 July</strong>. "
          "In 2026, <strong>Press Note 2</strong> reworked the land-border rules and the RBI published <strong>draft Foreign Investment Rules, 2026</strong> to replace the NDI Rules."),
    sections=[
        ("/ The two routes and the prohibited list", "Start here.",
         table(["Route", "Applies to", "What it means"], [
             ["Automatic", "Most manufacturing, IT, services and many other sectors, within any sectoral cap", "Invest first, report to the RBI through the bank afterwards"],
             ["Government", "Specified sectors, investment beyond automatic caps, and all investment from land-border countries", "Prior approval through the Foreign Investment Facilitation Portal before investing"],
             ["Prohibited", "Lottery, gambling and betting, chit funds, Nidhi companies, trading in transferable development rights, real estate business and farmhouses, manufacture of tobacco cigarettes, among others", "No FDI"]])
         + "<p>Sector caps and conditions change through press notes; check the current Consolidated FDI Policy for your sector before investing, or see sector pages such as <a href=\"india-telecom-fdi-100-automatic-2024.html\">telecom</a> and <a href=\"india-space-fdi-100-automatic-route-2024-reform-2026.html\">space</a>.</p>"),
        ("/ Filings and deadlines", "For every investment.",
         table(["Step", "Deadline", "Form"], [
             ["Allot shares or refund the money", "Within 60 days of receiving the inward remittance", "Board and shareholder approvals; valuation report"],
             ["Report the allotment", "Within 30 days of allotment", "Form FC-GPR on the FIRMS portal"],
             ["Transfer of shares between resident and non-resident", "Within 60 days of receipt or remittance of consideration", "Form FC-TRS"],
             ["Annual return on foreign liabilities and assets", "By 15 July every year", "FLA return"],
             ["Pricing", "At the time of issue or transfer", "Not below fair value for issue or transfer to a non-resident (and not above it for transfer to a resident)"]])
         + BOX
         + '<p>Checklists: <a href="form-fc-gpr-filing-checklist-india-2026.html">FC-GPR</a> &middot; <a href="form-fc-trs-filing-checklist-india-2026.html">FC-TRS</a> &middot; <a href="fla-return-foreign-liabilities-assets-rbi-india.html">FLA return</a> &middot; <a href="fema-compounding-foreign-subsidiary-india.html">fixing late filings by compounding</a>.</p>'),
        ("/ What changed in 2026", "And what is coming.",
         table(["Change", "Status"], [
             ["Press Note 2 (2026): land-border investment framework revised (beneficial ownership defined, tiered approvals, a reporting route for some cases)", "In force, followed by the NDI (Amendment) Rules, 2026 of 1 May 2026 and a DPIIT SOP of 4 May 2026; see <a href=\"press-note-2-2026-fdi-land-border-countries-china-10-percent-60-day-approval.html\">Press Note 2 explained</a>"],
             ["Draft Foreign Exchange Management (Foreign Investment) Rules, 2026: a simpler, principle-based code to replace the NDI Rules", "Published by the RBI in July 2026; comments closed 31 August 2026; DPIIT keeps interpreting FDI policy"],
             ["Foreign individuals investing in listed Indian shares", "Permitted under the 2026 amendments; see <a href=\"foreign-individuals-invest-indian-listed-shares-fema-schedule-iii-2026.html\">foreign individuals in listed shares</a>"],
             ["FEMA compounding for overseas investment moved to RBI Regional Offices", "From 23 October 2026; see <a href=\"fema-compounding-odi-rbi-regional-office-uin-circular-28-october-2026.html\">compounding routing</a>"]])
         + '<p>Related: <a href="foreign-company-setup-indian-subsidiary-wos.html">setting up an Indian subsidiary</a> &middot; <a href="fdi-vs-fpi-india-startup-investment.html">FDI vs FPI</a> &middot; <a href="uae-investor-investing-in-india-fdi-india-uae-bit-2024-dtaa-compliance.html">UAE investors in India</a>.</p>'
         + f'<p><strong>Sources:</strong> Foreign Exchange Management Act, 1999; Foreign Exchange Management (Non-debt Instruments) Rules, 2019 and (Amendment) Rules, 2026; DPIIT Consolidated FDI Policy and Press Note 2 (2026); RBI draft Foreign Exchange Management (Foreign Investment) Rules, 2026; RBI Master Direction on Foreign Investment in India. Secondary analyses checked 14 November 2026: Nishith Desai Associates, Chambers, Bar and Bench, Mondaq. <em>{UPDATED}</em> General information, not advice for your transaction.</p>'),
    ],
    faqs=[("What are the FDI rules in India?", "FDI is governed by the FEMA (Non-debt Instruments) Rules, 2019 and DPIIT's Consolidated FDI Policy. Most sectors are on the automatic route, some need government approval, a few are prohibited, and every investment is reported to the RBI through the bank."),
          ("Which investments need government approval?", "Investments in specified sectors, investment above automatic-route caps, and any investment from a country sharing a land border with India (revised by Press Note 2 of 2026)."),
          ("What is the deadline to file Form FC-GPR?", "Within 30 days of allotting shares to the foreign investor; shares must themselves be allotted within 60 days of receiving the money."),
          ("Which sectors are prohibited for FDI?", "Lottery, gambling and betting, chit funds, Nidhi companies, trading in transferable development rights, real estate business and farmhouses, and manufacture of tobacco cigarettes, among others."),
          ("What are the new FDI rules in 2026?", "Press Note 2 (2026) revised the land-border framework, with amendment rules from 1 May 2026, and the RBI published draft Foreign Investment Rules, 2026 in July 2026 to replace the NDI Rules."),
          ("Can BQP handle FDI compliance?", "Yes. " + CONTACT)],
    related=[("form-fc-gpr-filing-checklist-india-2026.html", "FC-GPR checklist"), ("press-note-2-2026-fdi-land-border-countries-china-10-percent-60-day-approval.html", "Press Note 2 (2026)"),
             ("foreign-company-setup-indian-subsidiary-wos.html", "Indian subsidiary set-up")],
    cta_h="Bringing foreign money into an Indian company?", cta_b=CONTACT,
    keywords="FDI rules in India, new FDI rules in India 2026, FDI rules and regulations India, automatic route government route FDI, FDI prohibited sectors India, FC-GPR deadline 30 days, FC-TRS 60 days, draft Foreign Investment Rules 2026, Press Note 2 2026",
    desc="FDI rules in India in 2026: automatic vs government route, prohibited sectors, land-border approvals, filings and deadlines (allotment 60 days, FC-GPR 30 days, FC-TRS 60 days, FLA 15 July), pricing, and the 2026 changes (Press Note 2, NDI Amendment Rules, draft Foreign Investment Rules).",
    howto={"name": "How to bring FDI into an Indian company", "description": "Steps for the investee company.", "steps": [
        {"name": "Confirm route and cap", "text": "Check the sector in the Consolidated FDI Policy and whether the investor is from a land-border country."},
        {"name": "Price and approve", "text": "Obtain a valuation, pass board and shareholder approvals, and receive the funds through banking channels."},
        {"name": "Allot and report", "text": "Allot within 60 days and file Form FC-GPR within 30 days of allotment."},
        {"name": "Annual reporting", "text": "File the FLA return by 15 July every year and FC-TRS for any later transfers."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch CK complete")
