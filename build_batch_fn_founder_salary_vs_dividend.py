# -*- coding: utf-8 -*-
"""Batch FN (23 Nov 2026): Founder salary vs dividend in India - how a founder of a private limited company should take
money out, tax on each route, the loan-to-founder trap, and NRI founders. Call-first.
Demand: sweep 22 Nov 2026 (ac44, founders), all 7 markets: "founder salary in india", "ceo salary in india" variants;
no page on the site covered founder pay.
Facts (checked 23 Nov 2026):
- New regime slabs unchanged for tax year 2026-27: nil to INR 4 lakh, 5% 4-8, 10% 8-12, 15% 12-16, 20% 16-20, 25% 20-24,
  30% above 24 lakh; rebate up to INR 60,000 makes income up to INR 12 lakh tax-free; standard deduction INR 75,000 for
  salaried (Budget 2026 reports: Moneylife, Business Today, ClearTax).
- Dividend TDS threshold INR 10,000 a year (Finance Act 2025, from 1 April 2025). From April 2026 no deduction for
  interest against dividend income (ClearTax summary of 2026 changes). Surcharge on dividend income capped at 15%.
- Company tax under the 22% regime about 25.17% effective; dividends are paid from post-tax profit and are not deductible.
- Salary and director remuneration are deductible for the company, subject to the related-party rule that lets the
  officer disallow payments that are excessive for the services (section 40A(2) of the 1961 Act, carried forward).
- Managerial remuneration limits in section 197 of the Companies Act, 2013 apply to public companies, not private ones.
- Loans or advances by a company to a shareholder with 10% or more of voting power (or to a concern in which the
  shareholder is substantially interested) are taxed as deemed dividend to the extent of accumulated profits (section
  2(22)(e) of the 1961 Act; carried into the 2025 Act's definition of dividend).
- Non-resident founders: salary for work done outside India is generally not taxable in India; director's fees from an
  Indian company are taxable in India under treaty directors' fees articles; dividends to non-residents 20% plus
  surcharge and cess or the treaty rate (site TDS calculator page).
Illustration uses only these rates; it is arithmetic, not a firm figure."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 23 November 2026."
SLUG = "founder-salary-vs-dividend-india-private-limited-company-tax-director-remuneration-deemed-dividend-nri-founder-2026"

C = contact("the company's expected profit this year, each founder's shareholding and other income, whether the company is on the 22% regime or claiming the startup tax holiday, and whether any founder lives outside India")
L = lambda h, t: f'<a href="{h}">{t}</a>'
PAGES = [dict(
    slug=SLUG,
    title="Founder Salary vs Dividend in India (2026): How Founders of a Private Limited Company Should Pay Themselves - Tax on Each Route, Loans to Founders and NRI Founders",
    em="salary is usually cheaper; dividends are taxed twice.",
    kicker="/ Startups &middot; Founders &middot; Tax &middot; Updated 2026-11-23",
    lead=("<strong>For most Indian startup founders, a salary is the cheaper way to take money out of a private limited company.</strong> "
          "Salary is a deductible expense for the company, so the profit paid out is taxed once, in the founder&rsquo;s hands, at slab rates. "
          "A dividend is paid out of profit that has <strong>already been taxed in the company at about 25%</strong>, and is then <strong>taxed again</strong> at the founder&rsquo;s slab rate. "
          "Under the new regime, income up to <strong>INR 12 lakh</strong> a year is tax-free after the rebate, and salaried founders also get a INR 75,000 standard deduction. "
          "Two things to avoid: a salary so large the tax officer calls it excessive for the work, and <strong>borrowing from your own company</strong>, which can be taxed as a deemed dividend. "
          "Founders living abroad follow different rules on salary, director&rsquo;s fees and dividends."),
    sections=[
        ("/ Salary, dividend or both", "How each route is taxed.",
         table(["", "Salary or director remuneration", "Dividend"], [
             ["Company&rsquo;s tax", "Deductible, so it reduces the company&rsquo;s taxable profit", "Not deductible: paid from profit after company tax of about 25.17% (22% regime)"],
             ["Founder&rsquo;s tax", "Slab rates; new regime: nil up to INR 4 lakh, up to 30% above INR 24 lakh; rebate makes income up to INR 12 lakh tax-free; INR 75,000 standard deduction", "Slab rates, with surcharge capped at 15%; no standard deduction; from April 2026 no deduction for interest against it"],
             ["Tax at source", "Company deducts TDS monthly", "10% TDS above INR 10,000 a year"],
             ["Paperwork", "Payroll, TDS returns, Form 16 (Form 130 from tax year 2026-27)", "Board (and for a final dividend, shareholder) approval, distributable profits"],
             ["Limits", "Must be reasonable for the work; Companies Act limits on managerial pay apply to public companies, not private ones", "Only out of profits; paid to all shareholders of the class in proportion"],
             ["Best for", "Founders working in the business, especially in early profitable years", "Investors, founders with high other income, or after the startup tax holiday when retained profit is large"]])
         + '<p><strong>Illustration, new regime, no other income:</strong> the company has INR 10 lakh of profit before paying the founder. <strong>As salary:</strong> the company pays no tax on it; the founder&rsquo;s taxable income is INR 9.25 lakh after the standard deduction, below INR 12 lakh, so no tax: the founder keeps INR 10 lakh. <strong>As dividend:</strong> the company first pays about INR 2.52 lakh of tax; the founder receives about INR 7.48 lakh, also tax-free after the rebate. Salary leaves the founder about INR 2.5 lakh better off.</p>'
         + call_box("How should the founders pay themselves this year?", ["Salary, dividend or a mix for each founder",
                                                                          "Effect of the 22% regime or the startup tax holiday",
                                                                          "Founders with loans from the company, and how to clear them",
                                                                          "Founders living abroad: what India taxes",
                                                                          "Board approvals, payroll and TDS"],
                    "expected profit, each founder&rsquo;s shareholding and other income, your tax regime and where each founder lives.")),
        ("/ Traps", "Where founders get caught.",
         ul("<strong>Loans from the company:</strong> a loan or advance to a shareholder holding 10% or more of the votes, or to a business in which that shareholder has a substantial interest, is taxed as a <strong>deemed dividend</strong> to the extent of the company&rsquo;s accumulated profits, even if it is repaid. Pay a salary or declare a dividend instead.",
            "<strong>Excessive salary:</strong> payments to related persons that are excessive for the services can be disallowed in the company&rsquo;s return. Document the role and keep pay in line with the business.",
            "<strong>Startup tax holiday years:</strong> if the company&rsquo;s profit is tax-free under " + L("startup-tax-holiday-section-80-iac-now-section-140-eligibility-imb-certificate-mat-115baa-2026.html", "the startup tax holiday") + ", the double-tax argument against dividends weakens, but minimum alternate tax still applies to the company.",
            "<strong>Investors:</strong> a dividend goes to every shareholder of the class; founders cannot take a dividend alone. Salary is the founder-only route.",
            "<strong>ESOPs and sweat equity</strong> are a separate route with their own tax timing; see the " + L("esop-perquisite-tax-calculator.html", "ESOP tax calculator") + ".",
            "<strong>Old or new regime:</strong> compare both each year with the " + L("new-vs-old-tax-regime-calculator.html", "regime calculator") + ".")),
        ("/ Founders living outside India", "NRI and foreign founders of Indian companies.",
         ul("<strong>Salary for work done abroad:</strong> generally not taxable in India for a non-resident. Salary for days worked in India can be.",
            "<strong>Director&rsquo;s fees:</strong> fees paid by an Indian company to a director are generally taxable in India under the directors&rsquo; fees article of tax treaties, wherever the director lives.",
            "<strong>Dividends:</strong> taxed in India at 20% plus surcharge and cess, or the lower treaty rate with a tax residency certificate and Form 41; see the " + L("tds-on-payment-to-foreign-company-calculator-royalty-fts-interest-dividend-treaty-rates-2026.html", "withholding calculator") + ". Your home country taxes them too, with credit.",
            "<strong>Loans:</strong> lending to the company from abroad has its own FEMA rules; see " + L("loan-from-nri-director-shareholder-to-indian-company-ecb-2026-rules.html", "loans from NRI directors") + ".",
            "<strong>Residence:</strong> spending long periods in India can make you resident and taxable on world income; check with the " + L("residential-status-calculator-india-nri-rnor-section-6.html", "residential status calculator") + ".")
         + '<p>Related: ' + L("how-to-pick-section-115baa-vs-115bab-vs-standard-decision-tree.html", "choosing the company&rsquo;s tax regime") + ' &middot; ' + L("founder-vesting-india-us-startup.html", "founder vesting") + ' &middot; ' + L("how-to-start-a-startup-in-india.html", "starting a startup in India") + '.</p>'
         + sources("Income-tax Act, 2025 and Income-tax Act, 1961 provisions on salary, dividends (including the deemed dividend rule in section 2(22)(e) of the 1961 Act), related-party payments (section 40A(2) of the 1961 Act) and the concessional company regime; new regime slabs, rebate and standard deduction for tax year 2026-27 as reported after Budget 2026 (Moneylife, Business Today, ClearTax); dividend TDS threshold of INR 10,000 (Finance Act, 2025); Companies Act, 2013, section 197. Checked 23 November 2026. The illustration is arithmetic on these rates; surcharge, other income and the old regime change the result.")),
    ],
    faqs=[("Is it better for a founder to take salary or dividend in India?", "Usually salary. Salary is deductible for the company, so the profit is taxed once in the founder's hands. A dividend comes out of profit already taxed at about 25% in the company and is taxed again at the founder's slab rate."),
          ("How much salary can a founder take from a private limited company?", "Company law does not cap managerial pay in a private company. For tax, the salary must be reasonable for the work done, because excessive payments to related persons can be disallowed in the company's return."),
          ("How are dividends taxed for a founder in India?", "At the founder's slab rate, with surcharge capped at 15% and no standard deduction. The company deducts 10% TDS where dividends exceed INR 10,000 in a year."),
          ("Can a founder take a loan from their own company?", "It is risky. A loan or advance to a shareholder with 10% or more of the voting power is taxed as a deemed dividend to the extent of the company's accumulated profits, even if repaid."),
          ("Is a founder's salary tax-free up to INR 12 lakh?", "Under the new regime, total income up to INR 12 lakh is tax-free after the rebate, and salaried founders also deduct INR 75,000, so salary up to about INR 12.75 lakh with no other income pays no tax."),
          ("How is an NRI founder of an Indian company taxed on salary and dividends?", "Salary for work done outside India is generally not taxable in India. Director's fees from the Indian company generally are. Dividends are taxed in India at 20% plus surcharge and cess or the lower treaty rate, and again at home with credit."),
          ("Can BQP plan founder pay for our company?", "Yes. " + C)],
    related=[("startup-tax-holiday-section-80-iac-now-section-140-eligibility-imb-certificate-mat-115baa-2026.html", "Startup tax holiday"),
             ("new-vs-old-tax-regime-calculator.html", "New vs old regime calculator"),
             ("esop-perquisite-tax-calculator.html", "ESOP tax calculator")],
    cta_h="Deciding how the founders get paid?", cta_b=C,
    keywords="founder salary India, founder salary vs dividend, director remuneration private limited company, how should founders pay themselves India, dividend tax India founder, deemed dividend loan to director, NRI founder salary tax India, CEO salary tax India startup",
    desc="Founder salary vs dividend in India (2026): salary is deductible and taxed once at slab rates (income up to INR 12 lakh tax-free under the new regime); dividends come from profit taxed at about 25% and are taxed again. Deemed dividend on loans to founders, excessive salary, and NRI founders.",
    howto={"name": "How founders decide between salary and dividend", "description": "Each year.", "steps": [
        {"name": "Estimate company profit", "text": "And whether the company is on the 22% regime or the startup tax holiday."},
        {"name": "Look at each founder's income", "text": "Other income, residence and the new or old regime."},
        {"name": "Set a reasonable salary", "text": "Deductible for the company; document the role."},
        {"name": "Use dividends for the rest", "text": "Out of profits, to all shareholders of the class."},
        {"name": "Clear founder loans", "text": "Avoid deemed dividend on loans and advances."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch FN complete")
