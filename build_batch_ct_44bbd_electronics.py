# -*- coding: utf-8 -*-
"""Batch CT (15 Nov 2026): presumptive taxation of non-residents providing services or technology to Indian
electronics manufacturing (section 44BBD of the 1961 Act, inserted by the Finance Act, 2025, from assessment year
2026-27; retained in the Income-tax Act, 2025 among the non-resident presumptive provisions).
Gap: no page on the site; semiconductor page ranks ~6 with foreign chip-company impressions.
Facts (LKS Attorneys analysis, updated 28 Jan 2026; taxguru/taxmann summaries): applies to a non-resident in the
business of providing services or technology in India for setting up an electronics manufacturing facility or in
connection with manufacturing electronic goods; the services/technology must be provided to a resident company
establishing or operating such a facility or a connected facility under a scheme notified by the Central Government,
and the resident must satisfy prescribed conditions; 25% of amounts received/receivable deemed business profits; no
set-off of unabsorbed depreciation or brought-forward losses; effective tax about 9.55% of gross receipts for a foreign
company (35% rate, surcharge, cess). Checked 15 Nov 2026."""
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


CONTACT = ("Email durgesh@bharatquantumprospera.com or WhatsApp +91 78018 87130 with the contract, the Indian customer and the scheme its facility is approved under. "
           "We reply within one working day on whether the presumptive scheme applies, the withholding rate and the Indian return, with a fixed-scope quote.")
SLUG = "section-44bbd-presumptive-tax-non-resident-electronics-semiconductor-services-25-percent-2026"
BOX = (f'<div style="border:1px solid var(--line);border-left:4px solid #C2312A;border-radius:10px;padding:16px 18px;margin:18px 0;background:var(--bg-soft)">'
       f'<p style="margin:0 0 8px;font-weight:600">Supplying equipment know-how or engineers to an Indian fab or electronics plant?</p>'
       f'<p style="margin:0">Whether your fees are taxed at roughly 9-9.5% of gross receipts, as fees for technical services, or not at all under a treaty depends on the contract, the customer&rsquo;s scheme approval and your presence in India. We review it before the first invoice. '
       f'<a href="{wa("Hi Durgesh, we are a foreign company providing services to an Indian electronics manufacturing facility. Does section 44BBD apply?")}" target="_blank" rel="noopener"><strong>WhatsApp CA Durgesh Chavda</strong></a>.</p></div>')

PAGES = [dict(
    slug=SLUG,
    title="Presumptive Tax for Foreign Companies Serving Indian Electronics and Semiconductor Plants (Section 44BBD): 25% Deemed Profit, About 9-9.5% Effective",
    em="tax certainty for overseas equipment, technology and service providers.",
    kicker="/ Foreign companies &middot; Electronics &middot; Semiconductors &middot; Updated 2026-11-15",
    lead=("A <strong>non-resident</strong> that provides <strong>services or technology</strong> to an Indian company <strong>setting up or operating an electronics manufacturing facility</strong> (or a connected facility) under a <strong>scheme notified by the Central Government</strong> is taxed on a presumptive basis: <strong>25% of its gross receipts</strong> is deemed to be its business profit. "
          "For a foreign company that works out to roughly <strong>9.1% to 9.55% of gross receipts</strong> after the 35% corporate rate, surcharge (nil, 2% or 5% depending on income) and 4% cess. The rule was introduced as <strong>section 44BBD</strong> of the 1961 Act by the <strong>Finance Act, 2025</strong> (from assessment year 2026-27) and is carried into the <strong>Income-tax Act, 2025</strong> alongside the other non-resident presumptive provisions. "
          "No expenses are deducted beyond the deemed 25%, and unabsorbed depreciation and past losses cannot be set off. It sits beside the treaty and fees-for-technical-services rules, so the contract still decides which applies."),
    sections=[
        ("/ Who it covers", "Conditions.",
         table(["Condition", "What it means"], [
             ["Non-resident service or technology provider", "Foreign company or other non-resident in the business of providing services or technology in India"],
             ["Purpose", "Setting up an electronics manufacturing facility, or in connection with manufacturing or producing electronic goods, articles or things in India"],
             ["Indian customer", "A resident company establishing or operating the facility, or a connected facility, under a scheme notified by the Central Government"],
             ["Customer conditions", "The resident company must satisfy the conditions prescribed for the scheme"],
             ["Deemed profit", "25% of amounts received or receivable (in India or abroad) for those services or technology"],
             ["Losses", "No set-off of unabsorbed depreciation or brought-forward business losses"]])
         + BOX),
        ("/ The numbers", "Illustration for a foreign company.",
         table(["Item", "Amount"], [
             ["Gross receipts from the Indian customer", "INR 10 crore"],
             ["Deemed profit at 25%", "INR 2.5 crore"],
             ["Tax at 35% plus 2% surcharge (income between INR 1 crore and 10 crore) and 4% cess (about 37.13%)", "About INR 92.8 lakh"],
             ["Effective rate on gross receipts", "About 9.3% (about 9.55% where the 5% surcharge applies)"]])
         + '<p>Compare this with fees for technical services taxed at 20% of gross under Indian law (or a 10-15% treaty rate), or business profits taxed at 35% on net income where there is a permanent establishment. See <a href="fees-for-technical-services-fts-taxability-india-make-available-treaty-withholding-2026.html">fees for technical services</a> and <a href="permanent-establishment-india-meaning-types-risk-tax-foreign-company-2026.html">permanent establishment</a>.</p>'),
        ("/ What to check", "Before signing and invoicing.",
         ul("Confirm the Indian customer's facility is approved under a notified scheme (for example the semiconductor and display fab or electronics component schemes) and meets the prescribed conditions; see <a href=\"india-semiconductor-ism-pli-foreign-chip-company.html\">India's semiconductor incentives for foreign chip companies</a>.",
            "Map each service and technology fee in the contract: installation, commissioning, training, technical assistance, software and know-how licences are often bundled.",
            "Agree the withholding rate with the customer; the Indian payer withholds under section 393(2) of the Income-tax Act, 2025 (formerly section 195), and a lower deduction certificate can align withholding with the presumptive tax.",
            "Compare the treaty position: if the treaty taxes the fee lower or not at all (for example a make-available clause), check which route is available and keep the tax residency certificate and Form 41.",
            "File an Indian income-tax return for the receipts, even under the presumptive scheme.")
         + '<p>Related: <a href="income-tax-act-2025-section-195-now-393-what-changed-nri-foreign.html">section 195 is now 393(2)</a> &middot; <a href="best-ca-pli-scheme-application-foreign-manufacturer.html">PLI applications for foreign manufacturers</a> &middot; <a href="india-services-for-foreign-companies-complete-list.html">services for foreign companies</a>.</p>'
         + f'<p><strong>Sources:</strong> Income-tax Act, 1961, section 44BBD (Finance Act, 2025, from assessment year 2026-27) and its counterpart in the Income-tax Act, 2025; LKS Attorneys, &ldquo;Union Budget 2025: navigating the new presumptive tax landscape for non-residents&rdquo; (updated 28 January 2026); summaries by Taxmann and TaxGuru. Checked 15 November 2026. Open questions remain on mixed contracts and the interaction with treaties. <em>{UPDATED}</em> General information, not advice for your contract.</p>'),
    ],
    faqs=[("What is section 44BBD?", "A presumptive tax rule for non-residents providing services or technology to a resident company setting up or operating an electronics manufacturing facility under a notified scheme: 25% of gross receipts is deemed profit. It was inserted by the Finance Act, 2025 from assessment year 2026-27 and carried into the Income-tax Act, 2025."),
          ("What is the effective tax rate under section 44BBD?", "About 9.1% to 9.55% of gross receipts for a foreign company: 25% deemed profit taxed at 35% plus surcharge (nil, 2% or 5% depending on income) and 4% cess."),
          ("Does it apply to any electronics customer in India?", "No. The customer must be a resident company establishing or operating an electronics manufacturing facility, or a connected facility, under a scheme notified by the Central Government and meeting the prescribed conditions."),
          ("Can losses or depreciation be set off?", "No. Unabsorbed depreciation and brought-forward business losses cannot be set off against the presumptive income."),
          ("How does it interact with tax treaties?", "Non-residents can generally rely on a treaty where it is more beneficial, for example where fees are not taxable as fees for technical services under a make-available clause. The contract and the customer's scheme status decide which route applies."),
          ("Can BQP advise on our India contract?", "Yes. " + CONTACT)],
    related=[("india-semiconductor-ism-pli-foreign-chip-company.html", "Semiconductor incentives for foreign companies"), ("fees-for-technical-services-fts-taxability-india-make-available-treaty-withholding-2026.html", "Fees for technical services"),
             ("permanent-establishment-india-meaning-types-risk-tax-foreign-company-2026.html", "Permanent establishment")],
    cta_h="Serving an Indian electronics or semiconductor plant?", cta_b=CONTACT,
    keywords="section 44BBD, presumptive tax non-resident electronics manufacturing, semiconductor fab foreign supplier tax India, 25% deemed profit non-resident services technology, 9.55% effective tax electronics, 25% deemed profit electronics services, Finance Act 2025 presumptive scheme non-resident, India semiconductor foreign company tax",
    desc="Section 44BBD (Finance Act 2025, carried into the Income-tax Act 2025): non-residents providing services or technology to Indian electronics manufacturing facilities under a notified scheme are taxed on 25% of gross receipts, about 9.1-9.55% effective for a foreign company; conditions, illustration, treaty and withholding checks.",
    howto={"name": "How a foreign supplier checks the electronics presumptive tax scheme", "description": "Steps before invoicing an Indian electronics facility.", "steps": [
        {"name": "Check the customer's scheme status", "text": "Confirm the facility is under a notified scheme and meets prescribed conditions."},
        {"name": "Classify the fees", "text": "Separate services, technology, equipment and licence components in the contract."},
        {"name": "Compare routes", "text": "Compare presumptive tax with treaty and fees-for-technical-services treatment."},
        {"name": "Align withholding", "text": "Agree the withholding rate with the payer; use a lower deduction certificate if needed."},
        {"name": "File in India", "text": "File the Indian return reporting the receipts under the scheme."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch CT complete")
