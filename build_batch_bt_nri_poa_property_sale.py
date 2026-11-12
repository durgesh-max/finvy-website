# -*- coding: utf-8 -*-
"""Batch BT (12 Nov 2026): NRI selling property in India from abroad through a power of attorney - POA steps plus tax steps.
Facts: a POA executed outside India is notarised abroad and apostilled (Hague Convention countries) or attested by the
Indian mission; it must be stamped in India within three months of first being received in India (Indian Stamp Act,
1899, section 18; adjudication by the Collector under section 32), and late stamping attracts penalty; registration is
needed where state rules require it for property powers. Tax: the buyer deducts TDS on the sale price at non-resident
rates unless the NRI obtains a lower or nil deduction certificate; from 1 October 2026 a buyer of property from a
non-resident can deduct and deposit TDS using PAN without a TAN; sale proceeds go to the NRO account; repatriation up to
USD 1 million per financial year from NRO balances with Form 15CA/15CB (Forms 145/146 under the 2025 Rules)."""
from urllib.parse import quote
from build_lib import page, write_page

UPDATED = "Last updated: 12 November 2026."


def wa(t):
    return "https://wa.me/917801887130?text=" + quote(t)


def ul(*x):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in x) + "</ul>"


def ol(*x):
    return "<ol>" + "".join(f"<li>{i}</li>" for i in x) + "</ol>"


CONTACT = ("WhatsApp +91 78018 87130 or email durgesh@bharatquantumprospera.com with the property city, purchase year and cost, the expected sale price and your country. "
           "We reply the same working day with the tax steps, the lower-TDS route and a fixed-scope quote; your lawyer handles the POA and sale deed.")
SLUG = "nri-sell-property-in-india-from-abroad-power-of-attorney-tds-repatriation-2026"
BOX = (f'<div style="border:1px solid var(--line);border-left:4px solid #C2312A;border-radius:10px;padding:16px 18px;margin:18px 0;background:var(--bg-soft)">'
       f'<p style="margin:0 0 8px;font-weight:600">The biggest avoidable cost is excess TDS</p>'
       f'<p style="margin:0">Without a lower deduction certificate the buyer deducts tax on the whole sale price, not on your gain, and the refund waits for your return. Apply before the deal is signed: '
       f'<a href="{wa("Hi Durgesh, I am an NRI selling property in India through a power of attorney. Can you get a lower TDS certificate?")}" target="_blank" rel="noopener"><strong>WhatsApp CA Durgesh Chavda</strong></a>.</p></div>')

PAGES = [dict(
    slug=SLUG,
    title="Selling Property in India While Living Abroad: Power of Attorney, TDS and Repatriation, Step by Step (2026)",
    em="sign once abroad, get the money out cleanly.",
    kicker="/ NRIs in the US, UK, UAE, Canada, Australia &middot; Property sale &middot; Updated 2026-11-12",
    lead=("You can sell a flat or plot in India without flying back. Sign a specific power of attorney abroad, have it notarised and apostilled (or attested at the Indian mission), and get it stamped in India within three months of it arriving there. "
          "On the tax side, the buyer will deduct TDS on the full sale price at non-resident rates unless you first obtain a lower deduction certificate; the money lands in your NRO account, and up to USD 1 million a financial year can be sent abroad with Form 15CA/15CB."),
    sections=[
        ("/ The power of attorney", "Do it in this order.",
         ol("<strong>Draft a specific POA</strong> for this property and sale (not a vague general one), naming the attorney and the powers: negotiate, sign the agreement and sale deed, receive payment into your NRO account, appear before the sub-registrar.",
            "<strong>Sign it abroad</strong> before a notary, then have it <strong>apostilled</strong> if the country is a Hague Apostille Convention member (US, UK, Canada, Australia and others), or attested by the Indian embassy or consulate.",
            "<strong>Courier it to India and stamp it within three months</strong> of it first being received in India; the Collector of Stamps adjudicates the duty. Late stamping attracts a penalty.",
            "<strong>Register it where required</strong>: many states require a registered POA for selling immovable property. Your lawyer confirms the rule for the property's state.")
         + BOX),
        ("/ The tax steps", "Start before the buyer pays.",
         ul("<strong>Work out the gain:</strong> sale price less indexed or actual cost, depending on when you bought; see <a href=\"nri-selling-indian-property-capital-gains.html\">capital gains for NRIs selling property</a>.",
            "<strong>Lower or nil TDS certificate:</strong> apply to the Income Tax Department so the buyer deducts tax on the gain, not the full price. Without it, TDS on the whole consideration can be far more than your actual tax.",
            "<strong>Buyer's TDS:</strong> from 1 October 2026 a buyer can deduct and deposit TDS on a purchase from a non-resident using PAN, without a TAN; see <a href=\"buying-property-from-nri-no-tan-form-141-from-1-october-2026.html\">the new buyer route</a>.",
            "<strong>Exemptions:</strong> reinvestment in another Indian residential property or specified bonds can reduce the tax; plan it before you sell.",
            "<strong>Your return:</strong> file in India for the year of sale to claim any refund of excess TDS, and report the sale in your country of residence with credit for Indian tax under the treaty."))
        ,
        ("/ Getting the money out", "From NRO to abroad.",
         ul("Sale proceeds are paid into your <strong>NRO account</strong>.",
            "You can remit up to <strong>USD 1 million per financial year</strong> from NRO balances, including property sale proceeds, after tax.",
            "The bank needs <strong>Form 15CA</strong> (and a CA's <strong>Form 15CB</strong> where applicable), now numbered Forms 145 and 146 under the Income-tax Rules, 2026.",
            "Keep the sale deed, TDS certificates and proof of the original purchase; banks ask for them.")
         + '<p>More: <a href="repatriate-money-from-india-to-abroad-nro-usd-1-million-15ca-15cb-2026.html">repatriating money from India (USD 1 million, 15CA/15CB)</a> &middot; <a href="sell-property-in-india-living-in-uk-usa-canada-australia-tax-both-countries-2026.html">tax in both countries on the sale</a> &middot; <a href="dubai-uae-nri-indian-income-above-15-lakh-deemed-resident-india-tax-2026.html">UAE NRIs: the INR 15 lakh deemed resident rule</a>.</p>'
         f'<p><strong>Sources:</strong> Indian Stamp Act, 1899, sections 18 and 32, and state stamp and registration rules; Hague Apostille Convention; Income-tax provisions on TDS on payments to non-residents and lower deduction certificates; FEMA rules on remittance from NRO accounts. <em>{UPDATED}</em> General information. BQP handles the tax and repatriation side; the POA and sale deed need a lawyer in the property&rsquo;s state.</p>'),
    ],
    faqs=[("Can an NRI sell property in India without coming to India?", "Yes. Sign a specific power of attorney abroad, have it notarised and apostilled or attested at the Indian mission, stamp it in India within three months of receipt, and register it where the state requires. The attorney then signs the sale deed."),
          ("How long is a power of attorney executed abroad valid for stamping in India?", "It must be stamped within three months of first being received in India under section 18 of the Indian Stamp Act. After that a penalty applies."),
          ("How much TDS does the buyer deduct when buying from an NRI?", "TDS at non-resident rates on the sale consideration unless the NRI obtains a lower or nil deduction certificate, which lets the buyer deduct on the actual gain instead."),
          ("How much of the sale money can I send abroad?", "Up to USD 1 million per financial year from your NRO account, after tax, with Form 15CA and, where applicable, a CA's Form 15CB."),
          ("Does the buyer need a TAN to buy from an NRI?", "Not from 1 October 2026: the buyer can deduct and deposit TDS using PAN."),
          ("Can BQP handle the tax side?", "Yes. " + CONTACT)],
    related=[("nri-selling-indian-property-capital-gains.html", "Capital gains for NRIs selling property"),
             ("repatriate-money-from-india-to-abroad-nro-usd-1-million-15ca-15cb-2026.html", "Repatriation: USD 1 million, 15CA/15CB"),
             ("buying-property-from-nri-no-tan-form-141-from-1-october-2026.html", "Buying from an NRI: no TAN from 1 October 2026")],
    cta_h="Selling property in India from abroad?", cta_b=CONTACT,
    keywords="NRI sell property in India from abroad, NRI power of attorney India property, POA apostille India, power of attorney stamping three months India, NRI property sale TDS lower deduction certificate, repatriate property sale proceeds USD 1 million, NRI property sale USA UK UAE",
    desc="Selling a flat or plot in India while living in the US, UK, UAE, Canada or Australia: how to execute and stamp a power of attorney (apostille, three-month rule), cut TDS with a lower deduction certificate, and repatriate up to USD 1 million a year with Form 15CA/15CB.",
    howto={"name": "How an NRI sells property in India from abroad", "description": "Power of attorney, tax and repatriation steps.", "steps": [
        {"name": "Execute a specific POA abroad", "text": "Notarise and apostille it, or attest it at the Indian mission."},
        {"name": "Stamp it in India within three months", "text": "Have it adjudicated and registered where the state requires."},
        {"name": "Get a lower TDS certificate", "text": "Apply before the sale so TDS is on the gain, not the full price."},
        {"name": "Repatriate from NRO", "text": "Send up to USD 1 million per financial year with Form 15CA/15CB."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch BT complete")
