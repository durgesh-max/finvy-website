# -*- coding: utf-8 -*-
"""Batch HH (25 Nov 2026): 54EC bonds (now section 85 of the Income-tax Act, 2025) - capital gains bonds for long-term
gains on land or buildings: 6 months to invest, Rs 50 lakh cap per tax year, 5-year lock-in, about 5.25% taxable interest,
issuers, NRIs, loan = transfer.
Demand: sweep ac96 (25 Nov 2026), all 7 markets: "54ec bonds lock in period", "54ec bonds time limit", "54ec bonds interest
rate", "54ec bonds list", "capital gains bonds sbi", "are capital gains bonds taxable", "54ec bonds where to buy".
Facts (checked 25 Nov 2026): Income Tax Department section 85 pages; taxsutra / caclubindia Act text (LTCG from land or
building, six months, long-term specified asset, Rs 50 lakh per tax year); Grip Invest REC 5.25% 2031 bond; Bondscanner
REC / IRFC 54EC pages (5.25%, 5 years; IRFC interest 15 October, REC 30 June); Jiraaf REC guide (500 units / Rs 50 lakh
across issuers). Issuer list and rates change: confirm the open issue."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 25 November 2026."
SLUG = "54ec-bonds-section-85-capital-gains-bonds-lock-in-interest-rate-limit-nri-2026"

C = contact("the sale date, sale price, cost and year of purchase of the property, whether you are resident or NRI, and how much of the gain you plan to put into bonds or a house")
L = lambda h, t: f'<a href="{h}">{t}</a>'
PAGES = [dict(
    slug=SLUG,
    title="54EC Bonds (2026): Capital Gains Bonds Under New Section 85, Lock-in, Interest Rate, Rs 50 Lakh Limit and NRIs",
    em="six months to invest, five years to hold.",
    kicker="/ Property sellers and NRIs &middot; Capital gains &middot; Updated 2026-11-25",
    lead=("<strong>54EC bonds, called capital gains bonds, let you save tax on a long-term gain from selling land or a building.</strong> "
          "From 1 April 2026 the exemption sits in section 85 of the Income-tax Act, 2025 (it was section 54EC). "
          "You invest the gain, not the full sale price, in specified bonds within six months of the sale, up to &#8377;50 lakh in a tax year, and hold them for five years. "
          "The interest, reported at about 5.25% a year on current issues, is taxable. Residents and NRIs can both use it."),
    sections=[
        ("/ Quick answers", "What sellers ask most.",
         ul("<strong>What is the lock-in period?</strong> Five years from the date of allotment. Selling, transferring or taking a loan against the bonds in that time brings the exempt gain back to tax.",
            "<strong>What is the time limit?</strong> Invest within six months of the date of transfer of the property. The six months run from the sale, not from the end of the year or the return due date.",
            "<strong>How much can I invest?</strong> Up to &#8377;50 lakh in a tax year, across all issuers together. Bonds are issued in units of &#8377;10,000.",
            "<strong>What is the interest rate?</strong> Current issues are reported at about 5.25% a year, paid annually. The interest is fully taxable at your slab rate.",
            "<strong>Which gains qualify?</strong> Only long-term capital gains on land, a building or both. Gains on shares, mutual funds, gold or short-term property sales do not.",
            "<strong>Can NRIs invest?</strong> Yes, NRIs can claim the exemption on property sold in India. Tax is deducted on the bond interest paid to NRIs.")),
        ("/ The rules at a glance", "Section 85 (formerly 54EC) in one table.",
         table(["Point", "Rule"], [
             ["Asset sold", "Land or building (or both), held long term (more than 24 months)"],
             ["What to invest", "The long-term capital gain, in whole or part (not the full sale price)"],
             ["Time limit", "Within six months of the date of transfer"],
             ["Maximum", "&#8377;50 lakh in a tax year, across all issuers"],
             ["Lock-in", "Five years; a loan against the bonds counts as a transfer"],
             ["Interest", "About 5.25% a year on current issues, taxable"],
             ["Issuers", "Specified bonds such as those issued by REC, PFC and IRFC; check which issues are open"],
             ["If you break the lock-in", "The exempted gain becomes taxable in the year of transfer or loan"]])
         + '<p>Exemption is proportionate: if you invest only part of the gain, only that part is exempt. A gain above &#8377;50 lakh can be covered by combining section 85 with the house exemption in section 82 (formerly 54); see '
         + L("which-section-54-vs-54f-vs-54ec-decision-tree-india.html", "section 54 vs 54F vs 54EC") + '.</p>'),
        ("/ For NRIs selling property in India", "Bonds, TDS and timing.",
         ul("<strong>Buyer&rsquo;s TDS:</strong> the buyer deducts tax on the gain at the time of sale whether or not you plan to buy bonds. To deduct less, apply for a " + L("nil-lower-tds-certificate-form-128-formerly-form-13-section-395-how-to-apply-2026.html", "lower TDS certificate (Form 128, formerly Form 13)") + " before the sale and show the planned bond investment.",
            "<strong>Refund route:</strong> if full TDS was deducted, invest in bonds within six months and claim the exemption and the refund in your Indian return.",
            "<strong>Paying for the bonds:</strong> NRIs usually invest from their NRO account, where the sale proceeds land; check the issuer&rsquo;s NRI application rules.",
            "<strong>Repatriation:</strong> on maturity, the principal and interest can be moved abroad within the NRO repatriation rules with Forms 145 and 146 (formerly 15CA and 15CB). See " + L("nri-selling-indian-property-capital-gains.html", "NRI property sale tax") + ".",
            "<strong>Residence country:</strong> the gain may also be taxable where you live; check the treaty and your foreign tax credit.")
         + call_box("Planning a property sale or bond investment", ["Long-term gain and exemption working",
                                                                   "Section 85 bonds vs house purchase (section 82 / 86)",
                                                                   "Lower TDS certificate before the sale",
                                                                   "NRI refund and ITR filing",
                                                                   "Repatriation of sale proceeds"],
                    "the sale date, price, cost and your residential status.")
         + sources("Income-tax Act, 2025, section 85 (Income Tax Department section pages); Income-tax Act, 1961, section 54EC; issuer information for REC, PFC and IRFC 54EC bonds as reported by Grip Invest, Bondscanner and Jiraaf. Rates and open issues change: confirm with the issuer before investing. This is tax information, not investment advice. Checked 25 November 2026.")),
    ],
    faqs=[("What is the lock-in period for 54EC bonds?", "Five years from the date of allotment. If you sell or transfer the bonds, or take a loan against them, within five years, the capital gain that was exempted becomes taxable."),
          ("What is the time limit to invest in 54EC bonds?", "Within six months of the date of transfer of the land or building. From 1 April 2026 the exemption is in section 85 of the Income-tax Act, 2025, with the same six-month window."),
          ("What is the maximum investment in 54EC bonds?", "Rs 50 lakh in a tax year across all issuers together. A gain above that can be covered by also buying a house under section 82 (formerly 54) where the conditions are met."),
          ("Is the interest on 54EC bonds taxable?", "Yes. Current issues are reported at about 5.25% a year, and the interest is taxable at your slab rate. Only the capital gain invested is exempt."),
          ("Can an NRI invest in 54EC bonds?", "Yes. An NRI selling land or a building in India can invest the long-term gain in section 85 bonds within six months and claim the exemption. Tax is deducted on interest paid to NRIs, and a lower TDS certificate can reduce the buyer's TDS on the sale."),
          ("Can BQP help with capital gains bonds?", "Yes. CA Durgesh Chavda can work out the exempt gain, compare bonds with a house purchase and handle the lower TDS certificate and return. " + C)],
    related=[("which-section-54-vs-54f-vs-54ec-decision-tree-india.html", "Section 54 vs 54F vs 54EC"),
             ("nri-selling-indian-property-capital-gains.html", "NRI selling property in India"),
             ("property-capital-gains-tax-calculator-india-indexation-12-5-vs-20-inherited-nri-2026.html", "Property capital gains calculator"),
             ("nil-lower-tds-certificate-form-128-formerly-form-13-section-395-how-to-apply-2026.html", "Lower TDS certificate"),
             ("income-tax-act-2025-section-mapping-old-vs-new-54-is-82-80c-is-123-nri.html", "Old vs new section numbers")],
    cta_h="Selling property and want to keep more of the gain?", cta_b=C,
    keywords="54EC bonds, 54EC bonds lock in period, 54EC bonds interest rate, 54EC bonds time limit, capital gains bonds, section 85 Income-tax Act 2025, 54EC bonds NRI, REC 54EC bonds, PFC 54EC bonds, IRFC 54EC bonds",
    desc="54EC bonds (2026), now section 85 of the Income-tax Act, 2025: invest long-term gains on land or buildings within 6 months, up to Rs 50 lakh a tax year, 5-year lock-in, about 5.25% taxable interest; issuers, NRIs and TDS.",
    howto={"name": "How to save capital gains tax with 54EC bonds", "description": "For a long-term gain on land or a building.", "steps": [
        {"name": "Work out the long-term gain", "text": "Sale price less cost and expenses, for property held more than 24 months."},
        {"name": "Decide bonds, house or both", "text": "Bonds cap at Rs 50 lakh a tax year; a house can cover the rest."},
        {"name": "Invest within six months", "text": "Apply to an open issue such as REC, PFC or IRFC before six months from the sale."},
        {"name": "Hold for five years", "text": "No sale, transfer or loan against the bonds."},
        {"name": "Claim in your return", "text": "Show the exemption under section 85 (formerly 54EC) and report the interest each year."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch HH complete")
