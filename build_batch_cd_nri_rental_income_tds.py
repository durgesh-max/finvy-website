# -*- coding: utf-8 -*-
"""Batch CD (14 Nov 2026): NRI landlords renting out property in India - tenant TDS and the landlord's return.
Facts: rent paid to a non-resident is subject to TDS under section 393(2) of the Income-tax Act, 2025 (formerly
section 195) at 30% plus cess (about 31.2%; surcharge above INR 50 lakh), with no minimum threshold; the tenant needs a
TAN and files the quarterly non-resident TDS statement (Form 144, formerly 27Q). The PAN-based no-TAN route from
1 October 2026 (Form 141) covers purchase of property from a non-resident, not rent. Lower or nil deduction
certificate: Form 128 (formerly Form 13). House property income: 30% standard deduction on net annual value after
municipal taxes, plus interest on a loan for the let-out property. Rent is current income: it can be repatriated from
the NRO account after tax with Forms 145/146 (formerly 15CA/15CB), outside the USD 1 million limit for capital.
Under tax treaties, income from immovable property is taxable where the property is (India); residence country gives
credit. Sources: TaxHeal, TDSMan (s.393(2)), Belong, DealPlexus (checked 14 Nov 2026); site form mapping page."""
from urllib.parse import quote
from build_lib import page, write_page

UPDATED = "Last updated: 14 November 2026."


def wa(t):
    return "https://wa.me/917801887130?text=" + quote(t)


def ul(*x):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in x) + "</ul>"


def table(head, rows):
    return ("<table><thead><tr>" + "".join(f"<th>{h}</th>" for h in head) + "</tr></thead><tbody>"
            + "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows) + "</tbody></table>")


CONTACT = ("WhatsApp +91 78018 87130 or email durgesh@bharatquantumprospera.com with the monthly rent, your other Indian income, any home loan on the property and your country of residence. "
           "We reply the same working day on a lower deduction certificate, the return and repatriation, with a fixed-scope quote.")
SLUG = "nri-rental-income-india-tenant-tds-31-2-percent-tan-form-144-2026"
BOX = (f'<div style="border:1px solid var(--line);border-left:4px solid #C2312A;border-radius:10px;padding:16px 18px;margin:18px 0;background:var(--bg-soft)">'
       f'<p style="margin:0 0 8px;font-weight:600">Most NRI landlords are over-deducted.</p>'
       f'<p style="margin:0">TDS is taken on the gross rent at about 31.2%, while tax is due only on rent after the 30% standard deduction, municipal tax and loan interest, at slab rates. A lower deduction certificate before the year starts keeps the money with you instead of waiting for a refund. '
       f'<a href="{wa("Hi Durgesh, I am an NRI renting out my flat in India. Can you help with a lower TDS certificate for my tenant?")}" target="_blank" rel="noopener"><strong>WhatsApp CA Durgesh Chavda</strong></a>.</p></div>')

PAGES = [dict(
    slug=SLUG,
    title="NRI Renting Out Property in India (2026): Tenant TDS at 31.2%, TAN, Form 144, Lower Deduction Certificate and Repatriation",
    em="the tenant deducts, the landlord claims it back.",
    kicker="/ NRI &middot; Rental income &middot; TDS &middot; Income-tax Act 2025 &middot; Updated 2026-11-14",
    lead=("When an NRI lets out a flat or house in India, the tenant must deduct tax from <strong>every rent payment, with no minimum threshold</strong>, at <strong>30% plus cess (about 31.2%)</strong> under section 393(2) of the Income-tax Act, 2025 (formerly section 195). "
          "The tenant needs a <strong>TAN</strong> and files the quarterly non-resident TDS statement, <strong>Form 144</strong> (formerly 27Q); the PAN-based no-TAN route from 1 October 2026 applies to buying property from an NRI, not to rent. "
          "The landlord is taxed only on rent after a <strong>30% standard deduction</strong>, municipal taxes and loan interest, so the excess TDS comes back through the return, or is avoided with a <strong>lower deduction certificate (Form 128, formerly Form 13)</strong>. Net rent can be sent abroad from the NRO account."),
    sections=[
        ("/ What the tenant must do", "Every month, from the first rupee.",
         table(["Step", "Detail"], [
             ["Deduct TDS", "30% plus 4% cess (about 31.2%) on the gross rent; surcharge applies if the landlord's income exceeds INR 50 lakh; lower rate if the landlord gives a certificate"],
             ["Get a TAN", "Required for a tenant deducting tax from rent paid to a non-resident"],
             ["Deposit and report", "Pay the TDS to the government and file the quarterly statement, Form 144 (formerly 27Q)"],
             ["Give a certificate", "Issue the TDS certificate to the landlord so the credit appears in the landlord's tax statement"],
             ["If the tenant does not deduct", "The tenant can be treated as in default, with interest; landlords should agree the process in the rent agreement"]])
         + "<p>The section and form numbers changed when the Income-tax Act, 2025 took effect on 1 April 2026; see <a href=\"old-vs-new-income-tax-form-numbers-2026-15ca-145-15cb-146-10f-41.html\">old vs new form numbers</a>.</p>"),
        ("/ What the landlord actually owes", "An example.",
         table(["Item", "Amount (INR)"], [
             ["Rent: 50,000 a month", "6,00,000"],
             ["TDS deducted by the tenant at about 31.2%", "1,87,200"],
             ["Less municipal tax paid (example)", "20,000"],
             ["Net annual value", "5,80,000"],
             ["Less 30% standard deduction", "1,74,000"],
             ["Income from house property", "4,06,000"]])
         + "<p>If this is the landlord's only Indian income, tax at the slab rates for the year is far below the INR 1,87,200 deducted, so most of it is refundable through the return, or avoidable with a lower deduction certificate. Interest on a loan taken for the let-out property is also deductible. Check the slab rates for the relevant year; NRIs do not get the rebate available to residents.</p>"
         + BOX),
        ("/ Landlord checklist", "Through the year.",
         ul("<strong>Before the year:</strong> apply for a lower or nil deduction certificate (Form 128) with an estimate of the year's rent and income, and give it to the tenant.",
            "<strong>Bank account:</strong> receive rent in your NRO account; it cannot be credited to an NRE account.",
            "<strong>Return:</strong> file the Indian return (usually ITR-2) by the due date and claim the TDS credit and refund.",
            "<strong>Repatriation:</strong> rent is current income, so after tax it can be remitted from the NRO account with the CA certificate and bank forms (Forms 145/146, formerly 15CA/15CB), outside the USD 1 million limit that applies to capital.",
            "<strong>Abroad:</strong> under India's tax treaties, income from immovable property is taxable in India; your country of residence taxes it too and gives credit for the Indian tax. Report it there (for example, US Schedule E, UK self-assessment, Canada T776, Australia rental schedule).")
         + '<p>Related: <a href="best-ca-for-nri-tax-return-filing-india-2026.html">NRI tax return filing</a> &middot; <a href="repatriate-money-from-india-to-abroad-nro-usd-1-million-15ca-15cb-2026.html">repatriating money from India</a> &middot; <a href="buying-property-from-nri-no-tan-form-141-from-1-october-2026.html">buying property from an NRI: no TAN from 1 October 2026</a>.</p>'
         + f'<p><strong>Sources:</strong> Income-tax Act, 2025, section 393(2) (formerly section 195 of the 1961 Act); Income-tax Rules, 2026 (Forms 128, 144, 145, 146); FEMA rules on NRO accounts and remittance of current income. Secondary summaries checked 14 November 2026: TaxHeal, TDSMan, Belong, DealPlexus. <em>{UPDATED}</em> General information, not advice for your situation.</p>'),
    ],
    faqs=[("How much TDS does a tenant deduct on rent paid to an NRI?", "30% plus 4% cess, about 31.2%, on the gross rent, with surcharge if the landlord's income exceeds INR 50 lakh. There is no minimum threshold, unlike rent paid to residents."),
          ("Does the tenant need a TAN to pay rent to an NRI?", "Yes. The PAN-based route without a TAN that started on 1 October 2026 applies to buying property from a non-resident, not to rent."),
          ("Which form does the tenant file?", "The quarterly non-resident TDS statement, Form 144 under the Income-tax Rules, 2026 (formerly Form 27Q), and a TDS certificate for the landlord."),
          ("Can an NRI landlord reduce the TDS?", "Yes. Apply for a lower or nil deduction certificate (Form 128, formerly Form 13) based on the expected income; the tenant then deducts at the certified rate."),
          ("How is NRI rental income taxed?", "As income from house property: net annual value (rent less municipal taxes) minus a 30% standard deduction and interest on a loan for the property, taxed at slab rates. Excess TDS is refunded through the return."),
          ("Can rent be sent abroad?", "Yes. Rent is current income; after tax it can be remitted from the NRO account with the CA certificate and bank forms, outside the USD 1 million limit for capital."),
          ("Can BQP get the lower TDS certificate and file the return?", "Yes. " + CONTACT)],
    related=[("best-ca-for-nri-tax-return-filing-india-2026.html", "NRI tax return filing"),
             ("repatriate-money-from-india-to-abroad-nro-usd-1-million-15ca-15cb-2026.html", "Repatriate money from India"),
             ("old-vs-new-income-tax-form-numbers-2026-15ca-145-15cb-146-10f-41.html", "Old vs new tax form numbers")],
    cta_h="Renting out your property in India from abroad?", cta_b=CONTACT,
    keywords="NRI rental income tax India, TDS on rent paid to NRI 2026, tenant TDS NRI landlord 31.2%, section 393(2) rent NRI, Form 144 27Q rent NRI, TAN required rent NRI, lower deduction certificate NRI rent Form 128, NRI rent repatriation NRO",
    desc="NRI landlords in 2026: tenant deducts TDS at about 31.2% on all rent under section 393(2) of the Income-tax Act, 2025, needs a TAN and files Form 144 (27Q); 30% standard deduction, lower deduction certificate (Form 128), NRO account, return and repatriation.",
    howto={"name": "How an NRI landlord handles tenant TDS in India", "description": "Steps for NRIs renting out property in India.", "steps": [
        {"name": "Estimate the year", "text": "Work out the rent, municipal taxes, loan interest and other Indian income for the year."},
        {"name": "Apply for a lower deduction certificate", "text": "File Form 128 so the tenant deducts at a lower or nil rate instead of about 31.2%."},
        {"name": "Make sure the tenant complies", "text": "The tenant obtains a TAN, deducts and deposits TDS, files Form 144 and issues the TDS certificate."},
        {"name": "File and repatriate", "text": "File the Indian return to claim any refund, then remit the net rent from the NRO account with Forms 145/146."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch CD complete")
