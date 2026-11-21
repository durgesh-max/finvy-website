# -*- coding: utf-8 -*-
"""Batch FI (21 Nov 2026): Does a foreign company have to file an income-tax return in India? Call-first page.
Demand: sweep 21 Nov 2026 (ac42), all 7 markets: "is foreign company required to file income tax return in india",
"is a non resident required to file income tax return in india", "does foreigner need to file tax return". No page on
the site answered it directly.
Facts (checked 21 Nov 2026):
- Income Tax Department guidance "Taxation of Non-Residents" (March 2026 edition): a non-resident files a return where
  income is taxable in India; filing is not required where the only income is specified income (dividend, interest,
  royalty, fees for technical services) and tax has been deducted at not less than the statutory rate; otherwise filing
  is required even though TDS was deducted.
- Section 115A(5) of the 1961 Act (carried into the 2025 Act): the exemption needs TDS at rates not lower than the
  section 115A rates (20% for royalty and FTS since the Finance Act, 2023). Commentary (LKS, TaxGuru, others) is divided
  on whether withholding at a lower treaty rate keeps the exemption; the cautious and common practice is to file.
- A foreign company with a branch, project office or other permanent establishment files a full return (ITR-6), with
  tax audit and transfer-pricing report where applicable; business income rate 35% plus surcharge and cess (site pages).
- Capital gains on Indian shares or assets, refund claims and loss carry-forward need a return.
- A foreign company with international transactions with an Indian associated enterprise that give it income taxable
  in India is within the transfer-pricing report requirement (Form 3CEB for FY 2025-26; due 31 October, return 30 Nov).
- Liaison office: no income, annual statement in Form 49C (site page).
- Due dates: company returns 31 October; 30 November where a transfer-pricing report is required; belated return by
  31 December (FY 2025-26: 31 December 2026), late fee INR 5,000, or INR 1,000 where total income is up to INR 5 lakh."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 21 November 2026."
SLUG = "does-foreign-company-need-to-file-income-tax-return-in-india-royalty-fees-dividend-capital-gains-itr-6-2026"

C = contact("the foreign company's country, what it earned from India in the year (fees, royalty, interest, dividend, share sale), the tax deducted and at what rate, and whether it has any office or staff in India")
PAGES = [dict(
    slug=SLUG,
    title="Does a Foreign Company Have to File an Income-Tax Return in India? (2026) Royalty, Service Fees, Dividends, Share Sales, Branches and the 31 December Belated Date",
    em="when TDS is the end of the matter, and when it is not.",
    kicker="/ Foreign companies &middot; Income tax &middot; Returns &middot; Updated 2026-11-21",
    lead=("<strong>A foreign company must file an Indian income-tax return for any year in which it has income taxable in India, unless a narrow exemption applies.</strong> "
          "The exemption covers a company whose <strong>only</strong> Indian income is dividends, interest, royalties or technical service fees, and only where tax was deducted at the <strong>full domestic rate</strong>. "
          "If tax was deducted at a <strong>lower treaty rate</strong>, the cautious and usual practice is to file. "
          "A return is also needed for a <strong>branch, project office or other permanent establishment</strong>, for <strong>capital gains</strong> on Indian shares or assets, and to <strong>claim a refund</strong> of excess TDS. "
          "TDS deducted by the Indian customer does not by itself remove the duty. "
          "For the year to 31 March 2026, a company that has not yet filed can still file a <strong>belated return by 31 December 2026</strong>."),
    sections=[
        ("/ By situation", "Is a return needed?",
         table(["Situation of the foreign company", "Indian return?", "Notes"], [
             ["Only royalty, service fees, interest or dividends from India; TDS at the full domestic rate", "No", "The exemption applies"],
             ["Same income, but TDS at a lower treaty rate", "Yes, in practice", "The exemption wording requires the domestic rate; most advisers file"],
             ["Branch, project office or other permanent establishment in India", "Yes", "Full company return with audited accounts; transfer-pricing report where it applies"],
             ["Sold shares of an Indian company or other Indian assets", "Yes", "Capital gains are reported even if the buyer deducted tax"],
             ["Wants a refund of excess TDS, or to carry forward a loss", "Yes", "Neither is possible without a return"],
             ["Income that it treats as exempt under a treaty (for example business income with no permanent establishment)", "Usually advisable", "Views differ; filing protects the treaty claim and starts the time limits running"],
             ["Liaison office only, no income", "No income return", "Annual statement of activities is filed instead"],
             ["No income from India and no presence", "No", "Nothing to report"]])
         + call_box("Indian tax return for a foreign company", ["Whether your company had to file for FY 2025-26 and earlier years",
                                                                 "Filing a belated return before 31 December 2026",
                                                                 "Getting a PAN, portal registration and digital signature in place",
                                                                 "Claiming a refund of excess TDS",
                                                                 "Notices for returns not filed in past years"],
                    "the company&rsquo;s country, its Indian income and the tax deducted, any office or staff in India, and whether it holds a PAN.")),
        ("/ How filing works", "Forms, dates and what you need.",
         ul("<strong>Form:</strong> companies, including foreign companies, file ITR-6 online.",
            "<strong>Due date:</strong> 31 October after the financial year ends on 31 March. It is 30 November if a transfer-pricing report is required. For FY 2025-26, audit cases were extended to 21 November 2026.",
            "<strong>Late filing:</strong> a belated return can be filed until 31 December following the year, with a late fee of INR 5,000 (INR 1,000 if total income is up to INR 5 lakh) and interest on any tax due. See <a href=\"belated-itr-31-december-2026-section-139-4-india.html\">belated returns</a>.",
            "<strong>What you need:</strong> an Indian PAN, registration on the income-tax portal, a digital signature for the authorised signatory, the TDS statement (Form 26AS / AIS), contracts and invoices, and a tax residency certificate with Form 41 if a treaty is claimed.",
            "<strong>Transfer pricing:</strong> a foreign company that earns royalty, fees or interest from its own Indian subsidiary is itself within the transfer-pricing report requirement for that income. See <a href=\"form-3ceb-tp-audit-india-2026-30-november-checklist.html\">the transfer-pricing report</a>.",
            "<strong>Rates:</strong> royalties, service fees, interest and dividends at the treaty or domestic rate on the gross amount; business income of a branch or permanent establishment at 35% plus surcharge and cess on net profit.")),
        ("/ Practical points", "What goes wrong.",
         ul("<strong>&ldquo;Our customer deducted tax, so we are done&rdquo;:</strong> true only if the full domestic rate was used and that is your only Indian income.",
            "<strong>Dividends from an Indian subsidiary at the treaty rate:</strong> the parent is usually expected to file.",
            "<strong>Mismatch notices:</strong> the tax department sees payments to you in the payer&rsquo;s TDS filings. A PAN with reported income and no return draws a notice.",
            "<strong>Refunds:</strong> where a customer deducted at 20% plus surcharge and cess although a 10% or 15% treaty rate applied, the excess comes back only through a return.",
            "<strong>Past years:</strong> if returns were missed, review the position before a notice arrives; options narrow with time.",
            "<strong>Liaison offices</strong> file an annual statement and not an income return. See <a href=\"liaison-office-branch-office-annual-activity-certificate-aac-form-49c-162-india-2026.html\">liaison and branch office annual filings</a>.")
         + '<p>Related: <a href="no-pe-declaration-india-format-sample-foreign-vendor-trc-form-41-10f-what-indian-customers-ask-for-2026.html">no-PE declaration and vendor documents</a> &middot; <a href="tds-on-payment-to-foreign-company-calculator-royalty-fts-interest-dividend-treaty-rates-2026.html">TDS on payments to foreign companies</a> &middot; <a href="tds-on-purchase-of-shares-from-non-resident-nri-foreign-company-unlisted-listed-rate-section-393-195-india-2026.html">TDS on share sales by non-residents</a> &middot; <a href="foreign-company-remote-employee-india-pe-risk-eor-contractor-subsidiary-2026.html">PE risk</a> &middot; <a href="deadline-desk-20-november-2026-to-31-january-2027-income-tax-gst-roc-nri-foreign-companies.html">deadlines to 31 January 2027</a>.</p>'
         + sources("Income Tax Department, &ldquo;Taxation of Non-Residents&rdquo; (March 2026 edition); Income-tax Act provisions on the duty to file a return, the filing exemption for non-residents with only dividend, interest, royalty or technical-service income taxed at source (section 115A(5) of the 1961 Act and its successor), transfer-pricing report and belated returns; commentary by Lakshmikumaran &amp; Sridharan and TaxGuru on foreign companies&rsquo; filing obligation. Checked 21 November 2026. Views differ on returns where a treaty rate or treaty exemption is used; this page takes the cautious position.")),
    ],
    faqs=[("Is a foreign company required to file an income-tax return in India?", "Yes, for any year in which it has income taxable in India, unless its only Indian income is dividends, interest, royalties or technical service fees and tax was deducted at the full domestic rate. A branch, permanent establishment, capital gains or a refund claim always needs a return."),
          ("If TDS has been deducted, does a foreign company still need to file?", "Often yes. TDS alone does not remove the duty. The exemption applies only to specified income taxed at source at the full domestic rate; where a lower treaty rate was used, the usual practice is to file."),
          ("Which ITR form does a foreign company file in India?", "ITR-6, filed online with a digital signature. The company needs an Indian PAN and registration on the income-tax portal."),
          ("What is the due date for a foreign company's return in India?", "31 October after the financial year, or 30 November where a transfer-pricing report is required. A belated return can be filed until 31 December; for FY 2025-26 that is 31 December 2026."),
          ("Does a foreign parent receiving dividends from its Indian subsidiary have to file?", "If tax was deducted at a treaty rate lower than the domestic rate, the parent is usually expected to file a return. If the full domestic rate was deducted and that is its only Indian income, the exemption applies."),
          ("Does a liaison office file an income-tax return?", "A liaison office earns no income in India, so it files an annual statement of its activities and not an income return."),
          ("Can BQP file the Indian return for a foreign company?", "Yes. " + C)],
    related=[("no-pe-declaration-india-format-sample-foreign-vendor-trc-form-41-10f-what-indian-customers-ask-for-2026.html", "No-PE declaration and vendor documents"),
             ("belated-itr-31-december-2026-section-139-4-india.html", "Belated return by 31 December 2026"),
             ("tds-on-payment-to-foreign-company-calculator-royalty-fts-interest-dividend-treaty-rates-2026.html", "TDS on payments to foreign companies: calculator")],
    cta_h="Foreign company with income from India and no return filed?", cta_b=C,
    keywords="is foreign company required to file income tax return in India, foreign company ITR India, does non resident need to file income tax return in India, section 115A(5) exemption, ITR-6 foreign company, foreign company royalty FTS return India, belated return foreign company 31 December 2026",
    desc="Does a foreign company have to file an income-tax return in India (2026)? Yes if it has India-taxable income, unless its only income is dividends, interest, royalty or service fees with TDS at the full domestic rate. Treaty-rate cases, branches, share sales, refunds, ITR-6, due dates.",
    howto={"name": "How a foreign company checks and files its Indian return", "description": "Steps.", "steps": [
        {"name": "List Indian income", "text": "Fees, royalty, interest, dividends, share sales, branch profits."},
        {"name": "Check the exemption", "text": "Only specified income, with TDS at the full domestic rate."},
        {"name": "Get set up", "text": "PAN, portal registration and digital signature."},
        {"name": "File ITR-6", "text": "By 31 October, or 30 November with a transfer-pricing report."},
        {"name": "If late", "text": "File a belated return by 31 December with the late fee."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch FI complete")
