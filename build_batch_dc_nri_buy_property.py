# -*- coding: utf-8 -*-
"""Batch DC (18 Nov 2026): can an NRI buy residential or commercial property in India. Demand: autocomplete sweep 18 Nov
2026 (ac10), all 7 markets: "can nri purchase commercial property in india"; the site had sale, TDS, rent,
inheritance and agricultural-land pages but no buying guide.
Facts: FEMA (Non-Debt Instruments) Rules, 2019, rule 24 - an NRI or OCI may acquire immovable property in India other
than agricultural land, farm house or plantation property, by purchase (no limit on number), gift from a relative (resident, NRI or OCI), or inheritance; payment only through banking channels -
inward remittance or NRE/FCNR(B)/NRO account; not by traveller's cheques or foreign currency notes. Repatriation (RBI
Master Direction on acquisition and transfer of immovable property / remittance of assets): for property bought with
foreign exchange or NRE/FCNR funds (including home-loan repayments from those sources), sale proceeds up to the amount
so paid can be repatriated; for residential property this is limited to two properties; balance and NRO-funded
proceeds through NRO within USD 1 million per financial year with Forms 15CA/15CB. Home loans from Indian banks and
housing finance companies are permitted, repaid by inward remittance or NRE/FCNR/NRO. TDS: an NRI buyer from a
resident seller deducts 1% where consideration is INR 50 lakh or more; buying from an NRI seller, TDS on capital
gains (no TAN needed from 1 October 2026). Sources: RBI master circular/master direction, Mondaq, TaxGuru, SBNRI and
Holistic Investment summaries (checked 18 Nov 2026)."""
from urllib.parse import quote
from build_lib import page, write_page

UPDATED = "Last updated: 28 November 2026."


def wa(t):
    return "https://wa.me/917801887130?text=" + quote(t)


def ul(*x):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in x) + "</ul>"


def table(head, rows):
    return ("<table><thead><tr>" + "".join(f"<th>{h}</th>" for h in head) + "</tr></thead><tbody>"
            + "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows) + "</tbody></table>")


CONTACT = ("Email info@bharatquantumprospera.com or WhatsApp +91 78018 87130 with the property type and city, the price, how you will pay (NRE, NRO, remittance or loan) and whether the seller is resident or NRI. "
           "We reply within one working day with the FEMA, TDS and documentation checklist and a fixed-scope quote.")
SLUG = "can-nri-buy-property-in-india-residential-commercial-fema-payment-home-loan-tds-2026"
BOX = (f'<div style="border:1px solid var(--line);border-left:4px solid #C2312A;border-radius:10px;padding:16px 18px;margin:18px 0;background:var(--bg-soft)">'
       f'<p style="margin:0 0 8px;font-weight:600">How you pay now decides what you can take back later.</p>'
       f'<p style="margin:0">Paying from an NRE account or by fresh remittance keeps the purchase price repatriable when you sell; paying from NRO does not. We check the payment route, the TDS and the power of attorney before you sign. '
       f'<a href="{wa("Hi Durgesh, I am an NRI buying property in India. Can you check the payment route and TDS?")}" target="_blank" rel="noopener"><strong>WhatsApp CA Durgesh Chavda</strong></a>.</p></div>')

PAGES = [dict(
    slug=SLUG,
    title="Can an NRI Buy Property in India? (2026) Residential and Commercial Property Rules, Payment from NRE or NRO, Home Loans, TDS and Repatriation",
    em="for NRIs and OCIs in the UAE, US, UK, Singapore, Canada and Australia.",
    kicker="/ NRIs &middot; Property &middot; FEMA &middot; Updated 2026-11-18",
    lead=("Yes. An NRI or OCI cardholder can buy <strong>residential and commercial property in India</strong> without RBI approval, with <strong>no limit on the number of properties</strong>. The exceptions are <strong>agricultural land, plantation property and farm houses</strong>, which can only be inherited. "
          "The price must be paid through <strong>banking channels</strong>, by inward remittance or from an <strong>NRE, FCNR or NRO account</strong>. Cash, traveller's cheques and foreign currency notes are not allowed. Indian banks and housing finance companies can give NRIs home loans. "
          "How you pay matters when you sell: the amount paid in foreign exchange or from NRE/FCNR funds can later be <strong>repatriated</strong> (for residential property, for up to two properties), and the rest goes through the NRO account within the <strong>USD 1 million a year</strong> limit. "
          "If you buy from a resident seller and the price is <strong>INR 50 lakh or more</strong>, you deduct <strong>1% TDS</strong>; if you buy from an NRI seller, TDS is on the seller's capital gain."),
    sections=[
        ("/ What an NRI can and cannot buy", "Under the FEMA Non-Debt Instruments Rules.",
         table(["Property", "Buy?", "Receive as gift?", "Inherit?"], [
             ["Residential flat, house or plot (non-agricultural)", "Yes, any number", "Yes, from a relative", "Yes"],
             ["Commercial property (office, shop, warehouse)", "Yes, any number", "Yes, from a relative", "Yes"],
             ["Agricultural land, plantation, farm house", "No (RBI approval needed, rarely given)", "No", "Yes"]])
         + BOX
         + '<p>Agricultural land rules are covered in <a href="nri-oci-agricultural-land-india-buy-inherit-sell-tax-fema-2026.html">NRIs and agricultural land</a>.</p>'),
        ("/ Paying, borrowing and repatriating", "The money trail.",
         table(["How you pay", "Allowed?", "On sale, can it go abroad?"], [
             ["Inward remittance from abroad", "Yes", "Up to the foreign exchange paid (residential: two properties)"],
             ["NRE or FCNR(B) account", "Yes", "Yes, same as a remittance"],
             ["Home loan repaid from NRE/FCNR or remittances", "Yes", "Up to the repayments made from those sources"],
             ["NRO account or loan repaid from NRO", "Yes", "Through NRO, within USD 1 million per financial year after tax, with Forms 15CA/15CB (Forms 145/146)"],
             ["Cash, traveller's cheques, foreign currency notes", "No", "&mdash;"]])
         + ul("<strong>Home loans:</strong> Indian banks and housing finance companies lend to NRIs for buying or building residential and commercial property; repayment is by remittance or from NRE, FCNR or NRO accounts.",
              "<strong>Signing from abroad:</strong> a power of attorney executed abroad is notarised and apostilled (or attested by the Indian mission) and adjudicated for stamp duty in India; registration needs the attorney's presence and the NRI's PAN.",
              "<strong>Under-construction property:</strong> check RERA registration and pay to the builder's designated account; the builder's receipts become your proof of foreign-exchange payment for future repatriation.")),
        ("/ Tax when you buy, own and sell", "The short version.",
         ul("<strong>Buying from a resident:</strong> deduct 1% TDS when the price (or stamp duty value) is INR 50 lakh or more, deposit it with your PAN and give the seller the TDS certificate.",
            "<strong>Buying from another NRI:</strong> TDS on the full amount paid at non-resident rates (12.5% plus surcharge and cess where the gain is long-term), unless the seller has a lower deduction certificate; an NRI buyer still needs a TAN (the PAN-only route from 1 October 2026 is for resident individual and HUF buyers). See <a href=\"buying-property-from-nri-no-tan-form-141-from-1-october-2026.html\">buying from an NRI</a> and <a href=\"nri-india-property-ldc-lower-deduction-certificate.html\">lower deduction certificates</a>.",
            "<strong>Rent:</strong> a tenant paying an NRI landlord deducts TDS on the rent; see <a href=\"nri-rental-income-india-tenant-tds-31-2-percent-tan-form-144-2026.html\">TDS on rent to NRIs</a>. File an Indian return to claim deductions and refunds.",
            "<strong>Selling later:</strong> long-term gains after 24 months are taxed at 12.5% without indexation for NRIs; reinvestment exemptions can apply. See <a href=\"nri-sell-property-in-india-from-abroad-power-of-attorney-tds-repatriation-2026.html\">selling from abroad</a>.",
            "<strong>Home country:</strong> US residents report the property only if held through an entity or account (FBAR covers accounts, not directly held land), and report rent and gains on their US return with credit for Indian tax; UK, Canada and Australia residents similarly declare foreign rent and gains.")
         + '<p>Related: <a href="nre-nro-fcnr-account-tax-rules.html">NRE, NRO and FCNR accounts</a> &middot; <a href="us-citizen-buy-own-property-india-oci-fema-tax-fbar-2026.html">US citizens buying property in India</a> &middot; <a href="repatriate-money-from-india-to-abroad-nro-usd-1-million-15ca-15cb-2026.html">repatriating money from India</a> &middot; <a href="nri-inheritance-indian-property-tax-fema-2026.html">inherited property</a>.</p>'
         + f'<p><strong>Sources:</strong> Foreign Exchange Management (Non-Debt Instruments) Rules, 2019 (rule 24); RBI directions on acquisition and transfer of immovable property in India and on remittance of assets; Income-tax Act, 2025. Secondary summaries checked 18 November 2026: Mondaq, TaxGuru, SBNRI, Holistic Investment. <em>{UPDATED}</em> General information; confirm current bank and state stamp duty practice before signing.</p>'),
    ],
    faqs=[("Can an NRI buy property in India?", "Yes. NRIs and OCIs can buy any number of residential or commercial properties without RBI approval. Agricultural land, plantation property and farm houses cannot be bought, only inherited."),
          ("Can an NRI purchase commercial property in India?", "Yes. Offices, shops and warehouses can be bought freely, paid by remittance or from NRE, FCNR or NRO accounts. The two-property limit on repatriation applies to residential property, not commercial."),
          ("Can an NRI pay for property from an NRO account?", "Yes, but the sale proceeds of NRO-funded property can only be taken abroad through the NRO account within USD 1 million per financial year after tax. Paying from NRE or by remittance keeps the purchase price repatriable."),
          ("Can an NRI get a home loan in India?", "Yes. Indian banks and housing finance companies give home loans to NRIs, repaid by remittance or from NRE, FCNR or NRO accounts."),
          ("Does an NRI buyer deduct TDS?", "Yes. When buying from a resident for INR 50 lakh or more, deduct 1%. When buying from an NRI, deduct TDS on the full amount paid at non-resident rates, unless the seller gives a lower deduction certificate (Form 128); from 1 October 2026 a resident individual or HUF buyer can deposit it with a PAN in Form 141, without a TAN."),
        ("Can an NRI sell property to another NRI or an OCI cardholder?", "Yes, for residential and commercial property: under FEMA an NRI or OCI can sell it to a person resident in India, to another NRI or to an OCI cardholder. Agricultural land, plantations and farmhouses are the exception - they can be sold only to an Indian citizen resident in India. The NRI buyer must pay through Indian banking channels - an NRE, NRO or FCNR account or money remitted from abroad - not in foreign currency notes or abroad. Because the seller is a non-resident, the buyer deducts TDS on the price at non-resident rates; an NRI buyer is outside the PAN-only route for resident individual buyers, so needs a TAN and files Form 144 (old 27Q), unless the seller gives a lower deduction certificate in Form 128. The seller can repatriate the sale money through the NRO account within USD 1 million a financial year (with Forms 145 / 146), or up to the foreign exchange originally brought in for the purchase. WhatsApp +91 78018 87130 with the property type, both parties' residential status and the expected price, or book a call."),
          ("Can BQP help with my purchase?", "Yes. " + CONTACT)],
    related=[("nri-sell-property-in-india-from-abroad-power-of-attorney-tds-repatriation-2026.html", "Selling property from abroad"), ("nri-oci-agricultural-land-india-buy-inherit-sell-tax-fema-2026.html", "NRIs and agricultural land"),
             ("repatriate-money-from-india-to-abroad-nro-usd-1-million-15ca-15cb-2026.html", "Repatriating money from India")],
    cta_h="Buying property in India from abroad?", cta_b=CONTACT,
    keywords="can NRI buy property in India, can NRI purchase commercial property in India, NRI property purchase rules FEMA, NRI home loan India, NRI pay property from NRO, NRI buyer TDS 1 percent, repatriation two residential properties, OCI buy property India 2026",
    desc="Can an NRI buy property in India (2026)? Residential and commercial property without limit (not agricultural land), payment by remittance or NRE/FCNR/NRO, home loans, repatriation limits (two residential properties, USD 1 million NRO), 1% TDS buying from residents and TDS buying from NRIs.",
    howto={"name": "How an NRI buys property in India", "description": "Steps from abroad.", "steps": [
        {"name": "Check the property type", "text": "Residential or commercial is allowed; agricultural land, plantations and farm houses are not."},
        {"name": "Plan the payment", "text": "Pay by remittance or from NRE/FCNR to keep the price repatriable; NRO payments are not repatriable beyond the USD 1 million route."},
        {"name": "Arrange finance and signing", "text": "Home loan from an Indian bank if needed; apostilled power of attorney for registration."},
        {"name": "Deduct TDS", "text": "1% for a resident seller at INR 50 lakh or more; TDS on capital gains for an NRI seller."},
        {"name": "Keep the paper trail", "text": "Bank advices, builder receipts and TDS certificates support repatriation when you sell."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch DC complete")
