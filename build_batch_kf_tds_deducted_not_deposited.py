# -*- coding: utf-8 -*-
"""Batch KF (27 Nov 2026): TDS deducted by the employer (or any payer) but not deposited - what it means for the employee,
section 205, the CBDT office memorandum of 11 March 2016, claiming credit, answering the demand, and the employer's liability.
Demand: sweep ac159 (27 Nov 2026), all 7 markets: "what happens if tds is deducted by employer but not deposited", plus
"tds mismatch notice reasons / intimation notice" and "outstanding tax demand"; no site page covered the case.
User steer 26 Nov 2026: more call bookings / WhatsApp enquiries - employees facing a demand for tax already cut from their
salary need a CA to reply and chase the credit.
Facts (verified 27 Nov 2026 by web search): section 205 bars a direct demand on the assessee to the extent tax was deducted
from their income; CBDT office memorandum F.No. 275/29/2014-IT(B) dated 11 March 2016 (reiterating a June 2015 letter)
directs that demands arising only because the deductor did not deposit deducted TDS are not to be enforced against the
deductee; tribunals and courts have allowed credit on the strength of Form 16 / 16A evidence, though outcomes are not
uniform and some decisions deny credit where the deposit is not in the records; the deductor is liable for the tax, interest
under section 201(1A) and penalty / prosecution provisions; corresponding provisions of the Income-tax Act, 2025 apply from
1 April 2026 (1961 Act section numbers used as people search them). Form 168 is the old 26AS; Form 130 the old Form 16.
No fees, no office claims, no statistics, no portal menu paths."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 27 November 2026."
SLUG = "tds-deducted-by-employer-but-not-deposited-section-205-cbdt-2016-credit-demand-what-to-do-2026"

C = contact("your salary slips or Form 130 (old Form 16) showing the TDS, your Form 168 (old 26AS) and AIS for the year, the 143(1) intimation or demand notice if one has come, the employer's name and TAN, and any emails with the employer about the missing deposit")
PAGES = [dict(
    slug=SLUG,
    title="TDS Deducted by Employer but Not Deposited (2026): Section 205, the CBDT 2016 Instruction, Claiming Credit and Answering the Demand",
    em="the tax was cut from your salary - you should not pay it twice.",
    kicker="/ Salaried employees, contractors and landlords whose TDS is missing from Form 168 (old 26AS) &middot; Updated 2026-11-27",
    lead=("<strong>If your employer deducted TDS from your salary but did not deposit it, the tax does not show in your Form 168 (old 26AS) and the return gets a demand or a reduced refund - but section 205 bars the department from collecting that tax from you again, and a CBDT instruction of 11 March 2016 tells officers not to enforce such demands against the employee.</strong> "
          "The fix is to prove the deduction (salary slips, Form 16), press the employer to deposit and file a correction, and answer any demand citing section 205 and the instruction."),
    sections=[
        ("/ What happens", "Why the demand appears, and why it should not stick.",
         table(["Point", "What it means for you"], [
             ["TDS missing from Form 168 / AIS", "The return's TDS claim is reduced when processed, creating a demand or a smaller refund"],
             ["Section 205", "No direct demand on you for tax that was deducted from your income"],
             ["CBDT office memorandum, 11 March 2016", "Demands arising only because the deductor did not deposit TDS are not to be enforced against the deductee"],
             ["Credit for the tax", "Often allowed on the strength of Form 16 / salary slips, but tribunal decisions are not uniform - evidence matters"],
             ["The employer", "Liable for the tax, interest for late deposit and penalty or prosecution provisions"]])
         + ul("<strong>Not the same as a late filing:</strong> sometimes the employer deposited the tax but filed the TDS return late or with the wrong PAN - a correction statement fixes that, and the credit then appears.",
              "<strong>Contractors, landlords and NRIs</strong> paid after TDS face the same issue when the payer does not deposit; the same protections apply.")),
        ("/ What to do", "Step by step.",
         ul("<strong>Check Form 168 (old 26AS) and AIS</strong> to see whether the TDS is missing, or present under a different PAN or quarter.",
            "<strong>Collect proof of deduction:</strong> salary slips, Form 130 (old Form 16), bank statements showing net salary credited.",
            "<strong>Ask the employer in writing</strong> to deposit the tax and file or correct the TDS return; keep the correspondence.",
            "<strong>File your return claiming the TDS</strong> shown in Form 16, with the proof ready.",
            "<strong>If a 143(1) demand comes:</strong> respond on the portal disagreeing with the demand, citing section 205 and the CBDT office memorandum of 11 March 2016, and attach the proof; raise a grievance if it is still pursued.",
            "<strong>If recovery is pressed</strong> or a refund is adjusted against it, write to the Assessing Officer with the evidence; an appeal is the next step if credit is refused.")
         + call_box("Missing TDS and demands", ["Form 168 / AIS reconciliation",
                                                "Reply to 143(1) demands citing section 205",
                                                "Letters to the employer and the Assessing Officer",
                                                "Refund adjustment and appeals",
                                                "TDS correction for employers and payers"],
                    "Salary slips, Form 16, Form 168 and the demand.")
         + sources("Income-tax Act, 1961, sections 199, 201, 205 and 271C, and the corresponding provisions of the Income-tax Act, 2025; CBDT office memorandum F.No. 275/29/2014-IT(B) dated 11 March 2016; tribunal and High Court decisions allowing credit on Form 16 evidence (outcomes vary); site 143(1) intimation, refund and TDS demand guides. Checked 27 November 2026.")),
    ],
    faqs=[("What happens if TDS is deducted by the employer but not deposited?", "The tax does not appear in your Form 168 (old 26AS), so when your return is processed the TDS claim is cut and a demand or smaller refund follows. But section 205 bars a direct demand on you for tax already deducted from your income, and a CBDT office memorandum of 11 March 2016 tells officers not to enforce such demands against the employee. The employer remains liable for the tax, interest and penalties."),
          ("Do I have to pay the tax again if my employer did not deposit my TDS?", "No - not for the tax that was actually deducted. Prove the deduction with salary slips and Form 130 (old Form 16), and answer any demand citing section 205 and the 2016 CBDT instruction. Credit for the tax itself is often allowed on that evidence, though tribunal decisions are not uniform, so keep the proof."),
          ("How do I reply to a demand for TDS my employer did not deposit?", "Respond to the 143(1) demand on the portal by disagreeing with it, cite section 205 and the CBDT office memorandum F.No. 275/29/2014-IT(B) of 11 March 2016, and attach the salary slips, Form 16 and the employer correspondence. If the demand is still pursued or a refund is adjusted, write to the Assessing Officer and, if needed, appeal."),
          ("Why is my TDS not showing in Form 26AS?", "Either the deductor did not deposit it, filed the TDS return late, or quoted a wrong PAN, amount or quarter. Check AIS and ask the deductor - a correction statement fixes errors and late filing; non-deposit is the employer's default, covered by section 205."),
          ("What action can be taken against an employer who does not deposit TDS?", "The employer is liable for the tax with interest under section 201(1A), can face penalty and, for deducted tax not deposited, prosecution provisions. Employees can also report the default to the TDS jurisdictional officer with their evidence."),
          ("What should I send if my TDS is missing?", "WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with your salary slips or Form 130 (old Form 16), Form 168 (old 26AS) and AIS, the 143(1) intimation or demand if any, and the employer's name and TAN. We reconcile the figures, draft the reply and the letters, and track the credit. You keep your own e-filing login.")],
    related=[("section-143-1-intimation-response-india-2026.html", "143(1) intimation and demand"),
             ("itr-refund-delayed-2026-why-and-what-to-do.html", "Income tax refund not received"),
             ("stay-of-income-tax-demand-20-percent-rule-budget-2026-10-percent-how-to-apply-format-2026.html", "Stay of income tax demand"),
             ("revised-itr-section-139-5-deadline-31-december-2026-india.html", "Revised ITR by 31 December 2026")],
    cta_h="TDS cut but not credited?", cta_b=C,
    keywords="tds deducted but not deposited, tds deducted by employer but not deposited, section 205 income tax, cbdt office memorandum 2016 tds, tds not showing in 26as, tds mismatch notice, employer not depositing tds, demand for tds not deposited",
    desc="TDS deducted by your employer but not deposited? Section 205 bars a direct demand on you and a CBDT instruction of 11 March 2016 says such demands are not to be enforced. How to prove the deduction, answer the 143(1) demand and claim credit; the employer's liability.",
    howto={"name": "What to do when TDS was deducted but not deposited", "description": "From spotting it to resolving the demand.", "steps": [
        {"name": "Check Form 168 and AIS", "text": "Confirm the TDS is missing and not under another PAN or quarter."},
        {"name": "Gather proof", "text": "Salary slips, Form 16 and bank credits showing net pay."},
        {"name": "Write to the employer", "text": "Ask them to deposit the tax and file or correct the TDS return."},
        {"name": "Answer any demand", "text": "Disagree on the portal citing section 205 and the 2016 CBDT instruction, with the proof."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch KF complete")
