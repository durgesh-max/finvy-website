# -*- coding: utf-8 -*-
"""Batch AQ: Round 28 - FEMA export rules from 1 October 2026: nine-month realisation, monthly EDF for services; deadline calculator."""
import json
import re
from build_lib import page, write_page

DOMAIN = "https://bharatquantumprospera.com"
CONTACT = "Email durgesh@bharatquantumprospera.com or WhatsApp +91 78018 87130. Fixed-scope quote within 48 hours."

_lrs = open("lrs-tcs-calculator.html", encoding="utf-8").read()
CALC_CSS = re.sub(r"\.calc-hero[^\n]*\n", "", re.search(r"<style>(.*?)</style>", _lrs, re.S).group(1))
CALC_CSS += "\n  .calc-embed .calc-main{padding:0;max-width:none}\n  .calc-embed .result-row .val{white-space:nowrap}\n"


def ul(*items):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


def src(*pairs):
    return "<p><strong>Sources:</strong> " + "; ".join(f'<a href="{u}" rel="nofollow noopener" target="_blank">{t}</a>' for t, u in pairs) + ".</p>"


SLUG = "fema-export-rules-1-october-2026-nine-month-realisation-edf-services"

JS = r'''
function addMonths(iso,m){
  var p=iso.split("-"),y=+p[0],mo=+p[1]-1+m,d=+p[2];
  y+=Math.floor(mo/12); mo=((mo%12)+12)%12;
  var last=new Date(Date.UTC(y,mo+1,0)).getUTCDate();
  return new Date(Date.UTC(y,mo,Math.min(d,last)));
}
function edfDue(iso){
  var p=iso.split("-"),end=new Date(Date.UTC(+p[0],+p[1],0));
  return new Date(end.getTime()+30*86400000);
}
function deadlines(o){
  var months=o.inr==="yes"?12:9;
  return {months:months, realise:addMonths(o.date,months), edf:o.kind==="services"?edfDue(o.date):null};
}
function show(d){return d.toLocaleDateString("en-GB",{day:"numeric",month:"long",year:"numeric",timeZone:"UTC"});}
function calc(){
  var date=document.getElementById("xDate").value; if(!date)return;
  var kind=document.getElementById("xKind").value, inr=document.getElementById("xInr").value;
  var r=deadlines({date:date,kind:kind,inr:inr});
  document.getElementById("xReal").textContent=show(r.realise);
  document.getElementById("xRealHint").textContent=r.months+" months from the "+(kind==="services"?"invoice date":kind==="warehouse"?"date of sale from the overseas warehouse":"date of shipment");
  document.getElementById("xEdf").textContent=r.edf?show(r.edf):"Shipping bill / customs EDF";
  document.getElementById("xPeriod").textContent=r.months+" months";
  document.getElementById("xPre").textContent=date<"2026-10-01"?"Before 1 Oct 2026: earlier rules apply; check with your bank":"2026 Regulations apply";
}
["xKind","xDate","xInr"].forEach(function(id){var e=document.getElementById(id);e.addEventListener("input",calc);e.addEventListener("change",calc);});
calc();
if(typeof module!=="undefined")module.exports={addMonths:addMonths,edfDue:edfDue,deadlines:deadlines};'''


def field(fid, label, hint, ctrl):
    return f'<div class="field"><label>{label} <span class="hint">{hint}</span></label>{ctrl}</div>'


INPUTS = (field("xKind", "What did you export?", "Software, IT, consulting, design and other services are all services.",
                '<select id="xKind"><option value="services">Services (including software)</option><option value="goods">Goods</option><option value="warehouse">Goods sent to a warehouse abroad</option></select>')
          + field("xDate", "Invoice date (services) / shipment or sale date (goods)", "The date the clock starts.", '<input id="xDate" type="date" value="2026-10-15" />')
          + field("xInr", "Invoiced or settled in Indian rupees?", "Rupee exports get 12 months instead of 9.",
                  '<select id="xInr"><option value="no">No (USD, EUR, GBP etc.)</option><option value="yes">Yes, INR</option></select>'))

app = {"@context": "https://schema.org", "@type": "WebApplication", "name": "Export Realisation and EDF Deadline Calculator (FEMA 2026)",
       "url": f"{DOMAIN}/{SLUG}.html", "applicationCategory": "FinanceApplication", "operatingSystem": "Any",
       "description": "Deadline to receive export proceeds and to file the EDF for services under the FEMA (Export and Import of Goods and Services) Regulations, 2026.",
       "offers": {"@type": "Offer", "price": "0", "priceCurrency": "INR"},
       "author": {"@type": "Person", "name": "CA Durgesh Chavda", "url": f"{DOMAIN}/founder.html"},
       "publisher": {"@type": "AccountingService", "name": "Bharat Quantum Prospera", "url": DOMAIN}}

BLOCK = (f"<style>{CALC_CSS}</style>"
         f'<script type="application/ld+json">{json.dumps(app, separators=(",", ":"), ensure_ascii=False)}</script>'
         f'<div class="calc-embed"><div class="calc-main"><div class="calc-card"><h2>Inputs</h2><p class="sub">Dates are calendar dates.</p>{INPUTS}</div>'
         '<div class="result-card"><div class="rlabel">Receive payment by</div><div class="rvalue red" id="xReal">-</div><div class="rhint" id="xRealHint"></div>'
         '<div class="result-row"><span class="lbl">Realisation period</span><span class="val" id="xPeriod">-</span></div>'
         '<div class="result-row"><span class="lbl">EDF due (services)</span><span class="val" id="xEdf">-</span></div>'
         '<div class="result-row"><span class="lbl">Rules</span><span class="val" id="xPre">-</span></div></div></div></div>'
         f"<script>{JS}\n</script>")

TABLE = ("<table><thead><tr><th>Export</th><th>Receive proceeds within</th><th>Clock starts</th></tr></thead><tbody>"
         "<tr><td>Services, including software</td><td>9 months</td><td>Invoice date</td></tr>"
         "<tr><td>Goods</td><td>9 months</td><td>Date of shipment</td></tr>"
         "<tr><td>Goods to a warehouse abroad</td><td>9 months</td><td>Date of sale from the warehouse</td></tr>"
         "<tr><td>Any of the above invoiced or settled in INR</td><td>12 months</td><td>Same as above</td></tr>"
         "<tr><td>Project exports</td><td>As per contract</td><td>As per contract</td></tr></tbody></table>")

sections = [
    ("/ Calculator", "Check your deadlines.", BLOCK),
    ("/ The new realisation periods", "Nine months, not fifteen.",
     "<p>The principal Regulations (Notification FEMA 23(R)/2026-RB, 13 January 2026) originally set 15 months. Before they took effect, RBI amended them (Notification FEMA 23(R)/(1)/2026-RB, 22 September 2026) to <strong>nine months</strong>, and 12 months for rupee exports. Several articles still quote 15 months; that figure never came into force.</p>" + TABLE +
     "<p>Your AD bank can extend the period on a reasoned request.</p>"),
    ("/ EDF for service exporters", "Now a monthly filing.",
     ul("Service exporters furnish the Export Declaration Form (EDF) to their AD bank within 30 days from the end of the month in which the invoice is raised.",
        "One EDF can cover all exports to one or more clients in that month.",
        "For services other than software, the EDF can instead be submitted on or before the date the payment is received.",
        "The AD bank can extend the time on a reasoned request.")),
    ("/ Other changes worth knowing", "From the 2026 Regulations.",
     ul("For exports up to INR 10 lakh per invoice or shipping bill, banks can close EDPMS entries, and allow reduction or non-realisation, on the exporter's declaration.",
        "Export receivables can be set off against import payables with the same overseas party, group companies or associated enterprises.",
        "Third-party receipts and payments are allowed once the AD bank is satisfied the transaction is genuine.",
        "Merchanting trade: both legs within six months.",
        "If proceeds stay unrealised well beyond the permitted period, future exports may need full advance payment or an irrevocable letter of credit.")),
    ("/ What freelancers and IT exporters should do", "Practical checklist.",
     ul("Put a nine-month payment term (or shorter) in client contracts and chase overdue invoices early.",
        "Diary the EDF date each month and file one consolidated EDF with your bank.",
        "Keep FIRA/FIRC or bank advices for every receipt; you need them for GST export (LUT) and income tax.",
        "Ask your bank for an extension before the nine months end if a client is delayed.",
        "Exports made before 1 October 2026 follow the earlier rules; confirm the position with your AD bank.") +
     src(("TaxUpdate: 22 September 2026 amendment", "https://taxupdate.in/finance/983/fema-export-realisation-period-october-1-2026-nine-months-rbi-amendment/"),
         ("TaxGuru: FEMA export-import regulations 2026", "https://taxguru.in/rbi/fema-export-import-regulations-2026-key-effective-1-october-2026.html")) +
     "<p><em>Last updated: 30 October 2026. Confirm against the RBI notifications and your AD bank's SOP before acting.</em></p>"),
]

faqs = [
    ("What is the export realisation period from 1 October 2026?", "Nine months for goods and services, or 12 months if the export is invoiced or settled in Indian rupees, under the FEMA (Export and Import of Goods and Services) Regulations, 2026 as amended on 22 September 2026."),
    ("Is the export realisation period 15 months?", "No. The January 2026 Regulations said 15 months, but RBI amended this to nine months (12 months for rupee exports) on 22 September 2026, before the Regulations took effect on 1 October 2026."),
    ("When does the nine-month period start for services?", "From the invoice date. For goods, it runs from the date of shipment, or from the date of sale for goods sent to a warehouse abroad."),
    ("When is the EDF due for export of services?", "Within 30 days from the end of the month in which the invoice is raised. One EDF can cover all of that month's exports. Services other than software may submit it on or before the date payment is received."),
    ("Does this apply to freelancers?", "Yes. Freelancers and consultants who invoice foreign clients are exporting services and should track the nine-month realisation period and EDF requirements with their bank."),
    ("Can BQP help with export compliance?", "Yes: EDF and EDPMS clean-up, extension requests, GST LUT and refunds, and FIRA reconciliation. " + CONTACT),
]

html = page(slug=SLUG,
            title="FEMA Export Rules From 1 October 2026: Nine-Month Realisation and Monthly EDF for Services",
            description="FEMA (Export and Import of Goods and Services) Regulations, 2026, in force from 1 October 2026: export proceeds within nine months (12 months for INR), counted from the invoice date for services; monthly EDF within 30 days of month-end. Free deadline calculator.",
            keywords="FEMA export regulations 2026, export realisation period 9 months, export realisation period 15 months, EDF for services monthly, export of services FEMA 2026, freelancer foreign payment deadline India",
            hero_kicker="/ FEMA &middot; Exporters &middot; Updated 2026-10-30",
            hero_title_html="FEMA Export Rules From 1 October 2026, <em>nine months to get paid.</em>",
            hero_lead="New FEMA export and import regulations took effect on 1 October 2026. Exporters of goods and services, including freelancers and IT companies billing foreign clients, must receive payment within nine months (12 months if invoiced in rupees). For services the clock starts on the invoice date, and the Export Declaration Form is filed monthly, within 30 days of the month-end. Many sources still say 15 months; RBI changed that on 22 September 2026.",
            sections=sections, faqs=faqs,
            related=[("freelancer-consultant-tax-india-2026-complete.html", "Related", "Freelancer and consultant tax"),
                     ("india-iec-gst-customs-foreign-exporter-importer-2026.html", "Related", "IEC, GST and customs for exporters")],
            cta_headline="Exporting services to foreign clients?", cta_body=CONTACT)
write_page(SLUG, html)
print("Batch AQ complete")
