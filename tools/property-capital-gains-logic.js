/* Property (land or building) capital gains in India: 12.5% without indexation vs 20% with indexation.
   Long-term if held more than 24 months (previous owner's holding counts for inherited or gifted property).
   Residents (individual/HUF) may choose 20% with indexation for land or buildings acquired before 23 July 2024;
   non-residents pay 12.5% without indexation. Property acquired before 1 April 2001: cost may be fair market value on
   1 April 2001 (capped at the stamp duty value on that date), indexed from 2001-02. Cess 4%; surcharge and basic
   exemption ignored (depend on total income). Section 54 (new house, up to INR 10 crore) and 54EC (bonds, up to INR 50
   lakh) reduce the gain. CII: CBDT, latest 384 for 2026-27 (Notification 85/2026, 15 July 2026). */
var CII = {2001:100,2002:105,2003:109,2004:113,2005:117,2006:122,2007:129,2008:137,2009:148,2010:167,2011:184,2012:200,
           2013:220,2014:240,2015:254,2016:264,2017:272,2018:280,2019:289,2020:301,2021:317,2022:331,2023:348,2024:363,
           2025:376,2026:384};
function fyOf(d) { var y = d.getUTCFullYear(), m = d.getUTCMonth() + 1; return m >= 4 ? y : y - 1; }
function monthsHeld(a, b) {
  var m = (b.getUTCFullYear() - a.getUTCFullYear()) * 12 + (b.getUTCMonth() - a.getUTCMonth());
  if (b.getUTCDate() < a.getUTCDate()) m -= 1;
  return m;
}
function propertyCapitalGains(input) {
  var errors = [];
  var buy = new Date(input.buyDate + "T00:00:00Z"), sale = new Date(input.saleDate + "T00:00:00Z");
  var cost = Number(input.cost || 0), price = Number(input.price), exp = Number(input.expenses || 0);
  var imp = Number(input.improvement || 0), impDate = input.improvementDate ? new Date(input.improvementDate + "T00:00:00Z") : null;
  var r54 = Math.min(Number(input.reinvest54 || 0), 100000000), r54ec = Math.min(Number(input.bonds54EC || 0), 5000000);
  var resident = input.resident !== false;
  if (isNaN(buy) || isNaN(sale)) errors.push("Enter valid purchase and sale dates.");
  else if (sale < buy) errors.push("Sale date must be after the purchase date.");
  if (!(price > 0)) errors.push("Enter the sale price.");
  if (cost < 0 || isNaN(cost)) errors.push("Enter the purchase cost.");
  if (imp > 0 && (!impDate || isNaN(impDate))) errors.push("Enter the year of the improvement.");
  if (errors.length) return { ok: false, errors: errors };
  var saleFY = fyOf(sale);
  if (!CII[saleFY]) return { ok: false, errors: ["The cost inflation index for the year of sale is not yet notified (latest: 2026-27)."] };
  var longTerm = monthsHeld(buy, sale) > 24;
  var gainA = price - exp - cost - imp;
  var res = { ok: true, longTerm: longTerm, saleFY: saleFY, gainNoIndex: Math.round(gainA) };
  if (!longTerm) { res.note = "short"; return res; }
  var exempt = r54 + r54ec;
  var taxable = function (g) { return Math.max(0, g - Math.min(exempt, Math.max(0, g))); };
  res.taxA = Math.round(taxable(gainA) * 0.125 * 1.04);
  var pre2001 = buy < new Date("2001-04-01T00:00:00Z");
  var baseFY = pre2001 ? 2001 : fyOf(buy);
  var canIndex = resident && buy < new Date("2024-07-23T00:00:00Z");
  res.canIndex = canIndex; res.pre2001 = pre2001;
  if (canIndex) {
    var idxCost = cost * CII[saleFY] / CII[baseFY];
    var idxImp = imp > 0 ? imp * CII[saleFY] / CII[Math.max(2001, fyOf(impDate))] : 0;
    var gainB = price - exp - idxCost - idxImp;
    res.indexedCost = Math.round(idxCost + idxImp); res.gainIndexed = Math.round(gainB);
    res.taxB = Math.round(taxable(gainB) * 0.20 * 1.04);
    res.best = res.taxB < res.taxA ? "indexed" : "flat";
  } else res.best = "flat";
  res.exemptApplied = exempt;
  return res;
}
if (typeof module !== "undefined") module.exports = { propertyCapitalGains: propertyCapitalGains, CII: CII, fyOf: fyOf };
