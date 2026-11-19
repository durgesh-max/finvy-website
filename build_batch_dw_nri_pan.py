# -*- coding: utf-8 -*-
"""Batch DW (20 Nov 2026): PAN for NRIs and OCIs in 2026 - apply from abroad with the new Form 93 / Form 95 (replacing
49A / 49AA from 1 April 2026), inoperative PAN consequences and fixes, reprints and corrections. Call-first page.
Demand: sweep 20 Nov 2026 (ac18), all 7 markets: "what happens if pan becomes inoperative", "pan card inoperative
means", "pan card replacement for nri", "nri pan card documents required", "nri pan card apply".
Facts (checked 20 Nov 2026): under the Income-tax Rules, 2026, Form 49A became Form 93 (Indian citizens) and Form 49AA
became Form 95 (foreign citizens, including OCI cardholders) from 1 April 2026; earlier applications remain valid
(Income Tax Department FAQ on Forms 93-96, KMGC, Visafoto); apply online via Protean (NSDL) or UTIITSL from abroad;
passport as identity proof, overseas address allowed, Aadhaar not required for NRIs; documents may need attestation;
processing commonly 15-20 days; fees differ for overseas dispatch - check the portal; inoperative PAN - refunds and
interest withheld and TDS/TCS at higher rates while inoperative; NRIs are exempt from PAN-Aadhaar linking but must
have non-resident status recorded, otherwise the PAN can show as inoperative (site page)."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 20 November 2026."
PAN = "nri-oci-pan-card-2026-apply-from-abroad-form-93-95-inoperative-pan-fix-refund"
NYE = "nri-year-end-tax-checklist-before-31-december-2026-refund-belated-itr-fast-ds-residency"

C_PAN = contact("your citizenship (Indian or OCI/foreign), whether you already have a PAN, its status on the portal, and any refund or TDS problem")
PAGES = [dict(
    slug=PAN,
    title="PAN Card for NRIs and OCIs (2026): Apply from Abroad with New Form 93 or 95, Fix an Inoperative PAN, and Unblock Refunds",
    em="what changed on 1 April 2026 and what to do if your PAN shows inoperative.",
    kicker="/ NRIs &middot; OCI &middot; PAN &middot; Updated 2026-11-20",
    lead=("NRIs and OCI cardholders can apply for a PAN from abroad online, through Protean (NSDL) or UTIITSL. From <strong>1 April 2026</strong> the forms have new numbers under the Income-tax Rules, 2026: <strong>Form 93</strong> (formerly 49A) for Indian citizens and <strong>Form 95</strong> (formerly 49AA) for foreign citizens, including OCIs. Your <strong>passport</strong> is the identity proof, an <strong>overseas address</strong> is accepted, and <strong>Aadhaar is not required</strong>. An existing PAN stays valid when you move abroad; never apply for a second one. "
          "If your PAN shows <strong>inoperative</strong>, refunds and interest on them are held back and TDS is deducted at higher rates, which hits NRIs selling property, earning rent or holding NRO deposits. NRIs are exempt from linking PAN with Aadhaar, but the department must have your <strong>non-resident status on record</strong>; otherwise the PAN can still show inoperative. Fix this before you file your FY 2025-26 return or claim a refund, and well before 31 December 2026."),
    sections=[
        ("/ Which form and what documents", "From 1 April 2026.",
         table(["You are", "Form (from 1 April 2026)", "Documents", "Notes"], [
             ["Indian citizen living abroad (NRI)", "Form 93 (formerly 49A)", "Indian passport; overseas address proof; photo and signature", "Aadhaar not required for NRIs"],
             ["OCI cardholder / foreign citizen", "Form 95 (formerly 49AA)", "Foreign passport and OCI card; overseas address proof", "Attestation may be needed for some documents"],
             ["Already have a PAN", "No new PAN; use the change/correction request", "Proof for the change (name, address, status)", "Holding two PANs attracts a penalty; surrender the duplicate"],
             ["Lost card", "Reprint or e-PAN download", "PAN details and verification", "e-PAN is accepted for most purposes"]])
         + call_box("my PAN or a blocked refund", ["Whether your PAN is operative and your status recorded as non-resident",
                                                   "How to fix an inoperative PAN without a second application",
                                                   "Refunds held back because of PAN status, and how to release them",
                                                   "TDS charged at higher rates on property sales, rent or NRO interest",
                                                   "Filing the FY 2025-26 return by 31 December 2026"],
                    "your PAN, a screenshot of its status on the e-filing portal, and details of any refund or TDS issue.")),
        ("/ Inoperative PAN: what happens and how to fix it", "Common for NRIs.",
         ul("<strong>Effects while inoperative:</strong> refunds are not issued and no interest is paid on them for that period; TDS and TCS apply at higher rates; banks, brokers and buyers may flag the PAN.",
            "<strong>Residents:</strong> link PAN with Aadhaar after paying the prescribed fee; the PAN becomes operative after linking.",
            "<strong>NRIs:</strong> you are exempt from linking, but your residential status must be updated with the department; NRIs often find their PAN marked inoperative because their records still show them as resident. See <a href=\"how-to-fix-pan-aadhaar-link-nri-oci-status-update-india.html\">fixing PAN status for NRIs and OCIs</a>.",
            "<strong>OCIs and foreign citizens:</strong> also exempt from linking; record status and passport details.",
            "<strong>After fixing:</strong> file or revise the return to claim refunds; see <a href=\"" + NYE + ".html\">NRI year-end checklist</a>.")),
        ("/ Where NRIs need a PAN", "And what goes wrong without one.",
         ul("<strong>Selling property:</strong> without a PAN, TDS can be charged at a higher rate; from 1 October 2026 buyers report the seller's PAN, or TRC and tax identification number if there is no PAN; see <a href=\"buying-property-from-nri-no-tan-form-141-from-1-october-2026.html\">buying property from an NRI</a>.",
            "<strong>Bank deposits, mutual funds, demat:</strong> PAN is required for KYC; see <a href=\"nri-oci-demat-trading-account-digital-kyc-from-abroad-sebi-3-december-2026.html\">digital KYC from abroad</a>.",
            "<strong>Filing returns and refunds:</strong> PAN is your login and refund account link; see <a href=\"which-itr-to-file-for-nri-ay-2026-27-itr-2-itr-3-refund-80c-deductions.html\">which ITR for NRIs</a>.",
            "<strong>New form numbers:</strong> see <a href=\"old-vs-new-income-tax-form-numbers-2026-15ca-145-15cb-146-10f-41.html\">old vs new income tax form numbers</a>.")
         + sources("Income-tax Rules, 2026 (Forms 93 to 96 replacing Forms 49A, 49AA and related forms from 1 April 2026) and Income Tax Department FAQs on Forms 93-96; Income-tax Act provisions on PAN, inoperative PAN and higher TDS/TCS. Secondary guides checked 20 November 2026: KMGC, Visafoto, Wise, BankBazaar. Fees and processing times vary; check the Protean or UTIITSL portal.")),
    ],
    faqs=[("Which form should an NRI use to apply for a PAN in 2026?", "Form 93 (formerly Form 49A) for Indian citizens living abroad, and Form 95 (formerly Form 49AA) for foreign citizens including OCI cardholders, from 1 April 2026. Applications on the old forms filed earlier remain valid."),
          ("Do NRIs need Aadhaar to get a PAN?", "No. NRIs and OCIs can apply with a passport and overseas address proof; Aadhaar is not required."),
          ("What happens if a PAN becomes inoperative?", "Refunds and interest on them are withheld and TDS or TCS is charged at higher rates until the PAN becomes operative again."),
          ("Why is my NRI PAN showing inoperative?", "NRIs are exempt from PAN-Aadhaar linking, but if the department's records still show you as resident, the PAN can be marked inoperative; update your residential status to fix it."),
          ("Can I apply for a new PAN if I lost mine?", "No. Request a reprint or download the e-PAN; holding two PANs is not allowed."),
          ("Can BQP fix my PAN status and claim my refund?", "Yes. " + C_PAN)],
    related=[("how-to-fix-pan-aadhaar-link-nri-oci-status-update-india.html", "Fix PAN status for NRIs and OCIs"), (NYE + ".html", "NRI year-end checklist"),
             ("old-vs-new-income-tax-form-numbers-2026-15ca-145-15cb-146-10f-41.html", "Old vs new form numbers")],
    cta_h="PAN problem holding up your refund?", cta_b=C_PAN,
    keywords="NRI PAN card apply 2026, Form 93 PAN NRI, Form 95 PAN OCI, Form 49AA replaced, what happens if PAN becomes inoperative, NRI PAN inoperative fix, PAN card replacement NRI, NRI PAN documents required",
    desc="PAN for NRIs and OCIs (2026): apply from abroad with Form 93 (was 49A) or Form 95 (was 49AA) from 1 April 2026; passport and overseas address, no Aadhaar; inoperative PAN effects (refunds held, higher TDS) and how NRIs fix status; reprints and duplicate PANs.",
    howto={"name": "How an NRI gets or fixes a PAN in 2026", "description": "Apply, check status and unblock refunds.", "steps": [
        {"name": "Check if you already have a PAN", "text": "Never apply twice; use change or reprint requests."},
        {"name": "Apply on the right form", "text": "Form 93 for Indian citizens, Form 95 for OCIs and foreign citizens, online via Protean or UTIITSL."},
        {"name": "Check status on the portal", "text": "Confirm the PAN is operative and your status is non-resident."},
        {"name": "Fix inoperative status", "text": "Residents link with Aadhaar; NRIs update residential status with the department."},
        {"name": "Claim refunds", "text": "File or revise the FY 2025-26 return by 31 December 2026."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch DW complete:", len(PAGES))
