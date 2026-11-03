// Residential status of an individual: Income-tax Act 1961 s.6 (FY 2025-26) and Income-tax Act 2025 s.6 (tax year 2026-27 on).
// Inputs:
//   act: "1961" | "2025"
//   days: days in India in the year; days4: days in India in the 4 preceding years
//   citizen, pio: booleans; category: "leaving" | "visiting" | "other"
//   incomeOver15L: total income other than income from foreign sources exceeds INR 15 lakh
//   liableAbroad: liable to tax in another country/territory by reason of domicile, residence or similar criteria
//   nrYears10: number of the 10 preceding years in which the person was a non-resident (0-10)
//   days7: days in India in the 7 preceding years
function residency(i) {
  var A = i.act === "2025";
  var S = A ? {
    a: "section 6(2)(a)", b: "section 6(2)(b)", leave: "section 6(3)", visit: "section 6(4)", visit15: "section 6(5)",
    deemed: "section 6(7)", deemedNot: "section 6(8)", norA1: "section 6(13)(a)(i)", norA2: "section 6(13)(a)(ii)", norB: "section 6(13)(b)", norC: "section 6(13)(c)", yr: "tax year"
  } : {
    a: "section 6(1)(a)", b: "section 6(1)(c)", leave: "Explanation 1(a) to section 6(1)", visit: "Explanation 1(b) to section 6(1)", visit15: "Explanation 1(b) to section 6(1)",
    deemed: "section 6(1A)", deemedNot: "the Explanation to section 6(1A)", norA1: "section 6(6)(a)", norA2: "section 6(6)(a)", norB: "section 6(6)(c)", norC: "section 6(6)(d)", yr: "previous year"
  };
  var errors = [];
  function num(v, lo, hi, name) { if (typeof v !== "number" || !isFinite(v) || v < lo || v > hi || Math.floor(v) !== v) errors.push(name + " must be a whole number from " + lo + " to " + hi); }
  num(i.days, 0, 366, "Days in India this year");
  num(i.days4, 0, 1461, "Days in India in the 4 preceding years");
  num(i.days7, 0, 2557, "Days in India in the 7 preceding years");
  num(i.nrYears10, 0, 10, "Years as non-resident out of the 10 preceding years");
  if (i.category === "leaving" && !i.citizen) errors.push("The 'leaving India for employment or as crew of an Indian ship' rule applies only to citizens of India");
  if (i.category === "visiting" && !i.citizen && !i.pio) errors.push("The 'coming on a visit' rule applies only to citizens of India or persons of Indian origin");
  if (errors.length) return { ok: false, errors: errors };

  var trace = [];
  var resA = i.days >= 182;
  trace.push((resA ? "Met" : "Not met") + ": " + S.a + " (182 days or more in the " + S.yr + "): " + i.days + " days.");
  var resB = false, threshold = 60, bApplies = true;
  if (i.category === "leaving" && i.citizen) {
    bApplies = false;
    trace.push("Not applicable: " + S.b + " (60 days + 365 days) does not apply to a citizen leaving India in the year for employment outside India or as crew of an Indian ship (" + S.leave + ").");
  } else if (i.category === "visiting" && (i.citizen || i.pio)) {
    if (i.incomeOver15L) {
      threshold = 120;
      trace.push("Applies with 120 days instead of 60: income other than foreign-source income exceeds INR 15 lakh for a citizen/person of Indian origin coming on a visit (" + S.visit15 + ").");
    } else {
      bApplies = false;
      trace.push("Not applicable: " + S.b + " does not apply to a citizen or person of Indian origin coming on a visit whose income other than foreign-source income does not exceed INR 15 lakh (" + S.visit + ").");
    }
  }
  if (bApplies) {
    resB = i.days >= threshold && i.days4 >= 365;
    trace.push((resB ? "Met" : "Not met") + ": " + S.b + " (" + threshold + " days or more in the " + S.yr + " and 365 days or more in the 4 preceding years): " + i.days + " days and " + i.days4 + " days.");
  }
  var resident = resA || resB, deemed = false;
  if (!resident) {
    if (i.citizen && i.incomeOver15L && !i.liableAbroad) {
      deemed = true;
      trace.push("Met: " + S.deemed + " deemed residence (citizen, income other than foreign-source income above INR 15 lakh, not liable to tax in any other country or territory by reason of domicile, residence or similar criteria).");
    } else {
      trace.push("Not met: " + S.deemed + " deemed residence (needs citizenship, income other than foreign-source income above INR 15 lakh, and no tax liability abroad by reason of domicile/residence).");
      return { ok: true, status: "NR", label: "Non-resident (NR)", trace: trace };
    }
  } else if (i.citizen && i.incomeOver15L && !i.liableAbroad) {
    trace.push("Not considered: " + S.deemed + " does not apply to an individual who is already resident under the day tests (" + S.deemedNot + ").");
  }
  if (deemed) {
    trace.push("Not ordinarily resident: a citizen deemed resident is not ordinarily resident (" + S.norC + ").");
    return { ok: true, status: "RNOR", label: "Resident but not ordinarily resident (RNOR), as a deemed resident", trace: trace };
  }
  var n1 = i.nrYears10 >= 9, n2 = i.days7 <= 729;
  var n3 = i.category === "visiting" && (i.citizen || i.pio) && i.incomeOver15L && i.days >= 120 && i.days < 182;
  trace.push((n1 ? "Met" : "Not met") + ": " + S.norA1 + " (non-resident in 9 or more of the 10 preceding years): " + i.nrYears10 + " years.");
  trace.push((n2 ? "Met" : "Not met") + ": " + S.norA2 + " (729 days or less in India in the 7 preceding years): " + i.days7 + " days.");
  if (i.category === "visiting" && (i.citizen || i.pio) && i.incomeOver15L) trace.push((n3 ? "Met" : "Not met") + ": " + S.norB + " (citizen/person of Indian origin with income other than foreign-source income above INR 15 lakh, in India 120 days or more but less than 182 days): " + i.days + " days.");
  if (n1 || n2 || n3) return { ok: true, status: "RNOR", label: "Resident but not ordinarily resident (RNOR)", trace: trace };
  return { ok: true, status: "ROR", label: "Resident and ordinarily resident (ROR)", trace: trace };
}

function countDaysInYear(stays, fyStartYear) {
  // stays: [{from:"YYYY-MM-DD", to:"YYYY-MM-DD" or ""}]; counts each calendar date in India once, arrival and departure days included.
  var start = Date.UTC(fyStartYear, 3, 1), end = Date.UTC(fyStartYear + 1, 2, 31), DAY = 86400000, seen = {}, n = 0;
  for (var k = 0; k < stays.length; k++) {
    var s = stays[k]; if (!s.from) continue;
    var p = s.from.split("-"), a = Date.UTC(+p[0], +p[1] - 1, +p[2]);
    var b = end;
    if (s.to) { var q = s.to.split("-"); b = Date.UTC(+q[0], +q[1] - 1, +q[2]); }
    if (b < a) continue;
    for (var t = Math.max(a, start); t <= Math.min(b, end); t += DAY) { if (!seen[t]) { seen[t] = 1; n++; } }
  }
  return n;
}

if (typeof module !== "undefined") module.exports = { residency: residency, countDaysInYear: countDaysInYear };
