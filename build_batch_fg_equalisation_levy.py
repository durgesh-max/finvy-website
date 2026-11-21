# -*- coding: utf-8 -*-
"""Batch FG (21 Nov 2026): Equalisation levy in India - abolished; what it was, when each part ended and what foreign
digital companies and their Indian customers deal with now. Call-first page.
Demand: sweep 21 Nov 2026 (ac42), all 7 markets, coverage 0.00: "equalisation levy india", "equalisation levy abolished
in india", "what is equalisation levy", "equalisation levy rate in india", "equalisation levy applicability in india",
"does india have digital services tax".
Facts (checked 21 Nov 2026):
- 6% levy on online advertisement services: Finance Act, 2016, from 1 June 2016; deducted by the Indian payer where
  payments to a non-resident exceeded INR 1 lakh a year; abolished for consideration on or after 1 April 2025 by the
  Finance Act, 2025 (Business Standard, India Briefing, Digital Policy Alert).
- 2% levy on non-resident e-commerce operators: Finance Act, 2020, from 1 April 2020; threshold INR 2 crore of Indian
  sales; paid by the operator; abolished from 1 August 2024 by the Finance (No. 2) Act, 2024.
- Section 10(50) exemption (income that bore the levy was exempt from income tax) given a sunset by the Finance Act,
  2025 and not carried into the Income-tax Act, 2025 (IndiaFilings and other commentary).
- After abolition: ordinary rules - section 9 (business connection, significant economic presence: INR 2 crore of
  payments or 3 lakh users, site SEP page), treaties (permanent establishment), royalty / fees for technical services
  characterisation, withholding under section 393 (old 195), GST reverse charge and OIDAR registration (site pages)."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 21 November 2026."
SLUG = "equalisation-levy-india-abolished-6-percent-2-percent-what-applies-now-foreign-digital-companies-2026"
SEP = "significant-economic-presence-foreign-saas-app-company-india-2-crore-3-lakh-users-2026.html"

C = contact("what you sell into India or buy from abroad (ads, software, a marketplace, cloud), the foreign company's country, yearly Indian revenue or spend, and whether there are people or an entity in India")
PAGES = [dict(
    slug=SLUG,
    title="Equalisation Levy in India: Abolished (2026) - the 6% Ad Levy Ended 1 April 2025, the 2% E-Commerce Levy Ended 1 August 2024, and What Applies Now",
    em="India no longer has a digital services tax.",
    kicker="/ Foreign companies &middot; Digital &middot; Tax &middot; Updated 2026-11-21",
    lead=("<strong>India has abolished the equalisation levy.</strong> "
          "The <strong>2% levy on foreign e-commerce operators ended on 1 August 2024</strong>, and the <strong>6% levy on online advertising paid to foreign companies ended on 1 April 2025</strong>. "
          "India therefore has no digital services tax today. "
          "That does not mean Indian revenue of a foreign digital business is tax-free. It now falls under the ordinary rules: whether the foreign company has a <strong>permanent establishment</strong> or a <strong>significant economic presence</strong> in India, whether the payment is a <strong>royalty or technical service fee</strong>, and whether the Indian customer must <strong>withhold tax</strong>. "
          "<strong>GST still applies</strong>: Indian businesses pay it under reverse charge on imported services, and foreign companies selling digital services to Indian consumers must register. "
          "Levy dues and filings for the years before abolition can still be examined."),
    sections=[
        ("/ What it was and when it ended", "The two levies.",
         table(["", "6% levy (online advertising)", "2% levy (e-commerce)"], [
             ["Started", "1 June 2016", "1 April 2020"],
             ["Charged on", "Payments by Indian businesses to non-residents for online advertising and ad space", "Sales of goods and services into India by non-resident e-commerce operators"],
             ["Threshold", "Payments above INR 1 lakh a year to one non-resident", "Indian sales above INR 2 crore a year"],
             ["Who paid it to the government", "The Indian payer, by deducting it from the payment", "The foreign operator, every quarter"],
             ["Ended", "1 April 2025 (Finance Act, 2025)", "1 August 2024 (Finance (No. 2) Act, 2024)"]])
         + '<p>Income that bore the levy was exempt from Indian income tax. With the levy gone, that exemption has ended too, so the income is tested under the normal income-tax rules.</p>'
         + call_box("Digital revenue from India, or payments to foreign platforms", ["Whether your Indian revenue is taxable in India now that the levy is gone",
                                                                                   "Withholding on ad, software, cloud and marketplace payments abroad",
                                                                                   "Treaty protection: tax residency certificate, Form 41 and a no-PE declaration",
                                                                                   "GST: reverse charge for Indian buyers, registration for foreign sellers",
                                                                                   "Old equalisation levy periods: notices, statements and refunds"],
                    "what is sold or bought, the foreign company&rsquo;s country, yearly Indian revenue or spend, and any people or entity in India.")),
        ("/ What applies now", "For foreign sellers and Indian buyers.",
         ul("<strong>Foreign company in a treaty country, no presence in India:</strong> business income is taxable in India only through a permanent establishment. To rely on the treaty it needs a tax residency certificate and Form 41 (formerly Form 10F), and customers usually ask for a no-PE declaration.",
            "<strong>Foreign company with no treaty protection:</strong> the significant economic presence rule can tax it without any physical presence: payments from India above INR 2 crore a year, or 3 lakh Indian users. See <a href=\"" + SEP + "\">significant economic presence</a>.",
            "<strong>Royalty or technical service fee:</strong> software licences, some cloud and platform fees and support services may be classed this way and taxed on the gross amount, usually at 10% to 15% under a treaty. See the <a href=\"tds-on-payment-to-foreign-company-calculator-royalty-fts-interest-dividend-treaty-rates-2026.html\">TDS calculator for payments to foreign companies</a>.",
            "<strong>Indian business buying ads from a foreign platform:</strong> the 6% deduction has stopped for payments from 1 April 2025. The payer must still decide whether income-tax withholding applies and keep the vendor&rsquo;s documents; the bank asks for Form 145 and, where needed, Form 146.",
            "<strong>GST:</strong> an Indian business pays 18% GST under reverse charge on imported services and normally claims it as credit. A foreign company supplying online services to Indian consumers registers and pays GST itself.",
            "<strong>Past years:</strong> levy for periods before abolition, the annual levy statement and any interest remain open to scrutiny. An Indian payer that did not deduct the 6% levy in those years can have the expense disallowed.")),
        ("/ Practical points", "Common questions from finance teams.",
         ul("<strong>Is anything due on ad spend with foreign platforms in 2026?</strong> No equalisation levy. Check income-tax withholding once per vendor, and account for GST under reverse charge.",
            "<strong>Did abolition make foreign platforms cheaper?</strong> Where the platform had added the 6% to invoices, that cost has gone. Contracts with a gross-up clause should be checked.",
            "<strong>Does the old exemption still protect us?</strong> No. Income that used to be exempt because the levy was paid is now looked at afresh.",
            "<strong>Selling to Indian consumers through an app or marketplace:</strong> income tax depends on treaty and presence; GST registration depends on what is supplied and to whom. See <a href=\"best-ca-oidar-gst-foreign-saas-india-2026.html\">GST for foreign online service providers</a>.",
            "<strong>An Indian subsidiary or team changes the answer:</strong> people in India who sell or conclude contracts can create a permanent establishment. See the <a href=\"foreign-company-remote-employee-india-pe-risk-eor-contractor-subsidiary-2026.html\">PE risk guide</a>.")
         + '<p>Related: <a href="fees-for-technical-services-fts-taxability-india-make-available-treaty-withholding-2026.html">fees for technical services</a> &middot; <a href="income-tax-act-2025-section-195-now-393-what-changed-nri-foreign.html">section 195 is now section 393</a> &middot; <a href="technology-licensing-royalty-payment-indian-company-to-foreign-company-fema-tds-gst-2026.html">royalty and licence payments abroad</a> &middot; <a href="for-foreign-clients.html">services for foreign clients</a>.</p>'
         + sources("Finance Act, 2016, Chapter VIII (equalisation levy from 1 June 2016); Finance Act, 2020 (2% levy from 1 April 2020); Finance (No. 2) Act, 2024 (2% levy withdrawn from 1 August 2024); Finance Act, 2025 (6% levy withdrawn from 1 April 2025; sunset of the related income-tax exemption); Income-tax Act, 2025, section 9 (significant economic presence) and section 393 (withholding on payments to non-residents); IGST Act provisions on import of services and online services; reports by Business Standard, India Briefing and Digital Policy Alert. Checked 21 November 2026. General information; the position for a business depends on its contracts and treaty.")),
    ],
    faqs=[("Is the equalisation levy still applicable in India?", "No. The 2% levy on non-resident e-commerce operators was withdrawn from 1 August 2024 and the 6% levy on online advertising from 1 April 2025. No equalisation levy applies to transactions after those dates."),
          ("What was the equalisation levy rate in India?", "6% on payments to non-residents for online advertising (from 1 June 2016 to 31 March 2025) and 2% on sales into India by non-resident e-commerce operators (from 1 April 2020 to 31 July 2024)."),
          ("Does India have a digital services tax?", "Not any more. With the equalisation levy abolished, foreign digital businesses are taxed in India only under the ordinary income-tax rules, such as permanent establishment, significant economic presence and royalty or technical service fees, plus GST on the supply."),
          ("Do Indian companies still deduct 6% on payments to Google or Meta entities abroad?", "No, not for payments from 1 April 2025. The payer should still check whether income-tax withholding applies, keep the vendor's tax residency certificate and Form 41, and pay GST under reverse charge."),
          ("How is a foreign digital company taxed in India after the equalisation levy?", "If it is resident in a treaty country and has no permanent establishment in India, its business income is generally not taxed here. Without treaty protection, significant economic presence can apply above INR 2 crore of Indian payments or 3 lakh users. Royalties and technical service fees are taxed on the gross amount at treaty or domestic rates."),
          ("Can old equalisation levy periods still be questioned?", "Yes. Levy, statements and interest for periods before abolition can be examined, and an Indian payer that failed to deduct the 6% levy in those years risks disallowance of the expense."),
          ("Can BQP advise on Indian tax for a foreign digital business?", "Yes. " + C)],
    related=[(SEP, "Significant economic presence for foreign SaaS and app companies"),
             ("tds-on-payment-to-foreign-company-calculator-royalty-fts-interest-dividend-treaty-rates-2026.html", "TDS on payments to foreign companies: calculator"),
             ("best-ca-oidar-gst-foreign-saas-india-2026.html", "GST for foreign online service providers")],
    cta_h="Selling digital services into India, or paying foreign platforms?", cta_b=C,
    keywords="equalisation levy India, equalisation levy abolished in India, what is equalisation levy, equalisation levy rate in India, equalisation levy applicability, does India have digital services tax, Google tax India, 6% equalisation levy online advertisement, 2% equalisation levy e-commerce",
    desc="Equalisation levy in India is abolished: the 2% e-commerce levy ended 1 August 2024 and the 6% online advertising levy ended 1 April 2025. What applies now to foreign digital companies and Indian payers: PE, significant economic presence, royalty/FTS withholding and GST.",
    howto={"name": "How to check Indian tax on digital revenue after the equalisation levy", "description": "For a foreign seller or Indian payer.", "steps": [
        {"name": "Confirm the dates", "text": "No 2% levy from 1 August 2024; no 6% levy from 1 April 2025."},
        {"name": "Check treaty and presence", "text": "Tax residency certificate, Form 41 and whether there is a permanent establishment."},
        {"name": "Classify the payment", "text": "Business income, royalty or technical service fee."},
        {"name": "Decide withholding", "text": "Under section 393, with Form 145 and 146 for the bank."},
        {"name": "Handle GST", "text": "Reverse charge for Indian business buyers; registration for foreign sellers to consumers."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch FG complete")
