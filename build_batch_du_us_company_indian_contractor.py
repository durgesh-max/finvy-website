# -*- coding: utf-8 -*-
"""Batch DU (20 Nov 2026): US companies paying Indian contractors - US forms (W-8BEN / W-8BEN-E, no 1099-NEC for foreign
persons working outside the US), India tax and GST for the contractor (44ADA presumptive, export of services under LUT,
FIRA), misclassification and PE risk, when to switch to EOR or a subsidiary. Call-first page.
Demand: sweep 18 Nov (ac10) seeds "us company paying indian contractor", "form 1099 indian contractor", "w-8ben indian
freelancer"; site had W-8BEN and freelancer pages but nothing for the US payer.
Facts: payments to a foreign person for services performed outside the US are not US-source income, so no chapter 3
withholding and no Form 1099-NEC; the payer keeps Form W-8BEN (individual) or W-8BEN-E (entity) to document foreign
status; India - resident contractor taxed on the fees; section 44ADA presumptive (50% of receipts) for specified
professionals up to INR 75 lakh where cash receipts do not exceed 5%; GST registration above INR 20 lakh aggregate
turnover (exports count) - services to a foreign client meeting IGST Act section 2(6) are zero-rated exports, supplied
without IGST under a Letter of Undertaking (RFD-11); foreign inward remittance advice (FIRA) as proof; long-term
exclusive contractors can be treated as employees, and a contractor habitually concluding contracts can create a
permanent establishment."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 20 November 2026."
USC = "us-company-paying-indian-contractor-w-8ben-no-1099-gst-lut-pe-risk-2026"
HUB = "foreign-company-india-advisor-market-research-entity-due-diligence-m-and-a-joint-venture-2026"

C_USC = contact("how many Indian contractors you pay, their roles and duration, how they are paid, and whether they work only for you")
PAGES = [dict(
    slug=USC,
    title="US Company Paying Indian Contractors (2026): W-8BEN, No 1099, Indian Tax and GST for the Contractor, and When Contractors Become a Risk",
    em="for US startups and businesses with talent in India.",
    kicker="/ US companies &middot; Contractors &middot; India &middot; Updated 2026-11-20",
    lead=("A US company paying an Indian contractor for work done in India <strong>does not withhold US tax and does not issue Form 1099-NEC</strong>. The income is not US-source. Instead, collect <strong>Form W-8BEN</strong> from an individual contractor (or <strong>W-8BEN-E</strong> from an Indian company) and keep it on file. "
          "On the Indian side, the contractor pays Indian income tax on the fees; many professionals can use <strong>presumptive taxation</strong> (50% of receipts) up to INR 75 lakh. Once turnover crosses <strong>INR 20 lakh</strong> the contractor needs GST registration, and their invoices to you are <strong>zero-rated exports</strong> issued under a Letter of Undertaking, so you are not charged Indian GST. "
          "The risks are mostly yours. Long-term, full-time, exclusive contractors can be treated as <strong>employees</strong> under Indian law, and a contractor who negotiates or signs contracts for you can create a <strong>permanent establishment</strong>, making part of your profits taxable in India. That is the point to consider an employer of record or an Indian subsidiary."),
    sections=[
        ("/ Who does what", "US company vs Indian contractor.",
         table(["Topic", "US company (payer)", "Indian contractor"], [
             ["Tax forms", "Collect W-8BEN (individual) or W-8BEN-E (entity); no Form 1099-NEC for services performed outside the US", "Provide W-8BEN / W-8BEN-E; report fees in the Indian return"],
             ["Withholding", "None in the US for services performed in India", "Pays advance tax in India; presumptive scheme may apply"],
             ["GST", "Not charged on export invoices under LUT", "Register above INR 20 lakh; file LUT; issue export invoices without IGST"],
             ["Payment proof", "Keep invoices and contracts", "Keep FIRA / bank advice for export proof"],
             ["Agreement", "Scope, deliverables, IP assignment, confidentiality, termination", "Independent business terms; no exclusivity clauses that look like employment"]])
         + call_box("paying contractors in India", ["Whether your contractors look like employees under Indian law",
                                                    "Permanent establishment risk from contractor roles",
                                                    "Contract terms for IP, confidentiality and termination",
                                                    "When an employer of record or Indian subsidiary becomes cheaper and safer",
                                                    "For contractors: GST, LUT and presumptive tax set-up"],
                    "the number of contractors, their roles, how long they have worked for you, and how they are paid.")),
        ("/ When contractors become a risk", "Signs you have outgrown the model.",
         ul("<strong>Employment look:</strong> fixed hours, your equipment, your managers, exclusivity, monthly fixed pay and long tenure point to employment; Indian labour and provident fund rules may then apply.",
            "<strong>Permanent establishment:</strong> a contractor who habitually negotiates or concludes contracts for you, or a fixed place at your disposal, can make part of your profits taxable in India; see <a href=\"permanent-establishment-india-meaning-types-risk-tax-foreign-company-2026.html\">permanent establishment</a>.",
            "<strong>IP ownership:</strong> without a clear assignment, code and designs may legally belong to the contractor.",
            "<strong>Scale:</strong> several full-time people in India usually justify an employer of record or a subsidiary; see <a href=\"employer-of-record-india-hire-from-abroad.html\">employer of record</a>, <a href=\"foreign-company-remote-employee-india-pe-risk-eor-contractor-subsidiary-2026.html\">contractor vs EOR vs subsidiary</a> and <a href=\"gcc-global-capability-centre-india-setup-us-company-safe-harbour-2026.html\">India capability centres</a>.")),
        ("/ For the Indian contractor", "Getting paid in dollars, compliantly.",
         ul("<strong>Income tax:</strong> fees are taxable in India; specified professionals can declare 50% of receipts as income under section 44ADA (up to INR 75 lakh if cash receipts are within 5%); see <a href=\"freelancer-consultant-tax-india-2026-complete.html\">freelancer tax guide</a>.",
            "<strong>GST:</strong> register once aggregate turnover (including exports) exceeds INR 20 lakh; file a Letter of Undertaking each year and invoice the US client without IGST if export conditions are met.",
            "<strong>Platforms and accounts:</strong> balances held abroad (PayPal, Wise, Payoneer) may need reporting; see <a href=\"wise-payoneer-paypal-revolut-balance-schedule-fa-freelancer-fast-ds.html\">foreign balances and Schedule FA</a>.",
            "<strong>W-8BEN:</strong> see <a href=\"what-is-form-w-8ben.html\">what is Form W-8BEN</a>.")
         + f'<p>Related: <a href="{HUB}.html">working with an Indian CA as a foreign company</a> &middot; <a href="us-incorporation.html">US incorporation</a>.</p>'
         + sources("US Internal Revenue Code source rules for personal services and IRS instructions for Forms W-8BEN, W-8BEN-E and 1099-NEC; Income-tax Act provisions on presumptive taxation (section 44ADA) and residency; CGST and IGST Acts (section 2(6) export of services, LUT under rule 96A); India&rsquo;s labour codes and permanent establishment rules under treaties. General information; confirm US positions with your US tax adviser.")),
    ],
    faqs=[("Does a US company need to issue a 1099 to an Indian contractor?", "No. Payments to a foreign person for services performed outside the US are not US-source income, so Form 1099-NEC is not required; collect and keep Form W-8BEN or W-8BEN-E instead."),
          ("Does a US company withhold tax on payments to an Indian contractor?", "Not for services performed in India. The contractor pays tax in India on the fees."),
          ("Does an Indian contractor charge GST to a US client?", "Usually not. Services to a foreign client meeting the export conditions are zero-rated and invoiced without IGST under a Letter of Undertaking; registration is needed above INR 20 lakh turnover."),
          ("Can paying Indian contractors create tax risk for a US company?", "Yes, if contractors look like employees or habitually conclude contracts for the company, which can create employment obligations or a permanent establishment in India."),
          ("When should a US company switch from contractors to an EOR or subsidiary?", "When people work full-time and exclusively for long periods, when headcount grows, or when roles involve selling or signing contracts in India."),
          ("Can BQP review our India contractor set-up?", "Yes. " + C_USC)],
    related=[("foreign-company-remote-employee-india-pe-risk-eor-contractor-subsidiary-2026.html", "Contractor vs EOR vs subsidiary"), ("what-is-form-w-8ben.html", "What is Form W-8BEN"),
             (HUB + ".html", "Working with an Indian CA")],
    cta_h="Paying contractors in India?", cta_b=C_USC,
    keywords="US company paying Indian contractor, 1099 for Indian contractor, W-8BEN Indian contractor, W-8BEN-E Indian company, hire contractors in India from US, Indian freelancer GST export LUT, 44ADA freelancer US clients, contractor misclassification India PE risk",
    desc="US company paying Indian contractors (2026): no US withholding or Form 1099-NEC for work done in India; collect W-8BEN / W-8BEN-E; contractor's Indian tax (44ADA) and GST export under LUT; misclassification and permanent establishment risk; when to move to EOR or a subsidiary.",
    howto={"name": "How a US company pays Indian contractors correctly", "description": "Steps for US payers.", "steps": [
        {"name": "Collect W-8BEN or W-8BEN-E", "text": "Document foreign status; no 1099-NEC for services outside the US."},
        {"name": "Sign a contractor agreement", "text": "Deliverables, IP assignment, confidentiality, non-exclusive terms."},
        {"name": "Receive compliant invoices", "text": "Export invoices under LUT where the contractor is GST-registered."},
        {"name": "Watch the risk signs", "text": "Full-time exclusive roles, selling or signing contracts, long tenure."},
        {"name": "Move when needed", "text": "Employer of record or Indian subsidiary as the team grows."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch DU complete:", len(PAGES))
