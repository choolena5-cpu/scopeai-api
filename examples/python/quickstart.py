"""Defaults to a free balance read. --news explicitly enables a paid request."""
import argparse
import json
import os
from scope_client import ScopeClient, ScopeError


def main():
    parser = argparse.ArgumentParser(description="ScopeAI hosted API example; confirm production availability first.")
    parser.add_argument("--news", action="store_true", help="Read news; may charge up to CNY 0.01")
    parser.add_argument("--request-key", help="Previously saved operation id, unchanged across retries")
    args = parser.parse_args()
    if not os.environ.get("SCOPE_API_KEY"):
        parser.error("Set SCOPE_API_KEY in your server environment.")
    if args.news and not args.request_key:
        parser.error("Paid news requires --request-key; save and reuse the same operation id on retries.")
    client = ScopeClient(base_url=os.environ.get("SCOPE_BASE_URL", "https://camcat.net"))
    try:
        result = client.news(args.request_key) if args.news else client.request("GET", "/geo/balance")
        print(json.dumps(result, ensure_ascii=False, indent=2))
    except ScopeError as error:
        print(json.dumps({"status": error.status, "response": error.body}, ensure_ascii=False))
        raise SystemExit(1) from None
    except Exception:
        print("Request failed. Verify connectivity and reuse your saved request id; do not create another paid operation.")
        raise SystemExit(1) from None


if __name__ == "__main__":
    main()
