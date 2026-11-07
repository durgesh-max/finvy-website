# -*- coding: utf-8 -*-
"""Batch BB: Indians in the UK, US, Canada and Australia, part 2: selling Indian property while living abroad (both
countries' tax), inheriting from India, parents paying for study abroad (LRS/TCS), and a 30-question money-transfer FAQ.
Facts as at 7 November 2026:
India: NRI long-term gains on property 12.5% without indexation (the 20%-with-indexation option for property bought
before 23 July 2024 is for resident individuals/HUFs only); short-term at slab rates (TDS 30%); buyer deducts TDS plus
surcharge and cess, in practice on the full price unless a lower deduction certificate (Form 128 under s.395 of the
Income-tax Act, 2025; Form 13 before April 2026) is obtained; buyers of NRI property can deposit TDS via Form 141 without
a TAN from 1 October 2026; NRO repatriation USD 1 million per financial year with Form 15CA/15CB (Form 145/146); no
inheritance tax in India; LRS USD 250,000; TCS from 1 April 2026: nil loan-funded education, 2% self-funded
education/medical above INR 10 lakh, 20% other purposes (incl. gifts/maintenance) above INR 10 lakh.
UK: CGT 18%/24%, GBP 3,000 annual exempt amount; overseas gains via Self Assessment; IHT residence-based from 6 April
2025 (long-term resident = 10 of the last 20 tax years). US: Form 8949/Schedule D, Form 1116, stepped-up basis on
inherited property, Form 3520 for gifts/bequests from foreign persons above USD 100,000, s.121 home-sale exclusion.
Canada: 50% inclusion rate (increase cancelled March 2025); deemed acquisition at fair market value on becoming
resident; T1135 above CAD 100,000. Australia: 50% CGT discount for residents (12 months), foreign income tax offset,
assets owned before becoming resident deemed acquired at market value then (s.855-45 ITAA 1997)."""
from urllib.parse import quote
from build_lib import page, write_page

UPDATED = "Last updated: 7 November 2026."


def wa(topic):
    return "https://wa.me/917801887130?text=" + quote(f"Hi Durgesh, {topic}. My situation: ")


def contact(where):
    return (f"WhatsApp +91 78018 87130 or email durgesh@bharatquantumprospera.com: tell us where you live ({where}) and what you want to do. "
            "We reply the same working day with what is needed and a fixed-scope quote. Form 15CB can usually be issued within 24 hours once documents are complete.")


def ul(*items):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


def ol(*items):
    return "<ol>" + "".join(f"<li>{i}</li>" for i in items) + "</ol>"


def table(head, rows):
    return ("<table><thead><tr>" + "".join(f"<th>{h}</th>" for h in head) + "</tr></thead><tbody>"
            + "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows) + "</tbody></table>")


def box(title, topic, extra=""):
    return (f'<div style="border:1px solid var(--line);border-left:4px solid #C2312A;border-radius:10px;padding:16px 18px;margin:18px 0;background:var(--bg-soft)">'
            f'<p style="margin:0 0 8px;font-weight:600">{title}</p>'
            f'<p style="margin:0">{extra}Message CA Durgesh Chavda on <a href="{wa(topic)}" target="_blank" rel="noopener"><strong>WhatsApp</strong></a> '
            f'or email <a href="mailto:durgesh@bharatquantumprospera.com">durgesh@bharatquantumprospera.com</a>. Or try the free '
            f'<a href="nri-send-money-to-from-india-checker.html">send-money checker</a>.</p></div>')


CHECKER = "nri-send-money-to-from-india-checker.html"
REPAT = "repatriate-money-from-india-to-abroad-nro-usd-1-million-15ca-15cb-2026.html"
GUIDES = ('<p>Country guides: <a href="send-money-uk-to-india-india-to-uk-nri-tax-fema-2026.html">UK</a> &middot; '
          '<a href="send-money-usa-to-india-india-to-usa-nri-tax-fema-2026.html">USA</a> &middot; '
          '<a href="send-money-canada-to-india-india-to-canada-nri-tax-2026.html">Canada</a> &middot; '
          '<a href="send-money-australia-to-india-india-to-australia-nri-tax-2026.html">Australia</a> &middot; '
          '<a href="send-money-europe-to-india-germany-netherlands-ireland-nri-2026.html">Europe</a></p>')
PAGES = []

# ---------------------------------------------------------------- 1. Property sale while living abroad
PROP_SLUG = "sell-property-in-india-living-in-uk-usa-canada-australia-tax-both-countries-2026"
PAGES.append(dict(
    slug=PROP_SLUG,
    title="Selling Property in India While Living in the UK, USA, Canada or Australia (2026): Tax in Both Countries and Moving the Money",
    em="India's TDS, your country's tax, and the transfer.",
    kicker="/ NRI property sale &middot; UK, US, Canada, Australia &middot; Updated 2026-11-07",
    lead=("India taxes an NRI's long-term gain on property at 12.5% without indexation (plus surcharge and cess), and the buyer deducts that tax at source, in practice on the whole price unless you obtain a lower deduction certificate (Form 128, the old Form 13). "
          "The country where you live usually taxes the same gain too: the UK at 18% or 24%, the US at 0%, 15% or 20%, Canada on 50% of the gain, and Australia with a 50% discount for residents. "
          "You do not pay twice in full: the Indian tax is credited against the foreign tax under the tax treaty. Then the proceeds go to your NRO account and can be sent abroad within USD 1 million a year with Form 15CA and a CA's Form 15CB."),
    sections=[
        ("/ The India side", "What happens in India.",
         table(["Point", "Rule for an NRI seller (2026)"], [
             ["Long-term (held more than 24 months)", "12.5% without indexation, plus surcharge and cess. The 20%-with-indexation option for property bought before 23 July 2024 is available only to resident individuals and HUFs, not NRIs."],
             ["Short-term (24 months or less)", "Taxed at slab rates; the buyer deducts 30% plus surcharge and cess."],
             ["TDS by the buyer", "On an NRI sale the buyer must deduct tax at source. Without a certificate, buyers and banks deduct on the full sale price, which can be many times the actual tax. From 1 October 2026 a buyer can deposit it using Form 141 without a TAN."],
             ["Lower deduction certificate", "Apply online (Form 128 under section 395 of the Income-tax Act, 2025; Form 13 before April 2026) with the purchase cost and computation, so TDS is limited to the real tax. Apply before the sale agreement is signed."],
             ["Reinvestment exemptions", "Section 54 (section 82 of the 2025 Act) for a new house in India; section 54EC (section 85) bonds up to INR 50 lakh within six months. Both reduce Indian tax, but the gain may still be taxable where you live."],
             ["Indian return", "File the Indian return for the year of sale to claim back excess TDS and report the gain."],
             ["Moving the money", "Proceeds into your NRO account; repatriate up to USD 1 million per financial year with Form 15CA and Form 15CB. The foreign exchange you originally paid for up to two residential properties can go on top."],
         ])
         + '<p>Calculators: <a href="nri-property-tds-ldc-calculator.html">NRI property TDS and lower deduction certificate calculator</a> &middot; <a href="nri-india-property-ldc-lower-deduction-certificate.html">how the certificate works</a> &middot; <a href="buying-property-from-nri-no-tan-form-141-from-1-october-2026.html">buyer\'s Form 141</a>.</p>'
         + box("Selling soon? Apply for the certificate before you sign.", "I am an NRI selling property in India")),
        ("/ The country where you live", "How the same gain is taxed abroad.",
         table(["Country", "How the gain is taxed", "Credit for Indian tax", "Points people miss"], [
             ["United Kingdom", "Capital gains tax at 18% (within the basic-rate band) or 24%, after the GBP 3,000 annual exempt amount. Reported on your Self Assessment return for the tax year of sale (the 60-day reporting rule is for UK property).",
              "Foreign tax credit relief for Indian tax under the India-UK treaty, up to the UK tax on the same gain.",
              "The gain is worked out in pounds: cost converted at the rate when you bought, proceeds at the rate when you sold, so a falling rupee can shrink or wipe out the gain in GBP terms. New arrivals under the FIG regime may claim relief for gains in their first four years."],
             ["United States", "Long-term gains at 0%, 15% or 20%, plus the 3.8% net investment income tax above the income thresholds. Reported on Form 8949 and Schedule D.",
              "Foreign tax credit on Form 1116, up to the US tax on that gain; any excess can be carried forward.",
              "Gain worked out in dollars. If it was your main home for 2 of the last 5 years, the section 121 exclusion (USD 250,000, or 500,000 for a married couple filing jointly) can apply to an Indian home. Inherited property gets a stepped-up basis (value at death)."],
             ["Canada", "50% of the gain is taxable at your marginal rate (the planned increase to two-thirds was cancelled in March 2025).",
              "Foreign tax credit for Indian tax on the gain.",
              "If you owned the property before moving to Canada, you are treated as having bought it at its fair market value on the day you became resident, so only the growth since then is taxed in Canada. Keep a valuation from that date. Indian property held for rent counts towards the CAD 100,000 T1135 limit."],
             ["Australia", "Australian residents get the 50% CGT discount if the property was held for at least 12 months; the rest is added to taxable income.",
              "Foreign income tax offset for the Indian tax, limited to the Australian tax on the same gain (and halved in line with the discount).",
              "Property owned before you became an Australian resident is treated as acquired at its market value on that date, so get a valuation. The discount is reduced for periods you were a foreign resident after 8 May 2012."],
         ])
         + "<p>Europe works on the same idea: residents of Germany, the Netherlands, Ireland, France and most of Europe are taxed on worldwide gains, with a credit for Indian tax under each treaty. The rules on property held for many years differ by country (Germany, for example, generally exempts private property sold after 10 years).</p>"
         + GUIDES),
        ("/ A worked example", "A flat in Pune bought in 2012, sold in 2026.",
         "<p>An NRI living in the UK sells a flat for INR 1.5 crore that cost INR 50 lakh in 2012. India: long-term gain INR 1 crore, tax at 12.5% = INR 12.5 lakh, plus 15% surcharge and 4% cess = about INR 14.95 lakh. Without a certificate, the buyer would deduct the same 14.95% on the full INR 1.5 crore, about INR 22.4 lakh, and the excess of about INR 7.5 lakh comes back only after the Indian return is processed.</p>"
         "<p>UK: the cost converted in 2012 at about INR 85 to the pound was about GBP 58,800; the proceeds at about INR 120 to the pound are about GBP 125,000. UK gain about GBP 66,200, less the GBP 3,000 exempt amount, at 24% = about GBP 15,200. The Indian tax of about GBP 12,500 (INR 14.95 lakh converted) is credited, leaving about GBP 2,700 payable in the UK.</p>"
         "<p>Figures are rounded and for illustration; exchange rates, surcharge and the UK band depend on the facts.</p>"),
        ("/ Order of steps", "Do it in this order.",
         ol("Collect the purchase deed, improvement bills and loan papers, and work out the gain in rupees and in your home currency.",
            "Apply for the lower deduction certificate before signing the agreement.",
            "Sign and register the sale; the buyer deducts TDS at the certificate rate and gives you the TDS certificate.",
            "Get the proceeds into your NRO account (not NRE).",
            "Get Form 15CB from a CA and file Form 15CA; the bank remits to your foreign account.",
            "File the Indian return for the year, then declare the gain on your UK, US, Canadian or Australian return with the foreign tax credit.")
         + f'<p><strong>Sources:</strong> Income-tax Act, 2025 and Finance (No. 2) Act, 2024 (12.5% from 23 July 2024); FEMA and RBI Master Direction on remittance facilities for NRIs; HMRC capital gains manuals; IRS Form 8949, Form 1116 and Publication 523; CRA guidance on the inclusion rate and immigrants; ATO guidance on CGT and becoming a resident. <em>{UPDATED}</em> General information, not advice for your situation.</p>'),
    ],
    faqs=[("Do I pay tax in India and in the UK, US, Canada or Australia when I sell my Indian property?", "Usually both countries tax the gain, but the Indian tax is credited against the foreign tax under the tax treaty, so in total you pay roughly the higher of the two, not both in full."),
          ("What is the capital gains tax rate for an NRI selling property in India in 2026?", "12.5% without indexation on long-term gains (held more than 24 months), plus surcharge and cess. Short-term gains are taxed at slab rates, with 30% TDS. NRIs cannot use the 20%-with-indexation option for property bought before 23 July 2024; that is for residents."),
          ("Why does the buyer deduct TDS on the full sale price?", "Without a lower deduction certificate the buyer cannot verify your cost, so TDS is deducted on the whole price. Apply for the certificate (Form 128, previously Form 13) before the sale so TDS matches the real tax."),
          ("How do I get the sale money out of India?", "The proceeds go to your NRO account. You can repatriate up to USD 1 million per financial year with Form 15CA and a Chartered Accountant's Form 15CB. The foreign exchange originally invested in up to two residential properties can be sent on top."),
          ("I bought the flat before moving to Canada or Australia. Is the whole gain taxed there?", "No. Both countries treat you as having acquired it at market value when you became resident, so only the growth after that date is taxed there. Keep a valuation from that date."),
          ("Can BQP handle the certificate, the return and the transfer?", "Yes: lower deduction certificate, Indian return, Form 15CB and repatriation, with a computation your foreign accountant can use. " + contact("UK, US, Canada or Australia"))],
    related=[("nri-selling-indian-property-capital-gains.html", "NRI property sale: capital gains in India"), ("nri-property-tds-ldc-calculator.html", "Property TDS and LDC calculator"),
             (REPAT, "Repatriate money from India"), (CHECKER, "Send-money checker")],
    cta_h="Selling in India while living abroad?", cta_b=contact("UK, US, Canada or Australia"),
    keywords="NRI selling property in India living in UK, sell property in India from USA tax, NRI property sale Canada tax, sell Indian property Australia CGT, capital gains tax both countries India UK, foreign tax credit Indian property sale, Form 128 lower TDS certificate NRI, repatriate property sale proceeds India 2026",
    desc="NRIs in the UK, US, Canada and Australia selling Indian property in 2026: India's 12.5% tax and TDS, the lower deduction certificate (Form 128), how each country taxes the same gain with a credit for Indian tax, and repatriating the money (USD 1 million a year).",
    howto={"name": "How to sell property in India while living abroad and move the money", "description": "Steps for an NRI in the UK, US, Canada or Australia to sell Indian property, limit TDS, and repatriate the proceeds with the foreign tax credit.", "steps": [
        {"name": "Work out the gain in both currencies", "text": "Collect the purchase deed and bills and compute the gain in rupees and in your home currency."},
        {"name": "Apply for a lower deduction certificate", "text": "Apply on Form 128 (formerly Form 13) before signing, so the buyer deducts TDS only on the real tax."},
        {"name": "Complete the sale", "text": "Register the sale; the buyer deducts TDS at the certificate rate and issues the TDS certificate."},
        {"name": "Receive into NRO", "text": "Have the proceeds credited to your NRO account."},
        {"name": "Repatriate with 15CA/15CB", "text": "Get Form 15CB from a CA, file Form 15CA online and ask the bank to remit, within USD 1 million per financial year."},
        {"name": "File in both countries", "text": "File the Indian return, then report the gain abroad and claim credit for the Indian tax under the treaty."}]}))

# ---------------------------------------------------------------- 2. Inheritance
INH_SLUG = "inherit-money-property-from-india-living-in-uk-usa-canada-australia-2026"
PAGES.append(dict(
    slug=INH_SLUG,
    title="Inheriting Money or Property From India While Living in the UK, USA, Canada or Australia (2026): Tax, Reporting and Transfer",
    em="what India and your country each need.",
    kicker="/ Inheritance &middot; UK, US, Canada, Australia &middot; Updated 2026-11-07",
    lead=("India has no inheritance or estate tax, and receiving an inheritance is not income for the heir. The UK, Canada and Australia do not tax the heir on receiving it either, and the US does not tax it, though a US person must report an inheritance from a non-US person above USD 100,000 on Form 3520. "
          "What is taxed is what the inheritance earns or gains afterwards. The money itself lands in an NRO account and can be sent abroad within USD 1 million a year with documents proving the inheritance, Form 15CA and a CA's Form 15CB."),
    sections=[
        ("/ The India side", "Receiving and moving an inheritance.",
         table(["Asset", "What happens", "Moving it abroad"], [
             ["Bank deposits and FDs", "Transmitted to the heir; held in an NRO account", "USD 1 million per financial year with proof of inheritance, 15CA and 15CB"],
             ["Flat, house or commercial property", "NRIs and OCIs can inherit any immovable property, including agricultural land, from a person resident in India", "Sell (agricultural land can be sold only to a resident Indian citizen), proceeds into NRO, then within USD 1 million a year"],
             ["Shares and mutual funds", "Transmitted to the heir's NRO demat or folio", "Redeem into NRO, then within USD 1 million a year"],
             ["Gold or jewellery", "No tax on receipt", "Physical export is restricted; selling and remitting the proceeds follows the NRO route"]])
         + ul("Documents banks ask for: death certificate, will with probate or a succession certificate or legal heir certificate, the transmission letter, and a CA's Form 15CB.",
              "Indian tax arises only later: interest on inherited deposits, rent, and capital gains when you sell. For a later sale, your holding period and cost include the previous owner's.",
              "Need probate? In Mumbai, Chennai and Kolkata it is generally needed for wills covering property there; elsewhere banks and registrars may still ask for it.")
         + box("Inherited something in India?", "I inherited money or property in India and live abroad")),
        ("/ The country where you live", "Receiving it and what follows.",
         table(["Country", "Tax on receiving it", "Forms", "Later"], [
             ["United Kingdom", "None for the heir. UK inheritance tax is on the estate of the person who died; since 6 April 2025 foreign assets are in scope only if that person was a long-term UK resident (10 of the last 20 tax years). A parent who always lived in India is normally outside it.", "None for receiving it", "Interest, rent and gains are taxable in the UK; your cost for a later sale is the value at the date of death"],
             ["United States", "None", "Form 3520 if bequests from non-US persons exceed USD 100,000 in the year; FBAR and Form 8938 for inherited Indian accounts", "Stepped-up basis (value at death) for a later sale; inherited Indian mutual funds are usually PFICs"],
             ["Canada", "None", "T1135 if your Indian property and accounts (excluding personal-use property) cost more than CAD 100,000", "Income and later gains taxable; cost generally the value when you inherited"],
             ["Australia", "None", "Nothing on receipt", "Income and later gains taxable; the cost base depends on when the deceased acquired the asset, so document the value at death"]])
         + GUIDES),
        ("/ Step by step", "From the death certificate to your foreign bank.",
         ol("Get the death certificate and find the will, nominations and joint holdings.",
            "Get probate, a succession certificate or a legal heir certificate, depending on the asset and the city.",
            "Open an NRO account (and NRO demat if there are shares).",
            "Transmit deposits, shares and funds; mutate the property records.",
            "Sell what you do not want to keep (with a lower deduction certificate for property).",
            "Get Form 15CB, file Form 15CA and repatriate within USD 1 million per financial year.",
            "Report it where you live: Form 3520 in the US if over USD 100,000; T1135 in Canada if you keep assets above CAD 100,000.")
         + f'<p><strong>Sources:</strong> Income-tax Act, 2025 (inheritances not income); FEMA (Acquisition and Transfer of Immovable Property in India) Regulations and RBI Master Direction on remittance facilities for NRIs; HMRC IHTM47020 (long-term UK residence test); IRS Form 3520 instructions; CRA Form T1135; ATO guidance on inherited assets. <em>{UPDATED}</em> General information, not advice for your situation.</p>'),
    ],
    faqs=[("Is there inheritance tax in India?", "No. India has no inheritance or estate tax, and an inheritance is not taxable income for the heir. Income from it later (interest, rent, capital gains) is taxable."),
          ("Do I pay tax in the UK, US, Canada or Australia on money inherited from India?", "Not on receiving it. The US requires Form 3520 if inheritances from non-US persons exceed USD 100,000 in a year. UK inheritance tax applies to the deceased's estate and reaches foreign assets only if they were a long-term UK resident."),
          ("How much inherited money can I take out of India?", "Up to USD 1 million per financial year from your NRO account, with documents proving the inheritance, Form 15CA and a Chartered Accountant's Form 15CB."),
          ("Can an NRI inherit agricultural land in India?", "Yes, NRIs and OCIs can inherit any immovable property, including agricultural land, farmhouses and plantations. Agricultural land can only be sold to a resident Indian citizen."),
          ("Do I need to report inherited Indian bank accounts abroad?", "In the US, yes: FBAR above USD 10,000 combined and Form 8938 above its threshold. In Canada, T1135 if the total cost of foreign property exceeds CAD 100,000."),
          ("Can BQP handle the transmission and the transfer?", "Yes: transmission paperwork with your Indian lawyer, Indian returns, Form 15CB and repatriation. " + contact("UK, US, Canada or Australia"))],
    related=[("nri-inheritance-indian-property-tax-fema-2026.html", "NRI inheritance of Indian property"), (REPAT, "Repatriate money from India"),
             (PROP_SLUG + ".html", "Selling Indian property while living abroad"), (CHECKER, "Send-money checker")],
    cta_h="Bring an inheritance home without delays", cta_b=contact("UK, US, Canada or Australia"),
    keywords="inherit money from India living in UK, inheritance from India USA tax Form 3520, inheritance from India Canada tax, inheritance from India Australia tax, transfer inheritance from India to abroad, NRI inheritance repatriation USD 1 million, is there inheritance tax in India",
    desc="Inheriting from India while living in the UK, US, Canada or Australia: no inheritance tax in India, no tax on receipt abroad (US Form 3520 above USD 100,000), UK IHT after April 2025, and repatriating within USD 1 million a year with Form 15CA/15CB.",
    howto={"name": "How to bring an inheritance from India to the UK, US, Canada or Australia", "description": "Steps for an heir living abroad to receive Indian assets and repatriate them.", "steps": [
        {"name": "Collect documents", "text": "Death certificate, will, nominations and details of each asset."},
        {"name": "Get legal title", "text": "Probate, succession certificate or legal heir certificate as the asset and city require."},
        {"name": "Open NRO accounts", "text": "Open an NRO bank account and NRO demat if needed, and transmit the assets."},
        {"name": "Sell what you will not keep", "text": "Sell property or securities into the NRO account, with a lower deduction certificate for property."},
        {"name": "Repatriate", "text": "Get Form 15CB, file Form 15CA and remit within USD 1 million per financial year."},
        {"name": "Report abroad", "text": "File Form 3520 in the US if over USD 100,000; T1135 in Canada if you keep more than CAD 100,000 of Indian assets."}]}))

# ---------------------------------------------------------------- 3. Parents funding study abroad
EDU_SLUG = "parents-send-money-child-studying-abroad-uk-usa-canada-australia-lrs-tcs-2026"
PAGES.append(dict(
    slug=EDU_SLUG,
    title="Parents Sending Money to a Child Studying in the UK, USA, Canada or Australia (2026): LRS Limit, TCS and How to Pay Less Upfront",
    em="TCS of 2%, 20% or nil depending on how you send it.",
    kicker="/ Study abroad &middot; LRS and TCS &middot; Updated 2026-11-07",
    lead=("Each parent can send up to USD 250,000 a financial year under the Liberalised Remittance Scheme. Since 1 April 2026 the bank collects TCS of nil on education paid from a loan by a specified lender, 2% on self-funded education above INR 10 lakh a year, but 20% above INR 10 lakh if the same money is sent as a gift or maintenance. "
          "TCS is not a cost: the parent gets it back through their Indian return or against salary TDS. The purpose code your bank uses is what decides the rate, so send fees and living costs as education, with the admission letter and cost estimate."),
    sections=[
        ("/ The rates", "What TCS applies (FY 2026-27).",
         table(["How it is sent", "TCS", "Documents"], [
             ["Education, paid from an education loan by a specified financial institution", "Nil", "Loan sanction letter, admission letter"],
             ["Education, self-funded (fees and, as your bank allows, living costs for the course)", "2% of the amount above INR 10 lakh in the financial year", "Admission letter, fee invoice or cost-of-attendance letter, Form A2"],
             ["Gift or maintenance to the child", "20% of the amount above INR 10 lakh", "Form A2, PAN"],
             ["Medical treatment abroad", "2% above INR 10 lakh", "Hospital estimate"]])
         + "<p>The INR 10 lakh threshold is per person sending money, across all LRS purposes in the year. Each parent has their own threshold and own USD 250,000 limit, if each sends from their own money.</p>"
         + '<p>Try the numbers: <a href="lrs-tcs-calculator.html">LRS TCS calculator</a> &middot; <a href="nri-send-money-to-from-india-checker.html">send-money checker</a>.</p>'),
        ("/ Example", "INR 40 lakh for a year in the UK, US, Canada or Australia.",
         table(["Sent as", "One parent sends all", "Each parent sends INR 20 lakh"], [
             ["Education loan", "Nil", "Nil"],
             ["Self-funded education", "2% of 30 lakh = INR 60,000", "2% of 10 lakh each = INR 40,000 in total"],
             ["Gift or maintenance", "20% of 30 lakh = INR 6,00,000", "20% of 10 lakh each = INR 4,00,000 in total"]])
         + "<p>All of it is refundable or adjustable, but INR 6 lakh locked up until the refund hurts cash flow. Coding the transfer correctly matters more than anything else.</p>"
         + box("Paying fees abroad this term?", "my child is studying abroad and we are sending money from India")),
        ("/ The student's side", "Is it taxable for the child abroad?",
         table(["Country", "Money from parents", "Watch for"], [
             ["United Kingdom", "Not taxable; the UK has no gift tax", "Interest on UK savings is taxable above the allowances; part-time work income is taxed under PAYE"],
             ["United States", "Not taxable", "Students on F-1 or J-1 visas are usually non-resident aliens for their first five calendar years, so Form 3520 and FBAR generally do not apply then. Once a US resident for tax, gifts from parents above USD 100,000 a year need Form 3520"],
             ["Canada", "Not taxable", "International students who become Canadian residents for tax should still file, for benefits such as the GST/HST credit"],
             ["Australia", "Not taxable", "Keep the transfer records and a gift note: the ATO looks at large inflows described as gifts (TA 2021/2)"]])
         + GUIDES),
        ("/ Getting TCS back", "It is a prepaid tax, not a fee.",
         ul("The bank's TCS appears in the parent's Form 26AS / annual information statement.",
            "Claim it in the parent's Indian return for the year; any excess over their tax is refunded.",
            "Salaried parents can ask their employer to take TCS into account when deducting TDS from salary, so the money comes back month by month.",
            "If the child earns in India (for example rent from a flat in their name), keep their Indian return filed too.")
         + f'<p><strong>Sources:</strong> RBI Master Direction on the Liberalised Remittance Scheme; Income-tax Act, 2025 and Finance Act 2026 (TCS rates from 1 April 2026); IRS guidance on exempt individuals (students) and Form 3520; ATO Taxpayer Alert TA 2021/2. <em>{UPDATED}</em> General information, not advice for your situation.</p>'),
    ],
    faqs=[("How much money can parents send to a child studying abroad?", "Up to USD 250,000 per parent per financial year under the Liberalised Remittance Scheme, for fees, living costs or gifts."),
          ("What is the TCS on money sent abroad for education in 2026?", "From 1 April 2026: nil if paid from an education loan by a specified financial institution; 2% of the amount above INR 10 lakh a year if self-funded. Sent as a gift or maintenance instead, it is 20% above INR 10 lakh."),
          ("Is TCS refundable?", "Yes. It is credited to the parent and can be claimed in their Indian income tax return, or adjusted against salary TDS through their employer."),
          ("Can both parents send money to save TCS?", "Each parent has their own INR 10 lakh threshold and USD 250,000 limit, so two parents sending from their own funds each get the threshold. It must genuinely be each parent's own money."),
          ("Is money from parents in India taxable for a student in the UK, US, Canada or Australia?", "No, none of these countries taxes gifts received. A US student who has become a US tax resident must file Form 3520 if gifts from parents exceed USD 100,000 in a year."),
          ("Can BQP help with large remittances or TCS refunds?", "Yes: planning the purpose and timing, Form 15CB where needed, and the parent's return to recover TCS. " + contact("India, with a child abroad"))],
    related=[("lrs-tcs-calculator.html", "LRS TCS calculator"), (CHECKER, "Send-money checker"),
             ("nri-gift-indian-relatives-section-56-fema-2026.html", "Gifts between NRIs and relatives")],
    cta_h="Sending fees abroad?", cta_b=contact("India, with a child abroad"),
    keywords="TCS on education remittance 2026, parents send money to child studying abroad, LRS limit for education, TCS 2% education above 10 lakh, send money to son in UK from India, send money to daughter in USA tuition TCS, student Canada money from parents tax, TCS refund LRS",
    desc="Parents in India paying for a child studying in the UK, US, Canada or Australia: USD 250,000 LRS limit per parent, TCS from 1 April 2026 (nil loan-funded, 2% self-funded education, 20% gifts above INR 10 lakh), worked example, refunds, and the student's tax position.",
    howto=None))

# ---------------------------------------------------------------- 4. FAQ hub (AEO)
FAQ_GROUPS = [
    ("Taking money out of India", [
        ("How much money can an NRI transfer from India abroad in a year?", "NRE and FCNR balances can be sent freely with no limit. NRO balances (rent, dividends, pension, old savings) and property sale proceeds can be sent up to USD 1 million per financial year (April to March), with Form 15CA and a Chartered Accountant's Form 15CB."),
        ("Can I move money from my NRO account to my NRE account?", "Yes. It counts as repatriation within the USD 1 million limit and needs the same Form 15CA and 15CB paperwork. Once in NRE it is freely repatriable."),
        ("What are Form 15CA and Form 15CB?", "Form 15CB is a Chartered Accountant's certificate on the nature of the payment and the tax position; Form 15CA is the remitter's online declaration based on it. Under the Income-tax Act, 2025 they are Form 146 and Form 145 from 1 April 2026."),
        ("How long does a Form 15CB take?", "Usually within 24 hours once the CA has the documents: source of money, tax paid, PAN and bank details. The bank then remits, often the same or next working day."),
        ("Can I do the repatriation from abroad without travelling to India?", "Yes. Form 15CB is signed digitally, Form 15CA is filed online and most banks accept the remittance request by secure message or email."),
        ("Can I send money from India to buy a house abroad?", "An NRI can use NRE funds freely or NRO funds within USD 1 million a year. A resident in India can buy property abroad under LRS within USD 250,000 a year, with TCS of 20% above INR 10 lakh."),
    ]),
    ("Sending money to India", [
        ("Is money I send to my parents in India taxable?", "No. Gifts from a relative are not taxable for the receiver in India, whatever the amount, and India does not tax the transfer itself. Keep the bank's inward remittance advice."),
        ("Is a gift to a friend in India taxable?", "For the friend, yes, once gifts from non-relatives exceed INR 50,000 in the financial year; then the whole amount is taxable as their income."),
        ("Is there a US tax on sending money to India?", "Only the 1% federal remittance excise tax from 1 January 2026, and only on transfers paid in cash, money order or cashier's cheque. Transfers from a US bank account or card are not covered."),
        ("Should I send money to my NRE or NRO account?", "Money earned abroad usually goes to NRE: interest is tax-free in India and it stays freely repatriable. NRO is for Indian income; its interest is taxable in India."),
    ]),
    ("Parents sending money abroad", [
        ("How much can my parents send me abroad?", "Up to USD 250,000 per parent per financial year under the Liberalised Remittance Scheme."),
        ("What TCS applies when parents send money abroad?", "From 1 April 2026: 20% of the amount above INR 10 lakh a year for gifts or maintenance; 2% above INR 10 lakh for self-funded education or medical treatment; nil for education paid from a loan by a specified lender; a flat 2% on overseas tour packages."),
        ("Is TCS refundable?", "Yes. It is a prepaid tax credited to the parent, claimed in their Indian return or adjusted against salary TDS."),
    ]),
    ("Where you live", [
        ("Is NRE interest taxable in the UK, US, Canada or Australia?", "Yes, for residents of those countries. It is tax-free only in India. Declare it on your return there."),
        ("Do I need to report my Indian bank accounts to the IRS?", "Yes, if you are a US person: FBAR if your foreign accounts together exceeded USD 10,000 at any time in the year, and Form 8938 above USD 50,000 at year-end or USD 75,000 at any time (single, living in the US)."),
        ("Do I need Form 3520 for money from my parents in India?", "If you are a US person and gifts or bequests from non-US persons exceed USD 100,000 in the year. It is a report, not a tax, but the late-filing penalty is steep."),
        ("Has the UK remittance basis ended?", "Yes, from 6 April 2025. UK residents are taxed on worldwide income and gains, with four years of relief for new arrivals who were non-resident for the previous 10 tax years. Former non-doms can bring older foreign income and gains in at 12% in 2025-26 and 2026-27 (15% in 2027-28) under the Temporary Repatriation Facility."),
        ("Do I need Form T1135 in Canada for my Indian accounts?", "Yes, if the total cost of your foreign property (Indian deposits, shares, funds, rented property; not personal-use property) exceeded CAD 100,000 at any time in the year."),
        ("Is money from my parents in India taxable in Australia?", "No, Australia has no gift tax. Keep proof that it is a genuine gift (bank records and a gift note), because the ATO looks at offshore money described as gifts or loans (TA 2021/2)."),
        ("Do I need to report Indian accounts in Germany, the Netherlands or Ireland?", "Residents are taxed on worldwide income, so Indian interest and gains go on your return there with a credit for Indian tax. Indian banks share account data with European tax authorities under the Common Reporting Standard."),
    ]),
    ("Property and inheritance", [
        ("Why is TDS deducted on the full price when an NRI sells property?", "Without a lower deduction certificate the buyer deducts tax on the whole sale price. Apply on Form 128 (formerly Form 13) before signing, so TDS matches the real tax on the gain."),
        ("Do I pay tax twice when I sell Indian property while living abroad?", "Both countries usually tax the gain, but the Indian tax is credited against the foreign tax under the treaty, so you pay roughly the higher of the two."),
        ("Is there inheritance tax in India?", "No. India has no inheritance or estate tax, and an inheritance is not income for the heir. The money can be repatriated within USD 1 million a year with proof of inheritance and Form 15CA/15CB."),
        ("Can an NRI inherit agricultural land?", "Yes, by inheritance NRIs and OCIs can hold any Indian property, including agricultural land; it can only be sold to a resident Indian citizen."),
    ]),
    ("Returning to India and FAST-DS", [
        ("What happens to my NRE account when I move back to India?", "Once you become resident, NRE and NRO accounts must be redesignated as resident accounts; foreign currency can be held in an RFC (resident foreign currency) account."),
        ("Do I have to declare my UK pension, ISA, 401(k), RRSP or super in India?", "Yes, in Schedule FA of your Indian return from your first year as resident and ordinarily resident. RNOR years generally need no Schedule FA."),
        ("What is FAST-DS 2026?", "A one-time scheme for foreign assets missing from Schedule FA. Assets built from income earned while non-resident usually fall in Category 2: a flat INR 1 lakh fee for a value up to INR 5 crore. Undisclosed foreign income is Category 1 at 60%."),
        ("What is the FAST-DS deadline?", "Declarations close on 31 December 2026."),
    ]),
]
FAQ_ALL = [qa for _, items in FAQ_GROUPS for qa in items]
FAQ_HTML = "".join(f'<h3 style="margin:22px 0 8px">{g}</h3>' + "".join(f"<p><strong>{q}</strong><br>{a}</p>" for q, a in items) for g, items in FAQ_GROUPS)
PAGES.append(dict(
    slug="nri-money-transfer-questions-answered-uk-usa-canada-australia-2026",
    title=f"{len(FAQ_ALL)} Questions Indians in the UK, USA, Canada and Australia Ask About Moving Money To and From India (2026)",
    em="short answers from a Chartered Accountant.",
    kicker="/ FAQ &middot; Money to and from India &middot; Updated 2026-11-07",
    lead=("The questions people actually ask about NRE and NRO accounts, repatriation limits, Form 15CA/15CB, TCS when parents send money, the 1% US remittance tax, Form 3520 and FBAR, the UK FIG regime, Canada's T1135, Australian gifts, property sales, inheritance and FAST-DS, answered in two or three sentences each. "
          "Rules as at November 2026."),
    sections=[("/ Quick numbers", "The figures behind most answers.",
               table(["Rule", "Figure"], [["NRO repatriation (NRIs)", "USD 1 million per financial year"], ["LRS (residents)", "USD 250,000 per person per financial year"],
                                          ["TCS on LRS above INR 10 lakh", "20% general; 2% education/medical; nil loan-funded education"], ["Gifts from non-relatives", "Taxable above INR 50,000 a year"],
                                          ["NRI long-term gain on property", "12.5% without indexation"], ["US remittance tax", "1% on cash-funded transfers"], ["US Form 3520", "Above USD 100,000"],
                                          ["FBAR", "Above USD 10,000"], ["Canada T1135", "Above CAD 100,000"], ["FAST-DS deadline", "31 December 2026"]])),
              ("/ All questions", "Grouped by topic.", FAQ_HTML + box("Your question is not here?", "I have a question about moving money between India and abroad")),
              ("/ Go deeper", "Guides and tools.",
               ul(f'<a href="{CHECKER}">Send-money checker</a> (your exact transfer)', f'<a href="{REPAT}">Repatriation step by step</a>',
                  f'<a href="{PROP_SLUG}.html">Selling Indian property while living abroad</a>', f'<a href="{INH_SLUG}.html">Inheriting from India</a>',
                  f'<a href="{EDU_SLUG}.html">Parents paying for study abroad</a>', '<a href="fast-ds-uk-pension-isa-canada-rrsp-australia-super-schedule-fa.html">FAST-DS for foreign pensions</a>')
               + GUIDES + f"<p><em>{UPDATED}</em> General information, not advice for your situation.</p>")],
    faqs=FAQ_ALL,
    related=[(CHECKER, "Send-money checker"), (REPAT, "Repatriate money from India"), (PROP_SLUG + ".html", "Selling property while living abroad")],
    cta_h="Ask a Chartered Accountant", cta_b=contact("your country"),
    keywords="NRI money transfer FAQ, how much money can NRI transfer from India, NRO to NRE transfer, Form 15CA 15CB FAQ, TCS when parents send money abroad, NRE interest taxable UK USA Canada Australia, Form 3520 parents India, T1135 India accounts, is there inheritance tax in India, FAST-DS deadline",
    desc=f"{len(FAQ_ALL)} short answers for Indians in the UK, US, Canada and Australia: NRO repatriation (USD 1 million), Form 15CA/15CB, LRS and TCS, US 1% remittance tax, Form 3520, FBAR, UK FIG, T1135, property sales, inheritance and FAST-DS.",
    howto=None))

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"],
                hero_kicker=p["kicker"], hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>',
                hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]],
                cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print(f"Batch BB complete: {len(PAGES)} pages, FAQ hub {len(FAQ_ALL)} questions")
