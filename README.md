# County-Wide Food Assistance Directory

Interactive directory of food pantries, soup kitchens, SNAP, WIC, senior meals, school programs, and farmers markets across Orange County, NY.

## Files

- `index.html` — published directory app
- `page.template.html` + `generate.py` — rebuild `index.html` from `directory.json`
- `directory.json`, `sites.json`, `programs.json`, `program_locations.json` — data
- Source PDF of the June 2026 town directory

## Rebuild

```bash
python3 generate.py
```
