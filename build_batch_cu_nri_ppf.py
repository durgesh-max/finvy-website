# -*- coding: utf-8 -*-
"""Batch CU (15 Nov 2026): PPF for NRIs. Demand: autocomplete sweep 15 Nov 2026, all 7 markets: "nri ppf",
"nri ppf premature closure", "nri ppf extension", "nri ppf account closure procedure"; no dedicated page.
Facts (PPF Scheme, 2019; consistent across Upstox, Bajaj Finserv, Scripbox, Business Today 24 Aug 2026):
NRIs cannot open a new PPF account; a resident who becomes NRI may continue the existing account until its 15-year
maturity, contributing within INR 1.5 lakh a year, on a non-repatriation basis; the five-year extension block is not
available to NRIs; premature closure after five years is allowed on change of residency status, with interest reduced
by one percentage point; proceeds are credited to an NRO account and can be remitted abroad within the USD 1 million
a financial year NRO limit with Forms 145/146 (formerly 15CA/15CB). Post-maturity interest for NRIs is reported
inconsistently (some accounts flagged under the Ministry of Finance August 2024 regularisation of irregular small
savings accounts) - page tells readers to confirm with the bank or post office. PPF interest is exempt in India; the
country of residence may tax it. Checked 15 Nov 2026."""
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


CONTACT = ("WhatsApp +91 78018 87130 or email durgesh@bharatquantumprospera.com with your PPF opening year, the date you became NRI and your country of residence. "
           "We reply the same working day on closure or continuation, repatriation and how your country taxes it.")
SLUG = "nri-ppf-account-rules-continue-maturity-premature-closure-extension-repatriation-2026"
BOX = (f'<div style="border:1px solid var(--line);border-left:4px solid #C2312A;border-radius:10px;padding:16px 18px;margin:18px 0;background:var(--bg-soft)">'
       f'<p style="margin:0 0 8px;font-weight:600">PPF is tax-free in India, not necessarily where you live.</p>'
       f'<p style="margin:0">The US, UK, Canada and Australia can tax PPF interest each year, and the account must be reported abroad. Moving the money out goes through NRO and Forms 145/146. '
       f'<a href="{wa("Hi Durgesh, I am an NRI with a PPF account in India. Should I continue it or close it, and how do I move the money?")}" target="_blank" rel="noopener"><strong>WhatsApp CA Durgesh Chavda</strong></a>.</p></div>')

PAGES = [dict(
    slug=SLUG,
    title="PPF for NRIs (2026): Can You Continue Your PPF After Becoming an NRI? Maturity, Premature Closure, Extension and Repatriation",
    em="continue to maturity, no new account, no extension.",
    kicker="/ NRI &middot; PPF &middot; Repatriation &middot; Updated 2026-11-15",
    lead=("An NRI <strong>cannot open a new PPF account</strong>, but a PPF opened while you were resident in India can <strong>continue until its 15-year maturity</strong>; you can keep depositing up to INR 1.5 lakh a year on a <strong>non-repatriation basis</strong>. "
          "The <strong>five-year extension</strong> after maturity is <strong>not available to NRIs</strong>, so plan to close the account at maturity. "
          "If you want out earlier, <strong>premature closure after five years</strong> is allowed when the reason is a <strong>change in residency status</strong>, with the interest reduced by one percentage point. "
          "The money is paid into your <strong>NRO account</strong> and can be sent abroad within the <strong>USD 1 million a year</strong> NRO limit with Forms 145/146 (formerly 15CA/15CB). PPF interest stays <strong>tax-free in India</strong>, but your country of residence may tax it."),
    sections=[
        ("/ The rules at a glance", "PPF after you become an NRI.",
         table(["Question", "Answer"], [
             ["Can an NRI open a new PPF?", "No"],
             ["Can I keep my existing PPF after becoming NRI?", "Yes, until the 15-year maturity, on a non-repatriation basis"],
             ["Can I keep depositing?", "Yes, within INR 1.5 lakh a financial year, from an NRO account (or normal banking channels)"],
             ["Can I extend after maturity in blocks of five years?", "No; the extension facility is for residents"],
             ["Can I close early?", "After five complete years, on change of residency status; interest reduced by 1 percentage point"],
             ["Where does the money go?", "Your NRO account; remittance abroad within USD 1 million a financial year with Forms 145/146"],
             ["Indian tax on PPF interest and maturity?", "Exempt"],
             ["Tax where you live?", "Often taxable: US, UK, Canada and Australia generally tax the interest and require the account to be reported"]])
         + BOX),
        ("/ Points to watch", "Where NRIs get caught out.",
         ul("<strong>Interest after maturity:</strong> sources and banks differ on whether an NRI's matured but unclosed account keeps earning interest; some NRI accounts were flagged under the Ministry of Finance&rsquo;s August 2024 regularisation of irregular small-savings accounts. Confirm with your bank or post office and close on maturity unless told in writing otherwise.",
            "<strong>Tell the bank you are NRI:</strong> update your residential status and KYC; link the PPF to an NRO account for credits.",
            "<strong>Returning to India:</strong> once you are resident again you can open a new PPF, and a resident can use the extension facility.",
            "<strong>US residents:</strong> PPF is generally treated as a foreign account for FBAR and Form 8938, and the interest is reported on the US return; the US-India treaty does not make it tax-free in the US. See <a href=\"what-is-fbar.html\">FBAR</a>.",
            "<strong>Moving the money:</strong> see <a href=\"repatriate-money-from-india-to-abroad-nro-usd-1-million-15ca-15cb-2026.html\">repatriating from NRO (USD 1 million, Forms 145/146)</a>.")
         + '<p>Related: <a href="nre-nro-fcnr-account-tax-rules.html">NRE vs NRO vs FCNR</a> &middot; <a href="nri-epf-pf-withdrawal-process-online-tax-form-19-15g-2026.html">EPF withdrawal for NRIs</a> &middot; <a href="nri-taxation-india-complete-guide.html">NRI taxation guide</a> &middot; <a href="nri-returning-india-tax-rnor-transition.html">returning to India</a>.</p>'
         + f'<p><strong>Sources:</strong> Public Provident Fund Scheme, 2019 (Ministry of Finance notification of 12 December 2019); Ministry of Finance office memorandum of August 2024 on regularisation of irregular small-savings accounts; FEMA rules on NRO remittances. Secondary summaries checked 15 November 2026: Upstox, Bajaj Finserv, Scripbox, Business Today (24 August 2026). <em>{UPDATED}</em> General information; confirm account-specific treatment with your bank or post office.</p>'),
    ],
    faqs=[("Can an NRI continue a PPF account?", "Yes, if it was opened while resident. It can run until its 15-year maturity, with deposits up to INR 1.5 lakh a year on a non-repatriation basis. NRIs cannot open a new PPF."),
          ("Can an NRI extend PPF after 15 years?", "No. The five-year block extension is available to residents only, so NRIs should close the account at maturity."),
          ("Can an NRI close PPF before maturity?", "Yes, after five complete years, if the reason is a change in residency status. Interest is reduced by one percentage point for the period."),
          ("Can PPF money be sent abroad?", "Yes. It is credited to the NRO account and can be remitted within the USD 1 million per financial year NRO limit, with Forms 145/146 (formerly 15CA/15CB)."),
          ("Is PPF interest taxable for NRIs?", "Not in India; PPF interest and maturity are exempt. The country of residence may tax it: the US, UK, Canada and Australia generally do, and the account must be reported there."),
          ("Can BQP help?", "Yes. " + CONTACT)],
    related=[("repatriate-money-from-india-to-abroad-nro-usd-1-million-15ca-15cb-2026.html", "Repatriating from NRO"), ("nre-nro-fcnr-account-tax-rules.html", "NRE vs NRO vs FCNR"),
             ("nri-epf-pf-withdrawal-process-online-tax-form-19-15g-2026.html", "EPF withdrawal for NRIs")],
    cta_h="NRI with a PPF account in India?", cta_b=CONTACT,
    keywords="NRI PPF, NRI PPF rules 2026, can NRI continue PPF, NRI PPF extension, NRI PPF premature closure, NRI PPF account closure procedure, PPF maturity NRI repatriation, PPF interest taxable US NRI",
    desc="PPF for NRIs (2026): no new account, but an existing PPF continues to its 15-year maturity (non-repatriation, INR 1.5 lakh a year); no five-year extension; premature closure after five years on change of residency (interest minus 1%); proceeds to NRO and remittable within USD 1 million; Indian vs foreign tax.",
    howto={"name": "How an NRI closes a PPF and moves the money abroad", "description": "Steps for NRIs with PPF accounts.", "steps": [
        {"name": "Update status", "text": "Inform the bank or post office that you are NRI and link an NRO account."},
        {"name": "Choose timing", "text": "Close at maturity, or after five years on change of residency (interest minus 1%)."},
        {"name": "Submit closure form", "text": "File the closure application with passport and KYC; proceeds go to NRO."},
        {"name": "Remit abroad", "text": "Remit within the USD 1 million NRO limit with Forms 145/146."},
        {"name": "Report abroad", "text": "Report the account and any interest in your country of residence."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch CU complete")
