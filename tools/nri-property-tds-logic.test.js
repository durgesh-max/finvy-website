const assert = require("assert");
const { nriPropertyTds, nriSurcharge } = require("./nri-property-tds-logic.js");
let n = 0;
function t(name, fn) { fn(); n++; }

t("surcharge bands", () => {
  assert.strictEqual(nriSurcharge(5000000), 0);
  assert.strictEqual(nriSurcharge(5000001), 0.10);
  assert.strictEqual(nriSurcharge(10000000), 0.10);
  assert.strictEqual(nriSurcharge(10000001), 0.15);
});
t("1.2 crore sale, 60 lakh cost", () => {
  const r = nriPropertyTds({ price: 12000000, cost: 6000000 });
  assert.strictEqual(r.tdsFull, 1794000);   // 1.2cr x 12.5% x 1.15 x 1.04
  assert.strictEqual(r.tax, 858000);        // 60L x 12.5% x 1.10 x 1.04
  assert.strictEqual(r.excess, 936000);
  assert.strictEqual(r.gain, 6000000);
});
t("40 lakh sale, 30 lakh cost", () => {
  const r = nriPropertyTds({ price: 4000000, cost: 3000000 });
  assert.strictEqual(r.tdsFull, 520000);
  assert.strictEqual(r.tax, 130000);
  assert.strictEqual(r.excess, 390000);
});
t("loss: no tax, all TDS is excess", () => {
  const r = nriPropertyTds({ price: 5000000, cost: 6000000 });
  assert.strictEqual(r.gain, 0);
  assert.strictEqual(r.tax, 0);
  assert.strictEqual(r.excess, r.tdsFull);
  assert.strictEqual(r.tdsFull, 650000);
});
t("short-term returns 30% TDS note", () => {
  const r = nriPropertyTds({ price: 5000000, cost: 4000000, longTerm: false });
  assert.strictEqual(r.longTerm, false);
  assert.strictEqual(r.tdsRate, 0.30);
});
t("validation", () => {
  assert.strictEqual(nriPropertyTds({ price: 0 }).ok, false);
  assert.strictEqual(nriPropertyTds({ price: 100, cost: -1 }).ok, false);
});
console.log(n + " tests passed");
