# -*- coding: utf-8 -*-
"""Batch GR (24 Nov 2026): Renouncing Indian citizenship and the surrender certificate - the process in brief (Indian
citizenship ends on acquiring foreign citizenship under section 9 of the Citizenship Act; surrender the Indian passport
online through Passport Seva and the mission; some missions also require a renunciation declaration under section 8 on
the MHA portal), and what changes for money, tax and property: bank accounts, PAN and KYC, demat and mutual funds,
property, tax residence (deemed residence applies only to Indian citizens), OCI. Call-first page.
Demand: sweep ac79 (24 Nov 2026), all 7 markets, zero site coverage: "renounce indian citizenship", "indian citizenship
renunciation", "surrender indian passport", "surrender certificate", "renounce indian citizenship usa / canada /
australia / singapore", "renounce indian citizenship and apply for oci".
Facts (checked 24 Nov 2026): mission pages (Netherlands, Birmingham, Oman, Pretoria, Chicago, Dubai, US) and VFS
checklists: surrender application online on Passport Seva, with foreign passport, naturalisation certificate and the
original Indian passport; holding an Indian passport after acquiring foreign nationality is an offence under the Passports
Act; missions differ on whether a separate section 8 renunciation is needed. Tax and FEMA points as on site pages (OCI tax,
OCI bank accounts, deemed residence rule for Indian citizens, OCI property)."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 24 November 2026."
SLUG = "renounce-indian-citizenship-surrender-certificate-bank-accounts-pan-property-tax-oci-2026"

C = contact("the country whose citizenship you took and when, whether you have surrendered your Indian passport, and your Indian bank accounts, investments, property and income")
L = lambda h, t: f'<a href="{h}">{t}</a>'
PAGES = [dict(
    slug=SLUG,
    title="Renouncing Indian Citizenship (2026): Surrender Certificate, and What Changes for Your Bank Accounts, PAN, Property and Tax",
    em="the passport is the easy part; update the money side too.",
    kicker="/ NRIs becoming foreign citizens &middot; Updated 2026-11-24",
    lead=("<strong>India does not allow dual citizenship: Indian citizenship ends when you voluntarily take another country&rsquo;s citizenship, and you must then surrender your Indian passport and get a surrender certificate through the Indian mission, applying online on the Passport Seva portal.</strong> "
          "Some missions also ask for a renunciation declaration on the Ministry of Home Affairs portal; keeping or using an Indian passport after becoming a foreign citizen is an offence. "
          "The surrender certificate is then needed for an OCI card or Indian visa. On the money side, very little has to be closed, but a lot has to be <strong>updated</strong>: bank and demat KYC with your new passport, PAN details, how you hold Indian property, and your tax position, where losing citizenship ends the deemed-residence rule that catches some Indian citizens."),
    sections=[
        ("/ Quick answers", "What people giving up Indian citizenship ask.",
         ul("<strong>Do I have to renounce Indian citizenship?</strong> It ends automatically when you take foreign citizenship voluntarily (section 9 of the Citizenship Act); you then surrender the passport and, where your mission asks, file a renunciation declaration.",
            "<strong>How do I get a surrender certificate?</strong> Apply online on Passport Seva, then submit at the mission or its service provider with your foreign passport, naturalisation certificate and the original Indian passport; fees and processing vary by country.",
            "<strong>Can I keep my Indian bank accounts?</strong> Yes as a non-resident of Indian origin or OCI: NRE, NRO and FCNR accounts can continue, but update KYC with the foreign passport and OCI details.",
            "<strong>Can I keep my property in India?</strong> Yes. Property you already own stays yours; as an OCI you can also buy residential and commercial property, but not new agricultural land, plantations or farmhouses.",
            "<strong>Does it change my Indian tax?</strong> Residence still depends on days in India, but the deemed-residence rule for Indian citizens with high Indian income and no tax elsewhere no longer applies.")),
        ("/ Money checklist", "What to update after the surrender certificate.",
         table(["Item", "What to do"], [
             ["Bank accounts", "Tell each bank, update KYC with foreign passport and OCI; resident accounts must already be NRO; NRE and FCNR can continue"],
             ["PAN", "Keep the same PAN and update citizenship and address details; never apply for a second PAN"],
             ["Demat and mutual funds", "Update KYC and status to OCI/foreign national; some fund houses restrict residents of the US or Canada"],
             ["Property", "Keep existing property; new purchases limited to residential and commercial; sale proceeds repatriated within FEMA limits"],
             ["Insurance and pensions", "Update nationality and address with insurers, EPF and NPS"],
             ["Tax return", "Keep filing an Indian return where you have Indian income; report Indian assets in your new country as it requires"]])
         + '<p>Details: ' + L("can-oci-open-nre-nro-account-nri-bank-accounts-tax-repatriation-2026.html", "OCI bank accounts") + ', ' + L("nri-oci-pan-card-2026-apply-from-abroad-form-93-95-inoperative-pan-fix-refund.html", "PAN for OCIs") + ' and ' + L("oci-cardholder-tax-india-complete-2026.html", "OCI cardholder tax") + '.</p>'),
        ("/ Order of steps", "A practical sequence.",
         ul("<strong>1. Surrender the Indian passport</strong> soon after naturalisation and get the surrender certificate (and renunciation certificate if your mission requires it).",
            "<strong>2. Apply for OCI</strong> using the surrender certificate, so you can live, work and hold property in India without a visa.",
            "<strong>3. Update banks, PAN, demat and insurers</strong> with the new passport and OCI number.",
            "<strong>4. Review tax:</strong> your residence days, Indian income, treaty position and home-country reporting; see " + L("dubai-uae-nri-indian-income-above-15-lakh-deemed-resident-india-tax-2026.html", "deemed residence for Indian citizens") + ".",
            "<strong>5. Plan property:</strong> what to keep, sell or gift, and how to repatriate; see " + L("us-citizen-buy-own-property-india-oci-fema-tax-fbar-2026.html", "foreign citizens owning Indian property") + ".")
         + call_box("money, tax and property after giving up Indian citizenship", ["Bank, demat and PAN updates",
                                                                                   "Indian tax residence and treaty position",
                                                                                   "Property: keep, sell, gift or repatriate",
                                                                                   "Home-country reporting of Indian assets",
                                                                                   "Clean-up of old accounts and filings"],
                    "your new citizenship, passport status and Indian assets and income.")
         + sources("Citizenship Act, 1955, sections 8 and 9; Passports Act, 1967; Indian mission and consulate pages on surrender of Indian passport and renunciation (Netherlands, Birmingham, Oman, Pretoria, Chicago, Dubai, United States) and VFS Global checklists (2026); FEMA rules on accounts and property of OCIs and persons of Indian origin; Income-tax Act residence rules. Immigration steps are handled with the mission; BQP advises on tax, FEMA and money. Checked 24 November 2026.")),
    ],
    faqs=[("How do I renounce Indian citizenship?", "Indian citizenship ends automatically when you voluntarily take another country's citizenship. You then surrender your Indian passport and get a surrender certificate by applying online on Passport Seva and submitting at the Indian mission or its service provider; some missions also require a renunciation declaration on the Ministry of Home Affairs portal."),
          ("What is a surrender certificate?", "The certificate the Indian mission issues when you surrender your Indian passport after becoming a foreign citizen. You need it to apply for an OCI card or an Indian visa; using or keeping an Indian passport after taking foreign citizenship is an offence."),
          ("Can I keep my Indian bank accounts after giving up Indian citizenship?", "Yes. As a person of Indian origin or OCI you can keep NRE, NRO and FCNR accounts; update KYC with your foreign passport and OCI details. Resident savings accounts should already have been converted to NRO when you became non-resident."),
          ("Can I keep property in India after renouncing citizenship?", "Yes. Property you already own stays yours. As an OCI you can buy residential and commercial property but not new agricultural land, plantations or farmhouses, and sale proceeds are repatriated within FEMA limits."),
          ("Does renouncing Indian citizenship change my Indian tax?", "Tax residence still depends on days spent in India, and Indian income stays taxable in India. But the deemed-residence rule, which can treat Indian citizens with high Indian income and no tax elsewhere as resident, no longer applies."),
          ("Can BQP help after I give up Indian citizenship?", "Yes. " + C)],
    related=[("oci-cardholder-tax-india-complete-2026.html", "OCI cardholder tax"),
             ("can-oci-open-nre-nro-account-nri-bank-accounts-tax-repatriation-2026.html", "OCI bank accounts"),
             ("nri-oci-pan-card-2026-apply-from-abroad-form-93-95-inoperative-pan-fix-refund.html", "PAN for NRIs and OCIs"),
             ("us-citizen-buy-own-property-india-oci-fema-tax-fbar-2026.html", "Foreign citizens owning Indian property"),
             ("nri-oci-demat-trading-account-digital-kyc-from-abroad-sebi-3-december-2026.html", "Demat and KYC from abroad")],
    cta_h="Just became a foreign citizen?", cta_b=C,
    keywords="renounce Indian citizenship, Indian citizenship renunciation, surrender Indian passport, surrender certificate India, renounce Indian citizenship USA, renounce Indian citizenship Canada, renounce Indian citizenship Australia, OCI after renunciation, bank account after renouncing Indian citizenship",
    desc="Renouncing Indian citizenship (2026): citizenship ends on taking foreign citizenship; surrender the Indian passport online via Passport Seva for a surrender certificate (needed for OCI); then update bank and demat KYC, PAN, property and tax - accounts and property can be kept, deemed residence no longer applies.",
    howto={"name": "What to do after taking foreign citizenship", "description": "Passport, OCI and money steps.", "steps": [
        {"name": "Surrender the Indian passport", "text": "Apply on Passport Seva and get the surrender certificate."},
        {"name": "Apply for OCI", "text": "Using the surrender certificate."},
        {"name": "Update banks and PAN", "text": "KYC with foreign passport and OCI; same PAN, updated details."},
        {"name": "Review tax", "text": "Residence days, Indian income, treaty and home-country reporting."},
        {"name": "Plan property", "text": "Keep, sell or gift; repatriate within FEMA limits."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch GR complete")
