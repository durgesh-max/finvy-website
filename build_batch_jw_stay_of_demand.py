# -*- coding: utf-8 -*-
"""Batch JW (27 Nov 2026): Stay of income tax demand pending appeal - the 20% guideline, the Budget 2026 announcement of
10% on core tax, how to apply, and what courts have said.
Demand: sweep ac140 (27 Nov 2026), all 7 markets: "stay of demand income tax", "... cbdt circular / circular pdf", "...
section", "... meaning", "... income tax act 2025", "... format", "... case laws"; no page covered stay of demand.
User steer 26 Nov 2026: more call bookings / WhatsApp enquiries - a stay application with an appeal needs a CA.
Facts (verified 27 Nov 2026): stay of demand pending appeal under section 220(6) of the 1961 Act (corresponding provisions
of the Income-tax Act, 2025 apply from 1 April 2026 - section number not restated); CBDT Office Memorandum of 29 February
2016 as modified by Instruction dated 31 July 2017 - stay generally granted on payment of 20% of the disputed demand, with
the officer able to ask for more or accept less in specified cases; Union Budget 2026-27 (speech para 113) announced a
reduction to 10% computed on the core tax demand - implementation status not confirmed, so readers are told to check;
High Courts (Delhi, Allahabad, Telangana) have held the 20% is not an automatic condition and the officer must decide the
application on merits (prima facie case, financial hardship). No fees, no timings, no office claims."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 27 November 2026."
SLUG = "stay-of-income-tax-demand-20-percent-rule-budget-2026-10-percent-how-to-apply-format-2026"

C = contact("the assessment order and demand notice, the appeal filed (or the order you want to appeal), the amount of the demand and what you have paid, and anything that shows financial hardship or a strong case on merits")
PAGES = [dict(
    slug=SLUG,
    title="Stay of Income Tax Demand (2026): How to Apply Pending Appeal, the 20% Rule, the Budget 2026 Cut to 10% and the Application Format",
    em="file the appeal, then stop the recovery.",
    kicker="/ Individuals, companies and NRIs facing a high-pitched assessment &middot; Recovery pending appeal &middot; Updated 2026-11-27",
    lead=("<strong>When an assessment raises a large demand that you are appealing, the department can still recover it - attach bank accounts, adjust refunds - unless you get a stay of demand pending the appeal.</strong> "
          "The CBDT's guidelines generally grant a stay on payment of 20% of the disputed demand, and the Union Budget 2026-27 announced a reduction to 10% computed on the core tax. "
          "Courts have also held the percentage is not automatic: the officer must look at your case, including a strong prima facie case and financial hardship."),
    sections=[
        ("/ How the stay works", "The rules in brief.",
         table(["Point", "Position"], [
             ["Who grants it", "The Assessing Officer, on application, once an appeal against the order is filed; if refused, the Principal Commissioner or Commissioner can be approached"],
             ["Standard condition", "CBDT guidelines (2016, modified in July 2017): stay generally on payment of 20% of the disputed demand, with discretion to ask for more or accept less in specified cases"],
             ["Budget 2026-27", "Announced a reduction to 10%, computed on the core tax demand - check whether it has been applied to your case before paying"],
             ["Courts", "High Courts have held the percentage is not a mandatory condition; the application must be decided on merits, considering prima facie case and hardship"],
             ["Old or new Act", "Demands from proceedings under the Income-tax Act, 1961 follow its provisions; the Income-tax Act, 2025 applies from 1 April 2026"]])),
        ("/ How to apply", "What a stay application should contain.",
         ul("<strong>File the appeal first</strong> (to the Commissioner (Appeals) or the next forum) and keep the acknowledgement.",
            "<strong>Write to the Assessing Officer</strong> on the e-filing portal or by letter: the order and demand, the appeal reference, the grounds showing a prima facie case, and any financial hardship.",
            "<strong>Offer what you can pay</strong> - the guideline percentage, or less with reasons - and ask for recovery to be kept in abeyance until the appeal is decided.",
            "<strong>If refused or not decided,</strong> approach the Principal Commissioner or Commissioner, and if needed the Tribunal or the High Court.",
            "<strong>Keep the order of stay</strong> safe and track any adjustment of refunds against the demand.")),
        ("/ When a stay matters most", "Typical situations.",
         ul("High-pitched additions in scrutiny or reassessment, such as unexplained cash or property transactions.",
            "Transfer pricing or international tax adjustments on companies with foreign parents.",
            "NRIs whose refunds are being adjusted against a disputed demand.",
            "Demands where the main issue is already decided in your favour in an earlier year or by a court.")
         + call_box("Stay of demand", ["Filing the appeal and stay application together",
                                       "Arguing prima facie case and financial hardship",
                                       "Approaching the Principal Commissioner if refused",
                                       "Stopping refund adjustments and bank attachments",
                                       "Representing in the appeal itself"],
                    "The order, the demand and the appeal.")
         + sources("Income-tax Act, 1961 (section 220(6)) and the corresponding provisions of the Income-tax Act, 2025; CBDT Office Memorandum of 29 February 2016 and Instruction of 31 July 2017; Union Budget 2026-27 speech (paragraph 113); High Court decisions (Delhi, Allahabad, Telangana) on the 20% guideline; site notice reply and 148A guides. Checked 27 November 2026.")),
    ],
    faqs=[("What is a stay of demand in income tax?", "An order keeping recovery of a disputed income tax demand in abeyance while your appeal against the assessment is pending, so the department does not attach your bank accounts or adjust refunds against it in the meantime."),
          ("How much do I have to pay to get a stay of income tax demand?", "Under the CBDT's guidelines a stay is generally granted on payment of 20% of the disputed demand, and the officer can ask for more or accept less in specified cases. The Union Budget 2026-27 announced a reduction to 10% computed on the core tax demand - check whether it applies to your demand. Courts have also held the percentage is not automatic."),
          ("Is the 20% deposit mandatory for a stay?", "No. Several High Courts have held that the 20% figure in the CBDT guidelines is not a mandatory condition and that the officer must decide the stay application on its merits, including a strong prima facie case and financial hardship."),
          ("How do I apply for a stay of demand?", "File the appeal, then apply to the Assessing Officer with the order, the demand, the appeal reference, your grounds and any hardship, offering the amount you can pay. If the officer refuses or does not decide, approach the Principal Commissioner or Commissioner, and if needed the Tribunal or the High Court."),
          ("Can the department adjust my refund against a disputed demand?", "It can propose to adjust refunds against an outstanding demand, but you can object, and once a stay is granted the disputed amount should not be recovered while the appeal is pending. Respond to any adjustment intimation on the portal within the time given."),
          ("What should I send to apply for a stay of demand?", "WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with the assessment order and demand notice, the appeal (or the order you want to appeal), the amount demanded and paid, and anything showing financial hardship or a strong case. We file the appeal and the stay application and follow up with the officer. You keep your own e-filing login."),
          ("Can BQP handle stay applications and appeals?", "Yes. CA Durgesh Chavda works online with individuals, companies, foreign-owned subsidiaries and NRIs facing disputed demands. " + C)],
    related=[("how-to-respond-to-income-tax-notice-india.html", "How to respond to an income tax notice"),
             ("section-148-148a-reassessment-notice-response-india.html", "Section 148 / 148A reassessment"),
             ("section-143-2-scrutiny-notice-response-india.html", "Section 143(2) scrutiny"),
             ("income-tax-notice-for-cash-deposit-reply-sft-10-lakh-limit-ais-compliance-portal-section-69a-2026.html", "Cash deposit notices"),
             ("section-143-1-intimation-response-india-2026.html", "Section 143(1) demand")],
    cta_h="Facing a disputed tax demand?", cta_b=C,
    keywords="stay of demand income tax, stay of demand cbdt circular, stay of demand 20 percent, stay of demand budget 2026 10 percent, stay of demand application format, section 220(6) stay, stay of demand income tax act 2025",
    desc="Stay of income tax demand pending appeal: the CBDT 20% guideline, the Budget 2026-27 announcement of 10% on core tax, what courts have said, how to apply to the Assessing Officer and the Principal Commissioner, and what to send.",
    howto={"name": "How to apply for a stay of income tax demand", "description": "From appeal to stay order.", "steps": [
        {"name": "File the appeal", "text": "Appeal the assessment order and keep the acknowledgement."},
        {"name": "Apply to the officer", "text": "Send the stay application with grounds, hardship and the amount you offer to pay."},
        {"name": "Escalate if refused", "text": "Approach the Principal Commissioner or Commissioner, then the Tribunal or High Court if needed."},
        {"name": "Track recovery", "text": "Keep the stay order and watch for refund adjustments or attachments."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch JW complete")
