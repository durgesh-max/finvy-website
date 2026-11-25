const assert = require("assert");
const { nriIncomeTax, nriSlabTax } = require("./nri-income-tax-logic.js");
let n = 0; function t(name, fn) { fn(); n++; }
t("new regime slab", () => { assert.strictEqual(nriSlabTax(1000000, "new"), 40000); });
t("old regime slab", () => { assert.strictEqual(nriSlabTax(1000000, "old"), 112500); });
t("no 87A: 10 lakh slab income pays tax", () => { const r = nriIncomeTax({ slab: 1000000 }); assert.strictEqual(r.tax, 41600); });
t("old regime deductions", () => { const r = nriIncomeTax({ slab: 1000000, regime: "old", deductions: 150000 }); assert.strictEqual(r.slabTax, 82500); });
t("equity gains", () => { const r = nriIncomeTax({ stcg: 100000, ltcgEq: 225000 }); assert.strictEqual(r.cgTax, 32500); assert.strictEqual(r.tax, 33800); });
t("surcharge capped at 15% on gains", () => { const r = nriIncomeTax({ slab: 30000000, ltcgOther: 1000000 }); assert.strictEqual(r.surcharge, Math.round(nriSlabTax(30000000, "new") * 0.25 + 125000 * 0.15)); });
t("refund vs tds", () => { const r = nriIncomeTax({ slab: 600000, tds: 187200 }); assert.strictEqual(r.tax, 10400); assert.strictEqual(r.refund, 176800); });
t("validation", () => { assert.strictEqual(nriIncomeTax({}).ok, false); assert.strictEqual(nriIncomeTax({ slab: -1 }).ok, false); });
console.log("all " + n + " tests passed");
