# -*- coding: utf-8 -*-
"""Batch LS (28 Nov 2026): Amending GST registration - core vs non-core fields, REG-14 within 15 days of the change, officer approval
in REG-15, clarification notices (REG-03 / REG-04), changes that need a fresh registration (PAN change, new state, constitution
change), and adding a place of business.
Demand: 'gst registration amendment', 'change address in gst registration', 'core and non core fields gst', 'add additional place of
business gst', 'change partner in gst registration' - 0 dedicated pages. Businesses moving premises or changing partners need help
and officers often query address changes. User steer 26 Nov 2026: more call bookings / WhatsApp enquiries.
Facts (CGST Act section 28; CGST Rules rule 19): a registered person applies in Form GST REG-14 within 15 days of the change; core
fields - legal name (where PAN does not change), principal place of business, additional places of business (within the state),
and addition or removal of partners, directors, karta or similar persons responsible for the business - need approval by the proper
officer, who passes an order in REG-15 within 15 days of the application (rule 19 as substituted from 1 November 2026 by Notification 05/2026-CT, per secondary sources found by web search 28 Nov 2026); the officer may ask for clarification in REG-03 and the applicant
replies in REG-04; if the officer takes no action in time, the registration stands amended as applied for; non-core field changes
(for example business details, bank accounts, goods and services) take effect without officer approval; amendments take effect from
the date of the event once approved; a change in PAN (for example proprietorship to partnership or company) needs a fresh
registration, as does a business in a new state; mobile and email of the authorised signatory are updated with OTP verification.
No fees, no portal menu paths. advisory_lib.contact() is not used."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources
from build_lib import page, write_page

A.UPDATED = "Last updated: 28 November 2026."
SLUG = "gst-registration-amendment-core-non-core-fields-reg-14-15-days-change-address-add-place-of-business-2026"

C = ("WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with your GSTIN, what changed and when (address, name, "
     "partners or directors, new premises), the new rent agreement or ownership proof, and any REG-03 query received. Or book a "
     "call directly.")
PAGES = [dict(
    slug=SLUG,
    title="GST Registration Amendment (2026): Core vs Non-Core Fields, REG-14 Within 15 Days, Officer Approval, Changing Address, Adding a Place of Business and When You Need a New GSTIN",
    em="update it within 15 days of the change.",
    kicker="/ GST-registered businesses &middot; Amendment of registration under section 28 &middot; Updated 2026-11-28",
    lead=("<strong>When something in your GST registration changes - the address, the business name, a partner or director, or a new godown or shop - you file an amendment in Form REG-14 within 15 days. "
          "Core fields such as the principal place of business and partners need the officer&rsquo;s approval within 15 days of the application; non-core fields update without approval. "
          "A change in PAN or a move to another state needs a fresh registration instead.</strong>"),
    sections=[
        ("/ Core vs non-core changes", "Rule 19 of the CGST Rules.",
         table(["Change", "Type", "What happens"], [
             ["Legal name (PAN unchanged)", "Core", "Officer approval (REG-15)"],
             ["Principal place of business (same state)", "Core", "Officer approval; address proof needed"],
             ["Additional place of business (same state)", "Core", "Officer approval"],
             ["Partners, directors, karta, trustees", "Core", "Officer approval"],
             ["Business activity, goods / services, bank account", "Non-core", "Updated without approval"],
             ["Mobile or email of authorised signatory", "Contact details", "Updated with OTP verification"],
             ["PAN changes (e.g. proprietorship to company)", "-", "Fresh registration; cancel the old one"],
             ["Business moves to another state", "-", "Fresh registration in the new state"]])
         + ul("<strong>Officer timeline:</strong> the officer approves in REG-15 within 15 days of the application, or asks for clarification in REG-03, which you answer in REG-04; if no action is taken in time, the registration stands amended as applied for.",
              "<strong>Effective date:</strong> once approved, the amendment applies from the date of the change you report.",
              "<strong>Rule 19 rewritten from 1 November 2026:</strong> the amendment rule was substituted with effect from 1 November 2026 - check the current timelines and documents before filing.")),
        ("/ Address changes and common problems", "Where amendments get rejected.",
         ul("<strong>Proof of premises:</strong> a rent or lease agreement, ownership document or consent letter with a utility bill, in the name and address exactly as applied.",
            "<strong>Physical verification:</strong> officers may verify the new premises - keep the name board, records and staff available.",
            "<strong>Invoices and e-way bills:</strong> do not use the new address on invoices before the amendment is approved; update e-way bill and e-invoice masters after.",
            "<strong>Late amendment:</strong> trading from an unregistered address risks notices, detention of goods in transit and suspension of registration.",
            "<strong>Constitution change:</strong> a proprietorship becoming a company or LLP gets a new PAN and needs a new GSTIN, with transfer of credit through ITC-02 where allowed.")
         + call_box("a GST registration amendment", ["Identifying core vs non-core changes",
                                                     "REG-14 with correct proofs",
                                                     "Replies to REG-03 queries",
                                                     "New registration for PAN or state changes",
                                                     "Updating invoices, e-way bills and e-invoice masters"],
                    "GSTIN, what changed and when, address proof, any REG-03 query.")
         + sources("CGST Act, 2017 (sections 22, 25 and 28); CGST Rules, 2017 (rules 19 and 41; Forms GST REG-03, REG-04, REG-14 and REG-15); site GST registration, GST registration cancellation and proprietorship conversion pages.")),
    ],
    faqs=[("How do I change my address in GST registration?", "File an amendment in Form GST REG-14 within 15 days of the change, with proof of the new premises. The principal place of business is a core field, so the officer must approve it within 15 days of the application."),
          ("What are core and non-core fields in GST registration?", "Core fields are the legal name (without PAN change), principal and additional places of business within the state, and partners, directors or similar persons - these need officer approval. Other details, such as business activity or bank accounts, are non-core and update without approval."),
          ("What is the time limit to amend GST registration?", "The amendment application must be filed within 15 days of the change. The officer then has 15 days from the application to approve or raise a query; if no action is taken, the registration stands amended as applied for."),
          ("Can I add a new shop or godown to my GST registration?", "Yes, an additional place of business in the same state is added through a core-field amendment with proof of the premises. A place of business in another state needs a separate GST registration."),
          ("When do I need a new GST registration instead of an amendment?", "When the PAN changes, for example when a proprietorship becomes a partnership, LLP or company, or when the business is moving to or opening in another state."),
          ("What should I send to start?", "WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with your GSTIN, what changed and when, the new address proof and any REG-03 query. Or book a call directly.")],
    related=[("gst-registration-cancellation-reg-16-reg-19-gstr-10-revocation-reg-21-certificate-download-2026.html", "GST registration cancellation and revocation"),
             ("gst-registration-rejected-or-suspended-reg-03-reg-05-rule-21a-reg-31-what-to-do-2026.html", "GST registration rejected or suspended"),
             ("convert-proprietorship-to-private-limited-company-india-business-transfer-section-47-xiv-gst-itc-02-2026.html", "Convert proprietorship to private limited company"),
             ("gst-consultant-online-india-registration-returns-lut-refund-notice-reply-gstr-9-near-me-2026.html", "GST consultant online")],
    cta_h="Changed address, partners or premises?", cta_b=C,
    keywords="gst registration amendment, change address in gst registration, core and non core fields gst, add additional place of business gst, change partner in gst registration, reg-14 amendment 15 days, new gstin pan change",
    desc="GST registration amendment: REG-14 within 15 days of the change; core fields (legal name, principal and additional place of business, partners / directors) need officer approval in REG-15 within 15 days of the application; non-core fields update directly; PAN change or new state needs a fresh GSTIN.",
    howto={"name": "How to amend GST registration", "description": "Within 15 days of the change.", "steps": [
        {"name": "Classify the change", "text": "Core, non-core, contact details - or a new registration."},
        {"name": "Prepare proof", "text": "Premises documents, partner or director details, as applicable."},
        {"name": "File REG-14", "text": "Within 15 days of the change."},
        {"name": "Follow up", "text": "Reply to REG-03 in REG-04; update invoices and e-way bill masters after approval."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch LS complete")
