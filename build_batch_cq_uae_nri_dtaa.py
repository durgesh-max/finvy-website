# -*- coding: utf-8 -*-
"""Batch CQ (15 Nov 2026): India-UAE tax treaty for NRIs living in the UAE (individual side).
Demand: Search Console shows "india uae dtaa", "india uae tax treaty", "dubai india tax treaty" with the existing
corporate-focused page ranking around 60; UAE is a priority market.
Facts: India-UAE DTAA (1992, protocols 2007 and 2012). Article 4 as amended: an individual is resident of the UAE if
present there for at least 183 days in the calendar year concerned. Article 10 dividends capped at 10%. Article 11
interest: 5% if beneficially owned by a bank or similar financial institution, 12.5% in other cases (government/central
bank exempt). Article 6/13(1): income and gains from immovable property in India taxable in India. Article 13(4): gains
on shares of an Indian company may be taxed in India. Article 13(5): gains on other property taxable only in the state
of residence; Delhi ITAT (Saket Kanoi, October 2024) and Cochin ITAT (2019) held mutual fund units are not shares, so
gains of a UAE resident on Indian mutual fund units are not taxable in India (tribunal level; revenue argued 13(4)).
Domestic: NRO interest and other income of non-residents subject to withholding under section 393(2) of the
Income-tax Act, 2025 (formerly 195) at 30% plus surcharge and cess for interest; dividends 20%; listed equity gains
STCG 20%, LTCG 12.5% above INR 1.25 lakh; NRE interest exempt. Treaty claims need TRC, Form 41 (formerly 10F), PAN.
UAE: no federal personal income tax on salaries; TRC issued by the Federal Tax Authority under Cabinet Decision 85 of
2022 (183-day test, and a 90-day test with conditions). Sources: Income Tax Department DTAA text; taxguru (Delhi
ITAT Saket Kanoi summary); EY tax alert and Gulf News on UAE residency (checked 15 Nov 2026)."""
from urllib.parse import quote
from build_lib import page, write_page

UPDATED = "Last updated: 15 November 2026."


def wa(t):
    return "https://wa.me/917801887130?text=" + quote(t)


def ul(*x):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in x) + "</ul>"


def table(head, rows):
    return ("<table><thead><tr>" + "".join(f"<th>{h}</th>" for h in head) + "</tr></thead><tbody>"
            + "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows) + "</tbody></table>")


CONTACT = ("WhatsApp +91 78018 87130 or email durgesh@bharatquantumprospera.com with your days in the UAE and India for the last two years and the Indian income you have (NRO interest, rent, mutual funds, shares, property sale). "
           "We reply the same working day with the treaty position, what your bank or fund house should deduct and how to claim any refund.")
SLUG = "india-uae-dtaa-for-nris-dubai-nro-interest-mutual-funds-property-trc-2026"
BOX = (f'<div style="border:1px solid var(--line);border-left:4px solid #C2312A;border-radius:10px;padding:16px 18px;margin:18px 0;background:var(--bg-soft)">'
       f'<p style="margin:0 0 8px;font-weight:600">Most Dubai NRIs overpay Indian tax by default.</p>'
       f'<p style="margin:0">Banks deduct 30%+ on NRO interest and fund houses deduct tax on redemptions unless you hand over a UAE tax residency certificate, Form 41 and a treaty declaration. The excess comes back only through an Indian return. '
       f'<a href="{wa("Hi Durgesh, I live in the UAE and have Indian income. Can you help me claim India-UAE treaty benefits?")}" target="_blank" rel="noopener"><strong>WhatsApp CA Durgesh Chavda</strong></a>.</p></div>')

PAGES = [dict(
    slug=SLUG,
    title="India-UAE DTAA for NRIs in Dubai and the UAE (2026): Tax on NRO Interest, Mutual Funds, Shares, Rent and Property, and the UAE Tax Residency Certificate",
    em="the treaty cuts tax on interest and dividends; property and rent stay taxable in India.",
    kicker="/ NRI &middot; UAE &middot; Tax treaty &middot; Updated 2026-11-15",
    lead=("For an NRI living in the UAE, the India-UAE tax treaty mainly helps on <strong>interest and dividends</strong>: Indian tax on <strong>NRO and other interest is capped at 12.5%</strong> (against 30% plus surcharge and cess under Indian law) and on <strong>dividends at 10%</strong> (against 20%). "
          "<strong>Rent and gains on Indian property stay fully taxable in India</strong>, and gains on <strong>shares of Indian companies</strong> remain taxable in India at Indian rates. Gains on <strong>Indian mutual fund units</strong> have been held <strong>not taxable in India</strong> for UAE residents by tax tribunals (Delhi ITAT, October 2024), because units are not shares. "
          "To use the treaty you need a <strong>UAE tax residency certificate</strong>, <strong>Form 41</strong> (formerly 10F) and your PAN; the treaty treats you as UAE resident if you were in the UAE for <strong>at least 183 days in the calendar year</strong>. Because the UAE has no personal income tax on salaries, whatever India collects is the final cost: there is no foreign tax credit to offset it."),
    sections=[
        ("/ Income by income", "What India can tax, and at what rate.",
         table(["Indian income", "Indian law (non-resident)", "Under the India-UAE treaty"], [
             ["NRO savings and fixed deposit interest", "30% withholding plus surcharge and cess", "Capped at 12.5% (Article 11); 5% if the lender is a bank or financial institution"],
             ["NRE and FCNR interest", "Exempt for non-residents", "Not needed: already exempt"],
             ["Dividends from Indian companies", "20% plus surcharge and cess", "Capped at 10% (Article 10)"],
             ["Indian mutual fund units (sale or redemption)", "Taxed as capital gains; tax deducted at source by the fund house", "Delhi ITAT (Oct 2024) and Cochin ITAT (2019): units are not shares, so taxable only in the UAE under Article 13(5); claim the refund in your Indian return"],
             ["Listed shares of Indian companies", "Short-term 20%; long-term 12.5% above INR 1.25 lakh a year", "Taxable in India (Article 13(4)); no treaty relief"],
             ["Rent from Indian property", "Taxable in India; tenant withholds tax", "Taxable in India (Article 6); no treaty relief"],
             ["Sale of Indian property", "Long-term gains 12.5%; tax deducted at source on the sale", "Taxable in India (Article 13(1)); a lower deduction certificate cuts the TDS to the real tax"],
             ["Salary for work done in the UAE", "Not taxable in India for a non-resident", "Not needed; days you work from India are taxable in India"]])
         + BOX),
        ("/ Residence", "Who counts as a UAE resident.",
         ul("<strong>Treaty test (Article 4):</strong> an individual is a UAE resident for the treaty if present in the UAE for at least 183 days in the calendar year concerned. Note that India's tax year runs April to March, so check both periods.",
            "<strong>UAE tax residency certificate:</strong> issued online by the Federal Tax Authority under Cabinet Decision No. 85 of 2022 (in force from 1 March 2023), on a 183-day presence test or a 90-day test with additional conditions; a tenancy contract or title deed and an entry-exit report are usually needed.",
            "<strong>India comes first:</strong> you must also be non-resident (or RNOR) under Indian law: under 182 days in India, and watch the 120-day rule if your Indian income exceeds INR 15 lakh. Indian citizens with Indian income above INR 15 lakh who are not liable to tax in any country can be deemed resident; see <a href=\"dubai-uae-nri-indian-income-above-15-lakh-deemed-resident-india-tax-2026.html\">deemed residence for UAE-based Indians</a> and the <a href=\"residential-status-calculator-india-nri-rnor-section-6.html\">residential status calculator</a>.")),
        ("/ How to claim it", "Paperwork that stops the over-deduction.",
         ul("Get your UAE tax residency certificate for the relevant year.",
            "File Form 41 (formerly Form 10F) electronically on the Indian income-tax portal; a PAN-less route exists, see <a href=\"how-to-file-form-10f-electronic-india-nri-no-pan-step-by-step.html\">Form 10F without PAN</a>.",
            "Give your bank the TRC, Form 41, a no-permanent-establishment declaration and a treaty declaration so NRO interest is taxed at 12.5%; give the same to fund houses and the company registrar for mutual funds and dividends.",
            "If tax was already deducted at the higher rate, file your Indian return (ITR-2) and claim the refund; keep the TRC and day-count records for the assessment.",
            "Selling property? Apply for a lower deduction certificate (Form 128, formerly 13) before the sale so TDS is based on the gain, not the sale price.")
         + '<p>Related: <a href="india-uae-tax-treaty-dtaa.html">India-UAE treaty for companies and Dubai holding structures</a> &middot; <a href="nri-mutual-funds-india-tax.html">NRI mutual funds and tax</a> &middot; <a href="nre-nro-fcnr-account-tax-rules.html">NRE vs NRO vs FCNR</a> &middot; <a href="nri-property-tds-ldc-calculator.html">NRI property TDS calculator</a> &middot; <a href="returning-from-uae-dubai-to-india-gratuity-uae-bank-account-tax-2026.html">returning from the UAE</a> &middot; <a href="indian-ca-for-clients-in-uae-gulf.html">CA for clients in the UAE and Gulf</a>.</p>'
         + f'<p><strong>Sources:</strong> India-UAE Double Taxation Avoidance Agreement (1992) as amended by the 2007 and 2012 protocols, Articles 4, 6, 10, 11 and 13 (Income Tax Department treaty text); Income-tax Act, 2025, section 393(2); Delhi ITAT, Saket Kanoi (October 2024) and Cochin ITAT (2019) on mutual fund units; UAE Cabinet Decision No. 85 of 2022 and Ministerial Decision No. 27 of 2023 on tax residency. Secondary summaries checked 15 November 2026: taxguru, EY tax alert, Gulf News. <em>{UPDATED}</em> Tribunal rulings can be challenged by the tax department; general information, not advice for your situation.</p>'),
    ],
    faqs=[("Does the India-UAE DTAA reduce tax on NRO interest?", "Yes. Indian tax on interest paid to a UAE resident is capped at 12.5% (5% for banks), against 30% plus surcharge and cess under Indian law. Give your bank a UAE tax residency certificate, Form 41 (formerly 10F) and a treaty declaration."),
          ("Are Indian mutual fund gains taxable for NRIs living in the UAE?", "Tax tribunals (Delhi ITAT in October 2024, Cochin ITAT in 2019) have held that mutual fund units are not shares, so gains of a UAE resident are taxable only in the UAE under Article 13(5) of the treaty, which means no tax in practice. Fund houses usually still deduct tax, so the refund is claimed in the Indian return. The tax department can contest the position."),
          ("Is rent or a property sale in India taxable for a Dubai NRI?", "Yes. Income and gains from Indian immovable property are taxable in India under the treaty. Long-term gains on property are taxed at 12.5%, and a lower deduction certificate can reduce the TDS on the sale to the actual tax."),
          ("Are gains on Indian shares taxable for UAE residents?", "Yes. Gains on shares of Indian companies may be taxed in India under Article 13(4), at Indian rates: 20% short-term and 12.5% long-term above INR 1.25 lakh a year for listed equity."),
          ("How many days must I spend in the UAE to use the treaty?", "The treaty treats an individual as UAE resident if present in the UAE for at least 183 days in the calendar year. The UAE tax residency certificate is issued on the UAE's own tests (183 days, or 90 days with conditions). You must also be non-resident or RNOR under Indian law."),
          ("Can I claim foreign tax credit in the UAE for Indian tax?", "No. The UAE does not levy personal income tax on individuals' salaries or investment income, so tax paid in India is a final cost. That is why reducing Indian withholding through the treaty matters."),
          ("Can BQP handle this for me?", "Yes. " + CONTACT)],
    related=[("india-uae-tax-treaty-dtaa.html", "India-UAE treaty for companies"), ("nri-mutual-funds-india-tax.html", "NRI mutual funds and tax"),
             ("dubai-uae-nri-indian-income-above-15-lakh-deemed-resident-india-tax-2026.html", "Deemed residence for UAE-based Indians")],
    cta_h="Living in the UAE with income in India?", cta_b=CONTACT,
    keywords="India UAE DTAA for NRI, India UAE tax treaty NRI, Dubai India tax treaty, NRO interest tax UAE resident 12.5%, mutual fund capital gains UAE NRI not taxable, India UAE DTAA article 13(5), UAE tax residency certificate NRI, Form 10F UAE NRI, NRI Dubai tax on Indian income 2026",
    desc="India-UAE DTAA for NRIs in Dubai and the UAE (2026): NRO interest capped at 12.5% (vs 30%+), dividends 10%, mutual fund gains held not taxable in India (Delhi ITAT 2024), shares, rent and property taxable in India, the 183-day test, UAE tax residency certificate and Form 41.",
    howto={"name": "How a UAE-based NRI claims India-UAE treaty benefits", "description": "Steps to stop excess Indian tax deduction.", "steps": [
        {"name": "Check residence", "text": "Confirm 183+ days in the UAE in the calendar year and non-resident status in India."},
        {"name": "Get the UAE TRC", "text": "Apply to the Federal Tax Authority for the tax residency certificate."},
        {"name": "File Form 41", "text": "File Form 41 (formerly 10F) on the Indian income-tax portal."},
        {"name": "Submit to payers", "text": "Give the TRC, Form 41 and treaty declarations to your bank, fund houses and registrars."},
        {"name": "Claim refunds", "text": "File the Indian return to recover tax deducted above the treaty rate."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch CQ complete")
