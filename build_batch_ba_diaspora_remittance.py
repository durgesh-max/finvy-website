# -*- coding: utf-8 -*-
"""Batch BA: Indians in the UK, US, Canada, Australia and Europe moving money to and from India, plus FAST-DS for foreign
pensions. Checker logic: tools/nri-money-transfer-logic.js (tests: node tools/nri-money-transfer-logic.test.js).
Facts as at 6 November 2026: LRS USD 250,000 and TCS from 1 April 2026 (Finance Act 2026: 2% education/medical above
INR 10 lakh, flat 2% tour packages, 20% other above INR 10 lakh); NRO repatriation USD 1 million per financial year;
Form 15CA/15CB = Form 145/146 under the Income-tax Act, 2025; UK FIG regime from 6 April 2025 and TRF 12% (2025-26,
2026-27) / 15% (2027-28); US 1% remittance excise tax from 1 January 2026, Form 3520 USD 100,000, FBAR USD 10,000,
Form 8938 USD 50,000/75,000, 2026 gift exclusion USD 19,000; Canada T1135 CAD 100,000; Australia TA 2021/2."""
import json
import re
from urllib.parse import quote
from build_lib import page, write_page

DOMAIN = "https://bharatquantumprospera.com"
UPDATED = "Last updated: 6 November 2026."


def wa(topic):
    return "https://wa.me/917801887130?text=" + quote(f"Hi Durgesh, I live in {topic} and need help moving money to/from India. My situation: ")


def contact(where):
    return (f"WhatsApp +91 78018 87130 or email durgesh@bharatquantumprospera.com: tell us where you live ({where}), how much you want to move and from which "
            "account. We reply the same working day with what is needed and a fixed-scope quote. Form 15CB can usually be issued within 24 hours once documents are complete.")


def ul(*items):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


def cta_box(where, text="Moving money and not sure what applies?"):
    return (f'<div style="border:1px solid var(--line);border-radius:10px;padding:16px 18px;margin:18px 0;background:var(--bg-soft)">'
            f'<p style="margin:0 0 8px;font-weight:600">{text}</p>'
            f'<p style="margin:0">Use the free <a href="nri-send-money-to-from-india-checker.html">send-money checker</a> or message CA Durgesh Chavda on '
            f'<a href="{wa(where)}" target="_blank" rel="noopener"><strong>WhatsApp</strong></a> with your country, amount and account.</p></div>')


INDIA_SIDE = ("<table><thead><tr><th>Money</th><th>Can it leave India?</th><th>Paperwork</th></tr></thead><tbody>"
              "<tr><td>NRE or FCNR deposit (principal and interest)</td><td>Yes, freely, no annual limit</td><td>Usually just your bank's declaration</td></tr>"
              "<tr><td>NRO balance: rent, dividends, pension, interest, savings from before you left</td><td>Up to USD 1 million per financial year (April to March)</td><td>Form 15CA online + CA certificate in Form 15CB (Form 145/146 from 1 April 2026)</td></tr>"
              "<tr><td>Sale of Indian property</td><td>Within the USD 1 million limit; the original foreign-exchange investment for up to two residential properties can go on top</td><td>Buyer's TDS, optional lower deduction certificate, then 15CA/15CB</td></tr>"
              "<tr><td>Resident parents sending money to you</td><td>Up to USD 250,000 per parent per financial year under LRS</td><td>PAN, Form A2; TCS 20% above INR 10 lakh for gifts (2% for education or medical)</td></tr></tbody></table>")
TO_INDIA = ul("<strong>Into your NRE account</strong>: only money earned or held abroad; interest is tax-free in India while you are non-resident and stays freely repatriable.",
              "<strong>Into your NRO account</strong>: allowed; NRO interest is taxable in India (tax deducted at source, reducible to the treaty rate with a tax residency certificate and Form 10F).",
              "<strong>To parents or other relatives</strong>: a gift from a relative is not taxable for them in India, whatever the amount. Keep the bank's inward remittance advice and a short gift note.",
              "<strong>To friends</strong>: gifts from non-relatives are taxable for the receiver once the year's total exceeds INR 50,000, and then in full.")
SRC_IN = f'<p><strong>India-side sources:</strong> FEMA and RBI Master Directions on remittance facilities for NRIs and the Liberalised Remittance Scheme; Income-tax Act and rules on Form 15CA/15CB; Finance Act 2026 for TCS from 1 April 2026. <em>{UPDATED}</em> General information, not advice for your situation.</p>'

COUNTRIES = {
    "UK": dict(name="the UK", adj="UK", slug="send-money-uk-to-india-india-to-uk-nri-tax-fema-2026",
               title="Send Money From the UK to India (and India to the UK) in 2026: Tax, FEMA and HMRC Rules for Indians in Britain",
               em="what HMRC and India each need.",
               lead=("Sending your own money from the UK to India needs no UK form and is not taxed in India; family in India pay no tax on gifts from you. Bringing money from India to the UK is just as simple from an NRE account, while NRO money (rent, dividends, property sale proceeds) can be repatriated up to USD 1 million a year with Form 15CA and a CA's Form 15CB. "
                     "Since 6 April 2025 the remittance basis has ended: UK residents are taxed on worldwide income, so interest and gains in India, even tax-free NRE interest, belong on your UK return. Former non-doms can bring older foreign income and gains to the UK at 12% under the Temporary Repatriation Facility in 2025-26 and 2026-27 (15% in 2027-28)."),
               outbound=ul("No UK tax or UK form on sending your own money to India; your bank may ask the source of funds for large transfers.",
                           "The UK has no gift tax, but gifts can fall into UK inheritance tax if you die within seven years. The GBP 3,000 annual exemption and regular gifts out of surplus income are exempt."),
               inbound=ul("Moving your own capital (savings, sale proceeds) into the UK is not itself taxed.",
                          "<strong>FIG regime</strong>: UK residents are taxed on worldwide income and gains. New arrivals with 10 prior tax years of non-UK residence can claim four years of relief on foreign income and gains.",
                          "<strong>Temporary Repatriation Facility</strong>: former remittance-basis users can designate pre-6 April 2025 foreign income and gains and pay 12% in 2025-26 and 2026-27, or 15% in 2027-28.",
                          "<strong>Indian income</strong> (NRO interest, rent, dividends, capital gains) goes on your UK self-assessment, with credit for Indian tax under the India-UK tax treaty. NRE interest is tax-free in India but taxable in the UK."),
               faq_c=[("Do I pay tax in India on money sent from the UK?", "No. Sending your own money to India is not taxed in India, and gifts to relatives are not taxable for them. Interest it earns in an NRO account is taxable in India; NRE interest is tax-free in India but taxable in the UK while you are UK resident."),
                      ("How much money can I bring from India to the UK?", "NRE and FCNR balances: no limit. NRO balances, including property sale proceeds: up to USD 1 million per financial year, with Form 15CA and a Chartered Accountant's Form 15CB."),
                      ("Is NRE interest taxable in the UK?", "Yes, for a UK resident. It is exempt in India while you are non-resident, so there is no Indian tax to credit; report it on your UK return. Under the FIG regime, qualifying new arrivals can claim relief for their first four years."),
                      ("What is the 12% Temporary Repatriation Facility?", "Former remittance-basis users can designate foreign income and gains that arose before 6 April 2025 and pay a flat 12% in 2025-26 and 2026-27 (15% in 2027-28) instead of normal UK rates. It can suit people with savings or gains built up in India.")]),
    "US": dict(name="the US", adj="US", slug="send-money-usa-to-india-india-to-usa-nri-tax-fema-2026",
               title="Send Money From the USA to India (and India to the USA) in 2026: 1% Remittance Tax, Form 3520, FBAR and FEMA",
               em="without IRS or FEMA surprises.",
               lead=("From the US: pay from your US bank account or card and the 1% federal remittance tax (from 1 January 2026) does not apply; it hits transfers paid in cash, money order or cashier's cheque. Gifts above USD 19,000 to one person in 2026 need Form 709, though tax is rarely due. Money received by relatives in India is tax-free for them. "
                     "From India: NRE balances move freely; NRO money (rent, dividends, property sale proceeds) up to USD 1 million a year with Form 15CA and a CA's Form 15CB. If you receive more than USD 100,000 in gifts from parents in India in a year, file Form 3520; Indian accounts above USD 10,000 in total need an FBAR."),
               outbound=ul("<strong>1% remittance tax</strong> (from 1 January 2026) on transfers funded with cash, money orders or cashier's cheques. Bank-account and US-card funded transfers are outside it.",
                           "<strong>Gift tax return</strong>: gifts above USD 19,000 per person in 2026 need Form 709; tax is rarely payable because of the lifetime exemption."),
               inbound=ul("<strong>Form 3520</strong>: if you receive more than USD 100,000 in a year as gifts from non-resident aliens (such as parents in India). It is a reporting form, not a tax, but late filing is penalised heavily.",
                          "<strong>FBAR and Form 8938</strong>: Indian bank accounts (NRE, NRO, FCNR) are foreign accounts. FBAR if the combined balance went above USD 10,000 at any time; Form 8938 above USD 50,000 at year-end or USD 75,000 at any time (single, living in the US).",
                          "<strong>Indian mutual funds</strong> are generally passive foreign investment companies (PFICs) for US persons, with punitive US tax: think before buying them.",
                          "<strong>NRE interest</strong> is tax-free in India but taxable in the US."),
               faq_c=[("Is there a tax on sending money from the US to India?", "Only the 1% federal remittance excise tax, from 1 January 2026, on transfers paid in cash, by money order or cashier's cheque. Transfers paid from a US bank account or US card are not covered. India does not tax the money received; gifts to relatives in India are tax-free for them."),
                      ("Do I need Form 3520 for money from my parents in India?", "Yes, if gifts from non-resident aliens total more than USD 100,000 in the year. It is information only, not a tax."),
                      ("Do I report my NRE account to the IRS?", "Yes. It counts towards the USD 10,000 FBAR threshold and Form 8938, and NRE interest is taxable on your US return even though it is tax-free in India."),
                      ("How much money can I bring from India to the US?", "NRE and FCNR balances: no limit. NRO balances and property sale proceeds: up to USD 1 million per financial year with Form 15CA and Form 15CB.")]),
    "CA": dict(name="Canada", adj="Canadian", slug="send-money-canada-to-india-india-to-canada-nri-tax-2026",
               title="Send Money From Canada to India (and India to Canada) in 2026: T1135, CRA and FEMA Rules for Indians in Canada",
               em="T1135, NRO limits and Form 15CB.",
               lead=("Sending your own money from Canada to India needs no Canadian form, Canada has no gift tax, and family in India pay no tax on gifts from you. Bringing money from India: NRE balances move freely; NRO money (rent, dividends, property sale proceeds) up to USD 1 million a year with Form 15CA and a CA's Form 15CB. "
                     "The point most Indians in Canada miss is Form T1135: if your Indian bank deposits, shares, mutual funds or rented property cost more than CAD 100,000 in total at any time in the year, you must file it, and Indian interest (even tax-free NRE interest) is taxable in Canada."),
               outbound=ul("No Canadian tax or form on sending your own money to India; Canada has no gift tax.",
                           "Attribution rules can apply to money lent or gifted to a spouse or minor child who invests it in Canada; money used by family in India is not affected."),
               inbound=ul("<strong>Form T1135</strong>: file if the total cost of specified foreign property was more than CAD 100,000 at any time in the year (simplified reporting up to CAD 250,000). Property used mainly personally is excluded; rented-out Indian property counts.",
                          "<strong>Worldwide income</strong>: Indian interest (including NRE interest), rent, dividends and gains go on your Canadian return, with foreign tax credit for Indian tax under the India-Canada treaty.",
                          "Money arriving from parents in India is not taxable in Canada."),
               faq_c=[("Do I need to file T1135 for my Indian bank accounts?", "Yes, if the total cost of your specified foreign property, including Indian deposits, shares, mutual funds and rented property, exceeded CAD 100,000 at any time in the year."),
                      ("Is money from my parents in India taxable in Canada?", "No. Canada has no gift tax and gifts are not income. Income the money later earns is taxable in the usual way."),
                      ("Is NRE interest taxable in Canada?", "Yes. It is tax-free in India while you are non-resident, but Canada taxes residents on worldwide income."),
                      ("How much can I transfer from India to Canada?", "NRE and FCNR: no limit. NRO and property sale proceeds: up to USD 1 million per financial year, with Form 15CA and Form 15CB.")]),
    "AU": dict(name="Australia", adj="Australian", slug="send-money-australia-to-india-india-to-australia-nri-tax-2026",
               title="Send Money From Australia to India (and India to Australia) in 2026: ATO, Gift and FEMA Rules for Indians in Australia",
               em="what the ATO and India each expect.",
               lead=("Sending your own money from Australia to India needs no ATO form and Australia has no gift tax; family in India pay no tax on gifts from you. Money coming from India: NRE balances move freely; NRO money (rent, dividends, property sale proceeds) up to USD 1 million a year with Form 15CA and a CA's Form 15CB. "
                     "A genuine gift from family in India is generally not assessable income in Australia, but keep the evidence: the ATO targets foreign income disguised as gifts or loans (Taxpayer Alert TA 2021/2), and Indian interest, rent and gains, even tax-free NRE interest, must be declared by Australian residents."),
               outbound=ul("No ATO form or Australian tax on sending your own money to India; Australia has no gift tax.",
                           "Banks report international transfers to AUSTRAC, so keep the reason and the source of funds on record.",
                           "Gifts can matter for Centrelink means tests if you receive payments."),
               inbound=ul("<strong>Gifts from family in India</strong>: generally not assessable. Keep a gift letter and the sender's bank record; the ATO watches for disguised income.",
                          "<strong>Trust money</strong> is different: distributions from a foreign trust can be taxable under section 99B.",
                          "<strong>Worldwide income</strong>: Indian interest (including NRE interest), rent, dividends and capital gains go on your Australian return, with a foreign income tax offset for Indian tax."),
               faq_c=[("Is money from my parents in India taxable in Australia?", "Generally no; Australia has no gift tax and a genuine gift is not income. Keep evidence that it is a gift, because the ATO targets foreign income disguised as gifts or loans."),
                      ("Do I declare my NRE interest in Australia?", "Yes. It is tax-free in India while you are non-resident, but Australian residents are taxed on worldwide income."),
                      ("How much money can I bring from India to Australia?", "NRE and FCNR balances: no limit. NRO balances and property sale proceeds: up to USD 1 million per financial year, with Form 15CA and Form 15CB."),
                      ("Do I need to report sending money to India to the ATO?", "No form is needed for your own money. Your bank reports international transfers to AUSTRAC as a matter of course.")]),
    "EU": dict(name="Europe", adj="European", slug="send-money-europe-to-india-germany-netherlands-ireland-nri-2026",
               title="Send Money From Germany, the Netherlands, Ireland or France to India (and Back) in 2026: FEMA, Tax and CRS for Indians in Europe",
               em="the India side, done right.",
               lead=("For Indians in Germany, the Netherlands, Ireland, France and the rest of Europe, the India side is the same everywhere: money you send home is not taxed in India and gifts to relatives are tax-free for them; NRE balances can be repatriated freely; NRO money (rent, dividends, property sale proceeds) up to USD 1 million a year with Form 15CA and a CA's Form 15CB. "
                     "On the European side, residents are generally taxed on worldwide income, so Indian interest (even tax-free NRE interest), rent and gains belong on your local return, and Indian banks report foreign residents' accounts under the Common Reporting Standard."),
               outbound=ul("Most European countries do not tax the sender on money sent abroad; some have gift taxes that can reach gifts by residents.",
                           "Banks may ask the source of funds for large transfers under anti-money-laundering rules."),
               inbound=ul("<strong>Worldwide income</strong>: declare Indian interest (including NRE interest), rent and gains locally, with credit under your country's tax treaty with India.",
                          "<strong>Common Reporting Standard</strong>: Indian financial institutions report accounts of foreign residents, so your tax office may already see your Indian balances.",
                          "<strong>Large gifts</strong> from family in India may fall under your country's gift or inheritance tax on the receiver, usually with family allowances: check before a big transfer."),
               faq_c=[("Is money sent from Germany or the Netherlands to India taxed in India?", "No. India does not tax money you send home, and gifts to relatives in India are tax-free for them."),
                      ("Can I bring money from India to Europe?", "Yes. NRE and FCNR balances freely; NRO balances and property sale proceeds up to USD 1 million per financial year, with Form 15CA and Form 15CB."),
                      ("Will my European tax office know about my Indian accounts?", "Very likely. India exchanges financial account information under the Common Reporting Standard, so declare Indian income on your local return."),
                      ("Is NRE interest taxable in Europe?", "In most countries, yes, for residents, because they are taxed on worldwide income. It is tax-free in India while you are non-resident.")]),
}

PAGES = []
for code, c in COUNTRIES.items():
    where = c["name"].replace("the ", "")
    PAGES.append(dict(
        slug=c["slug"], title=c["title"], em=c["em"], kicker=f"/ Indians in {where} &middot; Money to and from India &middot; Updated 2026-11-06", lead=c["lead"],
        sections=[
            (f"/ {where} to India", "Sending money home.", f"<h3>On the {c['adj']} side</h3>" + c["outbound"] + "<h3>On the Indian side</h3>" + TO_INDIA + cta_box(where)),
            (f"/ India to {where}", "Bringing money from India.", INDIA_SIDE + f"<h3>On the {c['adj']} side</h3>" + c["inbound"] +
             '<p>Step by step: <a href="repatriate-money-from-india-to-abroad-nro-usd-1-million-15ca-15cb-2026.html">how to repatriate money from India</a>.</p>'),
            ("/ Indian income while abroad", "Tax in both places, credit once.",
             ul("Interest on NRO deposits, rent and capital gains in India are taxed in India first, usually by tax deducted at source.",
                "With a tax residency certificate from your country and Form 10F, the bank can deduct at the treaty rate instead of the full rate, and you claim credit for Indian tax on your local return.",
                "File an Indian return to claim refunds of excess TDS and to carry forward losses.",
                'Moving back to India one day? Foreign accounts and pensions must be reported once you become resident and ordinarily resident. If you missed that, see <a href="fast-ds-uk-pension-isa-canada-rrsp-australia-super-schedule-fa.html">FAST-DS for foreign pensions and accounts</a> (declarations close 31 December 2026).') + SRC_IN),
            ("/ How we help", "Indian side, end to end.",
             ul("Form 15CB certificates and Form 15CA filing for NRO and property repatriation, usually within 24 hours of complete documents.",
                "Lower TDS certificates for property sales, Indian tax returns, refunds and treaty claims (TRC and Form 10F).",
                "Planning large transfers: which account, which financial year, LRS limits for parents, gift documentation.",
                f"We coordinate with your {c['adj']} tax adviser on how Indian income is reported there.") + cta_box(where, "Talk to a CA before you move money")),
        ],
        faqs=c["faq_c"] + [("Can Bharat Quantum Prospera help me from " + where + "?", "Yes, fully online. " + contact(where))],
        related=[("nri-send-money-to-from-india-checker.html", "Send-money checker"), ("repatriate-money-from-india-to-abroad-nro-usd-1-million-15ca-15cb-2026.html", "Repatriate money from India"),
                 ("form-15ca-15cb-foreign-remittance-india.html", "Form 15CA/15CB guide"), ("nre-nro-fcnr-account-tax-rules.html", "NRE vs NRO vs FCNR")],
        cta_h=f"Moving money between {where} and India?", cta_b=contact(where),
        keywords=(f"send money from {where} to India tax, transfer money {where} to India NRI, bring money from India to {where}, NRO repatriation {where}, "
                  f"Form 15CB {where} NRI, NRE interest taxable {where}, gift from parents in India {where} tax, Indian CA for NRIs in {where}"),
        desc=(f"Indians in {where}: sending money to India (no Indian tax, gifts to relatives tax-free) and bringing it back (NRE free; NRO up to USD 1 million a year with Form 15CA/15CB), "
              f"plus the {c['adj']} rules that apply. Updated 6 November 2026."),
        howto=None))

# Repatriation guide (HowTo)
PAGES.append(dict(
    slug="repatriate-money-from-india-to-abroad-nro-usd-1-million-15ca-15cb-2026",
    title="How to Repatriate Money From India to the UK, US, Canada or Australia in 2026: NRO USD 1 Million, Form 15CA/15CB, Step by Step",
    em="from NRO account to your foreign bank.",
    kicker="/ Repatriation &middot; Step by Step &middot; Updated 2026-11-06",
    lead=("NRIs can send NRE and FCNR money abroad freely. NRO money (rent, dividends, pension, interest, old savings) and property sale proceeds can be repatriated up to USD 1 million per financial year, April to March. The bank needs Form 15CA filed online and, in most cases, a Chartered Accountant's Form 15CB confirming tax has been paid; from 1 April 2026 these are Form 145 and Form 146 under the Income-tax Act, 2025. "
          "With documents ready, a 15CB can be issued within a day and the remittance usually completes in a few working days."),
    sections=[("/ The limits", "What can leave India.", INDIA_SIDE + cta_box("my country")),
              ("/ Step by step", "NRO to your foreign account.",
               "<ol><li><strong>Check the source</strong>: NRE/FCNR (free) or NRO/property sale (USD 1 million a year).</li>"
               "<li><strong>Make sure Indian tax is settled</strong>: TDS on interest or rent, buyer's TDS on a property sale, or advance tax; file the Indian return where needed.</li>"
               "<li><strong>CA certificate (Form 15CB / Form 146)</strong>: the CA checks the nature of the money, tax paid and treaty position, and certifies it.</li>"
               "<li><strong>Form 15CA (Form 145)</strong>: filed online on the income tax portal using the 15CB details.</li>"
               "<li><strong>Bank request</strong>: submit 15CA, 15CB, the bank's remittance form and undertaking, and proof of source (sale deed, statements).</li>"
               "<li><strong>Remittance</strong>: the bank sends the money to your account abroad, usually within a few working days.</li></ol>"
               "<p>Selling property? Get a <a href=\"nri-india-property-ldc-lower-deduction-certificate.html\">lower deduction certificate</a> before the sale if the actual gain is small, and use our <a href=\"nri-property-tds-ldc-calculator.html\">property TDS calculator</a>.</p>" + SRC_IN),
              ("/ Common mistakes", "What delays repatriation.",
               ul("Trying to send NRO money directly without a 15CB when the bank needs one.",
                  "Unpaid tax on the income behind the money, or no Indian return filed for the sale year.",
                  "Crossing USD 1 million in one financial year: split the remittance across April.",
                  "Moving NRO money into NRE first: that transfer is itself a repatriation within the USD 1 million limit and needs the same paperwork."))],
    faqs=[("How much money can an NRI repatriate from India in a year?", "From NRO accounts, including property sale proceeds, up to USD 1 million per financial year (April to March). NRE and FCNR balances have no limit."),
          ("Is Form 15CB required for NRO repatriation?", "In most cases, yes: the bank asks for Form 15CA filed online and a Chartered Accountant's Form 15CB confirming the tax position. From 1 April 2026 they are Form 145 and Form 146."),
          ("How long does NRO repatriation take?", "With documents ready, the CA certificate can be issued within a day and the bank usually completes the remittance in a few working days."),
          ("Can I transfer NRO to NRE?", "Yes, but it counts as repatriation within the USD 1 million limit and needs the same 15CA/15CB paperwork."),
          ("Can BQP do my Form 15CB?", "Yes. " + contact("your country"))],
    related=[("nri-send-money-to-from-india-checker.html", "Send-money checker"), ("best-ca-form-15cb-foreign-remittance-india-same-day.html", "Same-day Form 15CB"),
             ("nri-selling-indian-property-capital-gains.html", "NRI property sale tax"), ("form-15ca-15cb-foreign-remittance-india.html", "Form 15CA/15CB guide")],
    cta_h="Need a Form 15CB this week?", cta_b=contact("your country"),
    keywords="repatriate money from India, NRO repatriation USD 1 million, how to transfer money from NRO to abroad, Form 15CA 15CB NRO repatriation, NRI repatriation process 2026, repatriate property sale proceeds India, Form 145 146 repatriation",
    desc="How NRIs repatriate money from India in 2026: NRE/FCNR freely; NRO and property sale proceeds up to USD 1 million a year with Form 15CA and a CA's Form 15CB (Form 145/146 from 1 April 2026). Steps, documents, timelines and common mistakes.",
    howto={"name": "How to repatriate NRO money from India", "description": "Repatriate NRO balances or property sale proceeds within the USD 1 million annual limit using Form 15CA and Form 15CB.", "steps": [
        {"name": "Check the source", "text": "Confirm whether the money is NRE/FCNR (freely repatriable) or NRO/property sale proceeds (USD 1 million per financial year)."},
        {"name": "Settle Indian tax", "text": "Make sure TDS or tax on the income or sale has been paid and the return filed where required."},
        {"name": "Get Form 15CB", "text": "A Chartered Accountant certifies the nature of the payment and the tax position (Form 146 from 1 April 2026)."},
        {"name": "File Form 15CA", "text": "File Form 15CA online on the income tax portal using the 15CB details (Form 145 from 1 April 2026)."},
        {"name": "Submit to the bank", "text": "Give the bank 15CA, 15CB, its remittance form and proof of source; it remits to your foreign account."}]}))

# FAST-DS for foreign pensions and accounts
PAGES.append(dict(
    slug="fast-ds-uk-pension-isa-canada-rrsp-australia-super-schedule-fa",
    title="FAST-DS 2026 for UK Pensions and ISAs, Canadian RRSP/TFSA and Australian Super Not in Schedule FA",
    em="returning NRIs from the UK, Canada and Australia.",
    kicker="/ FAST-DS 2026 &middot; Returning NRIs &middot; Updated 2026-11-06",
    lead=("If you moved back to India from the UK, Canada or Australia and kept a pension, ISA, RRSP, TFSA, superannuation or bank account there, it had to be listed in the foreign-assets schedule (Schedule FA) of your Indian return from your first year as resident and ordinarily resident. "
          "Assets built from income earned while you were non-resident and not reported fall in Category 2 of FAST-DS 2026: a flat fee of INR 1 lakh if the value is INR 5 crore or less. Interest or dividends actually earned in resident years and not offered to tax are Category 1 (60%). Declarations close on 31 December 2026."),
    sections=[("/ Typical holdings", "How each is usually treated.",
               "<table><thead><tr><th>Holding</th><th>If built while non-resident and not in Schedule FA</th><th>Watch for</th></tr></thead><tbody>"
               "<tr><td>UK workplace pension or SIPP</td><td>Category 2 (INR 1 lakh, up to INR 5 crore)</td><td>India's relief for notified foreign retirement accounts (UK, US, Canada) under section 89A lets accruals be taxed on withdrawal</td></tr>"
               "<tr><td>UK ISA (cash or stocks)</td><td>Category 2</td><td>ISA interest and dividends are tax-free in the UK but taxable in India in resident years: unreported amounts are Category 1</td></tr>"
               "<tr><td>Canadian RRSP</td><td>Category 2</td><td>Canada is a notified country for section 89A</td></tr>"
               "<tr><td>Canadian TFSA</td><td>Category 2</td><td>Income inside it is tax-free in Canada, not in India once you are resident and ordinarily resident</td></tr>"
               "<tr><td>Australian superannuation</td><td>Category 2</td><td>Australia is not notified under section 89A: get the yearly position reviewed</td></tr>"
               "<tr><td>Foreign bank or brokerage account</td><td>Category 2</td><td>Unreported interest or dividends in resident years: Category 1</td></tr></tbody></table>"
               + cta_box("India (returned from abroad)", "Returned with a pension, ISA, RRSP or super?")),
              ("/ Before you file", "Check these first.",
               ul('Your residential status year by year since returning: RNOR years generally need no Schedule FA (<a href="residential-status-calculator-india-nri-rnor-section-6.html">residential status calculator</a>).',
                  "Whether any contributions were made from Indian income after you returned (Category 2 if that income was taxed in India).",
                  "Whether growth inside a foreign retirement account was taxable in India each year: a technical point that depends on the account and the treaty, so have it reviewed before choosing a category.",
                  "Total Category 2 value within INR 5 crore and Category 1 items within INR 1 crore.") +
               '<p>More: <a href="fast-ds-rsu-espp-us-shares-401k-which-category.html">FAST-DS for RSUs, ESPP and 401(k)</a>, <a href="fast-ds-returning-nri-foreign-accounts-not-reported.html">returning NRIs</a>, <a href="fast-ds-2026-eligibility-checker.html">eligibility checker</a>.</p>'
               f'<p><strong>Source:</strong> Finance Act, 2026, Chapter IV (sections 130 to 144), the Foreign Assets of Small Taxpayers Disclosure Scheme, 2026; section 89A of the Income-tax Act, 1961 and rule 21AAA. <em>{UPDATED}</em></p>')],
    faqs=[("Do I need FAST-DS for my UK pension after returning to India?", "If you have been resident and ordinarily resident and did not list it in Schedule FA, usually yes, under Category 2 (INR 1 lakh fee, value up to INR 5 crore) for a pension built while non-resident."),
          ("Is ISA income taxable in India?", "Yes, in years you are resident and ordinarily resident, even though it is tax-free in the UK. Unreported ISA interest or dividends are undisclosed foreign income (Category 1, 60%)."),
          ("Is Australian super covered by FAST-DS?", "Yes. Super built while non-resident and not reported after becoming resident and ordinarily resident is usually Category 2. Australia is not a notified country for section 89A, so have the yearly tax position reviewed."),
          ("What is the deadline?", "Declarations under FAST-DS 2026 close on 31 December 2026."),
          ("Can BQP file FAST-DS for my foreign pension?", "Yes. " + contact("India, returned from abroad"))],
    related=[("fast-ds-2026-eligibility-checker.html", "FAST-DS eligibility checker"), ("fast-ds-2026-filing-help-chartered-accountant.html", "FAST-DS filing help"),
             ("fast-ds-rsu-espp-us-shares-401k-which-category.html", "FAST-DS for RSUs and 401(k)")],
    cta_h="Declare your foreign pension before 31 December", cta_b=contact("India, returned from abroad"),
    keywords="FAST-DS UK pension, FAST-DS ISA, FAST-DS RRSP, FAST-DS TFSA, FAST-DS Australian super, UK pension Schedule FA returning NRI, ISA taxable in India, superannuation Schedule FA India, section 89A foreign retirement account",
    desc="FAST-DS 2026 for returning NRIs with a UK pension or ISA, Canadian RRSP/TFSA or Australian super missing from Schedule FA: usually Category 2 (INR 1 lakh, up to INR 5 crore); unreported income Category 1 (60%). Deadline 31 December 2026.",
    howto=None))

# Checker (tool)
LOGIC = open("tools/nri-money-transfer-logic.js", encoding="utf-8").read().replace(
    'if (typeof module !== "undefined") module.exports = { moneyTransfer: moneyTransfer, tcsOnLrs: tcsOnLrs };', "")
_lrs = open("lrs-tcs-calculator.html", encoding="utf-8").read()
CALC_CSS = re.sub(r"\.calc-hero[^\n]*\n", "", re.search(r"<style>(.*?)</style>", _lrs, re.S).group(1))
CALC_CSS += ("\n  .calc-embed .calc-main{padding:0;max-width:none}\n  .calc-embed .rtrace{margin:8px 0 0;padding-left:18px;font-size:13px;line-height:1.55}\n"
             "  .calc-embed .rtrace li{margin:0 0 6px}\n  .calc-embed .rsec{font-size:13px;margin:14px 0 0;font-weight:600}\n")


def fld(fid, label, hint, opts=None, num=None):
    if opts:
        ctrl = f'<select id="{fid}">' + "".join(f'<option value="{v}">{t}</option>' for v, t in opts) + "</select>"
    else:
        ctrl = f'<input id="{fid}" type="number" min="0" step="any" value="{num}" inputmode="decimal" />'
    return f'<div class="field" id="w_{fid}"><label for="{fid}">{label} <span class="hint">{hint}</span></label>{ctrl}</div>'


INPUTS = (fld("mCountry", "Where do you (or the person abroad) live?", "", [("UK", "United Kingdom"), ("US", "United States"), ("CA", "Canada"), ("AU", "Australia"), ("EU", "Europe (Germany, Netherlands, Ireland, France and others)")])
          + fld("mDir", "Which way is the money going?", "", [("toIndia", "From abroad to India"), ("fromIndia", "From India to abroad")])
          + fld("mFund", "How are you paying?", "Matters for the US 1% remittance tax.", [("bank", "From my bank account or card"), ("cash", "Cash, money order or cashier's cheque")])
          + fld("mCredit", "Where is it going in India?", "", [("relative", "To a relative (parents, spouse, siblings, children)"), ("ownNRE", "My own NRE account"), ("ownNRO", "My own NRO account"), ("nonRelative", "To a friend or someone who is not a relative")])
          + fld("mWho", "Who is sending it from India?", "", [("nri", "Me, an NRI, from my own Indian money"), ("resident", "A resident in India (for example my parents)")])
          + fld("mSource", "Which money?", "", [("NRO", "NRO account (rent, dividends, pension, savings)"), ("property", "Sale of Indian property"), ("NRE", "NRE account"), ("FCNR", "FCNR deposit")])
          + fld("mPurpose", "Purpose", "Decides the TCS rate.", [("gift", "Gift or maintenance for family abroad"), ("eduSelf", "Education (self-funded)"), ("eduLoan", "Education funded by a loan"), ("medical", "Medical treatment"), ("tour", "Overseas tour package"), ("investment", "Investment abroad")])
          + fld("mAmtINR", "Amount (INR)", "", num=1500000)
          + fld("mAmtUSD", "Amount (USD)", "", num=100000)
          + fld("mOtherGifts", "Other gifts from non-relatives this financial year (INR)", "For the INR 50,000 limit.", num=0)
          + fld("mNroSoFar", "Already repatriated from NRO this financial year (USD)", "For the USD 1 million limit.", num=0)
          + fld("mLrsSoFar", "Already sent abroad under LRS this financial year (INR)", "For the INR 10 lakh TCS threshold.", num=0)
          + fld("mRate", "Exchange rate (INR per USD)", "For the USD 250,000 LRS limit.", num=95))
CHECK_JS = LOGIC + r'''
(function(){
  function $(id){return document.getElementById(id);}
  function list(id, arr){$(id).innerHTML=arr.map(function(t){return "<li>"+t+"</li>";}).join(""); $(id+"H").style.display=arr.length?"":"none";}
  function vis(id, on){$("w_"+id).style.display=on?"":"none";}
  function show(){
    var dir=$("mDir").value, who=$("mWho").value, src=$("mSource").value, credit=$("mCredit").value;
    var into=dir==="toIndia", nri=!into&&who==="nri", res=!into&&who==="resident";
    vis("mFund",into&&$("mCountry").value==="US"); vis("mCredit",into); vis("mOtherGifts",into&&credit==="nonRelative");
    vis("mWho",!into); vis("mSource",nri); vis("mNroSoFar",nri&&(src==="NRO"||src==="property"));
    vis("mPurpose",res); vis("mLrsSoFar",res); vis("mRate",res&&$("mPurpose").value!=="eduLoan");
    vis("mAmtINR",!nri); vis("mAmtUSD",nri);
    var r=moneyTransfer({dir:dir,country:$("mCountry").value,fund:$("mFund").value,credit:credit,amountINR:Number($("mAmtINR").value),
      otherGiftsINR:Number($("mOtherGifts").value||0),who:who,source:src,amountUSD:Number($("mAmtUSD").value),nroSoFarUSD:Number($("mNroSoFar").value||0),
      purpose:$("mPurpose").value,lrsSoFarINR:Number($("mLrsSoFar").value||0),rate:Number($("mRate").value)});
    if(!r.ok){$("mOut").textContent="Check inputs";["mIndia","mForms","mLimits","mTax","mCountryOut"].forEach(function(id){list(id,[]);});list("mIndia",r.errors);return;}
    $("mOut").textContent=r.verdict;
    list("mIndia",r.india); list("mForms",r.forms); list("mLimits",r.limits); list("mTax",r.tax); list("mCountryOut",r.country);
  }
  ["mCountry","mDir","mFund","mCredit","mWho","mSource","mPurpose","mAmtINR","mAmtUSD","mOtherGifts","mNroSoFar","mLrsSoFar","mRate"].forEach(function(id){$(id).addEventListener("input",show);$(id).addEventListener("change",show);});
  show();
})();'''
WA_TOOL = "https://wa.me/917801887130?text=" + quote("Hi Durgesh, I used your send-money checker. I want to move money between India and: ")
app = {"@context": "https://schema.org", "@type": "WebApplication", "name": "Send Money To or From India Checker (UK, US, Canada, Australia, Europe)",
       "url": f"{DOMAIN}/nri-send-money-to-from-india-checker.html", "applicationCategory": "FinanceApplication", "operatingSystem": "Any",
       "description": "Shows the forms, limits, TCS and country-side reporting for sending money between India and the UK, US, Canada, Australia or Europe.",
       "offers": {"@type": "Offer", "price": "0", "priceCurrency": "INR"}, "author": {"@type": "Person", "name": "CA Durgesh Chavda", "url": f"{DOMAIN}/durgesh.html"},
       "publisher": {"@type": "AccountingService", "name": "Bharat Quantum Prospera", "url": DOMAIN}}
BLOCK = (f"<style>{CALC_CSS}</style>"
         f'<script type="application/ld+json">{json.dumps(app, separators=(",", ":"), ensure_ascii=False)}</script>'
         f'<div class="calc-embed"><div class="calc-main"><div class="calc-card"><h2>Your transfer</h2><p class="sub">Answer a few questions.</p>{INPUTS}</div>'
         '<div class="result-card"><div class="rlabel">Result</div><div class="rvalue red" id="mOut" style="font-size:22px;line-height:1.3">-</div>'
         '<p class="rsec" id="mIndiaH">In India</p><ul class="rtrace" id="mIndia"></ul>'
         '<p class="rsec" id="mFormsH">Forms</p><ul class="rtrace" id="mForms"></ul>'
         '<p class="rsec" id="mLimitsH">Limits</p><ul class="rtrace" id="mLimits"></ul>'
         '<p class="rsec" id="mTaxH">Tax</p><ul class="rtrace" id="mTax"></ul>'
         '<p class="rsec" id="mCountryOutH">Where you live</p><ul class="rtrace" id="mCountryOut"></ul>'
         f'<p style="font-size:13px;margin:14px 0 0"><a href="{WA_TOOL}" target="_blank" rel="noopener">Get this done by a CA (Form 15CB within 24 hours) &rarr;</a></p></div></div></div>'
         f"<script>{CHECK_JS}\n</script>")
PAGES.append(dict(
    slug="nri-send-money-to-from-india-checker",
    title="Send Money To or From India: Free Checker for Indians in the UK, US, Canada, Australia and Europe (2026)",
    em="forms, limits, TCS and tax in one place.",
    kicker="/ Free Tool &middot; Money to and from India &middot; Updated 2026-11-06",
    lead=("Pick your country, the direction and the money involved. The checker tells you what applies on the Indian side (NRE/NRO rules, the USD 1 million NRO limit, Form 15CA/15CB, the USD 250,000 LRS limit and TCS from 1 April 2026, gift rules for the receiver) and the main point to watch where you live: "
          "the 1% US remittance tax, Form 3520 and FBAR, the UK FIG regime, Canada's T1135, or the ATO's view of gifts."),
    sections=[("/ Checker", "Check your transfer.", BLOCK + '<p style="font-size:13px">General information based on the rules as at 6 November 2026, not advice for your situation.</p>'),
              ("/ Country guides", "Read more for where you live.",
               ul('<a href="send-money-uk-to-india-india-to-uk-nri-tax-fema-2026.html">United Kingdom</a>: FIG regime, 12% Temporary Repatriation Facility, NRE interest.',
                  '<a href="send-money-usa-to-india-india-to-usa-nri-tax-fema-2026.html">United States</a>: 1% remittance tax, Form 3520, FBAR, PFICs.',
                  '<a href="send-money-canada-to-india-india-to-canada-nri-tax-2026.html">Canada</a>: T1135 above CAD 100,000.',
                  '<a href="send-money-australia-to-india-india-to-australia-nri-tax-2026.html">Australia</a>: gifts, AUSTRAC, TA 2021/2.',
                  '<a href="send-money-europe-to-india-germany-netherlands-ireland-nri-2026.html">Europe</a>: worldwide income and CRS.',
                  '<a href="repatriate-money-from-india-to-abroad-nro-usd-1-million-15ca-15cb-2026.html">How to repatriate money from India</a>, step by step.')),
              ("/ Key numbers", "As at November 2026.",
               "<table><tbody><tr><td>NRO repatriation</td><td>USD 1 million per financial year</td></tr><tr><td>LRS (residents)</td><td>USD 250,000 per person per financial year</td></tr>"
               "<tr><td>TCS on LRS</td><td>20% above INR 10 lakh; 2% for self-funded education and medical above INR 10 lakh; nil for loan-funded education; flat 2% on tour packages</td></tr>"
               "<tr><td>Gifts from non-relatives</td><td>Taxable in full above INR 50,000 a year</td></tr><tr><td>US remittance tax</td><td>1% on cash-funded transfers from 1 January 2026</td></tr>"
               "<tr><td>US Form 3520</td><td>Gifts from non-resident aliens above USD 100,000 a year</td></tr><tr><td>Canada T1135</td><td>Foreign property cost above CAD 100,000</td></tr></tbody></table>" + SRC_IN)],
    faqs=[("How much money can an NRI send from India abroad?", "NRE and FCNR balances freely; NRO balances and property sale proceeds up to USD 1 million per financial year with Form 15CA and Form 15CB."),
          ("How much can my parents send me abroad?", "Up to USD 250,000 per parent per financial year under LRS. TCS of 20% applies on gifts above INR 10 lakh a year (2% for education or medical), refundable through their Indian return."),
          ("Is money sent to India taxable?", "Not in India for the transfer itself. Gifts to relatives are tax-free for them; gifts from non-relatives are taxable once the year's total exceeds INR 50,000."),
          ("Can BQP handle the paperwork?", "Yes. " + contact("your country"))],
    related=[("repatriate-money-from-india-to-abroad-nro-usd-1-million-15ca-15cb-2026.html", "Repatriate money from India"), ("lrs-tcs-calculator.html", "LRS TCS calculator"),
             ("nri-gift-indian-relatives-section-56-fema-2026.html", "Gifts to NRI relatives")],
    cta_h="Want a CA to handle the transfer paperwork?", cta_b=contact("your country"),
    keywords="send money to India checker, transfer money from India to UK USA Canada Australia, NRI money transfer rules 2026, how much money can NRI send from India, parents send money abroad LRS TCS 2026, NRO repatriation calculator, US remittance tax India, Form 3520 gift from parents India",
    desc="Free checker for Indians in the UK, US, Canada, Australia and Europe: forms, limits (NRO USD 1 million, LRS USD 250,000), TCS from 1 April 2026, gift tax rules and country-side reporting for sending money to or from India.",
    howto=None))

ALSO_READ = ("/ Also read", "Property, inheritance and study abroad.", ul(
    '<a href="sell-property-in-india-living-in-uk-usa-canada-australia-tax-both-countries-2026.html">Selling Indian property while living abroad</a>: tax in both countries and moving the money.',
    '<a href="inherit-money-property-from-india-living-in-uk-usa-canada-australia-2026.html">Inheriting money or property from India</a>: no Indian inheritance tax, Form 3520, repatriation.',
    '<a href="parents-send-money-child-studying-abroad-uk-usa-canada-australia-lrs-tcs-2026.html">Parents paying for study abroad</a>: LRS and TCS of nil, 2% or 20%.',
    '<a href="nri-money-transfer-questions-answered-uk-usa-canada-australia-2026.html">28 questions answered</a> about moving money to and from India.'))
for p in PAGES:
    p["sections"] = p["sections"] + [ALSO_READ]
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"],
                hero_kicker=p["kicker"], hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>',
                hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]],
                cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print(f"Batch BA complete: {len(PAGES)} pages")
