# -*- coding: utf-8 -*-
"""Batch EQ (21 Nov 2026): TDS on payments to a foreign company calculator - royalty, fees for technical services,
interest and dividend; domestic rate (20% plus surcharge and cess) vs treaty rate by country, with grossing up.
Treaty rates from the Income Tax Department's 'Withholding Tax Rates' table (viewed 21 Nov 2026): US royalty/FTS 10%/15%,
interest 10%/15%, dividend 15%/25%; UK royalty/FTS 10%/15%, interest 10%/15%, dividend 15%/10%; Singapore royalty and
FTS 10%, interest 10%/15%, dividend 10%/15%; UAE royalty 10%, no FTS article, interest 5%/12.5%, dividend 10%; Germany,
Netherlands, Japan, France, Ireland, Sweden 10% throughout; South Korea 10% (dividend 15%); Australia royalty 10%/15%,
no separate FTS article, interest and dividend 15%; Mauritius royalty 15%, FTS 10%, interest 7.5%, dividend 5%/15%;
Saudi Arabia royalty and interest 10%, no FTS article, dividend 5%. Domestic rate 20% on royalty and FTS since the
Finance Act 2023 (site NRI guide). Section 195 of the 1961 Act is section 393 of the Income-tax Act, 2025; Forms 15CA/15CB
are Forms 145/146 (site pages). Logic: tools/foreign-payment-tds-logic.js (node tools/foreign-payment-tds-logic.test.js, 8 tests)."""
import re, json
from urllib.parse import quote
from build_lib import page, write_page, DOMAIN
import advisory_lib as A
from advisory_lib import ul, call_box

A.UPDATED = "Last updated: 21 November 2026."
UPDATED = A.UPDATED

LOGIC = open("tools/foreign-payment-tds-logic.js", encoding="utf-8").read().replace(
    'if (typeof module !== "undefined") module.exports = { foreignPaymentTds: foreignPaymentTds, FPT_TREATY: FPT_TREATY, FPT_TYPES: FPT_TYPES };', "")
assert "module.exports" not in LOGIC
_lrs = open("lrs-tcs-calculator.html", encoding="utf-8").read()
CALC_CSS = re.sub(r"\.calc-hero[^\n]*\n", "", re.search(r"<style>(.*?)</style>", _lrs, re.S).group(1))
CALC_CSS += ("\n  .calc-embed .calc-main{padding:0;max-width:none}\n  .calc-embed .rtrace{margin:8px 0 0;padding-left:18px;font-size:13px;line-height:1.55}\n"
             "  .calc-embed .rtrace li{margin:0 0 6px}\n  .calc-embed .result-card .rtrace strong,.calc-embed .result-card .rtrace b{color:#fff}\n")

COUNTRIES = [("usa", "United States"), ("uk", "United Kingdom"), ("singapore", "Singapore"), ("uae", "UAE"), ("germany", "Germany"),
             ("netherlands", "Netherlands"), ("japan", "Japan"), ("france", "France"), ("ireland", "Ireland"), ("sweden", "Sweden"),
             ("korea", "South Korea"), ("australia", "Australia"), ("mauritius", "Mauritius"), ("saudi", "Saudi Arabia"), ("none", "Other / no treaty")]
TYPES = [("fts", "Fees for technical or consulting services"), ("royalty", "Royalty / software or IP licence"), ("interest", "Interest on a loan"), ("dividend", "Dividend")]


def sel(fid, label, hint, opts):
    return (f'<div class="field"><label for="{fid}">{label} <span class="hint">{hint}</span></label><select id="{fid}">'
            + "".join(f'<option value="{v}">{l}</option>' for v, l in opts) + "</select></div>")


def fld(fid, label, hint, val):
    return (f'<div class="field"><label for="{fid}">{label} <span class="hint">{hint}</span></label>'
            f'<input id="{fid}" type="number" value="{val}" min="0" step="any" inputmode="decimal"/></div>')


INPUTS = (sel("pType", "Type of payment", "As described in the contract.", TYPES)
          + sel("pCountry", "Recipient company&rsquo;s country", "Where it is tax resident.", COUNTRIES)
          + fld("pAmount", "Payment amount (INR)", "Invoice value before tax.", "1000000")
          + sel("pTrc", "Tax residency certificate and Form 10F (Form 41) available?", "Needed for the treaty rate.", [("yes", "Yes"), ("no", "No")])
          + sel("pGross", "Who bears the Indian tax?", "Net-of-tax contracts need grossing up.", [("no", "Recipient: deduct from the invoice"), ("yes", "Payer: pay the invoice in full, tax on top")]))
JS = LOGIC + r'''
(function(){
  function $(id){return document.getElementById(id);}
  function inr(n){ return "INR " + Math.round(n).toLocaleString("en-IN"); }
  function pct(x){ return (Math.round(x*10000)/100) + "%"; }
  function show(){
    var r=foreignPaymentTds({amount:$("pAmount").value,type:$("pType").value,country:$("pCountry").value,trc:$("pTrc").value,grossUp:$("pGross").value});
    var out=$("pOut"), list=$("pList");
    if(!r.ok){ out.textContent="Check inputs"; list.innerHTML=r.errors.map(function(e){return "<li>"+e+"</li>";}).join(""); return; }
    out.textContent = r.basis==="no-article" ? "Possibly no TDS: no treaty article" : "TDS about "+inr(r.tds)+" at "+pct(r.rate);
    var items=[];
    items.push("Domestic rate for a foreign company: <strong>"+pct(r.domestic)+"</strong> (20% plus surcharge and 4% cess).");
    if(r.basis==="treaty") items.push("India-"+r.countryName+" treaty rate for "+r.typeName.toLowerCase()+": <strong>"+pct(r.rate)+"</strong>, lower than the domestic rate, so it applies. Treaty saving: about "+inr(r.saving)+".");
    if(r.basis==="domestic" && r.treaty!==null && r.trc) items.push("The treaty rate ("+pct(r.treaty)+") is not lower, so the domestic rate applies.");
    if(r.basis==="domestic" && !r.trc && r.countryName!=="Other / no treaty") items.push("Without a tax residency certificate and Form 10F the treaty rate cannot be used. With them, the tax could be lower.");
    if(r.basis==="no-article") items.push("The India-"+r.countryName+" treaty has no separate article for technical services. Such fees are usually taxable in India only if the foreign company has a permanent establishment here, so tax may not be due. Get this confirmed before paying without deduction.");
    if(r.grossUp) items.push("Grossed up: the payment is treated as "+inr(r.gross)+" so that the recipient receives "+inr(r.net)+" after tax.");
    else items.push("Recipient receives <strong>"+inr(r.net)+"</strong> after TDS of "+inr(r.tds)+".");
    if(r.note) items.push("Treaty note: "+r.note);
    items.push("Also needed: Form 145 (formerly 15CA) and usually a CA certificate in Form 146 (15CB) before the bank remits; GST under reverse charge on imported services.");
    items.push("Estimate only: the nature of the payment, a permanent establishment, the recipient&rsquo;s PAN and anti-abuse rules can change the result.");
    list.innerHTML=items.map(function(e){return "<li>"+e+"</li>";}).join("");
  }
  ["pType","pCountry","pAmount","pTrc","pGross"].forEach(function(id){$(id).addEventListener("input",show);$(id).addEventListener("change",show);});
  show();
})();'''
SLUG = "tds-on-payment-to-foreign-company-calculator-royalty-fts-interest-dividend-treaty-rates-2026"
app = {"@context": "https://schema.org", "@type": "WebApplication", "name": "TDS on Payments to a Foreign Company Calculator (India)",
       "url": f"{DOMAIN}/{SLUG}.html", "applicationCategory": "FinanceApplication", "operatingSystem": "Any",
       "offers": {"@type": "Offer", "price": "0", "priceCurrency": "INR"},
       "description": "Estimates Indian withholding tax on royalty, technical service fees, interest and dividends paid to a foreign company: domestic rate vs treaty rate by country, with grossing up.",
       "author": {"@type": "Person", "name": "CA Durgesh Chavda", "url": f"{DOMAIN}/durgesh.html"}}
wa = "https://wa.me/917801887130?text=" + quote("Hi Durgesh, we need help with TDS and Form 145/146 on a payment to a foreign company.")
CALC = (f"<style>{CALC_CSS}</style><script type=\"application/ld+json\">{json.dumps(app, separators=(',', ':'))}</script>"
        f'<div class="calc-embed"><div class="calc-main"><div class="calc-card"><h2>The payment</h2><p class="sub">For payments by an Indian company to a foreign company with no permanent establishment in India.</p>{INPUTS}</div>'
        '<div class="result-card"><div class="rlabel">Result</div><div class="rvalue red" id="pOut" style="font-size:22px;line-height:1.3">-</div>'
        '<ul class="rtrace" id="pList"></ul>'
        f'<p style="font-size:13px;margin:14px 0 0"><a href="book-a-call.html">Book a call before you remit &rarr;</a> &middot; <a href="{wa}" target="_blank" rel="noopener">WhatsApp</a></p></div></div></div>'
        f"<script>{JS}\n</script>")
CONTACT = ("Book a call at book-a-call.html, WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with the contract or invoice, "
           "the recipient's country and documents (tax residency certificate, Form 10F / 41, PAN if any) and the remittance date.")

PAGES = [dict(
    slug=SLUG,
    title="TDS on Payment to a Foreign Company: Calculator (2026) for Royalty, Technical Service Fees, Interest and Dividends - Domestic 20.8% vs Treaty Rates by Country",
    em="work out the Indian withholding tax before you remit.",
    kicker="/ Calculator &middot; Foreign payments &middot; Withholding tax &middot; Updated 2026-11-21",
    lead=("When an Indian company pays a foreign company a <strong>royalty, a fee for technical services, interest or a dividend</strong>, it must deduct Indian tax before remitting. "
          "The domestic rate is <strong>20% plus surcharge and cess, about 20.8% to 21.84%</strong>. If the recipient gives a <strong>tax residency certificate and Form 10F</strong> (Form 41 under the new Act), the <strong>tax treaty rate</strong> applies where it is lower: usually <strong>10%</strong> (Singapore, Germany, the Netherlands, Japan, France, Ireland) or <strong>15%</strong> (United States, United Kingdom, Australia). "
          "Some treaties, including the <strong>UAE and Saudi Arabia</strong>, have no article for technical services. Those fees are then normally taxable in India only if the foreign company has a permanent establishment here. "
          "If the contract is net of tax, the payment must be <strong>grossed up</strong>. The bank will also ask for <strong>Form 145 and Form 146</strong> (formerly 15CA and 15CB). Pick the payment type and country below."),
    sections=[
        ("/ Calculator", "Domestic rate vs treaty rate.", CALC
         + call_box("TDS on our payment to a foreign company", ["The right rate for this contract and country",
                                                               "Whether the payment is royalty, technical services or business income",
                                                               "Documents from the recipient: TRC, Form 10F / 41, PAN, no-PE declaration",
                                                               "Form 145 and the CA certificate in Form 146 for the bank",
                                                               "GST reverse charge and gross-up clauses"],
                    "the contract or invoice, the recipient's country and documents, and when you need to remit.")),
        ("/ How it works", "Rates used and limits.",
         ul("<strong>Domestic rate:</strong> 20% on royalty and technical service fees (since the Finance Act 2023), interest on foreign-currency loans and dividends, plus surcharge of 2% above INR 1 crore or 5% above INR 10 crore, plus 4% cess.",
            "<strong>Treaty rate:</strong> applied to the gross amount without surcharge or cess; the lower of the treaty and domestic rates is used. Rates are from the Income Tax Department&rsquo;s withholding-rate table.",
            "<strong>Two-rate treaties:</strong> the calculator uses the general rate and shows when a lower one applies, for example 10% for equipment rentals under the US and UK treaties or for interest paid to banks.",
            "<strong>No technical services article:</strong> under treaties such as the UAE and Saudi Arabia the fee is treated as business profits; see <a href=\"fees-for-technical-services-fts-taxability-india-make-available-treaty-withholding-2026.html\">fees for technical services and the make-available test</a>.",
            "<strong>Section number:</strong> section 195 of the 1961 Act is section 393 of the Income-tax Act, 2025; see <a href=\"income-tax-act-2025-section-195-now-393-what-changed-nri-foreign.html\">what changed</a>.",
            "<strong>Not modelled:</strong> a permanent establishment in India, lower rates on specific bonds or loans, the recipient having no PAN, GST, and anti-abuse tests.")
         + '<p>Related: <a href="india-us-dtaa-withholding-rates.html">India-US withholding rates</a> &middot; <a href="technology-licensing-royalty-payment-indian-company-to-foreign-company-fema-tds-gst-2026.html">royalty and licence payments abroad</a> &middot; <a href="old-vs-new-income-tax-form-numbers-2026-15ca-145-15cb-146-10f-41.html">old vs new form numbers</a> &middot; <a href="branch-vs-subsidiary-india-tax-calculator-foreign-company-35-percent-vs-25-percent-dividend-treaty-2026.html">branch vs subsidiary calculator</a>.</p>'
         f'<p><strong>Sources:</strong> Income Tax Department, &ldquo;Withholding Tax Rates&rdquo; (treaty rate table, viewed 21 November 2026); Income-tax provisions on tax rates for non-residents and deduction at source on payments to non-residents; India&rsquo;s tax treaties. <em>{UPDATED}</em> Estimates only, not advice for your payment.</p>'),
    ],
    faqs=[("What is the TDS rate on payments to a foreign company from India?", "For royalty, technical service fees, interest on foreign-currency loans and dividends, the domestic rate is 20% plus surcharge and 4% cess (about 20.8% to 21.84%), or the lower tax treaty rate if the recipient provides a tax residency certificate and Form 10F."),
          ("What is the TDS rate on technical service fees paid to a US company?", "Under the India-US treaty the rate is 15% (10% for ancillary services and equipment rentals) with a tax residency certificate and Form 10F, compared with about 20.8% under domestic law. Whether the service is taxable at all depends on the treaty's make-available test."),
        ("Is TDS applicable on software purchased from outside India?", "Often not, where a tax treaty applies. After the Supreme Court's 2021 decision in Engineering Analysis, payments for off-the-shelf or end-user software licences are generally not royalty under India's treaties, because no copyright is transferred, so no Indian tax and no TDS arise if the seller has no permanent establishment in India and gives a tax residency certificate and Form 10F (Form 41 from tax year 2026-27). Customised software, development services or rights to modify or distribute the code need a separate review."),
        ("Is there an equalisation levy on software or SaaS bought from abroad?", "No. The 6% levy on online advertising was abolished from 1 April 2025 and the 2% levy on e-commerce operators from 1 August 2024, so payments to foreign SaaS and digital service companies no longer attract equalisation levy."),
        ("Is GST payable on software or services bought from a foreign company?", "Yes, usually by the Indian business buyer under reverse charge at 18%, with input tax credit where eligible. Foreign suppliers of online services to Indian consumers register for GST under the OIDAR rules instead."),
          ("Is TDS deducted on service fees paid to a UAE company?", "The India-UAE treaty has no separate article for technical services, so such fees are normally taxable in India only if the UAE company has a permanent establishment here. Get this confirmed before remitting without deduction."),
          ("What does grossing up mean?", "If the contract says the foreign company must receive the invoice amount in full, the Indian payer bears the tax, and the payment is increased so that the amount after tax equals the invoice: gross = net / (1 - rate)."),
          ("Which forms are needed to remit the payment?", "Form 145 (formerly 15CA) filed online and, in most taxable cases, a chartered accountant's certificate in Form 146 (formerly 15CB), given to the bank before remittance."),
          ("Can BQP certify and file for our remittance?", "Yes. " + CONTACT)],
    related=[("fees-for-technical-services-fts-taxability-india-make-available-treaty-withholding-2026.html", "Fees for technical services"),
             ("india-us-dtaa-withholding-rates.html", "India-US withholding rates"),
             ("technology-licensing-royalty-payment-indian-company-to-foreign-company-fema-tds-gst-2026.html", "Royalty and licence payments abroad")],
    cta_h="Paying a foreign company from India?", cta_b=CONTACT,
    keywords="TDS on payment to foreign company, India withholding tax calculator, TDS on royalty to non resident, TDS on fees for technical services foreign company, section 195 TDS rate 20.8%, DTAA rate royalty FTS by country, Form 15CA 15CB Form 145 146, grossing up section 195A",
    desc="Calculator: Indian TDS on royalty, technical service fees, interest and dividends paid to a foreign company. Domestic 20% plus surcharge and cess vs treaty rates for 14 countries (US, UK 15%; Singapore, Germany, Japan 10%; UAE no FTS article), TRC and grossing up.",
    howto={"name": "How to work out TDS on a payment to a foreign company", "description": "Use the calculator, then document it.", "steps": [
        {"name": "Classify the payment", "text": "Royalty, technical services, interest, dividend or business income."},
        {"name": "Get the recipient's documents", "text": "Tax residency certificate, Form 10F / 41 and PAN if available."},
        {"name": "Compare domestic and treaty rates", "text": "Use the lower rate; check for a no-article treaty."},
        {"name": "Gross up if the contract is net of tax", "text": "Gross = net / (1 - rate)."},
        {"name": "File and remit", "text": "Form 145, a CA certificate in Form 146 where needed, deposit TDS and file the TDS return."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch EQ complete")
