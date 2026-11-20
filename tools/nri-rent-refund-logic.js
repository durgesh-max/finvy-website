/* NRI rental income: TDS the tenant deducts on gross rent (30% plus surcharge and cess) vs tax on income from house
   property: (rent - municipal taxes paid) less 30% standard deduction less interest on a home loan for the let-out
   property; under the new regime a loss from house property is not set off against other income. Tax at FY 2025-26
   new-regime slabs on the incremental income (no section 87A rebate for non-residents), 4% cess, no surcharge below
   INR 50 lakh. Estimate only. */
function rentSlabTax(income) {
  var bands = [[400000, 0], [800000, 0.05], [1200000, 0.10], [1600000, 0.15], [2000000, 0.20], [2400000, 0.25], [Infinity, 0.30]];
  var tax = 0, prev = 0, x = Math.max(0, Number(income) || 0);
  for (var i = 0; i < bands.length; i++) { var top = bands[i][0], r = bands[i][1]; if (x > prev) tax += (Math.min(x, top) - prev) * r; prev = top; }
  return tax * 1.04;
}
function rentTdsSurcharge(amount) { if (amount > 10000000) return 0.15; if (amount > 5000000) return 0.10; return 0; }
function nriRentRefund(input) {
  var rent = Number(input.rent), muni = Number(input.municipal || 0), interest = Number(input.interest || 0), other = Number(input.other || 0);
  var errors = [];
  if (!(rent > 0)) errors.push("Enter the annual rent.");
  [muni, interest, other].forEach(function (v) { if (v < 0 || isNaN(v)) errors.push("Amounts cannot be negative."); });
  if (errors.length) return { ok: false, errors: errors };
  var tds = rent * 0.30 * (1 + rentTdsSurcharge(rent)) * 1.04;
  var nav = Math.max(0, rent - muni);
  var hp = Math.max(0, nav * 0.70 - interest);
  var tax = rentSlabTax(other + hp) - rentSlabTax(other);
  return { ok: true, tds: Math.round(tds), houseProperty: Math.round(hp), tax: Math.round(tax), refund: Math.round(Math.max(0, tds - tax)), highIncome: (other + hp) > 5000000 };
}
if (typeof module !== "undefined") module.exports = { nriRentRefund: nriRentRefund, rentSlabTax: rentSlabTax };
