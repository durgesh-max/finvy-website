# -*- coding: utf-8 -*-
"""Batch FR (23 Nov 2026): NPS for NRIs and OCI cardholders - who can open it, funding from NRE / NRO, tax deduction,
exit rules after the December 2025 PFRDA amendment (80% lump sum for non-government subscribers, only 60% tax-free),
citizenship change, home-country tax. Call-first page.
Demand: sweeps 22-23 Nov 2026 (ac44, ac45), all 7 markets: "nri nps account opening", "nri nps account".
Facts (checked 23 Nov 2026):
- NRIs and OCI cardholders can join NPS (All Citizen Model); Tier I only; enrolment needs an NRE or NRO account; if an
  NRI gives up Indian citizenship without an OCI card the account is closed (Business Standard Dec 2025, PFRDA KYC
  amendment, Outlook Money, Axis Bank, DFS All Citizen Model page). Joining age: 18 to 85 under the All Citizen Model per
  the DFS page; some providers still show 70.
- FEMA: NRO account expressly allowed as a payment source for NPS by NRIs and OCIs (June 2026 amendment to the Mode of
  Payment and Reporting Regulations; site page). Contributions from NRE are repatriable.
- PFRDA (Exits and Withdrawals) amendment, December 2025: non-government subscribers can take up to 80% as lump sum at
  normal exit, at least 20% in annuity; government subscribers stay 60:40; small corpus rules (Business Standard,
  PensionBazaar, others).
- Tax: section 10(12A) of the 1961 Act exempts 60% of the corpus; commentary (Business Standard Dec 2025, July 2026
  articles) says the portion above 60% is taxable at slab rates until the law is amended; annuity income is taxable;
  the extra deduction of INR 50,000 for own contributions is available only under the old regime (site eligibility page)."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 23 November 2026."
SLUG = "nps-for-nri-oci-account-opening-nre-nro-tax-deduction-80-percent-lump-sum-exit-2026"

C = contact("where you live, whether you are an NRI or OCI cardholder, your age, whether you already have an NPS account, and whether you have taxable income in India")
L = lambda h, t: f'<a href="{h}">{t}</a>'
PAGES = [dict(
    slug=SLUG,
    title="NPS for NRIs and OCI Cardholders (2026): Opening an Account From Abroad, NRE or NRO Funding, Tax, and the New 80% Lump Sum at Exit",
    em="useful only if you have Indian income to save tax on, or plan to retire in India.",
    kicker="/ NRIs &middot; Retirement &middot; Tax &middot; Updated 2026-11-23",
    lead=("<strong>NRIs and OCI cardholders can open a National Pension System (NPS) Tier I account from abroad, funded from an NRE or NRO account.</strong> "
          "Contributions from an NRE account can later be sent back abroad. "
          "Since <strong>December 2025</strong>, a non-government subscriber can take up to <strong>80% of the corpus as a lump sum</strong> at exit, with at least 20% buying an annuity. "
          "But Indian tax law still exempts only <strong>60%</strong>, so the extra 20% is taxable at slab rates until the law changes. The annuity is taxed as income. "
          "The extra INR 50,000 deduction for your own contributions works only under the old tax regime and only if you have taxable income in India. "
          "Your country of residence may tax the account too. NPS suits an NRI with Indian income or plans to retire in India; for others, check the home-country tax first."),
    sections=[
        ("/ The rules for NRIs", "Who can open it and how.",
         table(["Point", "Position in 2026"], [
             ["Who can join", "NRIs and OCI cardholders, Tier I only (Tier II is not available to them)"],
             ["Age at joining", "18 to 85 under the All Citizen Model (some providers still show 70; check at enrolment)"],
             ["Funding", "From an NRE account (repatriable) or NRO account (non-repatriable); the June 2026 FEMA amendment names NRO expressly"],
             ["KYC", "Can be done from abroad; PFRDA revised NRI and OCI KYC rules in December 2025"],
             ["Giving up Indian citizenship", "Without an OCI card, the account is closed and the balance paid to the NRO account"],
             ["Normal exit, non-government subscriber", "Up to 80% lump sum, at least 20% annuity (since December 2025)"],
             ["Normal exit, government subscriber", "60% lump sum, 40% annuity"]])
         + call_box("NPS while living abroad: is it worth it for you?", ["Whether you can use the deduction (old regime, Indian income)",
                                                                          "NRE or NRO funding and taking the money abroad later",
                                                                          "Tax on the lump sum, the extra 20% and the annuity",
                                                                          "How your country of residence treats NPS",
                                                                          "What happens to the account if you change citizenship or return"],
                    "where you live, your status, age, existing NPS account and Indian income.")),
        ("/ Tax", "In India, and at home.",
         table(["Stage", "India", "Country of residence"], [
             ["Contribution", "Extra deduction of INR 50,000 for own contributions under the old regime only; no benefit without Indian taxable income", "Usually no deduction for a foreign pension"],
             ["Growth", "Not taxed while invested", "May be taxed yearly or need reporting, depending on the country (US persons in particular)"],
             ["Lump sum at exit", "60% of the corpus exempt; the part above 60% is taxable at slab rates under current law", "Often taxable"],
             ["Annuity", "Taxable as income in India", "Taxable, with treaty credit"]])
         + ul("<strong>Before you choose 80%:</strong> taking the full 80% adds the extra 20% to your Indian income in that year. Spreading the exit or taking less can cost less tax.",
              "<strong>Old or new regime:</strong> the deduction for your own contributions is old-regime only; see " + L("is-nri-eligible-87a-rebate-indexation-nps-ppf-scss-sukanya-post-office-schemes-2026.html", "which benefits NRIs can use") + ".",
              "<strong>US residents:</strong> NPS is a foreign pension arrangement for US tax and may need annual reporting; take advice before contributing.",
              "<strong>UK residents:</strong> NPS is not a UK-registered pension, so UK relief does not apply; growth and withdrawals need checking under UK rules.",
              "<strong>Returning to India:</strong> the account continues; your status changes on record with the bank and NPS. See " + L("nri-returning-india-tax-rnor-transition.html", "returning to India") + ".")
         + '<p>Related: ' + L("nre-nro-fcnr-account-tax-rules.html", "NRE, NRO and FCNR rules") + ' &middot; ' + L("nro-to-nre-transfer-limit-tax-form-145-146-15ca-15cb-documents-usd-1-million-2026.html", "NRO to NRE transfer") + ' &middot; ' + L("how-to-invest-in-indian-stock-market-from-usa-uk-uae-nri-oci-foreigner-demat-pis-tax-2026.html", "investing in Indian shares from abroad") + ' &middot; ' + L("nri-pensioner-life-certificate-from-abroad-30-november-2026-indian-pension-tax-dtaa.html", "Indian pensions for NRIs") + '.</p>'
         + sources("PFRDA (Exits and Withdrawals under the National Pension System) (Amendment) Regulations, December 2025, as reported by Business Standard and others; PFRDA KYC amendments for NRIs and OCIs (December 2025, November 2026); Department of Financial Services, NPS All Citizen Model; FEMA (Mode of Payment and Reporting of Non-Debt Instruments) amendment of June 2026; Income-tax Act provisions on NPS deductions and the 60% exemption (section 10(12A) of the 1961 Act), with 2025-26 commentary that the part above 60% remains taxable. Checked 23 November 2026. Confirm the age limit and any later tax amendment before acting.")),
    ],
    faqs=[("Can an NRI open an NPS account?", "Yes. NRIs can open an NPS Tier I account, funded from an NRE or NRO account, and complete KYC from abroad. Tier II is not available to NRIs."),
          ("Can OCI cardholders invest in NPS?", "Yes, under current PFRDA rules OCI cardholders can join NPS Tier I, funded from an NRE or NRO account."),
        ("Is there a government pension scheme in India for NRIs?", "Yes: the National Pension System (NPS), regulated by the Pension Fund Regulatory and Development Authority (PFRDA), is open to NRIs and OCI cardholders joining between 18 and 85 (some providers still show 70). Atal Pension Yojana is aimed at Indian citizens in the unorganised sector and is not a practical route for NRIs, so NPS is the scheme to use. NRIs cannot open new accounts in PPF or the Senior Citizens Savings Scheme."),
        ("Is NPS for NRIs safe and who manages it?", "NPS money is invested by PFRDA-registered pension fund managers in equity, corporate bonds and government securities within PFRDA limits, with a central record-keeping agency holding your account. Returns are market-linked, not guaranteed."),
          ("How much can I withdraw from NPS at 60 now?", "A non-government subscriber can take up to 80% of the corpus as a lump sum, with at least 20% used to buy an annuity, under PFRDA's December 2025 amendment. Government subscribers remain at 60:40."),
          ("Is the NPS lump sum tax-free?", "Only 60% of the corpus is exempt under current Indian tax law. Commentary indicates the extra 20% now allowed is taxable at slab rates until the law is amended. The annuity is taxed as income."),
          ("Can an NRI claim tax deduction on NPS?", "Yes, if the NRI has taxable income in India and uses the old regime, including the extra INR 50,000 deduction for own contributions. Under the new regime that deduction is not available."),
          ("What happens to NPS if an NRI becomes a foreign citizen?", "If the person gives up Indian citizenship and does not hold an OCI card, the account is closed and the balance paid to the NRO account."),
          ("Can BQP advise on NPS while I live abroad?", "Yes, on tax and FEMA, not on product choice. " + C)],
    related=[("is-nri-eligible-87a-rebate-indexation-nps-ppf-scss-sukanya-post-office-schemes-2026.html", "Which benefits NRIs can use"),
             ("nre-nro-fcnr-account-tax-rules.html", "NRE, NRO and FCNR rules"),
             ("nri-returning-india-tax-rnor-transition.html", "Returning to India")],
    cta_h="Thinking about NPS from abroad?", cta_b=C,
    keywords="NPS for NRI, NRI NPS account opening, can OCI invest in NPS, NPS NRE NRO, NPS 80% lump sum 2026, NPS withdrawal tax NRI, NPS tax deduction NRI 80CCD(1B), NPS exit rules December 2025, NPS citizenship change",
    desc="NPS for NRIs and OCIs (2026): Tier I only, funded from NRE (repatriable) or NRO; non-government subscribers can take up to 80% lump sum since December 2025 but only 60% is tax-free; INR 50,000 extra deduction only under the old regime; account closes if citizenship changes without OCI.",
    howto={"name": "How an NRI opens an NPS account", "description": "From abroad.", "steps": [
        {"name": "Check it suits you", "text": "Indian taxable income, old regime, plans to retire in India, home-country tax."},
        {"name": "Choose the funding account", "text": "NRE for repatriable, NRO for non-repatriable."},
        {"name": "Enrol and complete KYC", "text": "Online from abroad with passport, address proof and bank details."},
        {"name": "Contribute", "text": "Tier I only; keep records for the deduction."},
        {"name": "Plan the exit", "text": "Decide how much lump sum to take; only 60% is tax-free."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch FR complete")
