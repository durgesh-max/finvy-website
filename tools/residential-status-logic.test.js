const { residency, countDaysInYear } = require("./residential-status-logic.js");
const assert = require("assert");
const base = { act: "1961", days: 0, days4: 0, citizen: true, pio: false, category: "other", incomeOver15L: false, liableAbroad: true, nrYears10: 0, days7: 2000 };
const T = (o) => residency(Object.assign({}, base, o));
let n = 0; const eq = (o, st, msg) => { const r = T(o); assert.strictEqual(r.ok && r.status, st, msg + " -> got " + JSON.stringify(r.status || r.errors)); n++; };

for (const act of ["1961", "2025"]) {
  // 182-day test
  eq({ act, days: 182 }, "ROR", act + ": exactly 182 days, long-term resident");
  eq({ act, days: 181, days4: 0 }, "NR", act + ": 181 days, no 365 in 4 yrs");
  // 60 + 365 test, ordinary person
  eq({ act, days: 60, days4: 365 }, "ROR", act + ": 60 + 365 boundary, other");
  eq({ act, days: 59, days4: 365 }, "NR", act + ": 59 days");
  eq({ act, days: 60, days4: 364 }, "NR", act + ": 364 in 4 yrs");
  // Citizen leaving India for employment: 60-day rule switched off
  eq({ act, category: "leaving", days: 150, days4: 1200 }, "NR", act + ": leaving for job, 150 days");
  eq({ act, category: "leaving", days: 182, days4: 1200 }, "ROR", act + ": leaving for job, 182 days");
  // Visiting, income <= 15L: 60-day rule switched off
  eq({ act, category: "visiting", days: 181, days4: 900, nrYears10: 2, days7: 1500 }, "NR", act + ": visiting, low income, 181 days");
  eq({ act, category: "visiting", days: 182, days4: 900, nrYears10: 2, days7: 1500 }, "ROR", act + ": visiting, low income, 182 days, long history");
  // Visiting, income > 15L: 120 days + 365 -> resident, and RNOR under 6(6)(c)/6(13)(b)
  eq({ act, category: "visiting", incomeOver15L: true, days: 120, days4: 365, nrYears10: 0, days7: 2000 }, "RNOR", act + ": visiting high income 120 days");
  eq({ act, category: "visiting", incomeOver15L: true, days: 119, days4: 400, liableAbroad: true }, "NR", act + ": visiting high income 119 days, taxed abroad");
  eq({ act, category: "visiting", incomeOver15L: true, days: 130, days4: 300, liableAbroad: true }, "NR", act + ": 130 days but only 300 in 4 yrs, taxed abroad");
  eq({ act, category: "visiting", incomeOver15L: true, days: 182, days4: 1400, nrYears10: 0, days7: 2000 }, "ROR", act + ": visiting high income 182 days, long history");
  // Deemed resident (1A / 6(7)): citizen, >15L, not liable abroad, not resident under day tests -> RNOR
  eq({ act, category: "visiting", incomeOver15L: true, liableAbroad: false, days: 10, days4: 0 }, "RNOR", act + ": deemed resident");
  eq({ act, incomeOver15L: true, liableAbroad: false, days: 0, days4: 0, citizen: true }, "RNOR", act + ": deemed resident, zero days");
  eq({ act, incomeOver15L: true, liableAbroad: false, days: 0, citizen: false, pio: true, category: "visiting" }, "NR", act + ": PIO not citizen cannot be deemed resident");
  eq({ act, incomeOver15L: false, liableAbroad: false, days: 0 }, "NR", act + ": income not above 15L, not deemed");
  // Deemed resident does not override day-test residence (Explanation to 1A / 6(8))
  eq({ act, incomeOver15L: true, liableAbroad: false, days: 200, nrYears10: 0, days7: 2000 }, "ROR", act + ": resident by days -> ROR, not deemed RNOR");
  // NOR tests for residents by days
  eq({ act, days: 200, nrYears10: 9, days7: 2000 }, "RNOR", act + ": NR in 9 of 10");
  eq({ act, days: 200, nrYears10: 8, days7: 729 }, "RNOR", act + ": 729 days in 7 yrs");
  eq({ act, days: 200, nrYears10: 8, days7: 730 }, "ROR", act + ": 730 days in 7 yrs");
  // Foreign national
  eq({ act, citizen: false, pio: false, days: 100, days4: 400, nrYears10: 0, days7: 1000 }, "ROR", act + ": foreigner 60+365");
  eq({ act, citizen: false, pio: false, days: 100, days4: 400, nrYears10: 10, days7: 1000 }, "RNOR", act + ": foreigner, NR 10 of 10");
}
// Validation
let r = residency(Object.assign({}, base, { category: "leaving", citizen: false })); assert.strictEqual(r.ok, false); n++;
r = residency(Object.assign({}, base, { category: "visiting", citizen: false, pio: false })); assert.strictEqual(r.ok, false); n++;
r = residency(Object.assign({}, base, { days: 367 })); assert.strictEqual(r.ok, false); n++;
r = residency(Object.assign({}, base, { days: 10.5 })); assert.strictEqual(r.ok, false); n++;
// Citations differ by Act
assert.ok(T({ act: "2025", days: 200 }).trace.join(" ").includes("section 6(2)(a)")); n++;
assert.ok(T({ act: "1961", days: 200 }).trace.join(" ").includes("section 6(1)(a)")); n++;
// Day counter (arrival and departure both counted, FY 1 Apr - 31 Mar, overlaps counted once)
assert.strictEqual(countDaysInYear([{ from: "2025-04-01", to: "2025-04-01" }], 2025), 1); n++;
assert.strictEqual(countDaysInYear([{ from: "2025-03-25", to: "2025-04-05" }], 2025), 5); n++;
assert.strictEqual(countDaysInYear([{ from: "2026-03-30", to: "2026-04-03" }], 2025), 2); n++;
assert.strictEqual(countDaysInYear([{ from: "2025-04-01", to: "" }], 2025), 365); n++;
assert.strictEqual(countDaysInYear([{ from: "2027-04-01", to: "" }], 2027), 366); n++; // FY 2027-28 includes 29 Feb 2028
assert.strictEqual(countDaysInYear([{ from: "2025-06-01", to: "2025-06-10" }, { from: "2025-06-05", to: "2025-06-15" }], 2025), 15); n++;
assert.strictEqual(countDaysInYear([{ from: "2025-10-27", to: "2025-11-03" }], 2025), 8); n++; // across a DST change elsewhere; UTC-safe
console.log("all " + n + " tests pass");
