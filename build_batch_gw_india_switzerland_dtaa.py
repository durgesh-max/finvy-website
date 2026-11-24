# -*- coding: utf-8 -*-
"""Batch GW (24 Nov 2026): India-Switzerland DTAA - treaty rates (10% on dividends, interest, royalties and fees for
technical services under the treaty as amended by the 2010 protocol), Switzerland's suspension of the MFN clause for
income accruing from 1 January 2025 after India's Supreme Court Nestle ruling (October 2023), what that means for Swiss
recipients of Indian dividends and for Indian residents with Swiss income, and how to claim.
Demand: sweep ac94 (24 Nov 2026), all 7 markets: "india switzerland dtaa", "dtaa between india and switzerland tds rates",
"india switzerland dtaa article 12", "india vs switzerland dtaa".
Facts (checked 24 Nov 2026): Swiss Federal Tax Administration (ESTV) notice and EY, Mondaq, India Briefing, Business Standard,
Taxscan (December 2024): Switzerland suspended the MFN clause in the 2010 protocol; income accruing on or after 1 January
2025 taxed in the source state at treaty rates (10% for dividends) without the MFN; the 5% MFN rate may still apply to
dividends for 2018 to 2024; Supreme Court of India (October 2023, Nestle case) held MFN benefits need a separate
notification. Treaty rates for interest, royalties and FTS stated at 10% as amended in 2010 (to confirm against treaty
text)."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 24 November 2026."
SLUG = "india-switzerland-dtaa-tax-treaty-rates-mfn-suspended-2025-nestle-dividend-10-percent"

C = contact("whether you are a Swiss company, a Swiss resident or an Indian resident, the income type (dividend, interest, royalty, technical fees or gains), the amounts and dates, and any past MFN-based refund claims")
L = lambda h, t: f'<a href="{h}">{t}</a>'
PAGES = [dict(
    slug=SLUG,
    title="India-Switzerland DTAA (2026): Treaty Rates, Article 12 and the MFN Suspension From 1 January 2025 After the Nestle Ruling",
    em="10% is the working rate again: the 5% MFN route is closed for income from 2025.",
    kicker="/ Swiss companies and NRIs in Switzerland &middot; DTAA &middot; Updated 2026-11-24",
    lead=("<strong>Under the India-Switzerland double tax avoidance agreement, as amended by the 2010 protocol, Indian tax on dividends, interest, royalties and fees for technical services paid to a Swiss resident is capped at 10%.</strong> "
          "The protocol&rsquo;s most-favoured-nation clause once let Swiss investors claim a 5% dividend rate by pointing to India&rsquo;s later treaties with OECD members such as Lithuania. After India&rsquo;s Supreme Court held in October 2023 (the Nestl&eacute; case) that such benefits need a separate notification, Switzerland suspended the MFN clause for income accruing from <strong>1 January 2025</strong>, so both countries now apply the treaty rates as written. "
          "Swiss recipients claim the 10% rate with a Swiss tax residency certificate, Form 41 (formerly Form 10F) and a PAN."),
    sections=[
        ("/ Quick answers", "What Swiss investors and NRIs ask.",
         ul("<strong>What is the TDS rate on dividends to a Swiss resident?</strong> 10% under the treaty, against 20% plus surcharge and cess without it.",
            "<strong>What does Article 12 cover?</strong> Royalties and fees for technical services, both capped at 10% of the gross amount.",
            "<strong>What changed on 1 January 2025?</strong> Switzerland stopped applying the MFN clause, so the 5% MFN dividend rate is no longer available for income accruing from that date; Swiss withholding on dividends to Indian residents also reverts to the treaty rate.",
            "<strong>What about dividends from 2018 to 2024?</strong> The Swiss notice indicates the MFN position may still apply to that period on the Swiss side; Indian authorities did not apply the 5% rate, so pending claims need case-by-case review.",
            "<strong>Does the MLI apply?</strong> Check the synthesised text; anti-abuse rules and beneficial ownership tests apply either way.")),
        ("/ Rates at a glance", "Indian tax on payments to a Swiss resident.",
         table(["Income", "India-Switzerland DTAA", "Without treaty benefit"], [
             ["Dividends", "10% (MFN 5% route closed from 1 January 2025)", "20% plus surcharge and cess"],
             ["Interest", "10%", "20% or other domestic rates plus surcharge and cess"],
             ["Royalties", "10%", "20% plus surcharge and cess"],
             ["Fees for technical services", "10%", "20% plus surcharge and cess"],
             ["Business profits", "Taxable in India only with a permanent establishment", "Taxable if there is a business connection"]])
         + '<p>Related: ' + L("india-netherlands-dtaa-tax-treaty-nri-company-rates-mfn-nestle-2026.html", "India-Netherlands DTAA and the Nestle MFN ruling") + ', ' + L("india-france-dtaa-2026-amending-protocol-dividend-5-15-capital-gains-mfn-removed-rates.html", "India-France protocol removing MFN") + ' and ' + L("what-is-dtaa.html", "what a DTAA is") + '.</p>'),
        ("/ What to do", "Claims, refunds and planning.",
         ul("<strong>Claim the treaty rate</strong> with a Swiss TRC, Form 41 and a PAN before the Indian payer deducts tax; see " + L("tax-residency-certificate-india-form-42-43-10fa-10fb-freelancer-youtube-2026.html", "tax residency certificates") + ".",
            "<strong>Stop MFN-based 5% claims</strong> on Indian dividends for income from 2025, and review any refund claims for earlier years.",
            "<strong>Swiss parent companies</strong> should model Indian dividend tax at 10% and check credit in Switzerland.",
            "<strong>Indian residents with Swiss income</strong> claim foreign tax credit in India for Swiss tax withheld at the treaty rate.",
            "<strong>Service providers</strong> should check permanent establishment risk for staff working in India.")
         + call_box("India-Switzerland treaty questions", ["Treaty rate on dividends, interest, royalties and FTS",
                                                             "MFN claims for 2018 to 2024",
                                                             "TRC, Form 41 and PAN",
                                                             "Foreign tax credit in India",
                                                             "PE review for Swiss companies"],
                    "the recipient, the income type, the amounts and dates.")
         + sources("Agreement between India and Switzerland for the avoidance of double taxation (1994, as amended by the 2010 protocol); Swiss Federal Tax Administration (ESTV) notice on suspension of the MFN clause (December 2024); Supreme Court of India, October 2023 (Nestle and others); analysis from EY, Mondaq, India Briefing, Business Standard and Taxscan. Confirm interest, royalty and FTS rates against the treaty text. Checked 24 November 2026.")),
    ],
    faqs=[("What is the India-Switzerland DTAA rate on dividends?", "10% of the gross dividend for a Swiss resident beneficial owner. The 5% rate some investors claimed under the MFN clause no longer applies to income accruing from 1 January 2025, after Switzerland suspended the clause."),
          ("Why did Switzerland suspend the MFN clause with India?", "India's Supreme Court held in October 2023, in a case involving Nestle, that MFN benefits apply only after a separate notification by the Indian government. Switzerland responded by suspending the MFN clause for income accruing from 1 January 2025, citing lack of reciprocity."),
          ("What does Article 12 of the India-Switzerland DTAA cover?", "Royalties and fees for technical services, taxable in India at up to 10% of the gross amount for a Swiss resident beneficial owner."),
          ("How does a Swiss company claim the treaty rate in India?", "Give the Indian payer a Swiss tax residency certificate, Form 41 (formerly Form 10F) and a PAN or the documents allowed instead, before tax is deducted."),
          ("Can BQP advise on the India-Switzerland DTAA?", "Yes. " + C)],
    related=[("india-netherlands-dtaa-tax-treaty-nri-company-rates-mfn-nestle-2026.html", "India-Netherlands DTAA and MFN"),
             ("india-france-dtaa-2026-amending-protocol-dividend-5-15-capital-gains-mfn-removed-rates.html", "India-France DTAA protocol"),
             ("india-germany-dtaa-tax-treaty-nri-company-rates-10-percent-2026.html", "India-Germany DTAA"),
             ("what-is-dtaa.html", "What is a DTAA"),
             ("tax-residency-certificate-india-form-42-43-10fa-10fb-freelancer-youtube-2026.html", "Tax residency certificates")],
    cta_h="Paying or receiving income between India and Switzerland?", cta_b=C,
    keywords="India Switzerland DTAA, India Switzerland tax treaty, DTAA between India and Switzerland TDS rates, India Switzerland DTAA article 12, Switzerland MFN suspension India, Nestle MFN ruling, India Switzerland dividend tax",
    desc="India-Switzerland DTAA (2026): 10% on dividends, interest, royalties and fees for technical services; Switzerland suspended the MFN clause for income from 1 January 2025 after the Supreme Court's Nestle ruling, ending 5% dividend claims; how to claim with TRC, Form 41 and PAN.",
    howto={"name": "How to apply the India-Switzerland treaty", "description": "For payments to a Swiss resident.", "steps": [
        {"name": "Identify the income type", "text": "Dividend, interest, royalty, FTS or business profits."},
        {"name": "Apply the treaty rate", "text": "10%, with no MFN reduction for income from 2025."},
        {"name": "Collect TRC, Form 41 and PAN", "text": "Before the Indian payer deducts tax."},
        {"name": "Review earlier MFN claims", "text": "For 2018 to 2024, case by case."},
        {"name": "Claim credit", "text": "In Switzerland for Indian tax, or in India for Swiss tax."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch GW complete")
