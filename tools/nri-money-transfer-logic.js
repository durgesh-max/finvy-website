// Sending money between India and the UK, US, Canada, Australia or Europe: what applies (rules as at November 2026).
// India side: FEMA (LRS USD 250,000 per financial year; NRO repatriation USD 1 million per financial year), Form 15CA/15CB
// (Form 145/146 under the Income-tax Act, 2025), TCS on LRS from 1 April 2026, gift rules for the receiver.
// Country side: the main reporting or tax point for someone living there. General information, not advice.
// Inputs:
//   dir: "toIndia" | "fromIndia"
//   country: "UK" | "US" | "CA" | "AU" | "EU"
//   toIndia:   fund: "bank" | "cash"   credit: "ownNRE" | "ownNRO" | "relative" | "nonRelative"
//              amountINR: number       otherGiftsINR: number (other gifts from non-relatives this financial year)
//   fromIndia: who: "nri" | "resident"
//              nri:      source: "NRE" | "FCNR" | "NRO" | "property"   amountUSD: number   nroSoFarUSD: number (already repatriated from NRO this year)
//              resident: purpose: "eduLoan" | "eduSelf" | "medical" | "tour" | "gift" | "investment"
//                        amountINR: number   lrsSoFarINR: number (LRS remittances already made this year)   rate: number (INR per USD)
var LRS_CAP_USD = 250000, NRO_CAP_USD = 1000000, TCS_THRESHOLD = 1000000, GIFT_LIMIT = 50000;

function tcsOnLrs(purpose, amount, soFar) {
  if (purpose === "eduLoan") return { tcs: 0, rule: "Education funded by a loan from a financial institution: no TCS." };
  if (purpose === "tour") return { tcs: Math.round(amount * 0.02), rule: "Overseas tour package: flat 2% on the whole amount, no threshold (from 1 April 2026)." };
  var excess = Math.max(0, soFar + amount - TCS_THRESHOLD) - Math.max(0, soFar - TCS_THRESHOLD);
  if (purpose === "eduSelf" || purpose === "medical")
    return { tcs: Math.round(excess * 0.02), rule: "Education (self-funded) or medical treatment: 2% on the part of your LRS remittances above INR 10 lakh in the financial year (from 1 April 2026)." };
  return { tcs: Math.round(excess * 0.20), rule: "Gift, maintenance, investment or other purposes: 20% on the part of your LRS remittances above INR 10 lakh in the financial year." };
}

var COUNTRY_IN = {   // money arriving in the country from India, and holding Indian accounts
  US: ["If you are a US person and receive more than USD 100,000 in a year as gifts from non-resident aliens (for example, parents in India), report it on Form 3520. It is a reporting form, not a tax, but the late-filing penalty is steep.",
       "Indian bank accounts (NRE, NRO, FCNR) count as foreign accounts: file an FBAR if their combined balance went above USD 10,000 at any time in the year, and Form 8938 if you cross its thresholds (USD 50,000 at year-end or USD 75,000 at any time for a single filer living in the US).",
       "NRE interest is tax-free in India but taxable in the US: show it on your US return."],
  UK: ["UK residents are taxed on worldwide income and gains. The remittance basis ended on 6 April 2025; new arrivals with 10 prior years of non-UK residence may claim the four-year foreign income and gains (FIG) relief.",
       "Bringing your own capital (savings, sale proceeds) into the UK is not itself taxed, but interest, rent, dividends and gains in India must be reported in the UK, with credit under the India-UK tax treaty for Indian tax paid.",
       "NRE interest is tax-free in India but taxable in the UK for a UK resident."],
  CA: ["File Form T1135 if the total cost of your specified foreign property (Indian bank deposits, shares, mutual funds, rented property) was more than CAD 100,000 at any time in the year. Property used mainly for personal use is not included.",
       "Canada taxes residents on worldwide income: report Indian interest (including NRE interest, tax-free in India), rent and gains, with foreign tax credit for Indian tax.",
       "Canada has no gift tax on money you receive from family in India."],
  AU: ["Australia has no gift tax; a genuine gift from family in India is generally not assessable income. Keep evidence (gift letter, the sender's bank statement), because the ATO watches for foreign income disguised as gifts or loans (Taxpayer Alert TA 2021/2).",
       "Australian residents are taxed on worldwide income: declare Indian interest (including NRE interest, tax-free in India), rent and capital gains, with a foreign income tax offset for Indian tax.",
       "Money from a trust is treated differently from a gift: get advice before receiving trust distributions."],
  EU: ["Residents of most European countries are taxed on worldwide income: declare Indian interest (including NRE interest, tax-free in India), rent and gains, and claim credit under the India tax treaty with your country.",
       "Indian financial institutions report accounts of foreign residents under the Common Reporting Standard, so your home tax office may already see your Indian balances.",
       "Large gifts may fall under your country's own gift or inheritance tax on the receiver, usually with family allowances: check the local rules before a big transfer."]
};
var GIFT_IN = {      // the receiver abroad, when parents or family in India send money
  US: [COUNTRY_IN.US[0], "Interest or gains the money later earns are taxable in the US in the usual way."],
  UK: ["The UK does not tax the person receiving a gift. Income or gains the money later earns are taxable in the UK in the usual way."],
  CA: [COUNTRY_IN.CA[2], "Income the money later earns is taxable in Canada in the usual way."],
  AU: [COUNTRY_IN.AU[0]],
  EU: [COUNTRY_IN.EU[2], "Income the money later earns is taxable where you live."]
};
var COUNTRY_OUT = {  // money leaving the country for India
  US: ["From 1 January 2026, a 1% US federal excise tax applies to remittances paid in cash, by money order or cashier's cheque. Transfers paid from a US bank account or a US-issued card are not covered.",
       "Gifts above USD 19,000 to one person in 2026 need a US gift tax return (Form 709). Tax is rarely payable because of the lifetime exemption, but the return is required."],
  UK: ["The UK has no gift tax, but gifts can fall into UK inheritance tax if you die within seven years. The GBP 3,000 annual exemption and regular gifts out of surplus income are exempt.",
       "Sending your own money to India needs no UK form; your bank may ask the source of funds for large transfers."],
  CA: ["Canada has no gift tax and no form for sending your own money to India. Keep records of the source of funds for large transfers.",
       "If you lend or gift money to family who then invest it in Canada, attribution rules can apply; money used in India by family there is not affected."],
  AU: ["Australia has no gift tax and no form for sending your own money to India. Banks report international transfers to AUSTRAC, so keep the reason and the source of funds on record.",
       "Gifts can matter for social security means tests if you receive Centrelink payments."],
  EU: ["Most European countries do not tax the sender on money sent abroad; some have gift taxes that can reach gifts by residents. Check your country's rules for large gifts.",
       "Banks may ask the source of funds for large transfers under anti-money-laundering rules."]
};

function moneyTransfer(i) {
  var e = [];
  if (i.dir !== "toIndia" && i.dir !== "fromIndia") e.push("Choose the direction");
  if (!COUNTRY_IN[i.country]) e.push("Choose your country");
  var amt = i.dir === "fromIndia" && i.who === "nri" ? i.amountUSD : i.amountINR;
  if (typeof amt !== "number" || !isFinite(amt) || amt <= 0) e.push("Enter the amount (more than zero)");
  ["otherGiftsINR", "nroSoFarUSD", "lrsSoFarINR"].forEach(function (k) {
    if (i[k] !== undefined && (typeof i[k] !== "number" || !isFinite(i[k]) || i[k] < 0)) e.push("Amounts already sent must be zero or more");
  });
  if (i.dir === "fromIndia" && i.who === "resident" && i.purpose !== "eduLoan" && (typeof i.rate !== "number" || !(i.rate > 0))) e.push("Enter the exchange rate (INR per USD)");
  if (e.length) return { ok: false, errors: e };

  var india = [], forms = [], limits = [], tax = [], flags = [], tcs = null, verdict;
  if (i.dir === "toIndia") {
    verdict = "Money coming into India: no Indian tax on the transfer itself";
    if (i.credit === "ownNRE") {
      india.push("Only money earned or held abroad can go into an NRE account. NRE balances and interest stay freely repatriable.");
      tax.push("NRE interest is tax-free in India while you are a non-resident (it becomes taxable after you become resident).");
    } else if (i.credit === "ownNRO") {
      india.push("An NRO account can take foreign remittances as well as Indian income.");
      tax.push("NRO interest is taxable in India; banks deduct tax at source, which you can reduce under the tax treaty with a tax residency certificate and Form 10F.");
      limits.push("Taking money back out of NRO later is limited to USD 1 million per financial year, with Form 15CA/15CB.");
    } else if (i.credit === "relative") {
      tax.push("Money received by a relative in India (parent, spouse, sibling, child and the other relatives listed in the Income-tax Act) as a gift is not taxable for them, whatever the amount.");
      india.push("The receiving bank issues a foreign inward remittance certificate or advice; keep it with a short gift note for the records.");
    } else {
      var total = i.amountINR + (i.otherGiftsINR || 0);
      if (total > GIFT_LIMIT) {
        tax.push("Gifts from people who are not relatives are taxable for the receiver if the total in the financial year exceeds INR 50,000; then the whole amount is taxable, not just the excess. This transfer takes the year's total to INR " + total.toLocaleString("en-IN") + ".");
        verdict = "Money coming into India: taxable for the receiver as a gift from a non-relative";
      } else {
        tax.push("Gifts from people who are not relatives are tax-free for the receiver while the year's total stays within INR 50,000 (this brings it to INR " + total.toLocaleString("en-IN") + ").");
      }
    }
    flags = COUNTRY_OUT[i.country].slice();
    if (i.country === "US" && i.fund === "cash") flags.unshift("Paying in cash, by money order or cashier's cheque: expect the 1% US remittance tax on this transfer (about INR " + Math.round(i.amountINR * 0.01).toLocaleString("en-IN") + "). Paying from your US bank account avoids it.");
    if (i.country === "US" && i.fund !== "cash") flags = flags.slice(1).concat(["Paid from a US bank account or card: the 1% US remittance tax does not apply."]);
  } else if (i.who === "nri") {
    if (i.source === "NRE" || i.source === "FCNR") {
      verdict = "Freely repatriable: no USD 1 million limit";
      india.push("NRE and FCNR balances (principal and interest) can be sent abroad freely.");
      forms.push("Form 15CA/15CB is generally not needed for your own NRE or FCNR money, as it is not taxable in India; your bank may ask for a simple declaration.");
    } else {
      var used = (i.nroSoFarUSD || 0) + i.amountUSD;
      verdict = used > NRO_CAP_USD ? "Over the USD 1 million NRO limit for this financial year" : "Allowed within the USD 1 million NRO limit, with Form 15CA/15CB";
      limits.push("NRO balances (including property sale proceeds) can be repatriated up to USD 1 million per financial year (April to March). This request takes you to USD " + used.toLocaleString("en-US") + "." + (used > NRO_CAP_USD ? " The excess needs to wait for the next financial year or needs RBI approval." : ""));
      forms.push("Form 15CA online on the income tax portal and, in most cases, a Chartered Accountant's certificate in Form 15CB confirming tax has been paid. From 1 April 2026 these are Form 145 and Form 146 under the Income-tax Act, 2025.");
      tax.push("Tax on the income behind the money (interest, rent, capital gains) must be paid or deducted at source before the remittance.");
      if (i.source === "property") {
        tax.push("On a property sale the buyer deducts tax at source; a lower deduction certificate can cut this if the actual gain is small.");
        limits.push("If the property was bought with money from abroad or from NRE/FCNR funds, the original foreign-exchange investment (for up to two residential properties) can be repatriated on top; the rest falls within the USD 1 million limit.");
      }
    }
    flags = COUNTRY_IN[i.country].slice();
  } else {
    var t = tcsOnLrs(i.purpose, i.amountINR, i.lrsSoFarINR || 0);
    tcs = t.tcs;
    india.push("Resident individuals send money abroad under the Liberalised Remittance Scheme (LRS), with PAN and Form A2 at the bank.");
    limits.push("LRS limit: USD 250,000 per person per financial year, for all purposes together.");
    if (i.purpose !== "eduLoan") {
      var usd = Math.round((i.amountINR + (i.lrsSoFarINR || 0)) / i.rate);
      if (usd > LRS_CAP_USD) limits.push("At INR " + i.rate + " per USD, this takes your LRS total to about USD " + usd.toLocaleString("en-US") + ", above the USD 250,000 limit.");
    }
    tax.push(t.rule + (tcs ? " TCS on this remittance: INR " + tcs.toLocaleString("en-IN") + ". TCS is an advance tax: you claim it back in your Indian return against your tax, or as a refund." : " TCS on this remittance: nil."));
    if (i.purpose === "gift") tax.push("A gift from a resident parent to a child abroad is not taxable for the child in India.");
    verdict = tcs ? "Allowed under LRS, with TCS of INR " + tcs.toLocaleString("en-IN") : "Allowed under LRS, no TCS on this remittance";
    flags = GIFT_IN[i.country].slice();
  }
  return { ok: true, verdict: verdict, india: india, forms: forms, limits: limits, tax: tax, country: flags, tcs: tcs };
}
if (typeof module !== "undefined") module.exports = { moneyTransfer: moneyTransfer, tcsOnLrs: tcsOnLrs };
