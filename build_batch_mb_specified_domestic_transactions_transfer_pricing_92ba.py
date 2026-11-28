# -*- coding: utf-8 -*-
"""Batch MB (28 Nov 2026): Transfer pricing for domestic transactions - specified domestic transactions (SDT) under section 92BA,
which entities are caught (profit-linked tax holidays, section 115BAB companies), the INR 20 crore threshold, arm's length price,
Form 3CEB, documentation, and how it differs from section 40A(2)(b).
Demand: sweep ac247 (28 Nov 2026), all 7 markets: 'transfer pricing for domestic transactions' (coverage 0.50) - SDT only mentioned
inside the Form 3CEB and subsidiary-setup pages. Companies with tax holidays or concessional regimes need a CA's 3CEB report. User
steer 26 Nov 2026: more call bookings.
Facts (Income-tax Act, 1961 sections 92BA, 92C, 92D, 92E, 40A(2)(b) and the related profit-linked sections; corresponding provisions
of the Income-tax Act, 2025): specified domestic transactions are transactions with related parties or transfers of goods and services
by entities claiming profit-linked deductions (for example under sections 10AA, 80-IA, 80-IAB, 80-IB, 80-IC, 80-IE, referred to via
sections 80A(6) and 80-IA(8) / (10)) and transactions of companies under the concessional section 115BAB regime with closely connected
persons; they are covered only where the aggregate value in the year exceeds INR 20 crore; payments covered only by section 40A(2)(b)
were removed from SDT from AY 2017-18 (Finance Act, 2017); SDT must be at arm's length, documented, and reported in the accountant's
report in Form 3CEB; section 40A(2)(b) separately allows disallowance of excessive payments to related persons. No penalty amounts,
no fees, no due dates invented. advisory_lib.contact() is not used."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources
from build_lib import page, write_page

A.UPDATED = "Last updated: 28 November 2026."
SLUG = "transfer-pricing-domestic-transactions-specified-domestic-transaction-section-92ba-20-crore-form-3ceb-2026"

C = ("WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with the deduction or regime you claim (SEZ, 80-IA, 80-IB, "
     "115BAB or other), the related parties and transactions with them, their values for the year, and your last Form 3CEB if "
     "any. Or book a call directly.")
PAGES = [dict(
    slug=SLUG,
    title="Transfer Pricing for Domestic Transactions (2026): Specified Domestic Transactions Under Section 92BA, the INR 20 Crore Threshold, Who Is Covered and Form 3CEB",
    em="only for tax-holiday and 115BAB-type businesses.",
    kicker="/ Companies with tax holidays, SEZ units and section 115BAB manufacturers &middot; Domestic transfer pricing &middot; Updated 2026-11-28",
    lead=("<strong>Transfer pricing in India is not only for cross-border deals. Section 92BA applies arm&rsquo;s length rules to specified domestic transactions - mainly where a business claims a profit-linked tax holiday or the concessional section 115BAB rate and deals with related parties - once the aggregate value crosses INR 20 crore in a year. "
          "Since 2017, ordinary payments to relatives and group concerns are no longer specified domestic transactions; they are tested only under section 40A(2)(b).</strong>"),
    sections=[
        ("/ What is covered", "Section 92BA.",
         table(["Point", "Rule"], [
             ["Who", "Entities claiming profit-linked deductions (for example SEZ units under 10AA, and deductions under 80-IA, 80-IAB, 80-IB, 80-IC, 80-IE) and companies under section 115BAB"],
             ["Which transactions", "Transfers of goods or services between the eligible unit and other businesses of the same person, and transactions with closely connected or related persons that shift profit into the concessional unit"],
             ["Threshold", "Aggregate value of such transactions above INR 20 crore in the year"],
             ["Not covered since AY 2017-18", "Payments that are covered only by section 40A(2)(b)"],
             ["Requirement", "Arm&rsquo;s length price, documentation, and the accountant&rsquo;s report in Form 3CEB"]])
         + ul("<strong>Why it exists:</strong> to stop profits being moved into a tax-exempt or low-rate unit through prices charged between related businesses.",
              "<strong>Section 40A(2)(b) still applies:</strong> excessive payments to relatives and related concerns can be disallowed even where section 92BA does not apply.")),
        ("/ Compliance and common gaps", "Before the 3CEB is signed.",
         ul("<strong>Map the units and parties:</strong> list the eligible unit, other units of the same person, and closely connected persons, with every transaction between them.",
            "<strong>Test the threshold:</strong> aggregate the year&rsquo;s specified domestic transactions; above INR 20 crore, transfer pricing applies.",
            "<strong>Benchmark:</strong> choose a method under section 92C, document comparables, and keep the records the rules require.",
            "<strong>Report:</strong> include specified domestic transactions in Form 3CEB with the international transactions, if any, by its due date.",
            "<strong>Assessments:</strong> adjustments reduce the tax-holiday profit and can bring penalties for missing documentation or reports.")
         + call_box("specified domestic transactions", ["Checking whether section 92BA applies",
                                                        "Threshold and transaction mapping",
                                                        "Benchmarking and documentation",
                                                        "Form 3CEB reporting",
                                                        "Transfer pricing assessments"],
                    "Deduction or regime claimed, related parties, transaction values, last 3CEB.")
         + sources("Income-tax Act, 1961 (sections 10AA, 40A(2)(b), 80A(6), 80-IA(8) and (10), 92BA, 92C, 92D, 92E and 115BAB) and the corresponding provisions of the Income-tax Act, 2025; Finance Acts 2015 and 2017; site Form 3CEB, transfer pricing and safe harbour pages.")),
    ],
    faqs=[("Does transfer pricing apply to domestic transactions in India?", "Yes, but only to specified domestic transactions under section 92BA - mainly transactions involving businesses that claim profit-linked tax holidays or the concessional section 115BAB regime - where the aggregate value exceeds INR 20 crore in the year."),
          ("What are specified domestic transactions?", "Transactions between a unit claiming a profit-linked deduction (such as an SEZ unit or a unit under section 80-IA or 80-IB) and other businesses of the same person or related persons, and transactions of section 115BAB companies with closely connected persons, that could shift profit into the concessional unit."),
          ("What is the threshold for specified domestic transactions?", "Transfer pricing applies when the aggregate value of specified domestic transactions in the year exceeds INR 20 crore."),
          ("Are payments to related parties under section 40A(2)(b) still specified domestic transactions?", "No. From assessment year 2017-18, payments covered only by section 40A(2)(b) were removed from the definition. They can still be disallowed under section 40A(2)(b) if excessive."),
          ("Do specified domestic transactions need Form 3CEB?", "Yes. They must be reported in the accountant's report in Form 3CEB, along with any international transactions, and supported by transfer pricing documentation."),
          ("What should I send to start?", "WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with the deduction or regime you claim, the related parties and transactions, their values and your last Form 3CEB. Or book a call directly.")],
    related=[("form-3ceb-tp-audit-india-2026-30-november-checklist.html", "Form 3CEB transfer pricing audit checklist"),
             ("best-ca-transfer-pricing-form-3ceb-india.html", "Transfer pricing and Form 3CEB"),
             ("transfer-pricing-safe-harbour-vs-apa-india-2026-15-5-percent-it-services-form-49-advance-pricing-agreement.html", "Safe harbour vs APA"),
             ("related-party-transactions-section-188-companies-act-approval-arms-length-aoc-2-wholly-owned-subsidiary-2026.html", "Related party transactions (section 188)")],
    cta_h="Claiming a tax holiday or the 115BAB rate?", cta_b=C,
    keywords="transfer pricing for domestic transactions, specified domestic transaction section 92ba, sdt threshold 20 crore, domestic transfer pricing india, 115bab closely connected person transfer pricing, form 3ceb sdt, 40a(2)(b) vs 92ba",
    desc="Transfer pricing for domestic transactions: specified domestic transactions under section 92BA for profit-linked tax holiday units and section 115BAB companies, INR 20 crore threshold, 40A(2)(b) payments removed from AY 2017-18, arm's length price, documentation and Form 3CEB.",
    howto={"name": "How to handle specified domestic transactions", "description": "Map, test, document, report.", "steps": [
        {"name": "Map units and parties", "text": "Eligible unit, other units of the same person, closely connected persons."},
        {"name": "Test the threshold", "text": "Aggregate value above INR 20 crore in the year."},
        {"name": "Benchmark and document", "text": "Method under section 92C; comparables and records."},
        {"name": "Report in Form 3CEB", "text": "With international transactions, by its due date."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch MB complete")
