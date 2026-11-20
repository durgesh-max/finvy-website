const assert = require("assert");
const { nriRentRefund, rentSlabTax } = require("./nri-rent-refund-logic.js");
let n = 0; function t(name, fn) { fn(); n++; }
t("slab", () => { assert.strictEqual(Math.round(rentSlabTax(420000)), 1040); });
t("6 lakh rent, nothing else", () => { const r = nriRentRefund({ rent: 600000 }); assert.strictEqual(r.tds, 187200); assert.strictEqual(r.houseProperty, 420000); assert.strictEqual(r.tax, 1040); assert.strictEqual(r.refund, 186160); });
t("municipal tax and interest reduce income", () => { const r = nriRentRefund({ rent: 1200000, municipal: 20000, interest: 300000 }); assert.strictEqual(r.houseProperty, 526000); });
t("loss not set off", () => { const r = nriRentRefund({ rent: 300000, interest: 400000, other: 1000000 }); assert.strictEqual(r.houseProperty, 0); assert.strictEqual(r.tax, 0); });
t("validation", () => { assert.strictEqual(nriRentRefund({ rent: 0 }).ok, false); });
console.log("all " + n + " tests passed");
