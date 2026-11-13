# -*- coding: utf-8 -*-
"""Batch CA (13 Nov 2026): where an ODI / overseas-borrowing / guarantee FEMA compounding application goes after
RBI A.P. (DIR Series) Circular No. 28/2026-27 (RBI/FED/2026-27/298) dated 23 October 2026.
Facts (circular text as transcribed by TaxGuru, 23 Oct 2026; Sansa Legal summary, 30 Oct 2026):
- Compounding of contraventions relating to overseas investment, borrowing and lending, and guarantees delegated from
  CEFA, Central Office to Regional Offices, under sections 10(4) and 11(1) of FEMA; builds on A.P. (DIR) Circular
  17/2024-25 (1 Oct 2024) and the Master Directions on compounding dated 22 April 2025 (to be updated).
- Overseas investment: routed by the UIN prefix of the foreign entity: Ahmedabad AH; Bengaluru BG; Mumbai BL, BY, PJ;
  Kolkata BN, CA, GA, GH; New Delhi CG, JM, JR, KA, ND, PT, WR; Hyderabad HY; Chennai KO, MA. Covers FEMA 19/RB-2000,
  FEMA 120/RB-2004, OI Rules 2022, OI Regulations 2022 (FEMA 400/2022-RB).
- Borrowing/lending and guarantees (FEMA 3/2000-RB, 4/2000-RB, 3(R)/RB-2018, 8/RB-2000, 8(R)/RB-2026): Regional Office
  with jurisdiction over the registered office of the Indian entity or place of domicile (Part C of Annexure I to the
  Master Directions). Lending/guarantees to a foreign entity in which the applicant has ODI follow the UIN routing.
- Stays with CEFA, Central Office, Mumbai: overseas investment contraventions where no UIN has been allotted, and
  applications covering categories delegated to different offices (filed as one application).
- Who may apply, contents and how the amount is worked out are unchanged (section 15 of FEMA; Master Directions).
- Earlier: A.P. (DIR Series) Circular No. 02 dated 1 April 2026 moved overseas investment references (approvals) to
  the same seven Regional Offices via the PRAVAAH portal, by UIN prefix (Taxmann, 3 April 2026).
"""
from urllib.parse import quote
from build_lib import page, write_page

UPDATED = "Last updated: 13 November 2026."


def wa(t):
    return "https://wa.me/917801887130?text=" + quote(t)


def ul(*x):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in x) + "</ul>"


def table(head, rows):
    return ("<table><thead><tr>" + "".join(f"<th>{h}</th>" for h in head) + "</tr></thead><tbody>"
            + "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows) + "</tbody></table>")


CONTACT = ("WhatsApp +91 78018 87130 or email durgesh@bharatquantumprospera.com with the UIN (if any), the dates of each remittance and share issue, and what was reported to the bank. "
           "We reply the same working day with the route (late submission fee or compounding), the office it goes to and a fixed-scope quote.")
SLUG = "fema-compounding-odi-rbi-regional-office-uin-circular-28-october-2026"
BOX = (f'<div style="border:1px solid var(--line);border-left:4px solid #C2312A;border-radius:10px;padding:16px 18px;margin:18px 0;background:var(--bg-soft)">'
       f'<p style="margin:0 0 8px;font-weight:600">No UIN? Your case still goes to Mumbai.</p>'
       f'<p style="margin:0">A UIN is allotted only when an investment is reported. Founders and NRIs who returned to India and never reported their foreign company have no UIN, so their compounding stays with CEFA at the Central Office. '
       f'<a href="{wa("Hi Durgesh, I hold shares in a foreign company and I am not sure it was reported under FEMA. Can you check what I need to do?")}" target="_blank" rel="noopener"><strong>WhatsApp CA Durgesh Chavda</strong></a>.</p></div>')

PAGES = [dict(
    slug=SLUG,
    title="FEMA Compounding for ODI, Overseas Loans and Guarantees: Which RBI Regional Office Handles Your Case (Circular 28 of 23 October 2026)",
    em="routed by the first letters of your UIN.",
    kicker="/ FEMA &middot; Overseas investment &middot; Compounding &middot; Updated 2026-11-13",
    lead=("Since <strong>23 October 2026</strong>, applications to compound FEMA contraventions on <strong>overseas investment (ODI), overseas borrowing and lending, and guarantees</strong> go to one of seven RBI Regional Offices instead of the Central Office in Mumbai "
          "(<strong>A.P. (DIR Series) Circular No. 28/2026-27</strong>, RBI/FED/2026-27/298). Overseas investment cases are allotted by the <strong>UIN prefix</strong> of the foreign entity: for example AH goes to Ahmedabad, BY to Mumbai and ND to New Delhi. "
          "Two kinds of case stay with CEFA at the Central Office: investments that have <strong>no UIN</strong> (never reported) and applications that mix categories belonging to different offices. Who may apply, what the application contains and how the amount is worked out have not changed."),
    sections=[
        ("/ Overseas investment: UIN prefix to Regional Office", "Find your office in ten seconds.",
         "<p>The UIN (unique identification number) is the number the RBI allots to each foreign entity when the first ODI is reported through the authorised dealer bank. Its first two letters decide the office:</p>"
         + table(["RBI Regional Office", "UIN prefix"], [
             ["Ahmedabad", "AH"], ["Bengaluru", "BG"], ["Mumbai", "BL, BY, PJ"], ["Kolkata", "BN, CA, GA, GH"],
             ["New Delhi", "CG, JM, JR, KA, ND, PT, WR"], ["Hyderabad", "HY"], ["Chennai", "KO, MA"],
             ["CEFA, Central Office, Mumbai", "No UIN allotted, or a mixed application"]])
         + "<p>It covers contraventions under the Overseas Investment Rules and Regulations, 2022 (FEMA 400/2022-RB) and the older regulations (FEMA 19/RB-2000 and FEMA 120/RB-2004), and other provisions to the extent they relate to the underlying overseas investment. "
           "The same seven offices have handled overseas investment <em>approvals</em> (references from banks on the PRAVAAH portal, routed by UIN prefix) since A.P. (DIR Series) Circular No. 02 of 1 April 2026.</p>"
         + BOX),
        ("/ Borrowing, lending and guarantees", "Routed by where you are, not by the UIN.",
         ul("<strong>External commercial borrowing, trade credit, lending and guarantees:</strong> the Regional Office with jurisdiction over the registered office of the Indian company or entity, or the applicant's place of domicile (Part C of Annexure I to the compounding Master Directions).",
            "<strong>Exception:</strong> a loan to, or guarantee for, a foreign entity in which the applicant has made ODI follows the overseas investment (UIN) routing.",
            "<strong>One set of facts, two categories in different offices:</strong> file one application with CEFA in Mumbai; it is not split.")),
        ("/ Typical cases we see", "Who is likely to need this.",
         table(["Situation", "Usual position"], [
             ["Indian resident founders hold a US or Singapore company that owns their Indian company", "Often outside the general permission (control from 10%); see <a href=\"triangular-structure-indian-founders-us-parent-indian-subsidiary-odi-schedule-iii-2026.html\">the triangular structure</a>. If done without approval, compounding"],
             ["NRI returned to India, still holds shares of a company they set up abroad, never reported", "No UIN, so CEFA, Central Office; first regularise the reporting through the bank"],
             ["Form ODI or the annual performance report filed late", "Usually a late submission fee through the bank within the time the regulations allow; compounding only beyond that"],
             ["Indian company gave a corporate guarantee for its foreign subsidiary without reporting", "Guarantee contravention linked to ODI, so the UIN office"],
             ["Indian company raised an ECB and missed reporting or end-use conditions", "Regional Office for the company's registered office"]])
         + '<p>Related: <a href="fema-compounding-foreign-subsidiary-india.html">FEMA compounding for Indian subsidiaries of foreign companies</a> &middot; <a href="form-odi-apr-annual-performance-report-india-2026.html">ODI annual performance report</a> &middot; <a href="fema-odi-us-entity-indian-founder.html">FEMA ODI for Indian founders</a>.</p>'),
        ("/ What has not changed", "Only the filing point moved.",
         ul("The power to compound is in section 15 of FEMA; the procedure is in the RBI Master Directions on compounding of contraventions dated 22 April 2025, which the RBI said will be updated for this change.",
            "Who may apply, the documents and declarations, and the way the compounding amount is calculated stay the same.",
            "Compounding is voluntary and settles the contravention; serious cases such as suspected money laundering are excluded and go to the Directorate of Enforcement.",
            "Authorised dealer banks have been asked to tell their customers about the change.")
         + f'<p><strong>Sources:</strong> RBI A.P. (DIR Series) Circular No. 28/2026-27 (RBI/FED/2026-27/298) dated 23 October 2026; A.P. (DIR Series) Circular No. 17/2024-25 dated 1 October 2024; A.P. (DIR Series) Circular No. 02/2026-27 dated 1 April 2026; Master Directions on compounding of contraventions under FEMA, 1999 (22 April 2025); Foreign Exchange Management (Overseas Investment) Rules and Regulations, 2022. <em>{UPDATED}</em> General information, not advice for your situation; confirm with your authorised dealer bank.</p>'),
    ],
    faqs=[("Which RBI office handles FEMA compounding for overseas investment now?", "Since 23 October 2026, one of seven Regional Offices chosen by the first two letters of the foreign entity's UIN: Ahmedabad (AH), Bengaluru (BG), Mumbai (BL, BY, PJ), Kolkata (BN, CA, GA, GH), New Delhi (CG, JM, JR, KA, ND, PT, WR), Hyderabad (HY) and Chennai (KO, MA)."),
          ("What if my foreign company has no UIN?", "Cases with no UIN stay with CEFA, Foreign Exchange Department, RBI Central Office, Mumbai. A UIN is allotted only when the ODI is reported, so unreported investments fall here."),
          ("Where do ECB, lending or guarantee contraventions go?", "To the Regional Office with jurisdiction over the Indian entity's registered office or the applicant's domicile. A loan or guarantee to a foreign entity in which the applicant holds ODI follows the UIN routing instead."),
          ("Did the compounding fee or procedure change?", "No. The circular changes only where the application is filed. Who may apply, the contents and the computation follow the 22 April 2025 Master Directions."),
          ("Which circular made this change?", "A.P. (DIR Series) Circular No. 28/2026-27 (RBI/FED/2026-27/298) dated 23 October 2026."),
          ("Is a late ODI filing always a compounding case?", "Not usually. A late Form ODI or annual performance report is normally regularised with a late submission fee through the bank, within the period the Overseas Investment Regulations allow. Compounding is for contraventions beyond that, such as investing without the required approval."),
          ("Can BQP prepare our compounding application?", "Yes. " + CONTACT)],
    related=[("triangular-structure-indian-founders-us-parent-indian-subsidiary-odi-schedule-iii-2026.html", "Triangular structure under FEMA"),
             ("fema-compounding-foreign-subsidiary-india.html", "FEMA compounding for foreign subsidiaries"),
             ("fema-breach-found-pre-ma-diligence-urgent-compounding-india.html", "FEMA breach found in due diligence")],
    cta_h="A FEMA gap in your overseas investment?", cta_b=CONTACT,
    keywords="FEMA compounding ODI regional office, RBI circular 28 2026-27 compounding, UIN prefix RBI regional office, compounding overseas investment contravention, ECB compounding regional office, CEFA RBI compounding no UIN, FEMA compounding Indian founder US company, ODI late reporting compounding 2026",
    desc="From 23 October 2026, FEMA compounding for ODI, overseas borrowing/lending and guarantee contraventions goes to seven RBI Regional Offices (RBI Circular 28/2026-27). UIN prefix table, what stays with CEFA (no UIN, mixed cases), jurisdiction for ECB and guarantees, and typical founder and NRI cases.",
    howto={"name": "How to file a FEMA compounding application for an overseas investment contravention", "description": "Steps after RBI Circular 28/2026-27.", "steps": [
        {"name": "List the contraventions", "text": "Map each remittance, share issue, loan and guarantee against the Overseas Investment Rules and what was reported to the bank."},
        {"name": "Check for a cheaper fix", "text": "Reporting delays within the permitted period are usually settled with a late submission fee through the bank instead of compounding."},
        {"name": "Find the office", "text": "Use the UIN prefix table; no UIN or a mixed case goes to CEFA, Central Office, Mumbai; ECB and guarantees go by registered office or domicile."},
        {"name": "File under the Master Directions", "text": "Prepare the application, declarations and documents required by the 22 April 2025 Master Directions and pay the compounding amount once the order is passed."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch CA complete")
