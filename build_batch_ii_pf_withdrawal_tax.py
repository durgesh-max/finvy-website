# -*- coding: utf-8 -*-
"""Batch II (25 Nov 2026): PF withdrawal tax rules 2026 - EPF withdrawal exempt after five years of continuous service
(service with earlier employers counts if the PF was transferred); before five years taxable: employer contribution and
interest on it as salary, employee's own contribution to the extent a deduction was claimed, interest on employee's
contribution as income from other sources; exceptions where termination is due to ill health, closure of the employer's
business or other reasons beyond the employee's control, or where the balance is transferred to a new employer's PF;
TDS (section 192A of the 1961 Act, carried into the 2025 Act) at 10% where the amount is Rs 50,000 or more and service is
under five years, higher rate without PAN; Form 15G / 15H for residents with income below taxable limit; interest on
employee contributions above Rs 2.5 lakh a year (Rs 5 lakh where no employer contribution) taxable annually from
1 April 2021.
Demand: sweep ac110 (25 Nov 2026), all 7 markets: "pf withdrawal tax", "pf withdrawal taxability", "pf withdrawal
taxable or not", "pf withdrawal taxability under which head", "pf withdrawal tax rules", "pf withdrawal tax rate",
"pf withdrawal tax calculator", "pf withdrawal tax free or not".
Facts (checked 25 Nov 2026): Business Today (10 June, 2 July and 29 July 2026), Bajaj Finserv, Angel One, Business
Standard, Cleartax summaries; site NRI EPF withdrawal page (5-year rule, Rs 2.5 lakh limit, heads)."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 25 November 2026."
SLUG = "pf-withdrawal-tax-rules-2026-epf-taxable-or-not-5-years-tds-10-percent-which-head"

C = contact("your total years of PF service (with transfers), the amount you plan to withdraw, the reason for leaving, and whether you claimed 80C on your contributions")
L = lambda h, t: f'<a href="{h}">{t}</a>'
PAGES = [dict(
    slug=SLUG,
    title="PF Withdrawal Tax Rules 2026: Is EPF Withdrawal Taxable, the 5-Year Rule, 10% TDS and Which Head of Income",
    em="five years of service decides almost everything.",
    kicker="/ Salaried employees &middot; Income tax &middot; Updated 2026-11-25",
    lead=("<strong>An EPF withdrawal is tax-free if you have completed five years of continuous service, counting earlier employers whose PF was transferred to the same account.</strong> "
          "If you withdraw before five years, the amount becomes taxable: the employer&rsquo;s contribution and interest on it as salary, your own contribution to the extent you claimed a deduction for it, and interest on your contribution as income from other sources. "
          "EPFO deducts TDS at 10% on a premature withdrawal of &#8377;50,000 or more if you have given your PAN, and at a higher rate without it."),
    sections=[
        ("/ Quick answers", "What people search for.",
         ul("<strong>Is PF withdrawal taxable?</strong> Not after five years of continuous service; yes before that, unless an exception applies.",
            "<strong>Under which head is PF withdrawal taxed?</strong> Employer&rsquo;s contribution and its interest: salary. Your own contribution: salary, only to the extent you claimed a deduction (such as 80C). Interest on your own contribution: income from other sources.",
            "<strong>What is the TDS on PF withdrawal?</strong> 10% where service is under five years and the amount is &#8377;50,000 or more, with PAN; a higher rate without PAN; no TDS below &#8377;50,000, though the amount can still be taxable.",
            "<strong>When is a withdrawal before five years tax-free?</strong> When employment ended due to ill health, closure of the employer&rsquo;s business or another reason beyond your control, or when the balance is transferred to your new employer&rsquo;s PF.",
            "<strong>Can I avoid TDS with Form 15G or 15H?</strong> Residents whose total income is below the taxable limit can submit Form 15G (or 15H if 60 or older); see " + L("form-15g-15h-no-tds-declaration-india-2026.html", "Form 15G / 15H") + ".",
            "<strong>Is PF interest taxable while I am still working?</strong> Interest on your own contributions above &#8377;2.5 lakh a year (&#8377;5 lakh where the employer does not contribute) is taxable every year since 1 April 2021.")),
        ("/ Tax on a premature withdrawal", "Which part goes where.",
         table(["Component", "Head of income", "Notes"], [
             ["Employer contribution", "Salary", "Taxed in the year of withdrawal, with relief for spreading where applicable"],
             ["Interest on employer contribution", "Salary", "Part of the same recomputation"],
             ["Your own contribution", "Salary (deduction reversed)", "Only to the extent you claimed 80C"],
             ["Interest on your contribution", "Income from other sources", "Taxed at your slab rate"]])
         + '<p>After five years of continuous service, all of these are exempt. Compare regimes with the ' + L("new-vs-old-tax-regime-calculator.html", "new vs old regime calculator") + '; for TDS on salary see ' + L("tds-on-salary-section-392-old-192-rates-limit-calculation-form-130-2026-27.html", "TDS on salary 2026-27") + '.</p>'),
        ("/ Before you withdraw", "Practical checks.",
         ul("<strong>Transfer, do not withdraw:</strong> moving the balance to a new employer keeps the service continuous and the money tax-free later.",
            "<strong>Check service years:</strong> make sure earlier PF accounts are transferred into your UAN so the five-year count is correct.",
            "<strong>Link PAN:</strong> without PAN, TDS is higher.",
            "<strong>Report in your return:</strong> taxable PF withdrawals and the TDS appear in your tax credit statement; match them in the ITR.",
            "<strong>Moving abroad?</strong> See " + L("nri-epf-pf-withdrawal-process-online-tax-form-19-15g-2026.html", "EPF withdrawal for NRIs") + " and " + L("epf-scheme-2026-changes-employers-foreign-subsidiaries-nri-withdrawal-12-months-wages-definition.html", "EPF Scheme 2026 changes") + ".")
         + call_box("PF withdrawal tax", ["Taxability check before withdrawal",
                                           "TDS and Form 15G / 15H",
                                           "ITR reporting of PF withdrawal",
                                           "Transfer vs withdrawal planning",
                                           "NRI PF withdrawals"],
                    "your service history and the withdrawal amount.")
         + sources("Income-tax Act, 1961 (exemption for accumulated balance after five years of continuous service; section 192A TDS) and the corresponding provisions of the Income-tax Act, 2025; Business Today (10 June, 2 July and 29 July 2026), Bajaj Finserv, Angel One, Business Standard and Cleartax summaries. Checked 25 November 2026.")),
    ],
    faqs=[("Is PF withdrawal taxable?", "Not if you have completed five years of continuous service, including earlier employers whose PF was transferred. A withdrawal before five years is taxable unless employment ended due to ill health, closure of the employer's business or another reason beyond your control."),
          ("Under which head is PF withdrawal taxed?", "On a taxable withdrawal, the employer's contribution and interest on it are taxed as salary, your own contribution is taxed as salary to the extent you claimed a deduction for it, and interest on your own contribution is taxed as income from other sources."),
          ("What is the TDS rate on PF withdrawal?", "10% where service is under five years and the withdrawal is Rs 50,000 or more, if PAN is furnished; a higher rate applies without PAN. No TDS is deducted below Rs 50,000, but the amount may still be taxable."),
          ("Is PF withdrawal after 5 years tax-free?", "Yes. After five years of continuous service the entire withdrawal, including interest, is exempt, apart from interest on employee contributions above the Rs 2.5 lakh yearly limit, which is taxed each year."),
          ("Can I submit Form 15G to avoid TDS on PF withdrawal?", "Yes, if you are resident and your total income including the withdrawal is below the taxable limit; seniors aged 60 or more use Form 15H. NRIs cannot use these forms."),
          ("Can BQP help with PF withdrawal tax?", "Yes. CA Durgesh Chavda can check whether your withdrawal is taxable, plan transfer versus withdrawal and report it correctly in your return. " + C)],
    related=[("nri-epf-pf-withdrawal-process-online-tax-form-19-15g-2026.html", "EPF withdrawal for NRIs"),
             ("form-15g-15h-no-tds-declaration-india-2026.html", "Form 15G / 15H"),
             ("epf-scheme-2026-changes-employers-foreign-subsidiaries-nri-withdrawal-12-months-wages-definition.html", "EPF Scheme 2026 changes"),
             ("tds-on-salary-section-392-old-192-rates-limit-calculation-form-130-2026-27.html", "TDS on salary 2026-27"),
             ("new-vs-old-tax-regime-calculator.html", "New vs old regime calculator")],
    cta_h="Planning a PF withdrawal?", cta_b=C,
    keywords="PF withdrawal tax, PF withdrawal taxable or not, EPF withdrawal taxability, PF withdrawal under which head, TDS on PF withdrawal 192A, PF withdrawal before 5 years tax, PF withdrawal tax rules 2026, PF withdrawal Form 15G",
    desc="PF withdrawal tax rules 2026: EPF withdrawal tax-free after 5 years of continuous service; before that taxed as salary and other sources, TDS 10% on Rs 50,000+, exceptions, Form 15G / 15H, interest above Rs 2.5 lakh.",
    howto={"name": "How to check if your PF withdrawal is taxable", "description": "Before submitting the claim.", "steps": [
        {"name": "Count continuous service", "text": "Include earlier employers whose PF was transferred."},
        {"name": "Check exceptions", "text": "Ill health, business closure or reasons beyond your control."},
        {"name": "Split the components", "text": "Employer share, your share, and interest on each."},
        {"name": "Plan TDS", "text": "Link PAN; residents below the limit can use Form 15G / 15H."},
        {"name": "Report in the ITR", "text": "Show taxable parts under the right heads and claim TDS."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch II complete")
