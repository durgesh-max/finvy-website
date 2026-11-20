/* Foreign company in India: tax on a branch vs an Indian subsidiary, FY 2026-27 rates.
   Branch: taxed as a foreign company at 35% plus surcharge (2% above INR 1 crore, 5% above INR 10 crore) and 4% cess;
   no further Indian tax when profits are remitted. Subsidiary: section 115BAA 22% plus 10% surcharge and 4% cess
   (25.168%); dividends paid to the foreign parent are subject to withholding at the treaty rate (with a TRC and Form 10F)
   or, without a treaty, 20% plus surcharge and cess. Marginal relief ignored. Estimate only. */
var BVS_TREATY = { usa: 0.15, canada: 0.15, australia: 0.15, uk: 0.10, singapore: 0.10, uae: 0.10, germany: 0.10,
  netherlands: 0.10, japan: 0.10, mauritius: 0.05, saudi: 0.05, qatar: 0.05, none: null };
function bvsSurchargeForeign(amount) { if (amount > 100000000) return 0.05; if (amount > 10000000) return 0.02; return 0; }
function branchVsSubsidiary(input) {
  var profit = Number(input.profit), payout = input.payout === undefined || input.payout === "" ? 100 : Number(input.payout);
  var country = String(input.country || "none");
  var errors = [];
  if (!(profit > 0)) errors.push("Enter the expected annual profit in India.");
  if (isNaN(payout) || payout < 0 || payout > 100) errors.push("Payout must be between 0 and 100%.");
  if (!(country in BVS_TREATY)) errors.push("Choose the parent company's country.");
  if (errors.length) return { ok: false, errors: errors };
  var branchTax = profit * 0.35 * (1 + bvsSurchargeForeign(profit)) * 1.04;
  var corpTax = profit * 0.22 * 1.10 * 1.04;
  var dividend = (profit - corpTax) * payout / 100;
  var rate = BVS_TREATY[country];
  var whtRate = rate === null ? 0.20 * (1 + bvsSurchargeForeign(dividend)) * 1.04 : rate;
  var wht = dividend * whtRate;
  var subTax = corpTax + wht;
  return { ok: true, branchTax: Math.round(branchTax), branchRate: branchTax / profit, corpTax: Math.round(corpTax),
    dividend: Math.round(dividend), whtRate: whtRate, wht: Math.round(wht), subTax: Math.round(subTax), subRate: subTax / profit,
    saving: Math.round(branchTax - subTax), treaty: rate !== null };
}
if (typeof module !== "undefined") module.exports = { branchVsSubsidiary: branchVsSubsidiary, BVS_TREATY: BVS_TREATY };
