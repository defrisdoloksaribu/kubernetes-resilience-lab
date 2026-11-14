"""Small HTTP fixture for reproducible Kubernetes integration tests."""

import json
import os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlsplit


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        path = urlsplit(self.path).path
        if path == "/":
            self.send_json(200, {"status": "running", "version": "ci"})
        elif path == "/healthz":
            self.send_json(200, {"status": "healthy"})
        else:
            self.send_json(404, {"status": "not_found"})

    def send_json(self, status, data):
        body = json.dumps(data).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "8000"))
    with ThreadingHTTPServer(("0.0.0.0", port), Handler) as server:
        server.serve_forever()
