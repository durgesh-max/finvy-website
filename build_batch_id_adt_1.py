# -*- coding: utf-8 -*-
"""Batch ID (25 Nov 2026): Form ADT-1 - notice to the Registrar of appointment of auditor (section 139(1) of the
Companies Act, 2013, rule 4(2) of the Companies (Audit and Auditors) Rules, 2014): within 15 days of the meeting at
which the auditor is appointed; auditor appointed at the first AGM for five years (to the sixth AGM). First auditor
(section 139(6)): board within 30 days of incorporation, else members within 90 days at an EGM, holds office till the
first AGM; ADT-1 for the first auditor was traditionally not required (rule 4(2) refers to section 139(1)), but after
MCA notification G.S.R. 359(E) of 30 May 2025 ICSI has sought clarification and practice is to file - stated as
uncertain. Casual vacancy (section 139(8)): board within 30 days; resignation-caused vacancy needs members' approval
within three months. Rotation (section 139(2), rule 5): listed companies, unlisted public companies with paid-up capital
of Rs 10 crore or more, private companies with paid-up capital of Rs 50 crore or more, and companies with public
borrowings of Rs 50 crore or more; individual one term of five years, firm two terms, five-year cooling off. Auditor
resignation: ADT-3 by the auditor within 30 days (section 140(2), rule 8).
Demand: sweep ac107 (25 Nov 2026), all 7 markets: "adt 1", "adt 1 form purpose", "adt 1 is mandatory for first auditor".
Facts (checked 25 Nov 2026): ICSI representation on ADT-1 applicability; Taxguru compilation on auditor appointment;
ca2013.com; IndiaFilings ADT-1 applicability; Cleartax on auditor resignation; site calendar page (ADT-1 within 15
days of the AGM)."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 25 November 2026."
SLUG = "form-adt-1-auditor-appointment-15-days-first-auditor-rotation-adt-3-india-2026"

C = contact("the company name, date of incorporation, the meeting at which the auditor was or will be appointed, and whether this is a first auditor, AGM appointment, casual vacancy or change of auditor")
L = lambda h, t: f'<a href="{h}">{t}</a>'
PAGES = [dict(
    slug=SLUG,
    title="Form ADT-1 Filing Procedure (2026): Auditor Appointment Within 15 Days, First Auditor, Five-Year Term, Rotation and ADT-3",
    em="every appointment needs a filing trail.",
    kicker="/ Companies appointing a statutory auditor &middot; Company law &middot; Updated 2026-11-25",
    lead=("<strong>Form ADT-1 is the notice a company files with the Registrar of Companies within 15 days of the meeting at which it appoints its statutory auditor.</strong> "
          "Under section 139(1) of the Companies Act, 2013, the auditor is appointed at the first annual general meeting for a term of five years, and rule 4(2) of the Companies (Audit and Auditors) Rules, 2014 requires the ADT-1 filing. "
          "A new company&rsquo;s first auditor is appointed by the board within 30 days of incorporation; whether ADT-1 is needed for that appointment has long been debated, and since MCA&rsquo;s May 2025 form changes most practitioners file it as the cautious course."),
    sections=[
        ("/ Quick answers", "What people search for.",
         ul("<strong>What is the purpose of ADT-1?</strong> To inform the Registrar that an auditor has been appointed, with the auditor&rsquo;s details, the period of appointment and the auditor&rsquo;s written consent and eligibility certificate.",
            "<strong>When is ADT-1 due?</strong> Within 15 days of the meeting at which the auditor is appointed.",
            "<strong>Is ADT-1 mandatory for the first auditor?</strong> Rule 4(2) refers to appointments under section 139(1), so filing for a first auditor under section 139(6) was traditionally treated as not required. After MCA notification G.S.R. 359(E) of 30 May 2025, ICSI has asked MCA to clarify, and filing ADT-1 for the first auditor is now the safer practice.",
            "<strong>How long is the auditor&rsquo;s term?</strong> Five years from the first AGM (to the conclusion of the sixth AGM), then reappointment subject to rotation limits.",
            "<strong>Who must rotate auditors?</strong> Listed companies, unlisted public companies with paid-up share capital of &#8377;10 crore or more, private companies with paid-up share capital of &#8377;50 crore or more, and companies with public borrowings of &#8377;50 crore or more: an individual auditor for one term of five years, a firm for two terms, then a five-year gap.",
            "<strong>What if the auditor resigns?</strong> The auditor files ADT-3 with the company and the Registrar within 30 days, and the board fills the casual vacancy.")),
        ("/ Appointment situations", "Who appoints, and what is filed.",
         table(["Situation", "Who appoints and when", "Filing"], [
             ["First auditor", "Board within 30 days of incorporation; if not, members within 90 days at an EGM; holds office till the first AGM", "ADT-1 now usually filed (see above)"],
             ["AGM appointment", "Members at the first AGM for five years", "ADT-1 within 15 days of the AGM"],
             ["Casual vacancy", "Board within 30 days; if caused by resignation, members must approve within three months", "ADT-1 for the new appointment"],
             ["Auditor resigns", "Auditor gives notice to the company", "ADT-3 by the auditor within 30 days"],
             ["Removal before term", "Special resolution and Central Government approval", "ADT-2 application, then ADT-1 for the new auditor"]])
         + '<p>Related: ' + L("form-inc-20a-commencement-of-business-180-days-penalty-applicability-india-2026.html", "INC-20A after incorporation") + ', ' + L("aoc-4-filing-deadline-30-october-2026-late-fee-india.html", "AOC-4 financial statements") + ' and the ' + L("foreign-owned-indian-subsidiary-annual-compliance-calendar-fy-2026-27.html", "subsidiary compliance calendar") + '.</p>'),
        ("/ Getting it right", "Common issues.",
         ul("<strong>Consent and certificate:</strong> obtain the auditor&rsquo;s written consent and certificate of eligibility under section 141 before the appointment.",
            "<strong>Late filing:</strong> ADT-1 can be filed late with additional fees that rise with the delay; file promptly.",
            "<strong>Term tracking:</strong> note the five-year term end and the rotation date in the compliance calendar.",
            "<strong>Foreign-owned subsidiaries:</strong> group auditors often audit the Indian subsidiary; check independence and rotation limits.",
            "<strong>Company secretarial support:</strong> see " + L("company-secretarial-services-india-remote.html", "company secretarial services") + " and " + L("form-mgt-14-board-shareholder-resolution-filing-india-2026.html", "MGT-14") + " for resolutions that must be filed.")
         + call_box("Auditor appointments", ["First auditor appointment and ADT-1",
                                              "AGM appointment and five-year term",
                                              "Casual vacancy and resignation (ADT-3)",
                                              "Rotation planning",
                                              "Late ADT-1 filings"],
                    "the company, the dates and the type of appointment.")
         + sources("Companies Act, 2013, sections 139, 140 and 141; Companies (Audit and Auditors) Rules, 2014, rules 4, 5 and 8; MCA notification G.S.R. 359(E) dated 30 May 2025; ICSI representation seeking clarification on applicability of e-form ADT-1; Taxguru, ca2013.com, IndiaFilings and Cleartax commentary. Checked 25 November 2026.")),
    ],
    faqs=[("What is Form ADT-1?", "The notice of appointment of auditor that a company files with the Registrar of Companies within 15 days of the meeting at which the auditor is appointed, under section 139(1) and rule 4(2)."),
          ("Is ADT-1 mandatory for the first auditor?", "Traditionally it was treated as not required, because rule 4(2) refers to appointments under section 139(1) and the first auditor is appointed under section 139(6). After MCA's May 2025 notification (G.S.R. 359(E)), ICSI has sought clarification, so filing ADT-1 for the first auditor is the safer course."),
          ("What is the due date for ADT-1?", "Within 15 days of the meeting, usually the AGM, at which the auditor is appointed."),
        ("What happens if ADT-1 is not filed?", "File it now, late. A late ADT-1 carries an additional fee that grows with the delay, and failing to comply with the auditor appointment rules in section 139 can lead to penalties under section 147 for the company and every officer in default. It also blocks the next step: the AOC-4 asks for the SRN of the ADT-1, so the financial statements cannot be filed cleanly until it is in place. First check what actually happened. If the auditor was appointed at the AGM and only the form was missed, a late ADT-1 with the board or AGM resolution and the auditor's consent and eligibility certificate is enough. If no auditor was ever appointed, the appointment has to be fixed first (by the board for a first auditor, or at a general meeting), and only then is ADT-1 filed. WhatsApp +91 78018 87130 with the CIN, the date of the AGM or board meeting that appointed the auditor and the auditor's consent letter, and we tell you which route applies and what has to be filed."),
        ("How do I check if ADT-1 was filed for my company?", "The company's filing history on the MCA website lists each e-form with its SRN and date, and the auditor details shown in the company's master data come from the latest ADT-1. If the auditor shown is an old firm, or no auditor appears at all, the form was probably not filed. Send us the CIN on WhatsApp +91 78018 87130 and we check the filing history and tell you what is missing."),
          ("What is the term of a statutory auditor?", "Five years from the conclusion of the first AGM to the conclusion of the sixth AGM, with reappointment subject to rotation rules for listed and larger companies."),
          ("Who files ADT-3?", "The resigning auditor, with the company and the Registrar, within 30 days of resignation."),
          ("Can BQP handle auditor appointment filings?", "Yes. CA Durgesh Chavda can prepare resolutions, consent and eligibility documents, and file ADT-1 and related forms on time. " + C)],
    related=[("form-inc-20a-commencement-of-business-180-days-penalty-applicability-india-2026.html", "Form INC-20A"),
             ("form-dir-12-director-appointment-resignation-30-days-late-fees-dir-11-india-2026.html", "Form DIR-12"),
             ("aoc-4-filing-deadline-30-october-2026-late-fee-india.html", "AOC-4 filing"),
             ("foreign-owned-indian-subsidiary-annual-compliance-calendar-fy-2026-27.html", "Subsidiary compliance calendar"),
             ("company-secretarial-services-india-remote.html", "Company secretarial services")],
    cta_h="Appointing or changing your auditor?", cta_b=C,
    keywords="ADT-1, form ADT 1, ADT-1 due date, ADT-1 form purpose, ADT-1 first auditor, auditor appointment section 139, auditor rotation, ADT-3 auditor resignation, casual vacancy auditor",
    desc="Form ADT-1 (2026): notice of auditor appointment within 15 days of the meeting (section 139(1), rule 4(2)); first auditor by board within 30 days and the ADT-1 question after G.S.R. 359(E); five-year term, rotation thresholds, casual vacancy, ADT-3.",
    howto={"name": "How to file Form ADT-1", "description": "After appointing the auditor.", "steps": [
        {"name": "Get consent and eligibility", "text": "Written consent and section 141 certificate from the auditor."},
        {"name": "Pass the resolution", "text": "Board (first auditor or casual vacancy) or members at the AGM."},
        {"name": "Intimate the auditor", "text": "Send the appointment letter."},
        {"name": "Prepare ADT-1", "text": "Auditor details, period, resolution and consent attached."},
        {"name": "File within 15 days", "text": "On the MCA portal with a director's digital signature."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch ID complete")
