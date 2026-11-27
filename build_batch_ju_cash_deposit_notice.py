# -*- coding: utf-8 -*-
"""Batch JU (27 Nov 2026): Income tax notice for cash deposits - why it comes, the bank reporting limits, how to reply on
the compliance portal or to a notice, and what happens if the source is not explained.
Demand: sweep ac138 (27 Nov 2026), all 7 markets: "income tax notice for cash deposit", "income tax notice cash deposit
limit", "reply to income tax notice for cash deposit", "income tax notice on cash deposit in bank", "do i have to pay
taxes on cash deposits"; no page covered cash deposit notices.
User steer 26 Nov 2026: more call bookings / WhatsApp enquiries - explaining the source of cash usually needs a CA.
Facts (verified 27 Nov 2026): banks report large cash deposits in the Statement of Financial Transactions (SFT) - cash
deposits of Rs 10 lakh or more in a financial year in savings accounts, with a higher limit for current accounts; the
reported amount appears in the AIS; a mismatch with the return leads to an e-campaign / compliance portal query, a section
133(6) letter or, for older years, a 148A reassessment notice; unexplained money is taxed under section 69A read with
115BBE at about 78% with surcharge and cess (site fact); cash receipts of Rs 2 lakh or more from a person in a day / for a
transaction are barred by section 269ST (old) and cash loans of Rs 20,000 or more by 269SS (site facts). Exact current-
account threshold basis not restated. No fees, no timings, no office claims."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 27 November 2026."
SLUG = "income-tax-notice-for-cash-deposit-reply-sft-10-lakh-limit-ais-compliance-portal-section-69a-2026"

C = contact("the notice or the compliance portal message (screenshot or PDF), your AIS for that year, bank statements showing the cash deposits, and whatever explains the cash - sales records, withdrawals redeposited, gift deeds, sale of an asset, agricultural or other income")
PAGES = [dict(
    slug=SLUG,
    title="Income Tax Notice for Cash Deposit (2026): Why It Comes, the Rs 10 Lakh Bank Reporting Limit, How to Reply on the Compliance Portal and Avoid Section 69A Tax",
    em="explain the source before it becomes income.",
    kicker="/ Individuals, traders, families and NRIs with Indian accounts &middot; AIS and compliance portal &middot; Updated 2026-11-27",
    lead=("<strong>An income tax notice for cash deposits usually starts with your bank's report: large cash deposits are reported in the Statement of Financial Transactions, show up in your Annual Information Statement (AIS), and the department asks you to explain them if your return does not.</strong> "
          "Most cases are settled by showing where the cash came from - business sales, money withdrawn earlier and redeposited, a documented gift or the sale of an asset. "
          "If the source is not explained, the deposit can be taxed as unexplained money under section 69A at about 78% including surcharge and cess."),
    sections=[
        ("/ Why the notice comes", "How the department finds the cash.",
         table(["Step", "What happens"], [
             ["Bank reports", "Cash deposits of Rs 10 lakh or more in a financial year in savings accounts (a higher limit applies to current accounts) are reported in the Statement of Financial Transactions"],
             ["AIS shows it", "The reported amount appears in your Annual Information Statement for that year"],
             ["Mismatch check", "If your return does not show income or sources that match, the system flags it"],
             ["Query or notice", "An e-campaign or compliance portal query, a section 133(6) letter asking for details, or for older years a reassessment notice under section 148A"]])),
        ("/ How to reply", "Show the source, with papers.",
         ul("<strong>Compliance portal query:</strong> give feedback against the transaction - for example the information is correct and already covered in the return, relates to someone else, or is duplicated - and add the explanation and documents.",
            "<strong>Business cash:</strong> link deposits to sales in your books, GST returns and cash book.",
            "<strong>Redeposited withdrawals or savings:</strong> show earlier withdrawals from your accounts and why the cash was held.",
            "<strong>Gifts and family money:</strong> a gift from a relative is exempt, but keep a gift deed and the giver's bank or source evidence.",
            "<strong>Sale of an asset or other income:</strong> sale deed, receipts, agricultural income records or similar.",
            "<strong>If the return missed income:</strong> a revised or updated return may be the cleaner route before a notice escalates.")),
        ("/ If it is not explained", "Why a careful reply matters.",
         ul("Unexplained money can be added under section 69A and taxed under section 115BBE at about 78% including surcharge and cess, with penalty exposure on top.",
            "Separate rules restrict cash itself: receiving Rs 2 lakh or more in cash from one person in a day or for one transaction, and taking or repaying loans or deposits of Rs 20,000 or more in cash, carry penalties equal to the amount.",
            "Reply within the time given; ignoring a section 133(6) letter or a portal query can lead to reassessment.")
         + call_box("Cash deposit notices", ["Reading the AIS and the bank's report",
                                             "Compliance portal responses",
                                             "Section 133(6) and 148A replies",
                                             "Revised or updated return where income was missed",
                                             "NRI accounts and family gifts"],
                    "The notice, AIS and bank statements.")
         + sources("Income-tax Act (sections 69A, 115BBE, 133(6), 148A, 269SS, 269ST) and the corresponding provisions of the Income-tax Act, 2025; SFT reporting rules; AIS and compliance portal guidance; site notice reply, AIS mismatch and 148A guides. Checked 27 November 2026.")),
    ],
    faqs=[("Why did I get an income tax notice for a cash deposit?", "Banks report large cash deposits - Rs 10 lakh or more in a financial year in savings accounts, with a higher limit for current accounts - in the Statement of Financial Transactions. The amount shows in your AIS, and if your return does not explain it, the department asks for the source through the compliance portal, a section 133(6) letter or a reassessment notice."),
          ("What is the cash deposit limit in a savings account to avoid an income tax notice?", "There is no limit on depositing your own explained money, but cash deposits of Rs 10 lakh or more in a financial year in savings accounts are reported to the department. Deposits below that can still be questioned if they do not match your income."),
          ("How do I reply to an income tax notice for cash deposit?", "Explain the source with documents: business sales linked to your books and GST returns, earlier withdrawals redeposited, a documented gift from a relative, sale of an asset, or other income. On the compliance portal give feedback against the transaction and attach the explanation; for a section 133(6) or 148A notice, reply on the e-filing portal within the time given."),
          ("What happens if I cannot explain a cash deposit?", "It can be added as unexplained money under section 69A and taxed under section 115BBE at about 78% including surcharge and cess, and penalty can follow. Where income was simply left out of the return, a revised or updated return may limit the damage."),
        ("What is the penalty under section 271AAC on unexplained income?", "Where income is added as unexplained cash credits, investments, money or expenditure (sections 68 to 69D) and taxed under section 115BBE, a further penalty of 10% of that tax can be levied under section 271AAC, on top of the tax at 60% plus surcharge and cess (about 78%). It does not apply to the extent the income was declared in the return and the tax paid before the end of the year. The Income-tax Act, 2025 has corresponding provisions from 1 April 2026."),
          ("Do I have to pay tax on cash deposits?", "Not on the deposit itself. Tax depends on what the money is - business income, salary already taxed, a gift from a relative or savings are treated differently - but you need to be able to show the source if asked."),
          ("What should I send to reply to a cash deposit notice?", "WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with the notice or portal message, your AIS for the year, bank statements showing the deposits, and whatever explains the cash - sales records, earlier withdrawals, gift deeds, sale documents or other income. We prepare the explanation and file the response. You keep your own e-filing login."),
          ("Can BQP handle cash deposit notices for NRIs and families?", "Yes. CA Durgesh Chavda works online with individuals, traders, families and NRIs with Indian accounts. " + C)],
    related=[("ais-mismatch-itr-what-to-do-feedback-revised-return-31-december-2026-e-campaign-nri.html", "AIS mismatch and e-campaigns"),
             ("how-to-respond-to-income-tax-notice-india.html", "How to respond to an income tax notice"),
             ("section-148-148a-reassessment-notice-response-india.html", "Section 148 / 148A reassessment"),
             ("revised-itr-section-139-5-deadline-31-december-2026-india.html", "Revised ITR"),
             ("itr-u-updated-return-48-months-section-139-8a-india.html", "Updated return (ITR-U)")],
    cta_h="Got a notice about cash deposits?", cta_b=C,
    keywords="income tax notice for cash deposit, reply to income tax notice for cash deposit, cash deposit limit income tax, income tax notice cash deposit in bank, sft cash deposit 10 lakh, section 69a unexplained money, ais cash deposit",
    desc="Income tax notice for cash deposits: how banks report deposits of Rs 10 lakh or more in the SFT and AIS, how to reply on the compliance portal or to a 133(6) / 148A notice with proof of source, and the section 69A / 115BBE tax if it is not explained.",
    howto={"name": "How to reply to an income tax notice for cash deposits", "description": "From the AIS entry to a documented reply.", "steps": [
        {"name": "Check the AIS", "text": "Find the reported cash deposits and the bank that reported them."},
        {"name": "Trace the source", "text": "Match each deposit to sales, withdrawals, gifts, asset sales or other income."},
        {"name": "Collect proof", "text": "Books, GST returns, bank statements, gift deeds or sale documents."},
        {"name": "Reply on time", "text": "Respond on the compliance portal or to the notice with the explanation and documents."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch JU complete")
