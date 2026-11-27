# -*- coding: utf-8 -*-
"""Batch KB (27 Nov 2026): Income tax for intraday and F&O traders - ITR-3, business codes 21009 / 21010 / 21011,
speculative vs non-speculative income, turnover, tax audit, loss set-off and carry forward, and fixing a missed return.
Demand: sweep ac148 (27 Nov 2026), all 7 markets: "intraday trading itr", "... business code", "... itr code", "... itr
form", "... itr filing", "... itr 3", "... itr 2", "speculative business loss carry forward how many years", "...
in new tax regime", "speculative loss carry forward for how many years", "share market tax details"; no page covered
intraday or F&O taxation.
User steer 26 Nov 2026: more call bookings / WhatsApp enquiries - trading income needs ITR-3, turnover working and often
a tax audit, which traders hand to a CA.
Facts (verified 27 Nov 2026): ITR-3 business codes 21009 (speculative trading - intraday), 21010 (futures and options
trading), 21011 (buying and selling shares - delivery); intraday equity trading is speculative business (section 43(5));
F&O on recognised exchanges is non-speculative business; speculative loss can be set off only against speculative income
and carried forward four years; non-speculative business loss can be set off against other income except salary and
carried forward eight years; carry forward needs the return filed by the due date; turnover for traders per the ICAI
Guidance Note - aggregate of absolute profits and losses; tax audit under section 44AB above the turnover limits (Rs 10
crore where cash receipts and payments are within 5%), and where presumptive rules interact - case-specific; whether
section 44AD applies to speculative income is disputed - not stated as settled. Corresponding provisions of the Income-tax
Act, 2025 apply from 1 April 2026 (sections not restated). No fees, no office claims, no statistics."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 27 November 2026."
SLUG = "intraday-fo-trading-income-tax-itr-3-business-code-21009-21010-turnover-audit-loss-carry-forward-2026"

C = contact("your broker's tax P&L and contract-note summary for the year, your AIS and Form 168 (old 26AS), bank statements, details of any other income (salary, rent, capital gains), last year's ITR if losses were carried forward, and any notice received")
PAGES = [dict(
    slug=SLUG,
    title="Intraday and F&O Trading Income Tax (2026): ITR-3, Business Codes 21009 / 21010, Turnover, Tax Audit and Carrying Forward Losses",
    em="file it as a business, or lose the loss.",
    kicker="/ Salaried traders, full-time traders and NRIs trading in India &middot; Speculative and non-speculative income &middot; Updated 2026-11-27",
    lead=("<strong>Intraday equity trading is speculative business income and F&O trading is non-speculative business income - neither is a capital gain - so traders file ITR-3, not ITR-1 or ITR-2.</strong> "
          "The return needs the right business code (21009 for intraday, 21010 for F&O, 21011 for delivery-based share trading), a turnover worked out the way the ICAI prescribes, and sometimes a tax audit. "
          "Get it wrong or file late and you lose the right to carry forward trading losses."),
    sections=[
        ("/ How trading income is taxed", "The three kinds of share-market income.",
         table(["Activity", "Head and code", "Losses"], [
             ["Intraday equity (no delivery)", "Speculative business income - code 21009", "Set off only against speculative income; carry forward four years"],
             ["Futures and options", "Non-speculative business income - code 21010", "Set off against other income except salary; carry forward eight years"],
             ["Delivery-based shares held as investments", "Capital gains (STCG / LTCG)", "Capital-loss rules; carry forward eight years"],
             ["Frequent delivery trading as a business", "Business income - code 21011", "Business-loss rules"]])
         + ul("<strong>Form:</strong> ITR-3 for anyone with intraday or F&O income, including salaried people who trade on the side.",
              "<strong>Losses need a timely return:</strong> business and speculative losses can be carried forward only if the return is filed by the due date.",
              "<strong>New regime:</strong> trading income is taxed at slab rates under either regime; check the regime choice rules for people with business income before switching.")),
        ("/ Turnover and tax audit", "Where traders get caught.",
         ul("<strong>Turnover:</strong> under the ICAI Guidance Note, trading turnover is the total of absolute profits and losses on each trade - not the contract value.",
            "<strong>Tax audit (section 44AB):</strong> required where turnover exceeds the limit - Rs 10 crore when cash receipts and payments are within 5%, which is usually the case for traders - and can also arise in some loss or low-profit cases linked to the presumptive scheme; check your facts.",
            "<strong>Presumptive scheme:</strong> whether section 44AD can apply to speculative income is disputed, so do not rely on it without advice.",
            "<strong>Expenses:</strong> brokerage, exchange charges, internet, advisory subscriptions and similar costs are deductible against trading income; STT is not deductible.")),
        ("/ If you missed or got it wrong", "Fixing the return.",
         ul("Filed ITR-2 showing F&O as capital gains? File a revised return in ITR-3 - for AY 2026-27 free until 31 December 2026.",
            "Missed the due date? A belated return by 31 December 2026 is possible, but losses (other than house property) cannot be carried forward.",
            "Got a notice for a mismatch between the AIS and your return? Reconcile with the broker's tax P&L and reply with the working.")
         + call_box("Trader tax returns", ["ITR-3 for intraday and F&O income",
                                           "Turnover working and tax audit",
                                           "Loss set-off and carry forward schedules",
                                           "Revised and belated returns",
                                           "Notices for AIS mismatches"],
                    "Broker tax P&L, AIS and bank statements.")
         + sources("Income-tax Act (sections 43(5), 44AB, 44AD, 70-73, 80, 139) and the corresponding provisions of the Income-tax Act, 2025; ITR-3 business codes 21009, 21010, 21011; ICAI Guidance Note on Tax Audit (turnover for derivatives and speculative transactions); site belated, revised return, tax audit and notice reply guides. Checked 27 November 2026.")),
    ],
    faqs=[("Which ITR should I file for intraday or F&O trading?", "ITR-3. Intraday equity trading is speculative business income and F&O is non-speculative business income, so ITR-1 and ITR-2 cannot be used - even if you are salaried and trade on the side."),
          ("What is the business code for intraday and F&O trading in the ITR?", "Code 21009 for speculative trading (intraday), 21010 for futures and options trading, and 21011 for buying and selling shares on delivery as a business."),
          ("For how many years can a speculative loss be carried forward?", "Four years, and it can be set off only against speculative income. A non-speculative business loss such as an F&O loss can be set off against other income except salary and carried forward for eight years. Both need the return filed by the due date."),
          ("Can I carry forward trading losses under the new tax regime?", "Trading losses from business can generally be carried forward under the new regime as well, but the return must be filed on time; check the regime rules for people with business income before switching between regimes."),
          ("Is a tax audit required for F&O trading?", "Only in some cases: when turnover - worked out as the total of absolute profits and losses - exceeds the section 44AB limit (Rs 10 crore when cash transactions are within 5%), or in certain low-profit or loss cases linked to the presumptive scheme. Have your turnover and profit checked before the due date."),
          ("What should I send to file my trading ITR?", "WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with your broker's tax P&L and contract-note summary, your AIS and Form 168 (old 26AS), bank statements, details of salary, rent or capital gains, last year's ITR if you carried forward losses, and any notice received. We work out turnover, check audit applicability and file ITR-3. You keep your own e-filing login."),
          ("Can BQP file ITR-3 for traders and NRIs?", "Yes. CA Durgesh Chavda works online with salaried and full-time traders and with NRIs trading in India. " + C)],
    related=[("revised-itr-section-139-5-deadline-31-december-2026-india.html", "Revised ITR by 31 December 2026"),
             ("belated-itr-31-december-2026-section-139-4-india.html", "Belated ITR by 31 December 2026"),
             ("form-3ca-3cb-3cd-tax-audit-india-2026-checklist.html", "Tax audit (Form 3CA / 3CB / 3CD)"),
             ("best-ca-section-44ad-44ada-presumptive-scheme-india.html", "Presumptive scheme (44AD / 44ADA)"),
             ("high-value-transaction-notice-income-tax-credit-card-spending-sft-limits-how-to-reply-2026.html", "High value transaction notices")],
    cta_h="Trading income to report?", cta_b=C,
    keywords="intraday trading itr, intraday trading business code, f&o itr 3, business code 21009 21010, speculative loss carry forward years, f&o turnover tax audit, intraday trading itr form, speculative business loss new tax regime",
    desc="Income tax for intraday and F&O traders: ITR-3, business codes 21009 / 21010 / 21011, speculative vs non-speculative income, turnover under the ICAI method, tax audit, loss set-off and carry forward (four / eight years), and what to send.",
    howto={"name": "How to file ITR-3 for intraday and F&O trading", "description": "From broker statement to filed return.", "steps": [
        {"name": "Get the broker's tax P&L", "text": "Download the year's tax P&L and contract-note summary."},
        {"name": "Split the income", "text": "Separate intraday (speculative), F&O (non-speculative) and delivery trades."},
        {"name": "Work out turnover", "text": "Total the absolute profits and losses and check audit applicability."},
        {"name": "File ITR-3 on time", "text": "Use the right codes and file by the due date to keep losses."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch KB complete")
