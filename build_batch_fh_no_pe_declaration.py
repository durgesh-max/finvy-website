# -*- coding: utf-8 -*-
"""Batch FH (21 Nov 2026): No-PE declaration for India - what it is, sample wording, and the vendor pack an Indian
customer asks a foreign company for (TRC, Form 41, PAN details). Call-first page for foreign vendors and Indian payers.
Demand: sweep 21 Nov 2026 (ac42), all 7 markets: "no permanent establishment declaration india", "no pe declaration
india format", "no pe declaration india template", "no pe declaration india sample", "why no pe certificate is required".
The site mentioned the declaration on treaty and remittance pages but had no page or sample.
Facts (checked 21 Nov 2026):
- Treaty benefit needs a tax residency certificate and the prescribed particulars, now in Form 41 (formerly Form 10F),
  filed electronically (Income Tax Department Form 41 FAQs; India Briefing Form 41 guide; Taxmann; site form pages).
- The no-PE declaration is not a government form. It is a self-declaration the Indian payer relies on when deciding
  withholding under section 393(2) (formerly section 195): business profits of a treaty resident are taxable in India
  only through a permanent establishment, and reduced treaty rates on royalty and technical service fees do not apply
  to income connected with one. Practitioner checklists list TRC, Form 41, PAN or alternative particulars and a no-PE
  declaration, with fresh copies each year.
- The payer remains liable as a deductor in default if tax was wrongly not withheld; declarations therefore carry an
  indemnity.
- Return filing: a non-resident who relies on a treaty rate lower than the domestic rate generally has to file an
  Indian return; the filing exemption applies where tax was withheld at the full domestic rate on the specified income.
The sample wording on the page is original, general text, not copied from any source."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 21 November 2026."
SLUG = "no-pe-declaration-india-format-sample-foreign-vendor-trc-form-41-10f-what-indian-customers-ask-for-2026"

C = contact("the foreign company's country, what it supplies to India, the Indian customer's request, and whether any staff, agents or projects are in India")
SAMPLE = ('<div style="border:1px solid var(--line);border-radius:10px;padding:16px 18px;margin:14px 0;background:var(--bg-soft);font-size:14.5px;line-height:1.6">'
          '<p style="margin:0 0 8px"><strong>[On the foreign company&rsquo;s letterhead]</strong></p>'
          '<p style="margin:0 0 8px">To: [Indian customer name and address]<br/>Date: [date]</p>'
          '<p style="margin:0 0 8px"><strong>Declaration for the financial year 1 April 20__ to 31 March 20__</strong></p>'
          '<p style="margin:0 0 8px">We, [company name], incorporated in [country], with registered office at [address] and tax identification number [number], declare that:</p>'
          '<ol style="margin:0 0 8px 18px;padding:0">'
          '<li>We are a tax resident of [country] under the tax treaty between India and [country]. Our tax residency certificate for the period is enclosed, and we have filed Form 41 on the Indian income-tax portal.</li>'
          '<li>We do not have a permanent establishment, fixed base or place of business in India within the meaning of that treaty, and the income you pay us is not connected with any such establishment.</li>'
          '<li>We are the beneficial owner of the income, and we are entitled to the benefits of the treaty.</li>'
          '<li>Our arrangements with you are for commercial reasons and not mainly to obtain a treaty benefit.</li>'
          '<li>We will tell you promptly if any of this changes during the year.</li>'
          '<li>If any statement here is incorrect, we will make good tax, interest and penalty that you have to pay as a result.</li>'
          '</ol>'
          '<p style="margin:0">For [company name]<br/>[Name, designation, signature of authorised signatory]</p></div>'
          '<p><em>Sample wording only. Sign it only if every statement is true for your company; adapt it to the treaty and contract.</em></p>')

PAGES = [dict(
    slug=SLUG,
    title="No-PE Declaration for India (2026): Format, Sample Wording and the Documents an Indian Customer Asks a Foreign Vendor For - TRC, Form 41 (Form 10F) and PAN",
    em="what to sign, what to send, and when not to sign.",
    kicker="/ Foreign companies &middot; Treaty benefits &middot; Withholding tax &middot; Updated 2026-11-21",
    lead=("<strong>A no-PE declaration is a signed statement by a foreign company that it has no permanent establishment in India.</strong> "
          "It is not a government form. Indian customers ask for it before paying a foreign vendor, because they must decide whether to withhold Indian tax, and they are liable if they get it wrong. "
          "It usually travels with two other documents: a <strong>tax residency certificate</strong> from the vendor&rsquo;s home country and <strong>Form 41</strong> (formerly Form 10F), which the vendor files online in India. "
          "Together these let the customer apply the tax treaty: <strong>no Indian tax on business income</strong> without a permanent establishment, and the <strong>lower treaty rate</strong> on royalties and technical service fees. "
          "The declaration is normally given once for each Indian financial year, April to March. "
          "<strong>Do not sign it as a formality.</strong> If you have staff, agents, a project site or long service visits in India, check first whether a permanent establishment exists."),
    sections=[
        ("/ The vendor pack", "What an Indian customer asks for, and why.",
         table(["Document", "Who issues it", "Why the customer needs it"], [
             ["Tax residency certificate (TRC)", "The tax authority of the vendor&rsquo;s country", "Required by Indian law before any treaty benefit is given"],
             ["Form 41 (formerly Form 10F)", "Filed by the vendor on the Indian income-tax portal", "Gives details the TRC may not show: status, tax number, address, period of residence"],
             ["No-PE declaration", "The vendor, on its letterhead", "Supports not withholding on business income, and using the treaty rate on royalties and service fees"],
             ["PAN, or the vendor&rsquo;s tax number and contact details", "Indian tax department, or the vendor", "Without a PAN a higher withholding rate can apply; identity details limit that for most treaty payments"],
             ["Contract and invoice", "Both parties", "Show what the payment is for, which decides the treaty article"]])
         + '<p>Customers usually ask for a fresh set each financial year, because the TRC and Form 41 are tied to a period.</p>'
         + call_box("An Indian customer has asked us for a no-PE declaration and Form 41", ["Whether your company can safely sign a no-PE declaration",
                                                                                         "Filing Form 41 online, with or without an Indian PAN",
                                                                                         "The right withholding rate for your contract under the treaty",
                                                                                         "Whether you need to file an Indian tax return afterwards",
                                                                                         "What to do if you already have people or projects in India"],
                    "your country, what you supply, the customer&rsquo;s request and any staff, agents or projects in India.")),
        ("/ Sample wording", "A short no-PE declaration.", SAMPLE),
        ("/ When not to sign", "Facts that can create a permanent establishment.",
         ul("<strong>An office, branch, warehouse or project site</strong> in India that the company uses for its business.",
            "<strong>Employees or contractors in India</strong> who habitually negotiate or conclude contracts for the company, or a remote employee working from India on core business. See the <a href=\"foreign-company-remote-employee-india-pe-risk-eor-contractor-subsidiary-2026.html\">PE risk guide</a>.",
            "<strong>Service visits:</strong> many treaties treat staff providing services in India beyond a number of days, often 90 in a year, as a permanent establishment.",
            "<strong>Construction or installation projects</strong> that run beyond the treaty period.",
            "<strong>An Indian subsidiary acting for the parent</strong>, for example signing customer contracts on its behalf. A subsidiary by itself is not a permanent establishment.",
            "<strong>No treaty with India:</strong> the declaration then has to address India&rsquo;s domestic tests, including <a href=\"significant-economic-presence-foreign-saas-app-company-india-2-crore-3-lakh-users-2026.html\">significant economic presence</a>.")
         + '<p>If any of these apply, get the position reviewed before signing. A wrong declaration exposes the vendor under the indemnity and the customer to tax, interest and penalty.</p>'),
        ("/ Practical points", "For vendors and for Indian payers.",
         ul("<strong>Form 41 is filed online.</strong> A foreign company without a PAN can register on the Indian income-tax portal for this purpose. See <a href=\"how-to-file-form-10f-electronic-india-nri-no-pan-step-by-step.html\">how to file it step by step</a>.",
            "<strong>The declaration does not set the rate.</strong> Royalties and technical service fees are still taxed in India at the treaty rate, usually 10% to 15%; the declaration only confirms the income is not tied to an Indian establishment. Use the <a href=\"tds-on-payment-to-foreign-company-calculator-royalty-fts-interest-dividend-treaty-rates-2026.html\">TDS calculator</a>.",
            "<strong>Indian tax return:</strong> a vendor that relies on a treaty rate lower than the domestic rate generally has to file an Indian return for that year.",
            "<strong>For Indian payers:</strong> keep the pack on file before remitting, check that the TRC covers the payment period, and match the declaration with what you know. If the vendor&rsquo;s people work at your site, a declaration alone will not protect you.",
            "<strong>Bank forms:</strong> the remittance still needs Form 145 and, where required, a CA certificate in Form 146.")
         + '<p>Related: <a href="fees-for-technical-services-fts-taxability-india-make-available-treaty-withholding-2026.html">fees for technical services</a> &middot; <a href="income-tax-act-2025-section-195-now-393-what-changed-nri-foreign.html">section 195 is now section 393</a> &middot; <a href="old-vs-new-income-tax-form-numbers-2026-15ca-145-15cb-146-10f-41.html">old and new form numbers</a> &middot; <a href="equalisation-levy-india-abolished-6-percent-2-percent-what-applies-now-foreign-digital-companies-2026.html">equalisation levy abolished</a> &middot; <a href="india-us-tax-treaty-dtaa.html">India-US treaty</a> &middot; <a href="india-uk-tax-treaty-dtaa.html">India-UK treaty</a>.</p>'
         + sources("Income-tax Act, 2025: treaty relief provisions requiring a tax residency certificate and prescribed particulars (Form 41, formerly Form 10F), and section 393(2) on withholding from payments to non-residents (formerly section 195); Income Tax Department, Form 41 FAQs; India Briefing guide to Form 41; India&rsquo;s tax treaties, articles on permanent establishment, business profits, royalties and fees for technical services. Checked 21 November 2026. The sample is general wording and not advice for a particular contract.")),
    ],
    faqs=[("What is a no-PE declaration in India?", "A signed statement by a foreign company that it has no permanent establishment in India under the applicable tax treaty. Indian customers rely on it, with the tax residency certificate and Form 41, when deciding whether and at what rate to withhold tax."),
          ("Is there an official format for a no-PE declaration?", "No. It is not a government form. It is a self-declaration on the foreign company's letterhead covering tax residency, absence of a permanent establishment in India, beneficial ownership, entitlement to treaty benefits, a duty to inform of changes and usually an indemnity."),
          ("Why do Indian companies ask foreign vendors for a no-PE certificate?", "Because the Indian payer must withhold tax on payments that are taxable in India and is liable for tax, interest and penalty if it fails to. Business income of a treaty resident is taxable in India only through a permanent establishment, so the payer documents that there is none."),
          ("Is a no-PE declaration enough to avoid TDS in India?", "Not by itself. The vendor also needs a tax residency certificate and Form 41, and royalties and technical service fees remain taxable at the treaty rate even without a permanent establishment."),
          ("How often must a no-PE declaration be given?", "Normally once for each Indian financial year, 1 April to 31 March, with a fresh tax residency certificate and Form 41."),
          ("Who signs the no-PE declaration?", "An authorised signatory of the foreign company, such as a director or the chief financial officer, on company letterhead."),
          ("Can BQP review or prepare our no-PE declaration and Form 41?", "Yes. " + C)],
    related=[("how-to-file-form-10f-electronic-india-nri-no-pan-step-by-step.html", "How to file Form 10F / Form 41 online"),
             ("foreign-company-remote-employee-india-pe-risk-eor-contractor-subsidiary-2026.html", "PE risk for foreign companies in India"),
             ("tds-on-payment-to-foreign-company-calculator-royalty-fts-interest-dividend-treaty-rates-2026.html", "TDS on payments to foreign companies: calculator")],
    cta_h="Asked for a no-PE declaration by an Indian customer?", cta_b=C,
    keywords="no PE declaration India, no permanent establishment declaration India, no PE declaration India format, no PE declaration India template, no PE declaration sample, no PE certificate India, Form 41 Form 10F foreign company, TRC India foreign vendor, documents for treaty benefit India",
    desc="No-PE declaration for India (2026): what it is, a sample format, and the vendor pack Indian customers ask foreign companies for - tax residency certificate, Form 41 (formerly Form 10F), PAN details. When it supports nil or treaty-rate withholding, and when not to sign.",
    howto={"name": "How a foreign vendor responds to an Indian customer's request for treaty documents", "description": "Vendor pack.", "steps": [
        {"name": "Get a tax residency certificate", "text": "From your home tax authority, covering the payment period."},
        {"name": "File Form 41 online", "text": "On the Indian income-tax portal; a PAN is not always needed."},
        {"name": "Check for a permanent establishment", "text": "Staff, agents, sites and service days in India."},
        {"name": "Sign the no-PE declaration", "text": "On letterhead, for the Indian financial year, only if true."},
        {"name": "Send the pack", "text": "With contract and invoice, before the customer remits."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch FH complete")
