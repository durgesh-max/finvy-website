# -*- coding: utf-8 -*-
"""Batch LX (28 Nov 2026): Joint bank accounts between an NRI and a resident parent or relative - adding an NRI to a parent's
resident savings account, a resident close relative on an NRE / FCNR(B) or NRO account, 'former or survivor' operation, power of
attorney, what happens on death, and tax on interest.
Demand: 'nri joint account with resident parent', 'can nri be joint holder in resident savings account', 'nre account joint holder
resident', 'former or survivor nri', 'nro joint account resident' - only touched on a FAST-DS FAQ page; no dedicated page. NRIs with
elderly parents in India ask this constantly. User steer 26 Nov / 19 Nov 2026: more call bookings, NRI audience.
Facts (RBI rules on deposits under FEMA; RBI circulars of 2011 (A.P. (DIR) 13) and 2014 (A.P. (DIR) 87), RBI FAQ on accounts of
non-residents - verified by web search 28 Nov 2026): an NRI may open an NRE or FCNR(B) account jointly with a resident close relative
(relative as defined in the Companies Act) on a 'former or survivor' basis; the resident can operate it during the NRI's lifetime only
as a power of attorney holder; banks may add an NRI close relative as joint holder to a resident's savings (resident) account on a
'former or survivor' basis, the NRI cannot operate it during the resident's lifetime, it stays a resident account, and if the NRI
becomes the survivor it is redesignated as an NRO account; an NRO account may be held jointly with a resident; an NRI cannot keep an
own resident savings account and must redesignate it to NRO (site page). Tax: interest is taxed in the hands of the person whose money
it is; NRE interest is exempt only while the holder is non-resident; NRO interest carries TDS for non-residents; the bank deducts TDS
based on the first holder's status. Bank practice may be stricter. No fees, no portal menu paths. advisory_lib.contact() not used."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources
from build_lib import page, write_page

A.UPDATED = "Last updated: 28 November 2026."
SLUG = "nri-joint-bank-account-with-resident-parent-nre-nro-former-or-survivor-power-of-attorney-tax-2026"

C = ("WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with the accounts involved (NRE, NRO, FCNR, resident savings), "
     "who holds them and in what order, your residency status and your parent&rsquo;s, and what you want to achieve (help with "
     "bills, succession, sending money). Or book a call directly.")
PAGES = [dict(
    slug=SLUG,
    title="NRI Joint Bank Account With a Resident Parent (2026): NRE, NRO and Resident Savings Accounts, Former or Survivor, Power of Attorney and Tax on Interest",
    em="who can operate, and who owns the money.",
    kicker="/ NRIs with parents or close relatives in India &middot; FEMA rules on joint accounts &middot; Updated 2026-11-28",
    lead=("<strong>An NRI can hold an NRE or FCNR(B) account jointly with a resident close relative, and a resident parent can add an NRI child to a resident savings account - but only on a &lsquo;former or survivor&rsquo; basis. "
          "In each case the second holder cannot operate the account while the first holder is alive, except a resident acting under a power of attorney on an NRE account. "
          "Interest is taxed in the hands of the person whose money it is, not simply the first name on the passbook.</strong>"),
    sections=[
        ("/ What is allowed", "RBI rules under FEMA.",
         table(["Account", "Joint holder allowed", "How it operates"], [
             ["NRE or FCNR(B) of the NRI", "Resident close relative", "Former or survivor; the resident can operate during the NRI&rsquo;s lifetime only as a power of attorney holder"],
             ["NRO of the NRI", "Resident (for example a parent)", "As agreed with the bank, typically former or survivor"],
             ["Resident savings account of the parent", "NRI close relative", "Former or survivor; the NRI cannot operate while the parent is alive; stays a resident account"],
             ["If the NRI becomes survivor of a resident account", "-", "The account is redesignated as an NRO account"],
             ["The NRI&rsquo;s own old savings account", "-", "Must be redesignated as NRO on becoming non-resident"]])
         + ul("<strong>Close relative:</strong> as defined in the Companies Act - parents, spouse, children, siblings and certain in-laws.",
              "<strong>Bank practice:</strong> banks can apply stricter terms; check the mode of operation in writing when opening.")),
        ("/ Tax, control and succession", "What families get wrong.",
         ul("<strong>Whose money is it:</strong> interest is taxed in the hands of the person who contributed the funds; adding a name does not move income for tax.",
            "<strong>NRE interest:</strong> exempt only while the account holder is non-resident; a resident joint holder does not change that.",
            "<strong>TDS:</strong> banks deduct TDS based on the first holder&rsquo;s status; NRO interest for non-residents carries higher TDS, which can be adjusted in the return or reduced under a DTAA.",
            "<strong>Operating for a parent:</strong> a power of attorney or bank mandate is often better than a joint account if the aim is paying bills.",
            "<strong>On death:</strong> the survivor gets access, but other legal heirs may still claim the money under succession law - a will and nominations keep it clean.")
         + call_box("NRI joint accounts", ["Choosing joint holding, nomination or power of attorney",
                                           "Redesignating resident accounts to NRO",
                                           "Tax on interest and TDS",
                                           "Repatriating NRO balances",
                                           "Succession planning for parents' accounts"],
                    "Accounts, holders and order, residency, what you want to achieve.")
         + sources("FEMA (Deposit) Regulations and the RBI Master Direction on deposits and accounts; RBI circulars A.P. (DIR Series) No. 13 of 2011 and No. 87 of 2014 and RBI FAQs on accounts of non-residents; Income-tax Act, 1961 (sections 10(4)(ii) and 195) and the corresponding provisions of the Income-tax Act, 2025; site NRE / NRO, moving abroad and NRO to NRE pages.")),
    ],
    faqs=[("Can an NRI open a joint account with a resident parent?", "Yes. An NRI can hold an NRE or FCNR(B) account jointly with a resident close relative such as a parent on a former or survivor basis, and an NRO account can also be held jointly with a resident. The resident can operate the NRE account during the NRI's lifetime only as a power of attorney holder."),
          ("Can an NRI be a joint holder in a parent's resident savings account?", "Yes, banks may add an NRI close relative as joint holder on a former or survivor basis. The NRI cannot operate the account while the parent is alive, and if the NRI becomes the survivor, the account is converted into an NRO account."),
          ("What does former or survivor mean?", "Only the first-named holder (the former) operates the account during their lifetime. The second holder can operate it only after the first holder's death."),
          ("Who pays tax on interest in a joint account?", "The person whose money is in the account. Adding a joint holder does not shift the income. NRE interest is exempt only while the holder is non-resident, and NRO interest for non-residents carries TDS."),
          ("Is a joint account better than a power of attorney for helping parents?", "Not always. A joint account affects ownership and succession; a power of attorney or bank mandate lets you operate without changing ownership. The right choice depends on what you want to achieve."),
          ("What should I send to start?", "WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with the accounts, holders and their order, your and your parent's residency, and what you want to achieve. Or book a call directly.")],
    related=[("can-oci-open-nre-nro-account-nri-bank-accounts-tax-repatriation-2026.html", "NRE and NRO accounts for NRIs and OCIs"),
             ("moving-abroad-from-india-becoming-nri-checklist-savings-account-to-nro-demat-mutual-funds-tax-2026.html", "Becoming an NRI: accounts checklist"),
             ("nro-to-nre-transfer-limit-tax-form-145-146-15ca-15cb-documents-usd-1-million-2026.html", "NRO to NRE transfer and the USD 1 million limit"),
             ("nri-senior-citizen-tax-india-2026-exemption-limit-80ttb-advance-tax-15h-pension-retire-to-india.html", "NRI and senior citizen tax in India")],
    cta_h="Managing accounts with parents in India?", cta_b=C,
    keywords="nri joint account with resident parent, can nri be joint holder in resident savings account, nre account joint holder resident, former or survivor nri, nro joint account resident, nri power of attorney bank account",
    desc="NRI joint bank accounts with a resident parent: NRE / FCNR(B) jointly with a resident close relative on former or survivor basis (resident operates only as power of attorney holder), NRI added to a parent's resident savings account (becomes NRO if NRI survives), NRO joint holding, and tax on interest.",
    howto={"name": "How to set up NRI-parent joint banking correctly", "description": "Choose the structure, then document it.", "steps": [
        {"name": "Redesignate your accounts", "text": "Your own resident savings to NRO on becoming an NRI."},
        {"name": "Pick the structure", "text": "Joint holding (former or survivor), nomination or power of attorney."},
        {"name": "Confirm with the bank", "text": "Mode of operation in writing; close relative proof."},
        {"name": "Keep tax clean", "text": "Interest taxed to the contributor; manage TDS and repatriation."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch LX complete")
