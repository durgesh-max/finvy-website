const assert = require("assert");
const { indiaEntry } = require("./india-entry-chooser-logic.js");
let n = 0; function t(name, fn) { fn(); n++; }
const base = { goal: "build", revenue: "yes", staff: "6+", sector: "open", duration: "long" };
t("build long-term = subsidiary", () => { assert.strictEqual(indiaEntry(base).primary, "Private limited subsidiary"); });
t("project = project office", () => { assert.strictEqual(indiaEntry({ ...base, goal: "project" }).primary, "Project office"); });
t("test, no revenue, no staff", () => { assert.strictEqual(indiaEntry({ ...base, goal: "test", revenue: "no", staff: "0" }).primary, "Contractors or distributor, no entity yet"); });
t("test, no revenue, few staff = EOR", () => { assert.strictEqual(indiaEntry({ ...base, goal: "test", revenue: "no", staff: "1-5" }).primary, "Employer of record"); });
t("restricted sector", () => { assert.ok(indiaEntry({ ...base, sector: "restricted" }).primary.indexOf("approval") > 0); });
t("sell with no staff = distributor", () => { assert.strictEqual(indiaEntry({ ...base, goal: "sell", staff: "0" }).primary, "Distributor or licensee, then a subsidiary"); });
t("few staff short term = EOR", () => { assert.strictEqual(indiaEntry({ ...base, staff: "1-5", duration: "short" }).primary, "Employer of record"); });
t("validation", () => { assert.strictEqual(indiaEntry({}).ok, false); });
console.log("all " + n + " tests passed");
