# -*- coding: utf-8 -*-
"""Batch GX (24 Nov 2026): India-Italy DTAA - one of India's older treaties with higher rates than the common 10%:
dividends 15% for a qualifying shareholding (otherwise up to 25%, so India's domestic 20% can be lower), interest 15%
(government interest exempt), royalties and fees for technical services 20%; the treaty rate applies without surcharge
and cess and the lower of treaty or domestic rate applies; capital gains (Article 13) and how to claim.
Demand: sweep ac94 (24 Nov 2026), all 7 markets: "india italy dtaa", "india italy dtaa income tax", "article 13 of india
italy dtaa", "india vs italy dtaa".
Facts (checked 24 Nov 2026): ClearTax, NoBroker, TaxGuru, India Briefing DTAA guide: dividends 15% (some sources show
15%/25% by shareholding), interest 15% with government interest exempt, royalties and FTS 20%; treaty text not retrieved,
so rates are stated with that caveat. Section 90(2) principle (lower of treaty or domestic rate) and no surcharge/cess on
treaty rates as on other site treaty pages."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 24 November 2026."
SLUG = "india-italy-dtaa-tax-treaty-rates-dividend-15-interest-royalty-fts-20-article-13-2026"

C = contact("whether you are an Italian company, an Italian resident or an Indian resident, the income type (dividend, interest, royalty, technical fees, salary or gains), the shareholding and amounts, and whether you have a TRC and PAN")
L = lambda h, t: f'<a href="{h}">{t}</a>'
PAGES = [dict(
    slug=SLUG,
    title="India-Italy DTAA (2026): Tax Treaty Rates for Dividends, Interest, Royalties and Technical Fees, Article 13 and How to Claim",
    em="higher rates than most treaties, so compare with the domestic rate every time.",
    kicker="/ Italian companies and NRIs in Italy &middot; DTAA &middot; Updated 2026-11-24",
    lead=("<strong>The India-Italy double tax avoidance agreement is one of India&rsquo;s older treaties and its rates are higher than the 10% common in newer ones: about 15% on dividends for a qualifying shareholding, 15% on interest, and 20% on royalties and fees for technical services, as reported by treaty guides.</strong> "
          "Because Indian law lets a non-resident use whichever is lower, the treaty or the Income-tax Act, the domestic rate can sometimes be the better option, especially where the treaty dividend rate for smaller holdings is higher than India&rsquo;s 20%. "
          "The treaty rate also applies without surcharge and cess. To claim it, the Italian recipient gives the Indian payer a tax residency certificate, Form 41 (formerly Form 10F) and a PAN."),
    sections=[
        ("/ Quick answers", "What Italian companies and NRIs ask.",
         ul("<strong>What is the dividend rate?</strong> About 15% for a qualifying shareholding; for other holdings treaty guides show a higher rate, so compare it with India&rsquo;s domestic 20% rate plus surcharge and cess.",
            "<strong>What about interest?</strong> 15%, with interest to the government and certain public bodies exempt.",
            "<strong>Royalties and technical fees?</strong> 20% of the gross amount, the same headline rate as Indian law, but without surcharge and cess when claimed under the treaty.",
            "<strong>Capital gains (Article 13)?</strong> Covered by the treaty&rsquo;s capital gains article; whether India taxes a particular gain depends on its wording and the asset, so check before relying on an exemption.",
            "<strong>Can the domestic rate be lower?</strong> Yes. The lower of the treaty rate and the Income-tax Act rate applies, so compare both for each payment.")),
        ("/ Rates at a glance", "Indian tax on payments to an Italian resident (as reported by treaty guides).",
         table(["Income", "India-Italy DTAA", "Without treaty benefit"], [
             ["Dividends", "About 15% for a qualifying holding; higher for others", "20% plus surcharge and cess"],
             ["Interest", "15% (government interest exempt)", "20% or other domestic rates plus surcharge and cess"],
             ["Royalties", "20%", "20% plus surcharge and cess"],
             ["Fees for technical services", "20%", "20% plus surcharge and cess"],
             ["Business profits", "Taxable in India only with a permanent establishment", "Taxable if there is a business connection"]])
         + '<p>Compare: ' + L("india-france-dtaa-2026-amending-protocol-dividend-5-15-capital-gains-mfn-removed-rates.html", "India-France DTAA") + ', ' + L("india-germany-dtaa-tax-treaty-nri-company-rates-10-percent-2026.html", "India-Germany DTAA") + ' and ' + L("what-is-dtaa.html", "what a DTAA is") + '.</p>'),
        ("/ Claiming and planning", "Documents and credit.",
         ul("<strong>Documents:</strong> Italian tax residency certificate, Form 41 and a PAN or the documents allowed instead; see " + L("tax-residency-certificate-india-form-42-43-10fa-10fb-freelancer-youtube-2026.html", "tax residency certificates") + ".",
            "<strong>Compare rates:</strong> for each payment, check whether the treaty rate or the domestic rate with surcharge and cess gives less tax.",
            "<strong>Technical fees:</strong> check how the treaty defines fees for technical services before applying the 20% rate; see " + L("fees-for-technical-services-fts-taxability-india-make-available-treaty-withholding-2026.html", "fees for technical services") + ".",
            "<strong>Credit in Italy:</strong> Indian tax at the treaty rate is generally creditable against Italian tax on the same income.",
            "<strong>Indian residents with Italian income</strong> claim foreign tax credit in India for Italian tax.")
         + call_box("India-Italy treaty questions", ["Treaty vs domestic rate on each payment",
                                                       "Dividend planning for Italian parents",
                                                       "TRC, Form 41 and PAN",
                                                       "PE review for Italian companies",
                                                       "Foreign tax credit in India"],
                    "the recipient, the income type, the holding and the amounts.")
         + sources("Agreement between India and Italy for the avoidance of double taxation (1993); rates as reported by ClearTax, NoBroker, TaxGuru and India Briefing's DTAA guide (2026); Income Tax Department treaty and withholding rate pages. The treaty text should be checked for exact rates and shareholding thresholds before relying on them. Checked 24 November 2026.")),
    ],
    faqs=[("What are the India-Italy DTAA rates?", "As reported by treaty guides: about 15% on dividends for a qualifying shareholding, 15% on interest (government interest exempt), and 20% on royalties and fees for technical services, all without surcharge and cess when claimed under the treaty. Check the treaty text for exact thresholds."),
          ("Is the India-Italy treaty rate always better than the domestic rate?", "No. A non-resident can use whichever is lower, the treaty or the Income-tax Act. Because some India-Italy rates are high, the domestic rate can be lower for some dividends, so compare both for each payment."),
          ("What does Article 13 of the India-Italy DTAA cover?", "Capital gains. Whether India can tax a particular gain depends on the article's wording and the type of asset, such as shares or immovable property, so check it before relying on an exemption."),
          ("How does an Italian company claim the treaty rate in India?", "Give the Indian payer an Italian tax residency certificate, Form 41 (formerly Form 10F) and a PAN or the documents allowed instead, before tax is deducted."),
          ("Can BQP advise on the India-Italy DTAA?", "Yes. " + C)],
    related=[("india-france-dtaa-2026-amending-protocol-dividend-5-15-capital-gains-mfn-removed-rates.html", "India-France DTAA"),
             ("india-switzerland-dtaa-tax-treaty-rates-mfn-suspended-2025-nestle-dividend-10-percent.html", "India-Switzerland DTAA"),
             ("india-germany-dtaa-tax-treaty-nri-company-rates-10-percent-2026.html", "India-Germany DTAA"),
             ("what-is-dtaa.html", "What is a DTAA"),
             ("tax-residency-certificate-india-form-42-43-10fa-10fb-freelancer-youtube-2026.html", "Tax residency certificates")],
    cta_h="Paying or receiving income between India and Italy?", cta_b=C,
    keywords="India Italy DTAA, India Italy tax treaty, India Italy DTAA rates, article 13 India Italy DTAA, India Italy DTAA dividend, India Italy DTAA royalty, India Italy DTAA income tax",
    desc="India-Italy DTAA (2026): about 15% on dividends for a qualifying holding, 15% on interest, 20% on royalties and fees for technical services, without surcharge and cess; compare with the domestic rate; Article 13 capital gains; how to claim with TRC, Form 41 and PAN.",
    howto={"name": "How to apply the India-Italy treaty", "description": "For payments to an Italian resident.", "steps": [
        {"name": "Identify the income type", "text": "Dividend, interest, royalty, FTS or gains."},
        {"name": "Compare treaty and domestic rates", "text": "Use the lower; treaty rates carry no surcharge or cess."},
        {"name": "Check holding thresholds", "text": "For the lower dividend rate."},
        {"name": "Collect TRC, Form 41 and PAN", "text": "Before the Indian payer deducts tax."},
        {"name": "Claim credit", "text": "In Italy for Indian tax, or in India for Italian tax."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch GX complete")
