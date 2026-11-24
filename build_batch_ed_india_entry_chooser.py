# -*- coding: utf-8 -*-
"""Batch ED (20 Nov 2026): India entry structure chooser for foreign companies - five questions (goal, income in India,
headcount, sector, horizon) recommending contractors/distributor, employer of record, liaison office, project office,
branch office, LLP or private limited subsidiary, with links to the detailed guides. Call-first tool.
Logic: tools/india-entry-chooser-logic.js (node tools/india-entry-chooser-logic.test.js, 8 tests).
Facts (site pages): liaison office cannot earn income; branch and project offices need AD bank / RBI approval under the
2016 regulations; LLP FDI only in 100% automatic sectors without conditions; subsidiary 100% FDI automatic in most
sectors, needs a resident director; EOR suits first hires without an entity; PE risk from staff and agents."""
import re, json
from urllib.parse import quote
from build_lib import page, write_page, DOMAIN
import advisory_lib as A
from advisory_lib import ul, call_box

A.UPDATED = "Last updated: 20 November 2026."
UPDATED = A.UPDATED

LOGIC = open("tools/india-entry-chooser-logic.js", encoding="utf-8").read().replace(
    'if (typeof module !== "undefined") module.exports = { indiaEntry: indiaEntry };', "")
_lrs = open("lrs-tcs-calculator.html", encoding="utf-8").read()
CALC_CSS = re.sub(r"\.calc-hero[^\n]*\n", "", re.search(r"<style>(.*?)</style>", _lrs, re.S).group(1))
CALC_CSS += ("\n  .calc-embed .calc-main{padding:0;max-width:none}\n  .calc-embed .rtrace{margin:8px 0 0;padding-left:18px;font-size:13px;line-height:1.55}\n"
             "  .calc-embed .rtrace li{margin:0 0 6px}\n  .calc-embed .result-card .rtrace strong,.calc-embed .result-card .rtrace b{color:#fff}\n"
             "  .calc-embed .result-card .rtrace a{color:#fff;text-decoration:underline}\n")
SEL = 'style="width:100%;padding:10px;border:1px solid var(--line);border-radius:8px;font:inherit"'


def sel(fid, label, opts):
    o = "".join(f'<option value="{v}">{t}</option>' for v, t in opts)
    return f'<div class="field"><label for="{fid}">{label}</label><select id="{fid}" {SEL}>{o}</select></div>'


INPUTS = (sel("eGoal", "What do you want to do in India?", [("build", "Build a team or operations"), ("sell", "Sell to Indian customers"), ("test", "Test the market / represent the parent"), ("project", "Execute a specific project or contract")])
          + sel("eRev", "Will the India presence earn income from Indian customers?", [("yes", "Yes"), ("no", "No")])
          + sel("eStaff", "People working for you in India in the next 12 months", [("6+", "6 or more"), ("1-5", "1 to 5"), ("0", "None")])
          + sel("eSector", "Is your sector open to 100% foreign investment under the automatic route?", [("open", "Yes / most likely"), ("restricted", "No or not sure (caps, approval, land-border owners)")])
          + sel("eDur", "Time horizon", [("long", "Long term (2+ years)"), ("short", "Short term or uncertain")]))
LINKS = {
    "Private limited subsidiary": "foreign-company-setup-indian-subsidiary-wos.html",
    "Private limited subsidiary (with approval where required)": "fdi-rules-india-2026-automatic-government-route-reporting-draft-foreign-investment-rules.html",
    "Employer of record": "employer-of-record-india-hire-from-abroad.html",
    "Liaison office": "rbi-approval-place-of-business-india-liaison-branch-project-office-form-fnc-2026.html",
    "Project office": "project-office-india-foreign-company-registration-fema-conditions-tax-2026.html",
    "Contractors or distributor, no entity yet": "us-company-paying-indian-contractor-w-8ben-no-1099-gst-lut-pe-risk-2026.html",
    "Distributor or licensee, then a subsidiary": "find-distributor-business-partner-in-india-foreign-company-agreement-checks-2026.html",
}
JS = LOGIC + r'''
(function(){
  var LINKS=''' + json.dumps(LINKS) + r''';
  function $(id){return document.getElementById(id);}
  function show(){
    var r=indiaEntry({goal:$("eGoal").value,revenue:$("eRev").value,staff:$("eStaff").value,sector:$("eSector").value,duration:$("eDur").value});
    var out=$("eOut"), list=$("eList");
    if(!r.ok){ out.textContent="Check inputs"; list.innerHTML=r.errors.map(function(e){return "<li>"+e+"</li>";}).join(""); return; }
    out.textContent=r.primary;
    var items=[];
    if(LINKS[r.primary]) items.push('Read the guide: <a href="'+LINKS[r.primary]+'">'+r.primary+'</a>.');
    items.push("Also consider: "+r.alternatives.join("; ")+".");
    items.push('Check the tax side too: <a href="permanent-establishment-risk-checker-india-foreign-company-2026.html">PE risk checker</a>.');
    items.push("Screening only: sector rules, your home country and your partners can change the answer.");
    list.innerHTML=items.map(function(e){return "<li>"+e+"</li>";}).join("");
  }
  ["eGoal","eRev","eStaff","eSector","eDur"].forEach(function(id){$(id).addEventListener("change",show);});
  show();
})();'''
SLUG = "india-entry-structure-chooser-subsidiary-llp-branch-liaison-eor-foreign-company-2026"
app = {"@context": "https://schema.org", "@type": "WebApplication", "name": "India Entry Structure Chooser for Foreign Companies",
       "url": f"{DOMAIN}/{SLUG}.html", "applicationCategory": "BusinessApplication", "operatingSystem": "Any",
       "offers": {"@type": "Offer", "price": "0", "priceCurrency": "INR"},
       "description": "Five questions recommending a subsidiary, LLP, branch, liaison or project office, employer of record or contractor model for India.",
       "author": {"@type": "Person", "name": "CA Durgesh Chavda", "url": f"{DOMAIN}/durgesh.html"}}
wa = "https://wa.me/917801887130?text=" + quote("Hi Durgesh, I used your India entry chooser and want to discuss the right structure for us.")
CALC = (f"<style>{CALC_CSS}</style><script type=\"application/ld+json\">{json.dumps(app, separators=(',', ':'))}</script>"
        f'<div class="calc-embed"><div class="calc-main"><div class="calc-card"><h2>Your India plan</h2><p class="sub">Answer five questions.</p>{INPUTS}</div>'
        '<div class="result-card"><div class="rlabel">Suggested structure</div><div class="rvalue red" id="eOut" style="font-size:22px;line-height:1.3">-</div>'
        '<ul class="rtrace" id="eList"></ul>'
        f'<p style="font-size:13px;margin:14px 0 0"><a href="{wa}" target="_blank" rel="noopener">Discuss it with CA Durgesh Chavda &rarr;</a></p></div></div></div>'
        f"<script>{JS}\n</script>")
CONTACT = ("Email info@bharatquantumprospera.com or WhatsApp +91 78018 87130 with your country, sector, what you want to do in India and your timeline. "
           "We reply within one working day to set up a call, then send a written scope and fixed-fee quote.")

PAGES = [dict(
    slug=SLUG,
    title="Which India Entry Structure Fits? (2026) Subsidiary, LLP, Branch, Liaison or Project Office, Employer of Record or Contractors - A Quick Chooser for Foreign Companies",
    em="answer five questions, get a starting point.",
    kicker="/ Tool &middot; Foreign companies &middot; Market entry &middot; Updated 2026-11-20",
    lead=("Foreign companies usually enter India in one of seven ways. They can engage <strong>contractors or a distributor</strong> with no entity, hire through an <strong>employer of record</strong>, or open a <strong>liaison office</strong>, which may not earn income. They can open a <strong>branch</strong> or <strong>project office</strong>, both with RBI approval, form an <strong>LLP</strong> (only in sectors open to 100% automatic foreign investment), or set up a <strong>private limited subsidiary</strong>, the most common route for anything long-term. "
          "The right choice depends on whether you will earn income in India, how many people you will have here, your sector's foreign-investment rules and how long you plan to stay. Each also carries tax consequences, especially permanent establishment risk if staff or agents work in India without an entity. "
          "Answer the five questions for a starting point, then book a call to confirm it for your sector and home country."),
    sections=[
        ("/ Chooser", "Five questions.", CALC
         + call_box("our India entry structure", ["Whether the suggested structure fits your sector and home-country tax",
                                                   "Approvals, timelines and documents",
                                                   "Permanent establishment and transfer pricing in each option",
                                                   "How to move from contractors or EOR to a subsidiary later",
                                                   "Banking, FEMA filings and first-year compliance"],
                    "your country, sector, what you want to do in India, expected headcount and timeline.")),
        ("/ The options at a glance", "What each allows.",
         ul("<strong>Contractors or distributor:</strong> fastest and lightest; watch permanent establishment and misclassification risk.",
            "<strong>Employer of record:</strong> hire employees without an entity; suitable for a few people, not for selling or signing contracts in India.",
            "<strong>Liaison office:</strong> represent the parent and promote business; no income in India; RBI-framework approval.",
            "<strong>Branch office:</strong> can earn specified income; taxed as a foreign company; RBI-framework approval.",
            "<strong>Project office:</strong> for a specific contract in India.",
            "<strong>LLP:</strong> for services in sectors open to 100% automatic foreign investment without conditions.",
            "<strong>Private limited subsidiary:</strong> the standard long-term vehicle; 100% foreign ownership in most sectors; one resident director.")
         + '<p>Detailed guides: <a href="india-market-entry-foreign-company-guide.html">India market entry guide</a> &middot; <a href="branch-office-vs-liaison-vs-wos-india-foreign.html">liaison vs branch vs subsidiary</a> &middot; <a href="can-foreign-national-register-company-in-india-how-long-documents-resident-director-2026.html">registering a company</a> &middot; <a href="foreign-company-india-advisor-market-research-entity-due-diligence-m-and-a-joint-venture-2026.html">working with an Indian CA</a>.</p>'
         f'<p><strong>Sources:</strong> Consolidated FDI Policy; FEMA (Non-Debt Instruments) Rules, 2019; FEMA establishment of branch, liaison or project office regulations, 2016; Companies Act, 2013; LLP Act, 2008. <em>{UPDATED}</em> Screening tool only, not advice for your situation.</p>'),
    ],
    faqs=[("What is the best way for a foreign company to enter India?", "For a long-term business with staff and Indian revenue, usually a private limited subsidiary; for testing the market, contractors, a distributor, an employer of record or a liaison office; for a specific contract, a project office."),
        ("What are the advantages and disadvantages of a foreign subsidiary in India?", "Advantages: a separate company with limited liability for the parent, about 25.17% tax under the concessional regime against 35% plus surcharge and cess for a branch, no RBI approval in sectors under the automatic route, freedom to carry on any permitted business, and more credibility with Indian customers, banks and staff. Disadvantages: more compliance (board meetings, statutory audit, annual filings with the Registrar, FEMA reporting such as share allotment and the annual foreign liabilities return), at least two directors with one resident in India, tax withheld on dividends paid to the parent, transfer pricing on intra-group dealings, and a slower exit than closing a branch."),
        ("Is a subsidiary or a branch better for a foreign company in India?", "For most foreign companies planning to trade in India for more than a couple of years, a subsidiary: lower tax, no RBI approval in most sectors and wider freedom to operate. A branch suits limited activities the RBI allows, such as export-import or professional services for the parent, and keeps profits taxable at the higher rate. Compare the numbers with the branch vs subsidiary calculator linked on this page."),
          ("Can a liaison office earn income in India?", "No. A liaison office can only represent the parent and promote its business; its expenses are funded by the parent."),
          ("When does an employer of record make sense?", "For a few employees in India before you set up an entity, provided they do not sell or sign contracts for you in India."),
          ("Can a foreign company use an LLP in India?", "Yes, in sectors open to 100% foreign investment under the automatic route without performance conditions."),
          ("Does the chooser give a final answer?", "No. It is a starting point; sector rules, your home country and partners can change it, which we review on a call."),
          ("Can BQP set up the structure?", "Yes. " + CONTACT)],
    related=[("india-market-entry-foreign-company-guide.html", "India market entry guide"), ("branch-office-vs-liaison-vs-wos-india-foreign.html", "Liaison vs branch vs subsidiary"),
             ("permanent-establishment-risk-checker-india-foreign-company-2026.html", "PE risk checker")],
    cta_h="Choosing how to enter India?", cta_b=CONTACT,
    keywords="India entry structure foreign company, subsidiary vs branch vs liaison office India, best way to enter Indian market, employer of record vs subsidiary India, LLP for foreign company India, India market entry chooser",
    desc="India entry structure chooser for foreign companies (2026): five questions recommend contractors or distributor, employer of record, liaison, branch or project office, LLP or private limited subsidiary, with links to detailed guides and PE checks.",
    howto={"name": "How a foreign company chooses an India entry structure", "description": "From goal to structure.", "steps": [
        {"name": "Define the goal", "text": "Build, sell, test or execute a project."},
        {"name": "Check income and headcount", "text": "Will India earn income; how many people in 12 months."},
        {"name": "Check sector rules", "text": "Automatic route, caps, approvals, land-border owners."},
        {"name": "Pick the structure", "text": "Use the chooser and the detailed guides."},
        {"name": "Confirm and set up", "text": "Approvals, entity, bank account, tax and FEMA registrations."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch ED complete")
