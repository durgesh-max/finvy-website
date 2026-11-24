# -*- coding: utf-8 -*-
"""Batch HA (25 Nov 2026): India-Kuwait DTAA for NRIs and companies - 10% caps on dividends, interest, royalties and
fees for technical services; lower of treaty or domestic rate; Kuwait has no personal income tax, so NRIs in Kuwait need
a Kuwaiti TRC to claim treaty rates and should watch India's deemed-residence rule for Indian citizens with Indian income
above INR 15 lakh who are not liable to tax elsewhere; NRO interest and rent planning; how to claim.
Demand: sweep ac94 (24 Nov 2026), all 7 markets: "india kuwait dtaa", "india kuwait dtaa rates", "dtaa between india and
kuwait".
Facts (checked 25 Nov 2026): Beacon Filing, calcguru (September 2026), TaxGuru, BCAS referencer: dividends, interest,
royalties and FTS capped at 10% (no shareholding tiers); lower of treaty and domestic rate under section 90(2) principle.
Deemed residence rule and NRO TDS as on site pages (dubai-uae deemed resident page, NRO interest pages). Form 41 per the
site's old-vs-new form number mapping."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 25 November 2026."
SLUG = "india-kuwait-dtaa-nri-tax-treaty-rates-10-percent-trc-deemed-resident-nro-2026"

C = contact("how long you have lived in Kuwait and your days in India, your Indian income (interest, rent, dividends, gains), whether you can get a Kuwaiti tax residency certificate, and any business or company payments involved")
L = lambda h, t: f'<a href="{h}">{t}</a>'
PAGES = [dict(
    slug=SLUG,
    title="India-Kuwait DTAA (2026): Tax Treaty Rates of 10%, TRC for NRIs in Kuwait, Deemed Residence and NRO Interest",
    em="10% on paper, but NRIs in Kuwait must prove treaty residence and watch the deemed-residence rule.",
    kicker="/ NRIs in Kuwait and Kuwaiti companies &middot; DTAA &middot; Updated 2026-11-25",
    lead=("<strong>The India-Kuwait double tax avoidance agreement caps Indian tax on dividends, interest, royalties and fees for technical services paid to a Kuwaiti resident at 10%, about half India&rsquo;s domestic withholding of 20% plus surcharge and cess, with no shareholding tiers.</strong> "
          "For the large Indian community in Kuwait, the catch is proof: the treaty rate needs a Kuwaiti tax residency certificate and Form 41 (formerly Form 10F), and because Kuwait has no personal income tax, an Indian citizen with Indian income above INR 15 lakh who is not liable to tax anywhere can be treated as resident in India under the deemed-residence rule. "
          "In every case the lower of the treaty rate and the Income-tax Act rate applies."),
    sections=[
        ("/ Quick answers", "What NRIs in Kuwait ask.",
         ul("<strong>What TDS applies to my NRO interest?</strong> 30% plus surcharge and cess by default; with a Kuwaiti TRC and Form 41 the bank can apply the 10% treaty rate.",
            "<strong>Is NRE interest taxed?</strong> No. NRE interest is exempt in India while you are a non-resident, so the treaty is not needed for it.",
            "<strong>Can I get a tax residency certificate in Kuwait?</strong> Kuwait issues residency certificates for treaty purposes through its tax authorities; apply well before the Indian payment date, since requirements and timing vary.",
            "<strong>Does the deemed-residence rule affect me?</strong> Possibly: an Indian citizen with Indian income (excluding foreign sources) above INR 15 lakh who is not liable to tax in any country can be deemed resident (RNOR) in India; see " + L("dubai-uae-nri-indian-income-above-15-lakh-deemed-resident-india-tax-2026.html", "deemed residence for Gulf NRIs") + ".",
            "<strong>What about rent and property sales?</strong> Rent and capital gains on Indian property remain taxable in India; the treaty does not usually reduce them.")),
        ("/ Rates at a glance", "Indian tax on payments to a Kuwaiti resident.",
         table(["Income", "India-Kuwait DTAA", "Without treaty benefit"], [
             ["Dividends", "10%", "20% plus surcharge and cess"],
             ["Interest (NRO, loans)", "10%", "30% on NRO interest, other domestic rates for loans, plus surcharge and cess"],
             ["Royalties", "10%", "20% plus surcharge and cess"],
             ["Fees for technical services", "10%", "20% plus surcharge and cess"],
             ["Rent and property gains", "Taxable in India under domestic law", "Same"]])
         + '<p>Related: ' + L("nri-nro-interest-tds-refund-calculator-treaty-rate-by-country-2026.html", "NRO interest TDS and treaty rates by country") + ' and ' + L("india-qatar-dtaa-2026-new-tax-treaty-rates-nri-qatar-investment-india.html", "India-Qatar DTAA") + '.</p>'),
        ("/ What to do", "A short checklist for NRIs in Kuwait.",
         ul("<strong>Get a Kuwaiti TRC</strong> for the relevant year and give it to your Indian bank or payer with Form 41 and your PAN.",
            "<strong>Count your days in India</strong> and your Indian income, to check non-resident status and the deemed-residence rule.",
            "<strong>Keep NRE and NRO separate:</strong> foreign earnings in NRE (tax-free interest), Indian income in NRO.",
            "<strong>File an Indian return</strong> where TDS was deducted above your actual tax, to claim a refund.",
            "<strong>Report correctly</strong> if you become resident again on return, including your Kuwaiti end-of-service benefits and accounts.")
         + call_box("India-Kuwait tax questions", ["Treaty rate on NRO interest and dividends",
                                                     "TRC, Form 41 and PAN",
                                                     "Deemed residence and RNOR checks",
                                                     "Refunds of excess TDS",
                                                     "Returning to India from Kuwait"],
                    "your days in India, your Indian income and your Kuwait documents.")
         + sources("Agreement between India and Kuwait for the avoidance of double taxation; rates as reported by Beacon Filing, calcguru (September 2026), TaxGuru and the BCAS referencer; Income-tax Act principles on the lower of treaty or domestic rate and deemed residence for Indian citizens, as explained on the linked site pages. Confirm the TRC process with the Kuwaiti authorities. Checked 25 November 2026.")),
    ],
    faqs=[("What are the India-Kuwait DTAA rates?", "Dividends, interest, royalties and fees for technical services paid by an Indian payer to a Kuwaiti resident are taxed in India at up to 10%, with no shareholding tiers. If the domestic rate is lower, the domestic rate applies."),
          ("How can an NRI in Kuwait reduce TDS on NRO interest?", "Give the Indian bank a Kuwaiti tax residency certificate, Form 41 (formerly Form 10F) and your PAN so it can deduct 10% under the treaty instead of 30% plus surcharge and cess, and file an Indian return to claim any excess back."),
          ("Does Kuwait having no income tax affect my Indian residence?", "It can. An Indian citizen whose Indian income (excluding foreign sources) is above INR 15 lakh and who is not liable to tax in any country can be deemed resident in India (as RNOR), so check your income and your status each year."),
          ("Is NRE interest taxable for an NRI in Kuwait?", "No. Interest on NRE accounts is exempt in India while you are a non-resident, so the treaty is not needed for it."),
          ("Can BQP advise NRIs in Kuwait?", "Yes. " + C)],
    related=[("dubai-uae-nri-indian-income-above-15-lakh-deemed-resident-india-tax-2026.html", "Deemed residence for Gulf NRIs"),
             ("nri-nro-interest-tds-refund-calculator-treaty-rate-by-country-2026.html", "NRO interest TDS by country"),
             ("india-qatar-dtaa-2026-new-tax-treaty-rates-nri-qatar-investment-india.html", "India-Qatar DTAA"),
             ("nre-nro-fcnr-account-tax-rules.html", "NRE, NRO and FCNR rules"),
             ("what-is-dtaa.html", "What is a DTAA")],
    cta_h="Living in Kuwait with income in India?", cta_b=C,
    keywords="India Kuwait DTAA, India Kuwait tax treaty, DTAA between India and Kuwait, NRI Kuwait tax, Kuwait tax residency certificate, NRO interest TDS Kuwait, deemed resident Kuwait NRI",
    desc="India-Kuwait DTAA (2026): 10% on dividends, interest, royalties and fees for technical services; NRIs in Kuwait need a Kuwaiti TRC and Form 41 to cut NRO interest TDS from 30% to 10%; deemed-residence rule for Indian income above INR 15 lakh; NRE interest exempt.",
    howto={"name": "How an NRI in Kuwait claims the treaty rate", "description": "For NRO interest and dividends.", "steps": [
        {"name": "Get a Kuwaiti TRC", "text": "For the year the income is paid."},
        {"name": "Submit Form 41 and PAN", "text": "To the Indian bank or payer."},
        {"name": "Check residence", "text": "Days in India and the deemed-residence rule."},
        {"name": "Track TDS", "text": "In Form 26AS and AIS."},
        {"name": "File for refunds", "text": "Where TDS exceeded your actual tax."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch HA complete")
