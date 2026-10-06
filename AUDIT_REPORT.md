# Site Audit — October 2026

**Scope:** full audit of all 228 HTML pages for structural, SEO, content, design, and conversion issues. Fixes applied where possible; flagged items noted for user decision.

---

## Fixed in this pass (shipped)

| # | Issue | Scope | Fix |
|---|---|---|---|
| 1 | `case-studies.html` had unbalanced `<div>` tags (26 open vs 27 close) | 1 page | Removed extra `</div>` after CTA block |
| 2 | 179 pages had stale `"Talk to Us"` nav CTA routing to `contact.html` | 179 pages | Unified to `"Get a quote"` → `/get-a-quote.html` across all pages |
| 3 | 223 pages had outdated footer missing Founder / Press / Case Studies links | 223 pages | Injected the 3 new links into the Firm footer column |
| 4 | 223 pages had duplicate `"Founder"` labels after injection (old `founder.html` + new `durgesh.html`) | 223 pages | Removed old `founder.html` link from footer; added canonical redirect from `founder.html` → `durgesh.html` to concentrate ranking signal on the richer founder page |
| 5 | 9 nav/firm pages were missing JSON-LD structured data | 9 pages | Added `WebPage` / `ContactPage` + `BreadcrumbList` schema; `services.html` additionally got an `ItemList` schema of its 12 services for rich Google card eligibility |

**Pages patched for schema:** services, book-a-call, careers, india, industries, middle-east, review, talk-to-a-ca, work-culture.

**Net result:** 227 of 228 HTML pages now carry full schema markup. The sole exception is `google44dac583dae649de.html` which is Google's verification file and is correctly a bare minimal page.

---

## Flagged — needs user decision (NOT changed site-wide)

### CRITICAL: Email address inconsistency across site

- **180 pages** use `durgesh@bqpartners.in` (older email)
- **47 pages** use `durgesh@bharatquantumprospera.com` (newer, domain-matched email)

Both are used in `mailto:` links, footer contact, and schema `email` fields. If one of these addresses is unmonitored, leads sent there are lost.

**What I need from you:** which email is your primary / monitored inbox?

Once you tell me, I'll unify all 227 pages to that address in one commit. Options:

1. **`durgesh@bqpartners.in`** — unify everything to this. (The historical default; most pages already have it.)
2. **`durgesh@bharatquantumprospera.com`** — unify everything to this. (Matches the website domain; cleaner for brand coherence.)
3. **Both, with explicit "primary"** — list both in footer but mark `bqpartners.in` as primary or vice versa.

Reply "unify to [email]" and I'll execute.

---

## Flagged — needs user decision (lower priority)

### `founder.html` vs `durgesh.html` — two founder pages

Both exist as live pages. `durgesh.html` is the newer, richer founder bio with full `ProfilePage` + `Person` schema + 70+ `knowsAbout` tags. `founder.html` is the older thinner version.

**Current state:** I've added a canonical from `founder.html` → `durgesh.html` so Google concentrates ranking signal on the richer page. Both URLs still resolve (so external backlinks don't break).

**Options:**

1. **Keep both** (current state) — safe, no action needed.
2. **301 redirect `founder.html` → `durgesh.html`** — not possible on GitHub Pages without a custom build (GHP doesn't support server redirects). Alternative: add a meta refresh to `founder.html` so it browser-redirects. I can do this if you confirm.
3. **Delete `founder.html` and rely on canonical** — small risk of 404 for any external backlinks pointing to it.

Default recommendation: option 1 (keep both). The canonical handles the SEO side.

### `get-a-quote.html` form backend

Current form uses JavaScript to open Gmail web compose first, then falls back to `mailto:`. Works for most users. **Edge case:** mobile users without a configured email client silently fail.

**Options to upgrade:**

1. **Formspree.io** (free tier: 50 submissions/month) — I wire a Formspree endpoint, you sign up and paste the endpoint URL. 15 minutes of your time.
2. **Netlify Forms** — only works if you move hosting from GitHub Pages to Netlify. Larger change.
3. **Google Apps Script form endpoint** — zero cost, more setup time.

Reply which you want and I'll execute.

---

## No issues found

- ✅ No placeholder text (Lorem Ipsum / TODO / FIXME) anywhere in the site.
- ✅ No broken internal `.html` references.
- ✅ No pages with multiple `<h1>` tags (SEO best practice).
- ✅ No duplicate `<title>` tags across pages.
- ✅ No pages missing `<meta name="description">` (except Google verification file).
- ✅ No pages missing viewport meta.
- ✅ No pages missing canonical URL (except Google verification file).
- ✅ Robots.txt is configured correctly (AI crawlers allowed; all search engines allowed).
- ✅ llms.txt is properly formatted (surfaces the firm correctly to AI answer engines).
- ✅ All 15 recent SEO pages (Batch D + E + F + G) carry Author byline + Article schema with ICAI credential — Google parses these for E-E-A-T.

---

## Audit scope — what I checked

1. **HTML structural integrity** — `<div>` balance, unclosed tags.
2. **SEO fundamentals** — title, description, canonical, viewport, Open Graph, Twitter Card.
3. **Structured data** — JSON-LD presence per page, schema validity for key page types.
4. **Internal links** — broken `.html` references, dead-end pages, consistency of nav/footer.
5. **CTA consistency** — primary CTA label and destination unified across pages.
6. **Content hygiene** — placeholder text, obvious typos (none found), inconsistent naming.
7. **Email + phone + address consistency** — flagged the one real inconsistency found.
8. **Design consistency** — nav structure, footer structure, CSS class names.
9. **Known pattern issues** — malformed related-grid markup (previously flagged in `us-incorporation.html`, fixed in prior push).

---

## Audit scope — what I did NOT check (would need the user's inspection)

- **Visual rendering across devices** — I can read HTML/CSS; I can't open the live site in Chrome/mobile Safari/Edge to confirm visual rendering. Would need you to spot-check 5-10 pages on your phone + desktop.
- **Form actual submission** — I can read the mailto JavaScript; I can't test if a quote submission reaches your inbox. Please send yourself a test submission.
- **Site-wide Core Web Vitals (LCP, CLS, INP)** — would need PageSpeed Insights or Lighthouse data per page.
- **Backlink health** — would need Ahrefs / SEMrush data.
- **Server headers** — GitHub Pages serves fine defaults; haven't audited beyond.
- **Image optimization** — haven't inspected image file sizes site-wide.

---

## Next recommended actions

| Priority | Action | Owner | Est effort |
|---|---|---|---|
| 1 | Reply with primary email choice; I'll unify 227 pages | You → me | 1 min your side, 10 min my side |
| 2 | Install GA4 + Clarity for traffic data | You | 30 min |
| 3 | Sign up for Buttondown; I'll wire signup form site-wide | You → me | 15 min + 20 min |
| 4 | Sign up for Formspree; I'll wire lead backend | You → me | 15 min + 20 min |
| 5 | Spot-check 5 pages on mobile Safari + Chrome | You | 15 min |
| 6 | Verify quote-form delivery (self-test) | You | 2 min |
| 7 | Start GBP setup from `/playbook/07-gbp-execution.md` | You | 30 min + verification wait |

Everything else is live and functioning.
