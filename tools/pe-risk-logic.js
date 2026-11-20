/* Permanent establishment risk screen for a foreign company with activity in India. Each answer adds points to a PE type;
   the result is the highest-risk type and an overall band. Screening only: the actual answer depends on the treaty
   (service PE days, construction PE months), facts and documents. */
var PE_QUESTIONS = [
  { id: "office", type: "Fixed place PE", w: 3, text: "Do you have an office, desk, warehouse, factory or other place in India at your disposal (owned, rented or provided by a group company or client)?" },
  { id: "staffIndia", type: "Fixed place PE", w: 2, text: "Do your own employees work from India regularly (including remote employees on your payroll)?" },
  { id: "contracts", type: "Dependent agent PE", w: 3, text: "Does anyone in India negotiate or sign contracts on your behalf, or play the principal role leading to contracts you conclude without material change?" },
  { id: "agentExclusive", type: "Dependent agent PE", w: 1, text: "Is your Indian agent, distributor or reseller working mainly or exclusively for you?" },
  { id: "serviceDays", type: "Service PE", w: 3, text: "Do your staff or contractors provide services in India for more than about 90 days in any 12-month period (treaty thresholds vary)?" },
  { id: "project", type: "Construction / installation PE", w: 3, text: "Do you run a construction, installation, assembly or supervisory project in India lasting more than about 6 months (treaty thresholds vary)?" },
  { id: "digital", type: "Significant economic presence (domestic law)", w: 1, text: "Do you earn more than INR 2 crore a year from Indian customers or have 3 lakh or more users in India (digital or remote business)?" },
  { id: "noTreaty", type: "Treaty protection", w: 2, text: "Is your company resident in a country with no tax treaty with India, or do you lack a tax residency certificate?" }
];
function peRisk(answers) {
  var scores = {}, total = 0, triggered = [];
  for (var i = 0; i < PE_QUESTIONS.length; i++) {
    var q = PE_QUESTIONS[i];
    if (answers && answers[q.id] === true) {
      scores[q.type] = (scores[q.type] || 0) + q.w;
      total += q.w;
      triggered.push(q.type);
    }
  }
  var top = null, topScore = 0;
  for (var k in scores) { if (scores[k] > topScore) { topScore = scores[k]; top = k; } }
  var band = total === 0 ? "low" : (topScore >= 3 || total >= 5 ? "high" : "medium");
  return { total: total, band: band, topType: top, types: Object.keys(scores) };
}
if (typeof module !== "undefined") module.exports = { peRisk: peRisk, PE_QUESTIONS: PE_QUESTIONS };
