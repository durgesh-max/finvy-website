# -*- coding: utf-8 -*-
"""Re-applies the cross-link callout boxes added after pages were built (rounds 59-61).
Idempotent: a box is added only if its marker comment is missing. Run after any builder that regenerates these pages:
    python build_callouts.py"""
import os

BOX = ('<!-- {m} --><section class="section"><div style="max-width:900px;margin:0 auto;border:1px solid #E4E7EA;'
       'border-left:4px solid #C2312A;border-radius:10px;padding:14px 18px;background:#F6F7F8;font:400 15px/1.6 Inter,system-ui,sans-serif">'
       '<strong>{t}</strong> {b}</div></section>\n')
PAY = "fast-ds-payment-due-date-interest-calculator-itns-289-form-3-form-4.html"
F40 = "form-40-foreign-retirement-account-401k-ira-uk-pension-rrsp-super-defer-tax-india.html"
TCS = "tcs-refund-foreign-remittance-lrs-how-to-claim-itr-employer-2026.html"
INS = "foreign-life-insurance-policy-returning-nri-schedule-fa-fast-ds-tax-on-maturity.html"
BOXES = {
    "fdpay": ("Filed Form 1?", f'Work out when Form 2 is due, the last date to pay and the 1% interest, and how ITNS 289, Form 3 and Form 4 work: <a href="{PAY}">FAST-DS payment calculator and steps</a>.'),
    "f40": ("Foreign pension after moving back?", f'Defer Indian tax on a 401(k), IRA, UK pension, RRSP or super with <a href="{F40}">Form 40 (formerly Form 10-EE)</a>; Australia is now notified.'),
    "tcsref": ("TCS is refundable.", f'Get it back through your return or your employer: <a href="{TCS}">TCS refund on foreign remittance, step by step</a>.'),
    "fins": ("Still holding a life policy from abroad?", f'It belongs in Schedule FA, and FAST-DS can cover a missed one: <a href="{INS}">foreign insurance policies for returning NRIs</a>.'),
}
TARGETS = {
    "fast-ds-2026-filing-help-chartered-accountant.html": ["fdpay", "fins"],
    "fast-ds-2026-foreign-asset-disclosure-scheme-31-december-deadline.html": ["fdpay"],
    "fast-ds-2026-calculator-foreign-asset-disclosure-cost.html": ["fdpay"],
    "income-tax-email-foreign-assets-fast-ds-what-to-do.html": ["fdpay"],
    "fast-ds-2026-eligibility-checker.html": ["fdpay", "fins"],
    "fast-ds-what-happens-if-i-do-not-declare-black-money-act.html": ["fdpay"],
    "fast-ds-rsu-espp-us-shares-401k-which-category.html": ["fdpay", "f40"],
    "fast-ds-returning-nri-foreign-accounts-not-reported.html": ["fdpay", "f40", "fins"],
    "h1b-holders-returning-to-india-tax-rnor-401k-2026.html": ["f40", "fins"],
    "residential-status-calculator-india-nri-rnor-section-6.html": ["f40"],
    "lrs-tcs-calculator.html": ["tcsref"],
    "tcs-20-foreign-remittance-lrs-india-2026.html": ["tcsref"],
    "year-end-lrs-tcs-20-planning-october-march-2026-27.html": ["tcsref"],
    "parents-send-money-child-studying-abroad-uk-usa-canada-australia-lrs-tcs-2026.html": ["tcsref"],
}
n = 0
for f, marks in TARGETS.items():
    if not os.path.exists(f):
        continue
    s = open(f, encoding="utf-8").read()
    add = "".join(BOX.format(m=m, t=BOXES[m][0], b=BOXES[m][1]) for m in marks if f"<!-- {m} -->" not in s)
    if not add:
        continue
    i = s.rfind("</main>")
    i = i if i > 0 else s.find("<footer")
    open(f, "w", encoding="utf-8").write(s[:i] + add + s[i:])
    n += 1
print("callouts re-applied on", n, "pages")
