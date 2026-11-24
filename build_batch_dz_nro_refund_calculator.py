# -*- coding: utf-8 -*-
"""Batch DZ (20 Nov 2026): NRO interest TDS refund calculator for NRIs by country of residence - TDS deducted by the bank
(30% plus surcharge and cess) vs the lower of treaty tax (with TRC and Form 10F) and new-regime slab tax for FY 2025-26.
Pushes belated / revised returns by 31 December 2026. Logic: tools/nro-interest-refund-logic.js
(node tools/nro-interest-refund-logic.test.js, 5 tests).
Facts: NRO interest taxable for NRIs; bank TDS at 30% plus surcharge and cess (31.2% below INR 50 lakh); treaty rates on
interest for non-bank recipients - UAE 12.5%, US/UK/Canada/Australia/Singapore 15%, Saudi Arabia 10%, Qatar 10%, Oman
10% (site treaty pages); new regime slabs FY 2025-26 0-4L nil, 4-8L 5%, 8-12L 10%, 12-16L 15%, 16-20L 20%, 20-24L 25%,
above 30%; no 87A rebate for non-residents; NRE/FCNR interest exempt."""
import re, json
from urllib.parse import quote
from build_lib import page, write_page, DOMAIN
import advisory_lib as A
from advisory_lib import ul, call_box

A.UPDATED = "Last updated: 20 November 2026."
UPDATED = A.UPDATED

LOGIC = open("tools/nro-interest-refund-logic.js", encoding="utf-8").read().replace(
    'if (typeof module !== "undefined") module.exports = { nroInterestRefund: nroInterestRefund, nroSlabTax: nroSlabTax, NRO_TREATY: NRO_TREATY };', "")
_lrs = open("lrs-tcs-calculator.html", encoding="utf-8").read()
CALC_CSS = re.sub(r"\.calc-hero[^\n]*\n", "", re.search(r"<style>(.*?)</style>", _lrs, re.S).group(1))
CALC_CSS += ("\n  .calc-embed .calc-main{padding:0;max-width:none}\n  .calc-embed .rtrace{margin:8px 0 0;padding-left:18px;font-size:13px;line-height:1.55}\n"
             "  .calc-embed .rtrace li{margin:0 0 6px}\n  .calc-embed .result-card .rtrace strong,.calc-embed .result-card .rtrace b{color:#fff}\n")
SEL = 'style="width:100%;padding:10px;border:1px solid var(--line);border-radius:8px;font:inherit"'


def fld(fid, label, hint, val):
    return (f'<div class="field"><label for="{fid}">{label} <span class="hint">{hint}</span></label>'
            f'<input id="{fid}" type="number" value="{val}" min="0" step="any" inputmode="decimal"/></div>')


INPUTS = (fld("nInt", "NRO interest for FY 2025-26 (INR)", "From your bank's interest certificate.", "500000")
          + fld("nOther", "Other Indian income (INR)", "Rent, gains at slab rates etc.; 0 if none.", "0")
          + f'<div class="field"><label for="nCty">Country of residence</label><select id="nCty" {SEL}>'
            '<option value="uae">UAE (12.5%)</option><option value="usa">USA (15%)</option><option value="uk">UK (15%)</option>'
            '<option value="canada">Canada (15%)</option><option value="australia">Australia (15%)</option><option value="singapore">Singapore (15%)</option>'
            '<option value="saudi">Saudi Arabia (10%)</option><option value="qatar">Qatar (10%)</option><option value="oman">Oman (10%)</option>'
            '<option value="none">Other / not sure</option></select></div>'
          + f'<div class="field"><label for="nTrc">Do you have a tax residency certificate and Form 10F?</label><select id="nTrc" {SEL}>'
            '<option value="y">Yes</option><option value="n">No</option></select></div>')
JS = LOGIC + r'''
(function(){
  function $(id){return document.getElementById(id);}
  function inr(n){ return "INR " + Math.round(n).toLocaleString("en-IN"); }
  function show(){
    var r=nroInterestRefund({interest:$("nInt").value,other:$("nOther").value,country:$("nCty").value,trc:$("nTrc").value==="y"});
    var out=$("nOut"), list=$("nList");
    if(!r.ok){ out.textContent="Check inputs"; list.innerHTML=r.errors.map(function(e){return "<li>"+e+"</li>";}).join(""); return; }
    out.textContent="About "+inr(r.refund)+" possible refund";
    var items=["Bank TDS at 30% plus surcharge and cess: about <strong>"+inr(r.tds)+"</strong>."];
    if(r.treatyTax!==null) items.push("Tax at your treaty rate: <strong>"+inr(r.treatyTax)+"</strong>.");
    items.push("Tax at slab rates on this interest (FY 2025-26, new regime): <strong>"+inr(r.slabTax)+"</strong>.");
    items.push("Lower of the two ("+(r.basis==="treaty"?"treaty":"slab")+"): <strong>"+inr(r.actual)+"</strong>. The difference can be claimed in a belated or revised return by <strong>31 December 2026</strong>.");
    if(r.highIncome) items.push("Total income is above INR 50 lakh, so surcharge may apply; get it computed on your figures.");
    items.push("Estimate only: assumes the new regime, no deductions and no other TDS. NRE and FCNR interest is exempt and should not be entered.");
    list.innerHTML=items.map(function(e){return "<li>"+e+"</li>";}).join("");
  }
  ["nInt","nOther","nCty","nTrc"].forEach(function(id){$(id).addEventListener("input",show);$(id).addEventListener("change",show);});
  show();
})();'''
SLUG = "nri-nro-interest-tds-refund-calculator-treaty-rate-by-country-2026"
app = {"@context": "https://schema.org", "@type": "WebApplication", "name": "NRO Interest TDS Refund Calculator for NRIs",
       "url": f"{DOMAIN}/{SLUG}.html", "applicationCategory": "FinanceApplication", "operatingSystem": "Any",
       "offers": {"@type": "Offer", "price": "0", "priceCurrency": "INR"},
       "description": "Compares bank TDS on NRO interest with the lower of treaty tax and slab tax to estimate an NRI's refund.",
       "author": {"@type": "Person", "name": "CA Durgesh Chavda", "url": f"{DOMAIN}/durgesh.html"}}
wa = "https://wa.me/917801887130?text=" + quote("Hi Durgesh, I am an NRI and want to claim my NRO interest TDS refund before 31 December.")
CALC = (f"<style>{CALC_CSS}</style><script type=\"application/ld+json\">{json.dumps(app, separators=(',', ':'))}</script>"
        f'<div class="calc-embed"><div class="calc-main"><div class="calc-card"><h2>Your NRO interest</h2><p class="sub">Use FY 2025-26 figures from the bank certificate.</p>{INPUTS}</div>'
        '<div class="result-card"><div class="rlabel">Result</div><div class="rvalue red" id="nOut" style="font-size:22px;line-height:1.3">-</div>'
        '<ul class="rtrace" id="nList"></ul>'
        f'<p style="font-size:13px;margin:14px 0 0"><a href="{wa}" target="_blank" rel="noopener">Claim it with us before 31 December &rarr;</a></p></div></div></div>'
        f"<script>{JS}\n</script>")
CONTACT = ("WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with your NRO interest certificates, Form 26AS / AIS and country of residence. "
           "We reply the same working day and file before 31 December 2026, with a fixed-scope quote.")

PAGES = [dict(
    slug=SLUG,
    title="NRO Interest TDS Refund Calculator for NRIs (2026): Bank TDS vs Treaty Rate vs Slab Tax, by Country",
    em="see how much of your NRO TDS you can claim back.",
    kicker="/ Calculator &middot; NRIs &middot; NRO interest &middot; Updated 2026-11-20",
    lead=("Indian banks deduct TDS of <strong>30% plus surcharge and cess (31.2% for most NRIs)</strong> on NRO interest. Your actual tax is often far lower: either the <strong>treaty rate</strong> for your country (12.5% for the UAE, 15% for the US, UK, Canada, Australia and Singapore, 10% for Saudi Arabia, Qatar and Oman) if you have a tax residency certificate and Form 10F, or <strong>slab tax</strong> if your Indian income is small. On the new regime for FY 2025-26, the first INR 4 lakh is tax-free. "
          "The difference is a refund, but only if you file. For FY 2025-26 the last date is <strong>31 December 2026</strong>, through a belated or revised return; an updated return after that cannot claim refunds. Enter your figures to estimate the gap."),
    sections=[
        ("/ Calculator", "Bank TDS vs your actual tax.", CALC
         + call_box("my NRO interest refund", ["Your exact refund on FY 2025-26 figures, including other Indian income",
                                                "Treaty claim with TRC and Form 10F, and Form 26AS / AIS checks",
                                                "Filing the belated or revised return before 31 December 2026",
                                                "Getting the bank to apply the treaty rate going forward",
                                                "Whether to keep money in NRO, NRE or FCNR"],
                    "NRO interest certificates, Form 26AS / AIS and your country of residence.")),
        ("/ How it works", "The rules behind the numbers.",
         ul("<strong>Bank TDS:</strong> 30% plus surcharge and cess on NRO interest paid to non-residents, unless you give the bank a TRC and Form 10F for the treaty rate.",
            "<strong>Treaty rate:</strong> applies to the gross interest and is final; no surcharge or cess is added.",
            "<strong>Slab tax:</strong> FY 2025-26 new-regime slabs (nil to INR 4 lakh, then 5% to 30%) plus 4% cess; non-residents do not get the section 87A rebate.",
            "<strong>Lower of the two:</strong> you pay the lower of treaty tax and domestic tax; file a return to claim the excess.",
            "<strong>NRE and FCNR interest:</strong> exempt for non-residents; do not include it.")
         + '<p>Next steps: <a href="nri-year-end-tax-checklist-before-31-december-2026-refund-belated-itr-fast-ds-residency.html">NRI year-end checklist</a> &middot; <a href="which-itr-to-file-for-nri-ay-2026-27-itr-2-itr-3-refund-80c-deductions.html">which ITR for NRIs</a> &middot; <a href="nre-nro-fcnr-account-tax-rules.html">NRE, NRO and FCNR</a> &middot; <a href="is-nre-fd-interest-taxable-in-uk-usa-canada-australia-singapore-uae-2026.html">how home countries tax Indian interest</a>.</p>'
         f'<p><strong>Sources:</strong> Income-tax Act provisions on TDS on payments to non-residents and slab rates for FY 2025-26; India&rsquo;s tax treaties (interest articles) as summarised on our treaty pages. <em>{UPDATED}</em> Estimates only, not advice for your situation.</p>'),
    ],
    faqs=[("How much TDS do banks deduct on NRO interest?", "30% plus surcharge and cess, which is 31.2% for most NRIs, unless you provide a tax residency certificate and Form 10F for the treaty rate."),
          ("Can NRIs get a refund of TDS on NRO interest?", "Yes, if the actual tax (the lower of treaty tax and slab tax) is less than the TDS; claim it by filing an Indian return. For FY 2025-26, a belated return is possible until 31 December 2026 and a revised return until 31 March 2027 (fee after 31 December)."),
        ("How does an NRI get Form 16 or Form 16A?", "Form 16 is the salary TDS certificate an employer issues, so an NRI gets it only if paid an Indian salary or pension; for NRO interest, rent or sale proceeds, the bank, tenant or buyer issues Form 16A (Form 16B for property). Ask the deductor or download it from their portal, and check every deduction against Form 26AS or the annual information statement on the income tax portal. From tax year 2026-27 the certificates are renamed under the Income-tax Act, 2025: Form 16 becomes Form 130 and Form 16A becomes Form 131."),
        ("Who is Form 16 applicable for?", "Anyone whose employer deducted tax from salary or pension during the year, resident or NRI. If no tax was deducted, the employer need not issue it, and income from interest, rent or professional fees is covered by Form 16A instead."),
          ("What is the treaty rate on NRO interest for the UAE, US and UK?", "12.5% for UAE residents and 15% for US and UK residents (non-bank recipients), with a TRC and Form 10F."),
          ("Do NRIs get the INR 12 lakh tax-free limit?", "No. The section 87A rebate that makes income up to INR 12 lakh tax-free under the new regime is only for residents; NRIs still get the nil band up to INR 4 lakh."),
          ("Is NRE interest included?", "No. NRE and FCNR interest is exempt for non-residents and should not be entered."),
          ("Can BQP file my refund claim?", "Yes. " + CONTACT)],
    related=[("nri-year-end-tax-checklist-before-31-december-2026-refund-belated-itr-fast-ds-residency.html", "NRI year-end checklist"),
             ("nre-nro-fcnr-account-tax-rules.html", "NRE, NRO and FCNR tax rules"),
             ("nri-property-sale-tds-calculator-lower-deduction-certificate-savings.html", "NRI property sale TDS calculator")],
    cta_h="TDS on your NRO interest?", cta_b=CONTACT,
    keywords="NRO interest TDS refund calculator, NRI TDS refund on FD interest, NRO interest tax rate NRI, treaty rate NRO interest UAE USA UK, NRI TDS 31.2 percent refund, NRI refund 31 December 2026",
    desc="Calculator for NRIs: bank TDS on NRO interest (31.2%) vs the lower of treaty tax (UAE 12.5%, US/UK/Canada/Australia/Singapore 15%, Saudi/Qatar/Oman 10%) and FY 2025-26 slab tax; estimate the refund and claim it by 31 December 2026.",
    howto={"name": "How an NRI claims back excess TDS on NRO interest", "description": "Estimate, then file.", "steps": [
        {"name": "Enter your figures", "text": "NRO interest, other Indian income, country and TRC status."},
        {"name": "Compare TDS with tax", "text": "See the lower of treaty and slab tax against bank TDS."},
        {"name": "Get TRC and Form 10F", "text": "For treaty rates now and in future years."},
        {"name": "File by 31 December 2026", "text": "Belated or revised ITR-2 for FY 2025-26 to claim the refund."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch DZ complete")
