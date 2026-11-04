// Run: node tools/fastds-eligibility-logic.test.js   (expected results worked out from Finance Act 2026, ss.131-140)
const { fastds } = require("./fastds-eligibility-logic.js");
const assert = require("assert");
const base = { kind: "asset", residentThen: true, residentSince: true, source: "taxedIndia", reportedFA: false, incomeReported: true, value: 2000000, otherCat1: 0, pmla: false, bmaDone: false };
let n = 0;
const T = (o, exp, msg, amt) => { const r = fastds(Object.assign({}, base, o)); const got = r.ok ? r.result : "ERROR"; assert.strictEqual(got, exp, msg + " -> " + got); if (amt !== undefined) assert.strictEqual(r.amount, amt, msg + " amount"); n++; };

// Category 2(b): bought from income taxed in India (e.g. RSUs taxed through Indian payroll), not in Schedule FA
T({}, "CAT2", "RSU shares from taxed salary, missing from Schedule FA", 100000);
T({ value: 50000000 }, "CAT2", "exactly INR 5 crore", 100000);
T({ value: 50000001 }, "NOT_ELIGIBLE", "above INR 5 crore");
T({ incomeReported: false }, "CAT2", "Cat 2 asset with unreported dividends (dividends go to Cat 1)", 100000);
// Category 2(a): bought while NR from foreign income, became resident, not in Schedule FA
T({ residentThen: false, residentSince: true, source: "foreignWhileNR" }, "CAT2", "returning NRI 401(k) not in Schedule FA", 100000);
T({ residentThen: false, residentSince: false, source: "foreignWhileNR" }, "NOT_NEEDED", "still NR, never resident since");
// Disclosed properly
T({ reportedFA: true, incomeReported: true }, "NOT_NEEDED", "disclosed in Schedule FA, income taxed");
T({ reportedFA: true, incomeReported: false }, "INCOME_ONLY", "disclosed asset, unreported interest");
// Category 1: untaxed source
T({ source: "untaxed", value: 4000000 }, "CAT1", "untaxed foreign account", 2400000);
T({ source: "untaxed", value: 10000000 }, "CAT1", "exactly INR 1 crore", 6000000);
T({ source: "untaxed", value: 10000001 }, "NOT_ELIGIBLE", "above INR 1 crore");
T({ source: "untaxed", value: 6000000, otherCat1: 4000001 }, "NOT_ELIGIBLE", "aggregate above INR 1 crore");
T({ source: "untaxed", value: 6000000, otherCat1: 4000000 }, "CAT1", "aggregate exactly INR 1 crore", 3600000);
T({ source: "untaxed", reportedFA: true, incomeReported: true }, "CAT1", "untaxed source even though listed in Schedule FA", 1200000);
// Foreign income
T({ kind: "income", value: 500000, incomeReported: false }, "CAT1", "unreported foreign income while resident", 300000);
T({ kind: "income", value: 500000, incomeReported: true }, "NOT_NEEDED", "foreign income reported");
T({ kind: "income", residentThen: false, residentSince: true, value: 500000, incomeReported: false }, "NOT_NEEDED", "income earned while NR");
T({ kind: "income", value: 9000000, otherCat1: 1500000, incomeReported: false }, "NOT_ELIGIBLE", "income aggregate above INR 1 crore");
// Exclusions
T({ pmla: true }, "EXCLUDED", "PMLA proceedings");
T({ bmaDone: true, source: "untaxed" }, "EXCLUDED", "BMA assessment completed");
// Validation
T({ value: 0 }, "ERROR", "zero value");
T({ value: -5 }, "ERROR", "negative value");
T({ otherCat1: -1 }, "ERROR", "negative other");
T({ kind: "x" }, "ERROR", "bad kind");
console.log("all " + n + " FAST-DS eligibility tests pass");
