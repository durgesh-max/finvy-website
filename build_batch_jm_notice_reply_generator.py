# -*- coding: utf-8 -*-
"""Batch JM (26 Nov 2026): free income tax / GST notice reply draft-letter generator (client-side, no AI, no data leaves the
browser). Lead magnet for sweep ac122 demand (26 Nov 2026), all 7 markets: "income tax notice reply ai tool / ai",
"income tax notice reply format in word / letter format in word pdf", "gst notice reply ai tool / ai", "gst notice reply
letter format word / pdf". User steer 26 Nov 2026: more call bookings / WhatsApp enquiries - every draft ends with a
'have a CA check this' WhatsApp block. Logic: tools/notice-reply-logic.js (node tools/notice-reply-logic.test.js, 8 tests).
Facts: site notice reply guides (no prescribed format, e-Proceedings, not editable after submission, DIN check under CBDT
Circular 19/2019); GST reply forms ASMT-11 (to ASMT-10), DRC-06 (to DRC-01), DRC-01A Part B, GSTR-3A (file returns)."""
import re, json
from urllib.parse import quote
from build_lib import page, write_page, DOMAIN
import advisory_lib as A
from advisory_lib import ul, call_box

A.UPDATED = "Last updated: 26 November 2026."
UPDATED = A.UPDATED

LOGIC = open("tools/notice-reply-logic.js", encoding="utf-8").read().replace(
    'if (typeof module !== "undefined") module.exports = { buildNoticeReply: buildNoticeReply, NOTICE_TYPES: NOTICE_TYPES };', "")
_lrs = open("lrs-tcs-calculator.html", encoding="utf-8").read()
CALC_CSS = re.sub(r"\.calc-hero[^\n]*\n", "", re.search(r"<style>(.*?)</style>", _lrs, re.S).group(1))
CALC_CSS += ("\n  .calc-embed .calc-main{padding:0;max-width:none}\n"
             "  .calc-embed select,.calc-embed input[type=text],.calc-embed textarea{width:100%;padding:10px;border-radius:8px;border:1px solid #ccc;font-size:15px;font-family:inherit;box-sizing:border-box}\n"
             "  .calc-embed textarea{min-height:64px;resize:vertical}\n"
             "  .calc-embed .qp{border-top:1px dashed #ddd;padding-top:10px;margin-top:6px}\n"
             "  .calc-embed pre.nr-out{white-space:pre-wrap;word-break:break-word;background:#fff;color:#1a1613;border-radius:8px;padding:14px;font:13px/1.55 ui-monospace,Menlo,Consolas,monospace;max-height:520px;overflow:auto}\n"
             "  .calc-embed .nr-btn{display:inline-block;margin:10px 8px 0 0;padding:10px 16px;border-radius:8px;border:0;font:600 14px Inter,sans-serif;cursor:pointer;text-decoration:none}\n"
             "  .calc-embed .nr-copy{background:#fff;color:#1a1613}\n  .calc-embed .nr-wa{background:#25D366;color:#fff}\n"
             "  .calc-embed .nr-err{margin:8px 0 0;padding-left:18px;font-size:13px}\n")


def sel(fid, label, hint, opts):
    o = "".join(f'<option value="{v}">{t}</option>' for v, t in opts)
    return f'<div class="field"><label for="{fid}">{label} <span class="hint">{hint}</span></label><select id="{fid}">{o}</select></div>'


def txt(fid, label, hint, ph=""):
    return f'<div class="field"><label for="{fid}">{label} <span class="hint">{hint}</span></label><input id="{fid}" type="text" placeholder="{ph}"/></div>'


def area(fid, label, hint, ph=""):
    return f'<div class="field"><label for="{fid}">{label} <span class="hint">{hint}</span></label><textarea id="{fid}" placeholder="{ph}"></textarea></div>'


TYPES = [("it1431", "Income tax: 143(1) proposed adjustment / intimation"), ("it1399", "Income tax: 139(9) defective return"),
         ("it1421", "Income tax: 142(1) notice"), ("it1432", "Income tax: 143(2) scrutiny notice"),
         ("it1336", "Income tax: 133(6) information request"), ("it148a", "Income tax: 148A show cause notice"),
         ("gstasmt10", "GST: ASMT-10 discrepancy (reply ASMT-11)"), ("gstdrc01a", "GST: DRC-01A intimation"),
         ("gstdrc01", "GST: DRC-01 show cause notice (reply DRC-06)"), ("gstr3a", "GST: GSTR-3A non-filing notice")]
QP = "".join(f'<div class="qp">{txt(f"nQ{i}", f"Query {i} from the notice", "Copy the wording from the notice." if i == 1 else "Optional.")}'
             f'{area(f"nA{i}", f"Your reply to query {i}", "Facts and figures only.")}'
             f'{txt(f"nX{i}", "Supporting document (annexure)", "Optional, e.g. bank interest certificate.")}</div>' for i in (1, 2, 3))
INPUTS = (sel("nType", "Notice type", "Pick the section or form named on the notice.", TYPES)
          + txt("nName", "Name", "As on the notice.") + txt("nId", "PAN or GSTIN", "PAN for income tax, GSTIN for GST.")
          + txt("nRef", "Notice DIN / reference number", "Optional.") + txt("nDate", "Notice date", "Optional, e.g. 10-11-2026.")
          + txt("nYear", "Assessment year / tax year or GST period", "Optional, e.g. 2026-27.") + QP)
WA_BASE = "https://wa.me/917801887130?text="
JS = LOGIC + r'''
(function(){
  function $(id){return document.getElementById(id);}
  var ids=["nType","nName","nId","nRef","nDate","nYear","nQ1","nA1","nX1","nQ2","nA2","nX2","nQ3","nA3","nX3"];
  function show(){
    var pts=[1,2,3].map(function(i){return {q:$("nQ"+i).value,a:$("nA"+i).value,ann:$("nX"+i).value};});
    var r=buildNoticeReply({type:$("nType").value,name:$("nName").value,id:$("nId").value,ref:$("nRef").value,date:$("nDate").value,year:$("nYear").value,points:pts});
    var out=$("nOut"), err=$("nErr"), wa=$("nWa");
    var label=$("nType").options[$("nType").selectedIndex].text;
    wa.href="''' + WA_BASE + r'''"+encodeURIComponent("Hi Durgesh, I have a notice ("+label+") and drafted a reply with your notice reply tool. Please check it before I submit. I will send the notice PDF and due date here.");
    if(!r.ok){ out.textContent="Fill in the fields on the left to build your draft."; err.innerHTML=r.errors.map(function(e){return "<li>"+e+"</li>";}).join(""); return; }
    err.innerHTML=""; out.textContent=r.text;
  }
  ids.forEach(function(id){$(id).addEventListener("input",show);$(id).addEventListener("change",show);});
  $("nCopy").addEventListener("click",function(){
    var t=$("nOut").textContent;
    if(navigator.clipboard){navigator.clipboard.writeText(t).then(function(){$("nCopy").textContent="Copied";setTimeout(function(){$("nCopy").textContent="Copy draft";},1500);});}
  });
  show();
})();'''
SLUG = "income-tax-gst-notice-reply-draft-letter-generator-free-tool-format-word"
app = {"@context": "https://schema.org", "@type": "WebApplication", "name": "Income Tax and GST Notice Reply Draft Letter Generator",
       "url": f"{DOMAIN}/{SLUG}.html", "applicationCategory": "BusinessApplication", "operatingSystem": "Any",
       "offers": {"@type": "Offer", "price": "0", "priceCurrency": "INR"},
       "description": "Free tool that builds a point-by-point draft reply letter for income tax notices (143(1), 139(9), 142(1), 143(2), 133(6), 148A) and GST notices (ASMT-10, DRC-01A, DRC-01, GSTR-3A) to copy into Word. Runs in the browser; nothing is uploaded.",
       "author": {"@type": "Person", "name": "CA Durgesh Chavda", "url": f"{DOMAIN}/durgesh.html"}}
CALC = (f"<style>{CALC_CSS}</style><script type=\"application/ld+json\">{json.dumps(app, separators=(',', ':'))}</script>"
        f'<div class="calc-embed"><div class="calc-main"><div class="calc-card"><h2>Your notice</h2><p class="sub">Nothing you type leaves your browser.</p>{INPUTS}</div>'
        '<div class="result-card"><div class="rlabel">Draft reply</div><ul class="nr-err" id="nErr"></ul><pre class="nr-out" id="nOut">-</pre>'
        '<button type="button" class="nr-btn nr-copy" id="nCopy">Copy draft</button>'
        f'<a class="nr-btn nr-wa" id="nWa" href="{WA_BASE}{quote("Hi Durgesh, I have a tax notice and want my reply checked.")}" target="_blank" rel="noopener">Have a CA check it on WhatsApp</a>'
        '<p style="font-size:13px;margin:12px 0 0">A reply cannot be edited once submitted. Before you upload it, have it checked against the notice, your return and the documents.</p></div></div></div>'
        f"<script>{JS}\n</script>")
CONTACT = ("WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with the notice PDF, your PAN or GSTIN, the period and the reply date. "
           "We read the notice and reply the same working day with a written scope to check or prepare your reply.")

PAGES = [dict(
    slug=SLUG,
    title="Income Tax and GST Notice Reply Generator (Free): Draft Letter Format to Copy into Word for 143(1), 142(1), 143(2), 133(6), ASMT-10 and DRC-01",
    em="a clean draft in minutes, checked by a CA before it goes in.",
    kicker="/ Free tool &middot; Income tax and GST notices &middot; Runs in your browser &middot; Updated 2026-11-26",
    lead=("<strong>Pick the notice type, enter your name, PAN or GSTIN and each query with your reply, and the tool builds a point-by-point draft letter you can copy into Word, save as PDF and upload.</strong> "
          "It covers income tax notices under sections 143(1), 139(9), 142(1), 143(2), 133(6) and 148A, and GST notices in ASMT-10, DRC-01A, DRC-01 and GSTR-3A. "
          "Nothing you type is uploaded. A reply cannot be edited once submitted, so have it checked before you file it."),
    sections=[
        ("/ Notice reply generator", "Build your draft reply.", CALC
         + call_box("my notice reply", ["Reading the notice and the section",
                                       "Reconciling figures with your return, Form 168 (old 26AS), AIS or GSTR-2B",
                                       "Drafting and filing the reply on the portal",
                                       "Adjournment requests and hearings",
                                       "Appeals if an order goes against you"],
                    "the notice PDF and the due date.")),
        ("/ How to use the draft", "From draft to submission.",
         ul("<strong>Quote the notice exactly:</strong> section or form, DIN or reference number, date and year, so the reply is matched to the right proceeding.",
            "<strong>Answer every query:</strong> one point per query, with figures that match your return and books.",
            "<strong>Attach evidence:</strong> each annexure the draft lists should be a clear PDF: bank certificates, ledgers, invoices, reconciliations.",
            "<strong>Submit online:</strong> income tax replies go through e-Proceedings on the e-filing portal; GST replies are filed on the GST portal in the form the notice names (ASMT-11, DRC-06 and so on).",
            "<strong>Check before you submit:</strong> a submitted reply stays on record. If you need more time, ask for an adjournment before the due date.")
         + '<p>Guides: <a href="income-tax-notice-reply-letter-format-sample-how-to-submit-e-proceedings-2026.html">income tax notice reply format</a> &middot; <a href="how-to-respond-to-income-tax-notice-india.html">responding to an income tax notice</a> &middot; <a href="gst-notice-response-india-asmt-drc-gstr.html">GST notice reply</a>.</p>'
         f'<p><strong>Sources:</strong> site income tax and GST notice guides; CBDT Circular 19/2019 (DIN); CGST Rules forms ASMT-10 / ASMT-11, DRC-01A, DRC-01 / DRC-06 and GSTR-3A. <em>{UPDATED}</em> A drafting aid, not advice for your situation.</p>'),
    ],
    faqs=[("Is there a free tool to draft an income tax notice reply?", "Yes. The generator on this page builds a point-by-point draft for income tax notices under sections 143(1), 139(9), 142(1), 143(2), 133(6) and 148A, which you can copy into Word and save as a PDF."),
          ("Can it draft a GST notice reply?", "Yes, for ASMT-10 (reply in ASMT-11), DRC-01A, DRC-01 (reply in DRC-06) and GSTR-3A notices. The figures still need to match your returns and books."),
          ("Is this an AI tool?", "No. It is a template builder that runs in your browser, so nothing you type is uploaded. It gives you a clean structure; the content of each reply has to come from your facts and documents."),
          ("Is there a prescribed format for a notice reply?", "No. A clear letter that quotes the notice, answers each query and lists the annexures is enough. Income tax replies go through e-Proceedings; GST replies use the form the notice names."),
          ("Should a CA check the draft?", "It is safer. A submitted reply cannot be edited, and a wrong admission or missed point can lead to an adjustment, demand or penalty. " + CONTACT)],
    related=[("income-tax-notice-reply-letter-format-sample-how-to-submit-e-proceedings-2026.html", "Income tax notice reply format"),
             ("how-to-respond-to-income-tax-notice-india.html", "Responding to an income tax notice"),
             ("gst-notice-response-india-asmt-drc-gstr.html", "GST notice reply")],
    cta_h="Got a notice?", cta_b=CONTACT,
    keywords="income tax notice reply generator, income tax notice reply ai tool, income tax notice reply format in word, gst notice reply ai tool, gst notice reply format, notice reply letter format, reply to income tax notice online, asmt-10 reply format, drc-01 reply format",
    desc="Free income tax and GST notice reply generator: build a point-by-point draft letter for 143(1), 139(9), 142(1), 143(2), 133(6), 148A, ASMT-10, DRC-01A, DRC-01 and GSTR-3A notices, copy it into Word, and have a CA check it before you submit.",
    howto={"name": "How to draft a notice reply with the generator", "description": "Free, in the browser.", "steps": [
        {"name": "Pick the notice type", "text": "Section or GST form named on the notice."},
        {"name": "Enter your details", "text": "Name, PAN or GSTIN, DIN / reference, date and year."},
        {"name": "Add each query and reply", "text": "One point per query, with the supporting document."},
        {"name": "Copy the draft", "text": "Paste into Word, finalise and save as PDF."},
        {"name": "Get it checked and submit", "text": "Upload on e-Proceedings or the GST portal before the due date."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch JM complete")
