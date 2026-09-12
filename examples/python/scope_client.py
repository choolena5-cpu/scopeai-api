"""Server-side ScopeAI client. Set SCOPE_BASE_URL and SCOPE_API_KEY in the environment.

Persist a request_key with your business operation before calling paid methods.
Network retries must reuse that key, the same parameters and conditional headers.
"""
import json
import os
import time
import urllib.error
import urllib.parse
import urllib.request


class ScopeError(Exception):
    def __init__(self, status, body):
        self.status, self.body = status, body
        super().__init__(f"Scope API returned HTTP {status}")


class ScopeClient:
    def __init__(self, base_url=None, api_key=None):
        self.base_url = (base_url or os.environ["SCOPE_BASE_URL"]).rstrip("/") + "/api/v1"
        self._key = api_key or os.environ["SCOPE_API_KEY"]

    def request(self, method, path, *, query=None, body=None, request_key=None, max_cents=None, etag=None):
        url = self.base_url + path + (("?" + urllib.parse.urlencode(query)) if query else "")
        headers = {"Authorization": "Bearer " + self._key, "Accept": "application/json"}
        if request_key is not None:
            headers["Idempotency-Key"] = request_key
        if max_cents is not None:
            headers["X-Max-Charge-Cents"] = str(max_cents)
        if etag is not None:
            headers["If-None-Match"] = etag
        data = None if body is None else json.dumps(body, ensure_ascii=False).encode()
        if data is not None:
            headers["Content-Type"] = "application/json"
        request = urllib.request.Request(url, data=data, headers=headers, method=method)
        # Deliberately no automatic retry of writes. The caller keeps the operation id.
        try:
            class NoRedirect(urllib.request.HTTPRedirectHandler):
                def redirect_request(self, req, fp, code, msg, headers, newurl):
                    raise urllib.error.HTTPError(req.full_url, code, "Redirect disabled", headers, fp)
            with urllib.request.build_opener(NoRedirect).open(request, timeout=30) as response:
                raw = response.read()
                return {"status": response.status, "etag": response.headers.get("ETag"), "body": json.loads(raw) if raw else None}
        except urllib.error.HTTPError as error:
            if error.code == 304:
                return {"status": 304, "etag": error.headers.get("ETag"), "body": None}
            raw = error.read()
            try:
                body = json.loads(raw)
            except (ValueError, UnicodeDecodeError):
                body = {"error": {"code": "invalid_error_response"}}
            raise ScopeError(error.code, body) from None

    def quote(self, project_id, revision, questions):
        return self.request("POST", "/geo/quotes", body={"project_id": project_id, "revision": revision,
            "product": "geo.measurement.standard", "target_id": "deepseek-model-api", "questions": questions, "repeats": 1, "max_unit_cents": 100})

    def accept(self, request_key, quote_id, maximum_cents):
        return self.request("POST", "/geo/checks", request_key=request_key, body={"quote_id": quote_id, "max_charge_cents": maximum_cents})

    def wait(self, check_id, timeout_seconds=300):
        deadline = time.monotonic() + timeout_seconds
        while True:
            response = self.request("GET", "/geo/checks/" + urllib.parse.quote(check_id, safe=""))
            if response["body"]["data"]["state"] not in ("queued", "running"):
                return response
            if time.monotonic() >= deadline:
                # Local wait expiry does not cancel or refund the server operation.
                return response
            time.sleep(3)


if __name__ == "__main__":
    print(json.dumps(ScopeClient().request("GET", "/account/balance"), ensure_ascii=False, indent=2))
