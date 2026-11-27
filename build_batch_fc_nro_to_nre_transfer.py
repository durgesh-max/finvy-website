# -*- coding: utf-8 -*-
"""Batch FC (21 Nov 2026): NRO to NRE transfer - is it allowed, the limit, tax, Form 145 / 146 and documents.
Call-first page.
Demand: sweep 21 Nov 2026 (ac36), all 7 markets: "nro to nre transfer", "nro to nre transfer limit", "is transfer of
funds from nro to nre taxable", "nro to nre transfer form 15ca", "transfer money from nro to nre icici / hdfc / sbi".
The site answered this only in one FAQ line on the repatriation page.
Facts (checked 21 Nov 2026):
- RBI Notification No. FEMA 5(R)(6)/2026-RB dated 18 June 2026, Foreign Exchange Management (Deposit) (Sixth Amendment)
  Regulations, 2026 (listed by RBI on 29 June 2026; in force on Gazette publication): Schedule 1 (NRE), para 3, new
  clause (k) - permitted credit: "Transfer from NRO account within the limit specified in Regulation 4 of Foreign
  Exchange Management (Remittance of Assets) Regulations, 2016"; Schedule 3 (NRO), para 3(B), new clause (v) - permitted
  debit: "Transfer to NRE or SNRR account within the limit" of the same regulation; SNRR account open to any person
  resident outside India, including with a bank branch in an IFSC. Read from the RBI site.
- Regulation 4, Remittance of Assets Regulations, 2016: USD 1 million per financial year for NRIs and PIOs from NRO
  balances, sale proceeds and inherited assets. The transfer was earlier allowed by RBI circular (A.P. (DIR Series)
  Circular No. 117, 7 May 2012), subject to payment of applicable tax.
- Form 15CA / 15CB became Form 145 / Form 146 from 1 April 2026 (site form-number page).
- NRE interest is exempt for a person resident outside India; NRO interest carries TDS at 30% plus surcharge and cess
  unless a treaty rate is claimed (site NRO refund calculator). TCS on LRS applies to residents, not to NRO transfers."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 21 November 2026."
SLUG = "nro-to-nre-transfer-limit-tax-form-145-146-15ca-15cb-documents-usd-1-million-2026"

C = contact("the country you live in, your bank, the amount you want to move and where the NRO money came from (rent, interest, property sale, inheritance or old savings)")
PAGES = [dict(
    slug=SLUG,
    title="How to Transfer Money From NRO to NRE (2026): Is It Allowed, the USD 1 Million Limit, Tax, Form 145 and 146 (Old 15CA and 15CB), Documents and Bank Steps",
    em="what the bank asks for and how to get it done.",
    kicker="/ NRI &middot; Bank accounts &middot; Repatriation &middot; Updated 2026-11-21",
    lead=("<strong>Yes, an NRI can transfer money from an NRO account to an NRE account.</strong> "
          "The limit is <strong>USD 1 million per financial year</strong> (April to March), and it is shared with any money you send abroad directly from the NRO account. "
          "<strong>The transfer itself is not taxed.</strong> What the bank checks is that Indian tax on the money behind it (rent, interest, sale proceeds) has been paid. "
          "For that it asks for <strong>Form 145</strong>, filed online, and usually a Chartered Accountant&rsquo;s certificate in <strong>Form 146</strong>. These replaced Form 15CA and Form 15CB from 1 April 2026. "
          "Once the money is in the NRE account it can be sent abroad freely, and NRE interest is tax-free in India while you are a non-resident. "
          "Since June 2026 the RBI&rsquo;s deposit regulations list this transfer expressly, so the rule is the same at every bank; only the bank&rsquo;s own request form differs."),
    sections=[
        ("/ The rule at a glance", "Limit, tax and paperwork.",
         table(["Question", "Answer"], [
             ["Is NRO to NRE transfer allowed?", "Yes. It is a permitted debit to the NRO account and a permitted credit to the NRE account under the FEMA deposit regulations"],
             ["Limit", "USD 1 million per financial year, counted together with direct remittances abroad from NRO balances, property sale proceeds and inheritance"],
             ["Is the transfer taxable?", "No. Tax is due on the income that created the balance, not on moving it"],
             ["Forms", "Form 145 online (old Form 15CA) and, in most cases, a CA certificate in Form 146 (old Form 15CB)"],
             ["Between whose accounts?", "Your own NRO and NRE accounts"],
             ["TCS", "None. TCS applies to residents remitting under the Liberalised Remittance Scheme, not to NRO transfers"],
             ["NRE to NRO (the reverse)", "Allowed freely with no limit or certificate, but the money then falls under the NRO rules"],
             ["After you move back to India", "NRE and NRO accounts must be redesignated as resident accounts, so do the transfer while you are still non-resident"]])
         + call_box("NRO to NRE transfer or sending NRO money abroad", ["Whether your money can move this year within the USD 1 million limit",
                                                                       "The CA certificate (Form 146) and Form 145 your bank asks for",
                                                                       "Tax still to pay or to claim back on NRO interest, rent or a property sale",
                                                                       "Money from a property sale or inheritance: what proof the bank needs",
                                                                       "Planning the transfer across two financial years if the amount is large"],
                    "your country, your bank, the amount, the source of the NRO balance and whether you filed an Indian tax return for that income.")),
        ("/ Step by step", "How the transfer is done.",
         ul("<strong>1. Identify the source:</strong> rent, interest, dividends, pension, sale of property or shares, inheritance, or savings from before you left India. The bank and the CA both ask.",
            "<strong>2. Settle the tax:</strong> check that TDS was deducted or tax was paid, and file the Indian return where one is due. If TDS on NRO interest was more than your treaty rate, claim the refund in the return; see the <a href=\"nri-nro-interest-tds-refund-calculator-treaty-rate-by-country-2026.html\">NRO interest refund calculator</a>.",
            "<strong>3. CA certificate (Form 146):</strong> the Chartered Accountant checks the source, the tax paid and the treaty position, and uploads the certificate.",
            "<strong>4. Form 145:</strong> filed on the income-tax portal by you, using the certificate details.",
            "<strong>5. Bank request:</strong> give the bank its NRO-to-NRE transfer form, the FEMA declaration, Form 145, Form 146 and proof of source.",
            "<strong>6. Credit to NRE:</strong> the bank moves the rupees to your NRE account. From there you can keep them in India or send them abroad.")
         + '<p><strong>Documents usually asked for:</strong> PAN, passport and visa or residence proof, NRO statement showing the credits, proof of source (sale deed, rent agreement, will or succession papers, maturity advice), proof of tax (TDS certificates, Form 26AS or AIS, return acknowledgment, challans), and the bank&rsquo;s own form.</p>'),
        ("/ Practical points", "What people get wrong.",
         ul("<strong>The limit is shared:</strong> NRO to NRE transfers and remittances abroad from NRO in the same April-to-March year add up towards USD 1 million. A large sale can be split across 31 March.",
            "<strong>Not taxed does not mean no paperwork:</strong> banks treat the transfer like a remittance abroad, because NRE money is freely repatriable.",
            "<strong>Property sale money:</strong> the buyer&rsquo;s TDS and your capital gains return come first. See <a href=\"nri-sell-property-in-india-from-abroad-power-of-attorney-tds-repatriation-2026.html\">selling Indian property from abroad</a>.",
            "<strong>Inherited money:</strong> India has no inheritance tax, but the bank wants the will or succession documents. See <a href=\"inherit-money-property-from-india-living-in-uk-usa-canada-australia-2026.html\">inheriting money or property from India</a>.",
            "<strong>Why move to NRE and not straight abroad:</strong> NRE keeps the money in rupees in India, with tax-free interest and no limit on sending it out later. If you need the money abroad now, remit directly from NRO; the paperwork is the same.",
            "<strong>Your home country:</strong> interest earned in India may still be taxable where you live, even when India does not tax it.",
            "<strong>SNRR accounts:</strong> the same June 2026 amendment also allows transfers from NRO to a Special Non-Resident Rupee account within the same limit.")
         + '<p>Related: <a href="repatriate-money-from-india-to-abroad-nro-usd-1-million-15ca-15cb-2026.html">repatriating money from India, step by step</a> &middot; <a href="nre-nro-fcnr-account-tax-rules.html">NRE, NRO and FCNR tax rules</a> &middot; <a href="old-vs-new-income-tax-form-numbers-2026-15ca-145-15cb-146-10f-41.html">old and new form numbers</a> &middot; <a href="nri-send-money-to-from-india-checker.html">send-money checker</a> &middot; <a href="nri-nre-nro-conversion-returning-india-2026.html">accounts when you return to India</a>.</p>'
         + sources("Reserve Bank of India, Foreign Exchange Management (Deposit) (Sixth Amendment) Regulations, 2026, Notification No. FEMA 5(R)(6)/2026-RB dated 18 June 2026 (Schedule 1, paragraph 3(k) and Schedule 3, paragraph 3(B)(v)); Foreign Exchange Management (Remittance of Assets) Regulations, 2016, regulation 4; RBI A.P. (DIR Series) Circular No. 117 of 7 May 2012; Income-tax Rules, 2026 (Forms 145 and 146). Checked 21 November 2026. Banks set their own forms and may ask for more documents.")),
    ],
    faqs=[("Can I transfer money from an NRO account to an NRE account?", "Yes. An NRI can transfer from their NRO account to their NRE account within USD 1 million per financial year. RBI's June 2026 amendment to the FEMA deposit regulations lists it as a permitted debit to NRO and credit to NRE."),
        ("How do I send money from NRO to NRE, step by step?", "1) Work out where the NRO balance came from - rent, interest, a property sale, inheritance or savings from before you became an NRI - and check that Indian tax on it has been paid or deducted (Form 168, old 26AS, shows the TDS). 2) A Chartered Accountant examines the source and tax position and issues Form 146 (old 15CB). 3) Form 145 (old 15CA) is filed online on the income tax portal using the Form 146 details. 4) Submit the bank's NRO-to-NRE (or outward remittance) request form with Forms 145 and 146, your declaration that the total for the financial year stays within USD 1 million, and any source documents the bank asks for - sale deed, rent agreement or succession papers. 5) The bank checks the documents and credits the NRE account. The steps are the same at ICICI, HDFC, SBI, Axis, Federal Bank or any other bank; only the request form differs. WhatsApp +91 78018 87130 with your bank, the amount, the country you live in and where the NRO money came from, and we issue the CA certificate and tell you what the bank will need."),
          ("What is the NRO to NRE transfer limit?", "USD 1 million per financial year, April to March. The limit is shared with money sent abroad directly from NRO balances, property sale proceeds and inheritance."),
          ("Is transfer of funds from NRO to NRE taxable?", "No. The transfer itself is not income. Indian tax must have been paid on the income behind the balance, such as rent, interest or capital gains, and the bank checks this before moving the money."),
          ("Is Form 15CA and 15CB required for NRO to NRE transfer?", "Banks generally ask for both. From 1 April 2026 they are Form 145, filed online, and Form 146, the Chartered Accountant's certificate."),
          ("Can I transfer from NRE to NRO?", "Yes, freely, with no limit and no CA certificate. The money then follows NRO rules, so sending it abroad later falls under the USD 1 million limit and paperwork."),
          ("Is the process different at ICICI, HDFC, SBI, Axis or Kotak?", "The FEMA rule and the tax forms are the same at every bank. Each bank has its own request form and declaration, and some ask for extra proof of source."),
          ("Can BQP issue the CA certificate for an NRO to NRE transfer?", "Yes. " + C)],
    related=[("repatriate-money-from-india-to-abroad-nro-usd-1-million-15ca-15cb-2026.html", "Repatriating money from India, step by step"),
             ("nri-nro-interest-tds-refund-calculator-treaty-rate-by-country-2026.html", "NRO interest TDS refund calculator"),
             ("nre-nro-fcnr-account-tax-rules.html", "NRE, NRO and FCNR tax rules")],
    cta_h="Need the CA certificate for an NRO to NRE transfer?", cta_b=C,
    keywords="NRO to NRE transfer, NRO to NRE transfer limit, is NRO to NRE transfer taxable, NRO to NRE transfer form 15CA 15CB, Form 145 Form 146 NRO, transfer money from NRO to NRE, USD 1 million NRO, NRE to NRO transfer",
    desc="NRO to NRE transfer in 2026: allowed up to USD 1 million per financial year (shared with NRO remittances abroad); the transfer is not taxed; banks ask for Form 145 and a CA certificate in Form 146 (old 15CA / 15CB). RBI's June 2026 amendment, steps and documents.",
    howto={"name": "How to transfer money from NRO to NRE", "description": "Steps for an NRI.", "steps": [
        {"name": "Identify the source", "text": "Rent, interest, property sale, inheritance or old savings."},
        {"name": "Settle Indian tax", "text": "Confirm TDS or tax paid and file the return where due."},
        {"name": "Get the CA certificate", "text": "Form 146 from a Chartered Accountant."},
        {"name": "File Form 145", "text": "Online on the income-tax portal."},
        {"name": "Submit to the bank", "text": "Transfer request, declaration, forms and proof of source."},
        {"name": "Receive the NRE credit", "text": "The money is then freely repatriable."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch FC complete")
