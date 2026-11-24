# -*- coding: utf-8 -*-
"""Batch FV (23 Nov 2026): NRI senior citizens and Indian tax - which senior-citizen benefits are for residents only,
what NRIs still get, and what changes when a senior NRI retires to India. Call-first page for retired and retiring NRIs
(Gulf, US, UK, Canada, Australia, Singapore) and their children.
Demand: sweep ac48 (23 Nov 2026), all 7 markets: "does nri senior citizen get tax exemption", "tax for senior citizens in
india", "what is the tax exemption limit for senior citizens", "nri retirement in india". No NRI senior page existed.
Facts (checked 23 Nov 2026):
- Old regime basic exemption: INR 2.5 lakh; resident senior (60-79) INR 3 lakh; resident super senior (80+) INR 5 lakh;
  non-residents INR 2.5 lakh at any age (Income Tax Department chart, benefits allowed to a senior citizen).
- New regime: INR 4 lakh basic exemption for all individuals; rebate (zero tax up to INR 12 lakh) for residents only.
- Interest deduction for senior citizens (80TTB, INR 50,000, old regime): resident senior citizens only; carried into the
  Income-tax Act, 2025 (commentary maps it to section 153), substance unchanged.
- Advance tax exemption (section 207 of the 1961 Act): resident senior citizens with no business or professional income
  only; NRIs do not get it (Income Tax Department FAQ).
- Section 194P (no return for 75+ with only pension and interest from the same bank): residents only.
- Health insurance deduction (80D): the higher INR 50,000 limit applies where the insured is a senior citizen, defined
  as an individual resident in India aged 60+ (via 80DDB); NRIs can claim for resident parents; medical expenditure for
  an uninsured senior is for resident seniors only (Niva Bupa NRI guide; Income Tax Department section 80D pages).
- Form 15H (no TDS declaration for seniors) is for residents only; NRO interest TDS 30% plus surcharge and cess or the
  treaty rate with a TRC (site page).
- Standard deduction on pension from a former employer (salary head): INR 75,000 new regime, INR 50,000 old regime."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 23 November 2026."
SLUG = "nri-senior-citizen-tax-india-2026-exemption-limit-80ttb-advance-tax-15h-pension-retire-to-india"

C = contact("your age, country of residence, your Indian income (interest, rent, pension, capital gains), your foreign pension, and when you plan to move back")
L = lambda h, t: f'<a href="{h}">{t}</a>'
PAGES = [dict(
    slug=SLUG,
    title="NRI Senior Citizen Tax in India (2026): Which Senior Benefits NRIs Do Not Get, and What Changes When You Retire to India",
    em="age helps only residents.",
    kicker="/ NRIs &middot; Senior citizens and retirement &middot; Updated 2026-11-23",
    lead=("<strong>An NRI aged 60 or 80 does not get India&rsquo;s senior-citizen tax benefits: almost all of them are for residents only.</strong> "
          "A non-resident&rsquo;s basic exemption is <strong>INR 2.5 lakh at any age</strong> under the old regime (residents get INR 3 lakh at 60 and INR 5 lakh at 80), and INR 4 lakh under the new regime, but without the rebate that makes income up to INR 12 lakh tax-free for residents. "
          "NRIs also lose the <strong>INR 50,000 interest deduction</strong> for seniors, the <strong>advance tax exemption</strong>, <strong>Form 15H</strong> and the no-return rule for those over 75. "
          "What NRIs keep: treaty rates on NRO interest, the standard deduction on an Indian pension, and the health insurance deduction for resident parents. "
          "The picture flips when you <strong>retire to India</strong>: once resident, the senior benefits apply, and a foreign pension can be shielded for a few years as RNOR."),
    sections=[
        ("/ Quick answers", "What senior NRIs and their children ask.",
         ul("<strong>Does an NRI senior citizen get a higher tax exemption?</strong> No. The higher limits of INR 3 lakh (60 to 79) and INR 5 lakh (80+) under the old regime are for residents only. A non-resident gets INR 2.5 lakh at any age.",
            "<strong>Can an NRI senior citizen claim the INR 50,000 interest deduction?</strong> No. It is for resident senior citizens under the old regime only. An NRI can claim up to INR 10,000 on savings account interest under the old regime.",
            "<strong>Does an NRI senior citizen pay advance tax?</strong> Yes, if the tax due after TDS is INR 10,000 or more. The advance tax exemption is for resident seniors without business income.",
            "<strong>Can an NRI senior submit Form 15H?</strong> No. Form 15H is for residents. NRO interest has TDS at 30% plus surcharge and cess, or a lower treaty rate with a tax residency certificate.",
            "<strong>Is income up to INR 12 lakh tax-free for an NRI?</strong> No. The rebate that makes it tax-free under the new regime is for residents only.")),
        ("/ Resident vs NRI senior", "Benefit by benefit.",
         table(["Benefit", "Resident senior citizen", "NRI aged 60+"], [
             ["Basic exemption, old regime", "INR 3 lakh (60 to 79); INR 5 lakh (80+)", "INR 2.5 lakh"],
             ["Basic exemption, new regime", "INR 4 lakh, plus rebate: no tax up to INR 12 lakh", "INR 4 lakh, no rebate"],
             ["Interest deduction (80TTB in the old Act)", "Up to INR 50,000 on deposit interest (old regime)", "Not available; INR 10,000 on savings interest only (old regime)"],
             ["Advance tax", "Exempt if no business or professional income", "Payable if tax due after TDS is INR 10,000 or more"],
             ["No-return rule at 75+ (pension and interest from one bank)", "Available", "Not available"],
             ["Form 15H (no TDS)", "Available", "Not available"],
             ["Health insurance deduction (80D)", "Up to INR 50,000 for own policy (old regime)", "INR 25,000 for own policy; up to INR 50,000 for resident senior parents"],
             ["Standard deduction on Indian pension", "INR 75,000 (new) / INR 50,000 (old)", "Same"],
             ["Treaty rate on interest", "Not relevant", "Yes, with a tax residency certificate and Form 10F (Form 41 from tax year 2026-27)"]])
         + '<p>The age and residence tests apply to the tax year (1 April to 31 March). Residence is decided by days in India each year; see ' + L("dubai-uae-nri-indian-income-above-15-lakh-deemed-resident-india-tax-2026.html", "deemed residence for Gulf NRIs") + ' for the INR 15 lakh rule.</p>'),
        ("/ What NRIs can still do", "Cutting tax on Indian income without the senior benefits.",
         ul("<strong>Claim the treaty rate</strong> on NRO interest and dividends: 10% to 15% in most treaties instead of 30% plus surcharge and cess. See the " + L("nri-nro-interest-tds-refund-calculator-treaty-rate-by-country-2026.html", "NRO TDS refund calculator") + ".",
            "<strong>Move savings to NRE or FCNR deposits</strong> if the money came from abroad: their interest is exempt for NRIs. See " + L("nre-nro-fcnr-account-tax-rules.html", "NRE, NRO and FCNR tax rules") + ".",
            "<strong>File a return to get excess TDS back:</strong> where total Indian income is low, TDS at 30% is often refundable in full or in part.",
            "<strong>Compare regimes each year:</strong> an NRI with mostly interest and capital gains often pays less under the new regime; an NRI with home loan interest or health insurance may not.",
            "<strong>Keep the tax residency certificate current</strong>, since the treaty rate depends on it.")
         + call_box("tax for a senior NRI or a retiring parent", ["Your residence status this year and next",
                                                                   "NRO interest, TDS and refunds",
                                                                   "Old vs new regime for your income",
                                                                   "Foreign pension and Social Security after moving back",
                                                                   "Timing the move to India"],
                    "your age, country, Indian income, foreign pension and planned move date.")),
        ("/ Retiring to India", "What changes when a senior NRI moves back.",
         ul("<strong>Resident senior benefits start</strong> in the first year you are resident: higher exemption (old regime), the INR 50,000 interest deduction, no advance tax without business income, Form 15H.",
            "<strong>RNOR years:</strong> a returning NRI is usually &lsquo;resident but not ordinarily resident&rsquo; for up to two or three years. Foreign pension and foreign interest received abroad are not taxed in India in those years. See " + L("best-ca-nri-returning-india-rnor-planning.html", "RNOR planning") + ".",
            "<strong>Foreign pensions after RNOR:</strong> taxable in India once you are ordinarily resident, with treaty relief. US Social Security is taxable only in the US under the India-US treaty; see " + L("us-social-security-taxable-in-india-dtaa-article-20-returning-nri.html", "US Social Security in India") + ". UK and other pensions depend on the treaty and the type of pension.",
            "<strong>Foreign tax credit</strong> needs Form 67 (Form 44 from tax year 2026-27) filed with the return; see " + L("form-67-foreign-tax-credit-india-2026.html", "foreign tax credit") + ".",
            "<strong>Report foreign assets</strong> in Schedule FA once ordinarily resident: pensions, accounts, property abroad.",
            "<strong>Convert accounts:</strong> NRE and NRO accounts must be redesignated as resident accounts; FCNR deposits can run to maturity, and an RFC account can hold foreign currency.")
         + sources("Income Tax Department, &lsquo;Benefits allowed to a senior citizen or super senior citizen&rsquo; and FAQ on exemption from advance tax for resident senior citizens; Income-tax Act, 1961, sections 80D, 80DDB, 80TTA, 80TTB, 87A, 194P, 197A and 207, carried into the Income-tax Act, 2025 from tax year 2026-27 (section numbers changed, substance largely unchanged per published concordances); Finance Act, 2025 (new regime slabs and rebate); Niva Bupa guide to health insurance deductions for NRIs; India-US tax treaty, Article 20. Checked 23 November 2026.")),
    ],
    faqs=[("Does an NRI senior citizen get tax exemption in India?", "No higher exemption. The INR 3 lakh (60 to 79) and INR 5 lakh (80+) limits under the old regime are for residents only. A non-resident gets INR 2.5 lakh under the old regime and INR 4 lakh under the new regime, at any age, without the rebate."),
          ("What is the tax exemption limit for senior citizens in India in 2026?", "For resident senior citizens: INR 3 lakh (60 to 79) or INR 5 lakh (80+) under the old regime; under the new regime, INR 4 lakh basic exemption for everyone, and a resident pays no tax up to INR 12 lakh because of the rebate."),
          ("Can an NRI senior citizen claim section 80TTB?", "No. The INR 50,000 interest deduction is for resident senior citizens under the old regime. An NRI can claim up to INR 10,000 on savings account interest under the old regime."),
          ("Do NRI senior citizens have to pay advance tax?", "Yes, if the tax due after TDS is INR 10,000 or more. The exemption from advance tax is only for resident senior citizens without business or professional income."),
          ("Can an NRI claim health insurance for parents in India?", "Yes, under the old regime: up to INR 50,000 if the parents are resident senior citizens, and INR 25,000 otherwise. The NRI's own policy is limited to INR 25,000."),
          ("Is foreign pension taxable when an NRI retires to India?", "Not while you are RNOR, usually for the first two or three years, if received abroad. After that it is taxable in India with treaty relief; US Social Security is taxable only in the US under the treaty."),
        ("How can a pensioner living abroad submit a life certificate online?", "Through Jeevan Pramaan: with an Aadhaar number, install the AadhaarFaceRD and Jeevan Pramaan Face apps on a smartphone and complete face authentication to generate a digital life certificate, which reaches the pension disbursing bank or office directly. November is the usual submission window for central government pensioners. Pensioners abroad without Aadhaar, or whose authentication fails, should ask their pension disbursing bank or the Indian mission which paper route it accepts, and a 2026 provision allows an authorised agent to help in some cases."),
        ("Is Indian pension taxable for an NRI?", "Under Indian law, yes: a pension paid by an Indian employer or the government is Indian-source income, usually with TDS by the payer. A tax treaty can change that: government pensions are usually taxable only in India, while private pensions are often taxable only in your country of residence, so check the treaty before accepting the TDS and claim a refund or foreign tax credit as needed."),
          ("Can BQP handle tax for a senior NRI or a retiring parent?", "Yes. " + C)],
    related=[("best-ca-nri-returning-india-rnor-planning.html", "RNOR planning for returning NRIs"),
             ("nri-nro-interest-tds-refund-calculator-treaty-rate-by-country-2026.html", "NRO TDS refund calculator"),
             ("us-social-security-taxable-in-india-dtaa-article-20-returning-nri.html", "US Social Security in India"),
             ("nre-nro-fcnr-account-tax-rules.html", "NRE, NRO and FCNR tax rules"),
             ("returning-to-india-from-uk-isa-uk-pension-property-split-year-india-tax-2026.html", "Returning from the UK")],
    cta_h="A senior NRI in the family?", cta_b=C,
    keywords="NRI senior citizen tax India, does NRI senior citizen get tax exemption, tax exemption limit for senior citizens India 2026, 80TTB NRI, advance tax NRI senior citizen, Form 15H NRI, NRI retirement in India tax, foreign pension tax India RNOR, 80D NRI parents",
    desc="NRI senior citizens get almost none of India's senior tax benefits: INR 2.5 lakh exemption at any age (old regime), no 80TTB, no advance tax exemption, no Form 15H, no rebate. What NRIs can still do, and what changes on retiring to India (RNOR, foreign pension, Form 67).",
    howto={"name": "How a senior NRI reduces Indian tax on interest", "description": "Steps without the resident senior benefits.", "steps": [
        {"name": "Get a tax residency certificate", "text": "From your country of residence, plus Form 10F (Form 41 from tax year 2026-27)."},
        {"name": "Ask the bank for the treaty rate", "text": "On NRO interest, instead of 30% plus surcharge and cess."},
        {"name": "Use NRE or FCNR deposits", "text": "For money from abroad; the interest is exempt for NRIs."},
        {"name": "Compare old and new regimes", "text": "For your mix of interest, rent and capital gains."},
        {"name": "File a return", "text": "To claim back excess TDS."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch FV complete")
