# -*- coding: utf-8 -*-
"""Batch KO (28 Nov 2026): How to convert a proprietorship into a private limited company in India - the business-transfer route,
the tax-neutral conditions, GST on a transfer of a going concern, and what moves to the company.
Demand: sweep ac237 (28 Nov 2026), all 7 markets: 'can i convert proprietorship to pvt ltd', 'how to convert proprietorship to
pvt ltd', 'can we convert proprietorship firm to private limited company', 'can i transfer sole proprietorship to pvt ltd
company' - no page on the site (FAQ added in PR #902). User steer 26 Nov 2026: more call bookings / WhatsApp enquiries.
Facts: the Companies Act, 2013 has no conversion route for a sole proprietorship (Part I of Chapter XXI covers firms and other
bodies, and LLPs convert under their own route); the usual method is to incorporate a company and transfer the business to it.
Section 47(xiv) of the Income-tax Act, 1961: transfer of a sole proprietary concern to a company is not a transfer if all assets
and liabilities of the concern become the company's, the proprietor holds at least 50% of the company's voting power for five
years from the succession, and the proprietor receives no consideration other than shares; breach makes the gain taxable in
the company's hands (section 47A). GST: services by way of transfer of a going concern are exempt; unused input tax credit
moves with Form GST ITC-02; the company needs its own GST registration. Stamp duty on the transfer of immovable property is a
state levy. No fees, no portal menu paths, no office claims. advisory_lib.contact() is not used."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources
from build_lib import page, write_page

A.UPDATED = "Last updated: 28 November 2026."
SLUG = "convert-proprietorship-to-private-limited-company-india-business-transfer-section-47-xiv-gst-itc-02-2026"

C = ("WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with the business name, what it does, whether it is "
     "GST-registered, the main assets and liabilities (stock, equipment, property, loans), and who else will hold shares in the "
     "new company. Or book a call directly.")
PAGES = [dict(
    slug=SLUG,
    title="How to Convert a Proprietorship into a Private Limited Company in India (2026): Business Transfer, Section 47(xiv) Tax-Neutral Conditions, GST and ITC-02",
    em="new company, then move the business.",
    kicker="/ Sole proprietors growing into a company &middot; Tax, GST, bank and licences &middot; Updated 2026-11-28",
    lead=("<strong>A sole proprietorship cannot be converted directly into a company - the Companies Act has a conversion route for firms and LLPs, but not for proprietorships. "
          "The usual route is to incorporate a private limited company with you as a director and shareholder, then transfer the running business to it under a business transfer agreement.</strong> "
          "Done on the right terms, the transfer can be tax-neutral, GST-exempt as a transfer of a going concern, and carry your unused input tax credit across."),
    sections=[
        ("/ The route, step by step", "Incorporate, then transfer.",
         table(["Step", "What happens"], [
             ["1. Incorporate the company", "Name, directors, shareholding and registered office; the proprietor is a director and the main shareholder"],
             ["2. Agree the transfer", "Business transfer agreement listing the assets, liabilities, contracts and employees moving to the company"],
             ["3. Pay in shares", "The company allots shares to the proprietor as the price for the business"],
             ["4. Move GST", "Company takes its own GST registration; unused credit moved with Form ITC-02"],
             ["5. Move everything else", "Bank accounts, contracts, licences, Udyam, website and invoices in the company's name"]])
         + ul("<strong>Why a company:</strong> limited liability, the ability to issue shares to investors or employees, and a structure lenders and larger customers prefer.",
              "<strong>What stays with you:</strong> income tax returns of the proprietorship up to the date of transfer, and any liabilities not taken over.")),
        ("/ Making the transfer tax-neutral", "Section 47(xiv) conditions.",
         ul("<strong>All assets and liabilities</strong> of the proprietorship immediately before the transfer become the company's.",
            "<strong>At least 50% of the voting power</strong> of the company is held by the former proprietor, and continues for five years from the transfer.",
            "<strong>Shares only:</strong> the proprietor receives no consideration other than shares in the company.",
            "<strong>If a condition is broken within five years,</strong> the gain that was exempt becomes taxable in the company's hands - plan any fundraise or exit with this in mind.",
            "<strong>Under the new law:</strong> section 47(xiv) is the 1961 Act provision; for transfers from 1 April 2026 check the corresponding provision of the Income-tax Act, 2025.")
         + ul("<strong>GST:</strong> a transfer of a business as a going concern is exempt, so no GST is charged on the transfer itself.",
              "<strong>Stamp duty:</strong> transferring immovable property to the company attracts state stamp duty; leasing it to the company is an alternative to weigh.")
         + call_box("converting a proprietorship into a private limited company", ["Incorporation and the shareholding plan",
                                                                                     "Business transfer agreement and valuation",
                                                                                     "Section 47(xiv) conditions and the five-year lock",
                                                                                     "GST registration, ITC-02 and going-concern exemption",
                                                                                     "Bank, licences, Udyam and contracts"],
                    "Business name and activity, GST status, main assets and liabilities, other shareholders.")
         + sources("Companies Act, 2013 (incorporation; Part I of Chapter XXI for firms and other bodies); Income-tax Act, 1961 (sections 47(xiv) and 47A) and Income-tax Act, 2025; CGST Act and exemption notification for services by way of transfer of a going concern; CGST Rules (Form ITC-02); state stamp laws; site company registration and founder salary pages.")),
    ],
    faqs=[("Can a proprietorship be converted into a private limited company?", "Not directly. The Companies Act has a conversion route for partnership firms and LLPs but not for a sole proprietorship. You incorporate a new private limited company and transfer the running business to it under a business transfer agreement."),
          ("Is tax payable when a proprietorship is transferred to a company?", "Not if the conditions of section 47(xiv) are met: all assets and liabilities move to the company, the proprietor holds at least 50% of the voting power for five years, and the consideration is only shares. If a condition is broken within five years, the exempt gain becomes taxable in the company's hands."),
          ("Is GST charged on transferring the business to the company?", "No, a transfer of a business as a going concern is exempt from GST. The company takes its own GST registration and the unused input tax credit of the proprietorship is moved to it with Form ITC-02."),
          ("Can I keep my proprietorship's GST number for the company?", "No. A GSTIN is linked to the PAN of the business, and the company has its own PAN, so the company registers separately; the proprietorship's registration is cancelled once the business has moved."),
          ("What happens to bank accounts, licences and contracts?", "They move to the company: open a company bank account, transfer or reapply for licences such as shop and establishment and professional tax, update Udyam, and assign or re-sign customer and supplier contracts in the company's name."),
          ("What should I send to start?", "WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with the business name and activity, whether it is GST-registered, the main assets and liabilities, and who else will hold shares in the new company. Or book a call directly.")],
    related=[("private-limited-company-registration-india-2026-spice-plus-name-check-documents-directors-process.html", "Private limited company registration"),
             ("founder-salary-vs-dividend-india-private-limited-company-tax-director-remuneration-deemed-dividend-nri-founder-2026.html", "Founder salary vs dividend"),
             ("convert-llp-to-private-limited-company-india-tax-free-conditions-section-47-xiii-capital-gains-losses-2026.html", "Convert an LLP to a private limited company"),
             ("gst-consultant-online-india-registration-returns-lut-refund-notice-reply-gstr-9-near-me-2026.html", "GST consultant online")],
    cta_h="Ready to move your business into a company?", cta_b=C,
    keywords="convert proprietorship to private limited company, proprietorship to pvt ltd, convert sole proprietorship to company india, section 47(xiv), business transfer agreement, itc-02, transfer of going concern gst",
    desc="How to convert a proprietorship into a private limited company in India: incorporate a company and transfer the business; section 47(xiv) tax-neutral conditions (all assets and liabilities, 50% voting power for five years, shares only); GST going-concern exemption and ITC-02; bank and licences.",
    howto={"name": "How to convert a proprietorship into a private limited company", "description": "Incorporate, then transfer the business.", "steps": [
        {"name": "Incorporate the company", "text": "Proprietor as director and main shareholder."},
        {"name": "Sign a business transfer agreement", "text": "All assets and liabilities, paid for in shares."},
        {"name": "Move GST", "text": "New registration for the company; ITC-02 for unused credit."},
        {"name": "Move bank, licences and contracts", "text": "Everything in the company's name; close the proprietorship's registrations."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch KO complete")
