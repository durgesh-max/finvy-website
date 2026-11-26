# -*- coding: utf-8 -*-
"""Batch JL (26 Nov 2026): CA for NRI / NRI tax consultant in India - online service page for NRIs with income or property
in Pune, Mumbai, Delhi NCR, Bengaluru, Chennai, Ahmedabad, Hyderabad, Coimbatore and elsewhere.
Demand: sweep ac122 (26 Nov 2026), all 7 markets: "ca for nri", "ca for nri in india", "ca for nri tax filing (in india /
near me)", "ca for nri in pune / delhi", "ca for nri returning to india", "ca for nri property sale", "nri tax consultant
(near me / bangalore / chennai / delhi / coimbatore / mumbai / ahmedabad / pune)", "tax consultant india for nri".
User steer 26 Nov 2026: more call bookings / WhatsApp enquiries - high-intent service page.
Facts: site NRI ITR, NRI property sale lower TDS certificate (Form 128 / section 395), repatriation (NRO USD 1 million,
Forms 145 / 146), NRE / NRO, RNOR and notice pages; Indian Stamp Act s.18 (instrument executed abroad stamped within three
months of receipt in India). No office claims per city; no fees."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 26 November 2026."
SLUG = "ca-for-nri-in-india-nri-tax-consultant-online-pune-mumbai-delhi-bangalore-chennai-ahmedabad-hyderabad-2026"

C = contact("the country you live in, your PAN, what Indian income or property you have (rent, interest, capital gains, a sale coming up), the tax year and any deadline or notice")
L = lambda h, t: f'<a href="{h}">{t}</a>'
PAGES = [dict(
    slug=SLUG,
    title="CA for NRI in India (2026): NRI Tax Consultant for ITR Filing, Property Sale TDS, Refunds and Notices - Online for Pune, Mumbai, Delhi, Bangalore, Chennai, Ahmedabad and Hyderabad",
    em="one CA for your Indian tax, from wherever you live.",
    kicker="/ NRIs, OCIs and returning Indians &middot; Online, no visit needed &middot; Updated 2026-11-26",
    lead=("<strong>An NRI usually needs a chartered accountant in India for four things: filing the Indian income tax return, cutting the TDS a buyer or tenant deducts, getting refunds of excess TDS, and replying to notices.</strong> "
          "The tax rules are the same whether your property or income is in Pune, Mumbai, Delhi NCR, Bengaluru, Chennai, Ahmedabad, Hyderabad or Coimbatore, and the work is done online, so you do not need a CA near you. "
          "WhatsApp CA Durgesh Chavda your country, PAN and what you need, and you get a reply the same working day."),
    sections=[
        ("/ What an NRI tax consultant does", "The work NRIs most often need.",
         table(["Need", "What the CA does", "Guide"], [
             ["Income tax return", "Files ITR-2 (or ITR-3 with business income) for Indian income; NRIs cannot use ITR-1 or ITR-4", L("which-itr-to-file-for-nri-ay-2026-27-itr-2-itr-3-refund-80c-deductions.html", "Which ITR for an NRI")],
             ["Selling property", "Works out the capital gain and applies for a lower TDS certificate (Form 128, old Form 13) so the buyer does not withhold up to 14.95% of the price", L("nri-india-property-ldc-lower-deduction-certificate.html", "Lower TDS certificate")],
             ["TDS refund", "Claims back excess TDS on rent, interest or a property sale through the return", L("nri-income-tax-calculator-india-2026-27-new-old-regime-capital-gains-tds-refund.html", "NRI tax and refund calculator")],
             ["Moving money abroad", "Certifies Form 146 (old 15CB) and guides Form 145 (old 15CA) for NRO repatriation within USD 1 million a year", L("repatriate-money-from-india-to-abroad-nro-usd-1-million-15ca-15cb-2026.html", "Repatriation steps")],
             ["Notices", "Reads the notice, prepares the reply and files it on the e-proceedings portal", L("how-to-respond-to-income-tax-notice-india.html", "Responding to a notice")],
             ["Treaty relief", "Uses your tax residency certificate and Form 41 (old 10F) to apply DTAA rates", L("what-is-dtaa.html", "DTAA by country")],
             ["Returning to India", "Plans RNOR years, foreign assets reporting (Schedule FA) and accounts", L("best-ca-nri-returning-india-rnor-planning.html", "Returning NRI planning")]])),
        ("/ Key rules NRIs ask about", "The short answers.",
         ul("<strong>Do I have to file?</strong> Yes if your Indian income is above the basic exemption limit, and it is the only way to claim back excess TDS. The Rs 12 lakh tax-free limit (87A rebate) is for residents only.",
            "<strong>Property sale TDS:</strong> the buyer deducts TDS on the price, not the gain: up to 14.95% on a long-term sale. NRIs pay 12.5% on long-term gains without the indexation option, so a lower TDS certificate usually saves a lot of locked-up cash.",
            "<strong>Rent and interest:</strong> tenants and banks deduct TDS at high rates on payments to NRIs (about 31.2% on NRO interest unless a treaty rate applies); the excess comes back through the return.",
            "<strong>NRE and NRO:</strong> NRE interest is tax-free while you are non-resident; NRO interest is taxable.",
            "<strong>Deadlines now:</strong> a belated or revised return for AY 2026-27 can be filed until 31 December 2026; after that, only an updated return (ITR-U) with extra tax.")),
        ("/ Working with a CA from abroad", "No visit to India needed.",
         ul("<strong>Online from start to finish:</strong> documents by WhatsApp or email, returns e-verified with Aadhaar OTP, net banking or a digital signature.",
            "<strong>Any city:</strong> the income tax rules are national. What changes from city to city is property registration and stamp duty, handled at the local sub-registrar; a power of attorney signed abroad must be stamped in India within three months of reaching India.",
            "<strong>What to send first:</strong> your country of residence, PAN, Form 168 (old 26AS) and AIS if you can download them, and documents for any sale or remittance.",
            "<strong>Selling soon?</strong> Start before the sale agreement is signed so the lower TDS certificate is in place before the buyer pays.")
         + call_box("NRI tax", ["NRI income tax return (ITR-2 / ITR-3)",
                                "Lower TDS certificate for a property sale",
                                "TDS refunds on rent, interest and sales",
                                "Form 146 (old 15CB) and repatriation",
                                "Notice replies and returning-NRI planning"],
                    "your country, PAN and what you need.")
         + sources("Income-tax Act, 2025 and Income-tax Rules, 2026 (new form numbers); FEMA rules on NRO repatriation; Indian Stamp Act, 1899 (section 18); site NRI ITR, lower TDS certificate, repatriation, NRE / NRO and notice guides. Checked 26 November 2026.")),
    ],
    faqs=[("Do I need a CA near me if I am an NRI?", "No. NRI tax work is done online: documents by WhatsApp or email, the return e-verified with Aadhaar OTP, net banking or a digital signature. The tax rules are the same in every Indian city."),
          ("What does a CA for NRI do?", "Files the Indian income tax return (ITR-2 or ITR-3), applies for a lower TDS certificate before a property sale, claims TDS refunds, certifies Form 146 (old 15CB) for repatriation, replies to notices and plans the return to India."),
          ("Can an NRI file ITR without a CA?", "Yes, on the income tax portal. A CA helps where there is a property sale, capital gains, treaty relief, foreign tax credit, a refund to claim or a notice."),
          ("I have property in Pune / Mumbai / Bengaluru. Does the city change the tax?", "No. Income tax and TDS rules are national. Only property registration, stamp duty and local paperwork differ by state and city."),
          ("Can a CA help an NRI selling property in India?", "Yes. The CA works out the capital gain, applies for a lower TDS certificate (Form 128) so the buyer deducts only your actual tax, plans section 54 / 54EC reinvestment, and handles the return and repatriation afterwards."),
          ("How does an NRI get a TDS refund?", "By filing an Indian income tax return showing the actual tax; the excess TDS is refunded to an Indian bank account, with interest at 0.5% a month where it applies."),
          ("Can BQP be my CA for NRI tax?", "Yes. CA Durgesh Chavda works online with NRIs in the US, UK, UAE, Canada, Australia, Singapore and elsewhere. " + C)],
    related=[("ca-for-nri-tax-return-filing.html", "NRI tax filing in India"),
             ("nri-india-property-ldc-lower-deduction-certificate.html", "Lower TDS certificate for a property sale"),
             ("which-itr-to-file-for-nri-ay-2026-27-itr-2-itr-3-refund-80c-deductions.html", "Which ITR for an NRI"),
             ("repatriate-money-from-india-to-abroad-nro-usd-1-million-15ca-15cb-2026.html", "Repatriating money abroad"),
             ("best-ca-nri-returning-india-rnor-planning.html", "Returning to India")],
    cta_h="Need a CA for your Indian tax?", cta_b=C,
    keywords="ca for nri, ca for nri in india, nri tax consultant, nri tax consultant near me, ca for nri tax filing, nri tax consultant pune, nri tax consultant mumbai, nri tax consultant delhi, nri tax consultant bangalore, nri tax consultant chennai, nri tax consultant ahmedabad, ca for nri property sale, tax consultant india for nri",
    desc="CA for NRI in India: online NRI tax consultant for ITR-2 filing, lower TDS certificate on property sales, TDS refunds, Form 146 (old 15CB) repatriation and notice replies, for NRIs with income or property in Pune, Mumbai, Delhi, Bangalore, Chennai, Ahmedabad and Hyderabad.",
    howto={"name": "How to start with a CA for NRI tax", "description": "Online, from abroad.", "steps": [
        {"name": "Send the basics", "text": "Country, PAN and what you need on WhatsApp or email."},
        {"name": "Share documents", "text": "Form 168 (old 26AS), AIS and any sale or remittance papers."},
        {"name": "Agree the scope", "text": "A written scope before work starts."},
        {"name": "Review and verify", "text": "Check the return or application and e-verify online."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch JL complete")
