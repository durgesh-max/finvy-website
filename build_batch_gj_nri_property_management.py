# -*- coding: utf-8 -*-
"""Batch GJ (24 Nov 2026): managing property in India from abroad - options (family with power of attorney, property
management company), the rent agreement, tenant TDS, NRO account, property tax, Indian return, repatriation, sale later.
Call-first page for NRIs; the firm handles the tax and FEMA side, not physical property management.
Demand: sweep ac59 (24 Nov 2026), all 7 markets: "nri property management services", "nri property management services
in india". Also on the 14 Nov demand list.
Facts (from site pages already checked): tenant deducts TDS on rent to an NRI at 30% plus cess (about 31.2%) under section
393(2) of the 2025 Act, from the first rupee, quarterly statement Form 144; lower deduction certificate Form 128; rent
taxed as house property with a 30% standard deduction; after-tax rent remitted from NRO with Forms 145/146 as current
income; a resident buyer can deposit TDS on a purchase from an NRI under own PAN (Form 141) from 1 October 2026."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 24 November 2026."
SLUG = "nri-property-management-india-from-abroad-power-of-attorney-rent-tds-itr-repatriation-2026"

C = contact("the property's city and type, whether it is let or vacant, who manages it today, the monthly rent, and your country of residence")
L = lambda h, t: f'<a href="{h}">{t}</a>'
PAGES = [dict(
    slug=SLUG,
    title="NRI Property Management in India (2026): Managing Your Flat From Abroad, Power of Attorney, Rent, TDS, Tax Return and Repatriation",
    em="someone holds the keys; you still own the tax.",
    kicker="/ NRIs &middot; Property in India &middot; Updated 2026-11-24",
    lead=("<strong>NRIs usually manage property in India through a trusted relative holding a registered power of attorney, or a property management company that finds tenants, collects rent and handles maintenance.</strong> "
          "Whoever manages it, the tax and FEMA duties stay with you: the tenant must deduct <strong>TDS of about 31.2%</strong> on rent paid to an NRI (from the first rupee), you file an <strong>Indian tax return</strong> to pay the right tax or claim the excess back, rent goes into your <strong>NRO account</strong>, and after-tax rent can be sent abroad with Forms 145 and 146. "
          "A <strong>lower deduction certificate (Form 128)</strong> can cut the TDS to your real tax, and a written, registered rent agreement protects you if a tenant does not pay or leave."),
    sections=[
        ("/ Quick answers", "What NRI owners ask.",
         ul("<strong>How can an NRI manage property in India?</strong> Through a family member or friend with a registered power of attorney, or a property management company under a written agreement. Either way, keep control of the bank account and the tax filings.",
            "<strong>Does the tenant have to deduct TDS for an NRI landlord?</strong> Yes: 30% plus cess (about 31.2%) on the gross rent from the first rupee, deposited under the tenant's TAN and reported in Form 144.",
            "<strong>How is NRI rental income taxed?</strong> As income from house property: rent minus municipal tax, minus a 30% standard deduction and home-loan interest, taxed at slab rates. Excess TDS comes back through your return.",
            "<strong>Can I send rent abroad?</strong> Yes. Rent is current income; after tax it can be remitted from the NRO account with Form 145 and a CA's certificate in Form 146.",
            "<strong>Who pays property tax and society charges?</strong> You, as owner; your manager can pay from your NRO account. Keep receipts: municipal tax paid is deductible from rent.")),
        ("/ Family vs property manager", "Choosing who manages it.",
         table(["", "Relative with power of attorney", "Property management company"], [
             ["Finds and vets tenants", "Yes, informally", "Yes, as a service"],
             ["Collects rent", "Into your NRO account (best)", "Usually into your NRO account; avoid rent going to their account"],
             ["Maintenance and repairs", "Depends on availability", "Included or charged separately"],
             ["Legal standing", "Registered power of attorney needed for agreements and court matters", "Service agreement; may also need a limited power of attorney"],
             ["Tax side", "Does not file your return", "Usually does not file your return"],
             ["Risk", "Family friction, informal records", "Fees, quality varies; check references and written terms"]])
         + '<p>Tax detail: ' + L("nri-rental-income-india-tenant-tds-31-2-percent-tan-form-144-2026.html", "TDS on rent paid to an NRI") + ' and ' + L("nri-rental-income-tds-refund-calculator-31-2-percent-vs-actual-tax-2026.html", "the NRI rent TDS refund calculator") + '.</p>'),
        ("/ Checklist", "Setting it up properly.",
         ul("<strong>Registered rent agreement</strong> with the tenant's PAN, rent, deposit, notice period and police verification where required.",
            "<strong>Rent into your NRO account</strong>, not a relative's or the manager's account, so income and TDS match your PAN.",
            "<strong>Tenant's TDS:</strong> make sure the tenant has a TAN, deducts TDS and gives you the TDS certificate; check Form 26AS.",
            "<strong>Lower deduction certificate:</strong> if your real tax is below 31.2%, apply in Form 128 before the year starts.",
            "<strong>File your Indian return</strong> every year with rent, deductions and TDS credit.",
            "<strong>Power of attorney:</strong> sign it abroad, notarise and apostille it (or attest at the Indian mission), then adjudicate it for stamp duty in India; limit its scope and revoke it when not needed.",
            "<strong>Selling later:</strong> see " + L("nri-selling-indian-property-capital-gains.html", "NRI property sale") + " and the country guides for the US, UK, Canada and Australia.")
         + call_box("tax on Indian property while you live abroad", ["Tenant TDS and Form 26AS check",
                                                                      "Lower deduction certificate (Form 128)",
                                                                      "Annual Indian tax return",
                                                                      "Repatriation of rent (Forms 145/146)",
                                                                      "Power of attorney and sale planning"],
                    "the property, rent, tenant and your country of residence.")
         + sources("Income-tax Act, 2025 (section 393(2), TDS on payments to non-residents) and Income-tax Rules, 2026 (Forms 128, 144, 145, 146); income from house property rules (30% standard deduction, municipal tax, interest); RBI rules on remittance of current income from NRO accounts; Registration Act and state stamp laws on powers of attorney and leases. Checked 24 November 2026.")),
    ],
    faqs=[("How can an NRI manage property in India?", "Through a trusted relative or friend holding a registered power of attorney, or a property management company under a written agreement. Keep the rent flowing into your own NRO account and keep filing your own Indian tax return."),
          ("What TDS does a tenant deduct for an NRI landlord?", "30% plus cess, about 31.2%, on the gross rent from the first rupee, using the tenant's TAN and the quarterly statement Form 144. A lower deduction certificate (Form 128) can reduce it."),
          ("Do NRIs have to file an Indian return for rental income?", "Yes, where Indian income exceeds the exemption or TDS is to be refunded. Rent is taxed as house property after a 30% standard deduction, and TDS deducted by the tenant is credited."),
          ("Can rent from Indian property be sent abroad?", "Yes. After tax, rent can be remitted from the NRO account as current income, with Form 145 and a chartered accountant's certificate in Form 146."),
          ("Should rent be paid to my relative or property manager in India?", "Better not. Have it paid into your NRO account so that the income, TDS and your PAN match, and so you keep control of the money."),
          ("Can BQP handle the tax side of my Indian property?", "Yes. " + C)],
    related=[("nri-rental-income-india-tenant-tds-31-2-percent-tan-form-144-2026.html", "TDS on rent paid to an NRI"),
             ("nri-rental-income-tds-refund-calculator-31-2-percent-vs-actual-tax-2026.html", "NRI rent TDS refund calculator"),
             ("nri-selling-indian-property-capital-gains.html", "NRI selling Indian property"),
             ("nre-nro-fcnr-account-tax-rules.html", "NRE, NRO and FCNR accounts"),
             ("can-nri-buy-property-in-india-residential-commercial-fema-payment-home-loan-tds-2026.html", "Can an NRI buy property in India")],
    cta_h="Property in India, you abroad?", cta_b=C,
    keywords="NRI property management India, NRI property management services in India, manage property in India from abroad, NRI rental income TDS 31.2%, power of attorney NRI property, NRI rent repatriation, NRI landlord India tax",
    desc="NRI property management in India (2026): relative with power of attorney or property management company; tenant TDS about 31.2% from the first rupee, Form 128 lower certificate, rent into NRO, Indian tax return, repatriating rent with Forms 145/146, and a setup checklist.",
    howto={"name": "How an NRI sets up management of a let property in India", "description": "Steps for tax-clean renting.", "steps": [
        {"name": "Choose a manager", "text": "Relative with registered power of attorney, or a property management company."},
        {"name": "Sign a registered rent agreement", "text": "With tenant PAN, rent, deposit and notice terms."},
        {"name": "Route rent to your NRO account", "text": "Not to the manager's account."},
        {"name": "Ensure tenant TDS", "text": "About 31.2% unless you hold a Form 128 certificate."},
        {"name": "File and repatriate", "text": "Indian return each year; remit after-tax rent with Forms 145/146."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch GJ complete")
