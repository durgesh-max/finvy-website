# -*- coding: utf-8 -*-
"""Batch GK (24 Nov 2026): GST refund for NRIs on Indian insurance premiums - why most individual policies no longer carry
GST from 22 September 2025, how NRIs claimed refunds on earlier premiums (export of service, NRE / foreign currency
payment), and what still attracts GST. Call-first page.
Demand: sweep ac60 (24 Nov 2026), all 7 markets: "nri gst refund process", "nri gst refund icici prudential".
Facts (checked 24 Nov 2026): GST on individual life (including term) and individual health insurance premiums was cut to
nil from 22 September 2025 after the 56th GST Council meeting; group policies still attract 18% (Outlook Money, Policybazaar,
Oneassure, Axis Max Life). Before that, insurers refunded GST to NRI policyholders treated as export of service when the
premium was paid from an NRE account or in foreign exchange, with residence abroad shown; payments from NRO accounts were
generally not eligible; an advance ruling for an insurer considered NRE-account premiums under section 2(6) IGST Act
(GST Council advance ruling listing; ClearTax; Niva Bupa). Conditions are applied by each insurer."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 24 November 2026."
SLUG = "nri-gst-refund-insurance-premium-india-2026-nre-export-of-service-gst-exempt"

C = contact("the policy type (term, health, savings, group), the insurer, the premium dates and amounts, and which account you paid from")
L = lambda h, t: f'<a href="{h}">{t}</a>'
PAGES = [dict(
    slug=SLUG,
    title="GST Refund for NRIs on Insurance Premiums (2026): Why Most Individual Policies Now Carry No GST, and Refunds on Earlier Premiums",
    em="nil GST since 22 September 2025 for individual cover.",
    kicker="/ NRIs &middot; Insurance and GST &middot; Updated 2026-11-24",
    lead=("<strong>Since 22 September 2025, premiums on individual life insurance (including term plans) and individual health insurance carry no GST in India, for residents and NRIs alike, so there is nothing to refund on premiums paid after that date.</strong> "
          "For premiums paid <strong>before</strong> 22 September 2025, many insurers refunded the GST to NRI policyholders, treating the policy as an export of service, if the premium was paid from an <strong>NRE account</strong> or in foreign currency and the policyholder lived abroad; payments from an <strong>NRO account</strong> generally did not qualify. "
          "Group policies still carry 18% GST. Each insurer runs its own refund process and documents, so check with yours."),
    sections=[
        ("/ Quick answers", "What NRI policyholders ask.",
         ul("<strong>Is GST charged on insurance for NRIs in 2026?</strong> Not on individual life, term or health policies: GST on these premiums has been nil since 22 September 2025.",
            "<strong>How do NRIs claim a GST refund on insurance?</strong> For premiums paid before 22 September 2025, through the insurer&rsquo;s NRI refund process, usually with proof of residence abroad (passport and visa or residence permit) and proof that the premium came from an NRE account or from abroad.",
            "<strong>Does paying from an NRO account qualify?</strong> Generally not; NRO money is treated as rupee funds in India, so the service is not treated as an export.",
            "<strong>Is GST still charged on any insurance?</strong> Yes: group policies (for example employer group health) and other non-individual covers still carry 18%.",
            "<strong>Can I claim the premium as a tax deduction?</strong> Under the old regime, NRIs can claim life insurance premiums under the investment deduction limit and health insurance for themselves and resident parents within the health insurance limits; see " + L("nri-senior-citizen-tax-india-2026-exemption-limit-80ttb-advance-tax-15h-pension-retire-to-india.html", "NRI senior citizen tax") + " for the health insurance limits.")),
        ("/ Before and after 22 September 2025", "What changed.",
         table(["", "Up to 21 September 2025", "From 22 September 2025"], [
             ["Individual term and life insurance", "18% GST (lower on some savings plans); NRI refund possible as export of service", "Nil GST"],
             ["Individual health insurance", "18% GST; NRI refund possible as export of service", "Nil GST"],
             ["Group insurance", "18% GST", "18% GST"],
             ["NRI refund conditions", "Paid from NRE or abroad, policyholder resident abroad, insurer's process", "Not needed for individual policies"]])),
        ("/ Practical points", "Getting money back on older premiums.",
         ul("<strong>Ask the insurer</strong> for its NRI GST refund form and the periods it covers; processes and time limits differ.",
            "<strong>Keep proof:</strong> passport pages with visa or residence permit, overseas address, and the bank statement showing the NRE or foreign payment.",
            "<strong>Renewals:</strong> check that renewals after 22 September 2025 were billed without GST; if GST was charged on an individual policy, ask for a correction.",
            "<strong>Returning to India:</strong> once you become resident, any old export treatment ends; update your KYC and pay future premiums from resident accounts.",
            "<strong>Foreign policies:</strong> insurance taken abroad is a different question (reporting and tax on maturity); see " + L("foreign-life-insurance-policy-returning-nri-schedule-fa-fast-ds-tax-on-maturity.html", "foreign life insurance for returning NRIs") + ".")
         + call_box("insurance, GST and tax for NRIs", ["Whether an older premium qualifies for a GST refund",
                                                         "Correcting GST billed after 22 September 2025",
                                                         "Insurance deductions in your Indian return",
                                                         "NRE vs NRO for paying premiums",
                                                         "Returning NRI: policies and KYC"],
                    "your policies, insurers, premium dates and the account used.")
         + sources("GST Council, 56th meeting (September 2025) recommendations exempting individual life and health insurance from 22 September 2025, as reported by Outlook Money, Policybazaar and insurers; IGST Act, section 2(6) (export of services); GST advance ruling on NRE-account premiums for an insurer (GST Council advance ruling listing); ClearTax and Niva Bupa guides on GST refunds for NRIs. Checked 24 November 2026.")),
    ],
    faqs=[("Is GST charged on insurance premiums for NRIs in 2026?", "Not on individual life, term or health insurance: GST on these premiums has been nil since 22 September 2025, for residents and NRIs alike. Group policies still carry 18%."),
          ("How can an NRI get a GST refund on insurance premiums?", "For premiums paid before 22 September 2025, through the insurer's NRI refund process, treating the policy as an export of service: usually proof of residence abroad and proof that the premium was paid from an NRE account or from abroad."),
          ("Can NRIs get a GST refund if they paid from an NRO account?", "Generally no. Premiums paid from an NRO account are usually not treated as an export of service, so insurers do not refund the GST."),
          ("Is GST charged on group health insurance?", "Yes. The nil rate from 22 September 2025 applies to individual policies; group policies still attract 18% GST."),
          ("Do I still need to pay premiums from an NRE account?", "For GST purposes it no longer matters for individual policies since 22 September 2025. NRE funds keep the money repatriable, which can still be useful."),
          ("Can BQP help with insurance and tax as an NRI?", "Yes. " + C)],
    related=[("nre-nro-fcnr-account-tax-rules.html", "NRE, NRO and FCNR accounts"),
             ("nri-senior-citizen-tax-india-2026-exemption-limit-80ttb-advance-tax-15h-pension-retire-to-india.html", "NRI senior citizen tax"),
             ("foreign-life-insurance-policy-returning-nri-schedule-fa-fast-ds-tax-on-maturity.html", "Foreign life insurance for returning NRIs"),
             ("gst-on-export-of-services-lut-without-lut-invoice-format-refund-freelancer-startup-2026.html", "GST on export of services"),
             ("nri-mutual-funds-india-tax.html", "NRI mutual funds tax")],
    cta_h="Insurance in India while living abroad?", cta_b=C,
    keywords="NRI GST refund insurance, NRI GST refund process, GST on term insurance NRI 2026, GST exempt individual health insurance September 2025, NRE account insurance premium GST refund, export of service insurance NRI",
    desc="GST refund for NRIs on insurance (2026): individual life, term and health premiums carry nil GST since 22 September 2025; for earlier premiums, NRIs paying from NRE or abroad could claim GST back as export of service through the insurer; NRO payments usually not eligible; group policies still 18%.",
    howto={"name": "How an NRI checks GST on insurance premiums", "description": "Steps for current and past premiums.", "steps": [
        {"name": "Check the policy type", "text": "Individual life, term or health: nil GST from 22 September 2025; group: 18%."},
        {"name": "Check premium dates", "text": "Refunds are relevant only for premiums before 22 September 2025."},
        {"name": "Check the paying account", "text": "NRE or foreign payment usually needed for export treatment."},
        {"name": "Apply through the insurer", "text": "Use its NRI GST refund form with residence and payment proof."},
        {"name": "Check renewal invoices", "text": "Ask for correction if GST was charged after 22 September 2025."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch GK complete")
