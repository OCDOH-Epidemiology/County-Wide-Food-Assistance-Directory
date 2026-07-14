# County-Wide Food Assistance Directory

Interactive directory of food pantries, soup kitchens, SNAP, WIC, senior meals, school programs, and farmers markets across Orange County, NY.

## Files

- `index.html` — published directory app (pantries, meals, map)
- `benefits.html` — SNAP, WIC, senior meals, Summer EBT, and school programs
- `page.template.html` + `benefits.template.html` + `generate.py` — rebuild published HTML from `directory.json`
- `directory.json`, `sites.json`, `programs.json`, `program_locations.json` — data
- Source PDF of the June 2026 town directory

## Rebuild

```bash
python3 generate.py
```

This writes both `index.html` and `benefits.html`.
