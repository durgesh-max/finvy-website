# -*- coding: utf-8 -*-
"""Batch BO (12 Nov 2026): returning to India from the UK - split year, ISA, UK pension, UK property, India tax.
Facts: UK split year treatment applies when UK resident under the Statutory Residence Test and one of the statutory cases
is met (Schedule 45, Finance Act 2013), claimed through Self Assessment; existing ISAs can be kept but non-residents cannot
subscribe; UK rent of non-resident landlords is paid with basic-rate tax deducted under the Non-Resident Landlord scheme
unless HMRC approves gross payment; the UK has no exit tax on leaving. India: non-resident and RNOR years generally exclude
foreign income received outside India; Schedule FA once resident and ordinarily resident; Form 40 (UK notified) defers
Indian tax on income accruing in specified UK pension accounts until withdrawal; ISA has no Indian recognition, so income
inside is taxable once resident and ordinarily resident; UK rent and interest taxable in India with credit for UK tax
(Form 67); UK State Pension treatment under the India-UK treaty should be checked case by case; FAST-DS Category 2
(INR 1 lakh) for assets earned while NRI and missing from Schedule FA; declarations close 31 December 2026."""
from urllib.parse import quote
from build_lib import page, write_page

UPDATED = "Last updated: 12 November 2026."
CK = "fast-ds-2026-eligibility-checker.html?kind=asset&then=no&since=yes&src=foreignWhileNR&fa=no&inc=yes&val=3000000"
F40 = "form-40-foreign-retirement-account-401k-ira-uk-pension-rrsp-super-defer-tax-india.html"


def wa(t):
    return "https://wa.me/917801887130?text=" + quote(t)


def ul(*x):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in x) + "</ul>"


def table(head, rows):
    return ("<table><thead><tr>" + "".join(f"<th>{h}</th>" for h in head) + "</tr></thead><tbody>"
            + "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows) + "</tbody></table>")


CONTACT = ("WhatsApp +91 78018 87130 or email durgesh@bharatquantumprospera.com with your UK leaving date, your UK accounts (ISA, pension, bank, property) and your stay in India for the last ten years. "
           "We reply the same working day with what is needed on the Indian side and a fixed-scope quote.")
SLUG = "returning-to-india-from-uk-isa-uk-pension-property-split-year-india-tax-2026"
BOX = (f'<div style="border:1px solid var(--line);border-left:4px solid #C2312A;border-radius:10px;padding:16px 18px;margin:18px 0;background:var(--bg-soft)">'
       f'<p style="margin:0 0 8px;font-weight:600">Back from the UK a few years and never listed the ISA, pension or bank account?</p>'
       f'<p style="margin:0">Savings built from UK salary while you were an NRI usually fit FAST-DS Category 2: a flat INR 1 lakh until 31 December 2026. '
       f'<a href="{CK}"><strong>Check it in the FAST-DS checker</strong></a> &middot; <a href="fast-ds-uk-pension-isa-canada-rrsp-australia-super-schedule-fa.html">UK pensions and ISAs in Schedule FA</a> &middot; '
       f'<a href="{wa("Hi Durgesh, I moved back from the UK and want to check my ISA/pension position in India.")}" target="_blank" rel="noopener"><strong>WhatsApp CA Durgesh Chavda</strong></a>.</p></div>')

PAGES = [dict(
    slug=SLUG,
    title="Returning to India From the UK: ISA, UK Pension, UK Property and What India Taxes (2026)",
    em="the ISA wrapper stops at Heathrow.",
    kicker="/ Returning NRIs &middot; United Kingdom &middot; Updated 2026-11-12",
    lead=("The UK has no exit tax, and split year treatment can end your UK residence part-way through the tax year. "
          "On the Indian side, your first years back are usually non-resident or RNOR years in which UK income received outside India is not taxed. "
          "Once you are resident and ordinarily resident, every UK account goes in Schedule FA: a UK workplace or personal pension can use Form 40 to defer Indian tax until withdrawal, but an ISA has no Indian shelter, so the income inside it becomes taxable in India."),
    sections=[
        ("/ Account by account", "UK side and India side.",
         table(["Item", "After you leave the UK", "In India once resident and ordinarily resident"], [
             ["ISA (cash or stocks and shares)", "Can be kept; no new subscriptions while non-resident", "Not recognised: interest, dividends and gains inside are taxable; Schedule FA"],
             ["Workplace or personal pension", "Stays invested; UK tax on withdrawals depends on the treaty and HMRC process", "Schedule FA; Form 40 can defer Indian tax on income inside until withdrawal"],
             ["UK State Pension", "Paid abroad", "Treaty position to be checked for your case before filing"],
             ["UK bank accounts", "Can be kept", "Schedule FA; interest taxed in India with credit for any UK tax"],
             ["UK property let out", "Rent paid with basic-rate tax deducted under the Non-Resident Landlord scheme unless HMRC approves gross payment", "Schedule FA; rent taxed in India with credit for UK tax via Form 67"]])
         + '<p>More on deferral: <a href="' + F40 + '">Form 40 for UK pensions and other foreign retirement accounts</a>.</p>'
         + BOX),
        ("/ Use the RNOR years well", "Planning points.",
         ul("<strong>Find your RNOR years</strong> with the <a href=\"residential-status-calculator-india-nri-rnor-section-6.html\">residential status calculator</a>; UK income and gains received outside India are generally not taxed in India then.",
            "<strong>ISA decision:</strong> because India gives the ISA no shelter once you are resident and ordinarily resident, many returning NRIs decide during the RNOR years whether to keep it.",
            "<strong>Split year in the UK:</strong> claimed through your Self Assessment return when one of the statutory cases applies; it decides which part of the year's income the UK taxes.",
            "<strong>NRE and FCNR accounts</strong> in India must be redesignated once you return for good; an RFC account can hold foreign currency. See <a href=\"nri-nre-nro-conversion-returning-india-2026.html\">NRE and NRO conversion on return</a>.",
            "<strong>Moving money:</strong> see <a href=\"send-money-uk-to-india-india-to-uk-nri-tax-fema-2026.html\">sending money between the UK and India</a> for FEMA and tax points."))
        ,
        ("/ If you returned years ago", "Fix it before 31 December 2026.",
         ul("UK accounts, ISAs and pensions built from salary earned while you were an NRI, not shown in Schedule FA after you became resident: <strong>FAST-DS Category 2, INR 1 lakh</strong> (asset up to INR 5 crore).",
            "ISA income, UK interest or UK rent earned while resident and ordinarily resident and never offered to tax in India: <strong>Category 1, 60%</strong> within INR 1 crore.",
            "Declare by 31 December 2026, pay after the Form 2 order, and report every year after.")
         + '<p>Related: <a href="fast-ds-returning-nri-foreign-accounts-not-reported.html">FAST-DS for returning NRIs</a> &middot; <a href="indian-ca-for-clients-in-uk.html">Indian CA for clients in the UK</a> &middot; <a href="returning-to-india-from-canada-rrsp-tfsa-departure-tax-india-tax-2026.html">returning from Canada</a> &middot; <a href="returning-from-uae-dubai-to-india-gratuity-uae-bank-account-tax-2026.html">returning from the UAE</a>.</p>'
         f'<p><strong>Sources:</strong> HMRC guidance on the Statutory Residence Test and split year treatment (Finance Act 2013, Schedule 45), ISA rules for non-residents and the Non-Resident Landlord scheme; Income-tax return instructions for Schedule FA; Form 40 and the notification of the UK for foreign retirement accounts; Finance Act, 2026, Chapter IV (FAST-DS). <em>{UPDATED}</em> General information. BQP advises on the Indian side; UK filings need a UK tax professional.</p>'),
    ],
    faqs=[("Can I keep my ISA after moving back to India?", "Yes, but you cannot pay into it while non-resident. In India it has no tax shelter: once you are resident and ordinarily resident, the interest, dividends and gains inside are taxable and the ISA goes in Schedule FA."),
          ("Is my UK pension taxable in India?", "List it in Schedule FA once you are resident and ordinarily resident. Form 40 can defer Indian tax on the income accruing inside until you withdraw, because the UK is a notified country."),
          ("Does the UK have an exit tax?", "No. Split year treatment may end your UK residence part-way through the tax year if you meet one of the statutory cases; it is claimed through Self Assessment."),
          ("How is rent from my UK flat taxed after I return?", "In the UK, under the Non-Resident Landlord scheme, with basic-rate tax deducted unless HMRC approves gross payment. In India, once you are resident and ordinarily resident, the rent is taxable with credit for the UK tax through Form 67."),
          ("I came back from the UK years ago and never reported my accounts. What now?", "If they were built from salary earned while you were an NRI, FAST-DS Category 2 settles it for a flat INR 1 lakh if you declare by 31 December 2026."),
          ("Can BQP help?", "On the Indian side, yes. " + CONTACT)],
    related=[(F40, "Form 40 for UK pensions"),
             ("fast-ds-uk-pension-isa-canada-rrsp-australia-super-schedule-fa.html", "UK pensions and ISAs in Schedule FA"),
             ("indian-ca-for-clients-in-uk.html", "Indian CA for clients in the UK")],
    cta_h="Moving back from the UK?", cta_b=CONTACT,
    keywords="returning to India from UK tax, ISA after moving to India, ISA taxable in India, UK pension India tax returning NRI, split year treatment leaving UK India, UK property rent NRL India tax, moving back to India from UK checklist",
    desc="Returning to India from the UK? No UK exit tax, split year treatment, what happens to your ISA, UK pension and UK property, how India taxes them once you are resident and ordinarily resident, Form 40 for UK pensions, and FAST-DS (INR 1 lakh) for missed reporting before 31 December 2026.",
    howto={"name": "How to handle UK accounts when returning to India", "description": "Steps for NRIs moving back from the UK.", "steps": [
        {"name": "Check split year treatment", "text": "Confirm with a UK adviser whether a statutory case applies and claim it in Self Assessment."},
        {"name": "Map your Indian residential status", "text": "Find your non-resident and RNOR years with the residential status calculator."},
        {"name": "Decide on the ISA and pension", "text": "Use Form 40 for the UK pension; review the ISA, which India does not shelter."},
        {"name": "Report once resident and ordinarily resident", "text": "List UK accounts and property in Schedule FA and fix missed years through FAST-DS by 31 December 2026."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch BO complete")
