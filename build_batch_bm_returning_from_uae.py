# -*- coding: utf-8 -*-
"""Batch BM (12 Nov 2026): returning from the UAE / Gulf - end-of-service gratuity, UAE accounts and property, India tax.
Facts: a non-resident, and a resident but not ordinarily resident, is not taxed in India on income that accrues and is
received outside India (for RNOR, unless from a business controlled or profession set up in India); salary for services
rendered in the UAE accrues outside India; the UAE levies no personal income tax, so there is no foreign tax credit;
Schedule FA applies only when resident and ordinarily resident; FAST-DS Category 2 (INR 1 lakh, up to INR 5 crore) covers
assets earned abroad while NRI and missing from Schedule FA; declarations close 31 December 2026; NRE/FCNR accounts must
be redesignated on return (FEMA), RFC account available for foreign currency brought back; the Income Tax Department has
been nudging owners of undisclosed UAE property (Business Standard, 26 Oct 2026)."""
from urllib.parse import quote
from build_lib import page, write_page

UPDATED = "Last updated: 12 November 2026."
CK = "fast-ds-2026-eligibility-checker.html?kind=asset&then=no&since=yes&src=foreignWhileNR&fa=no&inc=yes&val=2000000"


def wa(t):
    return "https://wa.me/917801887130?text=" + quote(t)


def ul(*x):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in x) + "</ul>"


def table(head, rows):
    return ("<table><thead><tr>" + "".join(f"<th>{h}</th>" for h in head) + "</tr></thead><tbody>"
            + "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows) + "</tbody></table>")


CONTACT = ("WhatsApp +91 78018 87130 or email durgesh@bharatquantumprospera.com with your return date, your UAE accounts and assets, and your stay in India for the last ten years. "
           "We reply the same working day with what is needed and a fixed-scope quote.")
SLUG = "returning-from-uae-dubai-to-india-gratuity-uae-bank-account-tax-2026"
BOX = (f'<div style="border:1px solid var(--line);border-left:4px solid #C2312A;border-radius:10px;padding:16px 18px;margin:18px 0;background:var(--bg-soft)">'
       f'<p style="margin:0 0 8px;font-weight:600">Moved back a few years ago and still hold UAE accounts or property?</p>'
       f'<p style="margin:0">Once you became resident and ordinarily resident they belonged in Schedule FA. Money earned in the UAE while you were an NRI usually fits FAST-DS Category 2: a flat INR 1 lakh until 31 December 2026. '
       f'<a href="{CK}"><strong>Check your case in the FAST-DS checker</strong></a> &middot; <a href="dubai-uae-property-not-disclosed-india-income-tax-nudge-fast-ds-2026.html">UAE property nudge</a> &middot; '
       f'<a href="{wa("Hi Durgesh, I have returned from the UAE and want to check my India tax position.")}" target="_blank" rel="noopener"><strong>WhatsApp CA Durgesh Chavda</strong></a>.</p></div>')

PAGES = [dict(
    slug=SLUG,
    title="Returning to India From the UAE or Dubai: Tax on End-of-Service Gratuity, UAE Bank Accounts and Property (2026)",
    em="tax-free there does not mean tax-free here.",
    kicker="/ Returning NRIs &middot; UAE &middot; Updated 2026-11-12",
    lead=("The UAE taxes none of it, so the Indian rules decide everything. Your end-of-service gratuity and final salary, earned for work in the UAE and paid into a UAE account, are generally not taxed in India if you are non-resident or resident but not ordinarily resident (RNOR) in that year. "
          "The risk comes later: once you become resident and ordinarily resident, every UAE bank account, investment and property must be in Schedule FA, and income from them is taxed in India with no UAE tax to credit. "
          "Many people who returned years ago never listed them; FAST-DS fixes that for INR 1 lakh until 31 December 2026."),
    sections=[
        ("/ Year by year", "Your residential status decides it.",
         table(["Your status in India", "UAE gratuity and salary paid in the UAE", "UAE accounts and property"], [
             ["Non-resident (often the year you return)", "Not taxed in India", "No Schedule FA; Indian income only"],
             ["Resident but not ordinarily resident (usually the next one to three years)", "Not taxed in India if received outside India", "No Schedule FA; UAE income generally not taxed"],
             ["Resident and ordinarily resident", "Global income taxed", "Schedule FA every year; UAE rent and interest taxed, no foreign tax credit"]])
         + '<p>Work out each year with the <a href="residential-status-calculator-india-nri-rnor-section-6.html">residential status calculator</a>; the day counts and the ten-year history matter.</p>'
         + BOX),
        ("/ Before and after you land", "Practical steps.",
         ul("<strong>Gratuity and final settlement:</strong> have them paid into your UAE account before you return; moving the money to India afterwards is a transfer of capital, not new income.",
            "<strong>NRE and FCNR accounts:</strong> tell your Indian bank you have returned; they must be redesignated as resident accounts. Foreign currency can be held in an RFC account.",
            "<strong>UAE bank accounts:</strong> you may keep them, but list them in Schedule FA once you are resident and ordinarily resident, and offer any interest to tax.",
            "<strong>UAE property:</strong> can be kept (section 6(4) of FEMA); rent becomes taxable in India once you are resident and ordinarily resident. See <a href=\"dubai-uae-property-not-disclosed-india-income-tax-nudge-fast-ds-2026.html\">the UAE property nudge</a>.",
            "<strong>Selling UAE assets during RNOR years</strong> generally keeps the gain outside Indian tax; after that it is taxed in India."))
        ,
        ("/ If you returned years ago", "The FAST-DS window.",
         ul("UAE accounts, investments or property built from salary earned while you were an NRI, not shown in Schedule FA after you became resident: <strong>Category 2, INR 1 lakh</strong> (foreign assets up to INR 5 crore in total).",
            "UAE rent or interest earned while resident and ordinarily resident and never offered to tax: <strong>Category 1, 60%</strong> within INR 1 crore.",
            "Declare by 31 December 2026; pay after the Form 2 order; then report every year.")
         + '<p>Related: <a href="fast-ds-returning-nri-foreign-accounts-not-reported.html">FAST-DS for returning NRIs</a> &middot; <a href="nri-nre-nro-conversion-returning-india-2026.html">NRE and NRO conversion on return</a> &middot; <a href="house-flat-property-abroad-not-in-schedule-fa-fast-ds-returning-nri.html">property abroad and FAST-DS</a>.</p>'
         f'<p><strong>Sources:</strong> Income-tax Act, 2025 provisions on residence and scope of total income; Income-tax return instructions for Schedule FA; Foreign Exchange Management Act, 1999, section 6(4) and the deposit regulations; Finance Act, 2026, Chapter IV (FAST-DS); Business Standard, 26 October 2026. <em>{UPDATED}</em> General information, not advice for your situation.</p>'),
    ],
    faqs=[("Is UAE end-of-service gratuity taxable in India?", "Generally not, if it is for work in the UAE, is paid into a UAE account, and you are non-resident or resident but not ordinarily resident in that year. Bringing the money to India later is a transfer of capital, not new income."),
          ("Can I keep my UAE bank account after moving back to India?", "Yes. Once you are resident and ordinarily resident, list it in Schedule FA every year and offer any interest to tax in India."),
          ("Is rent from my Dubai flat taxable after I return?", "Not in non-resident or RNOR years if it is received outside India. Once you are resident and ordinarily resident, it is taxable in India at slab rates, with no UAE tax to credit."),
          ("I returned from Dubai years ago and never reported my UAE account. What now?", "If the money was earned while you were an NRI, FAST-DS Category 2 settles it for a flat INR 1 lakh if you declare by 31 December 2026. Untaxed interest or rent is a separate Category 1 item at 60%."),
          ("What happens to my NRE account when I return?", "It must be redesignated as a resident account once you return for good. Foreign currency can be kept in an RFC account."),
          ("Can BQP plan my return?", "Yes. " + CONTACT)],
    related=[("fast-ds-returning-nri-foreign-accounts-not-reported.html", "FAST-DS for returning NRIs"),
             ("residential-status-calculator-india-nri-rnor-section-6.html", "Residential status calculator"),
             ("dubai-uae-property-not-disclosed-india-income-tax-nudge-fast-ds-2026.html", "UAE property and the FAST-DS nudge")],
    cta_h="Returned or returning from the UAE?", cta_b=CONTACT,
    keywords="returning to India from UAE tax, UAE gratuity taxable in India, end of service gratuity India tax, Dubai bank account after returning to India, UAE bank account Schedule FA, returning NRI Dubai tax, RNOR UAE income",
    desc="Returning to India from the UAE or Dubai? UAE end-of-service gratuity is generally not taxed in India in NRI or RNOR years; UAE accounts and property go in Schedule FA once you are resident and ordinarily resident. Year-by-year rules and the FAST-DS fix (INR 1 lakh) before 31 December 2026.",
    howto={"name": "How to handle UAE money when returning to India", "description": "Steps for NRIs moving back from the UAE.", "steps": [
        {"name": "Get gratuity paid in the UAE", "text": "Have the final settlement paid into your UAE account before you return."},
        {"name": "Work out your status each year", "text": "Use the residential status calculator to find your NRI, RNOR and resident years."},
        {"name": "Redesignate NRE accounts", "text": "Tell your Indian bank you have returned; use an RFC account for foreign currency."},
        {"name": "Report UAE assets when resident and ordinarily resident", "text": "List UAE accounts and property in Schedule FA, and fix missed years through FAST-DS by 31 December 2026."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch BM complete")
