# -*- coding: utf-8 -*-
"""Batch HC (25 Nov 2026): India-Malaysia DTAA - revised treaty (signed 2012, reported effective 1 April 2013 in India)
with maximum rates of 5% on dividends, 10% on interest, 10% on royalties and 10% on fees for technical services; lower of
treaty or domestic rate; NRIs in Malaysia (NRO interest, TRC from LHDN), Malaysian companies and Indian subsidiaries;
how to claim.
Demand: sweep ac95 (25 Nov 2026), all 7 markets: "india malaysia dtaa", "india vs malaysia dtaa", "india malaysia dtaa
income tax", "india malaysia dtaa pdf".
Facts (checked 25 Nov 2026): Orbitax treaty summary, PTI (May 2012 signing), Beacon Filing, ClearTax, NoBroker, PwC
Malaysia table reference: 5% dividends, 10% interest, 10% royalties, 10% FTS; revision 2012, effective in India from
1 April 2013 per secondary guides (caveated). TRC issuer in Malaysia is the Inland Revenue Board (LHDN / HASiL)."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 25 November 2026."
SLUG = "india-malaysia-dtaa-tax-treaty-rates-dividend-5-interest-royalty-fts-10-nri-2026"

C = contact("whether you are a Malaysian company, a Malaysian resident or an NRI in Malaysia, the income type (dividend, NRO interest, royalty, technical fees or gains), the amounts, and whether you have a Malaysian TRC and PAN")
L = lambda h, t: f'<a href="{h}">{t}</a>'
PAGES = [dict(
    slug=SLUG,
    title="India-Malaysia DTAA (2026): Tax Treaty Rates of 5% on Dividends and 10% on Interest, Royalties and Technical Fees, for NRIs and Companies",
    em="one of India's lower dividend rates, if you hold a Malaysian TRC.",
    kicker="/ NRIs in Malaysia and Malaysian companies &middot; DTAA &middot; Updated 2026-11-25",
    lead=("<strong>The revised India-Malaysia double tax avoidance agreement, signed in 2012, caps Indian tax on dividends paid to a Malaysian resident at 5% and on interest, royalties and fees for technical services at 10%, against India&rsquo;s domestic withholding of 20% (30% on NRO interest) plus surcharge and cess.</strong> "
          "Treaty guides report that it took effect in India from 1 April 2013. "
          "Malaysian residents, including NRIs working in Malaysia, claim the treaty rate by giving the Indian payer a tax residency certificate from Malaysia&rsquo;s Inland Revenue Board, Form 41 (formerly Form 10F) and a PAN; where the domestic rate is lower, it applies instead."),
    sections=[
        ("/ Quick answers", "What NRIs and Malaysian companies ask.",
         ul("<strong>What is the dividend rate?</strong> 5% of the gross dividend for a Malaysian resident beneficial owner, one of the lower dividend rates among India&rsquo;s treaties.",
            "<strong>What about NRO interest?</strong> 10% under the treaty with a Malaysian TRC and Form 41, instead of 30% plus surcharge and cess; NRE interest is exempt in India anyway.",
            "<strong>Royalties and technical fees?</strong> 10% of the gross amount each; check the treaty&rsquo;s definitions for each contract.",
            "<strong>Where do I get a TRC in Malaysia?</strong> From the Inland Revenue Board of Malaysia (LHDN, also known as HASiL), for the year the income is paid.",
            "<strong>Does rent or property gain get relief?</strong> Usually not: Indian rent and gains on Indian property stay taxable in India.")),
        ("/ Rates at a glance", "Indian tax on payments to a Malaysian resident.",
         table(["Income", "India-Malaysia DTAA", "Without treaty benefit"], [
             ["Dividends", "5%", "20% plus surcharge and cess"],
             ["Interest (NRO, loans)", "10%", "30% on NRO interest, other domestic rates for loans, plus surcharge and cess"],
             ["Royalties", "10%", "20% plus surcharge and cess"],
             ["Fees for technical services", "10%", "20% plus surcharge and cess"],
             ["Business profits", "Taxable in India only with a permanent establishment", "Taxable if there is a business connection"]])
         + '<p>Related: ' + L("india-singapore-tax-treaty-dtaa.html", "India-Singapore DTAA") + ', ' + L("nri-nro-interest-tds-refund-calculator-treaty-rate-by-country-2026.html", "NRO interest TDS by country") + ' and ' + L("what-is-dtaa.html", "what a DTAA is") + '.</p>'),
        ("/ What to do", "Claims, refunds and planning.",
         ul("<strong>Get a Malaysian TRC</strong> and give it to your Indian bank or payer with Form 41 and your PAN; see " + L("tax-residency-certificate-india-form-42-43-10fa-10fb-freelancer-youtube-2026.html", "tax residency certificates") + ".",
            "<strong>Check your Indian residence</strong> each year by days in India, and whether Malaysia taxes you, before relying on non-resident status.",
            "<strong>Claim refunds</strong> by filing an Indian return where TDS exceeded the treaty rate or your actual tax.",
            "<strong>Malaysian parent companies</strong> can plan Indian dividends at 5% and check credit in Malaysia.",
            "<strong>Indian residents with Malaysian income</strong> claim foreign tax credit in India for Malaysian tax.")
         + call_box("India-Malaysia treaty questions", ["Treaty rate on dividends and NRO interest",
                                                         "Malaysian TRC, Form 41 and PAN",
                                                         "Refunds of excess TDS",
                                                         "Malaysian companies with Indian subsidiaries",
                                                         "Foreign tax credit in India"],
                    "the recipient, the income type, the amounts and the documents.")
         + sources("Agreement between India and Malaysia for the avoidance of double taxation (revised, signed 2012); Orbitax treaty summary; PTI report on the 2012 signing; Beacon Filing, ClearTax and NoBroker guides; PwC Malaysia treaty withholding table; Inland Revenue Board of Malaysia treaty pages. Effective date and definitions should be confirmed against the treaty text. Checked 25 November 2026.")),
    ],
    faqs=[("What are the India-Malaysia DTAA rates?", "Indian tax on payments to a Malaysian resident is capped at 5% on dividends and 10% on interest, royalties and fees for technical services. Without the treaty, withholding is usually 20% (30% on NRO interest) plus surcharge and cess."),
          ("How can an NRI in Malaysia reduce TDS on NRO interest?", "Give the Indian bank a tax residency certificate from Malaysia's Inland Revenue Board, Form 41 (formerly Form 10F) and your PAN so it can deduct 10% under the treaty instead of 30% plus surcharge and cess, and file an Indian return to claim any excess back."),
          ("When did the revised India-Malaysia DTAA take effect?", "The revised treaty was signed in 2012; treaty guides report it took effect in India from 1 April 2013. Confirm against the official notification for older years."),
          ("Is NRE interest taxable for an NRI in Malaysia?", "No. Interest on NRE accounts is exempt in India while you are a non-resident, so the treaty is not needed for it."),
          ("Can BQP advise on the India-Malaysia DTAA?", "Yes. " + C)],
    related=[("india-singapore-tax-treaty-dtaa.html", "India-Singapore DTAA"),
             ("nri-nro-interest-tds-refund-calculator-treaty-rate-by-country-2026.html", "NRO interest TDS by country"),
             ("india-kuwait-dtaa-nri-tax-treaty-rates-10-percent-trc-deemed-resident-nro-2026.html", "India-Kuwait DTAA for NRIs"),
             ("what-is-dtaa.html", "What is a DTAA"),
             ("tax-residency-certificate-india-form-42-43-10fa-10fb-freelancer-youtube-2026.html", "Tax residency certificates")],
    cta_h="Living in Malaysia with income in India?", cta_b=C,
    keywords="India Malaysia DTAA, India Malaysia tax treaty, India Malaysia DTAA rates, India vs Malaysia DTAA, NRI Malaysia tax, Malaysia TRC LHDN, NRO interest TDS Malaysia",
    desc="India-Malaysia DTAA (2026): 5% on dividends and 10% on interest, royalties and fees for technical services; NRIs in Malaysia cut NRO interest TDS from 30% to 10% with a Malaysian TRC (LHDN), Form 41 and PAN; NRE interest exempt; revised treaty signed 2012.",
    howto={"name": "How to claim the India-Malaysia treaty rate", "description": "For NRO interest and dividends.", "steps": [
        {"name": "Get a Malaysian TRC", "text": "From the Inland Revenue Board for the relevant year."},
        {"name": "Submit Form 41 and PAN", "text": "To the Indian bank or payer."},
        {"name": "Check residence", "text": "Days in India and tax status in Malaysia."},
        {"name": "Track TDS", "text": "In Form 26AS and AIS."},
        {"name": "File for refunds", "text": "Where TDS exceeded the treaty rate."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch HC complete")
