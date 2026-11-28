# -*- coding: utf-8 -*-
"""Batch LB (28 Nov 2026): Income tax notice under section 133(6) (call for information) and summons under section 131 - what they
are, how they differ from assessment notices, how to reply, and consequences of ignoring them.
Demand: 'notice under section 133(6)', '133(6) notice reply', 'summons under section 131 income tax', 'information notice income
tax' - mentioned in about ten pages (cash deposit, property, HVT, NRI notice) but no dedicated page. High hire intent. User steer
26 Nov 2026: more call bookings / WhatsApp enquiries.
Facts (Income-tax Act, 1961; corresponding provisions in the Income-tax Act, 2025): section 133(6) lets an income tax authority
call for information from any person, including banks and other third parties, on points useful for a proceeding or an inquiry;
for an inquiry where no proceeding is pending, it needs higher approval; it is a request for information, not an assessment; often
issued to verify AIS / SFT data, property or cash transactions, or third-party payments. Section 131 gives authorities the powers
of a civil court - discovery and inspection, enforcing attendance, examining on oath, compelling production of books and documents
and issuing commissions; statements recorded under it are on oath; books produced can be impounded, and retained beyond fifteen
days (excluding holidays) only with higher approval. Not replying can attract penalty under section 272A and lead to a best-judgment
or reassessment route. No fees, no penalty amounts, no portal menu paths. advisory_lib.contact() is not used."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources
from build_lib import page, write_page

A.UPDATED = "Last updated: 28 November 2026."
SLUG = "income-tax-notice-section-133-6-information-request-summons-section-131-how-to-reply-2026"

C = ("WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with the notice or summons (all pages), the information "
     "or documents asked for, the deadline, and your return and AIS for the year mentioned. Or book a call directly.")
PAGES = [dict(
    slug=SLUG,
    title="Income Tax Notice Under Section 133(6) and Summons Under Section 131 (2026): What They Mean, How They Differ From Assessment Notices, and How to Reply",
    em="answer exactly what is asked, on time.",
    kicker="/ Individuals, NRIs, businesses and third parties &middot; Information notices and summons &middot; Updated 2026-11-28",
    lead=("<strong>A notice under section 133(6) is a request for information - from you or from a third party such as your bank - to verify a transaction or support an inquiry. "
          "A summons under section 131 goes further: the officer has the powers of a civil court and can require you to attend, produce books and give a statement on oath. "
          "Neither is an assessment by itself, but what you send or say becomes the record for whatever follows.</strong>"),
    sections=[
        ("/ 133(6) vs 131 vs assessment notices", "Know which one you have.",
         table(["Point", "Section 133(6)", "Section 131", "Assessment notices (143(2), 148)"], [
             ["Purpose", "Call for information on specific points", "Civil-court powers: attendance, documents, statements", "Start or reopen an assessment"],
             ["Sent to", "Any person, including banks and third parties", "The person whose evidence is needed", "The taxpayer being assessed"],
             ["Statement on oath", "No - written information", "Yes", "Not by itself"],
             ["Books and documents", "Copies or details asked for", "Production can be compelled; can be impounded", "As called for in the proceeding"],
             ["If ignored", "Penalty under section 272A; matter may escalate", "Penalty under section 272A; matter may escalate", "Best-judgment assessment and penalties"]])
         + ul("<strong>Why 133(6) notices come:</strong> to verify AIS or SFT entries, property purchases, cash deposits, large payments, or a counterparty&rsquo;s claims about you.",
              "<strong>No proceeding pending?</strong> An inquiry under 133(6) can still be made, with higher approval - so a notice does not mean an assessment has started.")),
        ("/ How to reply", "Precise, documented, on time.",
         ul("<strong>Read the questions carefully:</strong> answer each point asked, with supporting documents - no more and no less.",
            "<strong>Match your records:</strong> check the figures against your return, AIS, bank statements and books before you reply.",
            "<strong>Reply within the deadline</strong> through the e-proceedings facility or as the notice directs; if you need more time, ask for an adjournment before the date.",
            "<strong>Summons under 131:</strong> attend or seek a new date in writing; give statements carefully, as they are on oath; ask for a copy.",
            "<strong>Third-party notices:</strong> a bank, employer or buyer may be asked about you - keep your own explanation ready in case an assessment follows.")
         + call_box("a 133(6) notice or 131 summons", ["Reading what is actually asked",
                                                       "Reconciling with return, AIS and books",
                                                       "Drafting the reply and annexures",
                                                       "Preparing for a summons and statement",
                                                       "Handling the assessment that may follow"],
                    "The notice or summons, information asked for, deadline, return and AIS.")
         + sources("Income-tax Act, 1961 (sections 131, 133(6) and 272A) and the corresponding provisions of the Income-tax Act, 2025; site income tax notice reply, high value transaction, cash deposit and property purchase notice pages.")),
    ],
    faqs=[("What is a notice under section 133(6) of the Income-tax Act?", "It is a request from an income tax authority for information on specific points, sent to the taxpayer or to a third party such as a bank. It is used to verify transactions or support an inquiry and is not an assessment by itself."),
          ("How do I reply to a section 133(6) notice?", "Answer each question asked, attach supporting documents, check the figures against your return, AIS and bank statements, and submit within the deadline through the e-proceedings facility or as the notice directs. Ask for more time before the deadline if needed."),
          ("What is a summons under section 131?", "A summons issued using the powers of a civil court, requiring you to attend, produce books or documents and give a statement on oath. Books produced can be impounded, and keeping them beyond fifteen days, excluding holidays, needs higher approval."),
          ("What happens if I ignore a 133(6) notice or 131 summons?", "Not complying can attract penalty under section 272A, and the officer may move to a best-judgment assessment or reassessment using the information already available."),
          ("Does a 133(6) notice mean my case is under scrutiny?", "Not necessarily. It can be issued for an inquiry even when no proceeding is pending. But the reply forms part of the record, so it should be accurate and complete."),
          ("What should I send to start?", "WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with the notice or summons, the information asked for, the deadline, and your return and AIS for that year. Or book a call directly.")],
    related=[("how-to-respond-to-income-tax-notice-india.html", "How to respond to an income tax notice"),
             ("high-value-transaction-notice-income-tax-credit-card-spending-sft-limits-how-to-reply-2026.html", "High value transaction notice"),
             ("income-tax-notice-for-property-land-purchase-why-you-got-it-how-to-reply-source-of-funds-2026.html", "Income tax notice for property purchase"),
             ("income-tax-survey-section-133a-what-officers-can-do-statement-impounding-books-survey-vs-search-2026.html", "Income tax survey under section 133A")],
    cta_h="Received a 133(6) notice or a summons?", cta_b=C,
    keywords="notice under section 133(6), 133(6) notice reply, income tax information notice, summons under section 131 income tax, 131 summons statement on oath, ignore 133(6) notice penalty",
    desc="Income tax notice under section 133(6) and summons under section 131: what each means, how they differ from 143(2) and 148 assessment notices, how to reply on time with documents, statements on oath, impounding of books, and penalty under section 272A for non-compliance.",
    howto={"name": "How to reply to a 133(6) notice or 131 summons", "description": "Read, reconcile, reply.", "steps": [
        {"name": "Identify the notice", "text": "133(6) information request or 131 summons; note the deadline."},
        {"name": "Reconcile", "text": "Check figures against return, AIS, bank statements and books."},
        {"name": "Reply precisely", "text": "Answer each point with documents; seek time before the deadline if needed."},
        {"name": "Prepare for follow-up", "text": "Keep explanations ready in case an assessment follows."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch LB complete")
