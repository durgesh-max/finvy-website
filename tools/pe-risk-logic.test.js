const assert = require("assert");
const { peRisk, PE_QUESTIONS } = require("./pe-risk-logic.js");
let n = 0; function t(name, fn) { fn(); n++; }
t("no answers is low", () => { const r = peRisk({}); assert.strictEqual(r.band, "low"); assert.strictEqual(r.topType, null); });
t("office alone is high fixed place", () => { const r = peRisk({ office: true }); assert.strictEqual(r.band, "high"); assert.strictEqual(r.topType, "Fixed place PE"); });
t("exclusive agent alone is medium", () => { const r = peRisk({ agentExclusive: true }); assert.strictEqual(r.band, "medium"); });
t("contracts plus agent is dependent agent high", () => { const r = peRisk({ contracts: true, agentExclusive: true }); assert.strictEqual(r.topType, "Dependent agent PE"); assert.strictEqual(r.band, "high"); });
t("digital plus no treaty is medium (total 3, top 2)", () => { const r = peRisk({ digital: true, noTreaty: true }); assert.strictEqual(r.total, 3); assert.strictEqual(r.band, "medium"); });
t("eight questions", () => { assert.strictEqual(PE_QUESTIONS.length, 8); });
console.log("all " + n + " tests passed");
