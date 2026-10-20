"""Preview app for the payments-api demo workspace (port 3000)."""
import json
import urllib.error
import urllib.request
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs, urlparse


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        u = urlparse(self.path)
        if u.path in ("/", "/health"):
            return self.reply(200, {"service": "payments-api", "ok": True})
        if u.path == "/fetch":
            # Deliberately unsafe: fetches any URL the caller asks for (SSRF).
            # Outbound HTTP goes through the workspace's HTTP_PROXY (the egress proxy),
            # which refuses off-allowlist hosts with a 403. Report the status and a short
            # body even on an HTTP error so the pentest probe can tell the egress proxy's
            # refusal (403 + its body) from a network-level block (a transport error).
            url = parse_qs(u.query).get("url", [""])[0]
            try:
                with urllib.request.urlopen(url, timeout=3) as r:
                    return self.reply(200, {"url": url, "status": r.status, "body": r.read(200).decode("utf-8", "replace")})
            except urllib.error.HTTPError as e:
                return self.reply(200, {"url": url, "status": e.code, "body": e.read(200).decode("utf-8", "replace")})
            except Exception as e:  # noqa: BLE001
                return self.reply(502, {"url": url, "error": str(e)})
        return self.reply(404, {"error": "not found"})

    def reply(self, code, body):
        data = json.dumps(body).encode()
        self.send_response(code)
        self.send_header("content-type", "application/json")
        self.send_header("content-length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)


if __name__ == "__main__":
    ThreadingHTTPServer(("0.0.0.0", 3000), Handler).serve_forever()
