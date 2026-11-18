# -*- coding: utf-8 -*-
"""Batch DB (18 Nov 2026): can an NRI start a business in India - sole proprietorship, partnership, OPC, LLP or
private limited company. Demand: autocomplete sweep 18 Nov 2026 (ac10), all 7 markets: "can nri start a business in
india while working in usa", "can nri open sole proprietorship in india", "nri sole proprietorship india", "can nri
open partnership firm in india", "can nri open one person company in india"; no page on the site.
Facts: FEMA (Non-Debt Instruments) Rules, 2019, rule 12 and Schedule IV - NRIs/OCIs may contribute capital to a
proprietary concern, partnership firm or LLP on a non-repatriation basis without limit (deemed domestic investment),
except agricultural/plantation activity, real estate business and print media; repatriable investment in a firm or
proprietorship needs RBI approval; investment must be made by the NRI directly. OPC: Companies (Incorporation) Second
Amendment Rules, 2021, effective 1 April 2021 - an Indian citizen whether resident in India or otherwise can form an
OPC; 'resident' for OPC purposes is 120 days in the preceding financial year. LLP (Amendment) Act, 2021 / LLP rules
from 1 April 2022 - at least two designated partners, one resident in India (120 days in the financial year); FDI in
LLPs under the automatic route in sectors open to 100% automatic FDI without FDI-linked conditions. Private company:
section 149(3) - one director resident 182 days in the financial year; FC-GPR within 30 days of allotment for
repatriable investment. Tax: section 115BAA 22% plus surcharge and cess (25.168%); US persons owning foreign entities:
Forms 5471 / 8865 / 8858, FBAR and Form 8938; UAE NRIs with Indian income above INR 15 lakh not taxed elsewhere can be
deemed resident (RNOR). Sources: Mondaq/S.S. Rana (OPC 2021), Khaitan, SetIndiaBiz (LLP 120 days), TaxGuru, BCAJ
(Schedule IV) - checked 18 Nov 2026."""
from urllib.parse import quote
from build_lib import page, write_page

UPDATED = "Last updated: 18 November 2026."


def wa(t):
    return "https://wa.me/917801887130?text=" + quote(t)


def ul(*x):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in x) + "</ul>"


def table(head, rows):
    return ("<table><thead><tr>" + "".join(f"<th>{h}</th>" for h in head) + "</tr></thead><tbody>"
            + "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows) + "</tbody></table>")


CONTACT = ("Email info@bharatquantumprospera.com or WhatsApp +91 78018 87130 with your country of residence, citizenship (Indian or OCI), the business you plan, who will run it day to day in India, and whether profits must go abroad. "
           "We reply within one working day with the recommended structure, the registrations and a fixed-scope quote.")
SLUG = "can-nri-start-business-in-india-sole-proprietorship-partnership-opc-llp-company-2026"
BOX = (f'<div style="border:1px solid var(--line);border-left:4px solid #C2312A;border-radius:10px;padding:16px 18px;margin:18px 0;background:var(--bg-soft)">'
       f'<p style="margin:0 0 8px;font-weight:600">The structure decides whether profits can leave India.</p>'
       f'<p style="margin:0">A proprietorship or firm funded on a non-repatriation basis is simple, but the money is meant to stay in India. An LLP or private company with repatriable investment lets you take profits abroad, with more filings. We set up the entity, the bank accounts and the tax registrations, and run compliance while you are abroad. '
       f'<a href="{wa("Hi Durgesh, I am an NRI and want to start a business in India. Which structure should I use?")}" target="_blank" rel="noopener"><strong>WhatsApp CA Durgesh Chavda</strong></a>.</p></div>')

PAGES = [dict(
    slug=SLUG,
    title="Can an NRI Start a Business in India? (2026) Sole Proprietorship, Partnership, OPC, LLP or Private Limited Company Compared",
    em="for NRIs in the US, UAE, UK, Singapore, Canada and Australia.",
    kicker="/ NRIs &middot; Business set-up &middot; FEMA &middot; Updated 2026-11-18",
    lead=("Yes. An NRI or OCI can own a business in India while living abroad, and the choice of structure decides how the money can move. "
          "A <strong>sole proprietorship or partnership firm</strong> can take an NRI's capital only on a <strong>non-repatriation basis</strong> (treated as domestic money, with no limit) unless the RBI approves otherwise. It cannot be in agriculture or plantations, real estate business or print media. "
          "Since <strong>1 April 2021</strong> an Indian citizen living abroad can form a <strong>One Person Company (OPC)</strong>. An <strong>LLP</strong> needs at least one designated partner resident in India (120 days in the financial year). A <strong>private limited company</strong> needs one director resident in India (182 days in the financial year) and is the usual choice when profits or exit proceeds must go abroad: most sectors allow <strong>100% foreign investment under the automatic route</strong>. "
          "Indian business income is taxed in India; NRIs living in the US also report the Indian entity to the IRS, and UAE-based NRIs should check India's <strong>deemed residence</strong> rule."),
    sections=[
        ("/ The five structures", "Side by side.",
         table(["Structure", "Can an NRI own it?", "Money abroad?", "Who runs it in India", "Good for"], [
             ["Sole proprietorship", "Yes, non-repatriation basis (Schedule IV, NDI Rules)", "The capital stays in India; current profits after tax, credited to an NRO account, can be remitted with Forms 15CA/15CB", "NRI as proprietor; a local manager or power of attorney for day-to-day work (the investment itself must be made by the NRI)", "Small trading or service business, testing a market"],
             ["Partnership firm", "Yes, non-repatriation basis; repatriable needs RBI approval", "As for a proprietorship", "Resident partners usually manage", "Family businesses with resident relatives"],
             ["One Person Company", "Yes, for Indian citizens resident or not (from 1 April 2021); OCIs and foreign citizens cannot", "Repatriable or non-repatriable investment as a company", "Sole member-director, with a nominee", "Solo founder who wants limited liability"],
             ["LLP", "Yes; repatriable FDI only in sectors open to 100% automatic FDI without conditions", "Profit share can be repatriated for FDI-funded LLPs", "Two designated partners, one resident in India (120 days in the financial year)", "Consultancies and professional services"],
             ["Private limited company", "Yes; 100% FDI automatic route in most sectors", "Dividends, buy-backs and sale proceeds can be repatriated", "Two directors, one resident in India (182 days in the financial year)", "Anything you want to scale, raise money for or sell"]])
         + BOX),
        ("/ Working from abroad", "What NRIs in the US and the Gulf ask.",
         ul("<strong>While working in the USA:</strong> owning an Indian business is generally allowed, but actively working in it can conflict with some US visas (for example H-1B or F-1); take US immigration advice before you take an active role.",
            "<strong>US reporting:</strong> a US tax resident who owns 10% or more of an Indian company usually files <strong>Form 5471</strong> (Form 8865 for a partnership, Form 8858 for an entity treated as disregarded), plus <strong>FBAR</strong> and Form 8938 for Indian accounts, and the controlled foreign corporation rules can tax undistributed profits. Indian tax paid is creditable under the India-US treaty. See <a href=\"what-is-fbar.html\">FBAR basics</a>.",
            "<strong>UAE and other no-tax countries:</strong> an Indian citizen with Indian income above INR 15 lakh who is not liable to tax in any other country can be treated as resident (not ordinarily resident) in India; see <a href=\"dubai-uae-nri-indian-income-above-15-lakh-deemed-resident-india-tax-2026.html\">deemed residence for UAE NRIs</a>.",
            "<strong>Signing from abroad:</strong> directors and designated partners need a DIN and a Class 3 digital signature; documents signed abroad are usually notarised and apostilled. See <a href=\"din-for-foreign-national-director-india-documents-apostille-dsc-process-2026.html\">DIN and digital signature from abroad</a>.",
            "<strong>Funding the business:</strong> equity, or a loan from you as director or shareholder under the 2026 ECB rules; see <a href=\"loan-from-nri-director-shareholder-to-indian-company-ecb-2026-rules.html\">loans from NRI directors</a>.")),
        ("/ Tax and registrations", "The first-year list.",
         ul("<strong>Tax rates:</strong> a proprietorship is taxed at the NRI's individual slab rates; a domestic company can opt for 22% plus surcharge and cess (25.168%) under section 115BAA; an LLP pays 30% plus surcharge and cess. See <a href=\"which-is-better-llp-vs-private-limited-india.html\">LLP vs private limited</a>.",
            "<strong>Registrations:</strong> PAN, GST (if turnover crosses the threshold or for inter-state or export supplies), Udyam (MSME), shop and establishment licence, import-export code for trade, and a business bank account (banks' requirements for non-resident proprietors differ).",
            "<strong>FEMA filings:</strong> none for non-repatriable capital in a firm or proprietorship; FC-GPR within 30 days of share allotment and the annual FLA return for a company with foreign investment. See <a href=\"form-fc-gpr-filing-checklist-india-2026.html\">FC-GPR checklist</a>.",
            "<strong>Annual compliance:</strong> income-tax return and tax audit where applicable; for companies and LLPs, ROC annual filings (AOC-4, MGT-7 or Form 8 and Form 11).")
         + '<p>Related: <a href="nri-returning-startup-moving-to-india.html">returning NRIs starting up in India</a> &middot; <a href="nominee-resident-director-india-foreign-company.html">resident director options</a> &middot; <a href="nre-nro-fcnr-account-tax-rules.html">NRE and NRO accounts</a>.</p>'
         + f'<p><strong>Sources:</strong> Foreign Exchange Management (Non-Debt Instruments) Rules, 2019 (rule 12 and Schedule IV); Companies (Incorporation) Second Amendment Rules, 2021 (OPC, from 1 April 2021); Limited Liability Partnership (Amendment) Act, 2021 and LLP rules (resident designated partner, 120 days); Companies Act, 2013, section 149(3); Consolidated FDI Policy; Income-tax Act, 2025. Secondary summaries checked 18 November 2026: Mondaq / S.S. Rana, Khaitan &amp; Co, SetIndiaBiz, TaxGuru, BCAJ. <em>{UPDATED}</em> General information; US immigration and tax points need advice in the US.</p>'),
    ],
    faqs=[("Can an NRI start a business in India?", "Yes. An NRI can own a sole proprietorship or partnership on a non-repatriation basis, form a One Person Company (Indian citizens only), or set up an LLP or private limited company with repatriable foreign investment in most sectors."),
          ("Can an NRI open a sole proprietorship in India?", "Yes, with capital on a non-repatriation basis under Schedule IV of the FEMA Non-Debt Instruments Rules, as long as the business is not agriculture or plantations, real estate business or print media. Repatriable investment in a proprietorship needs RBI approval."),
          ("Can an NRI form a One Person Company?", "Yes. Since 1 April 2021 an Indian citizen, whether resident in India or not, can incorporate an OPC. OCI cardholders and foreign citizens cannot; they can use a private limited company instead."),
          ("Can an NRI start a business in India while working in the USA?", "Owning one is generally fine, but an active role can conflict with some US visas, so take US immigration advice. A US tax resident also reports the Indian entity to the IRS (Form 5471, 8865 or 8858) and files FBAR for Indian accounts."),
          ("Which structure is best for an NRI who wants profits abroad?", "Usually a private limited company (or an LLP in sectors open to automatic FDI) funded with repatriable investment, so dividends and exit proceeds can be remitted. It needs one director resident in India for 182 days in the financial year."),
          ("Can BQP set up and run the business for me?", "Yes. " + CONTACT)],
    related=[("which-is-better-llp-vs-private-limited-india.html", "LLP vs private limited"), ("nri-returning-startup-moving-to-india.html", "Returning NRIs starting up"),
             ("loan-from-nri-director-shareholder-to-indian-company-ecb-2026-rules.html", "Loans from NRI directors")],
    cta_h="Starting a business in India from abroad?", cta_b=CONTACT,
    keywords="can NRI start business in India, can NRI open sole proprietorship in India, NRI partnership firm India, can NRI open one person company, NRI LLP India, NRI private limited company India, NRI business while working in USA, Schedule IV non repatriation NRI",
    desc="Can an NRI start a business in India (2026)? Sole proprietorship and partnership on a non-repatriation basis (Schedule IV), OPC for Indian citizens abroad since 2021, LLP (120-day resident designated partner), private limited company (182-day resident director, 100% automatic FDI), tax, US reporting and UAE deemed residence.",
    howto={"name": "How an NRI starts a business in India", "description": "Steps from abroad.", "steps": [
        {"name": "Decide where profits will go", "text": "Non-repatriable capital suits a proprietorship or firm; repatriable investment points to a company or LLP."},
        {"name": "Pick the structure", "text": "Check the sector is permitted and who will be the resident director or designated partner."},
        {"name": "Get DIN and digital signature", "text": "Obtain a Class 3 DSC; notarise and apostille documents signed abroad."},
        {"name": "Register and open accounts", "text": "Incorporate or register, obtain PAN, GST and other licences, and open the business bank account."},
        {"name": "File and report", "text": "FC-GPR for repatriable share capital, annual ROC and tax filings in India, and home-country reporting such as Form 5471 and FBAR."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch DB complete")
