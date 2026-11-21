# -*- coding: utf-8 -*-
"""Batch EZ (21 Nov 2026): Can a foreign company or foreign national buy property or land in India? FEMA rules by
type of buyer. Call-first page.
Demand: sweep 21 Nov 2026 (ac34), all 7 markets: "can a foreign company buy residential property in india", "can foreign
company buy agricultural land in india", "can foreigner own land in india", "can a foreign company own land in india".
Site had pages for NRIs and US citizens / OCIs but none for foreign companies.
Facts (checked 21 Nov 2026; FEMA (Non-debt Instruments) Rules, 2019, Chapter IX as summarised by Taxmann, Lexology, IFLR,
MEA note and Beacon Filing; RBI Master Direction on immovable property):
- A person resident outside India with a branch, office or other place of business in India (not a liaison office) may
  acquire immovable property necessary for or incidental to that activity (rule 26), may mortgage it to an authorised
  dealer bank, and must file Form IPI with the RBI within 90 days of acquisition.
- A liaison office cannot acquire immovable property; it can take premises on lease for up to five years. Leases of up
  to five years are outside the rules for any non-resident.
- A foreign company with no place of business in India cannot buy immovable property directly.
- An Indian subsidiary is an Indian company and is not subject to these restrictions, but FDI policy bars 'real estate
  business' (dealing in land and property for profit) and restricts agriculture.
- Entities from Pakistan, Bangladesh, Sri Lanka, Afghanistan, China, Iran, Nepal, Bhutan (and Hong Kong, Macau, North
  Korea per the RBI direction) need prior RBI approval.
- Foreign nationals of non-Indian origin resident outside India cannot buy immovable property (lease up to five years;
  inheritance from a resident allowed); a foreign national resident in India under FEMA may buy, subject to the
  country list. NRIs and OCIs may buy residential and commercial property, not agricultural land, plantations or
  farmhouses (site NRI page)."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 21 November 2026."
SLUG = "can-foreign-company-or-foreigner-buy-property-land-in-india-fema-rules-branch-subsidiary-lease-2026"

C = contact("who the buyer is (foreign company, its Indian branch or subsidiary, or an individual), the country, the type of property and what it will be used for")
PAGES = [dict(
    slug=SLUG,
    title="Can a Foreign Company or Foreigner Buy Property or Land in India? (2026) FEMA Rules for Branches, Subsidiaries, Liaison Offices and Foreign Nationals",
    em="who can buy, who can only lease, and what to file.",
    kicker="/ Foreign companies &middot; Property &middot; FEMA &middot; Updated 2026-11-21",
    lead=("<strong>A foreign company cannot buy property in India directly.</strong> It can buy only through a presence here. "
          "A <strong>branch office or project office</strong> may buy property that is <strong>necessary for its permitted activity</strong>, and must report the purchase to the RBI in <strong>Form IPI within 90 days</strong>. "
          "A <strong>liaison office cannot buy</strong>; it can lease premises for up to five years. "
          "An <strong>Indian subsidiary</strong> is an Indian company, so it can buy an office, factory or land for its business like any other company. It cannot trade in real estate, and farming and agricultural land are restricted. "
          "A <strong>foreign national living abroad</strong> who is not of Indian origin cannot buy property in India, but can take a lease of up to five years or inherit from a resident. "
          "<strong>NRIs and OCI cardholders</strong> can buy residential and commercial property but not agricultural land. Buyers from certain neighbouring countries need prior RBI approval."),
    sections=[
        ("/ Who can buy what", "By type of buyer.",
         table(["Buyer", "Buy property?", "Conditions"], [
             ["Foreign company with no presence in India", "No", "Lease of up to five years is possible"],
             ["Liaison office", "No", "Lease of up to five years only"],
             ["Branch office or project office", "Yes, for its own permitted activity", "Property must be necessary for or incidental to the activity; Form IPI to the RBI within 90 days; can be mortgaged to an authorised bank"],
             ["Indian subsidiary (even 100% foreign-owned)", "Yes, for its business", "Treated as an Indian company; no dealing in land or property for profit; agricultural land and farming restricted"],
             ["Foreign national living outside India (not of Indian origin)", "No", "Lease of up to five years; can inherit from a person who was resident in India"],
             ["Foreign national resident in India", "Generally yes", "Must be resident under FEMA; citizens of listed countries need RBI approval"],
             ["NRI or OCI cardholder", "Residential and commercial: yes", "No agricultural land, plantation or farmhouse"]])
         + call_box("Buying or leasing property in India as a foreign business", ["Whether to buy through a branch, a subsidiary or simply lease",
                                                                              "FEMA reporting: Form IPI and the bank route for funds",
                                                                              "Stamp duty, registration, GST and TDS on the purchase",
                                                                              "Whether a planned activity counts as real estate business",
                                                                              "Selling later and sending the proceeds abroad"],
                    "the buyer entity and country, the property type and location, how it will be used and how the purchase will be funded.")),
        ("/ Practical points", "Before you sign.",
         ul("<strong>Lease first:</strong> a lease of up to five years needs no FEMA approval and suits most new entrants.",
            "<strong>Subsidiary route:</strong> most foreign groups that want to own premises do it through an Indian subsidiary; see the <a href=\"india-entry-structure-chooser-subsidiary-llp-branch-liaison-eor-foreign-company-2026.html\">India entry structure chooser</a>.",
            "<strong>Branch route:</strong> the branch itself needs RBI approval to exist; see <a href=\"rbi-approval-place-of-business-india-liaison-branch-project-office-form-fnc-2026.html\">RBI approval for a place of business</a>. Sending sale proceeds abroad later needs RBI approval.",
            "<strong>Real estate business:</strong> foreign investment is not allowed in buying and selling land or property for profit; construction-development, and leasing of completed property, are treated differently.",
            "<strong>Agricultural land:</strong> foreign companies and foreign nationals cannot buy it; state land laws add their own limits, even for Indian companies.",
            "<strong>Listed countries:</strong> entities and citizens of Pakistan, Bangladesh, Sri Lanka, Afghanistan, China, Iran, Nepal and Bhutan, among others, need prior RBI approval.",
            "<strong>Tax on purchase:</strong> buyers deduct TDS when buying from an NRI seller; see <a href=\"buying-property-from-nri-no-tan-form-141-from-1-october-2026.html\">buying property from an NRI</a>.")
         + '<p>Related: <a href="can-nri-buy-property-in-india-residential-commercial-fema-payment-home-loan-tds-2026.html">can an NRI buy property in India</a> &middot; <a href="us-citizen-buy-own-property-india-oci-fema-tax-fbar-2026.html">US citizens and OCIs buying property</a> &middot; <a href="branch-office-vs-liaison-vs-wos-india-foreign.html">branch vs liaison vs subsidiary</a> &middot; <a href="can-foreigner-own-100-percent-indian-company.html">can a foreigner own 100% of an Indian company</a>.</p>'
         + sources("Foreign Exchange Management (Non-debt Instruments) Rules, 2019, Chapter IX (acquisition and transfer of immovable property in India), including rule 26 and Form IPI; RBI Master Direction on acquisition and transfer of immovable property; consolidated FDI policy on real estate business; summaries by Taxmann, Lexology, IFLR and the Ministry of External Affairs. Checked 21 November 2026. State stamp, registration and land laws also apply; get the title checked by a lawyer.")),
    ],
    faqs=[("Can a foreign company buy property in India?", "Not directly. A foreign company can buy only through a branch or project office in India, for property needed for its permitted activity, or through an Indian subsidiary, which is treated as an Indian company."),
          ("Can a liaison office buy property in India?", "No. A liaison office cannot acquire immovable property; it can take premises on lease for up to five years."),
          ("What is Form IPI?", "A declaration to the Reserve Bank of India that a branch or other office of a foreign entity must file within 90 days of acquiring immovable property in India."),
          ("Can a foreign company buy agricultural land in India?", "No. Foreign companies and foreign nationals cannot buy agricultural land, and an Indian subsidiary faces foreign investment and state land-law restrictions on agricultural land."),
          ("Can a foreigner own land in India?", "A foreign national of non-Indian origin living outside India cannot buy immovable property, but can lease for up to five years or inherit from a resident. A foreign national resident in India generally can, subject to RBI approval for citizens of certain countries."),
          ("Can BQP help a foreign business buy or lease premises in India?", "Yes. " + C)],
    related=[("india-entry-structure-chooser-subsidiary-llp-branch-liaison-eor-foreign-company-2026.html", "India entry structure chooser"),
             ("rbi-approval-place-of-business-india-liaison-branch-project-office-form-fnc-2026.html", "RBI approval for a place of business"),
             ("can-nri-buy-property-in-india-residential-commercial-fema-payment-home-loan-tds-2026.html", "Can an NRI buy property in India")],
    cta_h="Need premises in India for a foreign business?", cta_b=C,
    keywords="can foreign company buy property in India, can foreigner own land in India, can a foreign company buy residential property in India, foreign company buy agricultural land India, Form IPI RBI, liaison office lease five years, branch office property India FEMA",
    desc="Can a foreign company or foreigner buy property in India (2026)? Not directly: a branch or project office can buy for its activity (Form IPI in 90 days), a liaison office can only lease up to five years, an Indian subsidiary can buy for its business; no agricultural land.",
    howto={"name": "How a foreign business gets premises in India", "description": "Lease or buy through the right entity.", "steps": [
        {"name": "Decide lease or buy", "text": "A lease of up to five years needs no FEMA approval."},
        {"name": "Choose the entity", "text": "Indian subsidiary or approved branch office; a liaison office can only lease."},
        {"name": "Check restrictions", "text": "Real estate business, agricultural land and listed-country approvals."},
        {"name": "Complete the purchase", "text": "Title check, stamp duty, registration and TDS where it applies."},
        {"name": "Report", "text": "Form IPI to the RBI within 90 days for a branch purchase."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch EZ complete")
