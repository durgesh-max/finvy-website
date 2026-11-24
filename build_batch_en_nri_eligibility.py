# -*- coding: utf-8 -*-
"""Batch EN (20 Nov 2026): Is an NRI eligible for ...? Tax reliefs (section 87A rebate, indexation option on property,
senior-citizen exemption limits, 80TTB) and schemes (NPS, PPF, SCSS, Sukanya Samriddhi, NSC, post office schemes).
Call-first page.
Demand: sweep 20 Nov 2026 (ac29), all 7 markets: "is nri eligible for 87a rebate", "can nri take indexation benefit",
"is nri eligible for nps", "is nri eligible for sukanya samriddhi", "can nri invest in post office schemes", "is nri
eligible for scss scheme", "can oci invest in post office". Low coverage on site.
Facts (checked 20 Nov 2026): section 87A rebate is for resident individuals only; the option to compute LTCG on land or
buildings acquired before 23 July 2024 at 20% with indexation (instead of 12.5% without) is for resident individuals and
HUFs only (Finance (No. 2) Act 2024) - NRIs pay 12.5% without indexation; higher basic exemption for senior citizens
(old regime) and section 80TTB are for residents only; NPS open to NRIs and OCI cardholders, contributions from NRE/NRO,
deductions under sections 80CCD(1)/(1B) in the old regime (secondary guides; Tier II reportedly not available to NRIs;
age band per PFRDA); post office small savings - no new accounts for NRIs: SCSS residents only, Sukanya Samriddhi
cannot be opened and the account is affected when the girl becomes NRI (scheme rules), PPF/NSC opened while resident
continue to maturity on a non-repatriation basis (PPF: no extension). Site PPF page consistent."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 20 November 2026."
SLUG = "is-nri-eligible-87a-rebate-indexation-nps-ppf-scss-sukanya-post-office-schemes-2026"

C = contact("your country of residence, which reliefs or schemes you are asking about, any Indian income or property sale this year, and accounts or schemes opened while you were resident")
PAGES = [dict(
    slug=SLUG,
    title="Is an NRI Eligible? (2026) Section 87A Rebate, Indexation on Property, Senior-Citizen Limits, NPS, PPF, SCSS, Sukanya Samriddhi and Post Office Schemes",
    em="the reliefs and schemes NRIs can and cannot use.",
    kicker="/ NRI &middot; Eligibility &middot; Tax reliefs &middot; Small savings &middot; Updated 2026-11-20",
    lead=("<strong>Several common reliefs are for residents only.</strong> An NRI <strong>does not get the section 87A rebate</strong>, so NRI income above the basic exemption limit is taxed even if a resident with the same income would pay nil. "
          "An NRI also <strong>cannot use the indexation option</strong> on land or buildings bought before 23 July 2024. Residents can choose 20% with indexation, but NRIs pay <strong>12.5% without indexation</strong>. The <strong>higher senior-citizen exemption limits</strong> and <strong>section 80TTB</strong> are also for residents only. "
          "For schemes, <strong>NPS is open to NRIs and OCI cardholders</strong>, funded from NRE or NRO, with deductions under the old regime. <strong>Post office small savings are not open to new NRI investors</strong>: no new PPF, NSC, SCSS or Sukanya Samriddhi accounts. "
          "PPF and NSC opened while you were resident <strong>continue to maturity</strong> on a non-repatriation basis. Sukanya Samriddhi has its own rule if the girl becomes an NRI."),
    sections=[
        ("/ Eligibility table", "Tax reliefs and schemes.",
         table(["Relief or scheme", "NRI eligible?", "Notes"], [
             ["Section 87A rebate", "No", "Resident individuals only"],
             ["Indexation option on property bought before 23 July 2024", "No", "Residents may choose 20% with indexation; NRIs pay 12.5% without"],
             ["Higher senior-citizen basic exemption (old regime)", "No", "Residents only"],
             ["Section 80TTB (interest deduction for seniors)", "No", "Residents only; NRIs may use 80TTA on savings interest in the old regime"],
             ["Section 80C, 80D (old regime)", "Yes, mostly", "Life insurance, ELSS, home-loan principal, tuition, health insurance; not new PPF/NSC"],
             ["NPS", "Yes (NRIs and OCI)", "Fund from NRE/NRO; 80CCD(1)/(1B) in the old regime; Tier II reportedly not available"],
             ["PPF", "No new account", "Existing account continues to maturity; no extension"],
             ["NSC, KVP, post office MIS/TD/RD", "No new investment", "Existing NSC held to maturity"],
             ["Senior Citizen Savings Scheme", "No", "Resident senior citizens only"],
             ["Sukanya Samriddhi", "No new account", "Scheme rules apply if the girl becomes an NRI; check with the post office or bank"]])
         + call_box("What I can still claim as an NRI", ["Your tax on Indian income without the 87A rebate",
                                                        "Property sale: 12.5% without indexation, section 54/54EC and TDS",
                                                        "Which deductions still work in the old regime",
                                                        "NPS, PPF and NSC you hold and what happens at maturity",
                                                        "Recovering excess TDS through the Indian return"],
                    "your Indian income, any property or investment sales, schemes you hold and your country of residence.")),
        ("/ Why it matters", "Common surprises for NRIs.",
         ul("<strong>Small incomes still taxed:</strong> without the 87A rebate, an NRI with Indian income above the basic exemption limit pays tax; see the <a href=\"nri-nro-interest-tds-refund-calculator-treaty-rate-by-country-2026.html\">NRO interest refund calculator</a>.",
            "<strong>Property sales:</strong> NRIs pay 12.5% without indexation on long-term gains, with TDS on the sale; reinvestment exemptions (sections 54, 54EC) still apply; see the <a href=\"nri-property-sale-tds-calculator-lower-deduction-certificate-savings.html\">NRI property TDS calculator</a>.",
            "<strong>Old vs new regime:</strong> most deductions need the old regime; compare before filing; see <a href=\"which-itr-to-file-for-nri-ay-2026-27-itr-2-itr-3-refund-80c-deductions.html\">which ITR an NRI files</a>.",
            "<strong>PPF after becoming an NRI:</strong> see <a href=\"nri-ppf-account-rules-continue-maturity-premature-closure-extension-repatriation-2026.html\">PPF for NRIs</a>.",
            "<strong>Investing instead:</strong> NRIs can use NRE fixed deposits, mutual funds, bonds and GIFT City products; see <a href=\"can-nri-invest-in-bonds-india-government-securities-rbi-retail-direct-ncd-tax-free-bonds-2026.html\">NRI bonds</a> and <a href=\"nri-mutual-funds-india-tax.html\">NRI mutual funds</a>.")
         + '<p>Related: <a href="moving-abroad-from-india-becoming-nri-checklist-savings-account-to-nro-demat-mutual-funds-tax-2026.html">becoming-an-NRI checklist</a> &middot; <a href="nri-taxation-india-complete-guide.html">NRI taxation guide</a>.</p>'
         + sources("Income-tax law: section 87A (resident individuals); proviso on long-term capital gains for land or buildings acquired before 23 July 2024 (resident individuals and HUFs; Finance (No. 2) Act 2024); senior-citizen exemption limits and section 80TTB (residents). PFRDA NPS rules for NRIs and OCI cardholders (as summarised by Outlook Money, Protean and other guides). Post office small savings scheme rules (SCSS, Sukanya Samriddhi, PPF, NSC) as summarised by India Post guides. Checked 20 November 2026.")),
    ],
    faqs=[("Is an NRI eligible for the section 87A rebate?", "No. The rebate is available only to resident individuals, so an NRI with Indian income above the basic exemption limit pays tax."),
          ("Can an NRI take the indexation benefit on property sold in India?", "No. The option to pay 20% with indexation on land or buildings bought before 23 July 2024 is for resident individuals and HUFs; NRIs pay 12.5% without indexation."),
          ("Is an NRI eligible for NPS?", "Yes. NRIs and OCI cardholders can open NPS and contribute from NRE or NRO accounts; deductions under section 80CCD apply in the old regime."),
          ("Can an NRI invest in post office schemes?", "Not in new accounts. NRIs cannot open new PPF, NSC, SCSS, Sukanya Samriddhi or other post office small savings accounts; PPF and NSC opened while resident continue to maturity."),
        ("Can NRI parents open a Sukanya Samriddhi account for their daughter?", "Generally no. The scheme is for a girl who is a resident Indian citizen when the account is opened, so a daughter living abroad with NRI parents does not qualify for a new account. If the account was opened while the family lived in India, the treatment after the girl or guardian becomes an NRI has varied over time and banks apply it differently: some allow deposits to continue to maturity on a non-repatriation basis, others treat the change as a reason to close. Tell the bank or post office within a month of the change and get its decision in writing."),
          ("Is an NRI eligible for the Senior Citizen Savings Scheme?", "No. SCSS is only for resident senior citizens."),
        ("Can an NRI claim section 80D for health insurance for parents in India?", "Yes, under the old regime only: section 80D (section 126 of the Income-tax Act, 2025 from tax year 2026-27) is open to any individual, resident or not. An NRI can deduct premiums paid for self, spouse and children up to INR 25,000 and for parents up to a further INR 25,000. The parents’ limit rises to INR 50,000 if they are senior citizens, which the law defines as residents of India aged 60 or more; parents who live abroad stay at INR 25,000 whatever their age. Pay by any mode other than cash (cash is allowed only for preventive health check-ups up to INR 5,000 within the limit). The deduction only helps if you have taxable Indian income to set it against."),
          ("Can BQP review what I can claim?", "Yes. " + C)],
    related=[("nri-ppf-account-rules-continue-maturity-premature-closure-extension-repatriation-2026.html", "PPF for NRIs"),
             ("nri-property-sale-tds-calculator-lower-deduction-certificate-savings.html", "NRI property TDS calculator"), ("nri-taxation-india-complete-guide.html", "NRI taxation guide")],
    cta_h="Not sure what you can claim as an NRI?", cta_b=C,
    keywords="is NRI eligible for 87A rebate, can NRI take indexation benefit, is NRI eligible for NPS, can NRI invest in post office schemes, is NRI eligible for SCSS, is NRI eligible for Sukanya Samriddhi, NRI 80TTB, NRI senior citizen exemption",
    desc="NRI eligibility (2026): no section 87A rebate; no indexation option on pre-23 July 2024 property (12.5% without); no senior-citizen limits or 80TTB; NPS open to NRIs and OCIs; no new PPF, NSC, SCSS, Sukanya or post office accounts - existing PPF/NSC continue to maturity.",
    howto={"name": "How an NRI checks which reliefs and schemes apply", "description": "A quick review before filing or investing.", "steps": [
        {"name": "Confirm residential status", "text": "Non-resident for the year in question."},
        {"name": "Drop resident-only reliefs", "text": "87A, indexation option, senior-citizen limits, 80TTB."},
        {"name": "Choose the regime", "text": "Old regime for 80C, 80D and 80CCD deductions."},
        {"name": "Review schemes you hold", "text": "PPF and NSC to maturity; no new post office accounts."},
        {"name": "File and claim refunds", "text": "Recover excess TDS through the Indian return."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch EN complete")
