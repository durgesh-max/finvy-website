/* India entry structure chooser for foreign companies. Inputs (strings): goal = "test" | "sell" | "build" | "project";
   revenue = "yes" | "no" (will the India presence earn income from Indian customers?); staff = "0" | "1-5" | "6+";
   sector = "open" | "restricted" (100% automatic-route sector or not); duration = "short" | "long".
   Returns a primary recommendation and alternatives with reasons. Screening only. */
function indiaEntry(i) {
  var goal = i.goal, revenue = i.revenue, staff = i.staff, sector = i.sector, duration = i.duration;
  var errors = [];
  if (["test", "sell", "build", "project"].indexOf(goal) < 0) errors.push("Choose what you want to do in India.");
  if (["yes", "no"].indexOf(revenue) < 0) errors.push("Say whether the India presence will earn income.");
  if (["0", "1-5", "6+"].indexOf(staff) < 0) errors.push("Choose the number of people in India.");
  if (["open", "restricted"].indexOf(sector) < 0) errors.push("Choose the sector type.");
  if (["short", "long"].indexOf(duration) < 0) errors.push("Choose the time horizon.");
  if (errors.length) return { ok: false, errors: errors };
  var primary, alts = [];
  if (goal === "project") { primary = "Project office"; alts = ["Private limited subsidiary", "Contractual arrangement with an Indian partner"]; }
  else if (goal === "test" && revenue === "no") {
    primary = staff === "0" ? "Contractors or distributor, no entity yet" : (staff === "1-5" ? "Employer of record" : "Liaison office");
    alts = staff === "0" ? ["Employer of record for a first hire", "Liaison office"] : ["Liaison office (no income allowed)", "Private limited subsidiary"];
  }
  else if (sector === "restricted") { primary = "Private limited subsidiary (with approval where required)"; alts = ["Joint venture with an Indian partner", "Branch office (RBI approval)"]; }
  else if (goal === "sell" && staff === "0") { primary = "Distributor or licensee, then a subsidiary"; alts = ["Private limited subsidiary", "Employer of record for local sales staff"]; }
  else if (staff === "1-5" && duration === "short") { primary = "Employer of record"; alts = ["Private limited subsidiary", "Branch office"]; }
  else { primary = "Private limited subsidiary"; alts = ["LLP (services, 100% automatic sectors)", "Branch office (RBI approval)"]; }
  return { ok: true, primary: primary, alternatives: alts };
}
if (typeof module !== "undefined") module.exports = { indiaEntry: indiaEntry };
