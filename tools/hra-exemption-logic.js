/* HRA exemption estimate (Income-tax Act, 1961 section 10(13A) / Income-tax Act, 2025 with rule 279 of the Income-tax
   Rules, 2026). Exempt HRA = least of (a) actual HRA received, (b) rent paid minus 10% of salary, (c) 50% of salary in
   the eight listed cities from 2026-27 (Mumbai, Delhi, Kolkata, Chennai, Bengaluru, Hyderabad, Pune, Ahmedabad) or 40%
   elsewhere. Salary = basic + DA forming part of retirement benefits + turnover-based commission, for the period the
   house was rented. Old regime only: in the new regime HRA is fully taxable. Annual figures. Estimate only. */
function hraExemption(input) {
  var basic = Number(input.basic || 0), da = Number(input.da || 0), comm = Number(input.commission || 0),
      hra = Number(input.hra || 0), rent = Number(input.rent || 0);
  var metro = input.metro === true || input.metro === "yes";
  var regime = input.regime === "new" ? "new" : "old";
  var errors = [];
  [basic, da, comm, hra, rent].forEach(function (v) { if (isNaN(v) || v < 0) errors.push("Amounts cannot be negative."); });
  if (errors.length) return { ok: false, errors: errors.slice(0, 1) };
  if (basic <= 0) return { ok: false, errors: ["Enter your basic salary for the year."] };
  if (hra <= 0) return { ok: false, errors: ["Enter the HRA you received for the year."] };
  var salary = basic + da + comm;
  var a = hra, b = Math.max(0, rent - 0.10 * salary), c = (metro ? 0.50 : 0.40) * salary;
  var exempt = regime === "new" ? 0 : Math.min(a, b, c);
  var limit = a <= b && a <= c ? "actual" : (b <= c ? "rent" : "salary");
  return { ok: true, regime: regime, salary: Math.round(salary), actual: Math.round(a), rentLess10: Math.round(b),
           pctSalary: Math.round(c), pct: metro ? 50 : 40, exempt: Math.round(exempt), taxable: Math.round(hra - exempt),
           limit: limit, rentForFull: Math.round(Math.min(hra, c) + 0.10 * salary) };
}
if (typeof module !== "undefined") module.exports = { hraExemption: hraExemption };
