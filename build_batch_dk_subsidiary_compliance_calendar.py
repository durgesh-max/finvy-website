# -*- coding: utf-8 -*-
"""Batch DK (19 Nov 2026): annual compliance calendar for a foreign-owned Indian subsidiary, FY 2026-27 (first year under
the Income-tax Act, 2025). Call-first page. Demand: sweep 19 Nov 2026 (ac15) seeds "indian subsidiary annual
compliance", "foreign subsidiary compliance india", "india subsidiary statutory audit"; no single calendar page for
foreign parents on the site.
Facts: advance tax 15 June/15 September/15 December/15 March; TDS deposit by the 7th (30 April for March); quarterly TDS
statements 31 July, 31 October, 31 January, 31 May; GSTR-1 by the 11th and GSTR-3B by the 20th (monthly filers); annual
GST return and reconciliation by 31 December of the next year; PF and ESI by the 15th; AGM within six months of year
end (by 30 September); AOC-4 within 30 days and MGT-7 within 60 days of the AGM; ADT-1 within 15 days of the AGM where
an auditor is appointed; DPT-3 by 30 June; MSME-1 half-yearly (30 April, 31 October) where dues to micro/small
suppliers exceed 45 days; DIR-3 KYC once every three years by 30 June; at least four board meetings a year with no gap
over 120 days (two for small companies); FLA return by 15 July; FC-GPR within 30 days of allotment, FC-TRS within 60
days, Form DI within 30 days; tax audit report by 30 September, transfer pricing accountant's report by 31 October,
return by 31 October (30 November with transfer pricing); master file by 30 November where thresholds are met. Dates
follow the current schedule; Income-tax Act, 2025 form numbers apply from FY 2026-27."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

HUB = "foreign-company-india-advisor-market-research-entity-due-diligence-m-and-a-joint-venture-2026"
CAL = "foreign-owned-indian-subsidiary-annual-compliance-calendar-fy-2026-27"

C_CAL = contact("your subsidiary's CIN or name, its activity, whether it has GST and payroll, and any foreign-parent transactions")
PAGES = [dict(
    slug=CAL,
    title="Annual Compliance Calendar for a Foreign-Owned Indian Subsidiary (FY 2026-27): Tax, GST, Payroll, Company Law, FEMA and Transfer Pricing Dates",
    em="for foreign parents and their India finance teams.",
    kicker="/ Foreign parents &middot; Compliance &middot; FY 2026-27 &middot; Updated 2026-11-19",
    lead=("A foreign-owned Indian subsidiary has five layers of compliance. <strong>Monthly</strong>: TDS deposit by the 7th, GST returns by the 11th and 20th, provident fund by the 15th. <strong>Quarterly</strong>: advance tax and TDS statements. <strong>Annual company law</strong>: audited accounts, an AGM by 30 September, then AOC-4 and MGT-7. <strong>FEMA</strong>: the FLA return by <strong>15 July</strong>, plus event-based FC-GPR, FC-TRS and Form DI. <strong>Year-end tax</strong>: tax audit by 30 September, transfer pricing report by 31 October, and the return by 31 October, or <strong>30 November</strong> where transfer pricing applies. "
          "FY 2026-27 (April 2026 to March 2027) is the first year under the <strong>Income-tax Act, 2025</strong>, so form names change. Most missed deadlines in foreign-owned subsidiaries are not the big returns. They are the FLA return, transfer pricing documentation for parent recharges, and board meetings."),
    sections=[
        ("/ Recurring deadlines", "Every month and quarter.",
         table(["Frequency", "What", "Due"], [
             ["Monthly", "TDS deposit (salaries, vendors, payments to the parent)", "7th of next month (30 April for March)"],
             ["Monthly", "GSTR-1 and GSTR-3B (monthly filers)", "11th and 20th of next month"],
             ["Monthly", "Provident fund and ESI", "15th of next month"],
             ["Quarterly", "Advance tax", "15 June, 15 September, 15 December, 15 March"],
             ["Quarterly", "TDS statements", "31 July, 31 October, 31 January, 31 May"],
             ["Half-yearly", "MSME-1 (if dues to micro or small suppliers are over 45 days)", "30 April and 31 October"],
             ["During the year", "Board meetings", "At least four, no gap over 120 days (two for small companies)"]])
         + call_box("compliance for our Indian subsidiary", ["A calendar tailored to your subsidiary's registrations and transactions",
                                                              "Gaps from past years and how to regularise them",
                                                              "Transfer pricing for recharges, royalties and services with the parent",
                                                              "FEMA filings for capital, loans and downstream investment",
                                                              "Who does what between your team and us each month"],
                    "the subsidiary's name or CIN, last filed accounts, registrations (GST, payroll) and a list of transactions with the parent.")),
        ("/ Annual deadlines (FY 2026-27)", "Year-end in 2027.",
         table(["Area", "What", "Due"], [
             ["Company law", "DPT-3 (return of deposits and exempt loans)", "30 June 2027"],
             ["Company law", "DIR-3 KYC (once every three years)", "30 June in the year it falls due"],
             ["FEMA", "FLA return (foreign liabilities and assets)", "15 July 2027"],
             ["Company law", "Statutory audit and AGM", "AGM by 30 September 2027"],
             ["Company law", "ADT-1 (auditor appointment, where made)", "Within 15 days of the AGM"],
             ["Company law", "AOC-4 (financial statements)", "Within 30 days of the AGM"],
             ["Company law", "MGT-7 / MGT-7A (annual return)", "Within 60 days of the AGM"],
             ["Income tax", "Tax audit report", "30 September 2027"],
             ["Income tax", "Transfer pricing accountant's report", "31 October 2027"],
             ["Income tax", "Return of income", "31 October 2027 (30 November 2027 with transfer pricing)"],
             ["Income tax", "Master file (if group thresholds are met)", "30 November 2027"],
             ["GST", "Annual return and reconciliation", "31 December 2027"]])
         + ul("<strong>Event-based FEMA filings:</strong> FC-GPR within 30 days of share allotment; FC-TRS within 60 days of a share transfer; Form DI within 30 days of downstream investment; ECB returns where a foreign loan exists.")),
        ("/ Where foreign-owned subsidiaries slip", "And the fix.",
         ul("<strong>FLA return missed:</strong> it applies every year to companies with foreign investment, even with no new investment; file late with the explanation the RBI asks for.",
            "<strong>Parent recharges without documentation:</strong> management fees, cost allocations and royalties need agreements, benefit evidence and arm's-length pricing; see <a href=\"transfer-pricing-india-foreign-mnc.html\">transfer pricing for foreign MNCs</a>.",
            "<strong>Withholding on payments to the parent:</strong> royalties, fees and interest need tax deducted at the domestic or treaty rate, with TRC and Form 10F; see <a href=\"technology-licensing-royalty-payment-indian-company-to-foreign-company-fema-tds-gst-2026.html\">royalty payments</a>.",
            "<strong>Resident director gaps:</strong> at least one director must stay in India 182 days in the financial year; see <a href=\"nominee-resident-director-india-foreign-company.html\">resident director options</a>.",
            "<strong>Board and AGM paperwork:</strong> minutes, registers and resolutions signed on time; foreign directors can attend by video.",
            "<strong>Old FEMA gaps:</strong> late FC-GPR or missing filings are regularised through late submission fees or compounding; see <a href=\"fema-compounding-foreign-subsidiary-india.html\">FEMA compounding</a>.")
         + f'<p>Related: <a href="{HUB}.html">working with an Indian CA as a foreign company</a> &middot; <a href="india-tax-compliance-calendar-fy-2026-27-complete.html">full tax compliance calendar FY 2026-27</a> &middot; <a href="get-capital-back-from-indian-subsidiary-dividend-buyback-capital-reduction-tax-2026.html">getting money back from a subsidiary</a> &middot; <a href="fla-return-foreign-liabilities-assets-rbi-india.html">FLA return</a>.</p>'
         + sources("Companies Act, 2013 (sections 92, 96, 137, 139, 149(3), 173) and rules; Income-tax Act, 2025 and the Income-tax Rules, 2026; CGST Act, 2017; Employees&rsquo; Provident Funds and ESI schemes; Foreign Exchange Management (Non-Debt Instruments) Rules, 2019 and the reporting regulations; RBI FLA return instructions. Dates follow the schedule in force on 19 November 2026; check CBDT, CBIC and MCA notifications for extensions.")),
    ],
    faqs=[("What annual compliance does a foreign-owned Indian subsidiary have?", "Statutory audit, AGM, AOC-4 and MGT-7 under company law; tax audit, transfer pricing report and income-tax return; GST and payroll filings; and FEMA filings including the annual FLA return by 15 July."),
          ("When is the FLA return due?", "By 15 July each year, for every Indian company that has received foreign direct investment or made overseas investment, even if nothing new happened in the year."),
          ("What is the income-tax return due date for a foreign-owned subsidiary?", "31 October after the year end, or 30 November where transfer pricing applies; for FY 2026-27 that is 31 October or 30 November 2027."),
          ("How many board meetings must an Indian subsidiary hold?", "At least four a year with no more than 120 days between meetings; small companies need two. Foreign directors can attend by video conference."),
          ("Does the subsidiary need transfer pricing documentation?", "Yes, if it has international transactions with associated enterprises such as the parent; an accountant's report is due by 31 October and documentation must be maintained."),
          ("Can BQP run our subsidiary's compliance?", "Yes. " + C_CAL)],
    related=[("india-tax-compliance-calendar-fy-2026-27-complete.html", "Tax compliance calendar FY 2026-27"), ("transfer-pricing-india-foreign-mnc.html", "Transfer pricing for foreign MNCs"),
             (HUB + ".html", "Working with an Indian CA")],
    cta_h="Want your Indian subsidiary's compliance handled?", cta_b=C_CAL,
    keywords="Indian subsidiary annual compliance, foreign subsidiary compliance India, compliance calendar foreign owned company India FY 2026-27, FLA return 15 July, AOC-4 MGT-7 due date, India subsidiary statutory audit, transfer pricing due date India 2027",
    desc="Annual compliance calendar for a foreign-owned Indian subsidiary (FY 2026-27): monthly TDS, GST and PF; quarterly advance tax and TDS statements; DPT-3, FLA (15 July), AGM, AOC-4, MGT-7; tax audit 30 September, TP report 31 October, return 31 October / 30 November 2027; GST annual return; common gaps.",
    howto={"name": "How a foreign parent keeps its Indian subsidiary compliant", "description": "Yearly cycle.", "steps": [
        {"name": "Map registrations", "text": "PAN, TAN, GST, PF/ESI, professional tax and FEMA history."},
        {"name": "Run monthly filings", "text": "TDS, GST, PF and ESI on time."},
        {"name": "Hold board meetings", "text": "Four a year, with minutes and resolutions."},
        {"name": "Close the year", "text": "Audit, AGM, AOC-4, MGT-7, FLA return."},
        {"name": "File tax", "text": "Tax audit, transfer pricing report and return; keep TP documentation for parent transactions."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch DK complete:", len(PAGES))
