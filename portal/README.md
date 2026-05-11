# Client Portal — bharatquantumprospera.com/portal/

The static portal pages (signup, login, dashboard, ITR intake) live in this folder
and are served by GitHub Pages alongside the rest of the site.

The auth + database + file-storage backend is a small PHP app (`api.php`) that
**runs separately on Namecheap** under the subdomain
**`api.bharatquantumprospera.com`**.

## Why split frontend and backend?

GitHub Pages can only serve static HTML/CSS/JS. It cannot run PHP, store files,
or maintain a database. Namecheap shared hosting can. So:

| Layer | Where | What's there |
|---|---|---|
| Static portal UI | GitHub Pages (this folder) | `index.html`, `itr-intake.html` |
| API + storage | Namecheap (subdomain) | `api.php`, `data/portal.sqlite`, `uploads/...` |

The two communicate via CORS-enabled cross-origin fetches, with the session
cookie set on the `api.` subdomain.

## One-time Namecheap setup (≈ 10 minutes)

### 1. Create the subdomain

cPanel → **Domains** → **Subdomains** → **Create New Subdomain**

- Subdomain: `api`
- Domain: `bharatquantumprospera.com`
- Document root: `/home/<your-cpanel-user>/api.bharatquantumprospera.com/`

### 2. Upload the backend files

The full set is in your `CRM/` working folder. Upload these to the document
root of `api.bharatquantumprospera.com`:

- `api.php`
- `.htaccess`
- `data/.htaccess`
- `uploads/.htaccess`

> The `data/portal.sqlite` and per-user upload folders are auto-created on
> first request — you do not upload them yourself.

### 3. Set folder permissions

In File Manager → right-click each → **Permissions**:

| Folder | Permission |
|---|---|
| `data/` | **755** |
| `uploads/` | **755** |

### 4. Enable SSL for the subdomain

cPanel → **SSL/TLS Status** → tick `api.bharatquantumprospera.com` → **Run AutoSSL**.
Wait 2–10 minutes. HTTPS is **required** because the session cookie uses
`SameSite=None; Secure`, which browsers reject over plain HTTP.

### 5. Verify

In a browser, visit:

```
https://api.bharatquantumprospera.com/api.php?action=me
```

Expected response:

```json
{"ok":false,"authenticated":false}
```

If you see that JSON, the backend is live. Now visit
`https://bharatquantumprospera.com/portal/` — the Client Portal tab in the
main nav also lands you there. Create an account, click **Start ITR intake**,
upload a small PDF, and confirm it lands in
`api.bharatquantumprospera.com/uploads/{userId}_{PAN}/...` via File Manager.

## File map on Namecheap after first signup

```
api.bharatquantumprospera.com/
├── api.php                 ← only file you actually upload
├── .htaccess
├── data/
│   ├── .htaccess
│   └── portal.sqlite       ← auto-created on first request
└── uploads/
    ├── .htaccess
    └── 1_ABCDE1234F/
        └── AY_2026-27/
            ├── Salary/
            │   └── 20260511_103415_Form_16.pdf
            └── CapGain/
                └── 20260511_103502_tax_pnl.xlsx
```

## Updating the portal UI later

Just edit `portal/index.html` or `portal/itr-intake.html` in this repo, commit,
and push. GitHub Pages redeploys within ~60 seconds. No Namecheap upload needed.

## Updating the backend later

Edit `api.php` in your CRM working folder, then re-upload to
`api.bharatquantumprospera.com/api.php` via cPanel File Manager.

---

For deeper config (file-size cap, allowed extensions, rate limits, schema),
see the comments at the top of `api.php`.
