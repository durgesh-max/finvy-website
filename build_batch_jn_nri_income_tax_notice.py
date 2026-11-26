# -*- coding: utf-8 -*-
"""Batch JN (27 Nov 2026): NRI income tax notice - why NRIs get notices from the Indian Income Tax Department and how to
reply from abroad (UAE / Dubai, US, UK and elsewhere).
Demand: sweep ac124 (27 Nov 2026), all 7 markets: "nri income tax notice", "nri getting income tax notice", "dubai nri
property income tax notice"; no existing page title targeted it.
User steer 26 Nov 2026: more call bookings / WhatsApp enquiries - high-intent service page.
Facts: e-Proceedings on the e-filing portal; DIN on every communication (CBDT Circular 19/2019); authorised representative;
reply within the time stated in the notice, adjournment on the portal; notice PDF password = PAN in lower case + date of
birth (DDMMYYYY); 143(1) demand - respond or pay within 30 days; 143(2) served within 3 months from the end of the FY of
filing; 148A show cause notice within 3 years (5 years where escaped income is Rs 50 lakh or more); no reply -> best
judgment assessment (section 144); deemed residence for Indian citizens with Indian income above Rs 15 lakh not liable to
tax elsewhere (section 6(1A), site page); India-UAE DTAA - gains on immovable property taxable where the property is (site
page); NRIs exempt from PAN-Aadhaar linking. No fees, no timings, no office claims."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 27 November 2026."
SLUG = "nri-income-tax-notice-india-why-nris-get-notices-how-to-reply-from-abroad-dubai-us-uk-2026"

C = contact("the notice PDF (the password is your PAN in lower case followed by your date of birth as DDMMYYYY), the assessment year, the returns you filed for that year, your Form 168 (old 26AS) and AIS, the country you live in and your days in India, and any property sale or purchase papers")
L = lambda h, t: f'<a href="{h}">{t}</a>'
PAGES = [dict(
    slug=SLUG,
    title="NRI Income Tax Notice (2026): Why NRIs Get Notices From the Indian Tax Department and How to Reply From Abroad (Dubai, US, UK)",
    em="read it, check it, reply on the portal from wherever you are.",
    kicker="/ NRIs, OCIs and Indians abroad &middot; Reply online, no visit needed &middot; Updated 2026-11-27",
    lead=("<strong>An NRI usually gets an Indian income tax notice because the department can see a transaction in India - a property sale or purchase, large deposits, NRO interest or TDS - that does not match a return, or because no return was filed at all.</strong> "
          "Living in Dubai, the US or the UK does not stop India taxing Indian income. Every notice can be answered online on the e-filing portal, by you or by a chartered accountant you authorise, without travelling to India. "
          "The first steps: check the DIN, note the deadline in the notice, and do not ignore it."),
    sections=[
        ("/ Why NRIs get notices", "The usual triggers.",
         table(["Trigger", "What the department sees", "Typical notice"], [
             ["Property sale with no return", "The buyer's TDS and the registrar's report show a sale, but no ITR declares the capital gain", "Non-filing e-campaign, section 142(1) or 148A"],
             ["Property purchase or large deposits", "High-value transactions in the AIS (property, deposits, mutual funds) with no matching income", "Information request or e-campaign asking for the source of funds"],
             ["TDS or AIS mismatch", "Income in Form 168 (old 26AS) / AIS different from the return", "Section 143(1) intimation with an adjustment or demand"],
             ["Residential status", "Days in India, or Indian income above Rs 15 lakh with no tax paid abroad (deemed resident)", "Scrutiny or a query on residential status"],
             ["Unreported NRO interest or rent", "Bank and tenant TDS returns report income the return left out", "143(1) adjustment or a 133(6) information notice"],
             ["Refund claims", "A large refund, treaty rates or deductions that need checking", "Section 143(2) scrutiny or a query before the refund is released"]])),
        ("/ How to reply from abroad", "Everything happens on the portal.",
         ul("<strong>Check the DIN:</strong> every genuine notice carries a document identification number you can verify on the e-filing portal (CBDT Circular 19/2019). Ignore emails asking you to pay through a link.",
            "<strong>Open the notice:</strong> log in to the e-filing portal with your PAN and open Pending Actions &gt; e-Proceedings. The PDF password is your PAN in lower case followed by your date of birth (DDMMYYYY).",
            "<strong>Note the deadline:</strong> reply within the time stated in the notice; if you need more time, ask for an adjournment on the portal with a reason.",
            "<strong>Authorise a CA:</strong> you can add a chartered accountant as your authorised representative on the portal so they can file the reply and attend video hearings.",
            "<strong>Verify online:</strong> replies and returns are verified with net banking, a digital signature or Aadhaar OTP if you have one (NRIs do not need to link Aadhaar with PAN).",
            "<strong>Do not ignore it:</strong> with no reply the officer can complete a best-judgment assessment, add income and levy interest and penalty.")),
        ("/ NRIs in Dubai and the UAE", "No UAE income tax does not mean no Indian tax.",
         ul("<strong>Indian income stays taxable in India:</strong> rent, NRO interest and capital gains on Indian property are taxed in India; under the India-UAE DTAA, gains on immovable property are taxed where the property is.",
            "<strong>Deemed residence:</strong> an Indian citizen with Indian income above Rs 15 lakh who is not liable to tax in any other country can be treated as resident (but not ordinarily resident) in India - a common trigger for queries on UAE-based NRIs.",
            "<strong>Property purchases:</strong> notices often ask how an Indian property was paid for; keep NRE / NRO statements and remittance records.",
            "<strong>Treaty rates:</strong> to use India-UAE DTAA rates you need a UAE tax residency certificate and Form 41 (old 10F).")
         + call_box("NRI notices", ["Checking the notice, DIN and time limit",
                                    "Reconciling Form 168 / AIS with your income",
                                    "Drafting and filing the reply on e-Proceedings",
                                    "Belated / revised return where one is still possible",
                                    "Appeal or rectification if the order is wrong"],
                    "the notice PDF, assessment year and your returns.")
         + sources("Income-tax Act, 1961 (sections 6, 133(6), 139, 142(1), 143, 144, 148A) and Income-tax Act, 2025; CBDT Circular 19/2019 (DIN); India-UAE DTAA; site notice-reply, AIS, deemed-resident and NRI ITR guides. Checked 27 November 2026.")),
    ],
    faqs=[("Why did I get an income tax notice as an NRI?", "Usually because a transaction in India - a property sale or purchase, deposits, NRO interest or TDS - appears in the department's records (Form 168 / AIS) but not in a return, or no return was filed. Residential status, refunds and treaty claims also lead to queries."),
        ("Why did I get an income tax notice about my NRE account?", "Usually because the NRE interest or large deposits appear in your AIS while your return shows you as resident, or does not explain them. NRE interest is exempt only while you are non-resident; if you have moved back to India and kept the NRE account, the interest becomes taxable and the account should be redesignated as a resident or RFC account. Reply with your days in India for the year, passport or travel records, the date the account was redesignated and the bank's interest certificate. If the interest was wrongly shown as taxable, give feedback in the AIS and explain it in the reply."),
          ("Can an NRI reply to an Indian income tax notice from abroad?", "Yes. Notices are answered on the e-filing portal under e-Proceedings. You can reply yourself or authorise a chartered accountant as your representative; video hearings are available where a hearing is needed. No visit to India is required."),
          ("How do I know an income tax notice is genuine?", "Check its DIN (document identification number) on the e-filing portal. Genuine notices also appear under Pending Actions when you log in with your PAN. Do not pay through links in emails or messages."),
          ("I live in Dubai and pay no tax there. Can India still tax me?", "Yes on Indian income - rent, NRO interest and gains on Indian property are taxed in India. An Indian citizen with Indian income above Rs 15 lakh who is not liable to tax anywhere else can also be treated as resident (not ordinarily resident) in India."),
          ("What happens if an NRI ignores an income tax notice?", "The officer can complete a best-judgment assessment on the information available, add income, and levy interest and penalty; refunds can be adjusted against the demand. It is always better to reply or ask for an adjournment within the time stated."),
          ("What should I send to reply to an income tax notice as an NRI?", "WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with the notice PDF, the assessment year, the returns filed for that year, Form 168 (old 26AS) and AIS, your country of residence and days in India, and any property sale or purchase papers and bank statements for the funds. We check the DIN and time limit, reconcile the figures and draft the reply for the portal."),
          ("Can BQP handle my NRI income tax notice?", "Yes. CA Durgesh Chavda works online with NRIs in the UAE, US, UK, Canada, Australia, Singapore and elsewhere. " + C)],
    related=[("how-to-respond-to-income-tax-notice-india.html", "How to respond to an income tax notice"),
             ("section-143-1-intimation-response-india-2026.html", "Section 143(1) intimation and demand"),
             ("ais-mismatch-itr-what-to-do-feedback-revised-return-31-december-2026-e-campaign-nri.html", "AIS mismatch and e-campaigns"),
             ("dubai-uae-nri-indian-income-above-15-lakh-deemed-resident-india-tax-2026.html", "Deemed resident rule for UAE NRIs"),
             ("nri-missed-itr-deadline-what-to-do-india.html", "Missed the ITR deadline"),
             ("ca-for-nri-in-india-nri-tax-consultant-online-pune-mumbai-delhi-bangalore-chennai-ahmedabad-hyderabad-2026.html", "CA for NRI in India")],
    cta_h="Got an Indian income tax notice?", cta_b=C,
    keywords="nri income tax notice, nri getting income tax notice, income tax notice for nri, dubai nri property income tax notice, nri reply income tax notice from abroad, income tax notice nri property sale, nri tax notice india",
    desc="NRI income tax notice: why NRIs get notices from the Indian Income Tax Department (property sale without a return, AIS mismatch, residential status, NRO interest), how to check the DIN and reply on e-Proceedings from Dubai, the US or the UK, and what to send a CA.",
    howto={"name": "How an NRI replies to an Indian income tax notice", "description": "Online, from abroad.", "steps": [
        {"name": "Check the DIN", "text": "Verify the notice on the e-filing portal."},
        {"name": "Note the deadline", "text": "Reply within the time stated, or ask for an adjournment."},
        {"name": "Reconcile", "text": "Match Form 168 / AIS with your income and documents."},
        {"name": "Reply on e-Proceedings", "text": "File the reply and annexures yourself or through an authorised CA."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch JN complete")
