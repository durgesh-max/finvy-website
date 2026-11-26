/* Notice reply draft-letter builder (income tax and GST notices). Builds a plain-text draft that can be pasted into Word
   and uploaded as a PDF on e-Proceedings (income tax) or the GST portal. It is a drafting aid, not advice: the reply must
   match the notice, the return and the evidence. No data leaves the browser. */
var NOTICE_TYPES = {
  it1431: { tax: "it", label: "Income tax: proposed adjustment / intimation under section 143(1)", to: "The Centralised Processing Centre, Income Tax Department", subj: "Response to the proposed adjustment under section 143(1)(a)", close: "I request that the proposed adjustment be dropped and the return be processed as filed." },
  it1399: { tax: "it", label: "Income tax: defective return notice under section 139(9)", to: "The Centralised Processing Centre, Income Tax Department", subj: "Response to the defective return notice under section 139(9)", close: "I request that the defect be treated as removed and the return be processed." },
  it1421: { tax: "it", label: "Income tax: notice under section 142(1)", to: "The Assessing Officer / National Faceless Assessment Centre", subj: "Reply to the notice under section 142(1)", close: "I request that the above be taken on record and that I be given an opportunity of being heard before any adverse view is taken." },
  it1432: { tax: "it", label: "Income tax: scrutiny notice under section 143(2)", to: "The Assessing Officer / National Faceless Assessment Centre", subj: "Reply to the notice under section 143(2)", close: "I request that the above be considered and the assessment be completed accepting the returned income, and that I be given an opportunity of being heard by video conference before any adverse view is taken." },
  it1336: { tax: "it", label: "Income tax: request for information under section 133(6)", to: "The Income Tax Officer", subj: "Reply to the notice under section 133(6)", close: "I request that the information be taken on record." },
  it148a: { tax: "it", label: "Income tax: show cause notice under section 148A", to: "The Assessing Officer", subj: "Reply to the show cause notice under section 148A", close: "I request that no order be passed for reopening the assessment, as the conditions for it are not met, and that I be given an opportunity of being heard." },
  gstasmt10: { tax: "gst", label: "GST: notice of discrepancy in ASMT-10 (reply in ASMT-11)", to: "The Proper Officer, GST Department", subj: "Reply in Form GST ASMT-11 to the notice in Form GST ASMT-10", close: "I request that the discrepancies be treated as explained and the proceedings be dropped." },
  gstdrc01a: { tax: "gst", label: "GST: intimation in DRC-01A before a show cause notice", to: "The Proper Officer, GST Department", subj: "Reply to the intimation in Form GST DRC-01A", close: "I request that no show cause notice be issued, as the proposed liability is not payable for the reasons above." },
  gstdrc01: { tax: "gst", label: "GST: show cause notice in DRC-01 (reply in DRC-06)", to: "The Proper Officer, GST Department", subj: "Reply in Form GST DRC-06 to the show cause notice in Form GST DRC-01", close: "I request that the proposed demand, interest and penalty be dropped, and that I be given a personal hearing before any order is passed." },
  gstr3a: { tax: "gst", label: "GST: notice for non-filing of returns in GSTR-3A", to: "The Proper Officer, GST Department", subj: "Response to the notice in Form GSTR-3A", close: "I request that the notice be treated as complied with, as the pending returns have now been filed." }
};

function buildNoticeReply(input) {
  input = input || {};
  var t = NOTICE_TYPES[input.type];
  var errors = [];
  if (!t) errors.push("Choose the notice type.");
  var name = String(input.name || "").trim(), id = String(input.id || "").trim().toUpperCase();
  if (!name) errors.push("Enter the name as it appears on the notice.");
  if (t && t.tax === "it" && !/^[A-Z]{5}[0-9]{4}[A-Z]$/.test(id)) errors.push("Enter a valid 10-character PAN.");
  if (t && t.tax === "gst" && !/^[0-9]{2}[A-Z0-9]{13}$/.test(id)) errors.push("Enter a valid 15-character GSTIN.");
  var pts = (input.points || []).filter(function (p) { return p && String(p.q || "").trim() && String(p.a || "").trim(); });
  if (!pts.length) errors.push("Enter at least one query from the notice with your reply.");
  if (errors.length) return { ok: false, errors: errors };
  var idLabel = t.tax === "it" ? "PAN" : "GSTIN";
  var yrLabel = t.tax === "it" ? "Assessment year / tax year" : "Tax period";
  var refLabel = t.tax === "it" ? "Notice DIN" : "Notice reference number";
  var L = [];
  L.push("To,");
  L.push(t.to);
  L.push("");
  L.push("Subject: " + t.subj + (input.year ? " for " + yrLabel.toLowerCase() + " " + String(input.year).trim() : ""));
  L.push("");
  L.push("Name: " + name);
  L.push(idLabel + ": " + id);
  if (input.ref) L.push(refLabel + ": " + String(input.ref).trim());
  if (input.date) L.push("Notice dated: " + String(input.date).trim());
  if (input.year) L.push(yrLabel + ": " + String(input.year).trim());
  L.push("");
  L.push("Respected Sir / Madam,");
  L.push("");
  L.push("1. With reference to the above notice, I submit my reply point by point below.");
  L.push("");
  var letters = "abcdefghij", ann = [];
  pts.forEach(function (p, i) {
    var a = String(p.ann || "").trim();
    L.push("(" + letters[i] + ") Query: " + String(p.q).trim());
    L.push("    Reply: " + String(p.a).trim() + (a ? " (Annexure " + String.fromCharCode(65 + ann.length) + ")" : ""));
    if (a) ann.push(String.fromCharCode(65 + ann.length) + " - " + a);
    L.push("");
  });
  L.push("2. " + t.close);
  L.push("");
  if (ann.length) { L.push("Annexures:"); ann.forEach(function (x) { L.push(x); }); L.push(""); }
  L.push("I declare that the information given above is true and correct to the best of my knowledge.");
  L.push("");
  L.push("Place: ____________");
  L.push("Date: ____________");
  L.push("");
  L.push(name);
  L.push("(Signature)");
  return { ok: true, tax: t.tax, label: t.label, text: L.join("\n"), annexures: ann.length, points: pts.length };
}
if (typeof module !== "undefined") module.exports = { buildNoticeReply: buildNoticeReply, NOTICE_TYPES: NOTICE_TYPES };
