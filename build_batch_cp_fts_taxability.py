# -*- coding: utf-8 -*-
"""Batch CP (15 Nov 2026): fees for technical services (sweep-4 demand: "fees for technical services taxability in india",
"fees for technical services definition", "withholding tax india", seen in all 7 markets).
Facts: FTS under Indian law = consideration for managerial, technical or consultancy services, excluding construction,
assembly, mining or like projects and salary (1961 Act Explanation 2 to s.9(1)(vii), carried into the Income-tax Act,
2025); FTS payable by a resident is deemed to arise in India (unless for a business or source outside India), whether or
not the non-resident rendered the services in India or has a presence here (2010 Explanation); domestic rate for a
non-resident without a PE: 20% on the gross amount plus surcharge and cess; treaties usually cap at 10-15%; the India-US,
India-UK, India-Singapore and India-Canada treaties tax technical services only if they 'make available' technical
knowledge, skill or know-how that lets the recipient apply it independently; the India-Australia treaty has no separate
FTS article; India-Germany caps FTS at 10%; services outside the treaty article are business profits, taxable only with
a PE. Payer withholds under section 393(2) (formerly 195); treaty claims need TRC, Form 41 (formerly 10F) and PAN; remittance
forms 145/146; if the payer bears the tax, the payment is grossed up. Sources: site DTAA pages; Income-tax Act; checked 15 Nov 2026."""
from urllib.parse import quote
from build_lib import page, write_page

UPDATED = "Last updated: 15 November 2026."


def wa(t):
    return "https://wa.me/917801887130?text=" + quote(t)


def ul(*x):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in x) + "</ul>"


def table(head, rows):
    return ("<table><thead><tr>" + "".join(f"<th>{h}</th>" for h in head) + "</tr></thead><tbody>"
            + "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows) + "</tbody></table>")


CONTACT = ("Email info@bharatquantumprospera.com or WhatsApp +91 78018 87130 with the contract, a description of the services and the supplier's country. "
           "We reply within one working day with the withholding rate, treaty position and documents, with a fixed-scope quote.")
SLUG = "fees-for-technical-services-fts-taxability-india-make-available-treaty-withholding-2026"
BOX = (f'<div style="border:1px solid var(--line);border-left:4px solid #C2312A;border-radius:10px;padding:16px 18px;margin:18px 0;background:var(--bg-soft)">'
       f'<p style="margin:0 0 8px;font-weight:600">The contract wording often decides the tax.</p>'
       f'<p style="margin:0">Whether a service "makes available" know-how, or is plain business income, depends on what is delivered. A review before signing (and before the first payment) avoids withholding at 20% when the treaty may allow nil. '
       f'<a href="{wa("Hi Durgesh, we are paying a foreign company for technical services. Is it taxable in India and what should we withhold?")}" target="_blank" rel="noopener"><strong>WhatsApp CA Durgesh Chavda</strong></a>.</p></div>')

PAGES = [dict(
    slug=SLUG,
    title="Fees for Technical Services (FTS) in India (2026): Definition, When Payments to Foreign Companies Are Taxable, the 'Make Available' Test and Withholding",
    em="taxable in India even if the work is done abroad, unless a treaty says otherwise.",
    kicker="/ International tax &middot; Withholding &middot; FTS &middot; Updated 2026-11-15",
    lead=("<strong>Fees for technical services (FTS)</strong> means payment for <strong>managerial, technical or consultancy services</strong>, other than construction, assembly or mining projects and salary. When an Indian business pays FTS to a foreign company, the income is <strong>treated as arising in India even if the services are rendered entirely outside India</strong> and the foreign company has no presence here. "
          "Under Indian law it is taxed at <strong>20% on the gross amount</strong> plus surcharge and cess, and the Indian payer must withhold tax under <strong>section 393(2) of the Income-tax Act, 2025</strong> (formerly section 195). "
          "Tax treaties usually cut this to <strong>10-15%</strong>, and some treaties (with the <strong>US, UK, Singapore and Canada</strong>) tax technical services only if they <strong>make available</strong> know-how that the Indian buyer can apply on its own; otherwise the payment is business profit, taxable in India only if the supplier has a permanent establishment here."),
    sections=[
        ("/ Is it FTS, and is it taxable?", "Three questions.",
         table(["Question", "If yes", "If no"], [
             ["Is it a managerial, technical or consultancy service (not construction/mining or salary)?", "Domestic FTS: taxable in India at 20% gross", "Check royalty or business-profits rules instead"],
             ["Does the supplier's treaty have an FTS article?", "Treaty rate applies (it depends on the treaty) if lower and documents are given", "No separate FTS article: check the royalty and business-profits articles (for example India-Australia)"],
             ["Does the treaty require the service to 'make available' know-how (US, UK, Singapore, Canada)?", "Taxable only if technical knowledge or skill is transferred so you can use it independently (for example, training your team)", "Routine services that do not transfer know-how fall outside FTS: business profits, taxable only with a PE"]])
         + BOX),
        ("/ How the Indian payer withholds", "Process and documents.",
         ul("Withhold under section 393(2) of the Income-tax Act, 2025 at the lower of the Act rate (20% plus surcharge and cess) and the treaty rate.",
            "For the treaty rate, collect the supplier's tax residency certificate, Form 41 (formerly 10F) and PAN; keep a no-PE declaration where relevant.",
            "If you agree to bear the tax, the payment is grossed up, so the tax cost rises.",
            "Deposit the tax, file the quarterly statement (Form 144) and certify the remittance on Forms 145/146 (formerly 15CA/15CB).",
            "GST is separate: imported services are taxed under reverse charge; see <a href=\"gst-reverse-charge-import-of-services-india-rcm-self-invoice-itc-2026.html\">RCM on import of services</a>.")
         + table(["Supplier's country", "FTS position under the treaty"], [
             ["United States", "'Fees for included services' with a make-available test; see <a href=\"india-us-tax-treaty-dtaa.html\">India-US treaty</a>"],
             ["United Kingdom", "Make-available test; see <a href=\"india-uk-tax-treaty-dtaa.html\">India-UK treaty</a>"],
             ["Singapore", "Make-available test; see <a href=\"india-singapore-tax-treaty-dtaa.html\">India-Singapore treaty</a>"],
             ["Canada", "Make-available test; see <a href=\"india-canada-dtaa-tax-treaty-nri-rates-capital-gains-foreign-tax-credit-2026.html\">India-Canada treaty</a>"],
             ["Germany", "FTS capped at 10%; see <a href=\"india-germany-dtaa-tax-treaty-nri-company-rates-10-percent-2026.html\">India-Germany treaty</a>"],
             ["Australia", "No separate FTS article; technical services fall within the royalty article only where they make know-how available; see <a href=\"india-australia-dtaa-tax-treaty-nri-rates-capital-gains-fito-2026.html\">India-Australia treaty</a>"]])
         + '<p>Related: <a href="income-tax-act-2025-section-195-now-393-what-changed-nri-foreign.html">section 195 is now 393(2)</a> &middot; <a href="permanent-establishment-india-meaning-types-risk-tax-foreign-company-2026.html">permanent establishment</a> &middot; <a href="significant-economic-presence-foreign-saas-app-company-india-2-crore-3-lakh-users-2026.html">foreign SaaS and SEP</a>.</p>'
         + f'<p><strong>Sources:</strong> Income-tax Act, 1961, section 9(1)(vii) and Explanation 2, and section 115A (carried into the Income-tax Act, 2025); Income-tax Act, 2025, section 393(2); India&rsquo;s tax treaties with the US, UK, Singapore, Canada, Germany and Australia. <em>{UPDATED}</em> General information, not advice for your contract.</p>'),
    ],
    faqs=[("What are fees for technical services under Indian tax law?", "Consideration for managerial, technical or consultancy services, excluding construction, assembly, mining or similar projects and income taxed as salary."),
          ("Is FTS paid to a foreign company taxable in India if the work is done abroad?", "Under Indian law, yes: FTS payable by an Indian business is treated as arising in India whether or not the services were rendered in India. A tax treaty may reduce or remove the tax."),
          ("What is the tax rate on FTS paid to non-residents?", "20% on the gross amount plus surcharge and cess under Indian law; treaties commonly cap it at 10-15%."),
          ("What does 'make available' mean?", "Under treaties such as India-US, India-UK, India-Singapore and India-Canada, technical services are taxable as FTS only if they transfer technical knowledge, skill or know-how that lets the recipient apply it independently. Services that do not, are business profits taxable only with a PE in India."),
          ("Which documents does the Indian payer need for the treaty rate?", "The supplier's tax residency certificate, Form 41 (formerly 10F) and PAN, plus the remittance forms 145/146 (formerly 15CA/15CB)."),
          ("Can BQP review our foreign service contracts?", "Yes. " + CONTACT)],
    related=[("income-tax-act-2025-section-195-now-393-what-changed-nri-foreign.html", "Section 195 is now 393(2)"), ("gst-reverse-charge-import-of-services-india-rcm-self-invoice-itc-2026.html", "GST on imported services"),
             ("india-us-tax-treaty-dtaa.html", "India-US tax treaty")],
    cta_h="Paying a foreign company for services?", cta_b=CONTACT,
    keywords="fees for technical services taxability in India, fees for technical services definition, FTS India non resident, make available clause India US treaty, withholding tax India foreign company, section 393 TDS FTS, FTS 20% section 115A, technical services foreign company India tax",
    desc="Fees for technical services (FTS) in India in 2026: definition, why FTS paid to a foreign company is taxable in India even for work done abroad, 20% Act rate vs 10-15% treaty rates, the 'make available' test (US, UK, Singapore, Canada), and withholding under section 393(2).",
    howto={"name": "How to decide withholding on a payment to a foreign service provider", "description": "Steps for Indian payers.", "steps": [
        {"name": "Classify the service", "text": "Managerial, technical or consultancy service (FTS), royalty, or plain business income."},
        {"name": "Check the treaty", "text": "FTS article, rate and whether a make-available test applies; if no FTS article, check PE."},
        {"name": "Collect documents", "text": "TRC, Form 41, PAN and, where relevant, a no-PE declaration."},
        {"name": "Withhold and report", "text": "Withhold at the lower of Act and treaty rate, file Form 144 and Forms 145/146."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch CP complete")
