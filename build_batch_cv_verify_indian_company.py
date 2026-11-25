# -*- coding: utf-8 -*-
"""Batch CV (18 Nov 2026): how a foreign buyer, importer or investor checks that an Indian company is genuine.
Demand: Google autocomplete sweep 18 Nov 2026 across US, UK, UAE, Canada, Australia, Singapore and India returned
"verify indian company", "how to check if a company is real", "list of background verification companies in india"
in all 7 markets. The site had a paid counterparty-DD service page but no free how-to.
Facts: official free registers - MCA21 'View Company or LLP Master Data' (CIN/LLPIN, status, incorporation date,
registered office, capital, last AGM and balance sheet dates, directors, charges) and 'View Director Master Data' by
DIN; CIN is 21 characters (listing status, industry code, state, year, ownership type e.g. PTC/PLC/FTC, number);
GST 'Search Taxpayer' on services.gst.gov.in (legal and trade name, status active/cancelled/suspended, registration
date, constitution, return filing); GSTIN is 15 characters (state code, PAN, entity number, Z, check digit); DGFT IEC
lookup for importers/exporters; Udyam registration verification; eCourts party-name search; IBBI public
announcements for insolvency; global sanctions lists (OFAC SDN, UN, EU). Checked 18 Nov 2026."""
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


CONTACT = ("Email info@bharatquantumprospera.com or WhatsApp +91 78018 87130 with the Indian company's name, CIN or GSTIN, and what you are about to sign or pay. "
           "We reply within one working day with the checks needed and a fixed-scope quote for a written verification or full due diligence report.")
SLUG = "how-to-verify-indian-company-is-genuine-mca-gst-iec-check-foreign-buyers-2026"
BOX = (f'<div style="border:1px solid var(--line);border-left:4px solid #C2312A;border-radius:10px;padding:16px 18px;margin:18px 0;background:var(--bg-soft)">'
       f'<p style="margin:0 0 8px;font-weight:600">About to pay an advance, sign a distributor deal or invest?</p>'
       f'<p style="margin:0">The free checks below catch fake and dormant companies. They do not tell you whether the accounts are real, who really owns the business or whether the directors have a history. A Chartered Accountant can read the filed financial statements, charges and director records and give you a written view. '
       f'<a href="{wa("Hi Durgesh, I need to verify an Indian company before signing / paying. Can you help?")}" target="_blank" rel="noopener"><strong>WhatsApp CA Durgesh Chavda</strong></a>.</p></div>')

PAGES = [dict(
    slug=SLUG,
    title="How to Verify an Indian Company Is Genuine (2026): Free MCA, GST, IEC and Court Checks for Foreign Buyers, Importers and Investors",
    em="ten minutes of free checks before you pay or sign.",
    kicker="/ Foreign companies &middot; Due diligence &middot; Supplier checks &middot; Updated 2026-11-18",
    lead=("You can check most of what an Indian company tells you, free, on government websites. Look up its <strong>CIN</strong> (company identification number) on the <strong>Ministry of Corporate Affairs (MCA) master data</strong> page to confirm it exists, is <strong>Active</strong> (not struck off or dormant), when it was incorporated, its registered office, capital and directors. "
          "Then check its <strong>GSTIN</strong> on the <strong>GST portal</strong> (status, legal name and whether it files returns), its <strong>IEC</strong> on the <strong>DGFT</strong> site if it imports or exports, the directors' other companies by <strong>DIN</strong>, court cases on <strong>eCourts</strong>, and insolvency notices on the <strong>IBBI</strong> site. "
          "Make sure the <strong>bank account name matches the legal name</strong> on these records before paying. These checks catch fake, dormant and struck-off companies; they do not verify the financials or the real owners, which is what a due diligence report covers."),
    sections=[
        ("/ The free checks", "What to check, and where.",
         table(["Check", "Where (free, official)", "What it tells you"], [
             ["Company exists and is active", "MCA: 'View Company or LLP Master Data' (enter CIN, LLPIN or name)", "Status (Active, Strike Off, Under process of striking off, Dormant, Amalgamated), incorporation date, registered office, authorised and paid-up capital, last AGM and balance sheet dates"],
             ["Directors", "MCA: same page and 'View Director Master Data' (by DIN)", "Who the directors are, when appointed, and their other companies"],
             ["Secured loans", "MCA master data: index of charges", "Whether lenders hold charges over the company's assets"],
             ["GST registration", "GST portal: 'Search Taxpayer' by GSTIN", "Legal and trade name, status (Active, Cancelled, Suspended), registration date, business type and whether returns are filed"],
             ["Import/export licence", "DGFT: IEC lookup", "Whether the importer-exporter code is valid and in whose name"],
             ["MSME status", "Udyam Registration portal: verify certificate", "Whether a claimed Udyam number (format UDYAM-XX-00-0000000) is real"],
             ["Court cases", "eCourts services: case search by party name", "Civil and criminal cases in district and high courts"],
             ["Insolvency", "IBBI: public announcements; NCLT cause lists", "Whether the company is in an insolvency or liquidation process"],
             ["Sanctions", "OFAC SDN, UN and EU consolidated lists", "Whether the company or its owners are sanctioned"]])
         + BOX),
        ("/ Reading the identifiers", "Spot a fake number in seconds.",
         ul("<strong>CIN (21 characters)</strong>, for example U12345GJ2019PTC123456: U or L (unlisted or listed), a five-digit industry code, the state code (GJ for Gujarat, MH for Maharashtra, KA for Karnataka, DL for Delhi), the year of incorporation, the type (PTC private, PLC public, FTC subsidiary of a foreign company, OPC one person company) and a registration number. The state and year must match what the company tells you.",
            "<strong>LLPIN</strong> has the form AAA-1234 for limited liability partnerships.",
            "<strong>GSTIN (15 characters)</strong>: a two-digit state code, the company's 10-character PAN, an entity number, the letter Z and a check character. The PAN inside the GSTIN should be the same across all the company's state registrations.",
            "If the documents you were sent show a different name, state or date from the official records, stop and ask why.")),
        ("/ Red flags", "When to get professional help.",
         ul("Status is Strike Off, Dormant or 'Under process of striking off', or GST is Cancelled or Suspended.",
            "Incorporated only months ago but claims years of export history or large factories.",
            "Paid-up capital of a few thousand dollars against a large order or advance.",
            "Last AGM or balance sheet date years old (annual filings not made).",
            "Directors who sit on dozens of unrelated companies, or recently replaced directors.",
            "A name very close to a well-known Indian group, a free email domain, or a residential registered office for a supposed manufacturer.",
            "Bank details in a different name from the legal name, or a request to change bank details by email (a common payment fraud).",
            "Pressure to pay a large advance before samples, inspection or a signed contract.")
         + '<p>Related: <a href="india-counterparty-background-check-compliance-dd.html">India counterparty background check and compliance DD</a> &middot; <a href="due-diligence-indian-company-foreign-buyer.html">due diligence on an Indian company for a foreign buyer</a> &middot; <a href="india-services-for-foreign-companies-complete-list.html">services for foreign companies</a>.</p>'
         + f'<p><strong>Sources:</strong> Ministry of Corporate Affairs MCA21 portal (company and director master data, index of charges); GST common portal taxpayer search; DGFT IEC services; Udyam Registration portal; eCourts services; Insolvency and Bankruptcy Board of India public announcements; OFAC, UN and EU sanctions lists. Portal names and fields checked 18 November 2026. <em>{UPDATED}</em> General information; official records can lag recent changes.</p>'),
    ],
    faqs=[("How can I check if an Indian company is real?", "Search its name or CIN on the Ministry of Corporate Affairs 'View Company or LLP Master Data' page. A genuine company shows its CIN, status (it should be Active), incorporation date, registered office, capital and directors. Then check its GSTIN on the GST portal's Search Taxpayer page."),
          ("Is it free to verify an Indian company?", "Yes. MCA master data, the GST taxpayer search, the DGFT IEC lookup, Udyam verification, eCourts and IBBI announcements are all free. Downloading full filed documents (financial statements, annual returns) from MCA requires a small fee."),
          ("What does 'Strike Off' mean on MCA?", "The Registrar has removed the company from the register, usually for not filing or not doing business. A struck-off company cannot legally trade or sign contracts until it is restored by the NCLT."),
          ("How do I verify an Indian exporter?", "Check its IEC on the DGFT site, its GSTIN and status on the GST portal, and its company record on MCA, and make sure the names match each other and the bank account."),
        ("What is the format of an Indian company registration number?", "An Indian company is identified by its Corporate Identification Number (CIN), issued by the Ministry of Corporate Affairs: 21 characters, for example U72900DL2015PTC123456. That reads as U or L (unlisted or listed), a five-digit industry code, a two-letter state code, the year of incorporation, the company type (PTC private, PLC public, OPC one person company, FTC subsidiary of a foreign company) and a six-digit registration number. An LLP has an LLPIN of the form AAA-1234 instead. Check that the state and year match what the company tells you, then look the number up free on the MCA master data page."),
        ("Where do I find an Indian company's CIN?", "On its certificate of incorporation, invoices and letterhead (companies must show it), its website, or by searching the company name on the MCA View Company or LLP Master Data page."),
        ("How do I check an Indian GST number?", "On the GST portal (gst.gov.in), use Search Taxpayer and enter the 15-character GSTIN. It shows the legal and trade name, whether the registration is active, cancelled or suspended, the date of registration, the type of business and whether returns are being filed. The PAN inside the GSTIN (characters 3 to 12) should match the company's PAN, and the name should match the MCA record and the invoice."),
        ("Can I search a GST number by PAN?", "Yes. On the GST portal, Search Taxpayer has a Search by PAN option that lists the GSTINs registered against a PAN, one for each state where the business is registered, with their status. It is useful to confirm that a supplier's GSTIN really belongs to its PAN."),
        ("What is the format of a GST number (GSTIN)?", "A GSTIN has 15 characters: a 2-digit state code, the 10-character PAN of the business, one character for the number of registrations in that state, the letter Z by default, and a final check character."),
        ("Does an Indian supplier need a GST number to sell to a foreign buyer?", "Not always: suppliers below the registration threshold who make only exempt supplies may not have one, but most established exporters and service providers are registered and quote their GSTIN on invoices. An export invoice without GST usually states that it is under a letter of undertaking (LUT)."),
          ("Do these checks prove the company is financially sound?", "No. They confirm identity and status. Financial health, real ownership, tax and legal exposure need a review of filed financial statements and records, which is what a due diligence report covers."),
          ("Can BQP verify a company for us?", "Yes. " + CONTACT)],
    related=[("india-counterparty-background-check-compliance-dd.html", "Counterparty background check"), ("due-diligence-indian-company-foreign-buyer.html", "Due diligence for a foreign buyer"),
             ("india-services-for-foreign-companies-complete-list.html", "Services for foreign companies")],
    cta_h="Need a written check on an Indian company?", cta_b=CONTACT,
    keywords="verify Indian company, how to check if an Indian company is genuine, check Indian company registration, MCA company master data, verify GSTIN, verify Indian supplier, verify Indian exporter IEC, Indian company strike off check, background check Indian company for foreign buyer",
    desc="How to verify an Indian company is genuine in 2026, free: MCA company and director master data (CIN, status, directors, charges), GST taxpayer search, DGFT IEC, Udyam, eCourts and IBBI checks, how to read CIN and GSTIN, and red flags before paying or signing.",
    howto={"name": "How to verify an Indian company before paying or signing", "description": "Free checks for foreign buyers, importers and investors.", "steps": [
        {"name": "Check MCA master data", "text": "Search the CIN or name; confirm status Active, incorporation date, registered office, capital and directors."},
        {"name": "Check GST and IEC", "text": "Search the GSTIN on the GST portal and the IEC on DGFT; confirm names and status match."},
        {"name": "Check directors and charges", "text": "Look up directors by DIN and review the index of charges."},
        {"name": "Check courts, insolvency and sanctions", "text": "Search eCourts, IBBI announcements and sanctions lists."},
        {"name": "Match the bank account", "text": "Confirm the beneficiary name matches the legal name before paying; get a due diligence report for large deals."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch CV complete")
