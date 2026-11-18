# -*- coding: utf-8 -*-
"""Batch DA (18 Nov 2026): loan from an NRI or foreign director / shareholder to an Indian private company under the
2026 ECB framework. Demand: autocomplete sweep 18 Nov 2026 (ac9) - "loan from nri director to indian company", "can
nri director give loan to indian company", "loan from nri director to indian company pdf" in all 7 markets; no page.
Facts: FEM (Borrowing and Lending) (First Amendment) Regulations, 2026 - notification FEMA 3(R)(5)/2026-RB dated 9 Feb
2026, effective 16 Feb 2026 on publication; recognised lenders broadened to persons resident outside India, which can
include individuals (Bar & Bench / Singhania, CalcGuru); limit higher of USD 1 billion outstanding ECB or total
borrowing up to 300% of net worth (India Briefing, Bar & Bench, Vinod Kothari); MAMP 3 years (1-3 years for
manufacturing up to USD 150 million); no numeric all-in-cost ceiling for MAMP of 3 years or more, cost in line with
market, arm's length for related-party lenders; FCY or INR denomination; negative end-use list (real estate business,
chit/Nidhi, agriculture/plantation, TDR, securities trading except strategic corporate actions, on-lending for those);
Form ECB 1 for LRN through AD bank before drawdown, revised ECB 1 for changes, Form ECB 2 event-based within 7 days of
month-end (A.P. (DIR) Circular 23 of 18 Feb 2026 substituted the forms); from 1 Apr 2026 each delayed ECB 2 under an
LRN is a separate instance for late submission fee (Circular 25, 30 Mar 2026). Companies Act: Companies (Acceptance
of Deposits) Rules, 2014 rule 2(1)(c)(viii) - amount from a director (private company: also a director's relative)
with a written declaration that it is not borrowed is not a deposit; disclosed in DPT-3. Non-repatriation NRI rupee
loans under the 2026 regulations are framed for resident individual borrowers (India Briefing, CalcGuru) - companies
should use ECB or non-repatriable equity (NDI Rules Schedule IV). Tax: interest to a non-resident - TDS under section
393(2) of the Income-tax Act, 2025 (old section 195); section 115A 20% on interest on foreign-currency borrowing;
treaty rates e.g. UAE 12.5%, US/UK/Singapore 15% (non-bank lender) with TRC and Form 10F (Form 41). Sources checked
18 Nov 2026."""
from urllib.parse import quote
from build_lib import page, write_page

UPDATED = "Last updated: 18 November 2026."


def wa(t):
    return "https://wa.me/917801887130?text=" + quote(t)


def ul(*x):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in x) + "</ul>"


def table(head, rows):
    return ("<table><thead><tr>" + "".join(f"<th>{h}</th>" for h in head) + "</tr></thead><tbody>"
            + "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows) + "</tbody></table>")


CONTACT = ("Email info@bharatquantumprospera.com or WhatsApp +91 78018 87130 with the lender's country and residential status, the amount, currency, whether repayment must go abroad, and the company's net worth. "
           "We reply within one working day with the right route (ECB, director loan or equity), the filings and a fixed-scope quote.")
SLUG = "loan-from-nri-director-shareholder-to-indian-company-ecb-2026-rules"
BOX = (f'<div style="border:1px solid var(--line);border-left:4px solid #C2312A;border-radius:10px;padding:16px 18px;margin:18px 0;background:var(--bg-soft)">'
       f'<p style="margin:0 0 8px;font-weight:600">Get the loan registered before the money arrives.</p>'
       f'<p style="margin:0">A loan from abroad that reaches the company without a Loan Registration Number is a FEMA contravention, and fixing it means compounding. We structure the loan, draft the agreement, obtain the LRN through your bank and set up the ECB 2, TDS and DPT-3 filings. '
       f'<a href="{wa("Hi Durgesh, an NRI director wants to lend money to our Indian company. Which route should we use?")}" target="_blank" rel="noopener"><strong>WhatsApp CA Durgesh Chavda</strong></a>.</p></div>')

PAGES = [dict(
    slug=SLUG,
    title="Loan from an NRI Director or Foreign Shareholder to an Indian Company (2026): ECB Rules, Director Loan Exemption, TDS on Interest and Filings",
    em="for NRI founders in the Gulf, US, UK and Singapore funding their Indian company.",
    kicker="/ NRIs &middot; Foreign shareholders &middot; FEMA &middot; Updated 2026-11-18",
    lead=("Yes, an NRI director or a foreign shareholder can lend money to an Indian private company. Under the <strong>revised External Commercial Borrowing (ECB) framework in force from 16 February 2026</strong>, any person resident outside India, including an individual NRI, can be a recognised lender. There is no longer any need to hold a minimum equity stake. "
          "The loan must have a <strong>minimum average maturity of three years</strong> and be priced in line with the market (at arm's length for a related party). It can be in <strong>foreign currency or rupees</strong> and can be repaid abroad. Before drawdown the company obtains a <strong>Loan Registration Number (LRN)</strong> by filing <strong>Form ECB 1</strong> through its bank, then files <strong>Form ECB 2</strong> within 7 days after each month with a drawdown or repayment. "
          "Under company law, a loan from a <strong>director</strong> (in a private company, also a director's relative) who declares in writing that the money is not borrowed is <strong>not a deposit</strong>; it is disclosed in the annual <strong>DPT-3</strong>. The company deducts <strong>TDS on interest</strong> paid to the NRI, at the treaty rate where a tax residency certificate is provided."),
    sections=[
        ("/ The routes compared", "Which one fits.",
         table(["Route", "Best for", "Key conditions", "Filings"], [
             ["ECB (repatriable loan)", "NRI or foreign director or shareholder who wants interest and principal back abroad", "Minimum average maturity 3 years; market-level cost (arm's length if related); permitted end-use; within the higher of USD 1 billion outstanding or borrowing up to 300% of net worth", "Form ECB 1 for the LRN before drawdown; Form ECB 2 within 7 days of the end of each month with a drawdown or repayment; revised ECB 1 for changes"],
             ["Director loan under the Companies Act", "Company law side of any loan from a director", "Director's written declaration that the money is their own and not borrowed; private company: director's relatives also covered", "Board resolution; disclosure in DPT-3 by 30 June; for a non-resident lender, FEMA still applies (normally ECB)"],
             ["Equity on non-repatriation basis", "NRI happy to keep the money in India long term", "Treated like a domestic investment under the FEMA (Non-Debt Instruments) Rules, Schedule IV; not a loan", "Share allotment under the Companies Act (PAS-3); no interest"],
             ["Equity or convertible notes (repatriable FDI)", "Start-ups and companies planning a fund-raise", "Pricing rules; sector caps; startup convertible notes for recognised startups", "FC-GPR within 30 days of allotment; FLA return"]])
         + BOX),
        ("/ The 2026 ECB rules in practice", "What changed on 16 February 2026.",
         ul("<strong>Who can lend:</strong> recognised lenders now include persons resident outside India, which can include individuals, so an NRI director in Dubai, London or Singapore can lend directly. The earlier minimum shareholding test for foreign equity holders no longer applies.",
            "<strong>How much:</strong> the higher of USD 1 billion of outstanding ECB, or total outstanding borrowing (foreign and domestic) of up to 300% of net worth on the last audited balance sheet.",
            "<strong>Maturity:</strong> three years minimum average maturity (manufacturing companies can borrow for one to three years up to USD 150 million outstanding).",
            "<strong>Cost:</strong> no fixed all-in-cost ceiling for loans of three years or more; the rate must be in line with market conditions, and at arm's length where the lender is a related party. Transfer pricing applies if the lender is an associated enterprise.",
            "<strong>End-use:</strong> working capital and general corporate purposes are generally allowed; the negative list includes real estate business (with exceptions such as construction-development and own-use premises), chit funds and Nidhi companies, agriculture and plantations, trading in transferable development rights, investing in securities other than strategic corporate actions, and on-lending for these.",
            "<strong>Reporting:</strong> monthly ECB 2 returns were replaced by event-based returns within 7 days of the end of the month in which a drawdown or repayment happens. From 1 April 2026 each late ECB 2 under an LRN counts as a separate instance for the late submission fee.",
            "<strong>Non-repatriation rupee loans from NRIs</strong> under the 2026 regulations are framed for resident individual borrowers, with repayment only to the NRO account. For a company, use ECB, a properly documented director loan that also meets FEMA, or non-repatriable equity; confirm the route with your bank before the money moves.")),
        ("/ Tax and company law", "Interest, TDS and deposits.",
         ul("<strong>TDS on interest:</strong> interest paid to a non-resident is subject to withholding under section 393(2) of the Income-tax Act, 2025 (section 195 of the 1961 Act). Interest on a foreign-currency loan is taxed at 20% under the domestic rule (plus surcharge and cess); a tax treaty can lower this, for example 12.5% under the India-UAE treaty and 15% under the US, UK and Singapore treaties for non-bank lenders, with a tax residency certificate and Form 10F (Form 41 under the new rules). Remittances need Form 15CA/15CB (Forms 145/146).",
            "<strong>Interest deduction:</strong> where interest to a non-resident associated enterprise exceeds INR 1 crore, the thin-capitalisation cap (30% of EBITDA) can restrict the deduction.",
            "<strong>Deposit rules:</strong> under rule 2(1)(c)(viii) of the Companies (Acceptance of Deposits) Rules, 2014, money from a director who gives a written declaration that it is not borrowed is not a deposit. A plain loan from a shareholder who is not a director or relative needs to fit the member-deposit route or be structured differently. All exempt receipts are reported in <a href=\"form-dpt-3-return-of-deposits-india-2026.html\">Form DPT-3</a>.",
            "<strong>Already received the money without an LRN?</strong> Stop further drawdowns, obtain the LRN, and regularise the delay through the bank (late submission fee) or compounding; see <a href=\"fema-compounding-foreign-subsidiary-india.html\">FEMA compounding</a>.")
         + '<p>Related: <a href="nominee-resident-director-india-foreign-company.html">resident director for a foreign-owned company</a> &middot; <a href="india-uae-dtaa-for-nris-dubai-nro-interest-mutual-funds-property-trc-2026.html">India-UAE treaty for NRIs</a> &middot; <a href="repatriate-money-from-india-to-abroad-nro-usd-1-million-15ca-15cb-2026.html">repatriating money from India</a> &middot; <a href="foreign-company-setup-indian-subsidiary-wos.html">setting up an Indian subsidiary</a>.</p>'
         + f'<p><strong>Sources:</strong> Foreign Exchange Management (Borrowing and Lending) (First Amendment) Regulations, 2026 (notification FEMA 3(R)(5)/2026-RB dated 9 February 2026, in force 16 February 2026); RBI A.P. (DIR Series) Circulars No. 23 (18 February 2026, revised Forms ECB 1 and ECB 2) and No. 25 (30 March 2026, late submission fee per return); Companies (Acceptance of Deposits) Rules, 2014; Income-tax Act, 2025. Secondary summaries checked 18 November 2026: India Briefing, Bar &amp; Bench (Singhania &amp; Partners), Vinod Kothari, EY, CalcGuru. <em>{UPDATED}</em> General information; confirm the structure with your AD bank before funds move.</p>'),
    ],
    faqs=[("Can an NRI director give a loan to an Indian private company?", "Yes. Since 16 February 2026 any person resident outside India, including an individual NRI, can lend as a recognised ECB lender. The company needs a Loan Registration Number through its bank before drawdown, a three-year minimum average maturity and a market-level interest rate."),
          ("Is a loan from a director a deposit under the Companies Act?", "No, if the director gives a written declaration that the money is their own and not borrowed (rule 2(1)(c)(viii) of the Deposit Rules). In a private company, loans from a director's relatives are also covered. The amount is still reported in DPT-3."),
          ("Does the company need RBI approval for a loan from a foreign shareholder?", "Not usually. ECB within the limits and conditions is under the automatic route: the company files Form ECB 1 with its authorised dealer bank to get an LRN, then Form ECB 2 for each month with a drawdown or repayment."),
          ("Can an NRI lend from an NRO account without ECB?", "The 2026 non-repatriation NRI loan route is framed for resident individual borrowers. For a company, use ECB, a director loan that also meets FEMA, or non-repatriable equity, and confirm with the bank first."),
          ("What TDS applies on interest paid to an NRI lender?", "Withholding under section 393(2) of the Income-tax Act, 2025: 20% plus surcharge and cess on interest on a foreign-currency loan under domestic law, or the lower treaty rate (for example 12.5% for UAE, 15% for US, UK and Singapore non-bank lenders) with a TRC and Form 10F."),
          ("Can BQP set up the loan and filings?", "Yes. " + CONTACT)],
    related=[("form-dpt-3-return-of-deposits-india-2026.html", "Form DPT-3 return of deposits"), ("fema-compounding-foreign-subsidiary-india.html", "FEMA compounding"),
             ("nominee-resident-director-india-foreign-company.html", "Resident director for a foreign-owned company")],
    cta_h="An NRI director or foreign shareholder wants to lend?", cta_b=CONTACT,
    keywords="loan from NRI director to Indian company, can NRI director give loan to Indian company, foreign shareholder loan India ECB 2026, ECB new framework 2026, ECB 1 LRN, ECB 2 event based reporting, director loan deposit exemption rule 2(1)(c)(viii), TDS on interest to NRI lender",
    desc="Loan from an NRI director or foreign shareholder to an Indian company (2026): revised ECB framework from 16 Feb 2026 (individual non-resident lenders, 3-year MAMP, USD 1 billion / 300% net worth limit, ECB 1 LRN, event-based ECB 2), director loan deposit exemption and DPT-3, TDS on interest and treaty rates.",
    howto={"name": "How an Indian company takes a loan from an NRI director or foreign shareholder", "description": "Steps under the 2026 ECB framework.", "steps": [
        {"name": "Choose the route", "text": "Repatriable ECB, director loan meeting FEMA, or non-repatriable equity, depending on whether money must return abroad."},
        {"name": "Sign the loan agreement", "text": "Three-year minimum average maturity, market-level interest, permitted end-use; board resolution and director's own-funds declaration."},
        {"name": "Get the LRN", "text": "File Form ECB 1 through the authorised dealer bank before the first drawdown."},
        {"name": "Receive and report", "text": "Receive funds through banking channels; file Form ECB 2 within 7 days after each month with a drawdown or repayment."},
        {"name": "Pay interest correctly", "text": "Deduct TDS at the domestic or treaty rate, file Forms 15CA/15CB, report in DPT-3 and the financial statements."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch DA complete")
