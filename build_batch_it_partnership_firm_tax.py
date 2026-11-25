# -*- coding: utf-8 -*-
"""Batch IT (25 Nov 2026): partnership firm taxation in India 2026 - flat 30% on total income (no slabs, no basic
exemption, no 87A), 12% surcharge above Rs 1 crore, 4% cess; partner interest deductible up to 12% simple and
remuneration within section 40(b) limits (Finance (No. 2) Act, 2024 from AY 2025-26: first Rs 6 lakh of book profit or
a loss - higher of Rs 3 lakh or 90%; balance - 60%); partner's share of profit exempt (10(2A)), remuneration and
interest taxable in the partner's hands; TDS 10% on partner payments under 194T from 1 April 2025; tax audit at Rs 1
crore turnover (Rs 10 crore if cash within 5%) / Rs 50 lakh profession; 44AD / 44ADA available to firms (not LLPs);
ITR-5, due 31 July (no audit) / 31 October (audit) / 30 November (transfer pricing); PAN in the firm's name.
Demand: sweep ac114 (25 Nov 2026), all 7 markets: "partnership firm tax rate", "partnership firm tax slab",
"partnership firm audit limit", "partnership firm itr due date", "partnership firm pan card", "partnership firm itr form".
Facts (checked 25 Nov 2026): Bajaj Finserv (FY 2025-26 slab page), ITAT Online Budget 2024 note on 40(b), Taxguru,
Tally, CAclubindia, Taxmann (194T); site pages on 194T, tax audit and 44AD."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 25 November 2026."
SLUG = "partnership-firm-tax-rate-india-2026-30-percent-40b-remuneration-audit-limit-itr-5-due-date"

C = contact("the firm's turnover and book profit, partners' capital and remuneration in the deed, whether accounts are audited, and the year you need to file for")
L = lambda h, t: f'<a href="{h}">{t}</a>'
PAGES = [dict(
    slug=SLUG,
    title="Partnership Firm Tax Rate in India 2026: Flat 30%, No Slabs, Partner Remuneration Limit (40(b)), Audit Limit, ITR-5 and Due Dates",
    em="a flat 30% from the first rupee, so partner pay planning matters.",
    kicker="/ Partnership firms and partners &middot; Income tax &middot; Updated 2026-11-25",
    lead=("<strong>A partnership firm in India pays a flat 30% income tax on its total income, plus a 12% surcharge if income exceeds &#8377;1 crore and 4% cess; there are no slabs and no basic exemption.</strong> "
          "Interest on partners' capital (up to 12%) and remuneration within the section 40(b) limits are deductible for the firm and taxed in the partners' hands, while each partner's share of profit is tax-free. "
          "Firms file ITR-5, by 31 July if not audited or 31 October if a tax audit applies."),
    sections=[
        ("/ Tax at a glance", "Firms and LLPs.",
         table(["Point", "Rule"], [
             ["Tax rate", "30% flat; surcharge 12% if income above &#8377;1 crore; 4% cess"],
             ["Slabs / basic exemption / 87A", "Not available to firms"],
             ["Interest to partners", "Deductible up to 12% simple a year, if the deed allows"],
             ["Remuneration to working partners", "First &#8377;6 lakh of book profit (or a loss): higher of &#8377;3 lakh or 90%; balance: 60%"],
             ["Partner's share of profit", "Exempt in the partner's hands"],
             ["TDS on partner payments", "10% under section 194T (from 1 April 2025)"],
             ["Presumptive taxation", "44AD / 44ADA available to partnership firms (not LLPs)"],
             ["Return", "ITR-5; due 31 July (no audit), 31 October (audit), 30 November (transfer pricing)"]])
         + '<p>See ' + L("section-194t-tds-partnership-firm-partners-india.html", "section 194T TDS on partners") + ' and ' + L("best-ca-section-44ad-44ada-presumptive-scheme-india.html", "presumptive taxation (44AD / 44ADA)") + '.</p>'),
        ("/ Worked example (illustrative)", "Firm with book profit of Rs 20 lakh before partner remuneration.",
         table(["Item", "Amount"], [
             ["Book profit", "&#8377;20,00,000"],
             ["Allowable remuneration: 90% of first Rs 6 lakh + 60% of Rs 14 lakh", "&#8377;5,40,000 + &#8377;8,40,000 = &#8377;13,80,000"],
             ["Taxable income of firm", "&#8377;6,20,000"],
             ["Firm tax at 30% + 4% cess", "&#8377;1,93,440"],
             ["Remuneration taxed in partners' hands", "At their own slab rates"]])
         + '<p>Remuneration must be authorised by the partnership deed and paid to working partners; amounts above the limit are disallowed. Partners can often pay less overall under their own slabs than the firm&rsquo;s flat 30%.</p>'),
        ("/ Audit, PAN and filing", "Compliance checklist.",
         ul("<strong>Tax audit:</strong> required if business turnover exceeds &#8377;1 crore (&#8377;10 crore if cash receipts and payments are each within 5%) or professional receipts exceed &#8377;50 lakh; see " + L("form-3ca-3cb-3cd-tax-audit-india-2026-checklist.html", "tax audit checklist") + ".",
            "<strong>PAN:</strong> the firm needs its own PAN, applied for with the partnership deed; registration with the Registrar of Firms is separate; see " + L("partnership-firm-registration-india-online-documents-certificate-form-1-registrar-of-firms-2026.html", "partnership firm registration") + ".",
            "<strong>Advance tax:</strong> firms pay advance tax in four instalments if tax exceeds &#8377;10,000.",
            "<strong>Alternate minimum tax:</strong> firms claiming certain profit-linked deductions may pay AMT instead of regular tax.",
            "<strong>Firm or LLP:</strong> both are taxed at 30%; an LLP gives limited liability but cannot use 44AD / 44ADA; see " + L("llp-registration-india-2026-process-documents-fillip-designated-partner-nri-foreign-partner.html", "LLP registration") + ".")
         + call_box("Firm taxation", ["Partner remuneration and interest planning",
                                       "Tax audit and ITR-5",
                                       "194T TDS on partners",
                                       "Firm vs LLP vs company",
                                       "Partnership deed review"],
                    "your firm's accounts and deed.")
         + sources("Income-tax Act, 1961 sections 10(2A), 40(b), 44AB, 44AD, 44ADA and 194T, Finance (No. 2) Act, 2024 and First Schedule rates, carried into the Income-tax Act, 2025; Bajaj Finserv, ITAT Online, Taxguru, Tally, CAclubindia and Taxmann commentary; site guides on 194T, tax audit and presumptive taxation. Checked 25 November 2026.")),
    ],
    faqs=[("What is the income tax rate for a partnership firm in India?", "A flat 30% on total income, plus a 12% surcharge where income exceeds Rs 1 crore and 4% health and education cess. Firms do not get income tax slabs, the basic exemption limit or the section 87A rebate."),
          ("How much remuneration can a partnership firm pay its partners?", "Under section 40(b), as revised from AY 2025-26: on the first Rs 6 lakh of book profit (or a loss), the higher of Rs 3 lakh or 90% of book profit; on the balance, 60%. Interest on capital is allowed up to 12% simple. The deed must authorise both."),
          ("What is the audit limit for a partnership firm?", "A tax audit is needed if business turnover exceeds Rs 1 crore, or Rs 10 crore where cash receipts and payments are each within 5%, or if professional receipts exceed Rs 50 lakh."),
          ("Which ITR form and due date apply to a partnership firm?", "ITR-5. It is due by 31 July if the accounts are not audited, 31 October if a tax audit applies, and 30 November where transfer pricing applies."),
          ("Is a partner's share of profit taxable?", "No. A partner's share of the firm's profit is exempt in the partner's hands. Remuneration and interest received from the firm are taxable as business income of the partner."),
          ("Can BQP handle partnership firm tax and audit?", "Yes. CA Durgesh Chavda can plan partner remuneration, run the tax audit, file ITR-5 and manage 194T TDS. " + C)],
    related=[("section-194t-tds-partnership-firm-partners-india.html", "Section 194T TDS on partners"),
             ("partnership-firm-registration-india-online-documents-certificate-form-1-registrar-of-firms-2026.html", "Partnership firm registration"),
             ("form-3ca-3cb-3cd-tax-audit-india-2026-checklist.html", "Tax audit checklist"),
             ("best-ca-section-44ad-44ada-presumptive-scheme-india.html", "Presumptive taxation"),
             ("llp-registration-india-2026-process-documents-fillip-designated-partner-nri-foreign-partner.html", "LLP registration")],
    cta_h="Running a partnership firm?", cta_b=C,
    keywords="partnership firm tax rate, partnership firm tax slab, partnership firm audit limit, partnership firm itr due date, partnership firm itr form, section 40(b) remuneration limit, partner remuneration calculation, partnership firm income tax 2026",
    desc="Partnership firm tax in India 2026: flat 30% plus surcharge and cess, no slabs, partner remuneration under section 40(b) (Rs 6 lakh / 90% / 60% from AY 2025-26), interest up to 12%, 194T TDS, audit limits, ITR-5 and due dates, worked example.",
    howto={"name": "How a partnership firm's tax is computed", "description": "Regular provisions.", "steps": [
        {"name": "Compute book profit", "text": "Profit before partner remuneration, after interest allowed up to 12%."},
        {"name": "Apply the 40(b) limit", "text": "90% of the first Rs 6 lakh (minimum Rs 3 lakh), 60% of the rest."},
        {"name": "Tax the firm at 30%", "text": "Plus surcharge above Rs 1 crore and 4% cess."},
        {"name": "Deduct TDS on partner payments", "text": "10% under section 194T."},
        {"name": "File ITR-5", "text": "By 31 July, or 31 October if audited."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch IT complete")
