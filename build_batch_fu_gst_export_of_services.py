# -*- coding: utf-8 -*-
"""Batch FU (23 Nov 2026): GST on export of services - the five conditions, LUT vs paying IGST, exporting without an LUT,
invoice wording, refunds, registration threshold. Call-first page for Indian freelancers, startups selling abroad and
Indian subsidiaries billing a foreign parent.
Demand: sweep ac47 (23 Nov 2026), all 7 markets: "is there gst on exports", "do i have to pay gst on exports",
"export of services under gst without lut", "gst invoice format for export of services with lut". The site covered the
intermediary change and US clients paying Indian contractors but had no general page on GST for service exports.
Facts (checked 23 Nov 2026):
- Export of services: section 2(6) IGST Act - supplier in India, recipient outside India, place of supply outside India,
  payment in convertible foreign exchange (or INR where RBI permits), supplier and recipient not merely establishments of
  the same person. Zero-rated supply under section 16 IGST Act: export under LUT/bond without IGST and claim refund of
  unutilised ITC, or pay IGST and claim refund of the IGST.
- LUT: Form GST RFD-11, online, valid for the financial year; file before the first export invoice of the year; supplies
  before the LUT are treated as with payment of IGST (commentary: Patron Accounting, Legal Suvidha, Olambit).
- Invoice endorsement: CGST Rule 46 proviso - "SUPPLY MEANT FOR EXPORT/SUPPLY TO SEZ UNIT OR SEZ DEVELOPER FOR
  AUTHORISED OPERATIONS UNDER BOND OR LETTER OF UNDERTAKING WITHOUT PAYMENT OF INTEGRATED TAX" or "... ON PAYMENT OF
  INTEGRATED TAX".
- Rule 96A: under LUT, payment must be received within one year of the invoice (or extended period), otherwise IGST with
  interest within 15 days.
- Refund of unutilised ITC: Form RFD-01 under Rule 89; 90% provisional sanction for zero-rated supplies based on system
  risk scores from 1 October 2025 (Rule 91(2) as amended; CBIC Instruction 06/2025-GST, 3 October 2025).
- Intermediary services: section 13(8)(b) IGST omitted from 30 March 2026 (section 157, Finance Act 2026) - site page.
- Registration: service providers with aggregate turnover up to INR 20 lakh (INR 10 lakh in special category states)
  need not register even for inter-state supplies (Notification 10/2017-Integrated Tax); exports count in aggregate
  turnover.
- FEMA: services export proceeds within nine months under the 2026 export regulations; EDF deemed filed for individuals
  and for companies up to INR 10 lakh per service (FEMA 23(R)/(2)/2026-RB, 2 November 2026) - site page."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 23 November 2026."
SLUG = "gst-on-export-of-services-lut-without-lut-invoice-format-refund-freelancer-startup-2026"

C = contact("what you sell, where your clients are, your annual turnover, whether you are GST-registered and whether you have filed an LUT this year")
L = lambda h, t: f'<a href="{h}">{t}</a>'
ENDORSE_LUT = "SUPPLY MEANT FOR EXPORT/SUPPLY TO SEZ UNIT OR SEZ DEVELOPER FOR AUTHORISED OPERATIONS UNDER BOND OR LETTER OF UNDERTAKING WITHOUT PAYMENT OF INTEGRATED TAX"
ENDORSE_PAID = "SUPPLY MEANT FOR EXPORT/SUPPLY TO SEZ UNIT OR SEZ DEVELOPER FOR AUTHORISED OPERATIONS ON PAYMENT OF INTEGRATED TAX"
PAGES = [dict(
    slug=SLUG,
    title="GST on Export of Services (2026): LUT vs Paying IGST, Exporting Without an LUT, Invoice Format and Refunds",
    em="zero GST, if you get five conditions and one form right.",
    kicker="/ Startups and freelancers &middot; GST &middot; Export of services &middot; Updated 2026-11-23",
    lead=("<strong>No GST is payable on a genuine export of services from India: it is a zero-rated supply.</strong> "
          "If the client is outside India, the place of supply is outside India and you are paid in foreign currency, a GST-registered exporter files a <strong>Letter of Undertaking (LUT, Form RFD-11)</strong> once a year and invoices <strong>without IGST</strong>, then claims back GST paid on inputs. "
          "<strong>Without an LUT</strong>, you must charge 18% IGST on the export invoice and claim it back as a refund, which ties up cash. "
          "The invoice must carry the export endorsement, and under the LUT the money must arrive within <strong>one year</strong> or IGST becomes payable with interest. "
          "Freelancers below INR 20 lakh a year need not register at all. Since 30 March 2026, intermediary services for foreign clients can also be exports."),
    sections=[
        ("/ Quick answers", "The questions exporters ask first.",
         ul("<strong>Is there GST on export of services?</strong> No GST is collected on a valid export. It is zero-rated under section 16 of the IGST Act, and you can claim a refund of input tax credit.",
            "<strong>Do I need an LUT?</strong> Yes, if you are registered and want to invoice without GST. Without it, you charge 18% IGST and claim it back.",
            "<strong>Can I export services without an LUT?</strong> Yes, by paying IGST on each export invoice and claiming a refund of that IGST. It works, but your money is blocked until the refund comes.",
            "<strong>Do I need GST registration to export services?</strong> Not if your aggregate turnover is up to INR 20 lakh in the year (INR 10 lakh in special category states). Exports count towards that turnover.",
            "<strong>What must the invoice say?</strong> The export endorsement (below), the client&rsquo;s name and address and the country, and the amount in foreign currency or with the exchange rate.")),
        ("/ The five conditions", "When a service counts as an export (section 2(6), IGST Act).",
         table(["Condition", "What it means in practice"], [
             ["1. Supplier in India", "You, your firm or your Indian company"],
             ["2. Recipient outside India", "The contracting client is located abroad"],
             ["3. Place of supply outside India", "Usually the client&rsquo;s location; not for services on goods or immovable property in India, or events in India. Intermediary services follow the general rule from 30 March 2026"],
             ["4. Paid in convertible foreign exchange", "Or in rupees where the RBI permits, such as Special Rupee Vostro accounts. PayPal, Wise or Payoneer receipts converted into India count, with the bank or platform advice as proof"],
             ["5. Not two establishments of one entity", "An Indian branch billing its foreign head office is not an export. An Indian subsidiary billing its foreign parent is a separate person and can export"]])
         + '<p>If any condition fails, the supply is taxable in India at the applicable rate (usually 18%). Indian sourcing agents and back-offices: see ' + L("gst-intermediary-services-export-section-13-8-b-omitted-30-march-2026.html", "the intermediary change from 30 March 2026") + '.</p>'),
        ("/ LUT vs paying IGST", "Two ways to export, and which to use.",
         table(["", "Under LUT (most exporters)", "With payment of IGST"], [
             ["GST on the invoice", "None", "18% IGST charged and paid"],
             ["Cash flow", "No tax paid on exports", "Tax paid, then refunded"],
             ["Refund", "Unutilised input tax credit, Form RFD-01 (Rule 89)", "The IGST paid on exports"],
             ["Time limit on payment", "One year from the invoice, or IGST plus interest (Rule 96A)", "No such condition"],
             ["Paperwork", "Form RFD-11 once each financial year", "No LUT"],
             ["Best for", "Almost all service exporters", "Exporters who cannot file an LUT, or with large input tax credit to use"]])
         + ul("<strong>File the LUT before the first export invoice of the financial year.</strong> It is online on the GST portal, takes minutes and is valid for that year only. If you have already exported this year without one, take advice before filing: the department can treat those invoices as supplies on payment of IGST.",
              "<strong>Refund timing:</strong> since 1 October 2025, 90% of refund claims for zero-rated supplies are sanctioned provisionally where the system rates the claim low-risk (Rule 91(2); CBIC Instruction 06/2025-GST). The balance follows after verification.",
              "<strong>Exports under LUT still go in GSTR-1 and GSTR-3B</strong> as zero-rated supplies; a nil tax amount does not mean nil reporting.")
         + call_box("GST on export of services", ["Whether your service qualifies as an export",
                                                   "GST registration and the LUT for this year",
                                                   "Invoices already raised without an LUT",
                                                   "Refund of input tax credit",
                                                   "Income tax and FEMA on foreign receipts"],
                    "your service, client countries, turnover and GST status.")),
        ("/ Invoice format", "What an export invoice must show.",
         ul("Your name, address and GSTIN; a serial number and date.",
            "The client&rsquo;s name and address, and the name of the country.",
            "A description of the service and its SAC code.",
            "The value, in foreign currency, with the rupee value at the exchange rate used.",
            "IGST rate and amount (nil under LUT).",
            "<strong>The endorsement under LUT:</strong> &ldquo;" + ENDORSE_LUT + "&rdquo;.",
            "<strong>The endorsement when IGST is paid:</strong> &ldquo;" + ENDORSE_PAID + "&rdquo;.",
            "Signature or digital signature of the supplier.")
         + '<p>The endorsement wording is from the proviso to Rule 46 of the CGST Rules. Many exporters also quote the LUT reference number (ARN) on the invoice.</p>'),
        ("/ Income tax and FEMA", "The other two laws on the same receipt.",
         ul("<strong>Income tax:</strong> export income is taxable in India like any other business income. Freelancers can often use the presumptive scheme; see " + L("freelancer-consultant-tax-india-2026-complete.html", "tax for freelancers and consultants") + ".",
            "<strong>FEMA:</strong> the 2026 export regulations require service export proceeds within nine months; since 2 November 2026 the EDF filing is deemed done for individuals, and for companies up to INR 10 lakh per service. See " + L("fema-services-export-edf-relief-freelancers-10-lakh-rbi-amendment-2-november-2026.html", "the EDF relief") + ".",
            "<strong>Note the two clocks:</strong> GST allows one year for payment under the LUT; FEMA expects realisation within nine months.",
            "<strong>Indian subsidiaries billing a foreign parent:</strong> exports under LUT, plus transfer pricing on the price; see " + L("transfer-pricing-safe-harbour-vs-apa-india-2026-15-5-percent-it-services-form-49-advance-pricing-agreement.html", "safe harbour vs APA") + ".",
            "<strong>US clients:</strong> they usually ask for Form W-8BEN or W-8BEN-E; see " + L("us-company-paying-indian-contractor-w-8ben-no-1099-gst-lut-pe-risk-2026.html", "US company paying an Indian contractor") + ".")
         + sources("Integrated Goods and Services Tax Act, 2017, sections 2(6), 13 and 16 (section 13(8)(b) omitted from 30 March 2026 by section 157 of the Finance Act, 2026); CGST Rules, 2017, Rules 46, 89, 91(2) and 96A; Form GST RFD-11; CBIC Instruction No. 06/2025-GST (3 October 2025) on 90% provisional refunds; Notification 10/2017-Integrated Tax (registration exemption for inter-state service suppliers up to the threshold); Foreign Exchange Management (Export and Import of Goods and Services) (Second Amendment) Regulations, 2026 (FEMA 23(R)/(2)/2026-RB, 2 November 2026); commentary from TaxGuru, Taxmann and practitioner guides. Checked 23 November 2026.")),
    ],
    faqs=[("Is GST applicable on export of services from India?", "No GST is collected on a valid export of services. It is a zero-rated supply: you either export under a Letter of Undertaking without IGST, or pay IGST and claim it back. You can also claim a refund of GST paid on inputs."),
        ("Is GST applicable outside India?", "GST is India's tax on supplies whose place of supply is in India; it is not charged on sales consumed abroad. Exports of goods and services are zero-rated, so they leave India without GST (under an LUT) or with a refund. Going the other way, Indian businesses pay GST on imported services under reverse charge, and foreign companies selling online services such as software, streaming or cloud subscriptions to Indian consumers must register and charge 18% IGST."),
        ("Does India have GST like VAT in other countries?", "Yes. India's Goods and Services Tax, in force since 1 July 2017, is a destination-based VAT: CGST and SGST on supplies within a state, IGST on supplies between states and on imports. Since 22 September 2025 most goods and services are taxed at 5% or 18%, with 40% on luxury and sin goods."),
          ("Can I export services without an LUT?", "Yes. You charge 18% IGST on the export invoice, pay it, and claim a refund of that IGST. The LUT route avoids blocking cash, so most exporters file it each year."),
          ("When should the LUT be filed for 2026-27?", "Before the first export invoice of the financial year. It is filed online in Form GST RFD-11 and is valid for that financial year only."),
          ("What is the invoice endorsement for export of services under LUT?", "SUPPLY MEANT FOR EXPORT/SUPPLY TO SEZ UNIT OR SEZ DEVELOPER FOR AUTHORISED OPERATIONS UNDER BOND OR LETTER OF UNDERTAKING WITHOUT PAYMENT OF INTEGRATED TAX, as required by the proviso to Rule 46 of the CGST Rules."),
          ("Does a freelancer need GST registration for foreign clients?", "Not if aggregate turnover, including exports, is up to INR 20 lakh in the financial year (INR 10 lakh in special category states). Above that, registration is required, and an LUT lets you invoice without GST."),
        ("Is GST charged on foreign inward remittance?", "Not on the money itself. Receiving a foreign remittance is not a supply; when it is payment for services you exported, the export is zero-rated, so under an LUT no GST is charged. Money from family abroad is not a supply either. The only GST is the 18% the bank charges on its own conversion or remittance fee, worked out on a small notional value of the conversion, not on the whole amount."),
        ("How is GST on foreign currency conversion calculated?", "GST at 18% is charged on a notional value of the conversion, not on the full amount. Under Rule 32(2)(b) of the CGST Rules, that value is 1% of the amount up to INR 1 lakh (minimum INR 250); INR 1,000 plus 0.5% of the amount between INR 1 lakh and INR 10 lakh; and INR 5,500 plus 0.1% of the amount above INR 10 lakh, capped at INR 60,000. So converting INR 5 lakh means GST on INR 3,000, about INR 540."),
        ("What is the GST rate on software services and does it apply to software exports?", "Software development, SaaS and IT services are taxed at 18% when supplied in India. Software or IT services exported to a foreign client and paid for in foreign exchange are zero-rated, so no GST is charged under an LUT. OIDAR (online information database access and retrieval) services sold by foreign companies to Indian consumers are taxed at 18% in India."),
        ("Do I need a FIRC or FIRA for export of services?", "Keep the bank's foreign inward remittance advice (FIRA, often called e-FIRC) or bank realisation record for each client payment. It proves the money arrived in convertible foreign exchange (or permitted rupees), which is one of the conditions for treating the service as an export and for any GST refund."),
          ("What happens if the foreign client pays late?", "Under an LUT, if payment is not received within one year of the invoice (or an extended period allowed), IGST becomes payable with interest. FEMA separately expects realisation within nine months."),
          ("Can BQP handle GST for our export of services?", "Yes. " + C)],
    related=[("gst-intermediary-services-export-section-13-8-b-omitted-30-march-2026.html", "Intermediary services as exports"),
             ("us-company-paying-indian-contractor-w-8ben-no-1099-gst-lut-pe-risk-2026.html", "US company paying an Indian contractor"),
             ("freelancer-consultant-tax-india-2026-complete.html", "Tax for freelancers and consultants"),
             ("fema-services-export-edf-relief-freelancers-10-lakh-rbi-amendment-2-november-2026.html", "FEMA EDF relief for service exports"),
             ("wise-payoneer-paypal-revolut-balance-schedule-fa-freelancer-fast-ds.html", "Wise, Payoneer, PayPal balances and Schedule FA")],
    cta_h="Billing clients abroad?", cta_b=C,
    keywords="GST on export of services, is there GST on exports, export of services under GST without LUT, GST invoice format for export of services with LUT, LUT RFD-11 2026-27, zero rated supply services, GST refund export of services, freelancer GST foreign client, Rule 96A one year",
    desc="GST on export of services (2026): no GST on a valid export; file an LUT (RFD-11) to invoice without IGST, or pay 18% IGST and claim a refund; the five conditions, invoice endorsement wording, one-year payment rule, 90% provisional refunds, INR 20 lakh registration threshold.",
    howto={"name": "How to export services from India without paying GST", "description": "LUT route for a registered exporter.", "steps": [
        {"name": "Check the five conditions", "text": "Supplier in India, client abroad, place of supply abroad, payment in foreign exchange, not two establishments of one entity."},
        {"name": "File the LUT", "text": "Form GST RFD-11 on the GST portal before the first export invoice of the financial year."},
        {"name": "Raise the export invoice", "text": "With the Rule 46 endorsement, client country and foreign currency value, nil IGST."},
        {"name": "Report in GST returns", "text": "Show the export as a zero-rated supply in GSTR-1 and GSTR-3B."},
        {"name": "Collect payment and claim refund", "text": "Receive payment within one year; claim refund of unutilised input tax credit in Form RFD-01."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch FU complete")
