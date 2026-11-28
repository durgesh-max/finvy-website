# -*- coding: utf-8 -*-
"""Batch LU (28 Nov 2026): Changing the object clause of a company - section 13 alteration of the memorandum by special resolution,
MGT-14 within 30 days, the extra steps for a company with unutilised public issue money, and the follow-on updates (GST, FEMA sector
check for foreign-owned companies, licences, NIC code).
Demand: 'change object clause of company', 'alteration of moa object clause', 'add new business activity private limited company',
'mgt-14 for change in object' - only mentioned on the NBFC and due diligence pages. Companies pivoting or adding a business line
need this done before starting the activity. User steer 26 Nov 2026: more call bookings / WhatsApp enquiries.
Facts (Companies Act, 2013 sections 4, 13 and 117): the memorandum states the objects; a company changes its objects by a special
resolution of shareholders altering the memorandum; the special resolution and the altered memorandum are filed in MGT-14 within 30
days; the alteration takes effect when the Registrar registers it; a company that raised money from the public through a prospectus
and still has unutilised money must also pass the resolution by postal ballot, publish the details in newspapers and give dissenting
shareholders an exit opportunity (section 13(8)); after the change, update the GST registration (business activity details), check
that a foreign-owned company's new activity is permitted under FEMA (automatic route or approval) and report as required, obtain any
sector licences, and update the business activity code and bank records. No fees, no portal menu paths. advisory_lib.contact() is not
used."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources
from build_lib import page, write_page

A.UPDATED = "Last updated: 28 November 2026."
SLUG = "change-object-clause-company-moa-alteration-section-13-special-resolution-mgt-14-new-business-activity-2026"

C = ("WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with the current memorandum, the new business activity "
     "you want to add or switch to, the shareholding (including any foreign shareholders), and any licence the new activity needs. "
     "Or book a call directly.")
PAGES = [dict(
    slug=SLUG,
    title="Change of Object Clause of a Company (2026): Altering the Memorandum Under Section 13, Special Resolution, MGT-14 and What to Update for a New Business Activity",
    em="change the memorandum before the business.",
    kicker="/ Private and public companies adding or switching business activities &middot; Companies Act section 13 &middot; Updated 2026-11-28",
    lead=("<strong>A company&rsquo;s memorandum states what business it is set up to do. Before starting a new line of business outside those objects, the company alters the object clause by a special resolution of shareholders and files it in MGT-14 within 30 days. "
          "The change takes effect when the Registrar registers it - and then the GST registration, licences and, for foreign-owned companies, the FEMA position need to follow.</strong>"),
    sections=[
        ("/ The steps", "Section 13 of the Companies Act.",
         table(["Step", "Rule"], [
             ["Draft the new object clause", "Clear wording for the main business, consistent with any licences needed"],
             ["Board meeting", "Approve the proposal and call a general meeting"],
             ["Special resolution", "Shareholders approve the altered memorandum"],
             ["MGT-14", "File the special resolution and altered memorandum within 30 days"],
             ["Registration", "The alteration takes effect when the Registrar registers it"],
             ["Public issue money unutilised", "Postal ballot, newspaper publication and an exit offer to dissenting shareholders (section 13(8))"]])
         + ul("<strong>Start the activity after registration:</strong> doing business outside the registered objects can expose contracts and directors to challenge.",
              "<strong>Articles too:</strong> check whether the articles also need changes, for example for new share classes or management rights linked to the new business.")),
        ("/ After the change", "The follow-on updates.",
         ul("<strong>GST:</strong> update business activity and goods / services details in the registration; add places of business if the new activity needs them.",
            "<strong>Foreign-owned companies:</strong> confirm the new activity is permitted for foreign investment under the automatic route, or obtain approval, and keep FEMA reporting consistent.",
            "<strong>Licences:</strong> regulated activities (for example lending, insurance broking, food, drugs) need their own registration before starting.",
            "<strong>Records:</strong> update the business activity code in company filings, bank KYC, Udyam and IEC where relevant.",
            "<strong>Name:</strong> if the name signals the old business, consider a name change (INC-24) at the same time.")
         + call_box("a change of object clause", ["Drafting the new object clause",
                                                  "Board and special resolutions",
                                                  "MGT-14 within 30 days",
                                                  "FEMA sector check for foreign-owned companies",
                                                  "GST, licence and record updates"],
                    "Current memorandum, new activity, shareholding, licences needed.")
         + sources("Companies Act, 2013 (sections 4, 13 and 117); Companies (Incorporation) Rules, 2014 (rule 32); FEMA (Non-debt Instruments) Rules, 2019 and the consolidated FDI policy; site MGT-14, change of company name and GST registration amendment pages.")),
    ],
    faqs=[("How do I change the object clause of a private limited company?", "Draft the new object clause, hold a board meeting, pass a special resolution of shareholders altering the memorandum, and file the resolution with the altered memorandum in MGT-14 within 30 days. The change takes effect when the Registrar registers it."),
          ("Is a special resolution needed to change the objects of a company?", "Yes. The memorandum, including the object clause, is altered by a special resolution of shareholders under section 13 of the Companies Act."),
          ("When does a change of object clause take effect?", "When the Registrar registers the alteration after the MGT-14 filing. The company should start the new activity only after that."),
          ("Are there extra steps for companies that raised money from the public?", "Yes. If money raised through a prospectus is still unutilised, the resolution must be passed by postal ballot, the details published in newspapers, and dissenting shareholders offered an exit."),
          ("What else must be updated after changing the object clause?", "The GST registration details, any sector licences for the new activity, the FEMA position for foreign-owned companies, the business activity code, and bank and other registrations."),
          ("What should I send to start?", "WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with the current memorandum, the new business activity, the shareholding and any licence the activity needs. Or book a call directly.")],
    related=[("form-mgt-14-board-shareholder-resolution-filing-india-2026.html", "Form MGT-14 resolution filing"),
             ("change-company-name-india-inc-24-special-resolution-mgt-14-name-reservation-fresh-certificate-2026.html", "Change of company name (INC-24)"),
             ("gst-registration-amendment-core-non-core-fields-reg-14-15-days-change-address-add-place-of-business-2026.html", "GST registration amendment"),
             ("can-foreigner-own-100-percent-indian-company.html", "Can a foreigner own 100% of an Indian company?")],
    cta_h="Adding a new line of business?", cta_b=C,
    keywords="change object clause of company, alteration of moa object clause, add new business activity private limited company, mgt-14 change in object, section 13 companies act special resolution, change main object company india",
    desc="Change of object clause: alter the memorandum by special resolution under section 13, file MGT-14 within 30 days, effective on registration by the Registrar, extra steps where public issue money is unutilised, and follow-on GST, FEMA sector, licence and record updates.",
    howto={"name": "How to change the object clause", "description": "Before starting the new business.", "steps": [
        {"name": "Draft the clause", "text": "Clear objects for the new activity; check licence needs."},
        {"name": "Pass the special resolution", "text": "Board meeting, then shareholders approve the altered memorandum."},
        {"name": "File MGT-14", "text": "Within 30 days; alteration effective on registration."},
        {"name": "Update the rest", "text": "GST details, FEMA check, licences, activity code, bank records."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch LU complete")
