"""Read the current ScopeAI GEO account balance without creating a paid task."""
import argparse
import json
import os
from scope_client import ScopeClient, ScopeError


def main():
    parser = argparse.ArgumentParser(description="ScopeAI hosted API example; confirm production availability first.")
    parser.parse_args()
    if not os.environ.get("SCOPE_API_KEY"):
        parser.error("Set SCOPE_API_KEY in your server environment.")
    client = ScopeClient(base_url=os.environ.get("SCOPE_BASE_URL", "https://camcat.net"))
    try:
        result = client.request("GET", "/geo/balance")
        print(json.dumps(result, ensure_ascii=False, indent=2))
    except ScopeError as error:
        print(json.dumps({"status": error.status, "response": error.body}, ensure_ascii=False))
        raise SystemExit(1) from None
    except Exception:
        print("Request failed. Verify connectivity and your server-side API key.")
        raise SystemExit(1) from None


if __name__ == "__main__":
    main()
