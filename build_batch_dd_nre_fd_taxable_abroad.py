# -*- coding: utf-8 -*-
"""Batch DD (18 Nov 2026): is NRE FD interest taxable abroad - UK, US, Canada, Australia, Singapore, UAE.
Demand: autocomplete sweep 18 Nov 2026 (ac11), all 7 markets: "nre fd interest taxable in uk", "is nre fd taxable",
"is nre fd tax free", "is fd on nre account taxable"; existing NRE page covers Indian tax only.
Facts: India - NRE interest exempt for a person resident outside India (section 10(4)(ii) of the 1961 Act, carried into
the Income-tax Act, 2025 schedule of exempt income); FCNR interest exempt for non-residents and RNORs; NRO interest
taxable with TDS (30% plus surcharge and cess, or treaty rate with TRC/Form 10F: 15% UK, US, Canada, Australia,
Singapore; 12.5% UAE). Residence countries: US citizens and residents taxed on worldwide income (Schedule B, FBAR above
USD 10,000 aggregate, Form 8938); UK residents taxed on worldwide income after the remittance basis ended on 6 April
2025, except qualifying new arrivals (10 consecutive years non-resident) who can claim the four-year FIG regime;
personal savings allowance GBP 1,000 basic / 500 higher / nil additional rate; Canada residents taxed on worldwide
income, Form T1135 if foreign property cost exceeds CAD 100,000; Australia residents taxed on worldwide income, but
temporary residents are not taxed on most foreign income; Singapore tax resident individuals exempt on foreign-sourced
income received (except through a partnership); UAE no personal income tax. Because India does not tax NRE interest,
there is no Indian tax to credit abroad. Sources: IRAS/PwC (Singapore), GOV.UK technical note and ICAEW (UK FIG),
ATO guidance (temporary residents), IRS and CRA guidance; checked 18 Nov 2026."""
from urllib.parse import quote
from build_lib import page, write_page

UPDATED = "Last updated: 18 November 2026."


def wa(t):
    return "https://wa.me/917801887130?text=" + quote(t)


def ul(*x):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in x) + "</ul>"


def table(head, rows):
    return ("<table><thead><tr>" + "".join(f"<th>{h}</th>" for h in head) + "</tr></thead><tbody>"
            + "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows) + "</tbody></table>")


CONTACT = ("Email info@bharatquantumprospera.com or WhatsApp +91 78018 87130 with your country of residence, how long you have lived there, and your NRE, NRO and FCNR balances. "
           "We reply within one working day with the Indian side (TDS, treaty rate, return) and the figures your overseas accountant needs, with a fixed-scope quote.")
SLUG = "is-nre-fd-interest-taxable-in-uk-usa-canada-australia-singapore-uae-2026"
BOX = (f'<div style="border:1px solid var(--line);border-left:4px solid #C2312A;border-radius:10px;padding:16px 18px;margin:18px 0;background:var(--bg-soft)">'
       f'<p style="margin:0 0 8px;font-weight:600">Tax-free in India is not tax-free everywhere.</p>'
       f'<p style="margin:0">Because India does not tax NRE interest, there is no Indian tax to offset abroad, so the full interest is usually taxed where you live. We give you an India-side statement of NRE, NRO and FCNR interest, TDS and treaty rates for your overseas return. '
       f'<a href="{wa("Hi Durgesh, I am an NRI. Is my NRE FD interest taxable where I live, and what do I report?")}" target="_blank" rel="noopener"><strong>WhatsApp CA Durgesh Chavda</strong></a>.</p></div>')

PAGES = [dict(
    slug=SLUG,
    title="Is NRE FD Interest Taxable in the UK, USA, Canada, Australia, Singapore or UAE? (2026) Country-by-Country Answer",
    em="tax-free in India, but often taxable where you live.",
    kicker="/ NRIs &middot; NRE &middot; Foreign tax &middot; Updated 2026-11-18",
    lead=("<strong>NRE fixed deposit interest is tax-free in India</strong> while you are a non-resident, but your <strong>country of residence may still tax it</strong>. "
          "<strong>USA, UK, Canada and Australia</strong> tax their residents on worldwide income, so NRE interest is normally taxable there in full. Because India charges no tax on it, there is <strong>no foreign tax credit</strong> to set off. Two exceptions: new UK arrivals who qualify for the <strong>four-year foreign income and gains (FIG) regime</strong> from April 2025, and <strong>temporary residents of Australia</strong>, who are generally not taxed on foreign income. "
          "<strong>Singapore</strong> tax residents are generally exempt on foreign-sourced income, and the <strong>UAE</strong> has no personal income tax, so NRE interest is usually not taxed in either. "
          "NRO interest is different: it is taxed in India (TDS 30% plus surcharge and cess, or the treaty rate, usually 15% and 12.5% for the UAE), and that Indian tax is creditable abroad."),
    sections=[
        ("/ Country by country", "Where NRE interest is taxed.",
         table(["Where you live", "Is NRE FD interest taxable there?", "What to report"], [
             ["United States", "Yes, for US citizens, green-card holders and residents (worldwide income)", "Interest on Schedule B; FBAR if foreign accounts exceed USD 10,000 in aggregate at any time; Form 8938 above its thresholds"],
             ["United Kingdom", "Yes for UK residents since the remittance basis ended on 6 April 2025; qualifying new arrivals (non-resident for the previous 10 years) can claim four years of FIG relief", "Self Assessment foreign pages; the personal savings allowance (GBP 1,000 basic rate, GBP 500 higher rate, nil additional rate) covers all savings interest"],
             ["Canada", "Yes, for Canadian residents (worldwide income)", "Interest in the T1 return in Canadian dollars; Form T1135 if the cost of foreign property exceeds CAD 100,000"],
             ["Australia", "Yes for Australian residents; temporary residents are generally not taxed on foreign investment income", "Foreign income in the tax return, converted to AUD"],
             ["Singapore", "Generally no: foreign-sourced income received by resident individuals is exempt (except through a Singapore partnership)", "Usually nothing for NRE interest"],
             ["UAE and other Gulf states", "No personal income tax", "Nothing locally; watch India's deemed-residence rule if Indian income exceeds INR 15 lakh"]])
         + BOX),
        ("/ The Indian side", "NRE, NRO and FCNR compared.",
         table(["Account", "Tax in India (non-resident)", "Credit abroad?"], [
             ["NRE (savings or FD)", "Exempt", "None needed; nothing to credit"],
             ["FCNR(B)", "Exempt for non-residents and while RNOR after return", "None needed"],
             ["NRO (savings or FD)", "Taxable; TDS 30% plus surcharge and cess, or treaty rate with TRC and Form 10F (Form 41)", "Yes, Indian tax is generally creditable under the treaty"]])
         + ul("<strong>Treaty rates on interest</strong> (non-bank recipient): 15% under the UK, US, Canada, Australia and Singapore treaties; 12.5% under the UAE treaty. See <a href=\"india-uae-dtaa-for-nris-dubai-nro-interest-mutual-funds-property-trc-2026.html\">India-UAE treaty</a>.",
              "<strong>Returning to India:</strong> NRE interest stays exempt only while you are a person resident outside India under FEMA; convert to resident or RFC accounts on return. See <a href=\"nri-nre-nro-conversion-returning-india-2026.html\">converting NRE and NRO on return</a>.",
              "<strong>Indian return:</strong> NRE interest alone does not require an Indian return; NRO interest, rent or capital gains above the exemption limit, or a TDS refund claim, do. NRIs usually file ITR-2 (ITR-3 with business income). See <a href=\"ca-for-nri-tax-return-filing.html\">NRI tax return filing</a>.")),
        ("/ Practical points", "Avoid the common mistakes.",
         ul("<strong>Report the interest as it accrues</strong> where your country taxes accrued interest (for example cumulative FDs may still need annual reporting in the US, Canada and Australia); check the local rule.",
            "<strong>Use the right exchange rate</strong> for each country's rules (annual average or transaction-date rates).",
            "<strong>Keep the bank's interest certificate</strong> for NRE, NRO and FCNR separately; NRO TDS certificates (Form 16A) support the foreign tax credit.",
            "<strong>Missed reporting abroad?</strong> Most countries have voluntary disclosure routes; fix it before the tax office asks, since banks report Indian accounts under CRS (and FATCA for US persons).")
         + '<p>Related: <a href="nre-nro-fcnr-account-tax-rules.html">NRE, NRO and FCNR tax rules</a> &middot; <a href="can-oci-open-nre-nro-account-nri-bank-accounts-tax-repatriation-2026.html">OCI bank accounts</a> &middot; <a href="what-is-fbar.html">FBAR basics</a> &middot; <a href="dubai-uae-nri-indian-income-above-15-lakh-deemed-resident-india-tax-2026.html">deemed residence for UAE NRIs</a>.</p>'
         + f'<p><strong>Sources:</strong> Income-tax Act, 2025 (exempt income; carried from section 10(4)(ii) and 10(15)(iv)(fa) of the 1961 Act); India&rsquo;s tax treaties (interest articles); GOV.UK technical note on changes to the taxation of non-UK domiciled individuals and ICAEW guidance on the FIG regime; IRAS and PwC Worldwide Tax Summaries (Singapore); ATO guidance on temporary residents; IRS (FBAR, Form 8938) and CRA (Form T1135). Checked 18 November 2026. <em>{UPDATED}</em> General information; confirm with a tax adviser in your country of residence.</p>'),
    ],
    faqs=[("Is NRE FD interest taxable in India?", "No, while you are a non-resident (a person resident outside India under FEMA). It becomes taxable once you return and become resident, so accounts should be converted on return."),
          ("Is NRE FD interest taxable in the UK?", "Usually yes for UK residents, because the remittance basis ended on 6 April 2025. Qualifying new arrivals who were non-resident for the previous 10 years can claim four years of relief under the FIG regime. The personal savings allowance applies to all savings interest."),
          ("Is NRE FD interest taxable in the USA?", "Yes for US citizens, green-card holders and US tax residents, who are taxed on worldwide income. Report it on Schedule B and file FBAR and Form 8938 where the thresholds are met."),
          ("Is NRE FD interest taxable in Canada or Australia?", "Yes for residents of Canada and Australia, who are taxed on worldwide income. Australian temporary residents are generally not taxed on foreign investment income. Canadians also check Form T1135 if foreign property exceeds CAD 100,000."),
          ("Is NRE FD interest taxable in Singapore or the UAE?", "Generally no. Singapore exempts foreign-sourced income received by resident individuals (except through a partnership), and the UAE has no personal income tax."),
          ("Can BQP prepare the India-side figures for my overseas return?", "Yes. " + CONTACT)],
    related=[("nre-nro-fcnr-account-tax-rules.html", "NRE, NRO and FCNR tax rules"), ("ca-for-nri-tax-return-filing.html", "NRI tax return filing"),
             ("india-uae-dtaa-for-nris-dubai-nro-interest-mutual-funds-property-trc-2026.html", "India-UAE treaty for NRIs")],
    cta_h="Not sure how your Indian interest is taxed abroad?", cta_b=CONTACT,
    keywords="is NRE FD interest taxable in UK, NRE FD taxable in USA, NRE FD taxable in Canada, NRE FD taxable in Australia, NRE interest Singapore tax, is NRE FD tax free, NRO interest treaty rate, FIG regime UK Indian interest",
    desc="Is NRE FD interest taxable abroad (2026)? Exempt in India, but taxable for residents of the US, UK (after the remittance basis ended 6 April 2025, except 4-year FIG relief), Canada and Australia (except temporary residents); generally not in Singapore or the UAE. NRO interest TDS and treaty rates.",
    howto={"name": "How an NRI handles Indian interest on an overseas tax return", "description": "Steps for NRE, NRO and FCNR interest.", "steps": [
        {"name": "Separate the accounts", "text": "Get interest certificates for NRE, FCNR and NRO separately."},
        {"name": "Check your residence country's rule", "text": "Worldwide taxation (US, UK, Canada, Australia) or exemption (Singapore, UAE); check FIG or temporary resident relief."},
        {"name": "Convert and report", "text": "Convert at the required exchange rate and report the interest and foreign accounts (FBAR, T1135 where applicable)."},
        {"name": "Claim credit for NRO TDS", "text": "Use Form 16A and the treaty rate to claim foreign tax credit; claim any excess Indian TDS back through an Indian return."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch DD complete")
