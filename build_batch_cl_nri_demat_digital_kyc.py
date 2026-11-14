# -*- coding: utf-8 -*-
"""Batch CL (15 Nov 2026): news-led page. SEBI circular dated 4 November 2026 (ref HO/38/30/12(3)2026-MIRSD-POD2/I/25175/2026),
effective 3 December 2026: intermediaries may accept digital KYC (and re-KYC) from individual persons resident outside
India (NRIs, OCIs, foreign nationals) residing in FATF-compliant countries, removing the requirement to be physically in
India during digital onboarding; in-person verification may be by video; KYC uploaded to the KRA within 3 working days;
residents of non-compliant countries stay under existing rules; KYC done before 3 December 2026 continues under old rules.
SEBI circular of 11 November 2026: intermediaries that are reporting financial institutions align FATCA/CRS reporting,
onboarding and KYC with the Income-tax Rules, 2026.
NRI investing basics: repatriable (NRE) investment in listed shares through the Portfolio Investment Scheme with a
designated bank (and, since the June 2026 amendments, a designated repatriable rupee account); non-repatriable through NRO;
NDI (Third Amendment) Rules notified 12 June 2026 (effective 13 June): any individual resident outside India, including
NRIs and OCIs, may hold below 10% of a listed company's paid-up equity, 24% in aggregate (earlier 5% and 10%); listed equity gains: short-term 20%, long-term 12.5% above
INR 1.25 lakh a year; tax deducted at source on NRI gains.
Sources: Moneylife, LiveLaw, Outlook Money, CorpLawUpdates (checked 15 Nov 2026); FEMA NDI Rules, 2019."""
from urllib.parse import quote
from build_lib import page, write_page

UPDATED = "Last updated: 15 November 2026."


def wa(t):
    return "https://wa.me/917801887130?text=" + quote(t)


def ul(*x):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in x) + "</ul>"


def table(head, rows):
    return ("<table><thead><tr>" + "".join(f"<th>{h}</th>" for h in head) + "</tr></thead><tbody>"
            + "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows) + "</tbody></table>")


CONTACT = ("WhatsApp +91 78018 87130 or email durgesh@bharatquantumprospera.com with your country of residence, whether you hold NRE or NRO accounts and what you want to invest in. "
           "We reply the same working day on the FEMA route, TDS and your Indian return.")
SLUG = "nri-oci-demat-trading-account-digital-kyc-from-abroad-sebi-3-december-2026"
BOX = (f'<div style="border:1px solid var(--line);border-left:4px solid #C2312A;border-radius:10px;padding:16px 18px;margin:18px 0;background:var(--bg-soft)">'
       f'<p style="margin:0 0 8px;font-weight:600">Opening the account is now easier; the tax side is not.</p>'
       f'<p style="margin:0">TDS is deducted on NRI gains, treaty relief depends on documents, and your country of residence taxes the same gains. We handle the Indian return and refunds. '
       f'<a href="{wa("Hi Durgesh, I am an NRI and want to invest in Indian shares. Can you help with the tax side?")}" target="_blank" rel="noopener"><strong>WhatsApp CA Durgesh Chavda</strong></a>.</p></div>')

PAGES = [dict(
    slug=SLUG,
    title="NRIs and OCIs Can Do KYC for Indian Demat and Trading Accounts From Abroad (SEBI, From 3 December 2026): How It Works, PIS, Limits and Tax",
    em="no trip to India to open the account.",
    kicker="/ NRI &middot; OCI &middot; Investing &middot; SEBI &middot; Updated 2026-11-15",
    lead=("From <strong>3 December 2026</strong>, NRIs, OCI cardholders and foreign nationals living in <strong>FATF-compliant countries</strong> can complete <strong>KYC digitally from abroad</strong> to open or update Indian broking, demat and other market accounts, without being physically in India (SEBI circular dated <strong>4 November 2026</strong>). "
          "Verification can be done by video, and the intermediary uploads the KYC to the KYC registration agency within three working days. Residents of non-compliant countries stay under the existing rules. "
          "The FEMA rules on how NRIs invest are unchanged: <strong>repatriable investment in listed shares goes through your bank's designated route</strong> (traditionally the Portfolio Investment Scheme linked to an NRE account, and since June 2026 also a designated repatriable rupee account), non-repatriable investment through NRO. Since 13 June 2026 an individual may hold <strong>below 10%</strong> of a listed company (earlier 5%), with a <strong>24%</strong> aggregate."),
    sections=[
        ("/ What changes on 3 December 2026", "Digital KYC from abroad.",
         table(["Point", "Detail"], [
             ["Who", "Individual persons resident outside India: NRIs, OCIs and foreign nationals"],
             ["Where they live", "FATF-compliant countries; others continue under existing KYC rules"],
             ["What is allowed", "Digital submission of KYC information and documents, for new accounts and re-KYC; in-person verification can be by video"],
             ["Records", "Intermediary uploads the KYC to the KRA within 3 working days, so it can be reused across intermediaries"],
             ["Earlier KYC", "KYC completed before 3 December 2026 continues under the earlier rules"],
             ["Related", "SEBI's 11 November 2026 circular asks intermediaries to align FATCA/CRS self-certification and reporting with the Income-tax Rules, 2026, so expect a declaration request"]])),
        ("/ How NRIs invest in Indian shares", "FEMA rules (unchanged).",
         table(["Topic", "Rule"], [
             ["Repatriable (NRE)", "Listed shares through the bank's designated route: the Portfolio Investment Scheme linked to an NRE account, or the designated repatriable rupee account introduced in June 2026; ask your bank which it offers"],
             ["Non-repatriable (NRO)", "Through an NRO account and NRO demat"],
             ["Holding limits (from 13 June 2026)", "Any individual resident outside India, including NRIs and OCIs: below 10% of a listed company's paid-up equity; 24% for all such individuals together (earlier 5% and 10% for NRIs/OCIs); see <a href=\"foreign-individuals-invest-indian-listed-shares-fema-schedule-iii-2026.html\">the June 2026 amendment</a>"],
             ["Mutual funds", "Allowed, but some fund houses restrict US and Canada residents because of FATCA; check before investing"],
             ["Tax on listed equity", "Short-term gains 20%; long-term gains 12.5% above INR 1.25 lakh a year; tax deducted at source on NRI gains"]])
         + BOX
         + '<p>Related: <a href="nri-mutual-funds-india-tax.html">NRI mutual funds and tax</a> &middot; <a href="can-oci-open-nre-nro-account-nri-bank-accounts-tax-repatriation-2026.html">NRE vs NRO vs FCNR for NRIs and OCIs</a> &middot; <a href="foreign-individuals-invest-indian-listed-shares-fema-schedule-iii-2026.html">foreign individuals in listed Indian shares</a> &middot; <a href="best-ca-for-nri-tax-return-filing-india-2026.html">NRI tax return</a>.</p>'
         + f'<p><strong>Sources:</strong> SEBI circular dated 4 November 2026 on KYC for persons resident outside India (effective 3 December 2026); SEBI circular dated 11 November 2026 on FATCA/CRS under the Income-tax Rules, 2026; FEMA (Non-debt Instruments) Rules, 2019 and (Third Amendment) Rules, 2026 notified 12 June 2026 (investment by individuals resident outside India); Income-tax Act, 2025. Secondary coverage checked 15 November 2026: Moneylife, LiveLaw, Outlook Money, CorpLawUpdates. <em>{UPDATED}</em> General information, not investment advice.</p>'),
    ],
    faqs=[("Can NRIs complete KYC online from abroad for a demat account?", "Yes, from 3 December 2026, if they live in a FATF-compliant country. SEBI's 4 November 2026 circular removes the need to be physically in India for digital KYC; verification can be done by video."),
          ("Does this apply to OCI cardholders?", "Yes. It covers individual persons resident outside India, including NRIs, OCIs and foreign nationals, living in FATF-compliant countries."),
          ("What if I live in a country that is not FATF-compliant?", "The existing KYC requirements continue to apply to you."),
          ("Do NRIs still need a PIS account to trade shares?", "Repatriable investment in listed shares goes through the bank's designated route: the PIS account linked to NRE, or the designated repatriable rupee account introduced in June 2026. Non-repatriable investment goes through NRO."),
          ("How much can an NRI hold in one listed company?", "Since 13 June 2026, below 10% of its paid-up equity (earlier 5%), with 24% for all individual non-resident investors together."),
          ("How are NRI share gains taxed?", "Listed equity: short-term gains at 20%, long-term gains at 12.5% above INR 1.25 lakh a year, with tax deducted at source."),
          ("Can BQP help?", "Yes. " + CONTACT)],
    related=[("nri-mutual-funds-india-tax.html", "NRI mutual funds and tax"), ("can-oci-open-nre-nro-account-nri-bank-accounts-tax-repatriation-2026.html", "NRE vs NRO vs FCNR"),
             ("foreign-individuals-invest-indian-listed-shares-fema-schedule-iii-2026.html", "Foreign individuals in listed shares")],
    cta_h="Investing in Indian markets from abroad?", cta_b=CONTACT,
    keywords="NRI digital KYC from abroad SEBI, NRI demat account online from abroad, OCI demat account KYC, SEBI circular 4 November 2026 KYC NRI, FATF compliant countries KYC NRI, NRI PIS account, NRI 10% limit listed company 2026, NRI trading account India 2026, NRI share tax India",
    desc="SEBI's 4 November 2026 circular lets NRIs, OCIs and foreign nationals in FATF-compliant countries complete KYC digitally from abroad from 3 December 2026. What changes, PIS and NRE/NRO routes, the June 2026 limits (below 10% per individual, 24% aggregate) and tax on NRI share gains.",
    howto={"name": "How an NRI opens an Indian demat and trading account from abroad", "description": "Steps from 3 December 2026.", "steps": [
        {"name": "Choose the route", "text": "Repatriable (NRE with PIS) or non-repatriable (NRO)."},
        {"name": "Complete digital KYC", "text": "Submit KYC documents online and complete video verification with the broker or depository participant."},
        {"name": "Link bank and demat", "text": "Link the NRE/PIS or NRO account with the matching demat and trading account."},
        {"name": "Handle tax", "text": "Track TDS on gains, claim treaty relief where available and file the Indian return."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch CL complete")
