/* Freelancer / consultant income tax estimate for a resident individual, tax year 2026-27.
   Profit: presumptive under section 44ADA (section 58 of the Income-tax Act, 2025) at 50% of gross receipts (or a
   higher declared %), available up to INR 75 lakh of receipts where cash receipts are within 5% (INR 50 lakh otherwise);
   or actual profit = receipts minus business expenses. Slab rates: new regime nil to INR 4 lakh, 5% to 8 lakh, 10% to
   12 lakh, 15% to 16 lakh, 20% to 20 lakh, 25% to 24 lakh, 30% above; old regime nil to 2.5 lakh (3 lakh at 60-80,
   5 lakh at 80+), 5% to 5 lakh, 20% to 10 lakh, 30% above, less deductions such as 80C / 80D. Section 87A rebate for
   residents: new regime full rebate up to INR 12 lakh total income with marginal relief just above; old regime up to
   INR 12,500 where income is up to INR 5 lakh. No standard deduction (salary only). Surcharge 10% above INR 50 lakh,
   15% above 1 crore, 25% above 2 crore (old regime 37% above 5 crore); surcharge marginal relief not applied. 4% cess.
   Estimate only. */
function flSlabTax(income, regime, age) {
  var first = regime === "old" ? (age === "80" ? 500000 : age === "60" ? 300000 : 250000) : 0;
  var bands = regime === "old"
    ? [[first, 0], [500000, 0.05], [1000000, 0.20], [Infinity, 0.30]]
    : [[400000, 0], [800000, 0.05], [1200000, 0.10], [1600000, 0.15], [2000000, 0.20], [2400000, 0.25], [Infinity, 0.30]];
  var tax = 0, prev = 0, x = Math.max(0, Number(income) || 0);
  for (var i = 0; i < bands.length; i++) { var top = bands[i][0], r = bands[i][1]; if (x > prev && top > prev) tax += (Math.min(x, top) - prev) * r; prev = Math.max(prev, top); }
  return tax;
}
function flSurchargeRate(total, regime) {
  if (total > 50000000) return regime === "old" ? 0.37 : 0.25;
  if (total > 20000000) return 0.25;
  if (total > 10000000) return 0.15;
  if (total > 5000000) return 0.10;
  return 0;
}
function freelancerTax(input) {
  var regime = input.regime === "old" ? "old" : "new";
  var age = input.age === "60" || input.age === "80" ? input.age : "below60";
  var method = input.method === "actual" ? "actual" : "44ada";
  var receipts = Number(input.receipts || 0), expenses = Number(input.expenses || 0), other = Number(input.other || 0),
      ded = Number(input.deductions || 0), tds = Number(input.tds || 0), pct = Number(input.pct || 50);
  var lowCash = input.lowCash !== false && input.lowCash !== "no";
  var errors = [];
  [receipts, expenses, other, ded, tds].forEach(function (v) { if (isNaN(v) || v < 0) errors.push("Amounts cannot be negative."); });
  if (isNaN(pct) || pct < 50 || pct > 100) errors.push("The presumptive profit rate must be between 50% and 100%.");
  if (errors.length) return { ok: false, errors: errors.slice(0, 1) };
  if (receipts <= 0) return { ok: false, errors: ["Enter your gross professional receipts for the year."] };
  var limit = lowCash ? 7500000 : 5000000, notes = [];
  if (method === "44ada" && receipts > limit) {
    method = "actual";
    notes.push("Receipts are above the INR " + (limit / 100000) + " lakh limit for section 44ADA, so actual profit is used; books and a tax audit are likely needed.");
  }
  var profit = method === "44ada" ? receipts * pct / 100 : Math.max(0, receipts - expenses);
  var gross = profit + other;
  var taxable = Math.max(0, gross - (regime === "old" ? ded : 0));
  var slabTax = flSlabTax(taxable, regime, age);
  var rebate = 0;
  if (regime === "new") {
    if (taxable <= 1200000) rebate = slabTax;
    else if (slabTax > taxable - 1200000) rebate = slabTax - (taxable - 1200000);
  } else if (taxable <= 500000) rebate = Math.min(slabTax, 12500);
  var afterRebate = slabTax - rebate;
  var surcharge = afterRebate * flSurchargeRate(taxable, regime);
  var cess = (afterRebate + surcharge) * 0.04;
  var tax = afterRebate + surcharge + cess;
  var due = Math.max(0, tax - tds);
  var advance = due >= 10000 ? (method === "44ada" ? "single" : "four") : "none";
  return { ok: true, regime: regime, method: method, profit: Math.round(profit), taxableIncome: Math.round(taxable),
           slabTax: Math.round(slabTax), rebate: Math.round(rebate), surcharge: Math.round(surcharge), cess: Math.round(cess),
           tax: Math.round(tax), effective: receipts > 0 ? Math.round(tax / receipts * 1000) / 10 : 0,
           refund: Math.round(Math.max(0, tds - tax)), due: Math.round(due), advance: advance, notes: notes };
}
if (typeof module !== "undefined") module.exports = { freelancerTax: freelancerTax, flSlabTax: flSlabTax };
