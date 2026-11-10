// FAST-DS 2026 payment timeline (Finance Act 2026, s.135):
// order (Form 2) within one month from the end of the month of declaration;
// pay within two months from the end of the month in which the order is received;
// or within a further two months with simple interest of 1% for every month or part of a month.
function ymd(s) {
  if (!s) return null;
  var m = /^(\d{4})-(\d{2})-(\d{2})$/.exec(s);
  if (!m) return null;
  var d = new Date(Date.UTC(+m[1], +m[2] - 1, +m[3]));
  return d.getUTCMonth() === +m[2] - 1 ? d : null;
}
function endOfMonthAfter(d, k) { return new Date(Date.UTC(d.getUTCFullYear(), d.getUTCMonth() + k + 1, 0)); }
function iso(d) { return d.toISOString().slice(0, 10); }
function monthsOrPart(from, to) {
  // whole months or part of a month from `from` (exclusive) to `to` (inclusive); from is a month-end
  // because `from` is always a month-end, every day of the next calendar month is "one month or part"
  var m = (to.getUTCFullYear() - from.getUTCFullYear()) * 12 + (to.getUTCMonth() - from.getUTCMonth());
  return Math.max(1, m);
}
function fastdsPayment(i) {
  var errors = [];
  var decl = ymd(i.declarationDate), order = ymd(i.orderDate), pay = ymd(i.paymentDate);
  var amount = Number(i.amount);
  if (!decl && !order) errors.push("Enter the declaration date or the date you received Form 2.");
  if (i.declarationDate && !decl) errors.push("Declaration date is not a valid date.");
  if (i.orderDate && !order) errors.push("Form 2 date is not a valid date.");
  if (i.paymentDate && !pay) errors.push("Payment date is not a valid date.");
  if (!(amount > 0)) errors.push("Enter the amount payable shown in Form 2.");
  if (decl && decl > new Date(Date.UTC(2026, 11, 31))) errors.push("Declarations under FAST-DS 2026 can be filed only up to 31 December 2026.");
  if (decl && decl < new Date(Date.UTC(2026, 7, 16))) errors.push("The scheme opened on 16 August 2026.");
  if (decl && order && order < decl) errors.push("Form 2 cannot be dated before the declaration.");
  if (errors.length) return { ok: false, errors: errors };
  var r = { ok: true, steps: [] };
  if (decl) r.orderBy = iso(endOfMonthAfter(decl, 1));
  var base = order || endOfMonthAfter(decl, 1);
  r.orderAssumed = !order;
  r.dueDate = iso(endOfMonthAfter(base, 2));
  r.extendedDate = iso(endOfMonthAfter(base, 4));
  r.interest = 0; r.months = 0; r.total = Math.round(amount);
  if (pay) {
    var due = endOfMonthAfter(base, 2), ext = endOfMonthAfter(base, 4);
    if (pay <= due) r.status = "on time";
    else if (pay <= ext) {
      r.months = monthsOrPart(due, pay);
      r.interest = Math.round(amount * 0.01 * r.months);
      r.total = Math.round(amount) + r.interest;
      r.status = "late, within the extended period";
    } else r.status = "after the extended period";
  }
  return r;
}
if (typeof module !== "undefined") module.exports = { fastdsPayment: fastdsPayment, endOfMonthAfter: endOfMonthAfter };
