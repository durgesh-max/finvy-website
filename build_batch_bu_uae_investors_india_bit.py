# -*- coding: utf-8 -*-
"""Batch BU (12 Nov 2026): UAE investors (companies, family offices, individuals) investing in India - FDI route,
India-UAE BIT 2024, tax treaty, compliance.
Facts: India-UAE Bilateral Investment Treaty signed 13 February 2024 in Abu Dhabi, in force 31 August 2024, replacing the
2013 agreement; asset-based definition that includes portfolio investment; protections include no denial of justice and
no targeted discrimination; investor-state arbitration after pursuing local remedies (reported as three years, against
five in India's Model BIT); third-party funding of claims prohibited; claims under the old BIT had to be made by
31 January 2025; the treaty stays until at least 31 August 2034. FDI: automatic route for most sectors; Form FC-GPR within
30 days of allotment; issue price not below fair value; annual FLA return by 15 July; investors with beneficial owners in
land-border countries need approval (Press Note 3 of 2020; 10% beneficial ownership test from Press Note 2 of 2026)."""
from urllib.parse import quote
from build_lib import page, write_page

UPDATED = "Last updated: 12 November 2026."


def wa(t):
    return "https://wa.me/917801887130?text=" + quote(t)


def ul(*x):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in x) + "</ul>"


def table(head, rows):
    return ("<table><thead><tr>" + "".join(f"<th>{h}</th>" for h in head) + "</tr></thead><tbody>"
            + "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows) + "</tbody></table>")


CONTACT = ("WhatsApp +91 78018 87130 or email durgesh@bharatquantumprospera.com with the investor entity (UAE company, free zone entity, family office or individual), the Indian target and the sector. "
           "We reply the same working day with the route, the filings and a fixed-scope quote, including due diligence on the Indian company.")
SLUG = "uae-investor-investing-in-india-fdi-india-uae-bit-2024-dtaa-compliance"
BOX = (f'<div style="border:1px solid var(--line);border-left:4px solid #C2312A;border-radius:10px;padding:16px 18px;margin:18px 0;background:var(--bg-soft)">'
       f'<p style="margin:0 0 8px;font-weight:600">Investing from Dubai or Abu Dhabi into an Indian company?</p>'
       f'<p style="margin:0">We check the Indian company before you wire money (financial, tax and compliance due diligence), structure the entry, and handle FC-GPR, valuation and annual FEMA filings. '
       f'<a href="{wa("Hi Durgesh, we are a UAE investor planning to invest in an Indian company. Can you advise on structure and due diligence?")}" target="_blank" rel="noopener"><strong>WhatsApp CA Durgesh Chavda</strong></a>.</p></div>')

PAGES = [dict(
    slug=SLUG,
    title="Investing in India From the UAE: FDI Route, the India-UAE BIT 2024 and Tax Treaty Points (2026 Guide)",
    em="protection signed, paperwork still yours.",
    kicker="/ UAE companies, family offices &amp; investors &middot; FDI &middot; Updated 2026-11-12",
    lead=("UAE companies, free zone entities, family offices and individuals invest in India mostly under the automatic FDI route, with no prior approval in most sectors. "
          "Since 31 August 2024 their investments are protected by the India-UAE Bilateral Investment Treaty, signed on 13 February 2024, which notably covers portfolio investment as well as direct investment. "
          "Protection does not replace compliance: the Indian company must report the investment on Form FC-GPR within 30 days of allotting shares, issue shares at not less than fair value, and file the annual FLA return."),
    sections=[
        ("/ The India-UAE BIT 2024 in brief", "What it gives investors.",
         table(["Feature", "What it means"], [
             ["In force", "From 31 August 2024 (signed 13 February 2024), replacing the 2013 agreement; stays until at least 31 August 2034"],
             ["Covered investments", "Asset-based definition that includes portfolio investment as well as FDI"],
             ["Protections", "Includes no denial of justice and no targeted discrimination"],
             ["Disputes", "Investor-state arbitration after pursuing local remedies first (reported as three years, against five in India's Model BIT)"],
             ["Third-party funding", "Funding of claims by third parties is not allowed"],
             ["Old-treaty claims", "Had to be made by 31 January 2025"]])
         + BOX),
        ("/ The FDI steps", "For an investment into an Indian company.",
         ul("<strong>Route:</strong> automatic route for most sectors; government approval for restricted sectors, and for investors with beneficial owners in countries sharing a land border with India (see <a href=\"press-note-2-2026-fdi-land-border-countries-china-10-percent-60-day-approval.html\">Press Note 2 of 2026: the 10% test</a>).",
            "<strong>Pricing:</strong> shares issued to a non-resident at not less than fair value under an internationally accepted method, supported by a valuation report.",
            "<strong>Reporting:</strong> Form FC-GPR within 30 days of allotment on the RBI FIRMS portal; transfers between residents and non-residents on Form FC-TRS.",
            "<strong>Annual:</strong> the FLA return by 15 July each year (<a href=\"fla-return-foreign-liabilities-assets-rbi-india.html\">FLA guide</a>), plus corporate and transfer pricing compliance if there are dealings with the UAE group.",
            "<strong>Before investing:</strong> financial, tax and legal due diligence on the Indian company; see <a href=\"transaction-due-diligence-india-for-global-buyers.html\">transaction due diligence in India</a>."))
        ,
        ("/ Tax points", "Dividends, exits and the treaty.",
         ul("<strong>Tax treaty:</strong> dividends, interest and capital gains are governed by the India-UAE tax treaty together with Indian law; see <a href=\"india-uae-tax-treaty-dtaa.html\">India-UAE DTAA</a> for rates and conditions.",
            "<strong>Treaty access:</strong> claiming treaty rates needs a UAE tax residency certificate and Form 10F, and the investor must meet the treaty's residence and anti-abuse conditions.",
            "<strong>Exits:</strong> plan the exit route (secondary sale, buy-back, IPO) at entry, because each is taxed and reported differently.",
            "<strong>Repatriation:</strong> dividends and sale proceeds can be repatriated after tax; see <a href=\"repatriate-profits-india-foreign-parent.html\">repatriating profits to a foreign parent</a>.")
         + '<p>Related: <a href="indian-ca-for-clients-in-uae-gulf.html">Indian CA for clients in the UAE and Gulf</a> &middot; <a href="dubai-free-zone-indian-branch-repatriation-ca.html">Dubai free zone companies with Indian branches</a> &middot; <a href="uae-corporate-tax-2026-qfzp-fta-update.html">UAE corporate tax 2026</a>.</p>'
         f'<p><strong>Sources:</strong> Bilateral Investment Treaty between India and the UAE (signed 13 February 2024, in force 31 August 2024) and Ministry of Finance announcement; FEMA (Non-debt Instruments) Rules, 2019; RBI Master Direction on Foreign Investment in India; Press Note 3 (2020) and Press Note 2 (2026). <em>{UPDATED}</em> General information, not advice for your situation.</p>'),
    ],
    faqs=[("When did the India-UAE bilateral investment treaty come into force?", "On 31 August 2024. It was signed in Abu Dhabi on 13 February 2024 and replaced the 2013 agreement."),
          ("Does the India-UAE BIT cover portfolio investments?", "Yes. Its asset-based definition of investment includes portfolio investment, which sets it apart from India's Model BIT approach."),
          ("Do UAE investors need approval to invest in an Indian company?", "Not in most sectors, which are under the automatic route. Restricted sectors need government approval, as do investors with beneficial owners in countries sharing a land border with India."),
          ("What must the Indian company file when a UAE investor buys shares?", "Form FC-GPR within 30 days of allotment, a valuation showing the price is not below fair value, and the annual FLA return by 15 July."),
          ("Can a UAE investor go straight to arbitration under the BIT?", "Not straight away. The treaty requires local remedies to be pursued first, reported as three years, before investor-state arbitration."),
          ("Can BQP handle due diligence and FDI compliance?", "Yes. " + CONTACT)],
    related=[("india-uae-tax-treaty-dtaa.html", "India-UAE tax treaty"),
             ("indian-ca-for-clients-in-uae-gulf.html", "Indian CA for UAE and Gulf clients"),
             ("transaction-due-diligence-india-for-global-buyers.html", "Transaction due diligence in India")],
    cta_h="Investing in India from the UAE?", cta_b=CONTACT,
    keywords="India UAE BIT 2024, India UAE bilateral investment treaty, UAE investor invest in India, Dubai company FDI India, UAE family office India investment, FC-GPR UAE investor, India UAE investment protection portfolio investment",
    desc="UAE companies, family offices and individuals investing in India: the automatic FDI route, the India-UAE Bilateral Investment Treaty (in force 31 August 2024, covers portfolio investment), FC-GPR, pricing and FLA filings, and the tax treaty points for dividends and exits.",
    howto={"name": "How a UAE investor invests in an Indian company", "description": "Steps from due diligence to annual filings.", "steps": [
        {"name": "Run due diligence", "text": "Financial, tax and legal checks on the Indian company before committing."},
        {"name": "Confirm the route", "text": "Automatic route for most sectors; approval for restricted sectors or land-border beneficial owners."},
        {"name": "Price and remit", "text": "Issue shares at not less than fair value and remit through banking channels."},
        {"name": "Report and maintain", "text": "File FC-GPR within 30 days of allotment and the FLA return by 15 July each year."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch BU complete")
