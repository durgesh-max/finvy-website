const assert = require("assert");
const { freelancerTax, flSlabTax } = require("./freelancer-tax-logic.js");
let n = 0; function t(name, fn) { fn(); n++; }
t("new regime slab", () => { assert.strictEqual(flSlabTax(1000000, "new"), 40000); });
t("old regime senior slabs", () => { assert.strictEqual(flSlabTax(600000, "old", "60"), 30000); assert.strictEqual(flSlabTax(600000, "old", "80"), 20000); });
t("44ADA 24 lakh receipts -> 12 lakh profit, nil tax (87A)", () => { const r = freelancerTax({ receipts: 2400000 }); assert.strictEqual(r.profit, 1200000); assert.strictEqual(r.tax, 0); });
t("marginal relief just above 12 lakh", () => { const r = freelancerTax({ receipts: 2420000 }); assert.strictEqual(r.taxableIncome, 1210000); assert.strictEqual(r.tax, Math.round(10000 * 1.04)); });
t("44ADA 40 lakh receipts new regime", () => { const r = freelancerTax({ receipts: 4000000 }); assert.strictEqual(r.slabTax, 200000); assert.strictEqual(r.tax, 208000); assert.strictEqual(r.advance, "single"); });
t("limit falls to 50 lakh with high cash", () => { const r = freelancerTax({ receipts: 6000000, lowCash: "no", expenses: 2000000 }); assert.strictEqual(r.method, "actual"); assert.strictEqual(r.profit, 4000000); assert.strictEqual(r.advance, "four"); });
t("75 lakh allowed with low cash", () => { const r = freelancerTax({ receipts: 7500000 }); assert.strictEqual(r.method, "44ada"); assert.strictEqual(r.profit, 3750000); });
t("old regime rebate up to 5 lakh", () => { const r = freelancerTax({ receipts: 1000000, regime: "old" }); assert.strictEqual(r.tax, 0); });
t("tds refund", () => { const r = freelancerTax({ receipts: 2000000, tds: 200000 }); assert.strictEqual(r.tax, 0); assert.strictEqual(r.refund, 200000); });
t("validation", () => { assert.strictEqual(freelancerTax({}).ok, false); assert.strictEqual(freelancerTax({ receipts: 100, pct: 40 }).ok, false); });
console.log("all " + n + " tests passed");
