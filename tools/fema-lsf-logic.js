// FEMA late submission fee (LSF) estimator. RBI A.P. (DIR Series) Circular No. 16 of 30 September 2022:
// returns that capture flows: INR 7,500 + 0.025% x A x n; returns that do not: INR 7,500 flat.
// n = years of delay, rounded up to the nearest month, to two decimals. Cap 100% of A. Rounded up to the nearest INR 100.
// LSF is available for three years from the due date; after that the delay goes to compounding.
var LSF_FORMS = {
  fcgpr: { name: "FC-GPR (shares issued to a non-resident)", flow: true },
  fctrs: { name: "FC-TRS (transfer of shares)", flow: true },
  di: { name: "Form DI (downstream investment)", flow: true },
  cn: { name: "Form CN (convertible notes)", flow: true },
  esop: { name: "Form ESOP", flow: true },
  llp: { name: "Form LLP(I) or LLP(II)", flow: true },
  invi: { name: "Form InVi", flow: true },
  fc: { name: "Form FC (overseas investment or disinvestment)", flow: true },
  ecb2: { name: "Form ECB 2", flow: true },
  fla: { name: "FLA return", flow: false },
  apr: { name: "Annual Performance Report (overseas investment)", flow: false },
  opi: { name: "Form OPI", flow: false },
  ecb1: { name: "Form ECB 1", flow: false }
};

function lsfParse(s) {
  var m = /^(\d{4})-(\d{2})-(\d{2})$/.exec(String(s || ""));
  if (!m) return null;
  var y = +m[1], mo = +m[2], d = +m[3];
  var dt = new Date(Date.UTC(y, mo - 1, d));
  if (dt.getUTCFullYear() !== y || dt.getUTCMonth() !== mo - 1 || dt.getUTCDate() !== d) return null;
  return { y: y, m: mo, d: d, t: dt.getTime() };
}

function femaLsf(input) {
  var errors = [];
  var form = LSF_FORMS[input.form];
  if (!form) errors.push("Choose the filing.");
  var due = lsfParse(input.due), filed = lsfParse(input.filed);
  if (!due) errors.push("Enter the due date.");
  if (!filed) errors.push("Enter the date you will file.");
  var amount = Number(input.amount);
  if (form && form.flow && !(amount > 0)) errors.push("Enter the amount reported in the form.");
  if (errors.length) return { ok: false, errors: errors };
  if (filed.t <= due.t) return { ok: true, late: false, formName: form.name, flow: form.flow };
  var months = (filed.y * 12 + filed.m) - (due.y * 12 + due.m);
  if (filed.d > due.d) months += 1;
  if (months < 1) months = 1;
  var limit = Date.UTC(due.y + 3, due.m - 1, due.d);
  var out = { ok: true, late: true, formName: form.name, flow: form.flow, months: months, n: Math.round(months / 12 * 100) / 100 };
  if (filed.t > limit) { out.available = false; return out; }
  out.available = true;
  if (!form.flow) { out.fee = 7500; out.capped = false; out.variable = 0; return out; }
  var variable = 0.00025 * amount * out.n;
  var raw = 7500 + variable;
  out.variable = variable;
  out.capped = raw > amount;
  if (out.capped) raw = amount;
  out.fee = Math.ceil(raw / 100 - 1e-9) * 100;
  out.amount = amount;
  return out;
}

if (typeof module !== "undefined") module.exports = { femaLsf: femaLsf, LSF_FORMS: LSF_FORMS };
