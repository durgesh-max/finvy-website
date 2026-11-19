# -*- coding: utf-8 -*-
"""Batch DS (20 Nov 2026): what a business loses if it misses the 21 November 2026 (audit) or 30 November 2026
(transfer pricing) ITR due date, and what to do. Call-first page for the deadline window.
Facts: CBDT Circular 07/2026 - audit-case ITR due 21 November 2026; TP cases 30 November 2026 (not extended); belated
return under section 139(4) by 31 December 2026 with section 234F fee up to INR 5,000 (INR 1,000 where total income
does not exceed INR 5 lakh) and section 234A interest at 1% per month on unpaid tax; business loss (other than
unabsorbed depreciation) can be carried forward only if the return is filed by the section 139(1) due date (sections
80 and 139(3); Delhi ITAT and HC rulings via Taxmann); section 80AC - deductions under sections 10AA and Part C of
Chapter VI-A (80-IA, 80-IAB, 80-IAC, 80-IB, 80-IBA, 80-IC, 80-ID, 80-IE, 80JJAA etc.) need the return by the due date;
Form 10-IC (115BAA) for the first year must be filed by the due date; individuals/HUFs with business income must file
Form 10-IEA by the due date to opt out of the default new regime (section 115BAC(6)); updated return later carries
25%-70% additional tax and cannot reduce tax or claim refund; condonation under section 119(2)(b) is discretionary."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 20 November 2026."
MS = "missed-itr-due-date-21-november-2026-audit-case-what-you-lose-loss-carry-forward-10-iea-80ac"
DESK = "deadline-desk-20-november-2026-to-31-january-2027-income-tax-gst-roc-nri-foreign-companies"

C_MS = contact("your entity type, whether the tax audit report is filed, losses or deductions you claim, and whether transfer pricing applies")
PAGES = [dict(
    slug=MS,
    title="Missed the 21 November 2026 ITR Deadline for Audit Cases (or 30 November for Transfer Pricing)? What You Lose and What to Do Now",
    em="business losses, deductions and regime choices depend on the due date.",
    kicker="/ Income tax &middot; Audit cases &middot; Deadline &middot; Updated 2026-11-20",
    lead=("The ITR due date for <strong>tax-audit cases</strong> for AY 2026-27 is <strong>21 November 2026</strong> (CBDT Circular 07/2026); <strong>transfer-pricing cases</strong> stay at <strong>30 November 2026</strong>. Missing it costs more than the late fee. "
          "A return filed late (a <strong>belated return</strong>, allowed until 31 December 2026) attracts a fee of up to INR 5,000 and interest at 1% a month on unpaid tax, and it can permanently lose three things. First, the <strong>carry-forward of business losses</strong> (unabsorbed depreciation survives). Second, profit-linked <strong>deductions under section 80AC</strong> (such as 80-IA, 80-IAC, 80-IBA, 80JJAA and 10AA). Third, <strong>regime elections</strong> that must be made by the due date: Form 10-IC for a company opting into the 22% regime for the first year, and Form 10-IEA for a proprietor opting out of the new regime. "
          "If you are close to the deadline, file on time even if minor schedules need revising later. A <strong>revised return</strong> can fix errors until 31 December 2026."),
    sections=[
        ("/ What depends on filing by the due date", "And what a belated return loses.",
         table(["Item", "Filed by due date", "Filed late (belated, by 31 December 2026)"], [
             ["Business loss carry-forward", "Allowed", "Lost (unabsorbed depreciation can still be carried forward)"],
             ["Profit-linked deductions (section 80AC: 10AA, 80-IA, 80-IAC, 80-IB, 80-IBA, 80JJAA and similar)", "Allowed if conditions are met", "Denied"],
             ["Company opting into section 115BAA for the first year (Form 10-IC)", "Option available", "Option not available for that year"],
             ["Proprietor or HUF with business income opting out of the new regime (Form 10-IEA)", "Old regime available", "Taxed under the default new regime"],
             ["Late fee (section 234F)", "Nil", "Up to INR 5,000 (INR 1,000 if total income is INR 5 lakh or less)"],
             ["Interest (section 234A)", "Nil", "1% per month on unpaid tax from the due date"],
             ["Revising the return later", "Revised return by 31 December 2026", "Revised return by 31 December 2026"]])
         + call_box("a tax return due on 21 or 30 November", ["Whether you can still file on time, and what to file first",
                                                              "Losses, deductions and regime elections at risk",
                                                              "Late fee and interest if you file belatedly",
                                                              "Condonation of delay where the loss is large",
                                                              "Transfer-pricing cases: documentation and penalty exposure"],
                    "your PAN, the tax audit report status, the last filed return and the losses or deductions you claim.")),
        ("/ If you have already missed it", "Options in order.",
         ul("<strong>File the belated return immediately</strong> under section 139(4), by 31 December 2026 at the latest, with the late fee and interest.",
            "<strong>Large losses or deductions at stake:</strong> an application for condonation of delay under section 119(2)(b) can be made, with reasons; relief is discretionary.",
            "<strong>Transfer-pricing cases:</strong> check that Form 3CEB was filed by 31 October 2026; a missing accountant's report carries its own penalty; see <a href=\"form-3ceb-tp-audit-india-2026-30-november-checklist.html\">Form 3CEB checklist</a>.",
            "<strong>After 31 December 2026:</strong> only an updated return is possible (additional tax of 25% to 70%), and it cannot claim a refund or a loss.",
            "<strong>Foreign-owned subsidiaries:</strong> late returns also delay refunds of withholding and can complicate dividend repatriation; see <a href=\"foreign-owned-indian-subsidiary-annual-compliance-calendar-fy-2026-27.html\">subsidiary compliance calendar</a>.")
         + f'<p>Related: <a href="itr-due-date-21-november-2026-audit-cases-cbdt-circular-07-2026.html">ITR due date 21 November 2026</a> &middot; <a href="belated-itr-31-december-2026-section-139-4-india.html">belated return</a> &middot; <a href="revised-itr-section-139-5-deadline-31-december-2026-india.html">revised return</a> &middot; <a href="{DESK}.html">deadline desk to 31 January 2027</a>.</p>'
         + sources("CBDT Circular No. 07/2026; Income-tax Act, 1961 for AY 2026-27 (sections 80, 80AC, 115BAA, 115BAC(6), 119(2)(b), 139(1), 139(3), 139(4), 139(5), 139(8A), 234A, 234F) and Rules (Forms 10-IC, 10-IEA). Case law on loss carry-forward via Taxmann (ITAT and High Court rulings), checked 19-20 November 2026.")),
    ],
    faqs=[("What is the ITR due date for audit cases for AY 2026-27?", "21 November 2026 under CBDT Circular 07/2026; returns for transfer-pricing cases are due 30 November 2026."),
          ("Can business losses be carried forward if the ITR is filed late?", "No. Business losses can be carried forward only if the return is filed by the section 139(1) due date; unabsorbed depreciation can still be carried forward."),
          ("Which deductions are lost if the return is late?", "Deductions covered by section 80AC, such as 10AA and 80-IA, 80-IAC, 80-IB, 80-IBA and 80JJAA, need the return by the due date."),
          ("What happens to Form 10-IC or 10-IEA if I miss the due date?", "A company cannot opt into section 115BAA for that first year without Form 10-IC by the due date, and a proprietor with business income who misses Form 10-IEA is taxed under the new regime for that year."),
          ("What is the late fee for a belated return?", "Up to INR 5,000 under section 234F (INR 1,000 if total income does not exceed INR 5 lakh), plus 1% monthly interest under section 234A on unpaid tax."),
          ("Can BQP file before the deadline?", "Yes. " + C_MS)],
    related=[("itr-due-date-21-november-2026-audit-cases-cbdt-circular-07-2026.html", "ITR due date 21 November 2026"), ("belated-itr-31-december-2026-section-139-4-india.html", "Belated return"),
             (DESK + ".html", "Deadline desk")],
    cta_h="Return due on 21 or 30 November?", cta_b=C_MS,
    keywords="missed ITR due date 21 November 2026, audit case ITR late consequences, business loss carry forward belated return, section 80AC deduction late return, Form 10-IC due date, Form 10-IEA due date, transfer pricing ITR 30 November 2026",
    desc="Missed the 21 Nov 2026 audit ITR (or 30 Nov TP) due date? Belated return by 31 Dec with 234F fee and 234A interest; business loss carry-forward, 80AC deductions and Form 10-IC / 10-IEA elections lost; condonation option; what to do now.",
    howto={"name": "What to do around the 21 and 30 November 2026 ITR deadlines", "description": "Steps for audit and transfer-pricing cases.", "steps": [
        {"name": "File by the due date", "text": "21 November (audit) or 30 November (transfer pricing), even if schedules need revision later."},
        {"name": "File elections with the return", "text": "Form 10-IC or Form 10-IEA by the due date where relevant."},
        {"name": "If missed, file belated", "text": "Section 139(4) return by 31 December 2026 with fee and interest."},
        {"name": "Seek condonation if needed", "text": "Section 119(2)(b) application where large losses or deductions are lost."},
        {"name": "Revise if required", "text": "Revised return by 31 December 2026 for errors."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch DS complete:", len(PAGES))
