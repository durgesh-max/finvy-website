# -*- coding: utf-8 -*-
"""Batch LT (28 Nov 2026): Changing the name of a company - name reservation, board and special resolution, MGT-14, INC-24
application, fresh certificate in INC-25, restrictions where filings are pending, showing the former name for two years, and
updating PAN, GST, bank and contracts.
Demand: 'change company name', 'inc-24 name change', 'how to change name of private limited company', 'company name change
procedure', 'former name on letterhead' - only mentioned on the company secretarial page. Rebrands and post-acquisition renames need
this done in order. User steer 26 Nov 2026: more call bookings / WhatsApp enquiries.
Facts (Companies Act, 2013 sections 4, 12, 13 and 16; Companies (Incorporation) Rules, 2014 rules 8 to 9A and 29): check the new name
against the naming rules and reserve it (a reserved name for a change of name stays valid for 60 days); board meeting and a special
resolution of shareholders; MGT-14 within 30 days of the special resolution; application in INC-24 for approval of the name change
(power delegated to the Registrar); the change takes effect when the Registrar issues a fresh certificate of incorporation in INC-25;
no approval is needed where the only change is adding or removing the word 'Private' on conversion; a company that has not filed its
annual returns or financial statements, or has not repaid deposits or debentures and interest, cannot change its name until it
rectifies the default; for two years after a change, the former name must be shown with the new name on letterheads, invoices and
other documents (section 12(3)(c)); afterwards update PAN, TAN, GST registration (legal name is a core field), bank accounts, IEC,
Udyam, licences, contracts and the common seal. No fees, no portal menu paths. advisory_lib.contact() is not used."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources
from build_lib import page, write_page

A.UPDATED = "Last updated: 28 November 2026."
SLUG = "change-company-name-india-inc-24-special-resolution-mgt-14-name-reservation-fresh-certificate-2026"

C = ("WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with the current and proposed names, the reason (rebrand, "
     "acquisition, trademark), confirmation that annual returns and financial statements are filed, and the registrations to "
     "update afterwards (GST, IEC, licences). Or book a call directly.")
PAGES = [dict(
    slug=SLUG,
    title="Change of Company Name in India (2026): Name Reservation, Special Resolution, MGT-14, INC-24, Fresh Certificate and What to Update Afterwards",
    em="reserve, resolve, apply - then update everything.",
    kicker="/ Private and public companies &middot; Companies Act section 13 &middot; Updated 2026-11-28",
    lead=("<strong>A company changes its name by reserving the new name, passing a special resolution, filing MGT-14 and applying to the Registrar in INC-24. "
          "The new name takes effect only when the Registrar issues a fresh certificate of incorporation. "
          "For two years the old name must appear alongside the new one, and PAN, GST, bank accounts, licences and contracts all need updating.</strong>"),
    sections=[
        ("/ The steps", "Section 13 and the Incorporation Rules.",
         table(["Step", "Rule"], [
             ["Check and reserve the name", "Follow the naming rules (no identical or undesirable names, trademark conflicts); a reserved name for a change of name is valid for 60 days"],
             ["Board meeting", "Approve the proposal and call a general meeting"],
             ["Special resolution", "Shareholders approve the change and the altered memorandum (and articles)"],
             ["MGT-14", "File the special resolution within 30 days"],
             ["INC-24", "Apply to the Registrar for approval of the name change"],
             ["Fresh certificate", "Name change effective on issue of the new certificate of incorporation (INC-25)"],
             ["Former name", "Show the former name with the new name on letterheads, invoices and documents for two years"]])
         + ul("<strong>Pending filings block it:</strong> a company that has not filed annual returns or financial statements, or has defaulted on deposits or debentures, cannot change its name until the default is set right.",
              "<strong>Only adding or removing &lsquo;Private&rsquo;:</strong> on conversion between private and public, no separate name-change approval is needed.")),
        ("/ After the new certificate", "The update list.",
         ul("<strong>Tax registrations:</strong> PAN and TAN records; GST registration (the legal name is a core field, so file an amendment); professional tax.",
            "<strong>Banks and payments:</strong> bank accounts, payment gateways, loan and security documents.",
            "<strong>Licences and IDs:</strong> IEC, Udyam, FSSAI or other licences, shops and establishment registration, trademark filings.",
            "<strong>Contracts and stationery:</strong> notify customers and vendors, update invoices, website, letterheads and the common seal if used.",
            "<strong>Foreign shareholders:</strong> update the details reported in FEMA filings where the investee name changes.")
         + call_box("a company name change", ["Name check and reservation",
                                              "Board and special resolutions",
                                              "MGT-14 and INC-24",
                                              "Fresh certificate follow-up",
                                              "GST, PAN, bank and licence updates"],
                    "Current and proposed names, reason, filing status, registrations to update.")
         + sources("Companies Act, 2013 (sections 4, 12, 13 and 16); Companies (Incorporation) Rules, 2014 (rules 8, 8A, 9, 9A and 29; Forms INC-24 and INC-25); site GST registration amendment, MGT-14 and company secretarial pages.")),
    ],
    faqs=[("How do I change the name of a private limited company?", "Check and reserve the new name, hold a board meeting, pass a special resolution of shareholders, file MGT-14 within 30 days, and apply to the Registrar in INC-24. The change takes effect when the Registrar issues a fresh certificate of incorporation."),
          ("How long is a reserved name valid for a change of name?", "A name reserved for changing the name of an existing company is valid for 60 days from approval, so the special resolution and INC-24 should follow promptly."),
          ("Can a company change its name if annual filings are pending?", "No. A company that has not filed its annual returns or financial statements, or has defaulted on deposits or debentures and interest, cannot change its name until the default is rectified."),
          ("Do I need to show the old company name after a change?", "Yes. For two years after the change, the former name must be printed along with the new name on letterheads, invoices, notices and other official documents."),
          ("What needs to be updated after a company name change?", "PAN and TAN records, the GST registration (legal name is a core field), bank accounts, IEC, Udyam and other licences, contracts, invoices, the website and stationery."),
          ("What should I send to start?", "WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with the current and proposed names, the reason, your filing status and the registrations to update. Or book a call directly.")],
    related=[("gst-registration-amendment-core-non-core-fields-reg-14-15-days-change-address-add-place-of-business-2026.html", "GST registration amendment"),
             ("form-mgt-14-board-shareholder-resolution-filing-india-2026.html", "Form MGT-14 resolution filing"),
             ("company-secretarial-services-india-remote.html", "Company secretarial services"),
             ("change-registered-office-company-india-inc-22-inc-23-mgt-14-within-city-another-state-procedure-2026.html", "Change registered office")],
    cta_h="Rebranding your company?", cta_b=C,
    keywords="change company name, inc-24 name change, how to change name of private limited company, company name change procedure india, name reservation 60 days, former name two years letterhead, inc-25 fresh certificate",
    desc="Change of company name in India: reserve the name (valid 60 days for a change), board meeting, special resolution, MGT-14 within 30 days, INC-24 to the Registrar, fresh certificate in INC-25, blocked if filings pending, former name shown for two years, then update PAN, GST, bank and licences.",
    howto={"name": "How to change a company name", "description": "From reservation to new certificate.", "steps": [
        {"name": "Reserve the name", "text": "Check naming rules and trademarks; reservation valid 60 days."},
        {"name": "Pass resolutions", "text": "Board meeting, then special resolution; MGT-14 within 30 days."},
        {"name": "Apply in INC-24", "text": "Registrar approval; fresh certificate in INC-25."},
        {"name": "Update records", "text": "Former name for two years; PAN, GST, bank, licences, contracts."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch LT complete")
