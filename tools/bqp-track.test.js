const assert = require("assert");
const T = require("../bqp-track.js");
let n = 0; function t(name, fn) { fn(); n++; }
const HOST = "bharatquantumprospera.com";
t("google referrer", () => { assert.deepStrictEqual(T.classify("https://www.google.com/", "", HOST), { src: "google", q: "" }); });
t("google country domain", () => { assert.strictEqual(T.classify("https://www.google.co.uk/", "", HOST).src, "google"); });
t("gemini before google", () => { assert.strictEqual(T.classify("https://gemini.google.com/app", "", HOST).src, "gemini"); });
t("bing with query", () => { assert.deepStrictEqual(T.classify("https://www.bing.com/search?q=nri+tds+refund", "", HOST), { src: "bing", q: "nri tds refund" }); });
t("chatgpt and perplexity", () => { assert.strictEqual(T.classify("https://chatgpt.com/", "", HOST).src, "chatgpt"); assert.strictEqual(T.classify("https://www.perplexity.ai/search/x", "", HOST).src, "perplexity"); });
t("utm wins", () => { assert.strictEqual(T.classify("https://www.google.com/", "?utm_source=Newsletter", HOST).src, "newsletter"); });
t("internal and empty referrer", () => { assert.strictEqual(T.classify("https://bharatquantumprospera.com/tools.html", "", HOST), null); assert.strictEqual(T.classify("", "", HOST), null); });
t("unknown site keeps host", () => { assert.strictEqual(T.classify("https://example.org/post", "", HOST).src, "example.org"); });
t("slug", () => { assert.strictEqual(T.slug("/"), "home"); assert.strictEqual(T.slug("/book-a-call.html"), "book-a-call"); });
t("ref text", () => {
  assert.strictEqual(T.refText({ src: "google", q: "", lp: "a" }, "a"), "Ref: a | via google");
  assert.strictEqual(T.refText({ src: "bing", q: "nri tax", lp: "a" }, "b"), "Ref: b | via bing | first page: a | search: nri tax");
});
t("whatsapp tagging", () => {
  const out = T.tagWhatsApp("https://wa.me/917801887130?text=Hi%20Durgesh", "Ref: a | via google");
  assert.strictEqual(decodeURIComponent(out.split("text=")[1]), "Hi Durgesh\n\n[Ref: a | via google]");
  assert.ok(/\?text=/.test(T.tagWhatsApp("https://wa.me/917801887130", "Ref: a | via direct")));
});
t("mailto tagging", () => {
  const a = T.tagMailto("mailto:info@bharatquantumprospera.com?subject=Hi&body=Hello", "Ref: a | via google");
  assert.ok(a.indexOf("subject=Hi&body=Hello" + encodeURIComponent("\n\n[Ref: a | via google]")) > -1);
  assert.ok(/\?body=/.test(T.tagMailto("mailto:info@bharatquantumprospera.com", "Ref: a | via direct")));
  assert.ok(/subject=Hi&body=/.test(T.tagMailto("mailto:info@bharatquantumprospera.com?subject=Hi", "Ref: a | via direct")));
});
t("link kinds", () => {
  assert.strictEqual(T.linkKind("https://wa.me/917801887130?text=x"), "whatsapp");
  assert.strictEqual(T.linkKind("mailto:info@bharatquantumprospera.com"), "email");
  assert.strictEqual(T.linkKind("tel:+917801887130"), "phone");
  assert.strictEqual(T.linkKind("book-a-call.html"), "book_call_link");
  assert.strictEqual(T.linkKind("nri-taxation-india-complete-guide.html"), "");
});
t("opt-in zones", () => {
  ["Europe/London", "Europe/Berlin", "Europe/Zurich", "Europe/Dublin", "Atlantic/Reykjavik", "Asia/Nicosia", "Atlantic/Canary"].forEach(z => assert.strictEqual(T.optInZone(z), true, z));
  ["Asia/Kolkata", "Asia/Calcutta", "Asia/Dubai", "America/New_York", "America/Toronto", "Australia/Sydney", "Asia/Singapore", "Atlantic/Bermuda", ""].forEach(z => assert.strictEqual(T.optInZone(z), false, z));
});
console.log("all " + n + " tests passed");
