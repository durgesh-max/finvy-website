# -*- coding: utf-8 -*-
"""Batch GP (24 Nov 2026): FEMA penalty in India - section 13 penalties (up to three times the sum involved, INR 2 lakh
where not quantifiable, INR 5,000 a day for continuing contraventions), who imposes them (Enforcement Directorate
adjudication), and the three ways out: late submission fee for reporting delays, compounding with the RBI under the
Foreign Exchange (Compounding Proceedings) Rules, 2024, or adjudication and appeal. Common NRI and company breaches.
Call-first page.
Demand: sweep ac72 (24 Nov 2026), all 7 markets: "fema penalty", "fema violation penalty", "fema penalty provisions",
"fema penalty cases", "rbi compounding application format / fees".
Facts (checked 24 Nov 2026): FEMA section 13(1) - penalty up to thrice the sum involved where quantifiable, up to INR 2
lakh otherwise, plus up to INR 5,000 a day for continuing contraventions; tribunals treat these as maximums (TaxTMI,
advocatekhoj, VJM Global). Compounding Proceedings Rules 2024 notified 12 September 2024: application fee INR 10,000 plus
GST; order within 180 days of the application; amount payable within 15 days of the order; not available for a similar
contravention within three years of an earlier compounding (RBI, Nishith Desai, Mondaq). Late submission fee for reporting
delays as already stated on site pages."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 24 November 2026."
SLUG = "fema-penalty-india-2026-section-13-violation-compounding-late-submission-fee-nri-company"

C = contact("what happened (late filing, investment without approval, money held abroad, wrong account), the amounts and dates, and whether you have received any notice")
L = lambda h, t: f'<a href="{h}">{t}</a>'
PAGES = [dict(
    slug=SLUG,
    title="FEMA Penalty in India (2026): Section 13 Penalties, ED Notices, Compounding With the RBI and Late Submission Fees",
    em="most breaches can be fixed before a notice arrives.",
    kicker="/ FEMA &middot; Penalties &middot; Updated 2026-11-24",
    lead=("<strong>Under section 13 of the Foreign Exchange Management Act, a contravention can attract a penalty of up to three times the sum involved, or up to INR 2 lakh where the amount cannot be quantified, plus up to INR 5,000 a day while it continues.</strong> "
          "These are maximums: the actual penalty is set case by case. FEMA is a civil law, and most problems can be cleared before any notice: late reports through the RBI&rsquo;s <strong>late submission fee</strong>, and other breaches through <strong>compounding</strong> with the RBI, where you admit the contravention and pay a computed amount (a fixed application fee; order within 180 days). "
          "Once the Enforcement Directorate starts adjudication, options narrow, so acting early is cheaper."),
    sections=[
        ("/ Quick answers", "What people facing a FEMA issue ask.",
         ul("<strong>What is the penalty for a FEMA violation?</strong> Up to three times the amount involved, or up to INR 2 lakh if it cannot be quantified, plus up to INR 5,000 for each day the contravention continues.",
            "<strong>Who imposes it?</strong> An adjudicating authority, usually in the Enforcement Directorate, after a show cause notice; appeals go to the Special Director (Appeals) or the Appellate Tribunal.",
            "<strong>Can I fix it myself first?</strong> Yes. Reporting delays are regularised by paying a late submission fee; other contraventions can be compounded with the RBI, which closes the matter without adjudication.",
            "<strong>Is FEMA criminal?</strong> No, it is civil, but unpaid penalties can be recovered strictly, and serious cases can overlap with income tax or black money law.",
            "<strong>How much does compounding cost?</strong> A fixed application fee with the application, and a compounding amount the RBI works out from the sum and the delay, payable within 15 days of the order - book a call and we will work out your likely amount.")),
        ("/ Routes compared", "Which route fits which problem.",
         table(["Route", "Used for", "Key points"], [
             ["Late submission fee", "Reports filed late (FC-GPR, FC-TRS, FLA return, ODI returns and similar)", "Pay the RBI's fee and file; available within the time window the RBI allows, otherwise compounding"],
             ["Compounding with the RBI", "Most contraventions, including old reporting delays, investments outside the rules, missed approvals", "Voluntary admission; fixed application fee; order within 180 days; pay within 15 days; not for a repeat of a similar contravention within three years"],
             ["Adjudication", "Where a show cause notice has been issued or compounding is refused or not used", "Penalty up to section 13 limits; appeal available"],
             ["Serious cases", "Money or assets held abroad in breach of the law", "Higher stakes, including confiscation; take advice before any filing"]])),
        ("/ Common breaches", "What we see most often for NRIs and companies.",
         ul("<strong>Foreign investment reporting:</strong> FC-GPR filed late after allotting shares to a foreign investor, or the annual FLA return missed; see " + L("fema-health-check-foreign-owned-indian-company-fc-gpr-fla-compounding-2026.html", "FEMA health check for foreign-owned companies") + ".",
            "<strong>Overseas investment:</strong> a US or Dubai company set up from India without ODI filings; see " + L("fema-compounding-odi-rbi-regional-office-uin-circular-28-october-2026.html", "ODI compounding") + ".",
            "<strong>Land-border investors:</strong> investment from China or other neighbouring countries without government approval; see " + L("press-note-2-2026-fdi-land-border-countries-china-10-percent-60-day-approval.html", "Press Note 2 (2026)") + ".",
            "<strong>NRI accounts:</strong> resident accounts not converted to NRO after moving abroad, or NRE accounts not re-designated on return.",
            "<strong>Found in due diligence:</strong> breaches discovered before a funding round or sale; see " + L("fema-breach-found-pre-ma-diligence-urgent-compounding-india.html", "FEMA breach found in diligence") + ".")
         + call_box("FEMA penalties and compounding", ["Working out which contraventions exist",
                                                        "Late submission fee or compounding: which route",
                                                        "Preparing the compounding application",
                                                        "Replying to a show cause notice",
                                                        "Cleaning up before a funding round or exit"],
                    "what happened, the amounts and dates, and any notice received.")
         + sources("Foreign Exchange Management Act, 1999, section 13 (penalties) and sections 15-19 (compounding, adjudication, appeals); Foreign Exchange (Compounding Proceedings) Rules, 2024, notified 12 September 2024, and RBI Master Direction on compounding of contraventions; RBI late submission fee framework for reporting delays; commentary from Nishith Desai Associates, Mondaq, TaxTMI and BCAJ. Each case turns on its facts; checked 24 November 2026.")),
    ],
    faqs=[("What is the penalty for a FEMA violation in India?", "Under section 13, up to three times the sum involved where it can be quantified, or up to INR 2 lakh where it cannot, plus up to INR 5,000 for every day the contravention continues. These are maximums; the adjudicating authority sets the actual amount."),
          ("Can a FEMA violation be settled without a penalty order?", "Usually yes. Late reports are regularised by paying the RBI's late submission fee, and most other contraventions can be compounded with the RBI by admitting them and paying a computed amount, which closes the matter without adjudication."),
          ("What is the RBI compounding application fee?", "A fixed application fee is payable with the application under the Foreign Exchange (Compounding Proceedings) Rules, 2024, separate from the compounding amount the RBI works out from the sum and the delay. Book a call and we will estimate your total. The RBI must pass an order within 180 days of the application, and the compounding amount is payable within 15 days of the order."),
          ("Is a FEMA violation a criminal offence?", "No. FEMA is a civil law with monetary penalties, though unpaid penalties are recovered strictly and holding assets abroad in breach of the law can also raise income tax and black money issues."),
          ("Who decides FEMA penalties?", "An adjudicating authority, typically in the Enforcement Directorate, after issuing a show cause notice. Orders can be appealed to the Special Director (Appeals) or the Appellate Tribunal for Foreign Exchange matters."),
        ("What should I do if I get an ED notice under FEMA?", "Do not ignore it. The Enforcement Directorate investigates FEMA contraventions under section 37 and can issue summons or ask for documents, and adjudication of a penalty starts only with a show cause notice. Read exactly what the notice asks for and by when, collect the bank records, RBI filings and approvals for the transactions in question, and reply or appear on time with a factual, documented account. Contraventions of section 3(a) are compounded by the ED itself, while the RBI compounding route asks for an undertaking that you are not under ED investigation - so check early which route is still open. If a penalty order is passed, the appeal lies to the Special Director (Appeals) or the Appellate Tribunal."),
        ("What should I send if I have received an ED notice or FEMA show cause notice?", "WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with the notice or summons, the transactions it refers to (bank statements, remittance records, Form 145 / 146 or FIRC copies), any RBI filings or approvals such as FC-GPR, ODI or LRS records, and earlier correspondence with your bank or the RBI. We review the exposure, prepare the reply and documents, and advise whether compounding is available."),
          ("Can BQP help with a FEMA penalty or compounding?", "Yes. " + C)],
    related=[("fema-compounding-foreign-subsidiary-india.html", "FEMA compounding for foreign subsidiaries"),
             ("fema-health-check-foreign-owned-indian-company-fc-gpr-fla-compounding-2026.html", "FEMA health check"),
             ("fema-compounding-odi-rbi-regional-office-uin-circular-28-october-2026.html", "ODI compounding"),
             ("press-note-2-2026-fdi-land-border-countries-china-10-percent-60-day-approval.html", "Land-border FDI rules"),
             ("fema-breach-found-pre-ma-diligence-urgent-compounding-india.html", "FEMA breach found in diligence")],
    cta_h="Facing a FEMA problem?", cta_b=C,
    keywords="FEMA penalty, FEMA violation penalty, FEMA penalty provisions, section 13 FEMA, FEMA penalty in India, RBI compounding, compounding application fee, late submission fee FEMA, FEMA show cause notice",
    desc="FEMA penalty in India (2026): section 13 allows up to three times the sum involved, INR 2 lakh where not quantifiable, and INR 5,000 a day for continuing breaches; fix it first through the RBI late submission fee or compounding (a fixed application fee plus the compounding amount, order within 180 days) before adjudication.",
    howto={"name": "How to deal with a FEMA contravention", "description": "Steps from discovery to closure.", "steps": [
        {"name": "List the contraventions", "text": "Late reports, missed approvals, wrong accounts, overseas investments."},
        {"name": "Pick the route", "text": "Late submission fee for reporting delays, compounding for the rest."},
        {"name": "File the application", "text": "Compounding with the RBI: the application with its fee and supporting documents."},
        {"name": "Pay and close", "text": "Pay the compounding amount within 15 days of the order."},
        {"name": "Reply to any notice", "text": "If a show cause notice arrives, respond on time and consider appeal routes."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch GP complete")
