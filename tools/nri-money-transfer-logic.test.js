// Run: node tools/nri-money-transfer-logic.test.js
const { moneyTransfer, tcsOnLrs } = require("./nri-money-transfer-logic.js");
const assert = require("assert");
let n = 0;
const ok = (c, m) => { assert.ok(c, m); n++; };
const has = (arr, s) => arr.some((x) => x.indexOf(s) !== -1);

// TCS on LRS (FY 2026-27)
assert.strictEqual(tcsOnLrs("eduLoan", 3000000, 0).tcs, 0); n++;
assert.strictEqual(tcsOnLrs("tour", 500000, 0).tcs, 10000); n++;              // flat 2%, no threshold
assert.strictEqual(tcsOnLrs("eduSelf", 1500000, 0).tcs, 10000); n++;          // 2% of 5 lakh
assert.strictEqual(tcsOnLrs("medical", 900000, 0).tcs, 0); n++;               // under threshold
assert.strictEqual(tcsOnLrs("gift", 1500000, 0).tcs, 100000); n++;            // 20% of 5 lakh
assert.strictEqual(tcsOnLrs("gift", 500000, 800000).tcs, 60000); n++;         // earlier 8 lakh: 3 lakh over -> 60,000
assert.strictEqual(tcsOnLrs("gift", 500000, 1200000).tcs, 100000); n++;       // already over: whole 5 lakh at 20%
assert.strictEqual(tcsOnLrs("investment", 1000000, 0).tcs, 0); n++;           // exactly 10 lakh: nil

// Into India
let r = moneyTransfer({ dir: "toIndia", country: "US", fund: "cash", credit: "relative", amountINR: 500000 });
ok(r.ok && has(r.country, "1% US remittance tax on this transfer (about INR 5,000)"), "US cash -> 1% flagged with amount");
ok(has(r.tax, "not taxable for them"), "gift to relative tax-free");
r = moneyTransfer({ dir: "toIndia", country: "US", fund: "bank", credit: "relative", amountINR: 500000 });
ok(!has(r.country, "on this transfer") && has(r.country, "does not apply") && has(r.country, "Form 709"), "US bank -> no 1%, Form 709 note kept");
r = moneyTransfer({ dir: "toIndia", country: "UK", fund: "bank", credit: "nonRelative", amountINR: 40000, otherGiftsINR: 20000 });
ok(r.verdict.indexOf("taxable for the receiver") !== -1 && has(r.tax, "INR 60,000"), "non-relative above 50k -> taxable");
r = moneyTransfer({ dir: "toIndia", country: "UK", fund: "bank", credit: "nonRelative", amountINR: 50000, otherGiftsINR: 0 });
ok(r.verdict.indexOf("no Indian tax") !== -1, "exactly 50k -> not taxable");
r = moneyTransfer({ dir: "toIndia", country: "CA", fund: "bank", credit: "ownNRE", amountINR: 1000000 });
ok(has(r.tax, "NRE interest is tax-free in India") && has(r.country, "no gift tax"), "own NRE, Canada");
r = moneyTransfer({ dir: "toIndia", country: "AU", fund: "bank", credit: "ownNRO", amountINR: 1000000 });
ok(has(r.limits, "USD 1 million") && has(r.country, "AUSTRAC"), "own NRO, Australia");

// Out of India: NRI
r = moneyTransfer({ dir: "fromIndia", country: "UK", who: "nri", source: "NRE", amountUSD: 2000000 });
ok(r.verdict.indexOf("Freely repatriable") !== -1 && !r.limits.length, "NRE has no cap");
ok(has(r.country, "remittance basis ended on 6 April 2025"), "UK in-flag");
r = moneyTransfer({ dir: "fromIndia", country: "US", who: "nri", source: "NRO", amountUSD: 400000, nroSoFarUSD: 500000 });
ok(r.verdict.indexOf("Allowed within") !== -1 && has(r.forms, "Form 145 and Form 146") && has(r.limits, "USD 900,000"), "NRO within cap");
ok(has(r.country, "FBAR") && has(r.country, "Form 3520"), "US in-flags");
r = moneyTransfer({ dir: "fromIndia", country: "US", who: "nri", source: "NRO", amountUSD: 600000, nroSoFarUSD: 500000 });
ok(r.verdict.indexOf("Over the USD 1 million") !== -1 && has(r.limits, "RBI approval"), "NRO over cap");
r = moneyTransfer({ dir: "fromIndia", country: "CA", who: "nri", source: "NRO", amountUSD: 1000000, nroSoFarUSD: 0 });
ok(r.verdict.indexOf("Allowed within") !== -1, "exactly USD 1 million allowed");
r = moneyTransfer({ dir: "fromIndia", country: "CA", who: "nri", source: "property", amountUSD: 300000 });
ok(has(r.limits, "two residential properties") && has(r.tax, "lower deduction certificate") && has(r.country, "T1135"), "property sale");

// Out of India: resident
r = moneyTransfer({ dir: "fromIndia", country: "AU", who: "resident", purpose: "gift", amountINR: 1500000, lrsSoFarINR: 0, rate: 95 });
ok(r.tcs === 100000 && r.verdict.indexOf("INR 1,00,000") !== -1, "resident gift TCS");
ok(has(r.country, "no gift tax") && !has(r.country, "worldwide income"), "resident gift: receiver gift rule only");
r = moneyTransfer({ dir: "fromIndia", country: "US", who: "resident", purpose: "gift", amountINR: 2000000, lrsSoFarINR: 0, rate: 95 });
ok(has(r.country, "Form 3520") && !has(r.country, "FBAR"), "US child receiving gift: Form 3520, not FBAR");
r = moneyTransfer({ dir: "fromIndia", country: "US", who: "resident", purpose: "eduLoan", amountINR: 4000000, lrsSoFarINR: 0 });
ok(r.tcs === 0 && r.verdict.indexOf("no TCS") !== -1, "education loan: no TCS, rate not needed");
r = moneyTransfer({ dir: "fromIndia", country: "UK", who: "resident", purpose: "investment", amountINR: 20000000, lrsSoFarINR: 5000000, rate: 95 });
ok(has(r.limits, "above the USD 250,000 limit"), "LRS cap exceeded (2.5 crore / 95 = ~263k)");
r = moneyTransfer({ dir: "fromIndia", country: "UK", who: "resident", purpose: "investment", amountINR: 20000000, lrsSoFarINR: 0, rate: 95 });
ok(!has(r.limits, "above the USD 250,000 limit"), "2 crore / 95 = ~210k within cap");

// Validation
ok(!moneyTransfer({ dir: "x", country: "UK", amountINR: 1 }).ok, "bad direction");
ok(!moneyTransfer({ dir: "toIndia", country: "JP", amountINR: 1 }).ok, "bad country");
ok(!moneyTransfer({ dir: "toIndia", country: "UK", credit: "relative", amountINR: 0 }).ok, "zero amount");
ok(!moneyTransfer({ dir: "fromIndia", country: "UK", who: "nri", source: "NRO", amountUSD: 10, nroSoFarUSD: -1 }).ok, "negative so far");
ok(!moneyTransfer({ dir: "fromIndia", country: "UK", who: "resident", purpose: "gift", amountINR: 100, lrsSoFarINR: 0, rate: 0 }).ok, "rate needed");
console.log("all " + n + " money-transfer tests pass");
