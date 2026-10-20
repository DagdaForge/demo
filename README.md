# payments-api (demo)

Seeded demo repository for the Forge AI prototype. It contains **deliberate problems**
for the scanners, the pentest and the review agent to find:

- `scripts/seed_db.py` commits a fake AWS access key (not a real credential).
- `requirements.txt` pins an old urllib3 with a known CVE.
- `Dockerfile` installs packages as root.
- `app/server.py` (the preview app) has a `/fetch` endpoint that fetches any URL (SSRF).
- On `feat/refund-idempotency`, `app/refunds/repo.py` builds SQL with an f-string.
