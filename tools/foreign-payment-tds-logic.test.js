const assert = require("assert");
const { foreignPaymentTds } = require("./foreign-payment-tds-logic.js");
let n = 0; function t(name, fn) { fn(); n++; }
t("domestic rate tiers", () => {
  assert.ok(Math.abs(foreignPaymentTds({ amount: 1000000, type: "fts", country: "none" }).rate - 0.208) < 1e-9);
  assert.ok(Math.abs(foreignPaymentTds({ amount: 50000000, type: "fts", country: "none" }).rate - 0.21216) < 1e-9);
  assert.ok(Math.abs(foreignPaymentTds({ amount: 200000000, type: "fts", country: "none" }).rate - 0.2184) < 1e-9);
});
t("US FTS with TRC uses treaty 15%", () => { const r = foreignPaymentTds({ amount: 1000000, type: "fts", country: "usa" }); assert.strictEqual(r.basis, "treaty"); assert.strictEqual(r.tds, 150000); assert.strictEqual(r.net, 850000); assert.strictEqual(r.saving, 58000); });
t("no TRC means domestic rate", () => { const r = foreignPaymentTds({ amount: 1000000, type: "royalty", country: "singapore", trc: "no" }); assert.strictEqual(r.basis, "domestic"); assert.strictEqual(r.tds, 208000); });
t("Singapore royalty 10%", () => { assert.strictEqual(foreignPaymentTds({ amount: 2000000, type: "royalty", country: "singapore" }).tds, 200000); });
t("UAE FTS has no article", () => { const r = foreignPaymentTds({ amount: 1000000, type: "fts", country: "uae" }); assert.strictEqual(r.basis, "no-article"); assert.strictEqual(r.tds, 0); assert.strictEqual(r.noArticle, true); });
t("UAE interest 12.5% and Mauritius interest 7.5%", () => { assert.strictEqual(foreignPaymentTds({ amount: 1000000, type: "interest", country: "uae" }).tds, 125000); assert.strictEqual(foreignPaymentTds({ amount: 1000000, type: "interest", country: "mauritius" }).tds, 75000); });
t("gross-up", () => { const r = foreignPaymentTds({ amount: 900000, type: "royalty", country: "germany", grossUp: "yes" }); assert.strictEqual(r.gross, 1000000); assert.strictEqual(r.tds, 100000); assert.strictEqual(r.net, 900000); });
t("validation", () => { assert.strictEqual(foreignPaymentTds({ amount: 0, type: "fts", country: "usa" }).ok, false); assert.strictEqual(foreignPaymentTds({ amount: 5, type: "rent", country: "usa" }).ok, false); });
console.log("all " + n + " tests passed");
