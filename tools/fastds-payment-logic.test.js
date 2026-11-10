// Run: node tools/fastds-payment-logic.test.js
const { fastdsPayment } = require("./fastds-payment-logic.js");
const assert = require("assert");
let n = 0;
const eq = (a, b, m) => { assert.deepStrictEqual(a, b, m); n++; };

// Declared 20 Nov 2026, Form 2 received 10 Dec 2026
let r = fastdsPayment({ declarationDate: "2026-11-20", orderDate: "2026-12-10", amount: 100000 });
eq(r.orderBy, "2026-12-31", "order expected by end of the following month");
eq(r.dueDate, "2027-02-28", "pay within two months from end of December");
eq(r.extendedDate, "2027-04-30", "further two months");
eq(r.orderAssumed, false);

// Paid on time
r = fastdsPayment({ orderDate: "2026-12-10", paymentDate: "2027-02-28", amount: 100000 });
eq([r.status, r.interest, r.total], ["on time", 0, 100000]);

// One day late = one month interest
r = fastdsPayment({ orderDate: "2026-12-10", paymentDate: "2027-03-01", amount: 100000 });
eq([r.status, r.months, r.interest, r.total], ["late, within the extended period", 1, 1000, 101000]);

// Paid in April = two months
r = fastdsPayment({ orderDate: "2026-12-10", paymentDate: "2027-04-30", amount: 4800000 });
eq([r.months, r.interest, r.total], [2, 96000, 4896000]);

// After the extended period
r = fastdsPayment({ orderDate: "2026-12-10", paymentDate: "2027-05-01", amount: 100000 });
eq(r.status, "after the extended period");

// Only declaration date: order assumed at the latest date
r = fastdsPayment({ declarationDate: "2026-12-31", amount: 100000 });
eq([r.orderBy, r.orderAssumed, r.dueDate, r.extendedDate], ["2027-01-31", true, "2027-03-31", "2027-05-31"]);

// Leap-year style month-end handling (order in Nov -> due 31 Jan)
r = fastdsPayment({ orderDate: "2026-11-30", amount: 100000 });
eq(r.dueDate, "2027-01-31");

// Validation
eq(fastdsPayment({ amount: 100 }).ok, false, "needs a date");
eq(fastdsPayment({ orderDate: "2026-12-10", amount: 0 }).ok, false, "needs amount");
eq(fastdsPayment({ declarationDate: "2027-01-05", amount: 100 }).ok, false, "after window");
eq(fastdsPayment({ declarationDate: "2026-08-01", amount: 100 }).ok, false, "before window");
eq(fastdsPayment({ declarationDate: "2026-12-10", orderDate: "2026-12-01", amount: 100 }).ok, false, "order before declaration");
eq(fastdsPayment({ orderDate: "2026-02-30", amount: 100 }).ok, false, "invalid date");
console.log("all " + n + " FAST-DS payment tests pass");
