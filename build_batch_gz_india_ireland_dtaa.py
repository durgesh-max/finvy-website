# -*- coding: utf-8 -*-
"""Batch GZ (24 Nov 2026): India-Ireland DTAA - 10% caps on dividends, interest (interest to specified institutions
exempt), royalties and fees for technical services, Article 8 on shipping and air transport (stated generally, text to
check), aircraft leasing questions, permanent establishment, MLI, and how to claim.
Demand: sweep ac94 (24 Nov 2026), all 7 markets: "india ireland dtaa", "india ireland dtaa income tax", "article 8 of india
ireland dtaa", "india ireland dtaa pdf".
Facts (checked 24 Nov 2026): ClearTax, NoBroker, Nishith Desai, TaxGuru: dividends, interest, royalties and FTS taxable at
up to 10% in the source country; interest to certain institutions exempt; treaty signed 2000, effective 2001. Article 8
text not retrieved - described generally with a caveat. Claim documents as on other site treaty pages."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 24 November 2026."
SLUG = "india-ireland-dtaa-tax-treaty-rates-dividend-interest-royalty-fts-10-percent-article-8-2026"

C = contact("whether you are an Irish company, an Irish resident or an Indian resident, the income type (dividend, interest, royalty, technical fees, lease rentals, salary or gains), the amounts, and whether you have a TRC and PAN")
L = lambda h, t: f'<a href="{h}">{t}</a>'
PAGES = [dict(
    slug=SLUG,
    title="India-Ireland DTAA (2026): Tax Treaty Rates of 10% on Dividends, Interest, Royalties and Technical Fees, Article 8 and How to Claim",
    em="a straightforward 10% treaty, with leasing and shipping questions to watch.",
    kicker="/ Irish companies and NRIs in Ireland &middot; DTAA &middot; Updated 2026-11-24",
    lead=("<strong>The India-Ireland double tax avoidance agreement, signed in 2000 and effective from 2001, caps Indian tax on dividends, interest, royalties and fees for technical services paid to an Irish resident at 10%, against India&rsquo;s domestic withholding of around 20% plus surcharge and cess.</strong> "
          "Interest paid to certain government and financial institutions is exempt. Article 8 deals with profits from shipping and air transport, which matters for airlines and the aircraft leasing businesses that make Ireland a common counterparty for Indian carriers. "
          "To get the treaty rate, the Irish recipient gives the Indian payer a tax residency certificate, Form 41 (formerly Form 10F) and usually a PAN."),
    sections=[
        ("/ Quick answers", "What Irish companies and NRIs ask.",
         ul("<strong>What are the treaty rates?</strong> Up to 10% on dividends, interest, royalties and fees for technical services paid by an Indian payer to an Irish resident beneficial owner.",
            "<strong>Is any interest exempt?</strong> Yes, interest paid to certain government bodies and financial institutions named in the treaty.",
            "<strong>What does Article 8 cover?</strong> Profits from operating ships and aircraft in international traffic; check the treaty text for how it allocates taxing rights and whether leasing income falls inside it.",
            "<strong>How are aircraft lease rentals treated?</strong> Depending on the lease terms and treaty definitions, payments by Indian airlines to Irish lessors can be argued as royalties or business profits, so the treaty position needs reviewing for each lease.",
            "<strong>Does the MLI apply?</strong> Check the synthesised text; the principal purpose test and beneficial ownership rules apply to treaty claims.")),
        ("/ Rates at a glance", "Indian tax on payments to an Irish resident.",
         table(["Income", "India-Ireland DTAA", "Without treaty benefit"], [
             ["Dividends", "10%", "20% plus surcharge and cess"],
             ["Interest", "10% (specified institutions exempt)", "20% or other domestic rates plus surcharge and cess"],
             ["Royalties", "10%", "20% plus surcharge and cess"],
             ["Fees for technical services", "10%", "20% plus surcharge and cess"],
             ["Business profits", "Taxable in India only with a permanent establishment", "Taxable if there is a business connection"]])
         + '<p>Related: ' + L("what-is-dtaa.html", "what a DTAA is") + ', ' + L("india-uk-tax-treaty-dtaa.html", "India-UK DTAA") + ' and ' + L("gift-city.html", "GIFT City, including aircraft leasing") + '.</p>'),
        ("/ Claiming and planning", "Documents and credit.",
         ul("<strong>Documents:</strong> an Irish tax residency certificate, Form 41 and a PAN or the documents allowed instead; see " + L("tax-residency-certificate-india-form-42-43-10fa-10fb-freelancer-youtube-2026.html", "tax residency certificates") + ".",
            "<strong>Substance:</strong> keep evidence of real activity in Ireland, since treaty benefits can be denied to conduit arrangements.",
            "<strong>Leasing and shipping:</strong> review each contract against Article 8 and the royalty definition before fixing the withholding rate.",
            "<strong>Credit in Ireland:</strong> Indian tax at the treaty rate is generally creditable against Irish tax on the same income.",
            "<strong>Indian residents with Irish income</strong> claim foreign tax credit in India for Irish tax.")
         + call_box("India-Ireland treaty questions", ["Treaty rate on dividends, interest, royalties and FTS",
                                                         "Aircraft and equipment leasing payments",
                                                         "TRC, Form 41 and PAN",
                                                         "PE review for Irish companies",
                                                         "Foreign tax credit in India"],
                    "the recipient, the payment type and the amounts.")
         + sources("Agreement between India and Ireland for the avoidance of double taxation (signed 2000, effective 2001); rates as reported by ClearTax, NoBroker, Nishith Desai Associates and TaxGuru; Income Tax Department treaty and withholding rate pages. Article 8 described generally; check the treaty text for its exact scope. Checked 24 November 2026.")),
    ],
    faqs=[("What are the India-Ireland DTAA rates?", "Dividends, interest, royalties and fees for technical services paid by an Indian payer to an Irish resident are taxed in India at up to 10%, with interest to certain government and financial institutions exempt. Without the treaty, withholding is usually 20% plus surcharge and cess."),
          ("What is Article 8 of the India-Ireland DTAA?", "The article on shipping and air transport, covering profits from operating ships and aircraft in international traffic. Check the treaty text for how it allocates taxing rights and whether leasing income is included."),
          ("How does an Irish company claim the treaty rate in India?", "Give the Indian payer an Irish tax residency certificate, Form 41 (formerly Form 10F) and a PAN or the documents allowed instead, before tax is deducted, and keep evidence of substance in Ireland."),
          ("Are aircraft lease rentals to Irish lessors taxed in India?", "It depends on the lease terms and the treaty definitions: such payments can be argued as royalties or as business profits, which changes the Indian tax position, so each lease needs review."),
          ("Can BQP advise on the India-Ireland DTAA?", "Yes. " + C)],
    related=[("what-is-dtaa.html", "What is a DTAA"),
             ("india-uk-tax-treaty-dtaa.html", "India-UK DTAA"),
             ("india-spain-dtaa-tax-treaty-royalty-fts-10-percent-mfn-notification-33-2024-rates.html", "India-Spain DTAA"),
             ("india-france-dtaa-2026-amending-protocol-dividend-5-15-capital-gains-mfn-removed-rates.html", "India-France DTAA"),
             ("tax-residency-certificate-india-form-42-43-10fa-10fb-freelancer-youtube-2026.html", "Tax residency certificates")],
    cta_h="Paying or receiving income between India and Ireland?", cta_b=C,
    keywords="India Ireland DTAA, India Ireland tax treaty, India Ireland DTAA rates, article 8 India Ireland DTAA, India Ireland DTAA royalty, India Ireland DTAA dividend, aircraft leasing Ireland India tax",
    desc="India-Ireland DTAA (2026): 10% on dividends, interest (specified institutions exempt), royalties and fees for technical services; Article 8 shipping and air transport; aircraft lease payments; how to claim with TRC, Form 41 and PAN.",
    howto={"name": "How to apply the India-Ireland treaty", "description": "For payments to an Irish resident.", "steps": [
        {"name": "Identify the income type", "text": "Dividend, interest, royalty, FTS, lease rental or business profits."},
        {"name": "Apply the treaty rate", "text": "Up to 10% on the main payment streams."},
        {"name": "Collect TRC, Form 41 and PAN", "text": "Before the Indian payer deducts tax."},
        {"name": "Review leasing and shipping contracts", "text": "Against Article 8 and the royalty definition."},
        {"name": "Claim credit", "text": "In Ireland for Indian tax, or in India for Irish tax."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch GZ complete")
