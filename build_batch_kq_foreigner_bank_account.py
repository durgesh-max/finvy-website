# -*- coding: utf-8 -*-
"""Batch KQ (28 Nov 2026): Can a foreigner open a bank account in India - by residence and purpose.
Demand: sweep ac238 (28 Nov 2026), all 7 markets: 'can a foreigner open a bank account in india', 'can a foreigner open a
savings account in india', 'can a non resident open a savings account in india' - no page on the site (FAQ added in PR #903).
User steer 26 Nov 2026: more call bookings / WhatsApp enquiries.
Facts (FEMA (Deposit) Regulations and the RBI Master Direction on deposits and accounts): a foreign national who is a person
resident in India under FEMA (for example living in India on an employment or business visa) can open an ordinary resident
account with passport, visa and residence registration where required; NRE and FCNR accounts are for non-resident Indian
citizens and persons of Indian origin (OCI cardholders); any person resident outside India may open an NRO account for bona
fide rupee transactions, with prior approval needed for nationals of certain countries; foreign tourists may open an NRO
account for up to six months; a person resident outside India with a business interest in India can open a Special
Non-Resident Rupee (SNRR) account for specified purposes; a foreign company banks in India through its subsidiary, branch,
liaison or project office, or an SNRR account. Repatriation from NRO is subject to limits and Forms 145/146. No fees, no
portal menu paths, no bank names, no office claims. advisory_lib.contact() is not used."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources
from build_lib import page, write_page

A.UPDATED = "Last updated: 28 November 2026."
SLUG = "can-foreigner-open-bank-account-in-india-resident-nro-nre-snrr-oci-tourist-company-2026"

C = ("WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with your nationality, whether you live in India or "
     "abroad, whether you hold an OCI card, and what the account is for (salary, rent, investment, business receipts). "
     "Or book a call directly.")
PAGES = [dict(
    slug=SLUG,
    title="Can a Foreigner Open a Bank Account in India? (2026) Resident Accounts, NRO, NRE for OCI Cardholders, Six-Month NRO for Tourists, SNRR and Company Accounts",
    em="it depends on residence and purpose.",
    kicker="/ Foreign nationals, OCI cardholders and foreign companies &middot; FEMA account rules &middot; Updated 2026-11-28",
    lead=("<strong>Yes - but the type of account depends on where you live and why you need it. A foreign national living in India can open an ordinary resident account; "
          "an OCI cardholder living abroad can open NRE and NRO accounts like an NRI; any non-resident can open an NRO account for genuine rupee transactions; "
          "tourists can keep an NRO account for up to six months; and a business interest in India can be handled through an SNRR account or the Indian entity.</strong>"),
    sections=[
        ("/ Which account fits you", "By residence and purpose.",
         table(["You are", "Account you can open", "Typical use"], [
             ["Foreign national living in India (for example on an employment visa)", "Ordinary resident savings or current account", "Salary, rent, daily expenses"],
             ["OCI cardholder or person of Indian origin living abroad", "NRE, NRO and FCNR, like an NRI", "Money from abroad (NRE), Indian income (NRO), foreign-currency deposits (FCNR)"],
             ["Any other person living abroad", "NRO account for bona fide rupee transactions", "Rent, dividends, sale proceeds, other Indian income"],
             ["Foreign tourist visiting India", "NRO account for up to six months", "Spending during the visit"],
             ["Person abroad with a business interest in India", "Special Non-Resident Rupee (SNRR) account", "Specified business transactions in rupees"],
             ["Foreign company", "Accounts of its Indian subsidiary, branch, liaison or project office; or SNRR", "Indian operations and receipts"]])
         + ul("<strong>Nationals of certain countries</strong> need prior RBI approval for some accounts; the bank will tell you if this applies.",
              "<strong>KYC:</strong> passport, visa or OCI card, proof of address (in India or abroad, depending on the account), PAN or a declaration where PAN is not held, and a photograph.",
              "<strong>Taking money out of India:</strong> NRE balances are freely repatriable; NRO balances can be repatriated within limits after tax, with Forms 145 and 146.")),
        ("/ When your status changes", "Re-designate the account.",
         ul("<strong>Moving to India:</strong> NRE and NRO accounts become resident accounts once you become resident under FEMA.",
            "<strong>Leaving India:</strong> a foreign national's resident account is re-designated as NRO when you leave to live abroad.",
            "<strong>Tax:</strong> interest on NRO and resident accounts is taxable in India, with TDS; NRE interest is tax-free only for NRIs and OCI cardholders who are non-resident.",
            "<strong>Investing:</strong> buying Indian shares or property brings its own FEMA rules - get the account right first.")
         + call_box("bank accounts in India for foreign nationals", ["Which account your status allows",
                                                                     "KYC and PAN",
                                                                     "Repatriation and Forms 145 / 146",
                                                                     "Tax on interest and TDS",
                                                                     "Accounts for a foreign company's Indian entity"],
                    "Nationality, where you live, OCI status, and what the account is for.")
         + sources("Foreign Exchange Management (Deposit) Regulations and the RBI Master Direction on deposits and accounts (resident, NRO, NRE, FCNR and SNRR accounts); FEMA rules on remittance from NRO accounts; Income-tax Act, 2025 and Income-tax Rules, 2026 (Forms 145 and 146); site NRE / NRO and foreign national company pages.")),
    ],
    faqs=[("Can a foreigner open a bank account in India?", "Yes. A foreign national living in India can open an ordinary resident account; an OCI cardholder living abroad can open NRE and NRO accounts; any person living abroad can open an NRO account for genuine rupee transactions; and a foreign tourist can open an NRO account for up to six months."),
          ("Can a foreigner open a savings account in India without living there?", "Yes, an NRO savings account, for bona fide rupee transactions such as rent, dividends or sale proceeds of Indian assets. NRE and FCNR accounts are only for non-resident Indian citizens and OCI cardholders or persons of Indian origin."),
          ("Can an OCI cardholder open an NRE account?", "Yes. OCI cardholders and persons of Indian origin living abroad can open NRE, NRO and FCNR accounts on the same footing as NRIs, and NRE interest is tax-free in India while they are non-resident."),
          ("Can a foreign tourist open a bank account in India?", "A foreign tourist can open an NRO account for up to six months to manage spending during the visit. For a longer stay, residence under FEMA allows an ordinary resident account."),
          ("How can a foreign company hold money in India?", "Through the bank accounts of its Indian subsidiary, branch, liaison or project office, or through a Special Non-Resident Rupee (SNRR) account for specified business transactions in rupees."),
          ("What should I send to start?", "WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with your nationality, where you live, whether you hold an OCI card and what the account is for. Or book a call directly.")],
    related=[("can-foreign-national-register-company-in-india-how-long-documents-resident-director-2026.html", "Can a foreign national register a company in India?"),
             ("nre-nro-fcnr-account-tax-rules.html", "NRE, NRO and FCNR tax rules"),
             ("rbi-approval-place-of-business-india-liaison-branch-project-office-form-fnc-2026.html", "Liaison, branch and project offices"),
             ("can-foreign-company-or-foreigner-buy-property-land-in-india-fema-rules-branch-subsidiary-lease-2026.html", "Can a foreigner buy property in India?")],
    cta_h="Need an Indian bank account as a foreign national?", cta_b=C,
    keywords="can a foreigner open a bank account in india, foreigner savings account india, non resident savings account india, nro account for foreigners, oci nre account, snrr account, foreign tourist bank account india",
    desc="Can a foreigner open a bank account in India? Resident account if living in India; NRE / NRO / FCNR for OCI cardholders; NRO for any non-resident with genuine rupee transactions; six-month NRO for tourists; SNRR or the Indian entity's accounts for business.",
    howto={"name": "How a foreign national chooses an Indian bank account", "description": "By residence and purpose.", "steps": [
        {"name": "Check residence", "text": "Living in India, or abroad; OCI card or not."},
        {"name": "Match the purpose", "text": "Salary, Indian income, money from abroad, or business."},
        {"name": "Prepare KYC", "text": "Passport, visa or OCI card, address proof, PAN or declaration."},
        {"name": "Plan repatriation and tax", "text": "NRE freely repatriable; NRO within limits with Forms 145 / 146."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch KQ complete")
