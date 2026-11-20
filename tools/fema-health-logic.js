/* FEMA health check for a foreign-owned Indian company. Each question is answered yes (compliant), no (gap) or na.
   Returns the gaps with the usual fix route. Screening only. */
var FEMA_CHECKS = [
  { id: "allot60", text: "Were shares allotted within 60 days of receiving each foreign remittance (or the money refunded within 15 days after that)?", fix: "Unallotted funds beyond 60 days are a contravention; regularise through compounding with the RBI." , route: "compounding" },
  { id: "fcgpr", text: "Was Form FC-GPR filed on FIRMS within 30 days of every allotment to a foreign investor?", fix: "File now; delays within three years of the due date are usually settled with a late submission fee, beyond that through compounding.", route: "lsf" },
  { id: "valuation", text: "Is there a fair-value report (CA, SEBI merchant banker or cost accountant) for every issue or transfer involving a non-resident?", fix: "Pricing without a valid report is a contravention; obtain the position in writing and regularise, usually by compounding.", route: "compounding" },
  { id: "fctrs", text: "Was Form FC-TRS filed within 60 days for every share transfer between a resident and a non-resident?", fix: "File now; late submission fee within three years of the due date, otherwise compounding.", route: "lsf" },
  { id: "fla", text: "Has the annual FLA return been filed by 15 July every year since the first foreign investment?", fix: "File the missed returns; follow the bank or RBI direction on late filing (late submission fee or compounding).", route: "lsf" },
  { id: "di", text: "If the company invested in another Indian company or LLP, was Form DI filed within 30 days?", fix: "File now; late submission fee or compounding depending on the delay.", route: "lsf" },
  { id: "ecb", text: "For any loan from a foreign lender, was an LRN obtained before drawdown and are ECB 2 returns filed?", fix: "Stop further drawdowns, obtain the LRN and file pending returns; delays are settled by late submission fee or compounding.", route: "lsf" },
  { id: "sector", text: "Was the sector cap, approval route and land-border (Press Note 3) position checked before each foreign investment?", fix: "Investment without a required approval is a serious contravention; take advice before any further investment.", route: "approval" }
];
function femaHealth(answers) {
  var gaps = [], answered = 0;
  for (var i = 0; i < FEMA_CHECKS.length; i++) {
    var c = FEMA_CHECKS[i], a = answers ? answers[c.id] : undefined;
    if (a === "yes" || a === "no") answered++;
    if (a === "no") gaps.push({ id: c.id, fix: c.fix, route: c.route });
  }
  var serious = gaps.some(function (g) { return g.route !== "lsf"; });
  var status = gaps.length === 0 ? (answered === 0 ? "unanswered" : "clean") : (serious ? "serious" : "fixable");
  return { gaps: gaps, count: gaps.length, status: status, answered: answered };
}
if (typeof module !== "undefined") module.exports = { femaHealth: femaHealth, FEMA_CHECKS: FEMA_CHECKS };
