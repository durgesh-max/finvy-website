/* NRO interest: TDS a bank deducts for a non-resident (30% plus surcharge and cess) vs the lower of (a) the treaty rate on
   the interest (with a TRC and Form 10F; treaty rate is final, no surcharge or cess) and (b) tax at new-regime slab rates
   for FY 2025-26 on the interest added to other Indian income (non-residents get no section 87A rebate; 4% cess; no
   surcharge modelled below INR 50 lakh total income). Estimate only. */
var NRO_TREATY = { uae: 0.125, usa: 0.15, uk: 0.15, canada: 0.15, australia: 0.15, singapore: 0.15, saudi: 0.10, qatar: 0.10, oman: 0.10, none: null };
function nroSlabTax(income) {
  var bands = [[400000, 0], [800000, 0.05], [1200000, 0.10], [1600000, 0.15], [2000000, 0.20], [2400000, 0.25], [Infinity, 0.30]];
  var tax = 0, prev = 0, x = Math.max(0, Number(income) || 0);
  for (var i = 0; i < bands.length; i++) {
    var top = bands[i][0], rate = bands[i][1];
    if (x > prev) tax += (Math.min(x, top) - prev) * rate;
    prev = top;
  }
  return tax * 1.04;
}
function nroTdsSurcharge(amount) {
  if (amount > 10000000) return 0.15;
  if (amount > 5000000) return 0.10;
  return 0;
}
function nroInterestRefund(input) {
  var interest = Number(input.interest), other = Number(input.other || 0);
  var country = input.country || "none", trc = !!input.trc;
  var errors = [];
  if (!(interest > 0)) errors.push("Enter the NRO interest for the year.");
  if (other < 0 || isNaN(other)) errors.push("Enter other Indian income (0 if none).");
  if (!(country in NRO_TREATY)) errors.push("Choose your country of residence.");
  if (errors.length) return { ok: false, errors: errors };
  var tds = interest * 0.30 * (1 + nroTdsSurcharge(interest)) * 1.04;
  var rate = NRO_TREATY[country];
  var treatyTax = (rate !== null && trc) ? interest * rate : null;
  var slabTax = nroSlabTax(other + interest) - nroSlabTax(other);
  var actual = treatyTax === null ? slabTax : Math.min(treatyTax, slabTax);
  var basis = (treatyTax !== null && treatyTax < slabTax) ? "treaty" : "slab";
  return { ok: true, tds: Math.round(tds), treatyTax: treatyTax === null ? null : Math.round(treatyTax), slabTax: Math.round(slabTax),
           actual: Math.round(actual), basis: basis, refund: Math.round(Math.max(0, tds - actual)), highIncome: (other + interest) > 5000000 };
}
if (typeof module !== "undefined") module.exports = { nroInterestRefund: nroInterestRefund, nroSlabTax: nroSlabTax, NRO_TREATY: NRO_TREATY };
