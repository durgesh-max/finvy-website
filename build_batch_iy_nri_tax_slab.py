# -*- coding: utf-8 -*-
"""Batch IY (25 Nov 2026): NRI income tax slab in India for 2026-27. NRIs use the same slab rates as residents on their
Indian income: new regime (default) nil up to Rs 4 lakh, 5% 4-8, 10% 8-12, 15% 12-16, 20% 16-20, 25% 20-24, 30%
above 24 lakh; old regime nil up to Rs 2.5 lakh, 5% 2.5-5, 20% 5-10, 30% above 10 lakh. Differences for NRIs: no
section 87A (section 156 of the 2025 Act) rebate in either regime (resident individuals only), so tax starts above
Rs 4 lakh (new) or Rs 2.5 lakh (old); no higher senior / super senior basic exemption in the old regime (Rs 3 lakh /
Rs 5 lakh are for residents). Surcharge 10% above Rs 50 lakh, 15% above Rs 1 crore, 25% above Rs 2 crore (old regime
37% above Rs 5 crore), capped at 15% on dividends and capital gains on shares; 4% cess. Special-rate incomes (capital
gains, etc.) taxed at their own rates. TDS on payments to NRIs (section 195, now section 393) is often higher than the
final liability, so refunds via ITR-2 / ITR-3. Budget 2026 made no slab changes.
Demand: sweep ac115 (25 Nov 2026), all 7 markets: "nri tax slab", "nri tax slab in india", "nri tax slab in india
2026", "nri tax brackets india", "nri tax rates in india", "nri taxable income in india", "nri tax rules".
Facts (checked 25 Nov 2026): Income Tax Department tax-rates page; BankBazaar, Bajaj Finserv, Business Today (FY 2026-27
slabs unchanged), Taxheal / Finlecture (NRIs: no 87A, no senior exemption uplift); site tax-rates 2026-27 page and
NRI eligibility page."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 25 November 2026."
SLUG = "nri-income-tax-slab-india-2026-27-new-old-regime-no-87a-rebate-basic-exemption-surcharge-tds"

C = contact("your country of residence, days in India this year and the last few years, and your Indian income by type (rent, interest, dividends, capital gains, salary)")
L = lambda h, t: f'<a href="{h}">{t}</a>'
PAGES = [dict(
    slug=SLUG,
    title="NRI Income Tax Slab in India 2026-27: New and Old Regime Rates, Why There Is No 87A Rebate, Basic Exemption, Surcharge and TDS",
    em="same slabs as residents, but no Rs 12 lakh rebate.",
    kicker="/ NRIs and OCI cardholders &middot; Indian income tax &middot; Updated 2026-11-25",
    lead=("<strong>NRIs pay income tax in India at the same slab rates as residents, but they cannot claim the section 87A rebate, so the tax-free income of up to &#8377;12 lakh under the new regime does not apply to them.</strong> "
          "Under the new regime (the default), tax starts above &#8377;4 lakh of Indian income; under the old regime it starts above &#8377;2.5 lakh, whatever the NRI&rsquo;s age. "
          "Capital gains are taxed at their own rates, and the TDS deducted on NRI income is often more than the final tax, which is why many NRIs file a return to claim a refund."),
    sections=[
        ("/ NRI tax slabs for 2026-27", "New regime and old regime side by side.",
         table(["Indian income (Rs)", "New regime (default)", "Old regime (opt in)"], [
             ["Up to 2.5 lakh", "Nil", "Nil"],
             ["2.5 lakh to 4 lakh", "Nil", "5%"],
             ["4 lakh to 5 lakh", "5%", "5%"],
             ["5 lakh to 8 lakh", "5%", "20%"],
             ["8 lakh to 10 lakh", "10%", "20%"],
             ["10 lakh to 12 lakh", "10%", "30%"],
             ["12 lakh to 16 lakh", "15%", "30%"],
             ["16 lakh to 20 lakh", "20%", "30%"],
             ["20 lakh to 24 lakh", "25%", "30%"],
             ["Above 24 lakh", "30%", "30%"]])
         + '<p>Add surcharge (10% above &#8377;50 lakh, 15% above &#8377;1 crore, 25% above &#8377;2 crore; the old regime goes to 37% above &#8377;5 crore; capped at 15% on dividends and capital gains on shares) and 4% health and education cess. Budget 2026 did not change the slabs. Compare all rates on the ' + L("tax-rates-in-india-2026-27-income-tax-slabs-percentage-corporate-gst-capital-gains-nri.html", "tax rates 2026-27 page") + '.</p>'),
        ("/ What is different for NRIs", "Rebate, exemption, special rates and TDS.",
         ul("<strong>No 87A rebate:</strong> the rebate (section 156 of the Income-tax Act, 2025) is for resident individuals only, so an NRI with &#8377;10 lakh of Indian income pays tax under both regimes; see " + L("is-nri-eligible-87a-rebate-indexation-nps-ppf-scss-sukanya-post-office-schemes-2026.html", "what NRIs are eligible for") + ".",
            "<strong>No senior-citizen uplift:</strong> the higher old-regime exemptions of &#8377;3 lakh (60 to 80) and &#8377;5 lakh (80+) are for residents; NRIs stay at &#8377;2.5 lakh.",
            "<strong>Only Indian income is taxed:</strong> income earned and received outside India is not taxed in India for an NRI; check your status with the " + L("residential-status-calculator-india-nri-rnor-section-6.html", "residential status calculator") + ".",
            "<strong>Special rates:</strong> capital gains on shares, mutual funds and property are taxed at their own rates, not the slabs; see " + L("nri-mutual-funds-india-tax.html", "NRI mutual fund tax") + ".",
            "<strong>NRE interest is exempt;</strong> NRO interest is taxable; see " + L("nre-nro-fcnr-account-tax-rules.html", "NRE, NRO and FCNR rules") + ".",
            "<strong>TDS is often higher than the tax:</strong> payers deduct TDS under section 195 (now section 393), often at flat rates; see " + L("income-tax-act-2025-section-195-now-393-what-changed-nri-foreign.html", "section 195 to 393") + " and the " + L("nri-nro-interest-tds-refund-calculator-treaty-rate-by-country-2026.html", "NRO interest TDS refund calculator") + ".")),
        ("/ Filing and treaty relief", "When to file and how to cut the tax.",
         ul("<strong>File a return</strong> if Indian income exceeds the basic exemption, to claim a refund of excess TDS, or to carry forward losses; NRIs use ITR-2 or ITR-3, not ITR-1; see " + L("which-itr-to-file-for-nri-ay-2026-27-itr-2-itr-3-refund-80c-deductions.html", "which ITR an NRI should file") + ".",
            "<strong>Treaty rates:</strong> a DTAA can cap tax on interest, dividends and royalties with a tax residency certificate; see " + L("what-is-dtaa.html", "what is a DTAA") + ".",
            "<strong>Choose the regime:</strong> the old regime still allows 80C, 80D and home-loan interest; run the " + L("new-vs-old-tax-regime-calculator.html", "new vs old regime calculator") + ".")
         + call_box("NRI tax filing", ["ITR-2 / ITR-3 for NRIs",
                                        "TDS refunds and lower TDS certificates",
                                        "DTAA relief and TRC",
                                        "Capital gains on property and shares",
                                        "Residential status review"],
                    "your Indian income and country of residence.")
         + sources("Income-tax Act, 2025 (section 156 rebate for residents; section 393 TDS) and Income-tax Act, 1961; Income Tax Department tax rates page; BankBazaar, Bajaj Finserv and Business Today on FY 2026-27 slabs; Taxheal and Finlecture NRI notes; site tax-rates and NRI eligibility guides. Checked 25 November 2026.")),
    ],
    faqs=[("What is the income tax slab for NRIs in India?", "The same as for residents: under the new regime nil up to Rs 4 lakh, then 5%, 10%, 15%, 20%, 25% and 30% above Rs 24 lakh; under the old regime nil up to Rs 2.5 lakh, 5%, 20% and 30% above Rs 10 lakh, plus surcharge and 4% cess."),
          ("Is income up to Rs 12 lakh tax-free for NRIs?", "No. The Rs 12 lakh tax-free limit comes from the section 87A rebate, which is available only to resident individuals. An NRI pays tax on Indian income above Rs 4 lakh under the new regime."),
          ("Do senior citizen NRIs get a higher basic exemption?", "No. The higher old-regime exemptions of Rs 3 lakh and Rs 5 lakh apply only to resident senior and super senior citizens; NRIs of any age have a Rs 2.5 lakh basic exemption under the old regime."),
          ("Which income of an NRI is taxable in India?", "Only income that arises, accrues or is received in India, such as rent, NRO interest, dividends, capital gains on Indian assets and salary for work done in India. NRE interest is exempt."),
          ("Can an NRI choose the old tax regime?", "Yes. The new regime is the default, but an NRI can opt for the old regime in the return if deductions such as 80C, 80D and home-loan interest make it cheaper."),
          ("Why is TDS on NRI income higher than the tax?", "Payers deduct TDS on payments to NRIs at prescribed rates without considering the slabs or the basic exemption, so the TDS is often more than the final tax; the excess is refunded when the NRI files ITR-2 or ITR-3."),
          ("Can BQP file my NRI return?", "Yes. CA Durgesh Chavda files NRI returns, claims TDS refunds, applies treaty rates and handles lower TDS certificates. " + C)],
    related=[("which-itr-to-file-for-nri-ay-2026-27-itr-2-itr-3-refund-80c-deductions.html", "NRI ITR filing"),
             ("is-nri-eligible-87a-rebate-indexation-nps-ppf-scss-sukanya-post-office-schemes-2026.html", "What NRIs are eligible for"),
             ("tax-rates-in-india-2026-27-income-tax-slabs-percentage-corporate-gst-capital-gains-nri.html", "Tax rates 2026-27"),
             ("nri-nro-interest-tds-refund-calculator-treaty-rate-by-country-2026.html", "NRO interest TDS refund calculator"),
             ("residential-status-calculator-india-nri-rnor-section-6.html", "Residential status calculator")],
    cta_h="Earning in India while living abroad?", cta_b=C,
    keywords="nri tax slab in india, nri tax slab 2026, nri income tax slab 2026-27, nri tax rates in india, nri tax brackets india, nri 87a rebate, nri basic exemption limit, nri taxable income in india",
    desc="NRI income tax slab in India 2026-27: same rates as residents (new regime nil to Rs 4 lakh, old regime nil to Rs 2.5 lakh), but no 87A rebate and no senior-citizen uplift, plus surcharge, cess, special rates, TDS and refunds.",
    howto={"name": "How an NRI works out Indian income tax", "description": "For NRIs with Indian income.", "steps": [
        {"name": "Confirm NRI status", "text": "Apply the day-count tests for the year."},
        {"name": "List Indian income", "text": "Rent, NRO interest, dividends, capital gains, Indian salary."},
        {"name": "Apply the slabs", "text": "New regime from Rs 4 lakh or old regime from Rs 2.5 lakh; no 87A rebate."},
        {"name": "Add special rates", "text": "Capital gains at their own rates, plus surcharge and cess."},
        {"name": "File and claim refund", "text": "ITR-2 / ITR-3, crediting TDS and treaty relief."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch IY complete")
