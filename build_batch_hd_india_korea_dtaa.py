# -*- coding: utf-8 -*-
"""Batch HD (25 Nov 2026): India-Korea DTAA - revised treaty signed 18 May 2015, in force 12 September 2016, applying in
India from fiscal years beginning 1 April 2017: interest, royalties and fees for technical services cut from 15% to 10%;
dividends at the treaty rate (reported as 15%; older tables show 15%/20% by holding); capital gains on shares taxed in the
source country; how Korean companies claim; Korean investment and manufacturing context.
Demand: sweep ac95 (25 Nov 2026), all 7 markets: "india south korea dtaa", "india korea dtaa income tax", "india korea
dtaa pdf".
Facts (checked 25 Nov 2026): PMIndia release on the revised agreement; SCC Online (entry into force 12 September 2016,
interest/royalty/FTS 15% to 10%, applies from 1 April 2017 in India); Business Standard (capital gains taxed at source);
Beacon Filing (signed 18 May 2015, dividends 15%); older Income Tax Department table shows 15%/20% - dividend rate
caveated."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 25 November 2026."
SLUG = "india-south-korea-dtaa-tax-treaty-rates-royalty-fts-interest-10-capital-gains-source-2026"

C = contact("whether you are a Korean company, a Korean resident or an Indian resident, the income type (dividend, interest, royalty, technical fees or share sale), the amounts, any Indian subsidiary or plant, and whether you have a TRC and PAN")
L = lambda h, t: f'<a href="{h}">{t}</a>'
PAGES = [dict(
    slug=SLUG,
    title="India-South Korea DTAA (2026): Royalties, Technical Fees and Interest at 10%, Dividend Rate, Capital Gains at Source and How to Claim",
    em="lower rates on technology payments, but share gains are taxed where the company sits.",
    kicker="/ Korean companies in India &middot; DTAA &middot; Updated 2026-11-25",
    lead=("<strong>India and the Republic of Korea signed a revised double tax avoidance agreement on 18 May 2015; it came into force on 12 September 2016 and applies in India to income from fiscal years beginning on or after 1 April 2017.</strong> "
          "It cut Indian tax on interest, royalties and fees for technical services paid to a Korean resident from 15% to 10%, and gave the country where a company is resident the right to tax gains on its shares. Dividends are taxed at the treaty rate, reported at 15%, against India&rsquo;s domestic 20% plus surcharge and cess. "
          "Korean recipients claim the treaty rate with a Korean tax residency certificate, Form 41 (formerly Form 10F) and a PAN."),
    sections=[
        ("/ Quick answers", "What Korean companies and their Indian partners ask.",
         ul("<strong>What are the rates on technology payments?</strong> 10% on royalties and fees for technical services, down from 15% under the old treaty.",
            "<strong>And interest?</strong> 10% under the revised treaty, also down from 15%.",
            "<strong>What is the dividend rate?</strong> Reported at 15% under the revised treaty; older official tables show 15% or 20% depending on the shareholding, so confirm against the treaty text for your holding.",
            "<strong>Are share gains taxed in India?</strong> Yes. The revised treaty lets the country where the company is resident tax gains on its shares, so gains on Indian shares are taxable in India.",
            "<strong>From when do the new rates apply?</strong> In India, to income from fiscal years beginning on or after 1 April 2017.")),
        ("/ Rates at a glance", "Indian tax on payments to a Korean resident.",
         table(["Income", "Revised India-Korea DTAA", "Without treaty benefit"], [
             ["Dividends", "Treaty rate, reported at 15%", "20% plus surcharge and cess"],
             ["Interest", "10% (was 15%)", "20% or other domestic rates plus surcharge and cess"],
             ["Royalties", "10% (was 15%)", "20% plus surcharge and cess"],
             ["Fees for technical services", "10% (was 15%)", "20% plus surcharge and cess"],
             ["Gains on Indian shares", "Taxable in India", "Taxable in India"]])
         + '<p>Related: ' + L("india-japan-dtaa-tax-treaty-rates-dividend-interest-royalty-fts-article-12-2026.html", "India-Japan DTAA") + ', ' + L("china-plus-one-india-moving-sourcing-manufacturing-to-india-foreign-company-2026.html", "moving sourcing and manufacturing to India") + ' and ' + L("what-is-dtaa.html", "what a DTAA is") + '.</p>'),
        ("/ Claiming and compliance", "Documents and planning.",
         ul("<strong>Documents:</strong> a Korean tax residency certificate, Form 41 and a PAN or the documents allowed instead; see " + L("tax-residency-certificate-india-form-42-43-10fa-10fb-freelancer-youtube-2026.html", "tax residency certificates") + ".",
            "<strong>Technical service contracts:</strong> Korean engineers working at Indian plants can create a permanent establishment; plan their days and roles.",
            "<strong>Transfer pricing:</strong> royalties, fees and parts purchases between Indian subsidiaries and Korean parents must be at arm&rsquo;s length and documented.",
            "<strong>Share sales and restructurings:</strong> model Indian capital gains tax on exits, since the treaty no longer shields gains on Indian shares.",
            "<strong>Credit in Korea:</strong> Indian tax at the treaty rate is generally creditable against Korean tax on the same income.")
         + call_box("India-Korea treaty questions", ["Royalty and FTS withholding at 10%",
                                                       "Dividend planning for Korean parents",
                                                       "Capital gains on Indian share sales",
                                                       "PE and transfer pricing for Korean groups",
                                                       "TRC, Form 41 and PAN"],
                    "the recipient, the payment type, the amounts and any plant or subsidiary.")
         + sources("Revised agreement between India and the Republic of Korea for the avoidance of double taxation (signed 18 May 2015, in force 12 September 2016); PMIndia release; SCC Online (October 2016); Business Standard (October 2016); Beacon Filing and ClearTax guides; Income Tax Department withholding tables. Dividend rate and thresholds should be confirmed against the treaty text. Checked 25 November 2026.")),
    ],
    faqs=[("What are the India-South Korea DTAA rates?", "Under the revised treaty, Indian tax on interest, royalties and fees for technical services paid to a Korean resident is capped at 10% (down from 15%), and dividends are taxed at the treaty rate, reported at 15%. Confirm the dividend rate for your shareholding against the treaty text."),
          ("When did the revised India-Korea DTAA take effect?", "It was signed on 18 May 2015, came into force on 12 September 2016, and applies in India to income from fiscal years beginning on or after 1 April 2017."),
          ("Are capital gains on Indian shares taxable for Korean residents?", "Yes. The revised treaty gives the country where the company is resident the right to tax gains on its shares, so gains on shares of Indian companies are taxable in India."),
          ("How does a Korean company claim the treaty rate in India?", "Give the Indian payer a Korean tax residency certificate, Form 41 (formerly Form 10F) and a PAN or the documents allowed instead, before tax is deducted."),
          ("Can BQP advise on the India-Korea DTAA?", "Yes. " + C)],
    related=[("india-japan-dtaa-tax-treaty-rates-dividend-interest-royalty-fts-article-12-2026.html", "India-Japan DTAA"),
             ("india-china-dtaa-tax-treaty-rates-10-percent-dividend-royalty-fts-press-note-fdi-2026.html", "India-China DTAA"),
             ("china-plus-one-india-moving-sourcing-manufacturing-to-india-foreign-company-2026.html", "China plus one in India"),
             ("what-is-dtaa.html", "What is a DTAA"),
             ("tax-residency-certificate-india-form-42-43-10fa-10fb-freelancer-youtube-2026.html", "Tax residency certificates")],
    cta_h="Paying or receiving income between India and Korea?", cta_b=C,
    keywords="India South Korea DTAA, India Korea DTAA, India Korea tax treaty, India Korea DTAA rates, India Korea DTAA royalty, India Korea capital gains, Korean company India tax",
    desc="India-South Korea DTAA (2026): revised treaty (signed 2015, in force 2016, applies from 1 April 2017) cuts interest, royalties and fees for technical services to 10%, dividends at the treaty rate (reported 15%), gains on Indian shares taxable in India; how to claim with TRC, Form 41 and PAN.",
    howto={"name": "How to apply the India-Korea treaty", "description": "For payments to a Korean resident.", "steps": [
        {"name": "Identify the income type", "text": "Dividend, interest, royalty, FTS or share gain."},
        {"name": "Apply the revised rate", "text": "10% on interest, royalties and FTS; treaty rate on dividends."},
        {"name": "Collect TRC, Form 41 and PAN", "text": "Before the Indian payer deducts tax."},
        {"name": "Review PE and transfer pricing", "text": "For engineers in India and group payments."},
        {"name": "Plan exits", "text": "Gains on Indian shares are taxable in India."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch HD complete")
