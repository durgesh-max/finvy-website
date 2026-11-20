const assert = require("assert");
const { nroInterestRefund, nroSlabTax } = require("./nro-interest-refund-logic.js");
let n = 0;
function t(name, fn) { fn(); n++; }
t("slab tax bands with cess", () => {
  assert.strictEqual(Math.round(nroSlabTax(400000)), 0);
  assert.strictEqual(Math.round(nroSlabTax(500000)), 5200);        // 1L x 5% x 1.04
  assert.strictEqual(Math.round(nroSlabTax(1200000)), 62400);      // (20k+40k) x 1.04
  assert.strictEqual(Math.round(nroSlabTax(3000000)), 499200);     // 480k x 1.04
});
t("UAE resident, 5 lakh interest, no other income, TRC", () => {
  const r = nroInterestRefund({ interest: 500000, other: 0, country: "uae", trc: true });
  assert.strictEqual(r.tds, 156000);
  assert.strictEqual(r.treatyTax, 62500);
  assert.strictEqual(r.slabTax, 5200);
  assert.strictEqual(r.actual, 5200);
  assert.strictEqual(r.basis, "slab");
  assert.strictEqual(r.refund, 150800);
});
t("US resident with large other income uses treaty 15%", () => {
  const r = nroInterestRefund({ interest: 1000000, other: 3000000, country: "usa", trc: true });
  assert.strictEqual(r.treatyTax, 150000);
  assert.strictEqual(r.slabTax, 312000);   // 10L at 30% x 1.04
  assert.strictEqual(r.actual, 150000);
  assert.strictEqual(r.basis, "treaty");
  assert.strictEqual(r.refund, 312000 - 150000);
});
t("no TRC falls back to slab", () => {
  const r = nroInterestRefund({ interest: 200000, other: 0, country: "uk", trc: false });
  assert.strictEqual(r.treatyTax, null);
  assert.strictEqual(r.slabTax, 0);
  assert.strictEqual(r.refund, 62400);
});
t("validation", () => {
  assert.strictEqual(nroInterestRefund({ interest: 0 }).ok, false);
});
console.log("all " + n + " tests passed");
