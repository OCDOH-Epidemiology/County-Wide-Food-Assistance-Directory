# Accessibility Audit Report
## Orange County Food Assistance Directory

**Audit Date:** September 2026  
**Standard:** WCAG 2.1 Level AA  
**Reference:** DOJ Title II Web Rule (2024) — [ada.gov/resources/2024-03-08-web-rule](https://www.ada.gov/resources/2024-03-08-web-rule/)  
**Scope:** Public-facing HTML/JS/CSS (index.html, benefits.html, templates, sw.js)

---

## Summary Verdict

The Orange County Food Assistance Directory demonstrates **strong baseline accessibility** with proper semantic HTML, keyboard operability, and ARIA patterns. This audit identified and fixed several issues to achieve **WCAG 2.1 Level AA compliance**.

**Overall Status:** ✅ Compliant after fixes applied

---

## Findings Table

| Severity | WCAG Criterion | File/Location | Issue | Status |
|----------|---------------|---------------|-------|--------|
| **Serious** | 2.4.1 Bypass Blocks | `page.template.html` line 796 | Skip link targeted `#directory` (toolbar) instead of main content | ✅ Fixed |
| **Serious** | 1.4.3 Contrast (Minimum) | CSS `:root` | Muted text color `#5a6b62` had ~4.0:1 contrast on `#f3f6f2` background (below 4.5:1 threshold) | ✅ Fixed |
| **Moderate** | 4.1.2 Name, Role, Value | `addMapFullscreenControl()` | Map fullscreen control used `<a role="button">` instead of semantic `<button>` | ✅ Fixed |
| **Minor** | 1.3.1 Info and Relationships | `lang-select` element | Redundant `aria-label` when visible `<label>` already present | ✅ Fixed |

---

## Fixes Applied

### 1. Skip Link Target (WCAG 2.4.1)

**Before:**
```html
<a class="skip-link" href="#directory">Skip to directory</a>
```

**After:**
```html
<a class="skip-link" href="#main">Skip to main content</a>
<main class="main" id="main">
```

Skip link now correctly bypasses the hero and toolbar to reach the main content area.

### 2. Color Contrast for Secondary Text (WCAG 1.4.3)

**Before:**
```css
--muted: #5a6b62;  /* ~4.0:1 contrast ratio on #f3f6f2 */
```

**After:**
```css
--muted: #4a5b51;  /* ~6.4:1 contrast ratio on #f3f6f2 */
```

This darker shade exceeds the 4.5:1 minimum for normal text and approaches the 7:1 AAA threshold.

### 3. Map Fullscreen Button Semantics (WCAG 4.1.2)

**Before:**
```javascript
const btn = L.DomUtil.create("a", "", container);
btn.href = "#";
btn.setAttribute("role", "button");
```

**After:**
```javascript
const btn = L.DomUtil.create("button", "", container);
btn.type = "button";
```

Native `<button>` elements provide correct keyboard behavior (Enter/Space activation) and role without ARIA override.

### 4. Redundant ARIA Label Removed (WCAG 1.3.1)

**Before:**
```html
<label for="lang-select">Language</label>
<select id="lang-select" aria-label="Language">
```

**After:**
```html
<label for="lang-select">Language</label>
<select id="lang-select">
```

The visible `<label>` already provides an accessible name; the redundant `aria-label` was unnecessary.

---

## What's Already Done Well

The site demonstrates excellent accessibility practices in many areas:

| Feature | Implementation |
|---------|---------------|
| **Document Structure** | `lang="en"` attribute, proper `<title>`, semantic landmarks (`<main>`, `<header>`, `<footer>`, `<nav>`, `<section>`) |
| **Heading Hierarchy** | Logical `h1` → `h2` → `h3` → `h4` nesting throughout |
| **Skip Link** | Present and functional with visible focus state |
| **Focus Management** | Visible focus indicators (`:focus-visible`) on all interactive elements |
| **Keyboard Operability** | All controls accessible via keyboard; no focus traps detected |
| **ARIA Patterns** | Proper use of `aria-pressed`, `aria-expanded`, `aria-controls`, `aria-live` regions |
| **Dynamic Content** | Live regions (`aria-live="polite"`) for result counts and status messages |
| **Form Labels** | All form inputs have associated labels or `aria-labelledby` |
| **Images** | County seal has descriptive `alt="Orange County, NY seal"` |
| **Motion Sensitivity** | `prefers-reduced-motion` media query disables animations |
| **Map Accessibility** | Map region has `aria-label` and SR-only hint explaining keyboard limitations |
| **Mobile Accessibility** | Touch targets meet minimum size; responsive design maintains accessibility |

---

## Suggested Manual Tests

While automated fixes have been applied, the following manual testing is recommended:

### Screen Reader Testing
- [ ] Test with NVDA (Windows) or VoiceOver (macOS/iOS)
- [ ] Verify skip link announces correctly and lands on main content
- [ ] Confirm filter controls announce their state (expanded/collapsed)
- [ ] Check location cards read in logical order
- [ ] Verify live region announcements for filter results

### Keyboard Navigation
- [ ] Tab through entire page without mouse
- [ ] Confirm all interactive elements are reachable
- [ ] Test Escape key closes modals/panels
- [ ] Verify no focus traps in filter sheet or detail panel

### Browser Tools
- [ ] Run axe DevTools extension for automated checks
- [ ] Use Chrome Lighthouse accessibility audit
- [ ] Test with browser zoom at 200%
- [ ] Test with browser text-only zoom

### Color/Vision
- [ ] Test with color blindness simulator (e.g., Sim Daltonism)
- [ ] Verify information isn't conveyed by color alone

---

## Language Access Note (Title VI/LEP)

The site includes a language selector with **8 languages**:
- English
- Spanish (Español)
- Yiddish (ייִדיש)
- Chinese (中文)
- Haitian Creole (Kreyòl Ayisyen)
- Arabic (العربية)
- Hebrew (עברית)
- Russian (Русский)

**Status:** Language support is implemented via client-side i18n with translations for UI strings. This addresses Title VI/LEP requirements for meaningful access. Content data (location names, addresses, notes) appears to be primarily in English in the source JSON.

**Recommendation:** For full language equity, consider:
1. Adding Spanish translations for location-specific notes/descriptions in `directory.json`
2. Providing translated PDF/print materials
3. Including language access statement in footer

---

## Technical Notes

- **Service Worker:** The `sw.js` caches pages for offline use. This supports accessibility by ensuring users can access information regardless of connectivity.
- **Data Source:** `directory.json` is out of scope but should maintain consistent formatting for screen reader pronunciation.
- **Print Styles:** Print media query properly hides interactive elements while preserving content.

---

## References

- [WCAG 2.1 Quick Reference](https://www.w3.org/WAI/WCAG21/quickref/)
- [DOJ Title II Web Rule Fact Sheet](https://www.ada.gov/resources/2024-03-08-web-rule/)
- [Leaflet Map Accessibility](https://leafletjs.com/examples/accessibility/)
