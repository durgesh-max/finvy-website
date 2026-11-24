# -*- coding: utf-8 -*-
"""Batch HB (25 Nov 2026): India-China DTAA - uniform 10% caps on dividends, interest (government and specified
institution interest exempt), royalties and fees for technical services (Article 12); the 2018 protocol in force from
2019 (as reported, updating exchange of information and anti-abuse provisions); MLI status flagged to check; how Chinese
companies claim the rate; and the FDI overlay (Press Note 3 of 2020 as eased by Press Note 2 of 2026). Call-first page.
Demand: sweep ac95 (25 Nov 2026), all 7 markets, the most suggestions of 10 treaty countries: "india china dtaa",
"india vs china dtaa", "india china dtaa rates", "india china dtaa treaty".
Facts (checked 25 Nov 2026): ClearTax, NoBroker, Beacon Filing, BCAS referencer, TaxGuru: 10% on dividends, interest,
royalties and FTS; government/central bank/specified institution interest exempt; Article 12 covers royalties and FTS;
2018 protocol in force from June 2019 (content described differently by sources); MLI coverage conflicting - stated as
"check". FDI rules as on the site's Press Note 2 (2026) page."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 25 November 2026."
SLUG = "india-china-dtaa-tax-treaty-rates-10-percent-dividend-royalty-fts-press-note-fdi-2026"

C = contact("whether you are a Chinese or Hong Kong company or individual, the income type (dividend, interest, royalty, technical fees or gains), the amounts, any Indian investment or subsidiary, and whether you have a TRC and PAN")
L = lambda h, t: f'<a href="{h}">{t}</a>'
PAGES = [dict(
    slug=SLUG,
    title="India-China DTAA (2026): Tax Treaty Rates of 10% on Dividends, Interest, Royalties and Technical Fees, and the FDI Rules That Sit on Top",
    em="a simple 10% treaty, but investment approvals still decide what you can do.",
    kicker="/ Chinese companies in India &middot; DTAA &middot; Updated 2026-11-25",
    lead=("<strong>The India-China double tax avoidance agreement caps Indian tax on dividends, interest, royalties and fees for technical services paid to a Chinese resident at a uniform 10%, against India&rsquo;s domestic withholding of 20% plus surcharge and cess; interest paid to the governments, central banks and certain financial institutions is exempt.</strong> "
          "A protocol signed in 2018 came into force in 2019 to update the treaty. "
          "The tax treaty does not override India&rsquo;s investment rules: foreign direct investment with Chinese beneficial ownership still needs government approval under Press Note 3 of 2020, eased in 2026 for non-controlling stakes within 10% from other land-border countries but not for China and Hong Kong investors. "
          "Chinese recipients claim the 10% rate with a Chinese tax residency certificate, Form 41 (formerly Form 10F) and a PAN."),
    sections=[
        ("/ Quick answers", "What Chinese companies and their Indian partners ask.",
         ul("<strong>What are the treaty rates?</strong> 10% on dividends, interest, royalties and fees for technical services for a Chinese resident beneficial owner.",
            "<strong>What does Article 12 cover?</strong> Royalties and fees for technical services together, both capped at 10% of the gross amount; check the treaty&rsquo;s definition of technical fees for each service contract.",
            "<strong>What did the 2018 protocol change?</strong> It updated the treaty and came into force in 2019; sources describe changes to exchange of information and anti-abuse provisions, so read the protocol text for your case.",
            "<strong>Does the MLI apply?</strong> Sources conflict on whether China and India listed this treaty under the Multilateral Instrument; check the current position before relying on it.",
            "<strong>Can a Chinese company invest in India freely?</strong> No. Investment with Chinese beneficial ownership needs prior government approval; see " + L("press-note-2-2026-fdi-land-border-countries-china-10-percent-60-day-approval.html", "Press Note 2 (2026) and land-border FDI") + ".")),
        ("/ Rates at a glance", "Indian tax on payments to a Chinese resident.",
         table(["Income", "India-China DTAA", "Without treaty benefit"], [
             ["Dividends", "10%", "20% plus surcharge and cess"],
             ["Interest", "10% (government and specified institutions exempt)", "20% or other domestic rates plus surcharge and cess"],
             ["Royalties", "10%", "20% plus surcharge and cess"],
             ["Fees for technical services", "10%", "20% plus surcharge and cess"],
             ["Business profits", "Taxable in India only with a permanent establishment", "Taxable if there is a business connection"]])
         + '<p>Related: ' + L("china-plus-one-india-moving-sourcing-manufacturing-to-india-foreign-company-2026.html", "China plus one: moving sourcing to India") + ', ' + L("india-japan-dtaa-tax-treaty-rates-dividend-interest-royalty-fts-article-12-2026.html", "India-Japan DTAA") + ' and ' + L("what-is-dtaa.html", "what a DTAA is") + '.</p>'),
        ("/ Claiming and compliance", "Documents and the investment overlay.",
         ul("<strong>Documents:</strong> a Chinese tax residency certificate, Form 41 and a PAN or the documents allowed instead; see " + L("tax-residency-certificate-india-form-42-43-10fa-10fb-freelancer-youtube-2026.html", "tax residency certificates") + ".",
            "<strong>Service contracts:</strong> technicians or engineers sent to India can create a permanent establishment; plan days and roles.",
            "<strong>Transfer pricing:</strong> payments between Indian subsidiaries and Chinese group companies must be at arm&rsquo;s length and documented.",
            "<strong>Investment approvals:</strong> share issues, transfers and downstream investment with Chinese beneficial ownership need approval before money moves.",
            "<strong>Credit in China:</strong> Indian tax at the treaty rate is generally creditable against Chinese tax on the same income.")
         + call_box("India-China tax and investment questions", ["Treaty rate on dividends, royalties and FTS",
                                                                   "TRC, Form 41 and PAN",
                                                                   "Press Note 3 / Press Note 2 approvals",
                                                                   "PE and transfer pricing for Chinese groups",
                                                                   "Indian subsidiary compliance"],
                    "the recipient, the payment type, the amounts and any investment plan.")
         + sources("Agreement between India and China for the avoidance of double taxation (1994) and the 2018 protocol (in force 2019); rates as reported by ClearTax, NoBroker, Beacon Filing, the BCAS referencer and TaxGuru; DPIIT Press Note 3 (2020) and Press Note 2 (2026) as summarised on the linked site page. MLI coverage and protocol details should be checked against official texts. Checked 25 November 2026.")),
    ],
    faqs=[("What are the India-China DTAA rates?", "Dividends, interest, royalties and fees for technical services paid by an Indian payer to a Chinese resident are taxed in India at up to 10%, with interest to the governments, central banks and certain financial institutions exempt. Without the treaty, withholding is usually 20% plus surcharge and cess."),
          ("What does Article 12 of the India-China DTAA cover?", "Royalties and fees for technical services together, both taxable in India at up to 10% of the gross amount for a Chinese resident beneficial owner."),
          ("Does the India-China tax treaty allow Chinese companies to invest in India freely?", "No. The tax treaty only allocates taxing rights. Foreign direct investment with Chinese beneficial ownership still needs prior government approval under Press Note 3 of 2020; the 2026 easing for non-controlling stakes within 10% does not cover China and Hong Kong investors."),
          ("How does a Chinese company claim the treaty rate in India?", "Give the Indian payer a Chinese tax residency certificate, Form 41 (formerly Form 10F) and a PAN or the documents allowed instead, before tax is deducted."),
          ("Can BQP advise on the India-China DTAA?", "Yes. " + C)],
    related=[("press-note-2-2026-fdi-land-border-countries-china-10-percent-60-day-approval.html", "Press Note 2 (2026): land-border FDI"),
             ("china-plus-one-india-moving-sourcing-manufacturing-to-india-foreign-company-2026.html", "China plus one in India"),
             ("india-japan-dtaa-tax-treaty-rates-dividend-interest-royalty-fts-article-12-2026.html", "India-Japan DTAA"),
             ("what-is-dtaa.html", "What is a DTAA"),
             ("tax-residency-certificate-india-form-42-43-10fa-10fb-freelancer-youtube-2026.html", "Tax residency certificates")],
    cta_h="Paying or receiving income between India and China?", cta_b=C,
    keywords="India China DTAA, India China tax treaty, India China DTAA rates, India vs China DTAA, Article 12 India China DTAA, Chinese company India tax, Press Note 3 China FDI India",
    desc="India-China DTAA (2026): uniform 10% on dividends, interest, royalties and fees for technical services (government interest exempt); 2018 protocol in force 2019; Chinese investment still needs approval under Press Note 3; how to claim with TRC, Form 41 and PAN.",
    howto={"name": "How to apply the India-China treaty", "description": "For payments to a Chinese resident.", "steps": [
        {"name": "Identify the income type", "text": "Dividend, interest, royalty, FTS or business profits."},
        {"name": "Apply 10%", "text": "Or the domestic rate if lower."},
        {"name": "Collect TRC, Form 41 and PAN", "text": "Before the Indian payer deducts tax."},
        {"name": "Check investment approvals", "text": "Press Note 3 for any share issue or transfer."},
        {"name": "Review PE and transfer pricing", "text": "For staff in India and group payments."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch HB complete")
