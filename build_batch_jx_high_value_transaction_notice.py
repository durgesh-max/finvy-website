# -*- coding: utf-8 -*-
"""Batch JX (27 Nov 2026): Income tax 'high value transaction' notices - credit card spending, cash deposits, fixed
deposits, shares and mutual funds, property and foreign currency reported in the SFT - and how to reply.
Demand: sweep ac141 (27 Nov 2026), all 7 markets: "high value transactions notice", "... reply", "... reply format",
"... reply meaning", "... reply pdf", "what is high value transaction", "high value transaction notice from income tax",
"income tax notice for credit card spending / usage", "income tax rules on credit card usage", "is foreign inward
remittance taxable"; no page covered high value transaction or credit card notices.
User steer 26 Nov 2026: more call bookings / WhatsApp enquiries - explaining a reported transaction usually needs a CA.
Facts (verified 27 Nov 2026): banks, card issuers, registrars, fund houses and companies report specified transactions
in the Statement of Financial Transactions (rule 114E of the 1962 Rules and the corresponding Income-tax Rules, 2026 from
1 April 2026); credit card bill payments of Rs 1 lakh or more in cash or Rs 10 lakh or more by any mode in a financial
year; cash deposits of Rs 10 lakh or more in savings accounts (higher limit for current accounts); time deposits of Rs 10
lakh or more; purchases of shares, mutual fund units, bonds or debentures of Rs 10 lakh or more; immovable property of
Rs 30 lakh or more (Rs 45 lakh from 1 April 2026, site fact - stated as reported); foreign currency sales of Rs 10 lakh
or more. Reported items show in the AIS; mismatches lead to compliance portal / e-campaign queries, section 133(6)
letters or, for older years, 148A; unexplained money under 69 / 69A / 69C taxed under 115BBE at about 78% (site fact).
Remittances from abroad: tax depends on the nature (NRI's own savings, gift from a relative, salary, business receipts).
No fees, no timings, no office claims."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 27 November 2026."
SLUG = "high-value-transaction-notice-income-tax-credit-card-spending-sft-limits-how-to-reply-2026"

C = contact("the notice or the compliance portal message (screenshot or PDF), your AIS for that year, the statement or record of the transaction flagged (card statements, bank statements, contract notes, sale deed or forex invoice), and what paid for it - salary, business income, savings, a loan, a gift or money from abroad")
PAGES = [dict(
    slug=SLUG,
    title="High Value Transaction Notice from Income Tax (2026): Credit Card Spending, the SFT Limits, Why It Comes and How to Reply",
    em="show what paid for it.",
    kicker="/ Salaried people, business owners, investors and NRIs with Indian accounts &middot; AIS and compliance portal &middot; Updated 2026-11-27",
    lead=("<strong>A 'high value transaction' notice means a bank, card issuer, fund house, registrar or other reporting entity told the Income Tax Department about a large transaction in your name - and your return does not seem to explain how you paid for it.</strong> "
          "The usual triggers are credit card bills of Rs 10 lakh or more in a year, large cash deposits, fixed deposits, share or mutual fund purchases, property deals and foreign currency purchases. "
          "Most cases close once you show the source - salary, business income, savings, a loan or a gift - with documents, and reply on time."),
    sections=[
        ("/ What gets reported", "The Statement of Financial Transactions limits.",
         table(["Transaction", "Reported when, in a financial year"], [
             ["Credit card bill payments", "Rs 1 lakh or more paid in cash, or Rs 10 lakh or more paid by any mode"],
             ["Cash deposits", "Rs 10 lakh or more in savings accounts (a higher limit applies to current accounts)"],
             ["Fixed / time deposits", "Rs 10 lakh or more"],
             ["Shares, mutual funds, bonds, debentures", "Purchases of Rs 10 lakh or more"],
             ["Immovable property", "Purchase or sale of Rs 30 lakh or more, reported as raised to Rs 45 lakh from 1 April 2026"],
             ["Foreign currency", "Purchases, including forex card loads and travellers' cheques, of Rs 10 lakh or more"]])
         + ul("<strong>Where it shows:</strong> reported transactions appear in your Annual Information Statement (AIS).",
              "<strong>Why a notice follows:</strong> the department compares the AIS with your return; if spending or investment is high against declared income, or the return was not filed, it asks you to explain.")),
        ("/ How to reply", "Point by point, with documents.",
         ul("<strong>Find the transaction</strong> in your AIS and check it is yours, correctly reported and not duplicated - an add-on card, a joint account or a family member's investment can be reported against you.",
            "<strong>Compliance portal query:</strong> give feedback against each transaction - for example the information is correct and already covered in the return, relates to another person, or is duplicate - and add your explanation.",
            "<strong>Show the source:</strong> salary credits, business receipts, savings built over earlier years, a loan, sale of an asset, or a gift from a relative with a gift deed and the giver's bank record.",
            "<strong>Credit card bills:</strong> link the card payments to your bank account and show that account is funded from declared income; business expenses on a personal card should be backed by books or reimbursement records.",
            "<strong>Section 133(6) letter or 148A notice:</strong> reply on the e-filing portal within the time given, with a covering explanation and the supporting papers.",
            "<strong>If income was missed:</strong> a revised return (until 31 December 2026 for this year, with a fee after that up to 31 March 2027) or an updated return may be the cleaner route before a notice escalates.")),
        ("/ What happens if it is not explained", "Why the reply matters.",
         ul("Unexplained investments, money or expenditure can be added under sections 69, 69A or 69C and taxed under section 115BBE at about 78% including surcharge and cess, with penalty exposure on top.",
            "Ignoring a compliance query or a section 133(6) letter can lead to a reassessment notice under section 148A.",
            "NRIs: large remittances or investments in India are usually explained by income earned abroad or savings - keep the foreign bank statements and remittance records ready.")
         + call_box("High value transaction notices", ["Reading the AIS and spotting reporting errors",
                                                         "Compliance portal responses",
                                                         "Section 133(6) and 148A replies",
                                                         "Revised or updated return where income was missed",
                                                         "NRI remittances and family gifts"],
                    "The notice, AIS and transaction records.")
         + sources("Income-tax Act (sections 69, 69A, 69C, 115BBE, 133(6), 148A, 285BA) and the corresponding provisions of the Income-tax Act, 2025; rule 114E (Statement of Financial Transactions) and the Income-tax Rules, 2026; Income Tax Department guidance on reporting of high-value transactions; AIS and compliance portal guidance; site cash deposit, property purchase notice, AIS mismatch and 148A guides. Checked 27 November 2026.")),
    ],
    faqs=[("What is a high value transaction notice from income tax?", "A query or notice asking you to explain a large transaction that a bank, card issuer, fund house, registrar or other entity reported in the Statement of Financial Transactions - such as credit card bills, cash deposits, fixed deposits, share or mutual fund purchases, property or foreign currency - because your return does not seem to account for it."),
          ("Can I get an income tax notice for credit card spending?", "Yes. Credit card bill payments of Rs 10 lakh or more in a financial year by any mode, or Rs 1 lakh or more in cash, are reported to the department and appear in your AIS. If your declared income does not support that spending, you may be asked to explain how the bills were paid."),
          ("How do I reply to a high value transaction notice?", "Check the transaction in your AIS, confirm it is yours and correctly reported, then explain the source with documents - salary, business income, savings, a loan, an asset sale or a documented gift. On the compliance portal give feedback against each transaction; for a section 133(6) or 148A notice, reply on the e-filing portal within the time given. There is no fixed format, but a point-by-point reply with papers works best."),
          ("What are the high value transaction limits for income tax reporting?", "In a financial year: credit card bills of Rs 1 lakh in cash or Rs 10 lakh by any mode; cash deposits of Rs 10 lakh in savings accounts (higher for current accounts); fixed deposits of Rs 10 lakh; share, mutual fund, bond or debenture purchases of Rs 10 lakh; property of Rs 30 lakh, reported as raised to Rs 45 lakh from 1 April 2026; and foreign currency purchases of Rs 10 lakh."),
        ("Can the income tax department see or track my bank account?", "Not in real time, but it sees a great deal. Banks report interest through TDS statements, and large transactions through the Statement of Financial Transactions, such as cash deposits adding up to INR 10 lakh or more in a year in savings accounts (INR 50 lakh in current accounts), fixed deposits of INR 10 lakh or more, and large credit card bill payments. All of this is linked to your PAN and shows up in your AIS, and mismatches with your return trigger e-campaign emails or notices. During an assessment or search the department can also ask a bank for full statements. Book a call if an AIS entry or a bank-related notice does not match your records."),
          ("Is money received from abroad taxable in India?", "It depends on what the money is. An NRI's own savings sent home, or a gift from a relative, is generally not taxable; salary, business receipts or fees for services can be. Large inward remittances can be reported and questioned, so keep the foreign bank statements and the reason for the transfer."),
        ("Is buying gold taxable, and do I show it in my return?", "Buying gold is not taxed in itself - what matters is that the money used can be explained from income or savings, because large purchases can be reported and questioned. Sellers must collect your PAN for cash purchases of Rs 2 lakh or more and cannot accept Rs 2 lakh or more in cash from one person for one transaction. Individuals with total income above Rs 1 crore report jewellery and bullion in Schedule AL. When you sell gold, the gain is a capital gain - long-term after 24 months, taxed at 12.5% without indexation."),
          ("What should I send to reply to a high value transaction notice?", "WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with the notice or portal message, your AIS for that year, the statement or record of the flagged transaction, and what paid for it - salary, business income, savings, a loan, a gift or money from abroad. We check the reporting, prepare the explanation and file the response. You keep your own e-filing login."),
          ("Can BQP handle high value transaction notices for NRIs and families?", "Yes. CA Durgesh Chavda works online with salaried people, business owners, investors and NRIs with Indian accounts. " + C)],
    related=[("income-tax-notice-for-cash-deposit-reply-sft-10-lakh-limit-ais-compliance-portal-section-69a-2026.html", "Cash deposit notices"),
             ("income-tax-notice-for-property-land-purchase-why-you-got-it-how-to-reply-source-of-funds-2026.html", "Property purchase notices"),
             ("ais-mismatch-itr-what-to-do-feedback-revised-return-31-december-2026-e-campaign-nri.html", "AIS mismatch and e-campaigns"),
             ("how-to-respond-to-income-tax-notice-india.html", "How to respond to an income tax notice"),
             ("section-148-148a-reassessment-notice-response-india.html", "Section 148 / 148A reassessment")],
    cta_h="Got a high value transaction notice?", cta_b=C,
    keywords="high value transaction notice, high value transactions notice reply, income tax notice for credit card spending, income tax notice credit card usage, sft limits income tax, what is high value transaction, high value transaction notice reply format",
    desc="High value transaction notices from income tax: the SFT limits for credit card bills, cash deposits, fixed deposits, shares and mutual funds, property and foreign currency, how they reach your AIS, how to reply on the compliance portal or to a 133(6) / 148A notice, and what to send.",
    howto={"name": "How to reply to a high value transaction notice", "description": "From the AIS entry to a documented reply.", "steps": [
        {"name": "Check the AIS", "text": "Find the reported transaction and confirm it is yours and correctly reported."},
        {"name": "Trace the source", "text": "Match it to salary, business income, savings, a loan, an asset sale or a gift."},
        {"name": "Collect proof", "text": "Bank and card statements, contract notes, sale deeds, gift deeds or remittance records."},
        {"name": "Reply on time", "text": "Respond on the compliance portal or to the notice with the explanation and documents."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch JX complete")
