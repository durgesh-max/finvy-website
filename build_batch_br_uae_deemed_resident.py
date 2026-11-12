# -*- coding: utf-8 -*-
"""Batch BR (12 Nov 2026): Dubai / UAE / Gulf NRIs with Indian income above INR 15 lakh - deemed resident rule.
Facts: an Indian citizen whose total income, other than income from foreign sources, exceeds INR 15 lakh and who is not
liable to tax in any other country by reason of domicile or residence is deemed resident in India (section 6(1A) of the
1961 Act; section 6(7) of the Income-tax Act, 2025 from tax year 2026-27); a deemed resident is resident but not
ordinarily resident, so income from foreign sources is not taxed unless derived from a business controlled in or a
profession set up in India; CBDT press release (2 February 2020) stated the provision is not meant to tax bona fide
workers' income earned abroad. Visitor rule: a citizen or person of Indian origin visiting India with Indian income above
INR 15 lakh is resident if in India 120 days or more in the year and 365 days or more in the four preceding years, and then
RNOR. The UAE levies no personal income tax. FEMA residence is a separate test. Schedule FA does not apply to RNOR."""
from urllib.parse import quote
from build_lib import page, write_page

UPDATED = "Last updated: 12 November 2026."


def wa(t):
    return "https://wa.me/917801887130?text=" + quote(t)


def ul(*x):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in x) + "</ul>"


def table(head, rows):
    return ("<table><thead><tr>" + "".join(f"<th>{h}</th>" for h in head) + "</tr></thead><tbody>"
            + "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows) + "</tbody></table>")


CONTACT = ("WhatsApp +91 78018 87130 or email durgesh@bharatquantumprospera.com with your Indian income for the year (rent, interest, capital gains, salary) and your days in India for the last five years. "
           "We reply the same working day with your status and a fixed-scope quote.")
SLUG = "dubai-uae-nri-indian-income-above-15-lakh-deemed-resident-india-tax-2026"
BOX = (f'<div style="border:1px solid var(--line);border-left:4px solid #C2312A;border-radius:10px;padding:16px 18px;margin:18px 0;background:var(--bg-soft)">'
       f'<p style="margin:0 0 8px;font-weight:600">Selling a flat or shares in India this year?</p>'
       f'<p style="margin:0">One large capital gain can take your Indian income above INR 15 lakh and change your status for that year. Check before you file: '
       f'<a href="residential-status-calculator-india-nri-rnor-section-6.html"><strong>residential status calculator</strong></a> &middot; '
       f'<a href="{wa("Hi Durgesh, I live in the UAE and my Indian income may cross INR 15 lakh. Am I a deemed resident?")}" target="_blank" rel="noopener"><strong>WhatsApp CA Durgesh Chavda</strong></a>.</p></div>')

PAGES = [dict(
    slug=SLUG,
    title="Living in Dubai With Indian Income Above INR 15 Lakh? The Deemed Resident Rule Explained (2026)",
    em="no UAE tax can make you an Indian resident on paper.",
    kicker="/ UAE &amp; Gulf NRIs &middot; Residential status &middot; Updated 2026-11-12",
    lead=("If you are an Indian citizen living in the UAE (or another zero-tax country such as Qatar, Bahrain or Oman), and your income from Indian sources exceeds INR 15 lakh in a year, Indian law can treat you as a <strong>deemed resident</strong> even if you spent no days in India, because you are not liable to tax in any other country. "
          "The rule is section 6(1A) of the 1961 Act, carried into section 6(7) of the Income-tax Act, 2025. "
          "The impact is narrower than it sounds: a deemed resident is resident but not ordinarily resident (RNOR), so your UAE salary and other foreign income stay outside Indian tax. What changes is your status in the return, and the planning around big Indian gains."),
    sections=[
        ("/ Does it apply to you?", "Three conditions, all needed.",
         table(["Test", "Meaning", "Typical UAE NRI"], [
             ["Indian citizen", "The rule does not apply to foreign citizens (OCI holders with a foreign passport)", "Yes, if you hold an Indian passport"],
             ["Income other than from foreign sources above INR 15 lakh", "Indian rent, interest, dividends, capital gains, Indian salary; foreign income is excluded", "Often crossed in the year a flat or shares are sold"],
             ["Not liable to tax in any other country by reason of residence or domicile", "Aimed at zero-tax jurisdictions", "The UAE has no personal income tax; get advice on whether your case is covered"]])
         + '<p>If you also visit India: with Indian income above INR 15 lakh, 120 days or more in India in the year plus 365 days in the previous four years makes you resident, and again RNOR.</p>'
         + BOX),
        ("/ What changes if you are a deemed resident", "And what does not.",
         ul("<strong>Your UAE salary and foreign income:</strong> not taxed in India, because a deemed resident is RNOR (unless the income comes from a business controlled in India or a profession set up in India). CBDT's February 2020 press release said the rule is not meant to tax bona fide workers abroad.",
            "<strong>Your Indian income:</strong> taxed as before, in the return filed as resident (RNOR) instead of non-resident.",
            "<strong>Schedule FA:</strong> not required for RNOR, so your UAE accounts do not need listing for that year.",
            "<strong>FEMA status:</strong> separate from income tax. Your NRE and NRO accounts depend on FEMA residence, not on this rule.",
            "<strong>TDS:</strong> buyers and banks may still deduct tax at non-resident rates; claim the difference as a refund in your return."))
        ,
        ("/ Plan around it", "Where it matters most.",
         ul("<strong>Property or share sales:</strong> spread large sales across years where possible, and check the INR 15 lakh test for each year. See <a href=\"nri-selling-indian-property-capital-gains.html\">NRIs selling property in India</a> and <a href=\"buying-property-from-nri-no-tan-form-141-from-1-october-2026.html\">the TAN-free TDS route for buyers</a>.",
            "<strong>Count your days</strong> if you visit often; the 120-day visitor rule and the deemed resident rule are separate tests.",
            "<strong>Moving back later?</strong> RNOR years are valuable; see <a href=\"returning-from-uae-dubai-to-india-gratuity-uae-bank-account-tax-2026.html\">returning from the UAE</a>.",
            "<strong>UAE property and FAST-DS:</strong> separate issue, for people already resident and ordinarily resident in India. See <a href=\"dubai-uae-property-not-disclosed-india-income-tax-nudge-fast-ds-2026.html\">the UAE property nudge</a>.")
         + f'<p><strong>Sources:</strong> Income-tax Act, 1961, section 6(1A) and 6(6); Income-tax Act, 2025, section 6; CBDT press release of 2 February 2020 on the deemed residence provision. <em>{UPDATED}</em> General information, not advice for your situation.</p>'),
    ],
    faqs=[("I live in Dubai. Can India treat me as a resident?", "Yes, if you are an Indian citizen, your income from Indian sources exceeds INR 15 lakh in the year, and you are not liable to tax in any other country by reason of residence or domicile. You are then a deemed resident, classed as resident but not ordinarily resident."),
          ("Will India tax my UAE salary if I am a deemed resident?", "No. A deemed resident is RNOR, and foreign income is not taxed unless it comes from a business controlled in India or a profession set up in India. CBDT said in February 2020 that the rule is not meant to tax bona fide workers abroad."),
          ("Which section is it under the new Act?", "Section 6(1A) of the 1961 Act, carried into section 6(7) of the Income-tax Act, 2025, which applies from tax year 2026-27."),
          ("Does it affect my NRE account?", "No. NRE and NRO accounts follow FEMA residence, which is a separate test from income-tax residence."),
          ("What counts towards INR 15 lakh?", "Income other than from foreign sources: Indian rent, interest, dividends, capital gains and any Indian salary. A large property or share sale in India is the most common trigger."),
          ("Can BQP check my status?", "Yes. " + CONTACT)],
    related=[("residential-status-calculator-india-nri-rnor-section-6.html", "Residential status calculator"),
             ("nri-residential-status-rnor-india.html", "NRI residential status and RNOR"),
             ("returning-from-uae-dubai-to-india-gratuity-uae-bank-account-tax-2026.html", "Returning from the UAE")],
    cta_h="UAE NRI with Indian income above INR 15 lakh?", cta_b=CONTACT,
    keywords="deemed resident UAE NRI, Dubai NRI 15 lakh rule, section 6(1A) deemed resident, section 6(7) Income-tax Act 2025, NRI in Gulf deemed resident India, zero tax country NRI India tax, UAE NRI RNOR",
    desc="Indian citizen living in Dubai or the UAE with Indian income above INR 15 lakh? The deemed resident rule (section 6(1A), now section 6(7) of the Income-tax Act, 2025) makes you RNOR: UAE salary stays outside Indian tax, but your filing status changes. Who it hits, what changes and how to plan.",
    howto={"name": "How a UAE NRI checks the deemed resident rule", "description": "Steps for Indian citizens living in zero-tax countries.", "steps": [
        {"name": "Add up Indian income", "text": "Total Indian rent, interest, dividends, capital gains and Indian salary for the year."},
        {"name": "Compare with INR 15 lakh", "text": "Above INR 15 lakh, the deemed resident rule can apply if you are not liable to tax elsewhere by residence."},
        {"name": "Count days in India", "text": "Check the 120-day visitor rule separately if you visit often."},
        {"name": "File with the right status", "text": "File as RNOR where the rule applies; foreign income stays outside Indian tax."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch BR complete")
