#!/usr/bin/env python3
"""Generate the Food Assistance Directory HTML pages from directory.json + templates."""
import json
from pathlib import Path

BUILD = Path(__file__).parent
DIRECTORY = json.loads((BUILD / "directory.json").read_text(encoding="utf-8"))
DATA_JSON = json.dumps(DIRECTORY, separators=(",", ":"), ensure_ascii=False)

OUTS = [
    (BUILD / "page.template.html", BUILD / "index.html"),
    (BUILD / "benefits.template.html", BUILD / "benefits.html"),
]

for template_path, out_path in OUTS:
    html = template_path.read_text(encoding="utf-8").replace("__DATA__", DATA_JSON)
    if "__DATA__" in html:
        raise SystemExit(f"Placeholder __DATA__ still present in {template_path.name}")
    out_path.write_text(html, encoding="utf-8")
    print(f"Wrote {out_path.name} ({out_path.stat().st_size:,} bytes)")
