# -*- coding: utf-8 -*-
"""Batch EE (20 Nov 2026): RBI's 2 November 2026 amendment to the FEMA export and import regulations - deemed EDF for
service exporters who are resident individuals (any amount) and for other exporters on inward remittances up to INR 10
lakh; IDPMS entry for import of services only for non-individual importers above INR 10 lakh. Call-first page.
Facts (RBI notification page, checked 20 Nov 2026): Foreign Exchange Management (Export and Import of Goods and Services)
(Second Amendment) Regulations, 2026, notification FEMA 23(R)/(2)/2026-RB dated 2 November 2026, stated to come into
force from 1 October 2026; inserts 'resident individual' = a person resident in India who is a natural person;
regulation 3(2) provisos - (a) a resident individual exporter of services is deemed to have submitted the EDF when it
gives the AD bank the information needed to receive and credit the payment; (b) any other exporter is deemed to have
submitted the EDF where the inward remittance for the service is not more than INR 10 lakh; regulation 18(1)(d) - AD
bank enters import-of-services details in IDPMS only where the importer is not a resident individual and the invoice or
contract value exceeds INR 10 lakh, within five working days of receipt of details. Principal regulations (13 January
2026) continue: nine-month realisation, monthly EDF for other service exports (site page)."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 20 November 2026."
SLUG = "fema-services-export-edf-relief-freelancers-10-lakh-rbi-amendment-2-november-2026"
OLD = "fema-export-rules-1-october-2026-nine-month-realisation-edf-services"

C = contact("whether you export services as an individual or a company, your typical invoice sizes, your bank, and any EDF reminders you have received")
PAGES = [dict(
    slug=SLUG,
    title="FEMA Relief for Service Exporters (RBI, 2 November 2026): Freelancers Deemed to Have Filed EDF, Companies Too for Remittances up to INR 10 Lakh",
    em="what the second amendment to the 2026 export regulations changes.",
    kicker="/ FEMA &middot; Service exports &middot; Freelancers &middot; Updated 2026-11-20",
    lead=("On <strong>2 November 2026</strong> the RBI notified the <strong>Foreign Exchange Management (Export and Import of Goods and Services) (Second Amendment) Regulations, 2026</strong> (FEMA 23(R)/(2)/2026-RB), stated to apply from 1 October 2026. "
          "It eases the monthly <strong>EDF</strong> (export declaration) filing that the new 2026 regulations introduced for service exports. A <strong>resident individual</strong>, such as a freelancer or consultant billing foreign clients, is now <strong>deemed to have filed the EDF</strong> once they give their bank the information needed to receive and credit the payment, whatever the amount. <strong>Companies, LLPs and firms</strong> get the same deemed filing for inward remittances of <strong>up to INR 10 lakh</strong> per service. "
          "On the import side, banks need to enter import-of-services details in IDPMS only for <strong>non-individual importers</strong> with invoices or contracts above <strong>INR 10 lakh</strong>. The nine-month realisation rule from the 2026 regulations is not changed by this amendment."),
    sections=[
        ("/ What changed", "Before and after the amendment.",
         table(["Who", "Before (from 1 October 2026)", "After the 2 November 2026 amendment"], [
             ["Resident individual exporting services (freelancer, consultant)", "Monthly EDF for service exports", "Deemed to have filed the EDF once payment details are given to the bank; no amount limit"],
             ["Company, LLP or firm exporting services", "Monthly EDF for service exports", "Deemed EDF where the inward remittance for the service is up to INR 10 lakh; above that, the normal EDF process"],
             ["Import of services by an individual", "IDPMS entry by the bank", "No IDPMS entry needed"],
             ["Import of services by a company", "IDPMS entry within five working days of receipt of documents", "IDPMS entry only above INR 10 lakh invoice or contract value, within five working days of receipt of details"],
             ["Realisation of export proceeds", "Nine months (12 months for INR invoices)", "Unchanged by this amendment"]])
         + call_box("FEMA filings for my service exports", ["Whether the deemed EDF covers your receipts",
                                                            "What your bank still needs from you",
                                                            "Realisation deadlines and overdue receivables",
                                                            "GST export of services under LUT and FIRA proof",
                                                            "For companies above INR 10 lakh: setting up the monthly EDF process"],
                    "your status (individual or company), bank, typical invoice values and any bank reminders on EDF.")),
        ("/ What to do now", "For freelancers, startups and service companies.",
         ul("<strong>Freelancers and consultants:</strong> make sure your bank has your purpose code and invoice details for each foreign receipt; the amendment treats that as the EDF.",
            "<strong>Companies and LLPs:</strong> map which receipts are up to INR 10 lakh (deemed) and which are larger (normal EDF); keep invoice and contract records by client.",
            "<strong>Realisation:</strong> track the nine-month realisation window from the invoice date and follow up overdue receivables; see <a href=\"" + OLD + ".html\">FEMA export rules from 1 October 2026</a>.",
            "<strong>GST:</strong> exports of services are zero-rated under a Letter of Undertaking where conditions are met; keep FIRA / bank advice as proof.",
            "<strong>Indian companies buying services from abroad:</strong> IDPMS entries apply only above INR 10 lakh; withholding tax and GST reverse charge rules are unchanged; see <a href=\"technology-licensing-royalty-payment-indian-company-to-foreign-company-fema-tds-gst-2026.html\">payments abroad for licences and services</a>.")
         + '<p>Related: <a href="freelancer-consultant-tax-india-2026-complete.html">freelancer tax guide</a> &middot; <a href="us-company-paying-indian-contractor-w-8ben-no-1099-gst-lut-pe-risk-2026.html">US companies paying Indian contractors</a> &middot; <a href="wise-payoneer-paypal-revolut-balance-schedule-fa-freelancer-fast-ds.html">foreign payment platforms and Schedule FA</a>.</p>'
         + sources("Foreign Exchange Management (Export and Import of Goods and Services) (Second Amendment) Regulations, 2026, notification FEMA 23(R)/(2)/2026-RB dated 2 November 2026 (RBI notification page); principal regulations FEMA 23(R)/2026-RB dated 13 January 2026 and First Amendment dated 22 September 2026. The stated effective date (1 October 2026) should be checked against the Gazette copy; confirm your bank's process.")),
    ],
    faqs=[("What did the RBI change for service exporters on 2 November 2026?", "Resident individuals exporting services are deemed to have submitted the EDF once they give their bank the payment details, and other exporters get the same deemed filing for inward remittances up to INR 10 lakh."),
          ("Do freelancers still need to file the monthly EDF?", "Under the amendment, a resident individual is deemed to have submitted the EDF when they furnish the information needed for the bank to receive and credit the payment, with no amount limit."),
          ("Does the INR 10 lakh limit apply to individuals?", "No. The INR 10 lakh threshold applies to exporters other than resident individuals, such as companies, LLPs and firms."),
          ("Has the nine-month realisation rule changed?", "No. The amendment does not change the realisation period set by the 2026 regulations."),
          ("What changed for imports of services?", "Banks enter import-of-services details in IDPMS only for importers that are not resident individuals and where the invoice or contract exceeds INR 10 lakh."),
          ("Can BQP help with export FEMA and GST compliance?", "Yes. " + C)],
    related=[(OLD + ".html", "FEMA export rules from 1 October 2026"), ("freelancer-consultant-tax-india-2026-complete.html", "Freelancer tax guide"),
             ("us-company-paying-indian-contractor-w-8ben-no-1099-gst-lut-pe-risk-2026.html", "US companies paying Indian contractors")],
    cta_h="Exporting services from India?", cta_b=C,
    keywords="FEMA EDF services export relief November 2026, RBI second amendment export import regulations 2026, freelancer EDF deemed, EDF 10 lakh remittance, IDPMS import of services 10 lakh, FEMA 23(R)/(2)/2026-RB",
    desc="RBI's 2 November 2026 amendment (FEMA 23(R)/(2)/2026-RB): resident individuals exporting services are deemed to have filed the EDF; companies and others too for remittances up to INR 10 lakh; IDPMS entry for service imports only for non-individuals above INR 10 lakh; realisation unchanged.",
    howto={"name": "How service exporters apply the November 2026 FEMA relief", "description": "Steps for freelancers and companies.", "steps": [
        {"name": "Check your status", "text": "Resident individual (any amount) or company / LLP / firm (up to INR 10 lakh per remittance)."},
        {"name": "Give the bank complete details", "text": "Purpose code, invoice and client details for each receipt."},
        {"name": "Run EDF for larger receipts", "text": "Companies: normal EDF process above INR 10 lakh."},
        {"name": "Track realisation", "text": "Nine months from invoice date (12 months for INR invoices)."},
        {"name": "Keep GST and tax records", "text": "LUT, export invoices, FIRA and income-tax records."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch EE complete")
