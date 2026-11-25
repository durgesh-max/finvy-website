const assert = require("assert");
const { hraExemption } = require("./hra-exemption-logic.js");
let n = 0; function t(name, fn) { fn(); n++; }
t("metro, rent-limited", () => { const r = hraExemption({ basic: 600000, hra: 300000, rent: 240000, metro: "yes" }); assert.strictEqual(r.rentLess10, 180000); assert.strictEqual(r.exempt, 180000); assert.strictEqual(r.limit, "rent"); assert.strictEqual(r.taxable, 120000); });
t("non-metro 40% cap", () => { const r = hraExemption({ basic: 600000, hra: 300000, rent: 400000, metro: "no" }); assert.strictEqual(r.pctSalary, 240000); assert.strictEqual(r.exempt, 240000); assert.strictEqual(r.limit, "salary"); });
t("actual HRA lowest", () => { const r = hraExemption({ basic: 1000000, hra: 150000, rent: 500000, metro: "yes" }); assert.strictEqual(r.exempt, 150000); assert.strictEqual(r.limit, "actual"); });
t("DA and commission count as salary", () => { const r = hraExemption({ basic: 500000, da: 100000, commission: 0, hra: 300000, rent: 300000, metro: "yes" }); assert.strictEqual(r.salary, 600000); assert.strictEqual(r.exempt, 240000); });
t("rent below 10% gives nil", () => { const r = hraExemption({ basic: 600000, hra: 200000, rent: 50000, metro: "yes" }); assert.strictEqual(r.exempt, 0); });
t("new regime nil", () => { const r = hraExemption({ basic: 600000, hra: 300000, rent: 240000, metro: "yes", regime: "new" }); assert.strictEqual(r.exempt, 0); assert.strictEqual(r.taxable, 300000); });
t("rent needed for full exemption", () => { const r = hraExemption({ basic: 600000, hra: 300000, rent: 0, metro: "yes" }); assert.strictEqual(r.rentForFull, 360000); });
t("validation", () => { assert.strictEqual(hraExemption({}).ok, false); assert.strictEqual(hraExemption({ basic: 100, hra: -1 }).ok, false); });
console.log("all " + n + " tests passed");
