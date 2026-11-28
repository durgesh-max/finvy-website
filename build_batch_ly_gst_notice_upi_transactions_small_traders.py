# -*- coding: utf-8 -*-
"""Batch LY (28 Nov 2026): GST notice based on UPI or bank transactions - why small traders and service providers receive them,
registration thresholds, what counts (and does not count) as turnover, exempt goods, how to reply, registering, and composition.
Demand: sweep ac245 (28 Nov 2026), all 7 markets: 'gst notice for upi transaction' (coverage 0.50) - no page on the site (UPI pages
are about fintech integration). The Karnataka notices to small traders in July 2025 made this a nationwide search topic; data-driven
notices from bank and UPI receipts can come in any state. High hire intent. User steer 26 Nov 2026: more call bookings.
Facts (CGST Act sections 22, 23, 24 and 73 / 74A; verified by web search 28 Nov 2026 - Business Standard, Business Today, Deccan
Chronicle, July 2025): tax departments match UPI and bank receipts against GST registration; registration is required once aggregate
turnover crosses INR 40 lakh for those supplying only goods (in most states) or INR 20 lakh for services (lower limits in some special
category states); aggregate turnover counts taxable and exempt supplies but a person supplying only exempt goods or services is not
required to register; personal receipts, loans, transfers between own accounts and refunds are not turnover; in the Karnataka case
officials said the notices proposed registration and payment of tax, interest and penalty, that recipients could reply with
documents, and that exempt items such as vegetables, fruit, milk and meat would not be taxed; the composition scheme offers a lower
rate for eligible small suppliers (site composition page). No fees, no portal menu paths. advisory_lib.contact() is not used."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources
from build_lib import page, write_page

A.UPDATED = "Last updated: 28 November 2026."
SLUG = "gst-notice-for-upi-transactions-small-traders-bank-receipts-registration-threshold-exempt-goods-how-to-reply-2026"

C = ("WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with the notice (all pages), the years and amounts it "
     "mentions, your bank and UPI statements, what you sell (goods, services, exempt items), and any personal or family money "
     "received in the same accounts. Or book a call directly.")
PAGES = [dict(
    slug=SLUG,
    title="GST Notice for UPI Transactions (2026): Why Small Traders Get Them, Registration Thresholds, What Is Not Turnover, Exempt Goods and How to Reply",
    em="UPI receipts are not automatically taxable turnover.",
    kicker="/ Shopkeepers, vendors, freelancers and small service providers &middot; GST notices from UPI and bank data &middot; Updated 2026-11-28",
    lead=("<strong>Tax departments now compare UPI and bank receipts with GST registrations. If your receipts in a year cross the registration threshold - INR 40 lakh for most goods-only businesses, INR 20 lakh for services - you may get a notice proposing registration, tax, interest and penalty. "
          "It is a proposal, not a final demand: personal receipts are not turnover, a person selling only exempt goods such as vegetables or milk need not register, and a documented reply can close or reduce it.</strong>"),
    sections=[
        ("/ What the department looks at - and what it misses", "Turnover vs receipts.",
         table(["Receipt type", "Counts towards GST turnover?"], [
             ["Sales of taxable goods or services", "Yes"],
             ["Sales of exempt goods or services", "Counts in aggregate turnover, but a person supplying only exempt items need not register"],
             ["Money from family, friends or own other accounts", "No - not a supply"],
             ["Loans, refunds, reimbursements, deposits returned", "No"],
             ["Cash sales not seen in UPI data", "Yes - include them in your own working"],
             ["Registration threshold", "INR 40 lakh for goods-only suppliers in most states; INR 20 lakh for services; lower in some special category states"]])
         + ul("<strong>Mixed accounts are the problem:</strong> when business and personal money run through the same UPI ID, the data overstates turnover - separate them in your reply with statements and explanations.",
              "<strong>Several years at once:</strong> these notices often cover multiple financial years; check each year against the threshold separately.")),
        ("/ How to reply", "Before the deadline in the notice.",
         ul("<strong>Read what is proposed:</strong> registration only, or tax, interest and penalty too - and for which years.",
            "<strong>Build a year-wise working:</strong> total receipts, minus personal and non-business credits, split into taxable and exempt sales, compared with the threshold.",
            "<strong>Reply in writing with evidence:</strong> bank and UPI statements, purchase bills, stock records, and proof that items sold are exempt.",
            "<strong>If you were liable:</strong> register, consider the composition scheme if eligible, and pay what is genuinely due - paying tax and interest before a formal show cause notice limits penalty in non-fraud cases.",
            "<strong>Do not just switch to cash:</strong> turnover is taxable however it is received, and cash raises other questions.")
         + call_box("a GST notice based on UPI data", ["Year-wise turnover working",
                                                       "Separating personal and exempt receipts",
                                                       "Written reply and hearing",
                                                       "Registration and composition if liable",
                                                       "Reply to a show cause notice and appeal"],
                    "The notice, bank and UPI statements, what you sell, personal receipts.")
         + sources("CGST Act, 2017 (sections 2(6), 22, 23, 24, 73 and 74A); notifications on the higher threshold for goods suppliers; reports on Karnataka GST notices to small traders based on UPI data (Business Standard, Business Today, Deccan Chronicle, July 2025); site GST registration, composition and GST notice reply pages.")),
    ],
    faqs=[("Why did I get a GST notice for UPI transactions?", "Tax departments compare UPI and bank receipts with GST registrations. If your receipts in a year exceed the registration threshold and you are not registered, the system flags you and a notice proposes registration and tax. The notice is based on receipts, which may include money that is not turnover."),
          ("Is all money received on UPI taxable under GST?", "No. Only consideration for supplies of goods or services is turnover. Money from family or friends, transfers between your own accounts, loans, refunds and reimbursements are not turnover, and exempt goods such as fresh vegetables, fruit and milk are not taxed."),
          ("What is the GST registration limit for small shops and service providers?", "INR 40 lakh of aggregate turnover in a year for those supplying only goods in most states, and INR 20 lakh for services, with lower limits in some special category states. A person supplying only exempt goods or services does not need to register."),
          ("How do I reply to a GST notice based on UPI data?", "Reply in writing before the deadline with a year-wise working that removes personal and non-business receipts and separates exempt sales, supported by bank and UPI statements, purchase bills and stock records. If tax is genuinely due, register and pay it with interest."),
          ("Should I stop accepting UPI payments to avoid GST notices?", "No. Turnover is taxable whether it is received by UPI or in cash, and moving to cash does not change your liability. Keep business and personal receipts in separate accounts instead."),
          ("What should I send to start?", "WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with the notice, the years and amounts mentioned, your bank and UPI statements, what you sell and any personal receipts in the same accounts. Or book a call directly.")],
    related=[("is-gst-registration-mandatory-for-startup-new-small-business-threshold-2026.html", "Is GST registration mandatory?"),
             ("gst-notice-response-india-asmt-drc-gstr.html", "GST notice reply"),
             ("gst-composition-scheme-turnover-limit-1-5-crore-rates-service-providers-6-percent-rules-2026.html", "GST composition scheme"),
             ("income-tax-notice-for-cash-deposit-reply-sft-10-lakh-limit-ais-compliance-portal-section-69a-2026.html", "Income tax notice for cash deposits")],
    cta_h="Got a GST notice over UPI receipts?", cta_b=C,
    keywords="gst notice for upi transaction, gst notice small traders upi, upi transactions gst limit, gst notice based on bank transactions, gst registration threshold 40 lakh 20 lakh, karnataka gst notice upi, reply to gst notice upi",
    desc="GST notice for UPI transactions: departments match UPI and bank receipts with registrations; threshold INR 40 lakh for goods-only suppliers and INR 20 lakh for services; personal receipts are not turnover; exempt goods are not taxed; reply year-wise with evidence; register and consider composition if liable.",
    howto={"name": "How to reply to a GST notice based on UPI data", "description": "Separate, compute, reply.", "steps": [
        {"name": "Read the proposal", "text": "Registration only, or tax, interest and penalty - for which years."},
        {"name": "Separate receipts", "text": "Remove personal and non-business credits; split taxable and exempt sales."},
        {"name": "Compare with the threshold", "text": "Year by year: INR 40 lakh goods / INR 20 lakh services."},
        {"name": "Reply or regularise", "text": "Written reply with evidence; register and pay if genuinely liable."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch LY complete")
