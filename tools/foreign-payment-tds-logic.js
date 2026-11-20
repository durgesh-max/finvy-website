/* TDS on payments by an Indian payer to a foreign company: royalty, fees for technical services (FTS), interest, dividend.
   Domestic rate for a foreign company: 20% plus surcharge (2% above INR 1 crore, 5% above INR 10 crore) and 4% cess.
   Treaty rate (Income Tax Department withholding-rate table, viewed 21 Nov 2026) applies flat, without surcharge or cess,
   when the recipient gives a tax residency certificate and Form 10F / Form 41; the lower of the two is used.
   null = the treaty has no separate FTS article (usually taxable in India only if there is a permanent establishment).
   Where a treaty has two rates the general (higher) one is used and the note says when the lower one applies.
   Grossing up: if the payer bears the tax, gross = net / (1 - rate). Estimate only. */
var FPT_TREATY = {
  usa: { name: "United States", royalty: 0.15, fts: 0.15, interest: 0.15, dividend: 0.15, note: "10% for equipment rentals and ancillary services, and for interest to banks; dividends 25% if the holding is under 10%." },
  uk: { name: "United Kingdom", royalty: 0.15, fts: 0.15, interest: 0.15, dividend: 0.10, note: "10% for equipment rentals and ancillary services, and for interest to banks; dividends 15% from property investment vehicles." },
  singapore: { name: "Singapore", royalty: 0.10, fts: 0.10, interest: 0.15, dividend: 0.10, note: "Interest 10% to banks and insurers; dividends 15% if the holding is under 25%." },
  uae: { name: "UAE", royalty: 0.10, fts: null, interest: 0.125, dividend: 0.10, note: "Interest 5% to banks." },
  germany: { name: "Germany", royalty: 0.10, fts: 0.10, interest: 0.10, dividend: 0.10, note: "" },
  netherlands: { name: "Netherlands", royalty: 0.10, fts: 0.10, interest: 0.10, dividend: 0.10, note: "" },
  japan: { name: "Japan", royalty: 0.10, fts: 0.10, interest: 0.10, dividend: 0.10, note: "" },
  france: { name: "France", royalty: 0.10, fts: 0.10, interest: 0.10, dividend: 0.10, note: "" },
  ireland: { name: "Ireland", royalty: 0.10, fts: 0.10, interest: 0.10, dividend: 0.10, note: "" },
  sweden: { name: "Sweden", royalty: 0.10, fts: 0.10, interest: 0.10, dividend: 0.10, note: "" },
  korea: { name: "South Korea", royalty: 0.10, fts: 0.10, interest: 0.10, dividend: 0.15, note: "" },
  australia: { name: "Australia", royalty: 0.15, fts: null, interest: 0.15, dividend: 0.15, note: "Royalties 10% in some cases; technical services can fall within the royalties article." },
  mauritius: { name: "Mauritius", royalty: 0.15, fts: 0.10, interest: 0.075, dividend: 0.05, note: "Dividends 15% if the holding is under 10%." },
  saudi: { name: "Saudi Arabia", royalty: 0.10, fts: null, interest: 0.10, dividend: 0.05, note: "" },
  none: { name: "Other / no treaty", royalty: null, fts: null, interest: null, dividend: null, note: "" }
};
var FPT_TYPES = { royalty: "Royalty", fts: "Fees for technical services", interest: "Interest", dividend: "Dividend" };
function fptSurcharge(amount) { if (amount > 100000000) return 0.05; if (amount > 10000000) return 0.02; return 0; }
function foreignPaymentTds(input) {
  var amount = Number(input.amount), type = String(input.type || ""), country = String(input.country || "none");
  var trc = input.trc !== false && input.trc !== "no", grossUp = input.grossUp === true || input.grossUp === "yes";
  var errors = [];
  if (!(amount > 0)) errors.push("Enter the payment amount.");
  if (!(type in FPT_TYPES)) errors.push("Choose the type of payment.");
  if (!(country in FPT_TREATY)) errors.push("Choose the recipient's country.");
  if (errors.length) return { ok: false, errors: errors };
  var t = FPT_TREATY[country], treaty = country === "none" ? undefined : t[type];
  var domestic = 0.20 * (1 + fptSurcharge(amount)) * 1.04;
  var noArticle = country !== "none" && treaty === null;
  var rate = domestic, basis = "domestic";
  if (trc && country !== "none") {
    if (noArticle) { rate = 0; basis = "no-article"; }
    else if (treaty < domestic) { rate = treaty; basis = "treaty"; }
  }
  var gross = grossUp ? amount / (1 - rate) : amount;
  var tds = gross * rate;
  return { ok: true, domestic: domestic, treaty: treaty === undefined ? null : treaty, rate: rate, basis: basis, noArticle: noArticle,
    gross: Math.round(gross), tds: Math.round(tds), net: Math.round(gross - tds), saving: Math.round(gross * (domestic - rate)),
    note: t.note, countryName: t.name, typeName: FPT_TYPES[type], trc: trc, grossUp: grossUp };
}
if (typeof module !== "undefined") module.exports = { foreignPaymentTds: foreignPaymentTds, FPT_TREATY: FPT_TREATY, FPT_TYPES: FPT_TYPES };
