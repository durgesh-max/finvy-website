const assert = require("assert");
const { femaHealth, FEMA_CHECKS } = require("./fema-health-logic.js");
let n = 0; function t(name, fn) { fn(); n++; }
t("unanswered", () => { assert.strictEqual(femaHealth({}).status, "unanswered"); });
t("all yes is clean", () => { const a = {}; FEMA_CHECKS.forEach(c => a[c.id] = "yes"); assert.strictEqual(femaHealth(a).status, "clean"); });
t("late FC-GPR only is fixable", () => { const r = femaHealth({ fcgpr: "no", fla: "yes" }); assert.strictEqual(r.status, "fixable"); assert.strictEqual(r.count, 1); });
t("no valuation is serious", () => { assert.strictEqual(femaHealth({ valuation: "no" }).status, "serious"); });
t("na ignored", () => { const r = femaHealth({ di: "na", ecb: "na", fcgpr: "yes" }); assert.strictEqual(r.status, "clean"); assert.strictEqual(r.answered, 1); });
t("eight checks", () => { assert.strictEqual(FEMA_CHECKS.length, 8); });
console.log("all " + n + " tests passed");
