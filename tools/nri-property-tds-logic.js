/* NRI property sale: TDS the buyer deducts on the full price (no certificate) vs tax on the actual long-term gain.
   Long-term (held more than 24 months): 12.5% without indexation for non-residents, surcharge 10% above INR 50 lakh and
   15% above INR 1 crore (capped at 15% for long-term gains), health and education cess 4%. Assumes the gain is the only
   Indian income (non-residents cannot set the basic exemption against long-term gains); ignores marginal relief and exemptions. */
function nriSurcharge(amount) {
  if (amount > 10000000) return 0.15;
  if (amount > 5000000) return 0.10;
  return 0;
}
function nriPropertyTds(input) {
  var price = Number(input.price), cost = Number(input.cost || 0), longTerm = input.longTerm !== false;
  var errors = [];
  if (!(price > 0)) errors.push("Enter the sale price.");
  if (cost < 0 || isNaN(cost)) errors.push("Enter the purchase cost (0 if unknown).");
  if (errors.length) return { ok: false, errors: errors };
  if (!longTerm) return { ok: true, longTerm: false, tdsRate: 0.30 };
  var r = 0.125, cess = 0.04;
  var tdsFull = price * r * (1 + nriSurcharge(price)) * (1 + cess);
  var gain = Math.max(0, price - cost);
  var tax = gain * r * (1 + nriSurcharge(gain)) * (1 + cess);
  return { ok: true, longTerm: true, gain: Math.round(gain), tdsFull: Math.round(tdsFull), tax: Math.round(tax),
           excess: Math.round(Math.max(0, tdsFull - tax)) };
}
if (typeof module !== "undefined") module.exports = { nriPropertyTds: nriPropertyTds, nriSurcharge: nriSurcharge };
