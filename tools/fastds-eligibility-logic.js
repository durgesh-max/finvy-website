// FAST-DS 2026 eligibility (Finance Act, 2026, Chapter IV, sections 130-144). One foreign asset or income item at a time.
// Inputs:
//   kind: "asset" | "income"            asset located outside India, or foreign income
//   residentThen: boolean               resident in India in the year the income arose / the asset was acquired
//   residentSince: boolean              (only when residentThen is false) became resident in India in any later year up to 2025-26
//   source: "untaxed" | "taxedIndia" | "foreignWhileNR"   source of the money used to buy the asset (asset only)
//   reportedFA: boolean                 asset shown in the foreign-assets schedule (Schedule FA) of every return where required
//   incomeReported: boolean             all income from the asset / the foreign income itself offered to tax in India in resident years
//   value: number (INR)                 asset value as on 31 March 2026 (asset) or income amount (income)
//   otherCat1: number (INR)             other Category 1 items being declared (for the INR 1 crore aggregate)
//   pmla: boolean                       proceeds of crime with PMLA proceedings initiated or pending
//   bmaDone: boolean                    Black Money Act assessment already completed for the year
function fastds(i) {
  var e = [];
  if (i.kind !== "asset" && i.kind !== "income") e.push("Choose asset or income");
  if (typeof i.value !== "number" || !isFinite(i.value) || i.value <= 0) e.push("Enter the value (more than zero)");
  if (typeof i.otherCat1 !== "number" || !isFinite(i.otherCat1) || i.otherCat1 < 0) e.push("Other Category 1 amount must be zero or more");
  if (e.length) return { ok: false, errors: e };
  var why = [];
  if (i.pmla) return { ok: true, result: "EXCLUDED", why: ["Section 140(a): the scheme does not apply to income or assets that are proceeds of crime with proceedings under the Prevention of Money-laundering Act initiated or pending."] };
  if (i.bmaDone) return { ok: true, result: "EXCLUDED", why: ["Section 140(b): the scheme does not apply to an assessment year for which assessment under the Black Money Act has been completed."] };

  if (!i.residentThen && !i.residentSince) {
    return { ok: true, result: "NOT_NEEDED", why: ["You were not resident when the income arose or the asset was acquired, and have not been resident since. Foreign income of a non-resident is generally not taxable in India and the foreign-assets schedule applies to residents, so there is normally nothing to declare. Section 131(1)(a) also makes a person eligible only if resident in the relevant year."] };
  }
  var LIMIT1 = 10000000, LIMIT2 = 50000000;
  if (i.kind === "income") {
    if (!i.residentThen) return { ok: true, result: "NOT_NEEDED", why: ["Foreign income earned while non-resident is generally not taxable in India, so it is not undisclosed foreign income (section 131(1)(k))."] };
    if (i.incomeReported) return { ok: true, result: "NOT_NEEDED", why: ["The income was offered to tax in India, so it is not undisclosed foreign income (section 131(1)(k))."] };
    var agg = i.value + i.otherCat1;
    why.push("Undisclosed foreign income: income from a source outside India, chargeable to tax in India, not offered to tax (section 131(1)(k)).");
    if (agg > LIMIT1) return { ok: true, result: "NOT_ELIGIBLE", why: why.concat(["Category 1 is available only if the aggregate of undisclosed foreign assets and income does not exceed INR 1 crore (section 133, Table, item 1). Aggregate: INR " + agg.toLocaleString("en-IN") + "."]) };
    return { ok: true, result: "CAT1", amount: Math.round(i.value * 0.6), why: why.concat(["Category 1: tax of 30% plus an equal amount, 60% in all (section 133, Table, item 1)."]) };
  }
  // asset
  if (i.source !== "untaxed" && i.reportedFA && i.incomeReported) return { ok: true, result: "NOT_NEEDED", why: ["The asset was bought from explained funds, shown in the foreign-assets schedule, and its income was offered to tax, so nothing is undisclosed."] };
  if (i.source === "untaxed") {
    var a1 = i.value + i.otherCat1;
    why.push("An asset outside India with no satisfactory explanation of the source of investment is an undisclosed asset located outside India (section 131(1)(j)).");
    if (a1 > LIMIT1) return { ok: true, result: "NOT_ELIGIBLE", why: why.concat(["Category 1 needs the aggregate of undisclosed foreign assets and income to be INR 1 crore or less (section 133, Table, item 1). Aggregate: INR " + a1.toLocaleString("en-IN") + "."]) };
    return { ok: true, result: "CAT1", amount: Math.round(i.value * 0.6), why: why.concat(["Category 1: 60% of the value as on 31 March 2026 (section 133, Table, item 1)."]) };
  }
  if (i.reportedFA && !i.incomeReported) {
    return { ok: true, result: "INCOME_ONLY", why: ["The asset itself was disclosed and acquired from explained funds, so it is not an undisclosed asset. Interest, dividends or gains from it that were not offered to tax are undisclosed foreign income: declare them under Category 1 (60%), or correct them through a revised or updated return where still possible."] };
  }
  // source explained (taxed in India, or foreign income while non-resident) but not in Schedule FA
  if (i.source === "foreignWhileNR" && !i.residentSince) return { ok: true, result: "NOT_NEEDED", why: ["The asset was bought while you were non-resident and you have not been resident since, so no foreign-assets schedule was required."] };
  why.push(i.source === "taxedIndia" ? "Asset bought from income already offered to tax in India but not shown in the foreign-assets schedule (section 133, Table, item 2(b))." : "Asset bought from foreign income while you were non-resident, not shown in the foreign-assets schedule after becoming resident (section 133, Table, item 2(a)).");
  if (i.value > LIMIT2) return { ok: true, result: "NOT_ELIGIBLE", why: why.concat(["Category 2 needs the asset value to be INR 5 crore or less (section 133, Table, item 2)."]) };
  var extra = i.incomeReported ? [] : ["Income from the asset that was not offered to tax in resident years is undisclosed foreign income and goes under Category 1 (60%)."];
  return { ok: true, result: "CAT2", amount: 100000, why: why.concat(["Category 2: a fee of INR 1 lakh (section 133, Table, item 2)."], extra) };
}
if (typeof module !== "undefined") module.exports = { fastds: fastds };
