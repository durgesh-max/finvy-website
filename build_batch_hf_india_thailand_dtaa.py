# -*- coding: utf-8 -*-
"""Batch HF (25 Nov 2026): India-Thailand DTAA - revised treaty (signed 2015, reported in force 2016): dividends 10%
(down from 15%/20%), interest and royalties reported at 10%; treatment of fees for technical services reported
differently (some guides say 10%, others that there is no separate FTS article so service fees are taxable only with a
PE) - flagged; how to claim; Thai companies and NRIs in Thailand.
Demand: sweep ac95 (25 Nov 2026), all 7 markets: "india thailand dtaa", "india thailand dtaa income tax", "india thailand
dtaa agreement".
Facts (checked 25 Nov 2026): KPMG Thailand tax update (April 2016: revised agreement lowers dividend rate to 10% from 15%
or 20%; more favourable on interest and royalties); NoBroker and Beacon Filing (10% on dividends, interest, royalties; FTS
conflict); ClearTax guide. Effective date and FTS treatment caveated."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 25 November 2026."
SLUG = "india-thailand-dtaa-tax-treaty-rates-dividend-interest-royalty-10-percent-fts-2026"

C = contact("whether you are a Thai company, a Thai resident or an NRI in Thailand, the income type (dividend, interest, royalty, service fees or gains), the amounts, and whether you have a Thai TRC and PAN")
L = lambda h, t: f'<a href="{h}">{t}</a>'
PAGES = [dict(
    slug=SLUG,
    title="India-Thailand DTAA (2026): Tax Treaty Rates of 10% on Dividends, Interest and Royalties, Technical Fees and How to Claim",
    em="10% on the main streams; check how service fees are treated before you invoice.",
    kicker="/ Thai companies and NRIs in Thailand &middot; DTAA &middot; Updated 2026-11-25",
    lead=("<strong>India and Thailand revised their double tax avoidance agreement in 2015, and the new treaty is reported to have taken effect in 2016.</strong> "
          "It lowered Indian tax on dividends paid to a Thai resident to 10% (from 15% or 20%), and guides report 10% on interest and royalties too, against India&rsquo;s domestic withholding of 20% (30% on NRO interest) plus surcharge and cess. "
          "Sources differ on fees for technical services: some list a 10% rate, while others say the treaty has no separate article for them, so service fees are taxable in India only if the Thai provider has a permanent establishment. Check the treaty text before fixing the withholding rate on service invoices. "
          "Thai recipients claim treaty rates with a Thai tax residency certificate, Form 41 (formerly Form 10F) and a PAN."),
    sections=[
        ("/ Quick answers", "What Thai companies and NRIs ask.",
         ul("<strong>What is the dividend rate?</strong> 10% under the revised treaty, down from 15% or 20% under the old one.",
            "<strong>Interest and royalties?</strong> Reported at 10% each under the revised treaty.",
            "<strong>What about technical or consultancy fees?</strong> Reported differently by guides; read the treaty&rsquo;s royalty and business profits articles to see whether a fee falls within a capped rate or is taxable only with a PE.",
            "<strong>Can an NRI in Thailand reduce TDS on NRO interest?</strong> Yes, with a Thai TRC, Form 41 and PAN the bank can apply the treaty rate instead of 30% plus surcharge and cess; NRE interest is exempt anyway.",
            "<strong>From when do the revised rates apply?</strong> The revised treaty is reported to have entered into force in 2016; confirm the first applicable year against the notification.")),
        ("/ Rates at a glance", "Indian tax on payments to a Thai resident.",
         table(["Income", "India-Thailand DTAA (revised)", "Without treaty benefit"], [
             ["Dividends", "10%", "20% plus surcharge and cess"],
             ["Interest (NRO, loans)", "10% (as reported)", "30% on NRO interest, other domestic rates for loans, plus surcharge and cess"],
             ["Royalties", "10% (as reported)", "20% plus surcharge and cess"],
             ["Fees for technical services", "Check the treaty: 10% or PE-only, as reported", "20% plus surcharge and cess"],
             ["Business profits", "Taxable in India only with a permanent establishment", "Taxable if there is a business connection"]])
         + '<p>Related: ' + L("india-malaysia-dtaa-tax-treaty-rates-dividend-5-interest-royalty-fts-10-nri-2026.html", "India-Malaysia DTAA") + ', ' + L("india-singapore-tax-treaty-dtaa.html", "India-Singapore DTAA") + ' and ' + L("what-is-dtaa.html", "all India treaty guides by country") + '.</p>'),
        ("/ Claiming and planning", "Documents and credit.",
         ul("<strong>Documents:</strong> a Thai tax residency certificate from the Revenue Department, Form 41 and a PAN or the documents allowed instead; see " + L("tax-residency-certificate-india-form-42-43-10fa-10fb-freelancer-youtube-2026.html", "tax residency certificates") + ".",
            "<strong>Service contracts:</strong> confirm the treaty treatment of each fee type before invoicing, and track days spent in India to manage PE risk.",
            "<strong>Refunds:</strong> file an Indian return where TDS exceeded the treaty rate or your actual tax.",
            "<strong>Credit in Thailand:</strong> Indian tax at the treaty rate is generally creditable against Thai tax on the same income.",
            "<strong>Indian residents with Thai income</strong> claim foreign tax credit in India for Thai tax.")
         + call_box("India-Thailand treaty questions", ["Treaty rate on dividends, interest and royalties",
                                                          "Service fee treatment and PE risk",
                                                          "Thai TRC, Form 41 and PAN",
                                                          "Refunds of excess TDS",
                                                          "Foreign tax credit in India"],
                    "the recipient, the payment type and the amounts.")
         + sources("Revised agreement between India and Thailand for the avoidance of double taxation (2015); KPMG Thailand tax update (April 2016); NoBroker, Beacon Filing and ClearTax guides; Income Tax Department treaty pages. Interest, royalty and technical fee treatment and the effective date should be confirmed against the treaty text. Checked 25 November 2026.")),
    ],
    faqs=[("What are the India-Thailand DTAA rates?", "Under the revised treaty, Indian tax on dividends paid to a Thai resident is capped at 10% (down from 15% or 20%), and guides report 10% on interest and royalties. The treatment of fees for technical services is reported differently, so check the treaty text."),
          ("Are technical service fees to a Thai company taxed in India?", "Guides differ: some list a 10% treaty rate, while others say the treaty has no separate technical fees article, so such fees are taxable in India only if the Thai company has a permanent establishment here. Check the treaty's royalty and business profits articles for each contract."),
          ("How can an NRI in Thailand reduce TDS on NRO interest?", "Give the Indian bank a Thai tax residency certificate, Form 41 (formerly Form 10F) and your PAN so it can apply the treaty rate instead of 30% plus surcharge and cess, and file an Indian return to claim any excess back."),
          ("When did the revised India-Thailand DTAA take effect?", "It was revised in 2015 and is reported to have entered into force in 2016. Confirm the first year its rates apply in India against the official notification."),
          ("Can BQP advise on the India-Thailand DTAA?", "Yes. " + C)],
    related=[("india-malaysia-dtaa-tax-treaty-rates-dividend-5-interest-royalty-fts-10-nri-2026.html", "India-Malaysia DTAA"),
             ("india-singapore-tax-treaty-dtaa.html", "India-Singapore DTAA"),
             ("nri-nro-interest-tds-refund-calculator-treaty-rate-by-country-2026.html", "NRO interest TDS by country"),
             ("what-is-dtaa.html", "What is a DTAA"),
             ("tax-residency-certificate-india-form-42-43-10fa-10fb-freelancer-youtube-2026.html", "Tax residency certificates")],
    cta_h="Paying or receiving income between India and Thailand?", cta_b=C,
    keywords="India Thailand DTAA, India Thailand tax treaty, India Thailand DTAA rates, India Thailand DTAA dividend, India Thailand fees for technical services, NRI Thailand tax, Thai company India tax",
    desc="India-Thailand DTAA (2026): revised treaty (2015) caps Indian tax on dividends at 10% (from 15%/20%), interest and royalties reported at 10%; technical fee treatment reported differently; how to claim with a Thai TRC, Form 41 and PAN; NRO interest for NRIs in Thailand.",
    howto={"name": "How to apply the India-Thailand treaty", "description": "For payments to a Thai resident.", "steps": [
        {"name": "Identify the income type", "text": "Dividend, interest, royalty, service fee or business profits."},
        {"name": "Check the treaty article", "text": "Especially for technical or consultancy fees."},
        {"name": "Collect TRC, Form 41 and PAN", "text": "Before the Indian payer deducts tax."},
        {"name": "Apply the treaty or domestic rate", "text": "Whichever is lower."},
        {"name": "Claim credit or refunds", "text": "In Thailand for Indian tax; Indian return for excess TDS."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch HF complete")
