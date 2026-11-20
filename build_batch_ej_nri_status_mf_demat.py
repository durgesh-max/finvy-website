# -*- coding: utf-8 -*-
"""Batch EJ (20 Nov 2026): How to change NRI status in mutual funds and demat - resident to NRI (moving abroad) and NRI
to resident (returning). Call-first page.
Demand: sweep 20 Nov 2026 (ac23), all 7 markets: "how to update nri status in demat account", "how to change nri status
in mutual funds", "how to change nri status to resident in mutual funds", "how to change nri status in bank account",
"how to update kyc for nri", "how to remove nri status".
Facts (checked 20 Nov 2026; Business Standard 'Moving abroad? Changes you must make in your bank, demat and MF accounts',
Finnovate, MFCentral service list, broker/RTA guides): becoming an NRI does not force a sale of mutual fund units; the
change is a KYC / tax-status update with the RTAs (CAMS, KFintech) or through MFCentral ('Change of Tax Status'),
with FATCA/CRS declaration and a bank mandate changed to NRO or NRE; the bank account must first be redesignated as NRO;
overseas address proof is needed; some online KYC modification routes are for residents only, so a form may be needed;
SIPs can continue from NRE/NRO; some fund houses restrict US and Canada residents; demat and trading accounts must be
re-designated to NRI status - many brokers require a new NRI (NRO non-PIS) demat, transfer of shares and closure of
the resident account, while some depository participants change the status; returning NRIs reverse the process
(resident status, resident bank mandate, resident demat; NRE/NRO accounts converted). A transfer between your own demat
accounts on change of status is not a sale."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 20 November 2026."
SLUG = "change-nri-status-mutual-funds-demat-resident-to-nri-nri-to-resident-kyc-2026"
CHECK = "moving-abroad-from-india-becoming-nri-checklist-savings-account-to-nro-demat-mutual-funds-tax-2026"

C = contact("whether you are moving abroad or returning, your country, the fund houses and brokers you use, your bank accounts and whether you hold US or Canada residency")
PAGES = [dict(
    slug=SLUG,
    title="How to Change NRI Status in Mutual Funds and Demat (2026): Resident to NRI When You Move Abroad, NRI to Resident When You Return",
    em="KYC, bank mandate, FATCA and demat steps, in the right order.",
    kicker="/ NRI &middot; Mutual funds &middot; Demat &middot; KYC &middot; Updated 2026-11-20",
    lead=("When you become an NRI you <strong>do not have to sell your mutual funds or shares</strong>, but you must update your status. "
          "First get your bank to <strong>redesignate your savings account as NRO</strong>, or open an NRE account. Then change your <strong>tax status to NRI</strong> with the registrars (CAMS and KFintech) or through <strong>MFCentral</strong>, update your <strong>FATCA/CRS</strong> declaration and overseas address, and switch the <strong>bank mandate</strong> to the NRO or NRE account. Your SIPs can continue from the new account. "
          "For <strong>shares</strong>, the demat and trading account must become an NRI account. Many brokers require a new NRI (NRO, non-PIS) demat: you transfer the shares into it and close the resident account. Moving shares between your own accounts is not a sale. "
          "<strong>Returning to India</strong> reverses the steps: resident status, a resident bank mandate and a resident demat. Some fund houses limit investors resident in the <strong>US and Canada</strong>, so check before investing more."),
    sections=[
        ("/ Step by step", "Moving abroad and returning.",
         table(["Step", "Resident to NRI (moving abroad)", "NRI to resident (returning)"], [
             ["1. Bank account", "Redesignate savings as NRO; open NRE for foreign earnings", "Convert NRO to resident savings; NRE to resident or RFC"],
             ["2. Mutual fund status", "Change tax status to NRI with CAMS / KFintech or via MFCentral", "Change tax status to resident"],
             ["3. FATCA / CRS and address", "Declare foreign tax residency and overseas address", "Update to Indian tax residency and address"],
             ["4. Bank mandate and SIPs", "Switch to NRO or NRE; SIPs continue", "Switch to the resident account"],
             ["5. Demat and trading", "Open an NRI (NRO non-PIS) demat, transfer shares, close the resident account; or ask the DP to change status", "Open a resident demat and transfer, or ask the DP; close PIS"],
             ["6. Tax", "TDS applies to NRI redemptions; file an Indian return", "Plan RNOR years and foreign asset reporting"]])
         + call_box("Changing my NRI status across bank, funds and demat", ["The right order so nothing goes on hold",
                                                                            "Which holdings are repatriable and which are not",
                                                                            "TDS on redemptions and how to claim it back",
                                                                            "US and Canada fund-house restrictions and PFIC questions",
                                                                            "RNOR planning if you are returning"],
                    "your PAN, list of folios and demat accounts, bank accounts, move date and country.")),
        ("/ Points that trip people up", "Before you submit.",
         ul("<strong>Order matters:</strong> change the bank account first; a folio linked to a resident account after you become an NRI is a common reason for a status change being put on hold.",
            "<strong>Online vs form:</strong> some online KYC modification routes work only for residents; NRIs may need the registrar&rsquo;s change-of-status form with overseas address proof.",
            "<strong>Repatriation:</strong> units bought with resident money are non-repatriable; new investments from NRE are repatriable.",
            "<strong>US and Canada residents:</strong> several fund houses do not accept new investments from them; US persons also face PFIC rules on Indian funds; see <a href=\"what-is-pfic.html\">PFIC explained</a>.",
            "<strong>Tax on redemptions:</strong> fund houses deduct TDS from NRI capital gains; file an Indian return to claim any excess; see <a href=\"nri-mutual-funds-india-tax.html\">NRI mutual fund tax</a>.",
            "<strong>Digital KYC from abroad:</strong> see <a href=\"nri-oci-demat-trading-account-digital-kyc-from-abroad-sebi-3-december-2026.html\">NRI demat and digital KYC</a>.")
         + f'<p>Related: <a href="{CHECK}.html">becoming-an-NRI checklist</a> &middot; <a href="nri-nre-nro-conversion-returning-india-2026.html">converting NRE and NRO accounts when returning</a> &middot; <a href="nri-returning-india-tax-rnor-transition.html">returning NRI and RNOR</a>.</p>'
         + sources("SEBI and KYC registration agency processes for change of tax status; MFCentral service list (Change of Tax Status, FATCA/CRS, bank mandate); RBI Master Direction on Deposits and Accounts (NRO redesignation); broker and registrar guidance as reported by Business Standard ('Moving abroad? Changes you must make in your bank, demat and MF accounts') and Finnovate. Checked 20 November 2026. Each fund house and broker has its own forms.")),
    ],
    faqs=[("Do I have to sell my mutual funds when I become an NRI?", "No. You update your tax status, FATCA details, address and bank mandate with the fund house or registrar; the units continue."),
          ("How do I change my status to NRI in mutual funds?", "Redesignate your bank account as NRO (or open NRE), then submit a change of tax status to CAMS or KFintech or through MFCentral, with FATCA/CRS, overseas address proof and the new bank mandate."),
          ("How do I update NRI status in my demat account?", "The demat and trading account must become an NRI account. Many brokers ask you to open an NRI (NRO non-PIS) demat, transfer your shares into it and close the resident account; some depository participants can change the status directly."),
          ("How do I change NRI status back to resident in mutual funds?", "Convert your NRE/NRO account to a resident account, then submit a change of tax status to resident with the registrar or MFCentral, update FATCA and switch the bank mandate."),
          ("Can NRIs in the US or Canada continue SIPs?", "Existing investments usually continue, but several fund houses do not accept new investments from US or Canada residents; check each fund house."),
          ("Can BQP help me change my status correctly?", "Yes. " + C)],
    related=[(CHECK + ".html", "Becoming-an-NRI checklist"), ("nri-mutual-funds-india-tax.html", "NRI mutual fund tax"),
             ("nri-nre-nro-conversion-returning-india-2026.html", "Returning: NRE/NRO conversion")],
    cta_h="Moving abroad or coming back?", cta_b=C,
    keywords="how to change NRI status in mutual funds, how to update NRI status in demat account, change NRI status to resident mutual funds, resident to NRI KYC change, MFCentral change of tax status, CAMS KFintech NRI status, how to remove NRI status",
    desc="How to change NRI status (2026): no need to sell; redesignate the bank account to NRO, change tax status with CAMS/KFintech or MFCentral, update FATCA and bank mandate; convert demat to an NRI account; reverse the steps when returning. US/Canada limits noted.",
    howto={"name": "How to change your status to NRI in mutual funds and demat", "description": "Bank first, then funds, then demat.", "steps": [
        {"name": "Redesignate the bank account", "text": "Savings to NRO; open NRE if needed."},
        {"name": "Change tax status", "text": "With CAMS / KFintech or MFCentral, with overseas address proof."},
        {"name": "Update FATCA and bank mandate", "text": "Declare foreign tax residency; switch to NRO/NRE."},
        {"name": "Convert the demat account", "text": "Open an NRI demat and transfer shares, or ask the DP."},
        {"name": "Check every folio", "text": "Confirm the status changed and SIPs continue."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch EJ complete")
