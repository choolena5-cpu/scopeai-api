"""Offline checks only: never calls the paid API or reads runtime credentials."""
from pathlib import Path
from html.parser import HTMLParser
import json
import re

root = Path(__file__).resolve().parents[1]
allowed = {"README.md", "README.en.md", ".gitignore", ".env.example", "openapi.json",
 "docs/status.md", "docs/pricing.md", "docs/faq.md", "docs/use-cases.md", "docs/getting-started.md",
 "examples/python/quickstart.py", "examples/python/scope_client.py", "examples/typescript/scope-client.ts",
 ".github/ISSUE_TEMPLATE/bug_report.md", "scripts/check_public_repo.py", "docs/showcase.md",
 "assets/brand-dark.png", "assets/brand-light.png", "assets/news.png", "assets/lutule-geo.png"}
files = [p for p in root.rglob("*") if p.is_file() and ".git" not in p.relative_to(root).parts and "__pycache__" not in p.relative_to(root).parts]
actual = {str(p.relative_to(root)) for p in files}
assert actual == allowed, f"Unexpected or missing public files: {actual ^ allowed}"
secret = re.compile(r"(?:gh[pousr]_[A-Za-z0-9]{30,}|sk-[A-Za-z0-9]{24,}|-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----)")
class AssetLinks(HTMLParser):
    def __init__(self):
        super().__init__()
        self.targets = []

    def handle_starttag(self, tag, attrs):
        for name, value in attrs:
            if name in {"src", "href"} and value:
                self.targets.append(value)
            elif name == "srcset" and value:
                self.targets.extend(item.strip().split()[0] for item in value.split(",") if item.strip())

for path in files:
    if path.suffix == ".png":
        data = path.read_bytes()
        assert data.startswith(b"\x89PNG\r\n\x1a\n"), f"Invalid image: {path.name}"
        assert len(data) < 2_000_000, f"Oversized image: {path.name}"
        continue  # Images receive visual privacy review before publishing.
    text = path.read_text()
    assert not secret.search(text), f"Possible credential in {path.relative_to(root)}"
    assert ("/" + "Users" + "/") not in text and ("PG" + "PASSWORD") not in text, f"Internal configuration in {path.relative_to(root)}"
    if path.suffix == ".py":
        compile(text, str(path), "exec")
    if path.suffix == ".md":
        html = AssetLinks()
        html.feed(text)
        targets = re.findall(r"\[[^\]]*\]\(([^)]+)\)", text) + html.targets
        for target in targets:
            if "://" in target or target.startswith("#"):
                continue
            assert (path.parent / target.split("#")[0]).is_file(), f"Broken link: {target}"
spec = json.loads((root / "openapi.json").read_text())
def visit(value):
    if isinstance(value, dict):
        if "$ref" in value:
            target = spec
            assert value["$ref"].startswith("#/")
            for part in value["$ref"][2:].split("/"):
                target = target[part.replace("~1", "/").replace("~0", "~")]
        for child in value.values():
            visit(child)
    elif isinstance(value, list):
        for child in value:
            visit(child)
visit(spec)
assert len(spec["paths"]) == 31
assert "接入预览" in (root / "README.md").read_text()
print(json.dumps({"public_files": len(files), "openapi_paths": len(spec["paths"]), "links": "passed", "credential_scan": "passed", "python_syntax": "passed", "network_calls": 0}))
