# -*- coding: utf-8 -*-
"""Batch LH (28 Nov 2026): MSME delayed payment recovery - the 45-day rule, compound interest at three times the RBI bank rate,
MSME Samadhan reference to the Micro and Small Enterprises Facilitation Council (MSEFC), conciliation and arbitration, the 75%
pre-deposit for challenging an award, and the buyer-side consequences.
Demand: 'msme delayed payment', 'msme samadhan complaint', 'msme 45 days payment rule', 'msefc case', 'interest on delayed payment
to msme' - mentioned on the Udyam, 43B(h), tax audit and MSME Form I pages but no dedicated recovery page. Very high hire intent:
micro and small suppliers chasing dues need help with the reference and documents. User steer 26 Nov 2026: more call bookings.
Facts (Micro, Small and Medium Enterprises Development Act, 2006): section 15 - the buyer must pay a micro or small supplier by the
agreed date, which cannot exceed 45 days from acceptance or deemed acceptance; with no agreement, within 15 days; section 16 -
compound interest with monthly rests at three times the bank rate notified by RBI on late payment; section 17 - the buyer is liable
for the amount with interest; section 18 - either party can refer the dispute to the MSEFC, which conducts conciliation and, if that
fails, arbitration (or refers it), with the award due within 90 days of the reference; MSME Samadhan is the online portal for filing
such references; section 19 - an application to set aside an award or decree needs a deposit of 75% of the amount; section 22 -
buyers must disclose unpaid MSE dues and interest in their accounts; section 23 - interest under section 16 is not deductible for
income tax. Benefits are for micro and small suppliers (not medium); courts have linked eligibility to Udyam registration at the time
of the contract. Section 43B(h) of the Income-tax Act separately disallows the buyer's deduction until payment. No fees, no portal
menu paths. advisory_lib.contact() is not used."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources
from build_lib import page, write_page

A.UPDATED = "Last updated: 28 November 2026."
SLUG = "msme-delayed-payment-recovery-samadhan-msefc-45-days-section-15-16-interest-3x-bank-rate-2026"

C = ("WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with your Udyam certificate (and its date), the purchase "
     "order or contract, invoices and delivery or acceptance proof, the payment terms, and what has been paid so far. Or book a "
     "call directly.")
PAGES = [dict(
    slug=SLUG,
    title="MSME Delayed Payment Recovery (2026): The 45-Day Rule, Interest at Three Times the RBI Bank Rate, MSME Samadhan and MSEFC Conciliation and Arbitration",
    em="the law is on the small supplier&rsquo;s side - use it.",
    kicker="/ Micro and small suppliers with dues stuck &middot; MSMED Act sections 15 to 23 &middot; Updated 2026-11-28",
    lead=("<strong>If you are a micro or small enterprise, a buyer must pay you within the agreed period - never more than 45 days from acceptance, or 15 days if nothing was agreed. "
          "Late payment carries compound interest with monthly rests at three times the RBI bank rate, and you can refer the dispute to the Micro and Small Enterprises Facilitation Council through MSME Samadhan for conciliation and arbitration.</strong>"),
    sections=[
        ("/ Your rights under the MSMED Act", "Sections 15 to 23.",
         table(["Section", "Rule"], [
             ["15 - payment period", "As agreed in writing, but not more than 45 days from acceptance or deemed acceptance; 15 days if no agreement"],
             ["16 - interest", "Compound interest with monthly rests at three times the RBI bank rate, from the due date"],
             ["17 - liability", "Buyer liable for the principal with that interest"],
             ["18 - reference", "Either party can refer to the MSEFC: conciliation first, then arbitration; award within 90 days of reference"],
             ["19 - challenging an award", "Buyer must deposit 75% of the amount awarded to apply to set it aside"],
             ["22 - disclosure", "Buyers must disclose unpaid MSE dues and interest in their annual accounts"],
             ["23 - tax", "Interest payable under section 16 is not deductible for the buyer&rsquo;s income tax"]])
         + ul("<strong>Who benefits:</strong> micro and small suppliers - not medium enterprises. Courts have tied eligibility to Udyam registration at the time of the contract, so check your registration date.",
              "<strong>Separate tax push:</strong> section 43B(h) of the Income-tax Act stops buyers deducting purchases from micro and small suppliers until they pay within the MSMED Act period.")),
        ("/ Recovering your dues", "From reminder to award.",
         ul("<strong>Build the file:</strong> Udyam certificate, purchase order or contract, invoices, delivery challans, acceptance or inspection proof, ledger confirmation and correspondence.",
            "<strong>Demand in writing:</strong> a notice citing sections 15 and 16, with the principal and interest computed, often prompts payment.",
            "<strong>File on MSME Samadhan:</strong> the reference goes to the MSEFC of the state where the supplier is located; attend conciliation with a clear computation.",
            "<strong>Arbitration and award:</strong> if conciliation fails, the Council arbitrates or refers the matter; an award is enforceable like a decree.",
            "<strong>Buyer challenges:</strong> a buyer seeking to set aside the award must first deposit 75% of the amount.")
         + call_box("MSME delayed payment recovery", ["Eligibility and Udyam date check",
                                                      "Principal and section 16 interest computation",
                                                      "Demand notice",
                                                      "MSME Samadhan reference and conciliation",
                                                      "Arbitration support and award enforcement"],
                    "Udyam certificate, contract, invoices, acceptance proof, payments received.")
         + sources("Micro, Small and Medium Enterprises Development Act, 2006 (sections 15 to 23); Income-tax Act, 1961 (section 43B(h)) and the corresponding provisions of the Income-tax Act, 2025; MSME Samadhan portal; Supreme Court decisions on MSEFC references; site Udyam, 43B(h) and MSME Form I pages.")),
    ],
    faqs=[("What is the 45-day payment rule for MSMEs?", "Under section 15 of the MSMED Act, a buyer must pay a micro or small supplier by the agreed date, which cannot be more than 45 days from acceptance or deemed acceptance of the goods or services. If there is no written agreement, payment is due within 15 days."),
          ("What interest can an MSME claim on delayed payment?", "Compound interest with monthly rests at three times the bank rate notified by the RBI, from the due date until payment, under section 16 of the MSMED Act."),
          ("How do I file an MSME delayed payment complaint?", "File a reference on the MSME Samadhan portal to the Micro and Small Enterprises Facilitation Council of your state, with your Udyam certificate, contract, invoices and acceptance proof. The Council tries conciliation first and then arbitration."),
          ("Can a medium enterprise use MSME Samadhan?", "No. The payment protection in sections 15 to 23 is for micro and small suppliers. Courts have also linked eligibility to Udyam registration at the time of the contract."),
          ("What happens if the buyer challenges the MSEFC award?", "To apply to set aside the award, the buyer must first deposit 75% of the amount awarded, which strongly favours the supplier."),
          ("What should I send to start?", "WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with your Udyam certificate and its date, the contract or purchase order, invoices, acceptance proof and payments received. Or book a call directly.")],
    related=[("udyam-msme-registration-benefits-india-2026.html", "Udyam MSME registration and benefits"),
             ("section-43b-h-year-2-impact-buyers-mse-india.html", "Section 43B(h): impact on buyers"),
             ("msme-form-i-half-year-october-2026-due-date.html", "MSME Form I half-yearly return"),
             ("form-3ca-3cb-3cd-tax-audit-india-2026-checklist.html", "Tax audit checklist")],
    cta_h="Buyer not paying your MSME invoices?", cta_b=C,
    keywords="msme delayed payment, msme samadhan complaint, msme 45 days payment rule, msefc case, interest on delayed payment to msme 3 times bank rate, section 15 16 msmed act, msme payment recovery",
    desc="MSME delayed payment recovery: buyer must pay micro and small suppliers within the agreed period (max 45 days, 15 if none) under section 15; compound interest at three times the RBI bank rate under section 16; MSME Samadhan reference to MSEFC, conciliation and arbitration in 90 days; 75% deposit to challenge.",
    howto={"name": "How to recover delayed MSME payments", "description": "From notice to award.", "steps": [
        {"name": "Check eligibility", "text": "Micro or small, with Udyam registration in place when the contract was made."},
        {"name": "Compute dues", "text": "Principal plus compound interest at three times the RBI bank rate from the due date."},
        {"name": "Send a demand notice", "text": "Cite sections 15 and 16 with the computation."},
        {"name": "File on MSME Samadhan", "text": "Reference to the state MSEFC; conciliation, then arbitration."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch LH complete")
