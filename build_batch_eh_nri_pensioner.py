# -*- coding: utf-8 -*-
"""Batch EH (20 Nov 2026): NRI pensioners - life certificate from abroad by 30 November 2026, and tax on Indian pension
for NRIs living in the UAE, US, UK, Canada, Australia and Singapore. Deadline-led, call-first page.
Demand: seasonal (life certificate window 1-30 November); "life certificate for pensioners living abroad",
"jeevan pramaan from abroad", "nri pension taxable in india"; no site page beyond calendar mentions.
Facts (checked 20 Nov 2026): annual life certificate due by 30 November 2026 (80+ may submit from 1 October); missing it
can hold the December pension, which resumes once the certificate is given - entitlement is not cancelled;
routes abroad: paper life certificate signed by an Indian embassy/consulate official or as accepted by the pension
disbursing bank, Jeevan Pramaan digital life certificate (whether the face-authentication app works outside India is
reported inconsistently - check the official FAQ and the bank); Indian pension is income arising in India and taxable
in India for a non-resident under domestic law; monthly pension is taxed as salary, commuted pension partly or fully
exempt depending on the employer; treaties: government-service pensions generally taxable only in India (unless the
person is a resident and national of the other country); private pensions for past employment taxable only in the
country of residence under some treaties (e.g. India-US, India-UK), while others let India tax too - check the treaty;
TRC and Form 10F needed for treaty relief; banks may deduct TDS; file an ITR to claim refunds; ITAT Delhi (Dec 2025)
reportedly held a US government pension received in India not taxable in India under the treaty."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 20 November 2026."
SLUG = "nri-pensioner-life-certificate-from-abroad-30-november-2026-indian-pension-tax-dtaa"

C = contact("your country of residence, the type of pension (central or state government, defence, bank, PSU or private employer, family pension), your pension bank, and whether tax has been deducted")
PAGES = [dict(
    slug=SLUG,
    title="NRI Pensioners: Life Certificate from Abroad by 30 November 2026, and Is Your Indian Pension Taxable? (UAE, US, UK, Canada, Australia)",
    em="keep the pension flowing and pay tax in the right country.",
    kicker="/ NRI &middot; Pension &middot; Life certificate &middot; DTAA &middot; Updated 2026-11-20",
    lead=("Pensioners must give their pension bank or authority a <strong>life certificate by 30 November 2026</strong>. Pensioners aged 80 and above could start from 1 October. "
          "A pensioner living abroad can usually do this with a <strong>paper life certificate signed at the Indian embassy or consulate</strong>, or in another form the pension bank accepts, or through the <strong>Jeevan Pramaan digital life certificate</strong>. Reports differ on whether the face-authentication app works outside India, so check with the bank. "
          "If the certificate is late, the <strong>December pension can be held</strong>. It resumes once the certificate is submitted, and the entitlement is not cancelled. "
          "On tax, Indian pension is <strong>taxable in India</strong> under Indian law even for a non-resident, and the bank may deduct TDS. Treaties can change this. "
          "<strong>Government pensions</strong> are generally taxable only in India. Under some treaties, for example India-US and India-UK, <strong>private-employer pensions</strong> are taxable only in the country where you live. "
          "To get treaty relief, give the bank your TRC and Form 10F, and file an Indian return to recover excess TDS."),
    sections=[
        ("/ Life certificate from abroad", "Routes and what to check.",
         table(["Route", "How", "Check"], [
             ["Paper life certificate via Indian mission", "Sign before an official at the Indian embassy or consulate; send to the pension bank", "The bank's format and whether it accepts scanned copies"],
             ["Bank-accepted alternatives", "Some banks accept certificates from their overseas branch or a notary", "Confirm with the pension disbursing bank in writing"],
             ["Jeevan Pramaan digital certificate", "Aadhaar-based biometric or face authentication", "Whether the app works from your country; Aadhaar and mobile linked"],
             ["Visiting India in November", "Submit at the bank branch or a Jeevan Pramaan centre", "Carry PPO number, Aadhaar and bank details"]])
         + call_box("My Indian pension while living abroad", ["Whether your pension is taxable in India or only where you live",
                                                               "Stopping excess TDS: TRC, Form 10F and a lower deduction certificate",
                                                               "Filing an Indian return to claim back TDS",
                                                               "Reporting the pension in your country and claiming credit",
                                                               "Life certificate route and what to do if December pension is held"],
                    "your PPO or pension details, pension bank, Form 16 or TDS statements and your country of residence.")),
        ("/ Tax on Indian pension for NRIs", "Domestic law and treaties.",
         table(["Pension type", "Indian law", "Under many treaties", "Action"], [
             ["Central / state government, defence", "Taxable in India", "Generally taxable only in India (unless you are a resident and national of the other country)", "Report in India; claim credit or exemption abroad as that country allows"],
             ["Bank, PSU or private employer pension", "Taxable in India", "Some treaties (e.g. India-US, India-UK) tax only in the country of residence; others let India tax too", "TRC and Form 10F to the bank; ITR to claim refund"],
             ["Commuted (lump sum) pension", "Fully exempt for government employees; partly exempt for others", "Usually follows the pension article", "Keep commutation papers"],
             ["Family pension", "Taxable as other income, with a standard deduction", "Depends on the treaty", "Check the treaty article"]])
         + ul("<strong>TDS:</strong> banks often deduct tax on pension paid to non-residents; a <a href=\"nil-lower-tds-certificate-form-128-formerly-form-13-section-395-how-to-apply-2026.html\">lower or nil deduction certificate</a> can reduce it.",
              "<strong>Treaty documents:</strong> a tax residency certificate from your country and <a href=\"nri-form-10f-e-filing-mandatory-india-2026.html\">Form 10F</a>.",
              "<strong>Return:</strong> file the Indian return to claim treaty relief and refunds; belated return for FY 2025-26 by 31 December 2026; see <a href=\"which-itr-to-file-for-nri-ay-2026-27-itr-2-itr-3-refund-80c-deductions.html\">which ITR an NRI files</a>.",
              "<strong>UAE residents:</strong> no UAE personal income tax, so Indian TDS is a real cost unless treaty relief applies; see the <a href=\"india-uae-dtaa-for-nris-dubai-nro-interest-mutual-funds-property-trc-2026.html\">India-UAE treaty guide</a>.",
              "<strong>Foreign pensions coming to India:</strong> see <a href=\"us-social-security-taxable-in-india-dtaa-article-20-returning-nri.html\">US Social Security in India</a>.")
         + sources("Department of Pension and Pensioners' Welfare and bank notices on the annual life certificate (November window; 80+ from 1 October); Jeevan Pramaan portal and FAQ; reports checked 20 November 2026 (Zee Business, Upstox, Outlook Money). Income-tax law on pension and commuted pension; India's tax treaties (government service and pension articles); ITAT Delhi decision on a US government pension (December 2025, as reported by LiveLaw). Treaty outcomes vary - check the specific treaty and your bank's process.")),
    ],
    faqs=[("What is the last date for the pensioner life certificate in 2026?", "30 November 2026. Pensioners aged 80 and above could submit from 1 October."),
          ("How can a pensioner living abroad submit a life certificate?", "Usually through a paper life certificate signed at the Indian embassy or consulate, another format the pension bank accepts, or the Jeevan Pramaan digital life certificate. Check whether the face-authentication app works from your country."),
          ("What happens if the life certificate is late?", "The pension can be held from December; it is released once the certificate is submitted. The entitlement is not cancelled."),
          ("Is Indian pension taxable for an NRI?", "Under Indian law, yes, because it arises in India. Treaties can change this: government pensions are generally taxable only in India, while under some treaties private pensions are taxable only in the country of residence."),
          ("How can an NRI pensioner stop excess TDS?", "Give the bank a tax residency certificate and Form 10F to claim treaty relief, apply for a lower deduction certificate, and file an Indian return to claim refunds."),
          ("Can BQP help NRI pensioners with tax?", "Yes. " + C)],
    related=[("us-social-security-taxable-in-india-dtaa-article-20-returning-nri.html", "US Social Security in India"), ("nri-form-10f-e-filing-mandatory-india-2026.html", "Form 10F for NRIs"),
             ("which-itr-to-file-for-nri-ay-2026-27-itr-2-itr-3-refund-80c-deductions.html", "Which ITR for NRIs")],
    cta_h="Receiving an Indian pension abroad?", cta_b=C,
    keywords="life certificate for pensioners living abroad, jeevan pramaan from abroad, life certificate last date 30 November 2026, NRI pension taxable in India, Indian pension DTAA, TDS on pension NRI, government pension taxable only in India",
    desc="NRI pensioners: life certificate by 30 November 2026 via the Indian embassy, a bank-accepted format or Jeevan Pramaan; late filing holds the December pension. Indian pension is taxable in India, but treaties often exempt private pensions; TRC, Form 10F and an ITR recover excess TDS.",
    howto={"name": "How an NRI pensioner keeps the pension flowing and pays the right tax", "description": "Life certificate and tax steps.", "steps": [
        {"name": "Submit the life certificate", "text": "By 30 November via the Indian mission, a bank-accepted format or Jeevan Pramaan."},
        {"name": "Identify the pension type", "text": "Government, bank or PSU, private employer or family pension."},
        {"name": "Check the treaty", "text": "Whether India or your country of residence taxes it."},
        {"name": "Give the bank TRC and Form 10F", "text": "To reduce TDS where treaty relief applies."},
        {"name": "File the Indian return", "text": "Claim refunds of excess TDS; belated FY 2025-26 return by 31 December 2026."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch EH complete")
