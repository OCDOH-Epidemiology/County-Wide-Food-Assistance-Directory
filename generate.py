#!/usr/bin/env python3
"""Generate the Food Assistance Directory HTML page from directory.json + template."""
import json
from pathlib import Path

BUILD = Path(__file__).parent
DIRECTORY = json.loads((BUILD / "directory.json").read_text(encoding="utf-8"))
DATA_JSON = json.dumps(DIRECTORY, separators=(",", ":"), ensure_ascii=False)
TEMPLATE = (BUILD / "page.template.html").read_text(encoding="utf-8")
HTML = TEMPLATE.replace("__DATA__", DATA_JSON)

OUTS = [
    BUILD / "index.html",
]
for out in OUTS:
    out.write_text(HTML, encoding="utf-8")
    print(f"Wrote {out} ({out.stat().st_size:,} bytes)")
