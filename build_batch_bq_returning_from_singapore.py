# -*- coding: utf-8 -*-
"""Batch BQ (12 Nov 2026): returning to India from Singapore - IR21 tax clearance, CPF, Singapore accounts, India tax.
Facts: IRAS requires employers to file Form IR21 at least one month before a non-citizen employee ceases employment or
leaves Singapore for more than three months, and to withhold monies due until clearance; this covers permanent residents
leaving permanently. Singapore permanent residents who give up PR and leave Singapore permanently can apply to withdraw
their CPF savings (CPF Board rules); foreign employees who are not PRs do not contribute to CPF. Singapore has no capital
gains tax and no exit tax. India: non-resident and RNOR years generally exclude foreign income received outside India;
Schedule FA once resident and ordinarily resident; Form 40 deferral applies only to retirement accounts in notified
countries (USA, UK, Canada, Australia), so CPF is not covered; FAST-DS Category 2 (INR 1 lakh) for assets earned while NRI
and missing from Schedule FA; declarations close 31 December 2026."""
from urllib.parse import quote
from build_lib import page, write_page

UPDATED = "Last updated: 12 November 2026."
CK = "fast-ds-2026-eligibility-checker.html?kind=asset&then=no&since=yes&src=foreignWhileNR&fa=no&inc=yes&val=3000000"


def wa(t):
    return "https://wa.me/917801887130?text=" + quote(t)


def ul(*x):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in x) + "</ul>"


def table(head, rows):
    return ("<table><thead><tr>" + "".join(f"<th>{h}</th>" for h in head) + "</tr></thead><tbody>"
            + "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows) + "</tbody></table>")


CONTACT = ("WhatsApp +91 78018 87130 or email durgesh@bharatquantumprospera.com with your PR or pass status, leaving date, CPF and other Singapore assets, and your stay in India for the last ten years. "
           "We reply the same working day with what is needed on the Indian side and a fixed-scope quote.")
SLUG = "returning-to-india-from-singapore-cpf-ir21-singapore-accounts-india-tax-2026"
BOX = (f'<div style="border:1px solid var(--line);border-left:4px solid #C2312A;border-radius:10px;padding:16px 18px;margin:18px 0;background:var(--bg-soft)">'
       f'<p style="margin:0 0 8px;font-weight:600">Back from Singapore a few years and never listed the bank, brokerage or CPF account?</p>'
       f'<p style="margin:0">Savings built from Singapore salary while you were an NRI usually fit FAST-DS Category 2: a flat INR 1 lakh until 31 December 2026. '
       f'<a href="{CK}"><strong>Check it in the FAST-DS checker</strong></a> &middot; <a href="fast-ds-returning-nri-foreign-accounts-not-reported.html">FAST-DS for returning NRIs</a> &middot; '
       f'<a href="{wa("Hi Durgesh, I moved back from Singapore and want to check my India tax position.")}" target="_blank" rel="noopener"><strong>WhatsApp CA Durgesh Chavda</strong></a>.</p></div>')

PAGES = [dict(
    slug=SLUG,
    title="Returning to India From Singapore: IR21 Tax Clearance, CPF, Singapore Accounts and What India Taxes (2026)",
    em="clear IRAS before you clear immigration.",
    kicker="/ Returning NRIs &middot; Singapore &middot; Updated 2026-11-12",
    lead=("Before you leave Singapore, your employer has to seek tax clearance (Form IR21) at least a month ahead and may hold back your final pay until IRAS clears it. "
          "Singapore has no exit tax and no capital gains tax. Permanent residents who give up PR and leave for good can apply to withdraw their CPF; employment pass holders who were not PRs have no CPF. "
          "In India, the first years back are usually non-resident or RNOR years; once you are resident and ordinarily resident, Singapore accounts and any CPF balance go in Schedule FA. CPF is not covered by Form 40, so plan its treatment early."),
    sections=[
        ("/ Item by item", "Singapore side and Indian side.",
         table(["Item", "When you leave Singapore", "In India once resident and ordinarily resident"], [
             ["Final salary and bonus", "Employer files IR21 at least one month ahead and withholds monies until clearance", "Not taxed in India if earned for Singapore work and paid there in a non-resident or RNOR year"],
             ["CPF (permanent residents)", "Withdrawal possible after giving up PR and leaving permanently", "If still held: Schedule FA; no Form 40 deferral because Singapore is not a notified country"],
             ["Bank and brokerage accounts", "Can be kept", "Schedule FA; interest, dividends and gains taxed in India"],
             ["Singapore property", "Can be kept; rent taxed in Singapore", "Schedule FA; rent taxed in India with credit for Singapore tax (Form 67)"]])
         + BOX),
        ("/ Use the RNOR years well", "Planning points.",
         ul("<strong>Find your RNOR years</strong> with the <a href=\"residential-status-calculator-india-nri-rnor-section-6.html\">residential status calculator</a>; foreign income and gains received outside India are generally not taxed in India then.",
            "<strong>CPF decision:</strong> if you are a PR, decide whether to withdraw before you become resident and ordinarily resident in India, since Form 40 cannot defer Indian tax on it.",
            "<strong>Restructure investments</strong> while Indian tax does not reach foreign gains, rather than after.",
            "<strong>NRE and FCNR accounts</strong> in India must be redesignated once you return for good; an RFC account can hold foreign currency. See <a href=\"nri-nre-nro-conversion-returning-india-2026.html\">NRE and NRO conversion on return</a>.",
            "<strong>Singapore company or ESOPs:</strong> shares in a Singapore employer or your own Singapore company stay reportable; for founders, see <a href=\"nri-returning-startup-moving-to-india.html\">moving a startup back to India</a>."))
        ,
        ("/ If you returned years ago", "Fix it before 31 December 2026.",
         ul("Singapore accounts, shares or CPF built from salary earned while you were an NRI, not shown in Schedule FA after you became resident: <strong>FAST-DS Category 2, INR 1 lakh</strong> (foreign assets up to INR 5 crore in total).",
            "Singapore interest, dividends or rent earned while resident and ordinarily resident and never offered to tax in India: <strong>Category 1, 60%</strong> within INR 1 crore.",
            "Declare by 31 December 2026, pay after the Form 2 order, and report every year after.")
         + '<p>Other country guides: <a href="returning-from-uae-dubai-to-india-gratuity-uae-bank-account-tax-2026.html">UAE</a> &middot; <a href="returning-to-india-from-uk-isa-uk-pension-property-split-year-india-tax-2026.html">UK</a> &middot; <a href="returning-to-india-from-canada-rrsp-tfsa-departure-tax-india-tax-2026.html">Canada</a> &middot; <a href="returning-to-india-from-australia-super-dasp-cgt-property-india-tax-2026.html">Australia</a> &middot; <a href="h1b-holders-returning-to-india-tax-rnor-401k-2026.html">USA</a>.</p>'
         f'<p><strong>Sources:</strong> IRAS guidance on tax clearance for foreign and SPR employees (Form IR21); CPF Board rules on withdrawal for permanent residents leaving Singapore permanently; Income-tax return instructions for Schedule FA; Form 40 and the notified countries for foreign retirement accounts; Finance Act, 2026, Chapter IV (FAST-DS). <em>{UPDATED}</em> General information. BQP advises on the Indian side; Singapore filings need a Singapore tax professional.</p>'),
    ],
    faqs=[("What is IR21 tax clearance?", "Before a non-citizen employee stops working in Singapore or leaves for more than three months, the employer must file Form IR21 with IRAS at least one month ahead and withhold monies due until IRAS gives clearance. It applies to permanent residents leaving permanently too."),
          ("Can I withdraw my CPF when I move back to India?", "Permanent residents who give up PR and leave Singapore permanently can apply to withdraw their CPF savings. Employment pass holders who were not PRs do not have CPF."),
          ("Is CPF taxable in India?", "If you still hold it once you are resident and ordinarily resident, it goes in Schedule FA. Form 40 deferral does not apply because Singapore is not a notified country, so plan the withdrawal or treatment during your non-resident or RNOR years."),
          ("Is my Singapore salary taxable in India after I return?", "Not if it was earned for work in Singapore and paid there in a year you are non-resident or RNOR in India."),
          ("I came back from Singapore years ago and never reported my accounts. What now?", "If they were built from salary earned while you were an NRI, FAST-DS Category 2 settles it for a flat INR 1 lakh if you declare by 31 December 2026."),
          ("Can BQP help?", "On the Indian side, yes. " + CONTACT)],
    related=[("fast-ds-returning-nri-foreign-accounts-not-reported.html", "FAST-DS for returning NRIs"),
             ("residential-status-calculator-india-nri-rnor-section-6.html", "Residential status calculator"),
             ("nri-returning-india-tax-rnor-transition.html", "Returning NRI: RNOR transition")],
    cta_h="Moving back from Singapore?", cta_b=CONTACT,
    keywords="returning to India from Singapore tax, IR21 tax clearance India, CPF withdrawal moving to India, CPF taxable in India, Singapore bank account Schedule FA, moving back to India from Singapore checklist, Singapore PR leaving permanently CPF",
    desc="Returning to India from Singapore? IR21 tax clearance before you leave, CPF withdrawal for permanent residents, how India taxes Singapore accounts and CPF once you are resident and ordinarily resident (no Form 40 for CPF), and FAST-DS (INR 1 lakh) for missed reporting before 31 December 2026.",
    howto={"name": "How to handle Singapore assets when returning to India", "description": "Steps for NRIs moving back from Singapore.", "steps": [
        {"name": "Start IR21 early", "text": "Ask your employer to file Form IR21 at least one month before your last day."},
        {"name": "Decide on CPF", "text": "If you are a PR leaving permanently, decide whether to withdraw CPF before you become resident and ordinarily resident in India."},
        {"name": "Map your Indian residential status", "text": "Find your non-resident and RNOR years with the residential status calculator."},
        {"name": "Report once resident and ordinarily resident", "text": "List Singapore accounts and CPF in Schedule FA and fix missed years through FAST-DS by 31 December 2026."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch BQ complete")
