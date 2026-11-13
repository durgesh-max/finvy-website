# -*- coding: utf-8 -*-
"""Batch BN (12 Nov 2026): returning to India from Canada - departure tax, RRSP, TFSA, Canadian accounts, India tax.
Facts (CRA emigrant rules): on emigration most property is deemed disposed of at fair market value (Form T1243); excluded
are Canadian real property, cash and registered plans such as RRSP, RRIF, RESP and TFSA; Form T1161 lists property where
the total fair market value exceeds CAD 25,000; the tax can be deferred by posting security (T1244). TFSA can be kept but
no contributions as a non-resident (1% per month tax on contributions made while non-resident). RRSP withdrawals by
non-residents bear 25% withholding, reducible by treaty in some cases. India: Form 40 (Canada notified) lets residents
defer Indian tax on income accruing in specified foreign retirement accounts until withdrawal; TFSA has no such
recognition, so income in it is taxable in India once resident and ordinarily resident; Schedule FA applies only when
resident and ordinarily resident; RNOR years generally exclude foreign income; FAST-DS Category 2 (INR 1 lakh) covers assets
earned abroad while NRI and missing from Schedule FA; declarations close 31 December 2026."""
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


CONTACT = ("WhatsApp +91 78018 87130 or email durgesh@bharatquantumprospera.com with your departure date, your Canadian accounts (RRSP, TFSA, bank, brokerage) and your stay in India for the last ten years. "
           "We reply the same working day with what is needed on the Indian side and a fixed-scope quote.")
SLUG = "returning-to-india-from-canada-rrsp-tfsa-departure-tax-india-tax-2026"
BOX = (f'<div style="border:1px solid var(--line);border-left:4px solid #C2312A;border-radius:10px;padding:16px 18px;margin:18px 0;background:var(--bg-soft)">'
       f'<p style="margin:0 0 8px;font-weight:600">Back from Canada a few years and never listed the RRSP, TFSA or bank account?</p>'
       f'<p style="margin:0">Savings built from Canadian salary while you were an NRI usually fit FAST-DS Category 2: a flat INR 1 lakh until 31 December 2026. '
       f'<a href="{CK}"><strong>Check it in the FAST-DS checker</strong></a> &middot; <a href="fast-ds-uk-pension-isa-canada-rrsp-australia-super-schedule-fa.html">RRSP and pensions in Schedule FA</a> &middot; '
       f'<a href="{wa("Hi Durgesh, I moved back from Canada and want to check my RRSP/TFSA position in India.")}" target="_blank" rel="noopener"><strong>WhatsApp CA Durgesh Chavda</strong></a>.</p></div>')

PAGES = [dict(
    slug=SLUG,
    title="Returning to India From Canada: Departure Tax, RRSP, TFSA and What India Taxes (2026)",
    em="two tax systems, one move.",
    kicker="/ Returning NRIs &middot; Canada &middot; Updated 2026-11-12",
    lead=("Leaving Canada triggers Canada's departure tax: most investments are treated as sold at market value on the day you leave, though RRSPs, TFSAs, cash and Canadian real estate are excluded. "
          "On the Indian side, your first years back are usually non-resident or RNOR years in which Canadian income is not taxed in India. Once you are resident and ordinarily resident, the RRSP, TFSA, bank and brokerage accounts all go in Schedule FA. "
          "An RRSP can use Form 40 to defer Indian tax until withdrawal; a TFSA has no such relief."),
    sections=[
        ("/ Account by account", "Canada side and India side.",
         table(["Item", "When you leave Canada", "In India once resident and ordinarily resident"], [
             ["Non-registered investments (shares, funds)", "Deemed sold at fair market value: departure tax on the gain (T1243); deferral possible with security", "Schedule FA; dividends and later gains taxed in India"],
             ["RRSP / RRIF", "Not deemed sold; withdrawals later bear Canadian non-resident withholding (25%, reducible by treaty in some cases)", "Schedule FA; Form 40 can defer Indian tax on income inside until withdrawal"],
             ["TFSA", "Can be kept; no contributions while non-resident (1% a month tax on contributions made as a non-resident)", "Not recognised in India: income inside is taxable; Schedule FA"],
             ["Bank accounts", "Not deemed sold", "Schedule FA; interest taxed in India with credit for Canadian tax"],
             ["Canadian home", "Not deemed sold; rent taxed in Canada as a non-resident", "Schedule FA; rent taxed in India with credit for Canadian tax"]])
         + '<p>Form T1161 lists your property when its total value exceeds CAD 25,000 on departure. More on Indian deferral: <a href="' + F40 + '">Form 40 for RRSP and other foreign retirement accounts</a>.</p>'
         + BOX),
        ("/ Use the RNOR years well", "Planning points.",
         ul("<strong>Find your RNOR years</strong> with the <a href=\"residential-status-calculator-india-nri-rnor-section-6.html\">residential status calculator</a>; foreign income and gains received outside India are generally not taxed in India then.",
            "<strong>Restructure before you are resident and ordinarily resident:</strong> decide what to keep in Canada, what to close and what to bring back while Indian tax does not reach it.",
            "<strong>TFSA:</strong> since India gives it no shelter and no new contributions are allowed, many returning NRIs review whether to keep it beyond the RNOR years.",
            "<strong>NRE and FCNR accounts</strong> in India must be redesignated once you return for good; foreign currency can sit in an RFC account. See <a href=\"nri-nre-nro-conversion-returning-india-2026.html\">NRE and NRO conversion on return</a>.",
            "<strong>CPP and OAS</strong> paid to you in India bear Canadian non-resident tax; check the India-Canada treaty position for your case before filing in India."))
        ,
        ("/ If you returned years ago", "Fix it before 31 December 2026.",
         ul("Canadian accounts and investments built from salary earned while you were an NRI, not shown in Schedule FA after you became resident: <strong>FAST-DS Category 2, INR 1 lakh</strong> (foreign assets up to INR 5 crore in total).",
            "TFSA income, interest or dividends earned while resident and ordinarily resident and never offered to tax: <strong>Category 1, 60%</strong> within INR 1 crore.",
            "Declare by 31 December 2026, pay after the Form 2 order, and report every year after.")
         + '<p>Related: <a href="fast-ds-returning-nri-foreign-accounts-not-reported.html">FAST-DS for returning NRIs</a> &middot; <a href="fast-ds-uk-pension-isa-canada-rrsp-australia-super-schedule-fa.html">RRSP, ISA and super in Schedule FA</a> &middot; <a href="indian-ca-for-clients-in-canada.html">Indian CA for clients in Canada</a>.</p>'
         f'<p><strong>Sources:</strong> Canada Revenue Agency guidance for emigrants (deemed disposition, Forms T1243, T1161 and T1244; TFSA and RRSP rules for non-residents); Income-tax return instructions for Schedule FA; Form 40 and the notification of Canada for foreign retirement accounts; Finance Act, 2026, Chapter IV (FAST-DS). <em>{UPDATED}</em> General information. BQP advises on the Indian side; Canadian filings need a Canadian tax professional.</p>'),
    ],
    faqs=[("What is Canada's departure tax?", "When you emigrate, Canada treats most of your property as sold at fair market value on the day you leave and taxes the gain. RRSPs, RRIFs, RESPs, TFSAs, cash and Canadian real estate are excluded. The tax can be deferred by posting security."),
          ("Can I keep my RRSP after moving back to India?", "Yes. Withdrawals later bear Canadian non-resident withholding. In India, list it in Schedule FA once you are resident and ordinarily resident; Form 40 can defer Indian tax on the income inside until you withdraw."),
          ("Is a TFSA tax-free in India?", "No. India does not recognise the TFSA, so income inside it is taxable in India once you are resident and ordinarily resident, and it goes in Schedule FA. Canada also bars contributions while you are non-resident."),
          ("When does India start taxing my Canadian income?", "Usually not in the non-resident or RNOR years after you return, if the income is received outside India. Once you are resident and ordinarily resident, your worldwide income is taxed in India."),
          ("I came back from Canada years ago and never reported my accounts. What now?", "If they were built from salary earned while you were an NRI, FAST-DS Category 2 settles it for a flat INR 1 lakh if you declare by 31 December 2026."),
          ("Can BQP help?", "On the Indian side, yes. " + CONTACT)],
    related=[(F40, "Form 40 for RRSP and foreign retirement accounts"),
             ("fast-ds-uk-pension-isa-canada-rrsp-australia-super-schedule-fa.html", "RRSP, ISA and super in Schedule FA"),
             ("residential-status-calculator-india-nri-rnor-section-6.html", "Residential status calculator")],
    cta_h="Moving back from Canada?", cta_b=CONTACT,
    keywords="returning to India from Canada tax, Canada departure tax India, RRSP after moving to India, TFSA taxable in India, TFSA non-resident India, Canada emigrant T1161, RRSP Schedule FA, moving back to India from Canada checklist",
    desc="Returning to India from Canada? Canada's departure tax (deemed disposition, T1243, T1161), what happens to your RRSP and TFSA, how India taxes them once you are resident and ordinarily resident, Form 40 for RRSP, and FAST-DS (INR 1 lakh) for missed reporting before 31 December 2026.",
    howto={"name": "How to handle Canadian accounts when returning to India", "description": "Steps for NRIs moving back from Canada.", "steps": [
        {"name": "Plan for departure tax", "text": "List non-registered investments and work out the deemed gain; consider deferral with security."},
        {"name": "Map your Indian residential status", "text": "Find your non-resident and RNOR years with the residential status calculator."},
        {"name": "Decide on RRSP and TFSA", "text": "Use Form 40 for the RRSP; review the TFSA, which India does not shelter."},
        {"name": "Report once resident and ordinarily resident", "text": "List Canadian accounts in Schedule FA and fix missed years through FAST-DS by 31 December 2026."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch BN complete")
