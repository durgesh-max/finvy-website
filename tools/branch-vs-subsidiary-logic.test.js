const assert = require("assert");
const { branchVsSubsidiary } = require("./branch-vs-subsidiary-logic.js");
let n = 0; function t(name, fn) { fn(); n++; }
t("small branch no surcharge", () => { const r = branchVsSubsidiary({ profit: 5000000, country: "usa" }); assert.strictEqual(r.branchTax, 1820000); assert.strictEqual(r.corpTax, 1258400); });
t("US parent full payout", () => { const r = branchVsSubsidiary({ profit: 5000000, country: "usa" }); assert.strictEqual(r.dividend, 3741600); assert.strictEqual(r.wht, 561240); assert.strictEqual(r.subTax, 1819640); });
t("surcharge tiers", () => { assert.strictEqual(branchVsSubsidiary({ profit: 50000000, country: "uk" }).branchTax, 18564000); assert.strictEqual(branchVsSubsidiary({ profit: 200000000, country: "uk" }).branchTax, 76440000); });
t("no treaty 20% plus cess", () => { const r = branchVsSubsidiary({ profit: 5000000, country: "none" }); assert.ok(Math.abs(r.whtRate - 0.208) < 1e-9); });
t("zero payout", () => { const r = branchVsSubsidiary({ profit: 5000000, country: "singapore", payout: 0 }); assert.strictEqual(r.wht, 0); assert.strictEqual(r.subTax, 1258400); });
t("validation", () => { assert.strictEqual(branchVsSubsidiary({ profit: 0, country: "usa" }).ok, false); assert.strictEqual(branchVsSubsidiary({ profit: 10, country: "mars" }).ok, false); });
console.log("all " + n + " tests passed");
