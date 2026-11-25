# -*- coding: utf-8 -*-
"""Batch JB (25 Nov 2026): Private limited company registration in India 2026 - online process on the MCA V3 portal
through SPICe+ (INC-32): Part A name reservation (name valid for 20 days from approval), Part B incorporation with the
linked e-MoA (INC-33), e-AoA (INC-34) and AGILE-PRO-S (INC-35: GSTIN optional, EPFO, ESIC, professional tax in some
states, bank account), DINs for directors allotted through the form, PAN and TAN issued with the certificate of
incorporation. Requirements: at least 2 directors (one resident in India - 182 days in the financial year) and 2
shareholders, Class 3 DSC for signatories, no minimum capital, registered office proof. Name check: MCA name search,
Companies (Incorporation) Rules (rule 8 / 8A) and trade mark search. Company registration check: MCA 'View company
/ LLP master data' (free, CIN or name). After incorporation: INC-20A within 180 days, first auditor within 30 days,
bank account, statutory registers, DIR-3 KYC. Typical timeline one to three weeks. Draft Companies (Incorporation)
Amendment Rules, 2026 (8 April 2026) proposed SPICe+ changes - not confirmed as final.
Demand: sweep ac110 (25 Nov 2026), all 7 markets: "company registration india", "company registration india online",
"company registration india name check", "company registration india check", "company registration india search".
Facts (checked 25 Nov 2026): MCA SPICe+ FAQs and Part A instruction kit; India Briefing (AGILE-PRO-S); Cleartax,
IndiaFilings, Razorpay Rize guides; site foreign-national, INC-20A, ADT-1 and company-verification pages."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 25 November 2026."
SLUG = "private-limited-company-registration-india-2026-spice-plus-name-check-documents-directors-process"

C = contact("the proposed company names, the business activity, the directors and shareholders (and whether any are NRIs or foreign nationals), the state of the registered office and your timeline")
L = lambda h, t: f'<a href="{h}">{t}</a>'
PAGES = [dict(
    slug=SLUG,
    title="Private Limited Company Registration in India (2026): Online Process on MCA (SPICe+), Company Name Check, Documents, Directors and Timeline",
    em="one form, but the name and documents decide how fast it goes.",
    kicker="/ Founders, NRIs and foreign promoters &middot; Company incorporation &middot; Updated 2026-11-25",
    lead=("<strong>A private limited company is registered online on the MCA portal through the SPICe+ form: Part A reserves the name and Part B incorporates the company, with the memorandum, articles and AGILE-PRO-S filed alongside, and PAN and TAN issued with the certificate of incorporation.</strong> "
          "You need at least two directors (one resident in India) and two shareholders, digital signatures for the signatories and a registered office address; there is no minimum capital. "
          "Most incorporations take one to three weeks, and the main delays come from rejected names and document mismatches."),
    sections=[
        ("/ Requirements at a glance", "What you need before you file.",
         table(["Point", "Requirement"], [
             ["Directors", "At least 2; at least one resident in India (182 days in the financial year); DIN allotted through SPICe+"],
             ["Shareholders", "At least 2 (directors can be shareholders); NRIs and foreign nationals allowed under FDI rules"],
             ["Digital signatures", "Class 3 DSC for each director and subscriber who signs"],
             ["Capital", "No minimum paid-up capital"],
             ["Registered office", "Address proof and a recent utility bill, with the owner's no-objection where rented"],
             ["Identity documents", "PAN and address proof for Indian directors; passport and apostilled or notarised proofs for foreign nationals"]])
         + '<p>Foreign promoters: ' + L("can-foreign-national-register-company-in-india-how-long-documents-resident-director-2026.html", "can a foreign national register a company in India") + '. Choosing a structure: ' + L("which-is-better-llp-vs-private-limited-india.html", "LLP vs private limited") + ', ' + L("llp-registration-india-2026-process-documents-fillip-designated-partner-nri-foreign-partner.html", "LLP registration") + ' and ' + L("opc-registration-india-2026-one-person-company-process-documents-nri-nominee-compliance.html", "OPC registration") + '.</p>'),
        ("/ Company name check and SPICe+ process", "Step by step on the MCA portal.",
         ul("<strong>Check the name:</strong> search existing company and LLP names on the MCA portal and the trade marks register; avoid names identical or too similar to existing ones and restricted words under the incorporation rules.",
            "<strong>SPICe+ Part A:</strong> reserve the name (one or two choices); an approved name stays reserved for 20 days, within which Part B must be filed.",
            "<strong>SPICe+ Part B:</strong> enter capital, directors (DINs are allotted through the form), subscribers, registered office and declarations.",
            "<strong>Linked forms:</strong> e-MoA (INC-33), e-AoA (INC-34) and AGILE-PRO-S (INC-35) for EPFO, ESIC, optional GSTIN, professional tax in some states and the company bank account.",
            "<strong>Certificate of incorporation:</strong> issued with the CIN, PAN and TAN once the Registrar approves.",
            "<strong>Already registered?</strong> Anyone can check a company's status free on the MCA master data search; see " + L("how-to-verify-indian-company-is-genuine-mca-gst-iec-check-foreign-buyers-2026.html", "how to verify an Indian company") + ".")),
        ("/ After incorporation", "The first-year compliance.",
         ul("<strong>Commencement of business:</strong> file INC-20A within 180 days after subscribers pay for their shares; see " + L("form-inc-20a-commencement-of-business-180-days-penalty-applicability-india-2026.html", "INC-20A") + ".",
            "<strong>First auditor:</strong> the board appoints it within 30 days; see " + L("form-adt-1-auditor-appointment-15-days-first-auditor-rotation-adt-3-india-2026.html", "ADT-1 and auditor appointment") + ".",
            "<strong>Bank account, registers and share certificates:</strong> open the account, maintain statutory registers and issue share certificates.",
            "<strong>Directors&rsquo; KYC:</strong> DIR-3 KYC for each director; see " + L("dir-3-kyc-director-annual-compliance-india.html", "DIR-3 KYC") + ".",
            "<strong>Startup benefits:</strong> apply for free DPIIT recognition; see " + L("how-to-register-startup-india-dpiit.html", "Startup India registration") + ".",
            "<strong>GST:</strong> register when you cross the threshold or need it for interstate or online sales; see " + L("is-gst-registration-mandatory-for-startup-new-small-business-threshold-2026.html", "GST registration thresholds") + ".")
         + call_box("Company incorporation", ["Name search and SPICe+ filing",
                                               "NRI and foreign shareholder documentation",
                                               "FDI reporting (FC-GPR) for foreign capital",
                                               "INC-20A, auditor and first-year compliance",
                                               "DPIIT recognition and GST"],
                    "your proposed names, founders and business.")
         + sources("Companies Act, 2013 and Companies (Incorporation) Rules, 2014; MCA SPICe+ FAQs and instruction kits; India Briefing on AGILE-PRO-S; Cleartax, IndiaFilings and Razorpay Rize SPICe+ guides; site foreign-national, INC-20A, ADT-1 and company-verification guides. Draft Companies (Incorporation) Amendment Rules, 2026 noted, not treated as final. Checked 25 November 2026.")),
    ],
    faqs=[("How do I register a private limited company in India?", "File the SPICe+ form on the MCA portal: Part A to reserve the name and Part B to incorporate, with the e-MoA, e-AoA and AGILE-PRO-S. The certificate of incorporation comes with the CIN, PAN and TAN."),
          ("How do I check if a company name is available in India?", "Search existing company and LLP names on the MCA portal and the trade marks register, then apply through SPICe+ Part A; an approved name is reserved for 20 days."),
          ("How can I check whether a company is registered in India?", "Use the free MCA master data search with the company name or CIN to see its status, directors, capital and filing history."),
          ("How many directors and shareholders does a private limited company need?", "At least two directors, one of whom must be resident in India (in India for at least 182 days in the financial year), and at least two shareholders."),
          ("How long does company registration take in India?", "Usually one to three weeks, depending on name approval, digital signatures and document checks; foreign directors' apostilled documents can add time."),
          ("Can an NRI or foreign national register a company in India?", "Yes. NRIs and foreign nationals can be directors and shareholders, subject to FDI rules and at least one resident director; foreign capital must be reported to the RBI."),
          ("Can BQP register my company?", "Yes. CA Durgesh Chavda handles name search, SPICe+ filing, NRI and foreign promoter documentation, FDI reporting and first-year compliance. " + C)],
    related=[("can-foreign-national-register-company-in-india-how-long-documents-resident-director-2026.html", "Foreign national company registration"),
             ("which-is-better-llp-vs-private-limited-india.html", "LLP vs private limited"),
             ("opc-registration-india-2026-one-person-company-process-documents-nri-nominee-compliance.html", "OPC registration"),
             ("form-inc-20a-commencement-of-business-180-days-penalty-applicability-india-2026.html", "INC-20A"),
             ("how-to-verify-indian-company-is-genuine-mca-gst-iec-check-foreign-buyers-2026.html", "Verify an Indian company")],
    cta_h="Ready to incorporate?", cta_b=C,
    keywords="company registration india, private limited company registration, company registration india online, company name check india, company registration check, spice plus form, how to register a company in india, pvt ltd registration process",
    desc="Private limited company registration in India 2026: SPICe+ online process on MCA (name reservation, incorporation, e-MoA, e-AoA, AGILE-PRO-S), company name check, documents, two directors (one resident) and shareholders, timeline and first-year compliance.",
    howto={"name": "How to register a private limited company in India", "description": "Through SPICe+ on the MCA portal.", "steps": [
        {"name": "Get digital signatures", "text": "Class 3 DSC for directors and subscribers."},
        {"name": "Check and reserve the name", "text": "MCA and trade mark search, then SPICe+ Part A."},
        {"name": "File SPICe+ Part B", "text": "With e-MoA, e-AoA and AGILE-PRO-S within 20 days."},
        {"name": "Receive the certificate", "text": "CIN, PAN and TAN issued on approval."},
        {"name": "Complete first-year steps", "text": "Bank account, INC-20A, first auditor, DIR-3 KYC."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch JB complete")
