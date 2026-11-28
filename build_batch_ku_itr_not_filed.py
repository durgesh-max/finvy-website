# -*- coding: utf-8 -*-
"""Batch KU (28 Nov 2026): What happens if you do not file an income tax return - belated return, late fee and interest, updated
return (ITR-U), notices, lost refunds and losses, and prosecution risk.
Demand: sweep ac235 (28 Nov 2026), all 7 markets: 'what happens if i don't file itr', 'what happens if i don t file itr for
one year / 2 years', 'what happens if i dont fill itr' - only an FAQ on the site (PR #900). User steer 26 Nov 2026: more call
bookings / WhatsApp enquiries.
Facts (matched to the site's belated ITR and ITR-U pages): belated return for AY 2026-27 by 31 December 2026; late fee under
section 234F INR 5,000 (INR 1,000 where total income does not exceed INR 5 lakh) - a statutory late fee, allowed by the user's
27 Nov rule; interest at 1% per month under section 234A on unpaid tax; a belated return cannot carry forward most losses;
updated return (ITR-U) up to 48 months from the end of the relevant assessment year with additional tax of 25%, 50%, 60% or
70% of the tax and interest depending on the year of filing, and it cannot claim a refund or increase a loss; refunds for
missed years need a condonation application; the department sees income through AIS / Form 26AS and follows up non-filers
with compliance e-mails and notices; wilful failure to file with significant tax unpaid can lead to prosecution. No fees, no
portal menu paths, no statistics. advisory_lib.contact() is not used."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources
from build_lib import page, write_page

A.UPDATED = "Last updated: 28 November 2026."
SLUG = "what-happens-if-i-dont-file-itr-india-belated-itr-u-late-fee-notice-prosecution-2026"

C = ("WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with the years you did not file, your income in those "
     "years (salary, interest, rent, capital gains, business), any TDS that was deducted, and any e-mail or notice you have "
     "received. Or book a call directly.")
PAGES = [dict(
    slug=SLUG,
    title="What Happens If I Don't File My ITR? (2026) Belated Return, Late Fee, Updated Return (ITR-U), Notices, Lost Refunds and Prosecution Risk",
    em="the cost grows the longer you wait.",
    kicker="/ Salaried, self-employed, NRIs and investors who missed a return &middot; AY 2026-27 and earlier years &middot; Updated 2026-11-28",
    lead=("<strong>If your income was above the basic exemption limit - or tax was deducted that you want back - not filing has a cost that grows with time. "
          "Until 31 December you can still file a belated return with a late fee and interest; after that the only route is an updated return (ITR-U) within 48 months, with 25% to 70% additional tax and no refund.</strong> "
          "Meanwhile the department already sees your salary, interest, property and share transactions in the AIS, so a missed return rarely stays unnoticed."),
    sections=[
        ("/ What each delay costs", "From late to very late.",
         table(["When you file", "Route", "What it costs or loses"], [
             ["By the due date", "Original return", "Nothing extra; losses carried forward; refunds paid"],
             ["After the due date, by 31 December 2026 (AY 2026-27)", "Belated return", "Late fee INR 5,000 (INR 1,000 if income up to INR 5 lakh), 1% per month interest on unpaid tax, most losses cannot be carried forward"],
             ["After 31 December, within 48 months", "Updated return (ITR-U)", "Additional tax of 25%, 50%, 60% or 70% of tax and interest by year; no refund, no new or larger loss"],
             ["Not at all", "-", "Notices, best-judgment assessment, interest and penalty, and possible prosecution for wilful failure"]])
         + ul("<strong>Refunds for missed years:</strong> an updated return cannot claim a refund; recovering old TDS needs a condonation of delay application.",
              "<strong>Losses:</strong> a business or capital loss not declared in a return filed on time cannot be carried forward.",
              "<strong>Loans, visas and tenders:</strong> banks, embassies and government buyers often ask for several years of returns.")),
        ("/ How non-filers are picked up", "And how to fix it.",
         ul("<strong>The department already has the data:</strong> TDS on salary, interest and rent, high-value transactions such as property purchases, large deposits and share sales all appear in the AIS against your PAN.",
            "<strong>What usually comes first:</strong> compliance e-mails and messages asking you to file or explain, followed by notices under the reassessment provisions if nothing is done.",
            "<strong>Fix it in order:</strong> file the current year by 31 December if possible; use ITR-U for earlier years where tax is due; apply for condonation where a refund is stuck; reply to any notice on time.",
            "<strong>Did you need to file at all?</strong> Even below the exemption limit, a return is needed in some cases - for example foreign assets, large deposits or spending, or to claim a refund of TDS.")
         + call_box("missed income tax returns", ["Which years must be filed and by which route",
                                                  "Belated return before 31 December",
                                                  "Updated returns (ITR-U) and additional tax",
                                                  "Condonation for stuck refunds",
                                                  "Replies to non-filing e-mails and notices"],
                    "Missed years, income and TDS in those years, any e-mail or notice received.")
         + sources("Income-tax Act, 1961 (sections 139(4), 139(8A), 234A and 234F) and Income-tax Act, 2025 for tax year 2026-27 onwards; CBDT guidance on condonation of delay; site belated ITR, ITR-U, condonation and income tax notice reply pages.")),
    ],
    faqs=[("What happens if I don't file my ITR?", "If your income was above the exemption limit, you can still file a belated return by 31 December with the late fee and interest. After that, only an updated return (ITR-U) within 48 months is possible, with 25% to 70% additional tax and no refund. Non-filers are followed up with e-mails and notices because the department already sees income in the AIS, and wilful failure with significant tax unpaid can lead to prosecution."),
          ("What is the penalty for not filing ITR on time?", "A late fee of INR 5,000 under section 234F (INR 1,000 if total income does not exceed INR 5 lakh) for a belated return, plus 1% per month interest under section 234A on any unpaid tax. If no return is filed at all, a best-judgment assessment, penalty and prosecution become possible."),
          ("Can I file ITR for previous years now?", "For the current assessment year, a belated return is possible until 31 December. For earlier years, an updated return (ITR-U) can be filed within 48 months from the end of the assessment year, with additional tax of 25%, 50%, 60% or 70% depending on how late it is; it cannot claim a refund or declare a loss."),
          ("I did not file ITR for two years. What should I do?", "List the income and TDS for each year from Form 26AS and the AIS, file updated returns where tax is due, and keep any notice deadlines. If those years would show refunds, a condonation application is the route instead. Filing before a notice arrives is better than after."),
          ("Do I get a notice if I don't file ITR?", "Usually yes, if the AIS shows income or transactions - first compliance e-mails or messages, then a notice if nothing is done. Reply on time, even if the answer is that no return was required."),
          ("What should I send to start?", "WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with the years you missed, your income and TDS in those years, and any e-mail or notice received. Or book a call directly.")],
    related=[("belated-itr-31-december-2026-section-139-4-india.html", "Belated ITR by 31 December 2026"),
             ("itr-u-updated-return-48-months-section-139-8a-india.html", "Updated return (ITR-U) within 48 months"),
             ("condonation-of-delay-income-tax-section-119-2-b-itr-refund-loss-application-2026.html", "Condonation of delay for refunds"),
             ("income-tax-notice-reply-letter-format-sample-how-to-submit-e-proceedings-2026.html", "Income tax notice reply")],
    cta_h="Missed one or more returns?", cta_b=C,
    keywords="what happens if i don't file itr, not filed itr for 2 years, penalty for not filing itr, can i file itr for previous years, itr not filed notice, belated return 31 december 2026, updated return itr-u",
    desc="What happens if you don't file your ITR: belated return by 31 December 2026 with INR 5,000 late fee (INR 1,000 up to INR 5 lakh) and interest; ITR-U within 48 months with 25-70% additional tax and no refund; AIS-driven notices; lost refunds and losses; prosecution for wilful failure.",
    howto={"name": "How to fix missed income tax returns", "description": "In the right order.", "steps": [
        {"name": "List the missed years", "text": "Income and TDS per year from Form 26AS and the AIS."},
        {"name": "File the current year", "text": "Belated return by 31 December if possible."},
        {"name": "Handle earlier years", "text": "ITR-U where tax is due; condonation where a refund is stuck."},
        {"name": "Answer notices", "text": "Reply on time, with the returns filed or an explanation."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch KU complete")
