const assert = require("assert");
const { buildNoticeReply, NOTICE_TYPES } = require("./notice-reply-logic.js");
let n = 0; function t(name, fn) { fn(); n++; }
const pts = [{ q: "Mismatch in interest income", a: "Interest of Rs 12,400 was offered under other sources", ann: "Bank interest certificate" }];
t("income tax 143(1) draft", () => { const r = buildNoticeReply({ type: "it1431", name: "Asha Rao", id: "abcde1234f", ref: "ITBA/123", date: "10-11-2026", year: "2026-27", points: pts }); assert.ok(r.ok); assert.ok(r.text.includes("PAN: ABCDE1234F")); assert.ok(r.text.includes("section 143(1)(a)")); assert.ok(r.text.includes("Annexure A")); assert.strictEqual(r.annexures, 1); });
t("GST DRC-01 uses GSTIN and DRC-06", () => { const r = buildNoticeReply({ type: "gstdrc01", name: "X Pvt Ltd", id: "24ABCDE1234F1Z5", year: "April 2024 - March 2025", points: pts }); assert.ok(r.ok); assert.ok(r.text.includes("GSTIN: 24ABCDE1234F1Z5")); assert.ok(r.text.includes("DRC-06")); assert.ok(r.text.includes("Tax period: April 2024")); });
t("invalid PAN rejected", () => { const r = buildNoticeReply({ type: "it1432", name: "A", id: "123", points: pts }); assert.strictEqual(r.ok, false); assert.ok(r.errors.some(e => e.includes("PAN"))); });
t("invalid GSTIN rejected", () => { const r = buildNoticeReply({ type: "gstasmt10", name: "A", id: "ABCDE1234F", points: pts }); assert.strictEqual(r.ok, false); assert.ok(r.errors.some(e => e.includes("GSTIN"))); });
t("needs a query point", () => { const r = buildNoticeReply({ type: "it1336", name: "A", id: "ABCDE1234F", points: [{ q: "x", a: "" }] }); assert.strictEqual(r.ok, false); });
t("no type", () => { assert.strictEqual(buildNoticeReply({}).ok, false); });
t("annexure letters skip points without annexure", () => { const r = buildNoticeReply({ type: "it1421", name: "A", id: "ABCDE1234F", points: [{ q: "q1", a: "a1" }, { q: "q2", a: "a2", ann: "Ledger" }] }); assert.ok(r.text.includes("(b) Query: q2")); assert.ok(r.text.includes("A - Ledger")); assert.strictEqual(r.annexures, 1); });
t("all ten types build", () => { Object.keys(NOTICE_TYPES).forEach(k => { const id = NOTICE_TYPES[k].tax === "it" ? "ABCDE1234F" : "27ABCDE1234F1Z5"; assert.ok(buildNoticeReply({ type: k, name: "A", id: id, points: pts }).ok, k); }); });
console.log("all " + n + " tests passed");
