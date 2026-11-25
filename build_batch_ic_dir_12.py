# -*- coding: utf-8 -*-
"""Batch IC (25 Nov 2026): Form DIR-12 - particulars of appointment of directors and key managerial personnel and changes
among them (section 170(2) of the Companies Act, 2013 read with rule 18 of the Companies (Appointment and Qualification of
Directors) Rules, 2014): within 30 days of appointment, change in designation or cessation; on resignation the company
files DIR-12 within 30 days of receiving the notice (section 168(1)); resigning director may file DIR-11 (section 168(1),
rule 16). Additional fees on late filing: 2x up to 30 days, 4x / 6x / 10x for longer delays, 12x beyond 180 days.
Section 172 penalty for default in sections 170 etc.: Rs 50,000 on company and each officer in default, Rs 500 per day
for continuing default, up to Rs 3 lakh (company) / Rs 1 lakh (officer) - stated as the section's general penalty.
Demand: sweep ac107 (25 Nov 2026), all 7 markets: "dir 12", "dir 12 meaning", "dir 12 due date", "dir 12 late fees",
"dir 12 form purpose", "dir 12 full form".
Facts (checked 25 Nov 2026): Taxguru (eForm DIR-12), Quicko, Razorpay Rize, legaldev and registerkaro guides; MCA DIR-11
instruction kit. Exact fee band edges vary between sources, so bands are described with the end points only."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 25 November 2026."
SLUG = "form-dir-12-director-appointment-resignation-30-days-late-fees-dir-11-india-2026"

C = contact("the company name, the director or KMP concerned, the date of appointment, change or resignation, and whether the DIN and DIR-3 KYC are active")
L = lambda h, t: f'<a href="{h}">{t}</a>'
PAGES = [dict(
    slug=SLUG,
    title="Form DIR-12 (2026): Director Appointment, Resignation and Change, 30-Day Due Date, Late Fees and DIR-11",
    em="file within 30 days of every board change.",
    kicker="/ Companies changing directors or KMP &middot; Company law &middot; Updated 2026-11-25",
    lead=("<strong>Form DIR-12 is the e-form a company files with the Registrar of Companies within 30 days of appointing a director or key managerial personnel (KMP), changing their designation, or when they resign or cease to hold office.</strong> "
          "It is required by section 170(2) of the Companies Act, 2013 and rule 18 of the Companies (Appointment and Qualification of Directors) Rules, 2014. "
          "Late filing attracts additional fees from 2 times the normal fee up to 12 times beyond 180 days, and continuing default can lead to a penalty under section 172. A resigning director may also file Form DIR-11 to put the resignation on record."),
    sections=[
        ("/ Quick answers", "What people search for.",
         ul("<strong>What is DIR-12?</strong> The return of particulars of directors and KMP (managing director, whole-time director, CEO, CFO, company secretary, manager) and changes among them.",
            "<strong>When is DIR-12 due?</strong> Within 30 days of the appointment, change in designation or cessation. On resignation, within 30 days of the company receiving the resignation notice.",
            "<strong>What are DIR-12 late fees?</strong> Additional fees rise with the delay: 2 times the normal fee for up to 30 days late, rising in bands to 12 times beyond 180 days. The normal fee depends on share capital.",
            "<strong>What is the penalty for not filing?</strong> Section 172 provides &#8377;50,000 on the company and each officer in default, plus &#8377;500 per day for continuing default, up to &#8377;3 lakh for the company and &#8377;1 lakh for an officer.",
            "<strong>What is DIR-11?</strong> A form the resigning director may file within 30 days of resigning, so the Registrar has the resignation on record even if the company delays DIR-12.",
            "<strong>Who signs it?</strong> A director or company secretary with a digital signature, and certification by a practising chartered accountant, company secretary or cost accountant where the form requires it.")),
        ("/ Attachments by event", "What to keep ready.",
         table(["Event", "Usual attachments"], [
             ["Appointment of director", "Consent in Form DIR-2, declaration that the person is not disqualified, board or shareholder resolution, letter of appointment"],
             ["Appointment of KMP", "Board resolution and appointment letter; " + L("form-mr-1-managerial-personnel-appointment-india-2026.html", "Form MR-1") + " for MD / WTD / manager where applicable"],
             ["Change in designation", "Board or shareholder resolution approving the change"],
             ["Resignation", "Resignation letter and proof of the date the company received it"],
             ["Removal or disqualification", "Resolution and supporting record"]])
         + '<p>Every director needs an active DIN; a deactivated DIN blocks DIR-12. See ' + L("dir-3-kyc-director-annual-compliance-india.html", "DIR-3 KYC") + ' and ' + L("din-for-foreign-national-director-india-documents-apostille-dsc-process-2026.html", "DIN for foreign nationals") + '.</p>'),
        ("/ Getting it right", "Common problems.",
         ul("<strong>Minimum directors:</strong> a private company needs at least two directors and every company needs a resident director; plan resignations so the board never falls below the minimum.",
            "<strong>Effective date:</strong> a resignation takes effect from the date the company receives the notice or a later date stated in it; use that date for the 30-day count.",
            "<strong>Related filings:</strong> " + L("form-mgt-14-board-shareholder-resolution-filing-india-2026.html", "MGT-14") + " for resolutions that must be filed, and MR-1 for managerial appointments.",
            "<strong>Foreign-owned companies:</strong> nominee and resident director changes follow the same 30-day rule; see " + L("nominee-resident-director-india-foreign-company.html", "nominee resident director") + ".",
            "<strong>Company not filing your resignation?</strong> File DIR-11 yourself and keep proof of delivery of the resignation letter.")
         + call_box("Director and KMP changes", ["DIR-12 for appointments and resignations",
                                                 "DIR-11 for resigning directors",
                                                 "Late DIR-12 and fee exposure",
                                                 "DIN and DIR-3 KYC issues",
                                                 "Resident and nominee director changes"],
                    "the change, the dates and the DIN status.")
         + sources("Companies Act, 2013, sections 168, 170 and 172; Companies (Appointment and Qualification of Directors) Rules, 2014, rule 18; Companies (Registration Offices and Fees) Rules, 2014 for additional fees; MCA instruction kit for Form DIR-11; Taxguru, Quicko and other practitioner guides. Fee band edges vary slightly between sources; check the MCA portal. Checked 25 November 2026.")),
    ],
    faqs=[("What is Form DIR-12?", "The e-form a company files with the Registrar of Companies to report the appointment of a director or key managerial personnel, a change in their designation, or their resignation or cessation, under section 170(2) of the Companies Act, 2013."),
          ("What is the due date for DIR-12?", "Within 30 days of the appointment, change or cessation. For a resignation, within 30 days of the company receiving the resignation notice."),
          ("What are the late fees for DIR-12?", "Additional fees are a multiple of the normal fee: 2 times for up to 30 days late, rising in bands to 12 times beyond 180 days. Continuing default can also attract a penalty under section 172."),
          ("Is DIR-11 mandatory for a resigning director?", "No, it is optional. A resigning director may file DIR-11 within 30 days of resigning to put the resignation on record; the company must still file DIR-12."),
          ("Can DIR-12 be filed if the director's DIN is deactivated?", "No. The DIN must be active, so complete DIR-3 KYC first if it is due."),
          ("Can BQP file DIR-12 for our company?", "Yes. CA Durgesh Chavda can prepare and file DIR-12, DIR-11 and related resolutions, and handle late filings and DIN issues. " + C)],
    related=[("form-mr-1-managerial-personnel-appointment-india-2026.html", "Form MR-1"),
             ("form-mgt-14-board-shareholder-resolution-filing-india-2026.html", "Form MGT-14"),
             ("dir-3-kyc-director-annual-compliance-india.html", "DIR-3 KYC"),
             ("nominee-resident-director-india-foreign-company.html", "Nominee resident director"),
             ("company-secretarial-services-india-remote.html", "Company secretarial services")],
    cta_h="Changed a director or KMP?", cta_b=C,
    keywords="DIR-12, form DIR 12, DIR-12 due date, DIR-12 late fees, DIR-12 meaning, DIR-12 full form, director appointment form, director resignation form, DIR-11, section 170 Companies Act",
    desc="Form DIR-12 (2026): file within 30 days of a director or KMP appointment, change or resignation (section 170(2), rule 18); late fees 2x to 12x; section 172 penalty; attachments; DIR-11 for resigning directors.",
    howto={"name": "How to file Form DIR-12", "description": "On the MCA V3 portal.", "steps": [
        {"name": "Pass the resolution", "text": "Board or shareholder approval of the appointment or change."},
        {"name": "Collect documents", "text": "DIR-2 consent, disqualification declaration, appointment or resignation letter."},
        {"name": "Check DIN status", "text": "The DIN must be active with KYC complete."},
        {"name": "Prepare and certify the form", "text": "Digital signature and professional certification where required."},
        {"name": "File within 30 days", "text": "Late filing carries additional fees."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch IC complete")
