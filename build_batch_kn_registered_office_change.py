# -*- coding: utf-8 -*-
"""Batch KN (28 Nov 2026): How to change the registered office of a company in India - within the city, outside local limits
under the same ROC, to another ROC in the same state, and to another state.
Demand: sweep ac231 (28 Nov 2026), all 7 markets: 'change registered office address', 'inc 22 change of registered office',
'change registered office address online' - no page on the site (FAQ added in PR #898). User steer 26 Nov 2026: more call
bookings / WhatsApp enquiries.
Facts: sections 12 and 13 of the Companies Act, 2013 and rules 25, 27, 28 and 30 of the Companies (Incorporation) Rules, 2014.
Within local limits: board resolution, Form INC-22 within 30 days. Outside local limits, same ROC: special resolution (filed in
MGT-14) and INC-22. Different ROC in the same state: confirmation of the Regional Director on Form INC-23, order filed with the
ROC, then INC-22. Another state: special resolution altering the memorandum, application on INC-23 to the Regional Director
after public advertisement and notice to creditors and others, order filed with the ROCs, then INC-22. Proof of address,
recent utility bill and owner's no-objection letter. No government fees, no portal menu paths, no office claims, no
statistics. advisory_lib.contact() is not used (it adds a response-time / fee line awaiting owner sign-off)."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources
from build_lib import page, write_page

A.UPDATED = "Last updated: 28 November 2026."
SLUG = "change-registered-office-company-india-inc-22-inc-23-mgt-14-within-city-another-state-procedure-2026"

C = ("WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with the company name and CIN, the current and new "
     "address (city and state), whether the new place is owned or rented, and when you plan to move. Or book a call directly.")
PAGES = [dict(
    slug=SLUG,
    title="How to Change the Registered Office of a Company in India (2026): Within the City, Same ROC, Another ROC or Another State - INC-22, INC-23 and MGT-14",
    em="the route depends on how far you move.",
    kicker="/ Private and public companies &middot; Board resolution to Regional Director approval &middot; Updated 2026-11-28",
    lead=("<strong>Moving a company's registered office is a filing with the Registrar of Companies, and the route depends on the distance: a board resolution and Form INC-22 within the same city; "
          "a special resolution as well when you leave the city but stay under the same ROC; and the Regional Director's approval on Form INC-23 when the move crosses into another ROC's area or another state.</strong> "
          "After the ROC records the change, GST, PAN and TAN records, bank accounts and licences must be updated too."),
    sections=[
        ("/ Four routes", "Pick the one that matches the move.",
         table(["Move", "Approval needed", "Filing"], [
             ["Within the same city, town or village (local limits)", "Board resolution", "INC-22 within 30 days of the change"],
             ["Outside local limits, same ROC", "Board resolution and special resolution of shareholders", "MGT-14 for the special resolution, then INC-22"],
             ["To another ROC's area in the same state", "Special resolution and confirmation by the Regional Director", "INC-23 to the Regional Director; order filed with the ROC; INC-22"],
             ["To another state", "Special resolution altering the memorandum, and approval by the Regional Director", "Public notice and notice to creditors and others; INC-23; order filed with the ROCs; INC-22"]])
         + ul("<strong>Documents for every route:</strong> proof of the new address (sale deed, lease or rent agreement), a recent utility bill, and a no-objection letter from the owner if the place is not owned by the company.",
              "<strong>Interstate moves take longest:</strong> the application must show that creditors and employees are not prejudiced, and objections can be raised before the Regional Director decides.",
              "<strong>The name board and stationery:</strong> the new registered office address must appear on the company's letterheads, invoices and outside the office.")),
        ("/ After the ROC records the change", "Update everything else.",
         ul("<strong>GST:</strong> amend the principal place of business in the GST registration; a move to another state needs a new GST registration there.",
            "<strong>Income tax:</strong> update the address on PAN and TAN records; the jurisdictional assessing officer can change.",
            "<strong>Banks and FEMA:</strong> inform the bank; a foreign-owned company also updates its bank and reporting records.",
            "<strong>Licences and registrations:</strong> shop and establishment, professional tax, import-export code, Udyam and any sector licences.",
            "<strong>Books and registers:</strong> keep statutory registers at the registered office unless a resolution allows another place.")
         + call_box("changing the registered office of a company", ["Which of the four routes applies",
                                                                     "Board and shareholder resolutions",
                                                                     "INC-22, MGT-14 and INC-23 filings",
                                                                     "Regional Director process for interstate moves",
                                                                     "GST, PAN / TAN, bank and licence updates"],
                    "Company name and CIN, current and new address, owned or rented, planned move date.")
         + sources("Companies Act, 2013 (sections 12 and 13); Companies (Incorporation) Rules, 2014 (rules 25, 27, 28 and 30; Forms INC-22, INC-23, INC-26 and INC-28); Companies (Management and Administration) Rules on MGT-14; CGST Act on amendment of registration; site company secretarial and ROC compliance calendar pages.")),
    ],
    faqs=[("How do I change the registered office within the same city?", "The board passes a resolution approving the new address and the company files Form INC-22 with the ROC within 30 days of the change, with proof of the new address, a recent utility bill and the owner's no-objection letter if the place is rented."),
          ("Do I need shareholder approval to change the registered office?", "Only when the office moves outside the local limits of the city, town or village. A move within local limits needs only a board resolution; a move outside them needs a special resolution of shareholders, filed in Form MGT-14, and then INC-22."),
          ("What is Form INC-23?", "It is the application to the Regional Director to confirm a shift of the registered office to an area under another ROC in the same state, or to another state. The Regional Director's order is filed with the ROC, and INC-22 is filed for the new address."),
          ("Can a company move its registered office to another state?", "Yes. It needs a special resolution altering the memorandum, a public notice and notice to creditors and others, an application on INC-23 to the Regional Director, and, once approved, the order filed with the ROCs and INC-22 for the new address. A new GST registration is needed in the new state."),
          ("What has to be updated after the registered office changes?", "The GST registration, PAN and TAN records, bank accounts, letterheads and invoices, and licences such as shop and establishment, professional tax, import-export code and Udyam."),
          ("What should I send to start?", "WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with the company name and CIN, the current and new address (city and state), whether the new place is owned or rented and the planned move date. Or book a call directly.")],
    related=[("company-secretarial-services-india-remote.html", "Company secretarial services"),
             ("roc-compliance-private-limited-company-llp-2026-27-calendar-due-dates-forms-late-fees.html", "ROC compliance calendar 2026-27"),
             ("private-limited-company-registration-india-2026-spice-plus-name-check-documents-directors-process.html", "Private limited company registration"),
             ("professional-tax-and-shop-establishment-registration-gujarat-ahmedabad-2026.html", "Professional tax and shop registration")],
    cta_h="Moving your company's registered office?", cta_b=C,
    keywords="change registered office address, change of registered office of company, inc 22, inc-23, shifting registered office to another state, registered office change within city, mgt-14 special resolution",
    desc="How to change the registered office of a company in India: board resolution and INC-22 within the city; special resolution (MGT-14) outside local limits; Regional Director approval on INC-23 for another ROC or another state; then update GST, PAN / TAN, bank and licences.",
    howto={"name": "How to change a company's registered office", "description": "Four routes by distance.", "steps": [
        {"name": "Identify the route", "text": "Within the city, same ROC, another ROC in the state, or another state."},
        {"name": "Pass the resolutions", "text": "Board resolution; special resolution when moving outside local limits."},
        {"name": "File with the ROC / Regional Director", "text": "INC-22; MGT-14 and INC-23 where needed."},
        {"name": "Update other records", "text": "GST, PAN / TAN, bank, licences, letterheads."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch KN complete")
