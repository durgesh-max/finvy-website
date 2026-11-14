# -*- coding: utf-8 -*-
"""Batch CE (14 Nov 2026): four pages from Google autocomplete demand seen in all seven markets (US, UK, UAE, Canada,
Australia, Singapore, India) that the site did not answer: India-Canada DTAA, India-Australia DTAA, setting up a UAE /
Dubai company from India, and the Indian tax residency certificate (Form 42/43, formerly 10FA/10FB).
Facts used (Income Tax Department withholding-rate chart; secondary summaries checked 14 Nov 2026):
- India-Canada: dividends 15% (company holding at least 10%) / 25% otherwise; interest 15%; royalties and fees for
  included services 10% to 15% depending on type; each country may tax capital gains under its domestic law.
- India-Australia: dividends 15%; interest 15%; royalties 10% / 15%; no separate article for fees for technical services.
- Treaty rate applies only where lower than the Income-tax Act rate (e.g. 20% on dividends to non-residents); claim
  needs a TRC and Form 10F (Form 41 under the Income-tax Rules, 2026); residence country gives credit.
- UAE company from India: resident individual's ODI within LRS USD 250,000 per financial year, only in an operating
  foreign entity with bona fide business, not financial services, no subsidiary where the individual has control
  (Schedule III); Indian company up to 400% of net worth (Schedule I); Form ODI through the AD bank, UIN, annual
  performance report by 31 December, Schedule FA. POEM: a foreign company managed in India is Indian-resident.
  UAE corporate tax 9% above AED 375,000 (0% below); small business relief for revenue up to AED 3 million for tax
  periods ending on or before 31 December 2026; registration mandatory.
- TRC for Indian residents: apply in Form 42 (formerly 10FA) on the e-filing portal; certificate in Form 43 (formerly
  10FB); section 159 of the Income-tax Act, 2025 and rule 75 (formerly rule 21AB). YouTube/AdSense: Google withholds US
  tax on US-viewer earnings; an Indian creator claims the India-US treaty royalty rate on Form W-8BEN with PAN."""
from urllib.parse import quote
from build_lib import page, write_page

UPDATED = "Last updated: 14 November 2026."
DATE = "2026-11-14"


def wa(t):
    return "https://wa.me/917801887130?text=" + quote(t)


def ul(*x):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in x) + "</ul>"


def table(head, rows):
    return ("<table><thead><tr>" + "".join(f"<th>{h}</th>" for h in head) + "</tr></thead><tbody>"
            + "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows) + "</tbody></table>")


def box(title, body, msg):
    return (f'<div style="border:1px solid var(--line);border-left:4px solid #C2312A;border-radius:10px;padding:16px 18px;margin:18px 0;background:var(--bg-soft)">'
            f'<p style="margin:0 0 8px;font-weight:600">{title}</p><p style="margin:0">{body} '
            f'<a href="{wa(msg)}" target="_blank" rel="noopener"><strong>WhatsApp CA Durgesh Chavda</strong></a>.</p></div>')


def src(text):
    return f'<p><strong>Sources:</strong> {text} <em>{UPDATED}</em> General information, not advice for your situation.</p>'


C_NRI = ("WhatsApp +91 78018 87130 or email durgesh@bharatquantumprospera.com with your country of residence, the Indian income (interest, rent, dividends, capital gains) and the years involved. "
         "We reply the same working day with the treaty position and a fixed-scope quote.")
C_UAE = ("WhatsApp +91 78018 87130 or email durgesh@bharatquantumprospera.com with who will own the UAE company (you, family or your Indian company), the business, and where it will be managed from. "
         "We reply the same working day with the FEMA route, the tax position on both sides and a fixed-scope quote.")
C_TRC = ("WhatsApp +91 78018 87130 or email durgesh@bharatquantumprospera.com with the country asking for the certificate, the year and the type of income. "
         "We reply the same working day and can file Form 42 for you.")


def treaty_page(country, slug, rows, country_notes, cg_text, faqs_extra, demonym, credit_name, related_send):
    return dict(
        slug=slug,
        title=f"India-{country} Tax Treaty (DTAA) for NRIs in {country} (2026): Rates on Interest, Dividends, Rent and Capital Gains, and How to Claim",
        em=f"what India deducts and what {country} credits.",
        kicker=f"/ NRI &middot; {country} &middot; DTAA &middot; Updated {DATE}",
        lead=(f"Under the India-{country} tax treaty, India can tax Indian income of a {demonym} resident, but the treaty caps the rate on some income: "
              f"<strong>{rows[0][1]} on dividends</strong> and <strong>15% on interest</strong>, with royalties at {rows[2][1]}. "
              f"The treaty rate applies only when it is lower than the Indian rate, and only if you give the payer a <strong>tax residency certificate from {country}</strong> and <strong>Form 10F (now Form 41)</strong>. "
              f"Rent from Indian property and capital gains on Indian property and shares remain taxable in India; {country} then taxes the same income as part of your worldwide income and gives a <strong>{credit_name}</strong> for the Indian tax."),
        sections=[
            ("/ Treaty rates vs Indian rates", "Use the lower one.",
             table(["Income from India", f"India-{country} treaty cap", "Indian rate for non-residents (before surcharge and cess)"], rows)
             + "<p>The Indian rate applies if it is lower than the treaty cap. Interest on NRE accounts and FCNR deposits is tax-free in India for NRIs, so the treaty matters mainly for NRO interest, dividends, rent and gains.</p>"
             + box("Your bank will deduct 30% on NRO interest unless you act.", f"Give the bank your {country} tax residency certificate, Form 10F (Form 41) and PAN before the interest is credited to get the 15% treaty rate.",
                   f"Hi Durgesh, I live in {country} and my Indian bank deducts 30% TDS on NRO interest. Can you help me claim the treaty rate?")),
            ("/ Capital gains and property", "India keeps the right to tax.",
             cg_text + ul("Rent from Indian property is taxed in India (tenant deducts about 31.2% TDS); see <a href=\"nri-rental-income-india-tenant-tds-31-2-percent-tan-form-144-2026.html\">NRI rental income</a>.",
                          "Selling Indian property: long-term gains at 12.5% for NRIs, with the buyer deducting TDS unless you obtain a lower deduction certificate; see the <a href=\"nri-property-tds-ldc-calculator.html\">NRI property TDS calculator</a>.")),
            ("/ How to claim and avoid paying twice", "Step by step.",
             ul(f"Get a tax residency certificate from the {country} tax authority for the relevant year.",
                "Fill Form 10F (Form 41 under the Income-tax Rules, 2026) on the Indian e-filing portal; you need a PAN.",
                "Give both to your Indian bank, tenant, company or buyer before payment, or claim the lower rate and refund in your Indian return.",
                f"Report the income in {country} and claim the {credit_name} for Indian tax actually paid, within the treaty cap.",
                *country_notes)
             + f'<p>Related: <a href="what-is-dtaa.html">what a DTAA is</a> &middot; <a href="nri-dtaa-claim-practical-trc-form-10f.html">claiming DTAA with TRC and Form 10F</a> &middot; <a href="{related_send}">sending money between India and {country}</a> &middot; <a href="sell-property-in-india-living-in-uk-usa-canada-australia-tax-both-countries-2026.html">selling Indian property while living abroad</a>.</p>'
             + src(f"India-{country} Double Taxation Avoidance Agreement; Income Tax Department chart of withholding rates under the Act and tax treaties; Income-tax Act, 2025 and Income-tax Rules, 2026 (Form 41). Rates are caps on Indian tax; confirm the article for your income type.")),
        ],
        faqs=[(f"What is the India-{country} DTAA rate on dividends?", f"{rows[0][1]} under the treaty. Indian domestic tax on dividends to non-residents is 20% plus surcharge and cess, so the lower of the two applies."),
              (f"What TDS applies on NRO interest for an NRI in {country}?", "The bank deducts 30% plus surcharge and cess by default. With a tax residency certificate, Form 10F (Form 41) and PAN, the treaty rate of 15% applies."),
              (f"Is NRE interest taxable for an NRI living in {country}?", f"NRE and FCNR interest is exempt in India for NRIs, but {country} taxes its residents on worldwide income, so it is usually reportable there."),
              (f"How do I avoid double tax on Indian income in {country}?", f"Pay Indian tax at the lower of the treaty and Indian rate, then claim a {credit_name} in {country} for the Indian tax."),
              *faqs_extra,
              ("Can BQP handle the Indian side?", "Yes. " + C_NRI)],
        related=[("nri-dtaa-claim-practical-trc-form-10f.html", "Claim DTAA: TRC and Form 10F"), (related_send, f"Money between India and {country}"),
                 ("what-is-dtaa.html", "What is a DTAA")],
        cta_h=f"NRI in {country} with income in India?", cta_b=C_NRI,
        keywords=f"India {country} DTAA, DTAA India and {country}, India {country} tax treaty rates, India {country} tax treaty capital gains, NRI {country} NRO interest TDS treaty, India {country} double tax avoidance agreement dividend interest, {demonym} resident Indian income tax",
        desc=f"India-{country} DTAA for NRIs in 2026: treaty caps on dividends ({rows[0][1]}), interest (15%) and royalties, Indian vs treaty rates, capital gains and rent, TRC and Form 10F (Form 41), and claiming the {credit_name}.",
        howto={"name": f"How an NRI in {country} claims the India-{country} treaty rate", "description": "Steps to cut Indian TDS and avoid double tax.", "steps": [
            {"name": "Get a tax residency certificate", "text": f"Obtain a TRC from the {country} tax authority for the year."},
            {"name": "File Form 10F (Form 41)", "text": "Submit it on the Indian e-filing portal with your PAN."},
            {"name": "Give documents to the payer", "text": "Your bank, tenant or company deducts at the treaty rate; otherwise claim a refund in your Indian return."},
            {"name": "Claim credit abroad", "text": f"Report the income in {country} and claim the {credit_name} for Indian tax paid."}]})


CANADA = treaty_page(
    "Canada", "india-canada-dtaa-tax-treaty-nri-rates-capital-gains-foreign-tax-credit-2026",
    [["Dividends", "15% (company holding at least 10%) / 25% (others)", "20%"],
     ["Interest (NRO deposits, loans)", "15%", "30% on NRO interest; 20% on some foreign-currency loans"],
     ["Royalties and fees for included services", "10% to 15%, depending on the type", "20%"],
     ["Rent from Indian property", "Taxable in India (no cap)", "Slab rates; tenant TDS about 31.2%"]],
    ["Canada's foreign tax credit is claimed on the T1 return; Indian property and accounts may also need form T1135 if the cost of specified foreign property exceeds CAD 100,000."],
    "<p>The India-Canada treaty lets each country tax capital gains under its own domestic law, so India taxes gains on Indian property and Indian shares, and Canada taxes the same gain as a Canadian resident's worldwide income with credit for the Indian tax.</p>",
    [("Does India tax capital gains of a Canadian resident?", "Yes. Under the India-Canada treaty each country may tax capital gains under its domestic law, so gains on Indian property and shares are taxed in India, and Canada gives a foreign tax credit."),
     ("For an individual shareholder, which dividend rate applies?", "The treaty cap for non-corporate shareholders is 25%, which is higher than the Indian 20% rate, so the Indian rate (plus surcharge and cess) applies.")],
    "Canadian", "foreign tax credit", "send-money-canada-to-india-india-to-canada-nri-tax-2026.html")

AUSTRALIA = treaty_page(
    "Australia", "india-australia-dtaa-tax-treaty-nri-rates-capital-gains-fito-2026",
    [["Dividends", "15%", "20%"],
     ["Interest (NRO deposits, loans)", "15%", "30% on NRO interest; 20% on some foreign-currency loans"],
     ["Royalties", "10% / 15%", "20%"],
     ["Rent from Indian property", "Taxable in India (no cap)", "Slab rates; tenant TDS about 31.2%"]],
    ["The treaty has no separate article for fees for technical services, so the treatment depends on how the payment is characterised; get this checked before invoicing.",
     "Australia's foreign income tax offset (FITO) is claimed in the Australian return for Indian tax paid."],
    "<p>India taxes gains on Indian property and on shares of Indian companies under its domestic law; Australia taxes its residents on worldwide gains and allows a foreign income tax offset for the Indian tax. Check the treaty's capital gains article for the type of asset you are selling.</p>",
    [("Does the India-Australia treaty cover fees for technical services?", "There is no separate article for fees for technical services, so the treatment depends on whether the payment is royalty or business income; check before invoicing."),
     ("What is the India-Australia DTAA rate on interest?", "15%. Without the treaty documents, Indian banks deduct 30% plus surcharge and cess on NRO interest.")],
    "Australian", "foreign income tax offset", "send-money-australia-to-india-india-to-australia-nri-tax-2026.html")

UAE = dict(
    slug="set-up-company-in-dubai-uae-from-india-odi-lrs-poem-corporate-tax-2026",
    title="Setting Up a Company in Dubai or the UAE From India (2026): FEMA ODI Route, LRS Limit, POEM Risk and UAE Corporate Tax",
    em="legal on both sides, if you do it in the right order.",
    kicker=f"/ Indians going global &middot; UAE &middot; FEMA ODI &middot; Updated {DATE}",
    lead=("An Indian resident can own a Dubai or UAE company, but it is <strong>overseas direct investment (ODI)</strong> under FEMA, not a simple LRS remittance: "
          "an individual can invest within the <strong>LRS limit of USD 250,000 a financial year</strong>, only in an <strong>operating company with a genuine business</strong> (not financial services) and not one that has its own subsidiary where the individual has control; "
          "an Indian company can invest up to <strong>400% of its net worth</strong>. The investment is reported through your bank (Form ODI and a UIN), with an <strong>annual performance report by 31 December</strong>. "
          "If the company is run from India, it can be treated as <strong>Indian-resident (POEM)</strong> and taxed in India on its global profit. In the UAE, corporate tax is <strong>0% up to AED 375,000 of profit and 9% above</strong>, and registration is compulsory."),
    sections=[
        ("/ Who invests, and the route", "Individual or Indian company.",
         table(["Investor", "FEMA route", "Main limits"], [
             ["Resident individual", "ODI under Schedule III of the Overseas Investment Rules, 2022, within LRS", "USD 250,000 per person per financial year; operating company only; no financial services; no subsidiary or step-down subsidiary where the individual has control"],
             ["Indian company or LLP", "ODI under Schedule I", "Total financial commitment up to 400% of net worth; round-tripping limit of two layers"],
             ["Family members", "Each resident individual has a separate LRS limit", "Each must meet the same conditions"]])
         + box("Paid for the UAE licence from your own account without telling the bank it was ODI?", "That is a reporting gap that is fixable, through late submission fees or compounding, which since 23 October 2026 is handled by RBI Regional Offices.",
               "Hi Durgesh, I set up a company in Dubai from India. Can you check whether my FEMA ODI filings are in order?")),
        ("/ The order of steps", "Do FEMA first, then remit.",
         ul("Choose the jurisdiction (mainland or free zone) and confirm the activity is a bona fide business.",
            "Open the ODI file with your authorised dealer bank: Form ODI, valuation where needed and declarations; the bank reports it and a UIN is allotted.",
            "Remit the capital through the bank under the ODI route, then incorporate and obtain the UAE licence.",
            "Within the prescribed time, submit evidence of investment (share certificate) to the bank.",
            "Every year: the annual performance report by 31 December, the foreign shares in Schedule FA of your Indian return, and UAE corporate tax registration and filing.")
         + '<p>Related: <a href="fema-compounding-odi-rbi-regional-office-uin-circular-28-october-2026.html">FEMA compounding for ODI from 23 October 2026</a> &middot; <a href="form-odi-apr-annual-performance-report-india-2026.html">ODI annual performance report</a> &middot; <a href="uae-corporate-tax-deadline-30-october-2026-top-up-tax-registration-30-november.html">UAE corporate tax deadlines</a> &middot; <a href="india-uae-tax-treaty-dtaa.html">India-UAE tax treaty</a>.</p>'),
        ("/ Tax on both sides", "Where the profit is taxed.",
         table(["Point", "Position"], [
             ["UAE corporate tax", "0% on taxable profit up to AED 375,000, 9% above; qualifying free zone income can be 0%; registration compulsory even with no tax"],
             ["UAE small business relief", "Revenue up to AED 3 million can elect relief for tax periods ending on or before 31 December 2026"],
             ["Place of effective management (POEM)", "If key management and commercial decisions are in substance made in India, the company is Indian-resident and taxed in India on its global income"],
             ["Dividends to you in India", "Taxable in India at your slab rate while you are resident; the India-UAE treaty and Indian rules decide credit"],
             ["Moving to the UAE yourself", "Your own residence changes the picture; see <a href=\"dubai-uae-nri-indian-income-above-15-lakh-deemed-resident-india-tax-2026.html\">deemed residence for UAE-based Indians</a>"]])
         + src("Foreign Exchange Management (Overseas Investment) Rules, 2022 (Schedules I and III) and Regulations, 2022; RBI Overseas Investment Directions; Liberalised Remittance Scheme; Income-tax Act, 2025, section 6 (place of effective management); UAE Federal Decree-Law No. 47 of 2022 on corporate tax. Secondary summaries checked 14 November 2026: TaxGuru, VJM Global.")),
    ],
    faqs=[("Can an Indian resident open a company in Dubai?", "Yes, as overseas direct investment under FEMA: within the LRS limit of USD 250,000 per financial year, in an operating company with a genuine business, reported through your bank with Form ODI."),
          ("Is setting up a Dubai company ODI or LRS?", "ODI. LRS is the remittance limit that an individual's ODI must fit within; the investment itself must follow the Overseas Investment Rules and be reported."),
          ("Can my Indian company own a UAE subsidiary?", "Yes, under Schedule I of the Overseas Investment Rules, with total financial commitment up to 400% of net worth and within the two-layer limit."),
          ("Will the UAE company be taxed in India?", "Only if its place of effective management is in India, meaning the key decisions are in substance made from India. Then it is Indian-resident and taxed in India on its global income."),
          ("What is UAE corporate tax for a small company?", "0% on taxable profit up to AED 375,000 and 9% above. Businesses with revenue up to AED 3 million can elect small business relief for tax periods ending on or before 31 December 2026."),
          ("What yearly filings does the Indian owner have?", "The ODI annual performance report by 31 December, Schedule FA in the Indian return, and UAE corporate tax registration and returns."),
          ("Can BQP handle the FEMA side?", "Yes. " + C_UAE)],
    related=[("fema-odi-us-entity-indian-founder.html", "FEMA ODI for Indian founders"), ("india-uae-tax-treaty-dtaa.html", "India-UAE tax treaty"),
             ("fema-compounding-odi-rbi-regional-office-uin-circular-28-october-2026.html", "FEMA compounding for ODI")],
    cta_h="Starting a UAE company from India?", cta_b=C_UAE,
    keywords="register company in Dubai from India, set up company in UAE from India, Indian resident Dubai company FEMA, ODI Dubai company LRS 250000, POEM UAE company Indian owner, UAE corporate tax 9% Indian owner, Indian company UAE subsidiary 400% net worth, Dubai free zone company Indian resident",
    desc="How an Indian resident or company sets up a Dubai/UAE company in 2026: FEMA ODI route (LRS USD 250,000, operating company, Schedule III conditions; Indian company up to 400% of net worth), Form ODI, UIN, APR by 31 December, POEM risk, UAE corporate tax 0%/9% and small business relief.",
    howto={"name": "How to set up a UAE company from India under FEMA", "description": "Steps for Indian residents and companies.", "steps": [
        {"name": "Check eligibility", "text": "Operating business, not financial services, within LRS (individual) or 400% of net worth (company)."},
        {"name": "File ODI with the bank", "text": "Submit Form ODI and documents; the bank reports and a UIN is allotted."},
        {"name": "Remit and incorporate", "text": "Send the capital under the ODI route, incorporate and obtain the UAE licence, then submit share evidence."},
        {"name": "Keep it compliant", "text": "Annual performance report by 31 December, Schedule FA, UAE corporate tax registration, and manage the company from outside India to avoid POEM."}]})

TRC = dict(
    slug="tax-residency-certificate-india-form-42-43-10fa-10fb-freelancer-youtube-2026",
    title="Tax Residency Certificate From India (2026): Form 42 and Form 43 (Formerly 10FA and 10FB), Who Needs One, and YouTube and Freelancer Income",
    em="apply online, get the certificate the foreign payer asks for.",
    kicker=f"/ Indian residents &middot; Foreign income &middot; DTAA &middot; Updated {DATE}",
    lead=("An Indian resident gets an Indian <strong>tax residency certificate (TRC)</strong> by filing <strong>Form 42</strong> (formerly Form 10FA) online on the income tax e-filing portal; the department issues the certificate in <strong>Form 43</strong> (formerly Form 10FB). "
          "The forms were renumbered when the Income-tax Rules, 2026 replaced the 1962 Rules on 1 April 2026 (rule 75, formerly rule 21AB; section 159 of the Income-tax Act, 2025). "
          "You need it when a foreign client, platform or tax authority asks for proof of Indian residence before applying a lower treaty withholding rate. "
          "For YouTube and AdSense income, Google usually asks for <strong>Form W-8BEN with your PAN</strong> to apply the India-US treaty rate, rather than a TRC."),
    sections=[
        ("/ Old and new form numbers", "Same certificate, new names.",
         table(["Purpose", "Until 31 March 2026", "From 1 April 2026"], [
             ["Application by a resident for a TRC", "Form 10FA (rule 21AB)", "Form 42 (rule 75)"],
             ["Certificate issued by the department", "Form 10FB", "Form 43"],
             ["Non-resident's self-declaration to an Indian payer", "Form 10F", "Form 41"]])
         + '<p>Full mapping: <a href="old-vs-new-income-tax-form-numbers-2026-15ca-145-15cb-146-10f-41.html">old vs new income tax form numbers</a>.</p>'),
        ("/ Who needs an Indian TRC", "Typical cases.",
         table(["You are", "Why the TRC is asked for"], [
             ["Freelancer or consultant with foreign clients", "Clients in countries that withhold tax on service or royalty payments apply the treaty rate only with a TRC"],
             ["Indian company exporting services or licensing software", "Foreign customers deduct tax unless the Indian company proves residence for the treaty"],
             ["Investor receiving foreign dividends or interest", "Foreign banks and brokers apply treaty rates on proof of residence"],
             ["Creator earning from YouTube or other US platforms", "Google applies US withholding on US-viewer earnings; the India-US treaty rate is claimed on Form W-8BEN with PAN, and a TRC is needed only if a platform specifically asks"],
             ["Indian resident claiming treaty relief abroad", "A foreign tax authority may ask for it with a refund claim"]])
         + box("Losing money to foreign withholding?", "A TRC filed before the client's payment often reduces the deduction to the treaty rate, and the tax actually withheld abroad can be credited in your Indian return using the foreign tax credit form.",
               "Hi Durgesh, my foreign client is deducting tax from my payments. Can you help me get an Indian tax residency certificate?")),
        ("/ How to apply", "On the e-filing portal.",
         ul("Log in to the income tax e-filing portal with your PAN and select Form 42.",
            "Enter the country for which the certificate is needed, the period, your residential status, and the nature of income or purpose.",
            "Attach supporting documents (for example, proof of address and, for companies, incorporation details) and verify the form.",
            "The tax officer examines the application and issues the certificate in Form 43; keep a copy for each year and each country that needs it.",
            "Claim credit in India for any foreign tax withheld, using the foreign tax credit form with your return.")
         + '<p>Related: <a href="best-ca-form-10f-electronic-trc-dtaa-india.html">TRC and Form 10F for treaty claims</a> &middot; <a href="what-is-dtaa.html">what a DTAA is</a> &middot; <a href="india-us-tax-treaty-dtaa.html">India-US tax treaty</a>.</p>'
         + src("Income-tax Act, 2025, section 159; Income-tax Rules, 2026, rule 75 and Forms 41, 42 and 43 (formerly rule 21AB and Forms 10F, 10FA and 10FB); Income Tax Department FAQs and guidance notes on forms under the 2026 Rules; Google AdSense and YouTube tax information (Form W-8BEN).")),
    ],
    faqs=[("How do I get a tax residency certificate in India?", "File Form 42 (formerly Form 10FA) online on the income tax e-filing portal. The department issues the TRC in Form 43 (formerly Form 10FB)."),
          ("What are Form 10FA and Form 10FB called now?", "From 1 April 2026, under the Income-tax Rules, 2026, Form 10FA is Form 42 (the application) and Form 10FB is Form 43 (the certificate)."),
          ("Do I need a TRC for YouTube earnings?", "Usually not. Google applies US withholding on US-viewer earnings and lets Indian creators claim the India-US treaty rate by submitting Form W-8BEN with their PAN. A TRC is needed only if a platform or client specifically asks."),
          ("Who can apply for an Indian TRC?", "A person resident in India for the year, such as an individual, firm or company, who needs to prove Indian residence to claim treaty benefits abroad."),
          ("Is Form 10F the same as a TRC?", "No. Form 10F (now Form 41) is a self-declaration that a non-resident gives to an Indian payer along with a TRC from their own country. Form 43 is the TRC India issues to its residents."),
          ("Can BQP file Form 42 for me?", "Yes. " + C_TRC)],
    related=[("best-ca-form-10f-electronic-trc-dtaa-india.html", "TRC and Form 10F"), ("old-vs-new-income-tax-form-numbers-2026-15ca-145-15cb-146-10f-41.html", "Old vs new form numbers"),
             ("india-us-tax-treaty-dtaa.html", "India-US tax treaty")],
    cta_h="A foreign client asking for your TRC?", cta_b=C_TRC,
    keywords="tax residency certificate India apply online, Form 10FA, Form 10FB, Form 42 Form 43 TRC, tax residency certificate India for YouTube channel, TRC India freelancer, how to get TRC in India, tax residency certificate India format, rule 75 TRC",
    desc="How an Indian resident gets a tax residency certificate in 2026: Form 42 application and Form 43 certificate (formerly 10FA and 10FB) under rule 75 and section 159 of the Income-tax Act, 2025; who needs one (freelancers, exporters, investors); YouTube uses Form W-8BEN.",
    howto={"name": "How to get an Indian tax residency certificate", "description": "Steps for Indian residents.", "steps": [
        {"name": "Open Form 42", "text": "Log in to the e-filing portal with your PAN and select Form 42."},
        {"name": "Enter the details", "text": "Country, period, residential status and nature of income or purpose."},
        {"name": "Attach and verify", "text": "Upload supporting documents and verify the form."},
        {"name": "Receive Form 43", "text": "The tax officer issues the TRC in Form 43; share it with the foreign payer before payment."}]})

for p in [CANADA, AUSTRALIA, UAE, TRC]:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch CE complete")
