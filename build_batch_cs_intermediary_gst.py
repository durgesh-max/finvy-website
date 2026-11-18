# -*- coding: utf-8 -*-
"""Batch CS (15 Nov 2026): GST on intermediary services after omission of section 13(8)(b) of the IGST Act.
Gap: no page on the site mentions it. Audience: Indian sourcing agents, marketing/sales agents, BPO/KPO and
consultants acting for foreign principals; foreign companies paying Indian agents; Indian businesses buying
intermediary services from abroad.
Facts: section 13(8)(b) IGST Act (place of supply of intermediary services = location of supplier) omitted by section
157 of the Finance Act, 2026, effective 30 March 2026 (date of assent; no separate commencement), prospective. Place of
supply now under section 13(2): location of the recipient. Export of services needs all five conditions of section 2(6)
IGST Act: supplier in India, recipient outside India, place of supply outside India, payment in convertible foreign
exchange (or INR where RBI permits), supplier and recipient not merely establishments of the same person. Exports are
zero-rated under section 16: under LUT without tax, or with IGST and refund. Definition of intermediary (section 2(13))
unchanged. Earlier periods: disputes may continue. Import side: intermediary services received by an Indian business
from abroad now have place of supply in India: reverse charge. Sources: Finance Act, 2026 s.157; IGST Act ss.2(6),
2(13), 13(2), 16; taxguru, taxmann, a2ztaxcorp analyses (checked 15 Nov 2026)."""
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


CONTACT = ("Email info@bharatquantumprospera.com or WhatsApp +91 78018 87130 with your agency or service agreement, where the client sits and how you are paid. "
           "We reply within one working day on export status, the LUT, refunds and any past-period exposure, with a fixed-scope quote.")
SLUG = "gst-intermediary-services-export-section-13-8-b-omitted-30-march-2026"
BOX = (f'<div style="border:1px solid var(--line);border-left:4px solid #C2312A;border-radius:10px;padding:16px 18px;margin:18px 0;background:var(--bg-soft)">'
       f'<p style="margin:0 0 8px;font-weight:600">Still charging 18% GST to your foreign principal?</p>'
       f'<p style="margin:0">From 30 March 2026 commissions and agency fees from foreign clients can be zero-rated exports, if the five export conditions are met and an LUT is in place. Earlier periods are a separate question. '
       f'<a href="{wa("Hi Durgesh, we act as an agent for a foreign company. Is our commission now an export under GST?")}" target="_blank" rel="noopener"><strong>WhatsApp CA Durgesh Chavda</strong></a>.</p></div>')

PAGES = [dict(
    slug=SLUG,
    title="GST on Intermediary Services From 30 March 2026: Section 13(8)(b) Omitted, Commission From Foreign Clients Now an Export",
    em="agents, sourcing offices and back-offices serving foreign principals.",
    kicker="/ GST &middot; Export of services &middot; Foreign clients &middot; Updated 2026-11-15",
    lead=("From <strong>30 March 2026</strong>, services of an Indian <strong>intermediary</strong> (an agent, broker or facilitator who arranges supplies between others, such as a sourcing agent, sales or marketing agent, or a facilitation back-office) for a <strong>client outside India can be a zero-rated export</strong> under GST. "
          "<strong>Section 157 of the Finance Act, 2026</strong> omitted <strong>section 13(8)(b) of the IGST Act</strong>, which used to fix the place of supply of intermediary services at the supplier's location in India and so made them taxable at 18% even when the client and the payment were foreign. "
          "The place of supply now follows the general rule (<strong>location of the recipient</strong>), so the service is an export if all five conditions in section 2(6) are met, and it can be supplied under a <strong>Letter of Undertaking without GST</strong>. The change is prospective: periods before 30 March 2026 stay under the old rule. The reverse also applies: an Indian business that uses a <strong>foreign intermediary</strong> now pays GST under <strong>reverse charge</strong>."),
    sections=[
        ("/ Before and after", "What changed.",
         table(["Situation", "Up to 29 March 2026", "From 30 March 2026"], [
             ["Indian sourcing agent paid commission by a US/UK/EU buyer", "Place of supply India; 18% GST payable", "Place of supply outside India; zero-rated export if section 2(6) conditions met"],
             ["Indian marketing or sales agent for a foreign principal", "18% GST payable", "Zero-rated export (under LUT or with IGST refund)"],
             ["Indian business pays a foreign agent or broker", "Outside Indian GST in most cases", "Place of supply India: import of service, GST under reverse charge"],
             ["Indian back-office providing its own services (not arranging supplies between others)", "Already an export if conditions met (not an intermediary)", "Same: export if conditions met"]])
         + BOX),
        ("/ The five export conditions", "All must be met (IGST Act, section 2(6)).",
         ul("The supplier is located in India.",
            "The recipient is located outside India.",
            "The place of supply is outside India (now true for intermediary services to a foreign recipient).",
            "Payment is received in convertible foreign exchange, or in Indian rupees where the RBI permits.",
            "The supplier and recipient are not merely establishments of the same person (an Indian branch of a foreign company does not qualify; a separate Indian subsidiary can).")
         + '<p><strong>Then:</strong> file a Letter of Undertaking (LUT) for the financial year and invoice without GST, or pay IGST and claim a refund; keep the foreign inward remittance records; claim refunds of input tax credit on zero-rated supplies.</p>'),
        ("/ What to check now", "Practical points.",
         ul("<strong>Is it really intermediary?</strong> The definition in section 2(13) is unchanged: arranging or facilitating supplies between two or more persons, excluding a person who supplies the main service on its own account. The classification still matters for earlier periods and for import tax.",
            "<strong>Invoices from 30 March 2026:</strong> if you still charged 18% GST to a foreign principal, review whether credit notes, refunds or LUT supplies apply.",
            "<strong>Earlier periods:</strong> the omission is prospective with no saving or retrospective clause; demands and refund rejections for earlier years may still be pursued, and practitioners differ on their effect.",
            "<strong>Indian buyers of foreign intermediary services</strong> (for example foreign sourcing agents or brokers): pay GST under reverse charge and self-invoice; see <a href=\"gst-reverse-charge-import-of-services-india-rcm-self-invoice-itc-2026.html\">RCM on import of services</a>.",
            "<strong>Income tax is separate:</strong> commission paid by an Indian business to a foreign agent can raise withholding questions; see <a href=\"fees-for-technical-services-fts-taxability-india-make-available-treaty-withholding-2026.html\">fees for technical services</a>.")
         + '<p>Related: <a href="gcc-global-capability-centre-india-setup-us-company-safe-harbour-2026.html">global capability centres in India</a> &middot; <a href="best-ca-oidar-gst-foreign-saas-india-2026.html">GST on foreign SaaS (OIDAR)</a> &middot; <a href="rule-96-10-omitted-retrospectively-exporters-igst-refund-circular-264-2026.html">IGST refunds for exporters</a> &middot; <a href="india-services-for-foreign-companies-complete-list.html">services for foreign companies</a>.</p>'
         + f'<p><strong>Sources:</strong> Finance Act, 2026, section 157 (omission of section 13(8)(b), effective on assent, 30 March 2026); Integrated Goods and Services Tax Act, 2017, sections 2(6), 2(13), 13(2) and 16. Secondary analyses checked 15 November 2026: taxguru, Taxmann, A2Z Taxcorp. No CBIC transition circular had been reported as of the sources checked. <em>{UPDATED}</em> General information, not advice for your contracts.</p>'),
    ],
    faqs=[("Are intermediary services to foreign clients an export under GST now?", "From 30 March 2026, yes, if the five export conditions in section 2(6) of the IGST Act are met. Section 157 of the Finance Act, 2026 omitted section 13(8)(b), so the place of supply is the recipient's location outside India."),
          ("What was section 13(8)(b) of the IGST Act?", "It deemed the place of supply of intermediary services to be the location of the supplier. An Indian agent serving a foreign principal therefore charged 18% GST even though the client and payment were foreign."),
          ("Does the change apply to earlier years?", "No. It applies from 30 March 2026, with no retrospective clause. Disputes over earlier periods may continue."),
          ("Do I need a Letter of Undertaking?", "To invoice exports without paying IGST, yes: file an LUT for the financial year on the GST portal. Otherwise pay IGST and claim the refund."),
          ("We are an Indian company paying a foreign sourcing agent. What changes?", "The place of supply is now India, so the agent's service is an import of service and you pay GST under reverse charge, generally with input tax credit if used for taxable business."),
          ("Can BQP review our agency arrangements?", "Yes. " + CONTACT)],
    related=[("gst-reverse-charge-import-of-services-india-rcm-self-invoice-itc-2026.html", "RCM on import of services"), ("gcc-global-capability-centre-india-setup-us-company-safe-harbour-2026.html", "Global capability centres"),
             ("rule-96-10-omitted-retrospectively-exporters-igst-refund-circular-264-2026.html", "IGST refunds for exporters")],
    cta_h="Serving a foreign principal from India?", cta_b=CONTACT,
    keywords="intermediary services GST 2026, section 13(8)(b) omitted, intermediary export of services GST, Finance Act 2026 section 157 intermediary, GST on commission from foreign company, sourcing agent GST export, place of supply intermediary 13(2), LUT intermediary services",
    desc="GST on intermediary services from 30 March 2026: Finance Act 2026 (s.157) omitted section 13(8)(b) IGST Act, so commission and agency fees from foreign clients can be zero-rated exports under LUT; five export conditions, earlier periods, and reverse charge when Indian businesses use foreign intermediaries.",
    howto={"name": "How an Indian intermediary moves to zero-rated export invoicing", "description": "Steps after the 30 March 2026 change.", "steps": [
        {"name": "Confirm intermediary status and recipient", "text": "Check the agreement: who the client is, where it is located and how you are paid."},
        {"name": "Test the five export conditions", "text": "Supplier in India, recipient abroad, place of supply abroad, foreign exchange receipt, not establishments of the same person."},
        {"name": "File an LUT", "text": "File the Letter of Undertaking for the financial year on the GST portal."},
        {"name": "Fix invoicing since 30 March 2026", "text": "Issue zero-rated invoices and review any 18% invoices issued after the change."},
        {"name": "Claim ITC refunds", "text": "Claim refund of unutilised input tax credit on zero-rated supplies."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch CS complete")
