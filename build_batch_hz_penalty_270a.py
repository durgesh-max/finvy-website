# -*- coding: utf-8 -*-
"""Batch HZ (25 Nov 2026): penalty for under-reporting and misreporting of income - section 270A of the 1961 Act (from AY
2017-18), now section 439 of the Income-tax Act, 2025: 50% of tax on under-reported income, 200% where it results from
misreporting (six categories); immunity / waiver under section 270AA, now section 440 (Form 68 under the 1961 Act, Form 161
under the 2025 Act; pay tax and interest, no appeal); 2025 Act change reported to allow waiver even for misreporting cases.
Demand: sweep ac106 (25 Nov 2026), all 7 markets: "penalty 270a", "penalty 270a income tax", "penalty 270aa", "penalty 270a
applicable from which year".
Facts (checked 25 Nov 2026): Income Tax Department pages on sections 439, 440 and 270AA and on penalties; ClearTax section
270A guide; Business Today (April 2026) and Business Standard on 200% misreporting penalty; ICAI Navi Mumbai / EIRC
presentation on section 440 amendment; TMI notes; Taxmann opinion. Immunity time limit stated as under the 1961 Act's
section 270AA (one month from the end of the month the order is received) with a caution to check section 440."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 25 November 2026."
SLUG = "penalty-section-270a-under-reporting-50-misreporting-200-immunity-270aa-now-section-439-440-2026"

C = contact("the assessment order and penalty notice (section, assessment year, DIN), the additions made, and whether you have filed an appeal or paid the demand")
L = lambda h, t: f'<a href="{h}">{t}</a>'
PAGES = [dict(
    slug=SLUG,
    title="Penalty Under Section 270A (Now Section 439): 50% for Under-Reporting, 200% for Misreporting, and Immunity Under 270AA (Now 440)",
    em="decide on immunity before the appeal clock runs out.",
    kicker="/ Taxpayers facing penalty notices &middot; Income tax &middot; Updated 2026-11-25",
    lead=("<strong>Section 270A of the Income-tax Act, 1961 (applicable from assessment year 2017-18) levies a penalty of 50% of the tax on under-reported income, rising to 200% where the under-reporting results from misreporting, such as suppressing facts, false entries or unrecorded receipts.</strong> "
          "Under the Income-tax Act, 2025 the same penalty is in section 439, at the same rates. "
          "A taxpayer can seek immunity from the penalty (and from prosecution) under section 270AA, now section 440, by paying the tax and interest in the assessment order within the demand notice period and not filing an appeal; the application is made in Form 68 under the 1961 Act and Form 161 under the 2025 Act."),
    sections=[
        ("/ Quick answers", "What people search for.",
         ul("<strong>What is the penalty under section 270A?</strong> 50% of the tax payable on under-reported income; 200% of that tax where the under-reporting is a consequence of misreporting.",
            "<strong>From which year does 270A apply?</strong> From assessment year 2017-18, when it replaced the old concealment penalty. From tax year 2026-27 it is section 439 of the 2025 Act.",
            "<strong>What counts as misreporting?</strong> Misrepresenting or suppressing facts, failing to record investments, claiming expenses not backed by evidence, recording false entries, not recording receipts that affect total income, and failing to report an international or specified domestic transaction under transfer pricing rules.",
            "<strong>What is section 270AA immunity?</strong> If you pay the tax and interest in the assessment order within the demand notice period and do not appeal, you can apply for immunity from the 270A penalty and from prosecution. Under section 270AA the application was due within one month from the end of the month in which the order was received; check section 440 for the current time limit.",
            "<strong>Is immunity available for misreporting?</strong> Under section 270AA, not where the penalty is for misreporting. Commentary on section 440 reports that the 2025 Act extends waiver to some misreporting cases; confirm against the section before relying on it.",
            "<strong>Can I appeal a 270A penalty?</strong> Yes, to CIT(A); see " + L("income-tax-appeal-cit-appeals-form-35-form-99-time-limit-30-days-fee-20-percent-pre-deposit-2026.html", "income tax appeals") + ". You cannot both appeal the assessment and claim immunity.")),
        ("/ 1961 Act vs 2025 Act", "Same framework, new numbers.",
         table(["Point", "Income-tax Act, 1961", "Income-tax Act, 2025"], [
             ["Penalty for under-reporting / misreporting", "Section 270A", "Section 439"],
             ["Rate", "50% / 200% of tax on under-reported income", "50% / 200% (unchanged)"],
             ["Immunity / waiver", "Section 270AA, Form 68", "Section 440, Form 161"],
             ["Applies to", "Assessment years from 2017-18", "Tax years from 2026-27"]])),
        ("/ Immunity or appeal?", "A decision with a deadline.",
         ul("<strong>Choose immunity</strong> when the additions are small or hard to dispute: pay the tax and interest, accept the order, and apply for immunity in time.",
            "<strong>Choose appeal</strong> when the additions are wrong in fact or law: appeal within 30 days and seek a stay of demand; the penalty can also be appealed.",
            "<strong>Respond to the show-cause notice</strong> for penalty with facts showing the income was not under-reported or that any variation is bona fide; see " + L("income-tax-notice-reply-letter-format-sample-how-to-submit-e-proceedings-2026.html", "notice reply format") + ".",
            "<strong>Fix it earlier:</strong> correcting the return before the department finds the gap avoids penalty exposure; see " + L("itr-u-updated-return-48-months-section-139-8a-india.html", "updated return (ITR-U)") + ".",
            "<strong>Background:</strong> " + L("section-143-2-scrutiny-notice-response-india.html", "scrutiny notices") + " and " + L("section-148-148a-reassessment-notice-response-india.html", "reassessment notices") + ".")
         + call_box("Penalty notices", ["Reply to penalty show-cause notice",
                                         "Immunity application (Form 68 / Form 161)",
                                         "Immunity vs appeal decision",
                                         "Appeal against penalty",
                                         "Stay of demand"],
                    "the assessment order, penalty notice and dates.")
         + sources("Income-tax Act, 1961, sections 270A and 270AA; Income-tax Act, 2025, sections 439 and 440 (Income Tax Department section pages); Income Tax Department page on penalties; ClearTax section 270A guide; Business Today (17 April 2026) and Business Standard on misreporting penalties; ICAI presentations on section 440; TMI notes and Taxmann commentary. Checked 25 November 2026.")),
    ],
    faqs=[("What is the penalty under section 270A?", "50% of the tax payable on under-reported income, increased to 200% where the under-reporting results from misreporting. From tax year 2026-27 the provision is section 439 of the Income-tax Act, 2025, at the same rates."),
          ("From which year is penalty under section 270A applicable?", "From assessment year 2017-18, when section 270A replaced the earlier concealment penalty. For tax years from 2026-27 it continues as section 439 of the Income-tax Act, 2025."),
          ("What is immunity under section 270AA?", "Immunity from the 270A penalty and from prosecution if you pay the tax and interest in the assessment order within the demand notice period and do not appeal, applying in Form 68 (Form 161 under section 440 of the 2025 Act). Under section 270AA the application was due within one month from the end of the month in which the order was received."),
          ("What is misreporting of income under section 270A?", "Misrepresentation or suppression of facts, failure to record investments, claiming expenditure not substantiated by evidence, recording false entries, failing to record receipts that affect total income, and failing to report an international or specified domestic transaction."),
          ("Can I appeal against a 270A penalty?", "Yes, before the Commissioner (Appeals). If you instead want immunity under section 270AA or 440, you must not appeal the assessment order."),
          ("Can BQP help with a 270A penalty notice?", "Yes. CA Durgesh Chavda can reply to the penalty notice, assess whether immunity or appeal is better, and file the application or appeal. " + C)],
    related=[("income-tax-appeal-cit-appeals-form-35-form-99-time-limit-30-days-fee-20-percent-pre-deposit-2026.html", "Income tax appeal to CIT(A)"),
             ("rectification-under-section-154-income-tax-now-section-287-time-limit-online-request-format-2026.html", "Rectification under section 154"),
             ("section-143-2-scrutiny-notice-response-india.html", "Scrutiny notice response"),
             ("itr-u-updated-return-48-months-section-139-8a-india.html", "Updated return (ITR-U)"),
             ("income-tax-act-2025-section-mapping-old-vs-new-54-is-82-80c-is-123-nri.html", "Old vs new section numbers")],
    cta_h="Received a penalty notice?", cta_b=C,
    keywords="penalty 270A, section 270A penalty, under-reporting penalty 50 percent, misreporting penalty 200 percent, section 270AA immunity, Form 68, section 439 Income-tax Act 2025, section 440 waiver, penalty 270A applicable from",
    desc="Penalty under section 270A (now section 439 of the 2025 Act): 50% of tax on under-reported income, 200% for misreporting, applicable from AY 2017-18; immunity under 270AA (now 440, Form 68 / Form 161); immunity vs appeal.",
    howto={"name": "How to respond to a 270A penalty notice", "description": "After an assessment with additions.", "steps": [
        {"name": "Read the assessment order", "text": "Identify the additions and whether misreporting is alleged."},
        {"name": "Decide immunity or appeal", "text": "Immunity needs payment and no appeal; appeal within 30 days."},
        {"name": "If immunity: pay and apply", "text": "Tax and interest within the notice period, then Form 68 / Form 161."},
        {"name": "If appeal: file and seek stay", "text": "Appeal to CIT(A) and apply for stay of demand."},
        {"name": "Reply to the show-cause notice", "text": "Facts showing no under-reporting or a bona fide position."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch HZ complete")
