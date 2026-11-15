const assert = require("assert");
const { propertyCapitalGains: f, fyOf } = require("./property-capital-gains-logic.js");
let n = 0; function t(name, fn) { fn(); n++; }
t("fy", () => { assert.strictEqual(fyOf(new Date("2026-03-31T00:00:00Z")), 2025); assert.strictEqual(fyOf(new Date("2026-04-01T00:00:00Z")), 2026); });
t("resident 2010 buy, 2026 sale: indexed wins", () => {
  const r = f({ buyDate: "2010-06-01", saleDate: "2026-09-01", cost: 4000000, price: 16000000 });
  assert.strictEqual(r.longTerm, true); assert.strictEqual(r.taxA, 1560000);
  assert.strictEqual(r.indexedCost, 9197605); assert.strictEqual(r.taxB, 1414898); assert.strictEqual(r.best, "indexed");
});
t("NRI same: flat only", () => {
  const r = f({ buyDate: "2010-06-01", saleDate: "2026-09-01", cost: 4000000, price: 16000000, resident: false });
  assert.strictEqual(r.canIndex, false); assert.strictEqual(r.taxA, 1560000); assert.strictEqual(r.taxB, undefined);
});
t("pre-2001 uses 2001-02 base", () => {
  const r = f({ buyDate: "1995-05-10", saleDate: "2026-06-01", cost: 1000000, price: 10000000 });
  assert.strictEqual(r.pre2001, true); assert.strictEqual(r.indexedCost, 3840000);
});
t("bought after 23 July 2024: no indexation", () => {
  const r = f({ buyDate: "2024-08-01", saleDate: "2026-09-01", cost: 5000000, price: 6000000 });
  assert.strictEqual(r.canIndex, false); assert.strictEqual(r.taxA, 130000);
});
t("short term", () => { const r = f({ buyDate: "2025-01-01", saleDate: "2026-06-01", cost: 1, price: 2 }); assert.strictEqual(r.longTerm, false); });
t("54EC capped at 50 lakh", () => {
  const r = f({ buyDate: "2010-06-01", saleDate: "2026-09-01", cost: 4000000, price: 16000000, resident: false, bonds54EC: 9000000 });
  assert.strictEqual(r.taxA, 910000);
});
t("future sale year rejected", () => { assert.strictEqual(f({ buyDate: "2010-01-01", saleDate: "2027-05-01", cost: 1, price: 2 }).ok, false); });
console.log(n + " tests passed");
