// node tools/fema-lsf-logic.test.js
var assert = require("assert");
var L = require("./fema-lsf-logic.js");
var f = L.femaLsf, n = 0;
function t(name, fn) { fn(); n++; }

t("FC-GPR, INR 1 crore, 5 months late: 7,500 + 0.025% x 1cr x 0.42 = 8,550 -> 8,600", function () {
  var r = f({ form: "fcgpr", amount: 10000000, due: "2026-06-10", filed: "2026-11-05" });
  assert.strictEqual(r.months, 5); assert.strictEqual(r.n, 0.42); assert.strictEqual(r.fee, 8600); assert.strictEqual(r.available, true);
});
t("part month rounds up: due 10 June, filed 21 November = 6 months, n 0.5", function () {
  var r = f({ form: "fctrs", amount: 50000000, due: "2026-06-10", filed: "2026-11-21" });
  assert.strictEqual(r.months, 6); assert.strictEqual(r.n, 0.5); assert.strictEqual(r.fee, 13800); // 7,500 + 6,250 = 13,750 -> 13,800
});
t("one day late counts as one month", function () {
  var r = f({ form: "fcgpr", amount: 1000000, due: "2026-11-20", filed: "2026-11-21" });
  assert.strictEqual(r.months, 1); assert.strictEqual(r.n, 0.08); assert.strictEqual(r.fee, 7600); // 7,500 + 20 = 7,520 -> 7,600
});
t("flat fee for FLA return whatever the delay", function () {
  var r = f({ form: "fla", amount: 0, due: "2026-07-15", filed: "2026-11-21" });
  assert.strictEqual(r.fee, 7500); assert.strictEqual(r.flow, false);
});
t("cap at 100% of the amount, rounded up to 100", function () {
  var r = f({ form: "fcgpr", amount: 5050, due: "2026-01-10", filed: "2026-11-21" });
  assert.strictEqual(r.capped, true); assert.strictEqual(r.fee, 5100);
});
t("more than three years late: LSF not available", function () {
  var r = f({ form: "fcgpr", amount: 10000000, due: "2023-11-20", filed: "2026-11-21" });
  assert.strictEqual(r.late, true); assert.strictEqual(r.available, false); assert.strictEqual(r.fee, undefined);
});
t("exactly three years late is still within the window", function () {
  var r = f({ form: "fcgpr", amount: 10000000, due: "2023-11-21", filed: "2026-11-21" });
  assert.strictEqual(r.available, true); assert.strictEqual(r.months, 36); assert.strictEqual(r.n, 3); assert.strictEqual(r.fee, 15000);
});
t("not late", function () {
  var r = f({ form: "fcgpr", amount: 10000000, due: "2026-11-30", filed: "2026-11-21" });
  assert.strictEqual(r.ok, true); assert.strictEqual(r.late, false);
});
t("validation", function () {
  assert.strictEqual(f({ form: "fcgpr", amount: 0, due: "2026-01-01", filed: "2026-02-01" }).ok, false);
  assert.strictEqual(f({ form: "x", amount: 1, due: "2026-01-01", filed: "2026-02-01" }).ok, false);
  assert.strictEqual(f({ form: "fcgpr", amount: 1, due: "2026-02-30", filed: "2026-03-01" }).ok, false);
});
console.log(n + " tests passed");
