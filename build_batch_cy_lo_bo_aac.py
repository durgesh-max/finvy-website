# -*- coding: utf-8 -*-
"""Batch CY (18 Nov 2026): annual compliance for a liaison office or branch office of a foreign company in India -
Annual Activity Certificate (AAC) and the income-tax annual statement (Form 49C / Form 162).
Demand: autocomplete sweep 18 Nov 2026 - "annual activity certificate liaison office" in all 7 markets; no page on
the site. Facts: FEMA 22(R)/2016-RB and RBI Master Direction - AAC for each financial year submitted by 30 September
to the AD Category-I bank and to the Director General of Income Tax (International Taxation), with audited financial
statements including a receipt and payment account, certified by a chartered accountant; the old 30 April date was
superseded. Form 49C (liaison office annual statement) under the 1961 Act: due within eight months of the financial
year end (30 November 2026 for FY 2025-26 per secondary guides); from FY 2026-27 replaced by Form 162 under section
505 of the Income-tax Act, 2025, with timing aligned to the AAC (confirm against the notification). A liaison office
cannot earn income; a branch office files an income-tax return as a foreign company. Sources: Treelife, TaxGuru,
CAclubindia summaries; RBI notification references (checked 18 Nov 2026)."""
from urllib.parse import quote
from build_lib import page, write_page

UPDATED = "Last updated: 18 November 2026."


def wa(t):
    return "https://wa.me/917801887130?text=" + quote(t)


def ul(*x):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in x) + "</ul>"


def table(head, rows):
    return ("<table><thead><tr>" + "".join(f"<th>{h}</th>" for h in head) + "</tr></thead><tbody>"
            + "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows) + "</tbody></table>")


CONTACT = ("Email info@bharatquantumprospera.com or WhatsApp +91 78018 87130 with the office type (liaison, branch or project), the AD bank and the last year filed. "
           "We reply within one working day with the filing calendar and a fixed-scope quote for the audit, AAC and income-tax filings.")
SLUG = "liaison-office-branch-office-annual-activity-certificate-aac-form-49c-162-india-2026"
BOX = (f'<div style="border:1px solid var(--line);border-left:4px solid #C2312A;border-radius:10px;padding:16px 18px;margin:18px 0;background:var(--bg-soft)">'
       f'<p style="margin:0 0 8px;font-weight:600">The AAC goes to two places, and the tax statement is separate.</p>'
       f'<p style="margin:0">Filing with the bank alone does not cover the income-tax department, and missed years make renewal or closure of the office harder. We audit the accounts, certify the AAC and file the tax statement in one engagement. '
       f'<a href="{wa("Hi Durgesh, we have a liaison / branch office in India and need the annual activity certificate and tax filings done.")}" target="_blank" rel="noopener"><strong>WhatsApp CA Durgesh Chavda</strong></a>.</p></div>')

PAGES = [dict(
    slug=SLUG,
    title="Annual Activity Certificate for a Liaison or Branch Office in India (2026): 30 September Deadline, Form 49C / Form 162 and Annual Compliance",
    em="what a foreign company's Indian office must file each year.",
    kicker="/ Foreign companies &middot; Liaison office &middot; Branch office &middot; Updated 2026-11-18",
    lead=("Every <strong>liaison office (LO)</strong>, <strong>branch office (BO)</strong> and project office of a foreign company in India must file an <strong>Annual Activity Certificate (AAC)</strong> for each financial year (April-March) by <strong>30 September</strong>. It is certified by a <strong>Chartered Accountant</strong>, filed with the office's <strong>authorised dealer (AD) bank</strong> and with the <strong>Director General of Income Tax (International Taxation)</strong>, and accompanied by the <strong>audited financial statements</strong>, including a receipt and payment account. "
          "The AAC confirms that the office carried on only the activities the RBI permitted. A liaison office also files an <strong>annual statement with the income-tax department</strong> (Form 49C under the 1961 rules, replaced by <strong>Form 162</strong> under the Income-tax Act, 2025 from FY 2026-27), and a branch office files an <strong>income-tax return</strong> as a foreign company."),
    sections=[
        ("/ The annual calendar", "What is due, and when.",
         table(["Filing", "Who", "Due", "Filed with"], [
             ["Audit of accounts", "LO, BO, project office", "Before the AAC", "Statutory auditor (Chartered Accountant)"],
             ["Annual Activity Certificate", "LO, BO, project office", "30 September (for the year to 31 March)", "AD Category-I bank and DGIT (International Taxation)"],
             ["Annual statement of activities", "Liaison office", "Form 49C for FY 2025-26 (within eight months of year end, by 30 November 2026 per current guidance); Form 162 from FY 2026-27, with timing aligned to the AAC", "Income-tax department"],
             ["Income-tax return", "Branch office (and project office)", "As for foreign companies (31 October; 30 November where transfer pricing applies)", "Income-tax department"],
             ["ROC filings (Form FC-1 at set-up; annual FC-3 accounts and FC-4 annual return)", "Offices that are a place of business under the Companies Act", "FC-3 within 6 months of year end; FC-4 within 60 days of year end", "Registrar of Companies"]])
         + BOX),
        ("/ What the AAC confirms", "Why the bank and the tax department want it.",
         ul("That the office carried on only the permitted activities (for a liaison office: representing the parent, promoting trade, technical or financial collaboration and acting as a communication channel; no commercial or trading income).",
            "That expenses were met from inward remittances from the parent (liaison office) and that permissions, such as validity and approved activities, were respected.",
            "That the accounts were audited and the office's bank accounts were used as permitted.",
            "<strong>Validity:</strong> a liaison office approval is usually for three years (two years for some sectors) and can be extended through the AD bank, which looks at the AAC record."))
        ,
        ("/ Problems we see", "And how they are fixed.",
         ul("Years of AACs not filed: file the pending years with audited accounts, and regularise any FEMA contravention through the AD bank or compounding; see <a href=\"fema-compounding-foreign-subsidiary-india.html\">FEMA compounding</a>.",
            "The office did commercial work (invoicing Indian customers): a liaison office cannot earn income, and this can create a permanent establishment and tax exposure for the parent; see <a href=\"permanent-establishment-india-meaning-types-risk-tax-foreign-company-2026.html\">permanent establishment</a>.",
            "Validity lapsed without extension: apply through the AD bank, or plan closure or conversion to a subsidiary; see <a href=\"branch-office-vs-liaison-vs-wos-india-foreign.html\">liaison vs branch vs subsidiary</a>.")
         + '<p>Related: <a href="india-market-entry-foreign-company-guide.html">India market entry guide</a> &middot; <a href="project-office-india-foreign-company-registration-fema-conditions-tax-2026.html">project office in India</a> &middot; <a href="india-services-for-foreign-companies-complete-list.html">services for foreign companies</a>.</p>'
         + f'<p><strong>Sources:</strong> Foreign Exchange Management (Establishment in India of a branch office or a liaison office or a project office or any other place of business) Regulations, 2016 (FEMA 22(R)/2016-RB) and the RBI Master Direction; Income-tax Rules (Form 49C) and the Income-tax Act, 2025 (Form 162 under section 505); Companies (Registration of Foreign Companies) Rules, 2014. Secondary guides checked 18 November 2026: Treelife, TaxGuru, CAclubindia. <em>{UPDATED}</em> Confirm current form numbers and dates against the latest notifications.</p>'),
    ],
    faqs=[("What is the due date for the Annual Activity Certificate of a liaison office?", "30 September each year, for the financial year ended 31 March, filed with the AD Category-I bank and the Director General of Income Tax (International Taxation)."),
          ("Who certifies the Annual Activity Certificate?", "A Chartered Accountant, usually the auditor of the office, together with the audited financial statements including a receipt and payment account."),
          ("Does a branch office also file an AAC?", "Yes. Branch, liaison and project offices all file an AAC. A branch office also files an income-tax return as a foreign company."),
          ("What is Form 49C?", "The annual statement a liaison office files with the income-tax department about its activities. Under the Income-tax Act, 2025 it is replaced by Form 162 from FY 2026-27."),
          ("What happens if AACs were not filed?", "Pending years should be filed with audited accounts; the delay is a FEMA contravention that may need regularisation or compounding, and it can hold up extension of the office's validity or its closure."),
          ("Can BQP handle our office's annual compliance?", "Yes. " + CONTACT)],
    related=[("branch-office-vs-liaison-vs-wos-india-foreign.html", "Liaison vs branch vs subsidiary"), ("project-office-india-foreign-company-registration-fema-conditions-tax-2026.html", "Project office in India"),
             ("fema-compounding-foreign-subsidiary-india.html", "FEMA compounding")],
    cta_h="Annual filings for your India liaison or branch office?", cta_b=CONTACT,
    keywords="annual activity certificate liaison office, AAC liaison office India due date, branch office annual activity certificate, Form 49C liaison office, Form 162 Income-tax Act 2025, liaison office annual compliance India, DGIT international taxation AAC, foreign company liaison office India 2026",
    desc="Annual Activity Certificate (AAC) for a liaison, branch or project office in India: due 30 September to the AD bank and DGIT (International Taxation) with audited accounts, Form 49C / Form 162 for liaison offices, income-tax return for branch offices, ROC filings and fixing missed years.",
    howto={"name": "How a liaison or branch office files its annual compliance in India", "description": "Annual steps for foreign companies' Indian offices.", "steps": [
        {"name": "Close and audit the accounts", "text": "Prepare financial statements and a receipt and payment account for the year to 31 March; get them audited."},
        {"name": "Prepare the AAC", "text": "Chartered Accountant certifies that only permitted activities were carried on."},
        {"name": "File by 30 September", "text": "Submit the AAC with audited accounts to the AD bank and DGIT (International Taxation)."},
        {"name": "File the tax statement or return", "text": "Form 49C / Form 162 for a liaison office; income-tax return for a branch office."},
        {"name": "Track validity", "text": "Apply for extension through the AD bank before the approval lapses."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch CY complete")
