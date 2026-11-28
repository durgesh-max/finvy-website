# -*- coding: utf-8 -*-
"""Batch KV (28 Nov 2026): Can the income tax department see my bank account - what banks report, how it reaches your AIS, and
when officers ask for full statements.
Demand: sweep ac235 (28 Nov 2026), all 7 markets: 'can income tax department see my bank account', 'can income tax department
track my bank account', 'how to check bank account details in income tax website' - only an FAQ on the site (PR #900). User
steer 26 Nov 2026: more call bookings / WhatsApp enquiries.
Facts (matched to the site's high value transaction page): banks and other reporting entities file a Statement of Financial
Transactions; reporting limits include cash deposits of INR 10 lakh or more in a year in savings accounts (a higher limit for
current accounts), fixed / time deposits of INR 10 lakh or more, credit card bills of INR 1 lakh or more in cash or INR 10
lakh or more by any mode, purchases of shares, mutual funds and bonds of INR 10 lakh or more, and foreign currency purchases
of INR 10 lakh or more; interest is reported through TDS statements; all of it is linked to the PAN and appears in the Annual
Information Statement (AIS) and Form 26AS (Form 168 from tax year 2026-27); mismatches trigger compliance e-mails and notices;
in an assessment or search, statements can be called for. No fees, no portal menu paths, no statistics. advisory_lib.contact()
is not used."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources
from build_lib import page, write_page

A.UPDATED = "Last updated: 28 November 2026."
SLUG = "can-income-tax-department-see-my-bank-account-sft-limits-ais-cash-deposit-notice-2026"

C = ("WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with the transaction or AIS entry that worries you, the "
     "bank accounts involved, the source of the money, and any e-mail or notice received. Or book a call directly.")
PAGES = [dict(
    slug=SLUG,
    title="Can the Income Tax Department See My Bank Account? (2026) What Banks Report, SFT Limits, Your AIS and When Statements Are Called For",
    em="not live - but it sees a lot.",
    kicker="/ Salaried, self-employed, NRIs and families &middot; Cash deposits, FDs, credit cards, investments &middot; Updated 2026-11-28",
    lead=("<strong>The income tax department does not watch your account in real time, but banks report interest and large transactions against your PAN, and all of it appears in your Annual Information Statement (AIS). "
          "When those entries do not match your return, you get a compliance e-mail or a notice - and in an assessment or search, the department can ask the bank for full statements.</strong>"),
    sections=[
        ("/ What banks and others report", "Statement of Financial Transactions (SFT) and TDS.",
         table(["Transaction", "Reported when it reaches"], [
             ["Cash deposits", "INR 10 lakh or more in a year in savings accounts (a higher limit for current accounts)"],
             ["Fixed / time deposits", "INR 10 lakh or more in a year"],
             ["Credit card bill payments", "INR 1 lakh or more in cash, or INR 10 lakh or more by any mode, in a year"],
             ["Shares, mutual funds, bonds", "Purchases of INR 10 lakh or more in a year"],
             ["Foreign currency", "Purchases (including forex card loads) of INR 10 lakh or more in a year"],
             ["Interest on deposits", "Reported through TDS statements, whatever the amount when TDS applies"]])
         + ul("<strong>Linked to your PAN:</strong> that is why every account, deposit and investment asks for it.",
              "<strong>Where you see it:</strong> the AIS and Form 26AS (now Form 168) show what has been reported; check them before filing.",
              "<strong>Property deals</strong> are reported by registrars above their own limit, and show up in the AIS too.")),
        ("/ When it becomes a problem, and what to do", "Mismatch, e-mail, notice.",
         ul("<strong>A mismatch:</strong> an AIS entry that is not in your return - for example a cash deposit, FD or share purchase - is the usual trigger.",
            "<strong>First step from the department:</strong> a compliance e-mail or message asking you to explain or file; reply with your feedback on the AIS entry and the source of the money.",
            "<strong>If not resolved:</strong> a notice asking you to explain the source, with possible addition of unexplained money as income.",
            "<strong>During an assessment or search:</strong> the officer can call for full bank statements from you or the bank.",
            "<strong>Keep a paper trail:</strong> gifts with gift deeds, loans with agreements, sale proceeds with deeds and contract notes, cash from business with books.")
         + call_box("AIS entries, bank transactions and notices", ["Checking your AIS against your return",
                                                                  "Explaining cash deposits and large transactions",
                                                                  "AIS feedback and revised or updated returns",
                                                                  "Replies to compliance e-mails and notices",
                                                                  "Source-of-funds documentation"],
                    "The worrying transaction or AIS entry, bank accounts, source of money, any e-mail or notice.")
         + sources("Income-tax Act and Rules on the Statement of Financial Transactions and TDS statements; Annual Information Statement; site high value transaction notice, cash deposit notice and Form 26AS vs AIS pages.")),
    ],
    faqs=[("Can the income tax department see my bank account?", "Not in real time, but it sees a great deal. Banks report interest through TDS statements and large transactions through the Statement of Financial Transactions - such as cash deposits of INR 10 lakh or more in a year in savings accounts and fixed deposits of INR 10 lakh or more - all linked to your PAN and shown in your AIS."),
          ("How much cash can I deposit in my bank account without the tax department knowing?", "Banks report cash deposits that add up to INR 10 lakh or more in a year in savings accounts, with a higher limit for current accounts. Smaller deposits are not automatically safe if they are unexplained income - what matters is that every deposit has a source you can show."),
          ("Can the tax department see my credit card spending?", "Yes, above the reporting limits: credit card bill payments of INR 1 lakh or more in cash, or INR 10 lakh or more by any mode, in a year are reported and appear in the AIS."),
          ("How do I see what the department knows about my bank transactions?", "Check your Annual Information Statement (AIS) and Form 26AS (now Form 168) on the income tax e-filing portal. If an entry is wrong, submit feedback on it; if it is right but missing from your return, correct the return."),
          ("What happens if my AIS shows a large deposit that is not in my return?", "You may get a compliance e-mail asking you to explain it, and later a notice. Reply with the source - salary savings, a gift with a gift deed, a loan agreement or sale proceeds - and revise or update the return if income was left out."),
          ("What should I send to start?", "WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with the transaction or AIS entry, the bank accounts involved, the source of the money and any e-mail or notice received. Or book a call directly.")],
    related=[("high-value-transaction-notice-income-tax-credit-card-spending-sft-limits-how-to-reply-2026.html", "High value transaction notice"),
             ("income-tax-notice-for-cash-deposit-reply-sft-10-lakh-limit-ais-compliance-portal-section-69a-2026.html", "Cash deposit notice reply"),
             ("form-26as-vs-ais-vs-tis-india-2026.html", "Form 26AS vs AIS vs TIS"),
             ("what-happens-if-i-dont-file-itr-india-belated-itr-u-late-fee-notice-prosecution-2026.html", "What happens if you don't file ITR")],
    cta_h="Worried about a bank transaction in your AIS?", cta_b=C,
    keywords="can income tax department see my bank account, can income tax department track bank account, how much cash can i deposit in bank without income tax notice, sft reporting limits, ais bank transactions, credit card spending income tax",
    desc="Can the income tax department see your bank account? Not live, but banks report interest via TDS and large transactions via SFT (cash deposits INR 10 lakh savings, FDs INR 10 lakh, credit cards, investments, forex) to your PAN and AIS; mismatches trigger e-mails and notices.",
    howto={"name": "How to stay on the right side of AIS reporting", "description": "Check, explain, correct.", "steps": [
        {"name": "Check your AIS", "text": "Compare reported transactions with your records and return."},
        {"name": "Give feedback on wrong entries", "text": "Correct duplicates or entries that are not yours."},
        {"name": "Explain the source", "text": "Keep gift deeds, loan agreements and sale documents."},
        {"name": "Correct the return", "text": "Revise or update it if income was missed; reply to notices on time."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch KV complete")
