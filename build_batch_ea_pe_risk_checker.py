# -*- coding: utf-8 -*-
"""Batch EA (20 Nov 2026): permanent establishment risk checker for foreign companies with activity in India - eight
yes/no questions mapped to fixed place, dependent agent, service, construction PE, significant economic presence and
treaty protection. Call-first tool. Logic: tools/pe-risk-logic.js (node tools/pe-risk-logic.test.js, 6 tests).
Facts: PE types under India's treaties - fixed place, dependent agent (habitually concludes or plays the principal role
in concluding contracts), service PE (threshold days vary by treaty, commonly 90 days in a 12-month period), construction
or installation PE (commonly 6 to 12 months by treaty); significant economic presence under domestic law (INR 2 crore
payments or 3 lakh users) is a business connection but treaty PE rules generally prevail for treaty residents with a
TRC; consequences: profits attributable taxed in India at foreign company rates, filing obligations."""
import re, json
from urllib.parse import quote
from build_lib import page, write_page, DOMAIN
import advisory_lib as A
from advisory_lib import ul, call_box

A.UPDATED = "Last updated: 20 November 2026."
UPDATED = A.UPDATED

LOGIC = open("tools/pe-risk-logic.js", encoding="utf-8").read().replace(
    'if (typeof module !== "undefined") module.exports = { peRisk: peRisk, PE_QUESTIONS: PE_QUESTIONS };', "")
_lrs = open("lrs-tcs-calculator.html", encoding="utf-8").read()
CALC_CSS = re.sub(r"\.calc-hero[^\n]*\n", "", re.search(r"<style>(.*?)</style>", _lrs, re.S).group(1))
CALC_CSS += ("\n  .calc-embed .calc-main{padding:0;max-width:none}\n  .calc-embed .rtrace{margin:8px 0 0;padding-left:18px;font-size:13px;line-height:1.55}\n"
             "  .calc-embed .rtrace li{margin:0 0 6px}\n  .calc-embed .result-card .rtrace strong,.calc-embed .result-card .rtrace b{color:#fff}\n"
             "  .calc-embed .peq{display:flex;gap:10px;align-items:flex-start;margin:0 0 12px;font-size:14px;line-height:1.45}\n  .calc-embed .peq input{margin-top:3px;width:18px;height:18px;flex:0 0 18px}\n")
IDS = ["office", "staffIndia", "contracts", "agentExclusive", "serviceDays", "project", "digital", "noTreaty"]
SLUG = "permanent-establishment-risk-checker-india-foreign-company-2026"
wa = "https://wa.me/917801887130?text=" + quote("Hi Durgesh, I used your PE risk checker and want to discuss our India activities.")
JS = LOGIC + r'''
(function(){
  var ids=''' + json.dumps(IDS) + r''';
  var box=document.getElementById("peQs");
  box.innerHTML=PE_QUESTIONS.map(function(q){return '<label class="peq"><input type="checkbox" id="pe_'+q.id+'"/><span>'+q.text+'</span></label>';}).join("");
  function show(){
    var a={}; ids.forEach(function(id){a[id]=document.getElementById("pe_"+id).checked;});
    var r=peRisk(a), out=document.getElementById("peOut"), list=document.getElementById("peList");
    var label={low:"Low risk on these answers",medium:"Medium risk: review needed",high:"High risk: get advice before you scale"}[r.band];
    out.textContent=label;
    var items=[];
    if(r.band==="low"){items.push("None of the common PE triggers is ticked. Keep it that way as you grow: avoid staff, offices or agents in India who could change the answer.");}
    else{
      items.push("Main exposure: <strong>"+r.topType+"</strong>.");
      if(r.types.length>1) items.push("Also flagged: "+r.types.filter(function(t){return t!==r.topType;}).join(", ")+".");
      items.push("A PE makes the profits linked to your India activity taxable in India at foreign-company rates, with return filing and transfer pricing obligations.");
      items.push("Common fixes: an Indian subsidiary or employer of record for staff, tighter agent contracts, tracking service and project days against your treaty, and a tax residency certificate.");
    }
    items.push("Screening only: the answer depends on your treaty, facts and contracts.");
    list.innerHTML=items.map(function(e){return "<li>"+e+"</li>";}).join("");
  }
  ids.forEach(function(id){document.getElementById("pe_"+id).addEventListener("change",show);});
  show();
})();'''
app = {"@context": "https://schema.org", "@type": "WebApplication", "name": "India Permanent Establishment Risk Checker",
       "url": f"{DOMAIN}/{SLUG}.html", "applicationCategory": "BusinessApplication", "operatingSystem": "Any",
       "offers": {"@type": "Offer", "price": "0", "priceCurrency": "INR"},
       "description": "Eight-question screen showing whether a foreign company's India activities may create a permanent establishment.",
       "author": {"@type": "Person", "name": "CA Durgesh Chavda", "url": f"{DOMAIN}/durgesh.html"}}
CALC = (f"<style>{CALC_CSS}</style><script type=\"application/ld+json\">{json.dumps(app, separators=(',', ':'))}</script>"
        '<div class="calc-embed"><div class="calc-main"><div class="calc-card"><h2>Your India activities</h2><p class="sub">Tick everything that applies today or in the next 12 months.</p><div id="peQs"></div></div>'
        '<div class="result-card"><div class="rlabel">Result</div><div class="rvalue red" id="peOut" style="font-size:22px;line-height:1.3">-</div>'
        '<ul class="rtrace" id="peList"></ul>'
        f'<p style="font-size:13px;margin:14px 0 0"><a href="{wa}" target="_blank" rel="noopener">Discuss your result with CA Durgesh Chavda &rarr;</a></p></div></div></div>'
        f"<script>{JS}\n</script>")
CONTACT = ("Email info@bharatquantumprospera.com or WhatsApp +91 78018 87130 with your country, what your people and partners do in India, and how long. "
           "We reply within one working day to set up a call, then send a written scope and fixed-fee quote.")

PAGES = [dict(
    slug=SLUG,
    title="Permanent Establishment Risk Checker for Foreign Companies in India (2026): Eight Questions on Offices, Staff, Agents, Services and Projects",
    em="find out whether your India activity may be taxable in India.",
    kicker="/ Tool &middot; Foreign companies &middot; Permanent establishment &middot; Updated 2026-11-20",
    lead=("A foreign company becomes taxable in India on the profits linked to its India activity if it has a <strong>permanent establishment (PE)</strong> here. The usual triggers are a <strong>fixed place</strong> at its disposal, <strong>employees working from India</strong>, an <strong>agent who concludes contracts</strong> for it, <strong>services</strong> in India beyond the treaty's day threshold (commonly 90 days in 12 months), or a <strong>project</strong> beyond the treaty's time limit. "
          "Under Indian domestic law, large revenue or user numbers from India (INR 2 crore or 3 lakh users) also create a business connection, though treaty protection usually decides the final answer for treaty residents with a tax residency certificate. "
          "Tick the questions below to see where you stand, then book a call to check your treaty, contracts and options before the exposure grows."),
    sections=[
        ("/ Checker", "Eight questions.", CALC
         + call_box("permanent establishment risk", ["Which PE types your India activities may create under your treaty",
                                                       "Service and project day counts against treaty thresholds",
                                                       "Agent and distributor contract terms that avoid dependent agent PE",
                                                       "Subsidiary, employer of record or contractor: which fits now",
                                                       "If a PE exists: profit attribution, filings and fixing past years"],
                    "your country, what your staff, agents and partners do in India, and for how long.")),
        ("/ What each answer means", "The PE types behind the questions.",
         ul("<strong>Fixed place PE:</strong> an office, branch, factory or other place through which the business is carried on, including space provided by others but at your disposal.",
            "<strong>Dependent agent PE:</strong> a person in India who habitually concludes contracts, or plays the principal role leading to them, for your company.",
            "<strong>Service PE:</strong> services furnished in India by your staff or contractors beyond the treaty's threshold (often 90 days in a 12-month period; some treaties differ).",
            "<strong>Construction or installation PE:</strong> a site or project beyond the treaty time limit (often 6, 9 or 12 months).",
            "<strong>Significant economic presence:</strong> Indian domestic-law test for remote and digital businesses; treaties usually still require a PE for treaty residents.",
            "<strong>No treaty or no TRC:</strong> without treaty protection, the wider domestic business-connection rules apply.")
         + '<p>Read more: <a href="permanent-establishment-india-meaning-types-risk-tax-foreign-company-2026.html">permanent establishment in India</a> &middot; <a href="foreign-company-remote-employee-india-pe-risk-eor-contractor-subsidiary-2026.html">remote employees, EOR and subsidiaries</a> &middot; <a href="significant-economic-presence-foreign-saas-app-company-india-2-crore-3-lakh-users-2026.html">significant economic presence</a> &middot; <a href="us-company-paying-indian-contractor-w-8ben-no-1099-gst-lut-pe-risk-2026.html">US companies paying Indian contractors</a> &middot; <a href="foreign-company-india-advisor-market-research-entity-due-diligence-m-and-a-joint-venture-2026.html">working with an Indian CA</a>.</p>'
         f'<p><strong>Sources:</strong> Income-tax Act, 2025 (business connection and significant economic presence, carried from section 9(1)(i) of the 1961 Act); India&rsquo;s tax treaties (Article 5); OECD Model Commentary. <em>{UPDATED}</em> Screening tool only, not advice for your situation.</p>'),
    ],
    faqs=[("What creates a permanent establishment in India?", "Typically a fixed place at the company's disposal, employees working from India, an agent who concludes contracts for it, services beyond the treaty's day threshold, or a construction or installation project beyond the treaty's time limit."),
          ("Does a remote employee in India create a PE?", "It can. An employee working from India for a foreign company, especially in sales or management roles or from a home office the company relies on, can create a fixed place or agency PE; many companies use an employer of record or a subsidiary instead."),
          ("How many days create a service PE in India?", "It depends on the treaty; many use about 90 days in a 12-month period, and some count days differently or set other thresholds."),
          ("What happens if a foreign company has a PE in India?", "Profits attributable to the PE are taxable in India at foreign-company rates, and the company must file Indian returns and meet transfer pricing rules."),
          ("Is the checker result final?", "No. It is a screen; the answer depends on your treaty, contracts and facts, which we review on a call."),
          ("Can BQP review our PE position?", "Yes. " + CONTACT)],
    related=[("permanent-establishment-india-meaning-types-risk-tax-foreign-company-2026.html", "Permanent establishment in India"),
             ("foreign-company-remote-employee-india-pe-risk-eor-contractor-subsidiary-2026.html", "Remote employees, EOR or subsidiary"),
             ("foreign-company-india-advisor-market-research-entity-due-diligence-m-and-a-joint-venture-2026.html", "Working with an Indian CA")],
    cta_h="Worried about a taxable presence in India?", cta_b=CONTACT,
    keywords="permanent establishment risk India checker, PE risk India foreign company, does my company have a PE in India, service PE 90 days India, dependent agent PE India, remote employee India PE, significant economic presence India",
    desc="PE risk checker for foreign companies in India (2026): eight questions on offices, employees, agents, services, projects, digital revenue and treaty protection, showing the main permanent establishment exposure and what to do next.",
    howto={"name": "How a foreign company screens its India PE risk", "description": "Eight-question check and next steps.", "steps": [
        {"name": "Answer the questions", "text": "Offices, staff, agents, services, projects, digital revenue, treaty status."},
        {"name": "See the main exposure", "text": "Fixed place, dependent agent, service or construction PE."},
        {"name": "Check your treaty", "text": "Service and project thresholds and the TRC."},
        {"name": "Fix the structure", "text": "Subsidiary or employer of record, agent contracts, day tracking."},
        {"name": "Review yearly", "text": "Re-check as headcount and activity in India grow."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch EA complete")
