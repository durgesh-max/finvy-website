/* NRI income tax estimate for 2026-27 (Indian income only). Slab income at new-regime rates (nil to INR 4 lakh, 5% to
   8 lakh, 10% to 12 lakh, 15% to 16 lakh, 20% to 20 lakh, 25% to 24 lakh, 30% above) or old-regime rates (nil to
   INR 2.5 lakh at any age for non-residents, 5% to 5 lakh, 20% to 10 lakh, 30% above, less deductions such as 80C / 80D).
   No section 87A rebate for non-residents, and special-rate gains cannot use any unused basic exemption (resident-only
   relief). Equity STCG (listed shares / equity funds) 20%; equity LTCG 12.5% above INR 1.25 lakh; other LTCG
   (property, unlisted shares, debt funds bought before April 2023 etc.) 12.5%. Surcharge on total income: 10% above
   INR 50 lakh, 15% above 1 crore, 25% above 2 crore, 37% above 5 crore (old regime only); capped at 15% on capital
   gains tax. 4% cess. Marginal relief not applied. Estimate only. */
function nriSlabTax(income, regime) {
  var bands = regime === "old"
    ? [[250000, 0], [500000, 0.05], [1000000, 0.20], [Infinity, 0.30]]
    : [[400000, 0], [800000, 0.05], [1200000, 0.10], [1600000, 0.15], [2000000, 0.20], [2400000, 0.25], [Infinity, 0.30]];
  var tax = 0, prev = 0, x = Math.max(0, Number(income) || 0);
  for (var i = 0; i < bands.length; i++) { var top = bands[i][0], r = bands[i][1]; if (x > prev) tax += (Math.min(x, top) - prev) * r; prev = top; }
  return tax;
}
function nriSurchargeRate(total, regime) {
  if (total > 50000000) return regime === "old" ? 0.37 : 0.25;
  if (total > 20000000) return 0.25;
  if (total > 10000000) return 0.15;
  if (total > 5000000) return 0.10;
  return 0;
}
function nriIncomeTax(input) {
  var regime = input.regime === "old" ? "old" : "new";
  var slab = Number(input.slab || 0), stcg = Number(input.stcg || 0), ltcgEq = Number(input.ltcgEq || 0),
      ltcgOther = Number(input.ltcgOther || 0), ded = Number(input.deductions || 0), tds = Number(input.tds || 0);
  var errors = [];
  [slab, stcg, ltcgEq, ltcgOther, ded, tds].forEach(function (v) { if (isNaN(v) || v < 0) errors.push("Amounts cannot be negative."); });
  if (errors.length) return { ok: false, errors: errors.slice(0, 1) };
  if (slab + stcg + ltcgEq + ltcgOther <= 0) return { ok: false, errors: ["Enter at least one Indian income figure."] };
  var slabTaxable = Math.max(0, slab - (regime === "old" ? ded : 0));
  var slabTax = nriSlabTax(slabTaxable, regime);
  var cgTax = stcg * 0.20 + Math.max(0, ltcgEq - 125000) * 0.125 + ltcgOther * 0.125;
  var total = slabTaxable + stcg + ltcgEq + ltcgOther;
  var rate = nriSurchargeRate(total, regime);
  var surcharge = slabTax * rate + cgTax * Math.min(rate, 0.15);
  var cess = (slabTax + cgTax + surcharge) * 0.04;
  var tax = slabTax + cgTax + surcharge + cess;
  return { ok: true, regime: regime, taxableIncome: Math.round(total), slabTax: Math.round(slabTax), cgTax: Math.round(cgTax),
           surcharge: Math.round(surcharge), cess: Math.round(cess), tax: Math.round(tax),
           effective: total > 0 ? Math.round(tax / total * 1000) / 10 : 0,
           refund: Math.round(Math.max(0, tds - tax)), due: Math.round(Math.max(0, tax - tds)) };
}
if (typeof module !== "undefined") module.exports = { nriIncomeTax: nriIncomeTax, nriSlabTax: nriSlabTax };
