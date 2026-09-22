# County-Wide Food Assistance Directory

Interactive directory of food pantries, soup kitchens, SNAP, WIC, senior meals, school programs, and farmers markets across Orange County, NY.

## Files

- `index.html` — published directory app (pantries, meals, map)
- `benefits.html` — SNAP, WIC, senior meals, Summer EBT, and school programs
- `page.template.html` + `benefits.template.html` + `generate.py` — rebuild published HTML from `directory.json`
- `directory.json`, `sites.json`, `programs.json`, `program_locations.json` — data
- `Food Assistance Locations.xlsx` + `import_locations.py` — spreadsheet workflow for editing locations (see below)
- Source PDF of the June 2026 town directory

## Rebuild

```bash
python3 generate.py
```

This writes both `index.html` and `benefits.html`.

## Updating locations from the spreadsheet

`Food Assistance Locations.xlsx` holds every row in `directory.json`'s `sites`
list, split into tabs by program type (Pantry, Senior, Soup Kitchen, SNAP,
Market, WIC, Mini-Pantry, Hot Meals, School) plus an "All Locations" master
tab. **Edit only the "All Locations" tab** — the program-type tabs are
generated reference views and are not read back in. See the "Read Me" tab in
the workbook for column details.

```bash
python3 import_locations.py   # All Locations tab -> directory.json (sites only)
python3 generate.py           # directory.json -> index.html + benefits.html
```

`import_locations.py` matches rows back to `directory.json` by the "ID (do
not edit)" column, so re-running it after small edits produces a small diff.
Leave the ID blank on a new row to add a location; delete a row to remove
one. This is a rebuild-and-republish workflow, not a live runtime fetch —
the spreadsheet itself doesn't drive the published site.
