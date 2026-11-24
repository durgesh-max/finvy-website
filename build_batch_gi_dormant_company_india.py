# -*- coding: utf-8 -*-
"""Batch GI (24 Nov 2026): dormant company status in India (section 455 Companies Act) - who can apply, MSC forms, reduced
compliance, what still applies (income tax return, FLA for foreign-owned companies), and dormant vs strike-off. Call-first
page for founders and foreign parents with inactive Indian subsidiaries.
Demand: sweep ac57 (24 Nov 2026), all 7 markets: "dormant company india", "sleeping company india", "dormant company in
india example". No page on the site.
Facts (checked 24 Nov 2026): section 455 of the Companies Act, 2013 lets a company formed for a future project or to hold
an asset or intellectual property with no significant accounting transaction, or an inactive company, apply for dormant
status; listed companies cannot; application in Form MSC-1 under Rule 3 of the Companies (Miscellaneous) Rules, 2014;
certificate in MSC-2; annual return of a dormant company in MSC-3; return to active status in MSC-4 (MCA instruction
kits; ca2013.com; CAclubindia). Board meetings: at least one in each half of a calendar year with a 90-day gap (section
173(5)). Rule 3 conditions exclude companies with investigation or prosecution pending, outstanding deposits, loans or
statutory dues, among others. Income tax return remains mandatory for every company; FLA return remains for companies with
foreign investment (site pages)."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 24 November 2026."
SLUG = "dormant-company-india-section-455-msc-1-msc-3-foreign-subsidiary-vs-strike-off-2026"

C = contact("the company's activity in the last two years, its assets and liabilities, any loans or dues outstanding, its shareholders (Indian or foreign) and whether you plan to restart or close it")
L = lambda h, t: f'<a href="{h}">{t}</a>'
PAGES = [dict(
    slug=SLUG,
    title="Dormant Company in India (2026): Section 455 Status, MSC-1 and MSC-3, What Still Applies, and Dormant vs Strike-Off",
    em="pause the company without closing it.",
    kicker="/ Companies &middot; Dormant status &middot; Updated 2026-11-24",
    lead=("<strong>An Indian company that is not trading can apply to the Registrar of Companies for dormant status under section 455 of the Companies Act, 2013, by filing Form MSC-1, and then file a short annual return (MSC-3) instead of the full set of filings.</strong> "
          "It suits a company formed for a future project, one that only holds an asset or intellectual property, or one with no significant accounting transaction in the last two financial years. Listed companies, and companies with outstanding loans, deposits, statutory dues or pending investigations, cannot apply. "
          "Dormant status does not switch off everything: the company still files its <strong>income tax return</strong>, and a foreign-owned company still files the <strong>FLA return</strong> with the RBI. "
          "If there is no plan to restart, <strong>striking off</strong> the company may be cleaner."),
    sections=[
        ("/ Quick answers", "What founders and foreign parents ask.",
         ul("<strong>What is a dormant company in India?</strong> A company that has obtained dormant status from the Registrar under section 455 because it has no significant accounting transactions, for example one formed for a future project or holding only an asset or IP.",
            "<strong>What is an example of a dormant company?</strong> A subsidiary set up by a foreign group for a project that has not started, a company that owns only a property or a trademark, or a startup that has paused operations for two years.",
            "<strong>How do I apply?</strong> Pass a special resolution (or get the required consent), then file Form MSC-1 with the Registrar; once approved, the Registrar issues a certificate in MSC-2.",
            "<strong>What does a dormant company still have to do?</strong> File MSC-3 every year, hold at least one board meeting in each half of the calendar year, keep the minimum number of directors, file its income tax return and, if foreign-owned, the FLA return.",
            "<strong>How does it become active again?</strong> By filing Form MSC-4 with the Registrar once it wants to start business again.")),
        ("/ Dormant vs strike-off vs active", "Choosing the right route.",
         table(["", "Dormant (section 455)", "Strike off (STK-2)", "Stay active"], [
             ["Best for", "A pause with a plan to restart, or a company holding an asset or IP", "A company with no future plans and no assets or liabilities", "Any company still trading"],
             ["ROC filings", "MSC-3 annual return", "Ends after the company is struck off", "Full annual filings (AOC-4, MGT-7)"],
             ["Income tax return", "Still required", "Required until closure", "Required"],
             ["Foreign-owned: FLA return", "Still required", "Until closure", "Required"],
             ["Restart", "MSC-4", "Restoration only through the tribunal", "Not needed"]])
         + '<p>Closing instead: see ' + L("close-company-in-india-strike-off-stk-2-procedure-restore-foreign-subsidiary-2026.html", "strike-off and restoration") + '. Annual filings for active foreign-owned companies: ' + L("foreign-owned-indian-subsidiary-annual-compliance-calendar-fy-2026-27.html", "the subsidiary compliance calendar") + '.</p>'),
        ("/ Before you apply", "Conditions and practical points.",
         ul("<strong>No significant accounting transaction:</strong> paying ROC fees, statutory payments, allotting shares and paying for office and records upkeep do not count as significant transactions.",
            "<strong>Clear the blockers first:</strong> outstanding loans, deposits or statutory dues, pending prosecutions or investigations, and unfiled returns stop the application.",
            "<strong>Keep minimum directors:</strong> two for a private company, three for a public company, one for a one person company, and the resident director requirement continues.",
            "<strong>Foreign parents:</strong> keep FEMA reporting current (FLA return each year) even while dormant; plan whether to inject funds or repatriate before applying.",
            "<strong>Tax:</strong> a dormant company with no income still files a nil or loss return; brought-forward losses follow normal rules when it restarts.")
         + call_box("dormant status or closing a company", ["Whether the company qualifies for dormant status",
                                                            "MSC-1 application and board resolutions",
                                                            "Dormant vs strike-off for a foreign subsidiary",
                                                            "Income tax and FLA filings while dormant",
                                                            "Restarting with MSC-4"],
                    "the company's last two years of activity, assets, liabilities and shareholders.")
         + sources("Companies Act, 2013, sections 455 and 173(5); Companies (Miscellaneous) Rules, 2014 and amendments; MCA instruction kits for Forms MSC-1 and MSC-4; ca2013.com and CAclubindia commentary on dormant companies; Income-tax Act provisions on mandatory company returns; RBI FLA return requirements. Checked 24 November 2026.")),
    ],
    faqs=[("What is a dormant company in India?", "A company that has obtained dormant status from the Registrar of Companies under section 455 of the Companies Act, 2013, because it has been formed for a future project, holds an asset or intellectual property, or has had no significant accounting transaction in the last two financial years."),
          ("How do I make my company dormant in India?", "Check the conditions, pass the required resolution, and file Form MSC-1 with the Registrar. If approved, the Registrar issues a certificate of dormant status in Form MSC-2."),
          ("What filings does a dormant company make?", "An annual return of dormant company in Form MSC-3, plus its income tax return every year and, if it has foreign investment, the FLA return to the RBI. It must hold at least one board meeting in each half of the calendar year."),
          ("Can a foreign-owned subsidiary in India become dormant?", "Yes, if it meets the conditions. FEMA reporting such as the FLA return continues, and the resident director requirement still applies."),
          ("Is it better to make a company dormant or strike it off?", "Dormant status suits a pause with a plan to restart or a company holding an asset or IP. If there is no plan to restart and no assets or liabilities, striking off is usually simpler."),
        ("How do I close an LLP in India?", "An LLP that has stopped business can apply to be struck off. Settle all liabilities and close the bank account, bring annual filings (Form 8 and Form 11) and tax returns up to date, then file Form 24 on the MCA portal with the consent of all partners, a statement of accounts showing nil assets and liabilities certified by a practising professional, and affidavits and indemnity bonds from the designated partners. The Registrar gives notice and allows objections, usually for a month, before striking the name off."),
        ("Can an LLP with liabilities or pending disputes use Form 24?", "No. Form 24 is only for LLPs with nil assets and liabilities and no ongoing business, contracts, employees or disputes. Others have to settle these first or go through winding up, which is slower and involves the tribunal or a voluntary liquidation process."),
          ("Can BQP handle dormant status or closure?", "Yes. " + C)],
    related=[("close-company-in-india-strike-off-stk-2-procedure-restore-foreign-subsidiary-2026.html", "Strike-off and restoration"),
             ("foreign-owned-indian-subsidiary-annual-compliance-calendar-fy-2026-27.html", "Subsidiary compliance calendar"),
             ("mgt-7-mgt-7a-annual-return-29-november-2026-india.html", "MGT-7 annual return"),
             ("doing-business-in-india-2026-guide-for-foreign-companies-entity-tax-fdi-compliance-repatriation.html", "Doing business in India"),
             ("does-foreign-company-need-to-file-income-tax-return-in-india-royalty-fees-dividend-capital-gains-itr-6-2026.html", "Foreign company tax return in India")],
    cta_h="Company not trading?", cta_b=C,
    keywords="dormant company India, sleeping company India, section 455 Companies Act, MSC-1 dormant company, MSC-3 annual return, dormant company example India, dormant vs strike off, foreign subsidiary dormant India",
    desc="Dormant company in India (2026): section 455 status for companies formed for future projects, holding assets or IP, or inactive for two years; MSC-1 application, MSC-3 annual return, MSC-4 to restart; income tax and FLA filings still apply; dormant vs strike-off for foreign subsidiaries.",
    howto={"name": "How to make an Indian company dormant", "description": "Steps under section 455.", "steps": [
        {"name": "Check eligibility", "text": "No significant accounting transactions; no outstanding loans, deposits, dues or proceedings."},
        {"name": "Pass the resolution", "text": "Board and shareholder approval as required."},
        {"name": "File Form MSC-1", "text": "With the Registrar of Companies."},
        {"name": "Receive MSC-2", "text": "The certificate of dormant status."},
        {"name": "Keep up reduced filings", "text": "MSC-3 yearly, income tax return, FLA if foreign-owned, board meetings."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch GI complete")
