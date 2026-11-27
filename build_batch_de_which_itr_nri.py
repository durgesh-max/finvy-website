# -*- coding: utf-8 -*-
"""Batch DE (19 Nov 2026): which ITR should an NRI file, does an NRI need to file, refunds and deductions (80C).
Demand: autocomplete sweep 19 Nov 2026 (ac12), all 7 markets: "which itr to file for nri", "which itr for nri
salaried person", "which itr form for nri with no income", "does nri need to file itr", "can nri get tax refund in
india", "can nri claim 80c deduction", "is dividend income taxable for nri". Site had commercial NRI ITR pages only.
Facts: FY 2025-26 (AY 2026-27) returns under the Income-tax Act, 1961; ITR-1 and ITR-4 are only for resident
individuals, so NRIs file ITR-2 (no business income) or ITR-3 (business/profession); due date 31 July 2026 (non-audit),
belated/revised by 31 December 2026 with late fee up to INR 5,000; filing required if total income exceeds the basic
exemption (INR 4 lakh new regime, INR 2.5 lakh old regime) or to claim a refund / carry forward losses; section 87A
rebate is for resident individuals only; NRIs cannot set the basic exemption against special-rate capital gains
(111A/112/112A); 80C (old regime) available to NRIs for life insurance, existing PPF, ELSS, tuition fees, home-loan
principal; 80TTA on savings interest (NRO); 80TTB for resident seniors only; Schedule FA only for resident and
ordinarily resident; refund to a pre-validated Indian account (NRO/NRE) or a foreign account where no Indian account;
dividend: TDS 20% plus surcharge and cess or treaty rate. Sources: CalcGuru, ClearTax, Patron Accounting, 1 Finance
(checked 19 Nov 2026), Income-tax Act provisions."""
from urllib.parse import quote
from build_lib import page, write_page

UPDATED = "Last updated: 19 November 2026."


def wa(t):
    return "https://wa.me/917801887130?text=" + quote(t)


def ul(*x):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in x) + "</ul>"


def table(head, rows):
    return ("<table><thead><tr>" + "".join(f"<th>{h}</th>" for h in head) + "</tr></thead><tbody>"
            + "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows) + "</tbody></table>")


CONTACT = ("Email info@bharatquantumprospera.com or WhatsApp +91 78018 87130 with your country of residence, days in India, and your Indian income (rent, interest, capital gains, dividends) with the TDS shown in Form 168 (old 26AS) / AIS. "
           "We reply with the right form, the refund position and the scope of work.")
SLUG = "which-itr-to-file-for-nri-ay-2026-27-itr-2-itr-3-refund-80c-deductions"
BOX = (f'<div style="border:1px solid var(--line);border-left:4px solid #C2312A;border-radius:10px;padding:16px 18px;margin:18px 0;background:var(--bg-soft)">'
       f'<p style="margin:0 0 8px;font-weight:600">Missed 31 July? You still have until 31 December 2026.</p>'
       f'<p style="margin:0">Most NRIs overpay through TDS on NRO interest, rent and property sales. A belated FY 2025-26 return claims it back, with a late fee of up to INR 5,000. We prepare ITR-2 or ITR-3, apply your treaty rate and track the refund. '
       f'<a href="{wa("Hi Durgesh, I am an NRI and need to file my Indian ITR for FY 2025-26. Which form and can I get a refund?")}" target="_blank" rel="noopener"><strong>WhatsApp CA Durgesh Chavda</strong></a>.</p></div>')

PAGES = [dict(
    slug=SLUG,
    title="Do NRIs Need to File ITR? NRI ITR Filing (AY 2026-27): Which ITR to File (ITR-2 or ITR-3, Not ITR-1), Last Date, Who Must File, Refunds and 80C",
    em="for NRIs in the UAE, US, UK, Singapore, Canada and Australia.",
    kicker="/ NRIs &middot; Income-tax return &middot; Updated 2026-11-19",
    lead=("An NRI files <strong>ITR-2</strong> for salary, rent, interest, dividends and capital gains from India, and <strong>ITR-3</strong> if there is business or professional income. <strong>ITR-1 (Sahaj) and ITR-4 (Sugam) are only for residents</strong>, so an NRI cannot use them. "
          "You must file if your Indian income is above the basic exemption limit (<strong>INR 4 lakh</strong> under the new regime, INR 2.5 lakh under the old regime for FY 2025-26). You should also file to <strong>claim a refund of excess TDS</strong> or carry forward losses. NRE and FCNR interest is exempt and does not count. "
          "The FY 2025-26 due date was <strong>31 July 2026</strong>; a belated return can still be filed until <strong>31 December 2026</strong> with a late fee of up to INR 5,000. "
          "Under the old regime NRIs can claim <strong>section 80C</strong> (life insurance, an existing PPF, ELSS, children's tuition fees, home-loan principal). They <strong>cannot get the section 87A rebate</strong>, which is for residents only."),
    sections=[
        ("/ Which form", "Pick by the type of income.",
         table(["Your Indian income", "Form", "Notes"], [
             ["Salary for work in India, rent, interest, dividends, capital gains (shares, mutual funds, property)", "ITR-2", "Most NRIs; includes the residential status schedule and DTAA relief"],
             ["Any business or professional income (consulting, freelancing, a proprietorship, partner's remuneration)", "ITR-3", "Books of account and tax audit rules can apply"],
             ["Only NRE / FCNR interest (exempt)", "No return needed", "File anyway if TDS was wrongly deducted and you want it back"],
             ["Small income below the exemption limit but TDS deducted", "ITR-2 (or ITR-3)", "File to claim the refund"],
             ["ITR-1 or ITR-4", "Not allowed", "Only for resident individuals"]])
         + BOX),
        ("/ Rules that differ for NRIs", "Where NRIs overpay or get it wrong.",
         ul("<strong>No 87A rebate:</strong> the rebate that makes income up to INR 12 lakh tax-free under the new regime is only for residents.",
            "<strong>Special-rate gains:</strong> NRIs cannot use the unused basic exemption against short-term equity gains (20%) or long-term gains (12.5%); residents can.",
            "<strong>Deductions (old regime only):</strong> 80C for life insurance, an existing PPF account, ELSS, tuition fees and home-loan principal; 80D health insurance; 80TTA up to INR 10,000 on savings interest (NRO). Not available: 80TTB (resident senior citizens), new PPF or NSC investments, and the Senior Citizens Savings Scheme.",
            "<strong>Dividends:</strong> taxable for NRIs; the company deducts TDS at 20% plus surcharge and cess, or the lower treaty rate if you give a TRC and Form 10F.",
            "<strong>Treaty relief:</strong> claim treaty rates on interest, dividends and royalties with a tax residency certificate and Form 10F (Form 41 under the new rules). See <a href=\"india-uae-dtaa-for-nris-dubai-nro-interest-mutual-funds-property-trc-2026.html\">India-UAE treaty</a>.",
            "<strong>Schedule FA:</strong> foreign assets are reported only by resident and ordinarily resident individuals; NRIs and RNORs do not fill it.")),
        ("/ Refunds and filing", "Getting your money back.",
         ul("<strong>Check Form 26AS and the AIS</strong> for TDS on NRO interest, rent (31.2% or more) and property sales, and match it to your income.",
            "<strong>Refund account:</strong> pre-validate an Indian bank account (usually your NRO account) on the e-filing portal; an NRI with no Indian account can give a foreign bank account for the refund.",
            "<strong>Verify within 30 days</strong> of filing (net banking, Aadhaar OTP if linked, or digital signature); an unverified return is treated as not filed.",
            "<strong>From FY 2026-27</strong> returns move to the Income-tax Act, 2025 and the new ITR forms; the same principles apply. See <a href=\"ay-2026-27-itr-forms-new-disclosures-india.html\">ITR forms and new disclosures</a>.")
         + '<p>Related: <a href="nri-missed-itr-deadline-what-to-do-india.html">NRI missed the ITR deadline</a> &middot; <a href="belated-itr-31-december-2026-section-139-4-india.html">belated return by 31 December 2026</a> &middot; <a href="ca-for-nri-tax-return-filing.html">NRI tax return filing</a> &middot; <a href="is-nre-fd-interest-taxable-in-uk-usa-canada-australia-singapore-uae-2026.html">is NRE interest taxed abroad</a> &middot; <a href="residential-status-calculator-india-nri-rnor-section-6.html">residential status calculator</a>.</p>'
         + f'<p><strong>Sources:</strong> Income-tax Act, 1961 (sections 80C, 80D, 80TTA, 80TTB, 87A, 111A, 112A, 139) for FY 2025-26; ITR-2 and ITR-3 instructions for AY 2026-27; Income-tax Act, 2025 from FY 2026-27. Secondary guides checked 19 November 2026: ClearTax, CalcGuru, Patron Accounting, 1 Finance. <em>{UPDATED}</em> General information; your treaty and residential status can change the answer.</p>'),
    ],
    faqs=[("Which ITR should an NRI file?", "ITR-2 for salary, rent, interest, dividends and capital gains from India; ITR-3 if there is any business or professional income. ITR-1 and ITR-4 are only for residents."),
        ("What is the last date for NRI ITR filing for AY 2026-27?", "For NRIs filing ITR-2 (salary, rent, interest, capital gains), the due date was 31 July 2026 and it was not extended. Non-audit business or professional income (ITR-3) had a later date, and audit cases were extended to 21 November 2026. If you missed your date, a belated return can still be filed by 31 December 2026 with a late fee, and refunds can still be claimed. A return already filed can be revised until 31 March 2027 (free until 31 December 2026, then with a fee)."),
        ("Can an NRI file ITR-1?", "No. ITR-1 (Sahaj) and ITR-4 (Sugam) are only for resident individuals, so NRIs use ITR-2, or ITR-3 if they have business or professional income in India."),
          ("Does an NRI need to file an ITR in India?", "Yes if taxable Indian income (excluding exempt NRE / FCNR interest) is above the basic exemption limit - INR 4 lakh under the new regime or INR 2.5 lakh under the old, with no rebate for non-residents. File even below that to claim back excess TDS - common after a property sale, where the buyer deducts tax on the full price, or on NRO interest and rent - or to carry forward capital losses. With only NRE or FCNR interest, no return is needed."),
        ("Can an NRI file an income tax return without an Aadhaar card?", "Yes. Non-residents are exempt from the requirement to quote Aadhaar and from PAN-Aadhaar linking, so an NRI or OCI without Aadhaar files with PAN alone and leaves the Aadhaar field blank. What matters is that the PAN is operative and that the department's records show non-resident status - if the PAN shows inoperative because the records still treat you as resident, update the residential status first. Without Aadhaar, the return cannot be e-verified by Aadhaar OTP, but it can be verified through net banking or a pre-validated Indian bank or demat account, a digital signature, or by signing the ITR-V and posting it to CPC Bengaluru within 30 days of filing. A refund still needs a pre-validated Indian bank account, usually the NRO account. An NRI who holds an Aadhaar can quote it and use OTP verification. WhatsApp +91 78018 87130 with your PAN status, residential status and income details, or book a call."),
        ("How can an OCI cardholder file an income tax return in India?", "An OCI card does not change how you are taxed: like any individual, you are taxed on your residential status for the year, and most OCI holders living abroad are non-residents. File ITR-2 (or ITR-3 with business income) on the income tax e-filing portal with your PAN, reporting only Indian income. Verify the return with net banking, a digital signature, an EVC through a pre-validated bank or demat account, Aadhaar OTP if you have Aadhaar, or by signing the ITR-V and posting it to CPC Bengaluru within 30 days. There is no 87A rebate for non-residents, and refunds go to a pre-validated Indian account (a non-resident with no Indian account can give one foreign account)."),
        ("What should an OCI or NRI send to get an Indian return filed?", "WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with your PAN, your days in India for the year, Form 168 (old 26AS) and AIS, TDS certificates, NRO / NRE statements, any property sale or rent papers, and the bank account for the refund. We work out your residential status, pick the right ITR and file it for you to verify."),
          ("Which ITR for an NRI with no income?", "None is required, but if TDS was deducted (for example on NRO interest) file ITR-2 to claim the refund."),
          ("Can an NRI claim 80C deduction?", "Yes, under the old regime: life insurance, an existing PPF account, ELSS, children's tuition fees and home-loan principal. NRIs cannot open new PPF accounts, buy new NSCs or invest in the Senior Citizens Savings Scheme."),
          ("Can an NRI get a tax refund in India?", "Yes. File ITR-2 or ITR-3 claiming the excess TDS; the refund goes to a pre-validated Indian account (usually your NRO account; confirm with your bank before using an NRE account), or to a foreign account if you have no Indian account. For FY 2025-26 a belated return is possible until 31 December 2026."),
          ("Can BQP file my NRI return?", "Yes. " + CONTACT)],
    related=[("nri-missed-itr-deadline-what-to-do-india.html", "NRI missed the ITR deadline"), ("ca-for-nri-tax-return-filing.html", "NRI tax return filing"),
             ("belated-itr-31-december-2026-section-139-4-india.html", "Belated return by 31 December 2026")],
    cta_h="Filing your Indian return from abroad?", cta_b=CONTACT,
    keywords="which ITR to file for NRI, which ITR for NRI AY 2026-27, does NRI need to file ITR, NRI ITR with no income, can NRI claim 80C, NRI tax refund India, is dividend taxable for NRI, ITR-2 for NRI",
    desc="Which ITR should an NRI file (AY 2026-27)? ITR-2 (or ITR-3 with business income); ITR-1/ITR-4 only for residents; who must file; 31 July and 31 December 2026 dates; no 87A rebate; 80C and other deductions; refunds to a pre-validated Indian (usually NRO) account or a foreign account; dividends and treaty relief.",
    howto={"name": "How an NRI files an Indian income-tax return", "description": "Steps for FY 2025-26.", "steps": [
        {"name": "Confirm residential status", "text": "Count days in India to confirm non-resident (or RNOR) status."},
        {"name": "Collect income and TDS", "text": "Download Form 26AS and AIS; gather interest certificates, rent, capital gains statements."},
        {"name": "Choose the form and regime", "text": "ITR-2 or ITR-3; compare old regime (80C, 80D) with the new regime."},
        {"name": "Claim treaty relief and refund", "text": "Apply treaty rates with TRC and Form 10F; pre-validate a refund bank account."},
        {"name": "File and verify", "text": "File by 31 December 2026 (belated for FY 2025-26) and e-verify within 30 days."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch DE complete")
