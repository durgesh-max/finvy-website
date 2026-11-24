# -*- coding: utf-8 -*-
"""Batch GU (24 Nov 2026): India-Japan DTAA - treaty rates (dividends, interest, royalties and fees for technical
services at 10%, interest to the government and central bank exempt), Article 12 without a "make available" clause,
capital gains under Article 13, the MLI and principal purpose test, how Japanese companies and Indian residents claim the
rate (TRC, Form 41 formerly 10F, PAN), and foreign tax credit. Call-first page for Japanese companies in India and NRIs in
Japan.
Demand: sweep ac93 (24 Nov 2026), all 7 markets: "india japan dtaa", "indo japan dtaa", "article 12 of india japan dtaa",
"india japan dtaa pdf", "india vs japan dtaa".
Facts (checked 24 Nov 2026): India-Japan DTAA signed 7 March 1989, in force for Indian withholding from 1 April 1990,
amended by protocol; 10% caps on dividends (Article 10), interest (Article 11, with government/central bank exemptions)
and royalties and fees for technical services (Article 12, no make-available test) - ClearTax, NoBroker, Beacon Filing,
India Law Offices; MLI applies to the treaty (Japan Ministry of Finance MLI page: Japan notifications 26 September 2018,
India 25 June 2019), including the principal purpose test (CBDT PPT guidance, EY alert, January 2025). Capital gains
article stated without a share-gains conclusion. Treaty-claim documents as on site pages (TRC, Form 41, PAN)."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 24 November 2026."
SLUG = "india-japan-dtaa-tax-treaty-rates-dividend-interest-royalty-fts-article-12-2026"

C = contact("whether you are a Japanese company, a Japanese resident or an Indian resident, the type of income (dividend, interest, royalty, technical fees, salary or gains), the amounts, and whether you have a TRC and PAN")
L = lambda h, t: f'<a href="{h}">{t}</a>'
PAGES = [dict(
    slug=SLUG,
    title="India-Japan DTAA (2026): Tax Treaty Rates for Dividends, Interest, Royalties and Technical Fees, Article 12 and How to Claim",
    em="10% on the main payment streams, if you can show treaty residence.",
    kicker="/ Japanese companies and NRIs in Japan &middot; DTAA &middot; Updated 2026-11-24",
    lead=("<strong>The India-Japan double tax avoidance agreement, signed in 1989 and amended by protocol, caps Indian tax on dividends, interest, royalties and fees for technical services paid to a Japanese resident at 10%, against India&rsquo;s domestic withholding of around 20% plus surcharge and cess.</strong> "
          "Interest paid to the governments or central banks is exempt, and unlike the India-US treaty, Article 12 has no &ldquo;make available&rdquo; test, so most technical service fees fall within the 10% rate. "
          "The treaty is modified by the Multilateral Instrument, including the principal purpose test. To get the rate, the Japanese recipient gives the Indian payer a tax residency certificate, Form 41 (formerly Form 10F) and usually a PAN; otherwise TDS is deducted at the domestic rate."),
    sections=[
        ("/ Quick answers", "What Japanese companies and NRIs ask.",
         ul("<strong>What is the dividend rate?</strong> 10% of the gross dividend under Article 10, if the Japanese resident is the beneficial owner.",
            "<strong>What does Article 12 cover?</strong> Royalties and fees for technical services, both capped at 10%; there is no make-available clause, so managerial, technical and consultancy fees are generally covered.",
            "<strong>Is interest taxed?</strong> At up to 10% under Article 11, with exemptions for interest paid to the governments, central banks and certain government-backed lenders.",
            "<strong>Are capital gains covered?</strong> Yes, under Article 13; whether India can tax a particular share sale depends on that article and the facts, so confirm before relying on an exemption.",
            "<strong>Does the MLI apply?</strong> Yes. Both countries listed the treaty under the Multilateral Instrument, so the principal purpose test can deny benefits to arrangements made mainly to obtain them.")),
        ("/ Rates at a glance", "Indian tax on payments to a Japanese resident.",
         table(["Income", "India-Japan DTAA", "Without treaty benefit"], [
             ["Dividends", "10%", "20% plus surcharge and cess"],
             ["Interest", "10% (government and central bank interest exempt)", "20% or other domestic rates plus surcharge and cess"],
             ["Royalties", "10%", "20% plus surcharge and cess"],
             ["Fees for technical services", "10% (no make-available test)", "20% plus surcharge and cess"],
             ["Business profits", "Taxable in India only with a permanent establishment", "Taxable if there is a business connection"],
             ["Capital gains", "Article 13 decides, case by case", "Domestic capital gains rules"]])
         + '<p>Related: ' + L("fees-for-technical-services-fts-taxability-india-make-available-treaty-withholding-2026.html", "fees for technical services and treaty tests") + ', ' + L("india-germany-dtaa-tax-treaty-nri-company-rates-10-percent-2026.html", "India-Germany DTAA") + ' and ' + L("what-is-dtaa.html", "what a DTAA is") + '.</p>'),
        ("/ Claiming the rate", "Documents and credit.",
         ul("<strong>Tax residency certificate</strong> from the Japanese tax office for the relevant period; see " + L("tax-residency-certificate-india-form-42-43-10fa-10fb-freelancer-youtube-2026.html", "tax residency certificates") + ".",
            "<strong>Form 41</strong> (formerly Form 10F) with the details the TRC does not give, and a PAN, or the alternative documents allowed for non-residents without one.",
            "<strong>Beneficial ownership and PPT:</strong> keep evidence that the Japanese entity has substance and a business reason, not only a treaty reason.",
            "<strong>Credit in Japan:</strong> Indian tax withheld at the treaty rate is generally creditable against Japanese tax on the same income.",
            "<strong>Indian residents with Japanese income</strong> claim foreign tax credit in India for Japanese tax, filing the foreign tax credit form before the return.")
         + call_box("India-Japan treaty questions", ["Treaty rate on dividends, interest, royalties and FTS",
                                                       "TRC, Form 41 and PAN for Indian payers",
                                                       "Permanent establishment and PPT review",
                                                       "Foreign tax credit in India",
                                                       "Japanese subsidiaries and branches in India"],
                    "the recipient, the payment type and the amounts.")
         + sources("Agreement between India and Japan for the avoidance of double taxation (1989, as amended by protocol), Articles 10 to 13; Japan Ministry of Finance page on the MLI and the Japan-India convention; CBDT guidance on the principal purpose test (January 2025, EY alert); guides from ClearTax, NoBroker, Beacon Filing and India Law Offices (2026). Check the treaty text and synthesised text for the exact wording before relying on a rate. Checked 24 November 2026.")),
    ],
    faqs=[("What are the India-Japan DTAA rates?", "Dividends, interest, royalties and fees for technical services paid by an Indian payer to a Japanese resident are taxed in India at up to 10%, with interest to the governments and central banks exempt. Without the treaty, Indian withholding is usually 20% plus surcharge and cess."),
          ("What does Article 12 of the India-Japan DTAA cover?", "Royalties and fees for technical services, both taxable in India at up to 10% of the gross amount. Unlike the India-US treaty, it has no make-available test, so most managerial, technical and consultancy fees are covered."),
          ("How does a Japanese company claim the India-Japan treaty rate?", "Give the Indian payer a tax residency certificate from Japan, Form 41 (formerly Form 10F) and a PAN or the documents allowed instead, and keep evidence of beneficial ownership and substance, because the MLI principal purpose test applies to this treaty."),
          ("Does the MLI apply to the India-Japan DTAA?", "Yes. Both countries listed the treaty under the Multilateral Instrument (Japan in 2018, India in 2019), so the principal purpose test can deny benefits to arrangements whose main purpose is to obtain them."),
          ("Can BQP advise on the India-Japan DTAA?", "Yes. " + C)],
    related=[("indian-ca-for-clients-in-japan.html", "Indian CA for clients in Japan"),
             ("fees-for-technical-services-fts-taxability-india-make-available-treaty-withholding-2026.html", "Fees for technical services"),
             ("india-germany-dtaa-tax-treaty-nri-company-rates-10-percent-2026.html", "India-Germany DTAA"),
             ("tax-residency-certificate-india-form-42-43-10fa-10fb-freelancer-youtube-2026.html", "Tax residency certificates"),
             ("what-is-dtaa.html", "What is a DTAA")],
    cta_h="Paying or receiving income between India and Japan?", cta_b=C,
    keywords="India Japan DTAA, Indo Japan DTAA, India Japan tax treaty, Article 12 India Japan DTAA, India Japan DTAA dividend rate, India Japan DTAA royalty, India Japan DTAA fees for technical services, India Japan MLI",
    desc="India-Japan DTAA (2026): 10% caps on dividends, interest, royalties and fees for technical services (government interest exempt), Article 12 without a make-available test, capital gains under Article 13, MLI principal purpose test, and how to claim with TRC, Form 41 and PAN.",
    howto={"name": "How to claim the India-Japan treaty rate", "description": "For a Japanese recipient of Indian income.", "steps": [
        {"name": "Confirm the income article", "text": "Dividend, interest, royalty, FTS, business profits or gains."},
        {"name": "Get a Japanese TRC", "text": "For the period the income is paid."},
        {"name": "Give Form 41 and PAN", "text": "To the Indian payer before payment."},
        {"name": "Check PPT and substance", "text": "Keep evidence of a business purpose."},
        {"name": "Claim credit in Japan", "text": "For Indian tax withheld at the treaty rate."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch GU complete")
