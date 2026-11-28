# -*- coding: utf-8 -*-
"""Batch KP (28 Nov 2026): Director resignation and removal in India - DIR-11, DIR-12, sections 168 and 169, and the minimum and
resident director rules.
Demand: sweep ac231 (28 Nov 2026), all 7 markets: 'director resignation dir-11', 'what to do when a director resigns',
'remove director from company (form)' - no page on the site (FAQ added in PR #898). User steer 26 Nov 2026: more call
bookings / WhatsApp enquiries.
Facts: Companies Act, 2013 - section 168: a director resigns by written notice; the resignation takes effect from the date the
company receives the notice or a later date stated in it; the company files Form DIR-12 within 30 days and places the fact
in the next board report; the director may forward a copy with reasons to the ROC in Form DIR-11 within 30 days; the
director remains liable for offences committed during the tenure. Section 149: at least two directors for a private
company and three for a public company, and at least one director resident in India (in India for at least 182 days in
the financial year). Section 169: removal by ordinary resolution after special notice under section 115; the director is
heard at the meeting and may make a written representation; not available for a director appointed by the Tribunal under
section 242; DIR-12 within 30 days. No fees, no portal menu paths, no office claims. advisory_lib.contact() is not used."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources
from build_lib import page, write_page

A.UPDATED = "Last updated: 28 November 2026."
SLUG = "director-resignation-removal-india-dir-11-dir-12-section-168-169-resident-director-2026"

C = ("WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with the company name and CIN, the current directors, "
     "who is leaving and why (resignation or removal), and whether a replacement director is ready. Or book a call directly.")
PAGES = [dict(
    slug=SLUG,
    title="Director Resignation and Removal in India (2026): DIR-11, DIR-12, Sections 168 and 169, Minimum and Resident Director Rules",
    em="keep the board compliant on the way out.",
    kicker="/ Private and public companies &middot; Indian and foreign directors &middot; Updated 2026-11-28",
    lead=("<strong>A director resigns by written notice; the company files Form DIR-12 within 30 days, and the director may also file DIR-11. "
          "A director who will not go can be removed by shareholders by ordinary resolution under section 169, after special notice and a chance to be heard.</strong> "
          "Either way, the company must still meet the minimum number of directors and keep at least one director resident in India."),
    sections=[
        ("/ Resignation and removal side by side", "Who acts, and what is filed.",
         table(["Point", "Resignation (section 168)", "Removal (section 169)"], [
             ["Who starts it", "The director, by written notice to the company", "Shareholders, by special notice of a resolution"],
             ["Approval", "None needed; the board takes note", "Ordinary resolution at a general meeting"],
             ["Effective from", "Date the company receives the notice, or a later date stated in it", "Date the resolution is passed"],
             ["Company filing", "DIR-12 within 30 days; mention in the next board report", "DIR-12 within 30 days"],
             ["Director's own filing", "DIR-11 with reasons, within 30 days (optional)", "Right to be heard and to send a written representation"],
             ["Not available for", "-", "A director appointed by the Tribunal under section 242"]])
         + ul("<strong>Liability continues:</strong> a director who resigns remains liable for offences that took place during the tenure.",
              "<strong>Minimum directors:</strong> a private company needs at least two directors and a public company three; appoint a replacement before the resignation takes effect if it would drop the count.",
              "<strong>Resident director:</strong> at least one director must have stayed in India for 182 days or more in the financial year - important when an Indian director of a foreign-owned company leaves.",
              "<strong>Signing authority:</strong> update bank mandates, digital signature use and authorised signatories on GST and income tax records.")),
        ("/ Practical steps", "Resignation or removal.",
         ul("<strong>Resignation:</strong> written notice with the effective date; board meeting to note it and, if needed, appoint a replacement; DIR-12 with the resignation letter and proof of delivery; update the register of directors.",
            "<strong>Removal:</strong> special notice from shareholders; send it to the director; hold the general meeting and allow the director to be heard; pass the ordinary resolution; file DIR-12.",
            "<strong>Disputed exits:</strong> if the company does not file DIR-12, the director's own DIR-11 creates the record; keep proof that the notice was delivered.",
            "<strong>Shareholders' agreements:</strong> check nomination rights and notice terms before acting.")
         + call_box("director resignation or removal", ["Resignation letter and effective date",
                                                       "Board and general meeting resolutions",
                                                       "DIR-11 and DIR-12 filings",
                                                       "Minimum and resident director compliance",
                                                       "Bank, GST and signatory updates"],
                    "Company name and CIN, current directors, who is leaving and why, replacement plans.")
         + sources("Companies Act, 2013 (sections 115, 149, 168, 169 and 242); Companies (Appointment and Qualification of Directors) Rules, 2014 (Forms DIR-11 and DIR-12); site company secretarial and director disqualification pages.")),
    ],
    faqs=[("How does a director resign from a private limited company?", "By giving written notice of resignation to the company. The resignation takes effect from the date the company receives the notice or a later date stated in it. The company files Form DIR-12 within 30 days and notes the resignation in the next board report."),
          ("Is filing DIR-11 compulsory for a resigning director?", "It is optional. A resigning director may send a copy of the resignation with reasons to the ROC in Form DIR-11 within 30 days. It is useful when the company may not file DIR-12 promptly, because it creates the director's own record."),
          ("Can the last director or the only resident director resign?", "The director can resign, but the company must keep at least two directors (three for a public company) and at least one director who stayed in India for 182 days or more in the financial year. Appoint a replacement before the resignation takes effect to avoid a default."),
          ("How can shareholders remove a director?", "By an ordinary resolution under section 169, after special notice of the resolution. The director must receive the notice, may make a written representation and has the right to be heard at the meeting. The company then files DIR-12 within 30 days. A director appointed by the Tribunal cannot be removed this way."),
          ("Is a director liable after resigning?", "Yes, for offences that took place during the tenure. Resignation does not end liability for past defaults, so keep a record of the date the notice was delivered."),
          ("What should I send to start?", "WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with the company name and CIN, the current directors, who is leaving and why, and whether a replacement director is ready. Or book a call directly.")],
    related=[("company-secretarial-services-india-remote.html", "Company secretarial services"),
             ("director-disqualified-section-164-2-din-deactivated-fix-india.html", "Director disqualified or DIN deactivated"),
             ("change-registered-office-company-india-inc-22-inc-23-mgt-14-within-city-another-state-procedure-2026.html", "Change of registered office"),
             ("roc-compliance-private-limited-company-llp-2026-27-calendar-due-dates-forms-late-fees.html", "ROC compliance calendar 2026-27")],
    cta_h="A director leaving the board?", cta_b=C,
    keywords="director resignation dir-11, dir-12 resignation of director, how to remove a director from a company india, section 168 resignation, section 169 removal of director, resident director requirement",
    desc="Director resignation and removal in India: written notice and DIR-12 within 30 days (DIR-11 optional) under section 168; removal by ordinary resolution after special notice under section 169; minimum two directors and one resident director; liability for past defaults.",
    howto={"name": "How to handle a director's exit", "description": "Resignation or removal.", "steps": [
        {"name": "Check the board", "text": "Minimum directors and the resident director after the exit."},
        {"name": "Notice or special notice", "text": "Resignation letter, or shareholders' special notice for removal."},
        {"name": "Resolutions", "text": "Board takes note of resignation; general meeting passes removal."},
        {"name": "File and update", "text": "DIR-12 within 30 days; bank, GST and signatory records."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch KP complete")
