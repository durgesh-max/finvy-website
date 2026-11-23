# -*- coding: utf-8 -*-
"""Batch GE (24 Nov 2026): NRI and the Hindu Undivided Family (HUF) - can an NRI be karta, how the HUF's residence is
decided, tax for a resident vs non-resident HUF, delegation to a resident coparcener, practical banking and filing points.
Call-first page for NRIs with family HUFs in India.
Demand: sweep ac53 (24 Nov 2026), all 7 markets: "can nri be karta of huf", "huf nri karta", "nri huf". No HUF page on
the site.
Facts (checked 24 Nov 2026):
- No legal bar on an NRI being karta (CAclubindia article on the NRI karta; Kaanoon; Inshorts summary).
- Residence of an HUF (section 6(2) of the 1961 Act, carried into the 2025 Act): resident unless control and management of
  its affairs are wholly outside India; the karta's own residence is relevant to whether a resident HUF is ordinarily
  resident or not (RNOR tests applied to the karta); if the karta delegates management to a coparcener in India, the HUF
  is resident (Income Tax Department residential status page; CAclubindia; Teachoo).
- An HUF has its own PAN, basic exemption and slab rates; it can choose the new regime; the section 87A rebate is for
  resident individuals only, not HUFs.
- Since the 2005 amendment to the Hindu Succession Act, daughters are coparceners; courts have held an eldest daughter can
  be karta (Delhi High Court, Sujata Sharma, 2015)."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 24 November 2026."
SLUG = "nri-karta-huf-residential-status-tax-india-can-nri-be-karta-2026"

C = contact("the HUF's assets and income in India, who the karta and coparceners are, where each of them lives, and who actually manages the HUF's affairs")
L = lambda h, t: f'<a href="{h}">{t}</a>'
PAGES = [dict(
    slug=SLUG,
    title="Can an NRI Be Karta of an HUF? (2026): HUF Residential Status, Tax and What Changes When the Karta Lives Abroad",
    em="yes, but where the HUF is managed decides its tax.",
    kicker="/ NRIs &middot; HUF &middot; Updated 2026-11-24",
    lead=("<strong>Yes. Nothing in law stops an NRI from being the karta of a Hindu Undivided Family (HUF), including after a parent&rsquo;s death when the eldest coparcener living abroad becomes karta.</strong> "
          "What changes is the HUF&rsquo;s tax position. An HUF is <strong>resident in India unless the control and management of its affairs is wholly outside India</strong>; if an NRI karta runs everything from abroad, the HUF can be <strong>non-resident</strong> and taxed only on its Indian income. "
          "If any part of the management happens in India, for example through a coparcener in India handling the bank account or property, the HUF stays resident, and the karta&rsquo;s own residence decides whether it is ordinarily resident. "
          "The HUF keeps its own PAN, basic exemption and slab rates whoever the karta is."),
    sections=[
        ("/ Quick answers", "What NRI families ask.",
         ul("<strong>Can an NRI be karta of an HUF?</strong> Yes. The karta is usually the senior-most coparcener; living abroad does not disqualify them. Daughters are coparceners too, and courts have accepted an eldest daughter as karta.",
            "<strong>Does the HUF become an NRI if the karta is an NRI?</strong> Not automatically. The HUF is non-resident only if its control and management is wholly outside India. Any management in India keeps it resident.",
            "<strong>What difference does it make?</strong> A non-resident HUF is taxed only on income earned or received in India. A resident and ordinarily resident HUF is taxed on worldwide income. A resident but not ordinarily resident HUF sits in between.",
            "<strong>Can the NRI karta hand over day-to-day management?</strong> Yes, the karta can let a coparcener in India manage affairs, but that makes the HUF resident.",
            "<strong>Does the HUF still file a return?</strong> Yes, in its own PAN, if its income exceeds the basic exemption or it needs a refund.")),
        ("/ HUF residence", "How the karta's location plays out.",
         table(["Situation", "HUF status", "Taxed on"], [
             ["Karta abroad, all decisions and management wholly outside India", "Non-resident", "Indian income only"],
             ["Karta abroad, but a coparcener or agent manages affairs in India", "Resident; ordinary residence follows the karta", "Worldwide income if ordinarily resident"],
             ["Karta in India", "Resident", "Worldwide income if the karta is ordinarily resident"],
             ["Karta recently returned to India", "Resident", "May be resident but not ordinarily resident for a few years, based on the karta's past residence"]])
         + '<p>The residence tests for the karta are the same day-count tests used for individuals; see ' + L("nri-residential-status-rnor-india.html", "NRI residential status and RNOR") + '.</p>'),
        ("/ Practical points", "Running an HUF with a karta abroad.",
         ul("<strong>Paper the management:</strong> if the aim is a non-resident HUF, keep decisions, bank operations and property management documented from abroad. A routine power of attorney to someone in India can make the HUF resident.",
            "<strong>Bank accounts and investments:</strong> banks treat HUF accounts differently when the karta lives abroad; check how the bank will let the karta operate, and update KYC after a change of karta.",
            "<strong>Change of karta:</strong> on the death of the karta, the next senior coparcener takes over; update PAN details, bank mandates and property records.",
            "<strong>Tax:</strong> the HUF can choose the old or new regime each year; the zero-tax rebate up to INR 12 lakh is for resident individuals, not HUFs.",
            "<strong>Selling HUF property:</strong> TDS depends on the HUF&rsquo;s residence; a non-resident HUF selling property faces TDS at non-resident rates; see " + L("nri-selling-indian-property-capital-gains.html", "NRI property sale") + ".",
            "<strong>Partition:</strong> a partition ends the HUF for tax only when recognised under the tax law; plan it with the family&rsquo;s property and FEMA position in mind.")
         + call_box("an HUF with an NRI karta", ["Whether the HUF is resident or non-resident",
                                                  "How to manage the HUF from abroad",
                                                  "HUF return, regime choice and TDS",
                                                  "Change of karta, PAN and bank records",
                                                  "Sale of HUF property or partition"],
                    "the HUF's assets, members, where each lives and who manages its affairs.")
         + sources("Income-tax Act, 1961, section 6(2) and 6(6) (residence of an HUF and of its karta), carried into the Income-tax Act, 2025; Income Tax Department guidance on residential status; CAclubindia, &lsquo;The curious case of the NRI karta&rsquo;; Hindu Succession (Amendment) Act, 2005 (daughters as coparceners); Delhi High Court, Sujata Sharma v. Manu Gupta (2015) on a daughter as karta; Finance Act, 2025 (new regime slabs; rebate for resident individuals). Checked 24 November 2026.")),
    ],
    faqs=[("Can an NRI be karta of an HUF?", "Yes. There is no legal bar on a non-resident being karta. The karta is usually the senior-most coparcener, and living abroad does not change that."),
          ("Does an HUF become non-resident if the karta is an NRI?", "Only if the control and management of the HUF's affairs is wholly outside India. If any part of the management is in India, for example a coparcener in India handles its bank account or property, the HUF remains resident."),
          ("How is the residential status of an HUF decided?", "An HUF is resident unless its control and management is wholly outside India. A resident HUF is ordinarily resident or not ordinarily resident depending on the karta's own past residence in India."),
          ("Is an NRI HUF taxed on foreign income?", "A non-resident HUF is taxed only on income earned or received in India. A resident and ordinarily resident HUF is taxed on worldwide income."),
          ("Can an HUF claim the INR 12 lakh zero-tax rebate?", "No. The rebate is for resident individuals only. An HUF gets the basic exemption and slab rates of the regime it chooses."),
          ("Can BQP advise on an HUF with an NRI karta?", "Yes. " + C)],
    related=[("nri-residential-status-rnor-india.html", "NRI residential status and RNOR"),
             ("nri-selling-indian-property-capital-gains.html", "NRI selling Indian property"),
             ("nri-inheritance-indian-property-tax-fema-2026.html", "NRI inheriting Indian property"),
             ("gift-money-from-parents-in-india-tax-usa-uk-canada-australia-form-3520-lrs-tcs-2026.html", "Gift money from parents in India"),
             ("nri-senior-citizen-tax-india-2026-exemption-limit-80ttb-advance-tax-15h-pension-retire-to-india.html", "NRI senior citizen tax")],
    cta_h="HUF with a karta abroad?", cta_b=C,
    keywords="can NRI be karta of HUF, NRI karta HUF, NRI HUF, residential status of HUF, HUF control and management, HUF non-resident, HUF tax India 2026, HUF karta living abroad",
    desc="Can an NRI be karta of an HUF? Yes. The HUF is non-resident only if its control and management is wholly outside India; otherwise resident, with ordinary residence following the karta. Tax for resident vs non-resident HUFs, delegation, bank and PAN points, property sale and partition.",
    howto={"name": "How to work out an HUF's residence when the karta is an NRI", "description": "Steps for the tax year.", "steps": [
        {"name": "Map who manages what", "text": "Decisions, bank operations, property, investments."},
        {"name": "Check where management happens", "text": "Wholly outside India means non-resident; any part in India means resident."},
        {"name": "Apply the karta's residence tests", "text": "For a resident HUF, decides ordinarily resident or not."},
        {"name": "Decide the tax base", "text": "Indian income only, or worldwide income."},
        {"name": "File in the HUF's PAN", "text": "Choose the old or new regime."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch GE complete")
