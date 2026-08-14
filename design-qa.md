# Design QA

## Evidence

- Source visual truth: `/Users/huangshifu/Documents/Codex/2026-07-26/https-chatgpt-com-share-6a65d6fa-d4b4/outputs/shishishun365/design-reference.png`
- Browser-rendered desktop implementation: `/Users/huangshifu/Documents/Codex/2026-07-26/https-chatgpt-com-share-6a65d6fa-d4b4/work/site-rebuild/implementation-desktop-final.png`
- Browser-rendered mobile implementation: `/Users/huangshifu/Documents/Codex/2026-07-26/https-chatgpt-com-share-6a65d6fa-d4b4/work/site-rebuild/implementation-mobile-final.png`
- Full top-of-page comparison input: `/Users/huangshifu/Documents/Codex/2026-07-26/https-chatgpt-com-share-6a65d6fa-d4b4/work/site-rebuild/design-comparison-top.png`
- Focused hero comparison input: `/Users/huangshifu/Documents/Codex/2026-07-26/https-chatgpt-com-share-6a65d6fa-d4b4/work/site-rebuild/design-comparison-hero.png`

## Normalization

- Source pixels: 916 × 1717.
- Desktop CSS viewport: 1440 × 1024; device pixel ratio 1; full-page implementation pixels: 1440 × 7506.
- Mobile CSS viewport: 390 × 844; device pixel ratio 1; full-page implementation pixels: 390 × 12297.
- Full top comparison: source scaled to 1440 × 2682 and implementation cropped to the same 1440 × 2682 region, then placed side by side at 2880 × 2682.
- Focused hero comparison: source hero cropped to 916 × 650 and scaled to 1440 × 1022; implementation hero cropped to 1440 × 1022; both shown side by side at 2880 × 1022.
- State: age confirmation accepted; desktop and mobile navigation closed unless explicitly testing the open state; initial product selected unless explicitly testing 事事顺516.
- The two white floating controls visible at the far right of some captures are Chrome-extension overlays, not website UI, and were excluded from the visual judgment.

## Findings

- No remaining P0, P1, or P2 visual or interaction findings.
- Fonts and typography: Noto Serif SC and Noto Sans SC preserve the source's refined Song-style display hierarchy and restrained sans-serif navigation. The master slogan retains the exact text “喝事事顺酒 事事顺”. The second-screen title uses the requested three fixed lines without orphan characters.
- Spacing and layout rhythm: the cinematic split hero, two-column editorial culture section, four-product gallery, and alternating story/craft/moment sections maintain consistent alignment and vertical rhythm. Desktop and mobile show no horizontal overflow.
- Colors and visual tokens: deep wine red, near-black red, antique gold, warm ivory, and ink text match the established visual system. The second-screen right side was intentionally changed from cream to near-black wine red per user feedback.
- Image quality and asset fidelity: the exact supplied brand lockup is used in header, age gate, and footer. All four products use the supplied real product references rather than generated substitutes. Existing premium editorial imagery is reused for culture, craft, and occasion sections.
- Copy and content: the first-screen “一杯酒，敬……” subtitle was removed. Public-facing cultural copy avoids pricing, channel tactics, targets, distributor identities, equity, and other commercial-sensitive material.
- Accessibility and interaction: semantic headings and landmarks are present; focus styles are visible; reduced-motion preferences are respected; mobile menu supports open, close, link navigation, and Escape; all four product selectors expose button semantics and update the live detail region.

## Comparison History

1. Earlier finding [P2]: the second-screen light panel no longer matched the user's desired dark treatment. Fix: changed the right panel to near-black wine red and remapped heading, body, and divider colors to gold and warm white. Post-fix evidence: `design-comparison-top.png` and desktop culture capture.
2. Earlier finding [P2]: the second-screen three-line title wrapped “祝愿” and “修行” into orphan characters at desktop width. Fix: wrapped each requested line as a nonbreaking display line and widened the manifesto column. Post-fix evidence: desktop culture capture and `design-comparison-top.png`.
3. Earlier finding [P2]: product selectors declared `role=listitem`, overriding native button semantics. Fix: removed the conflicting roles while retaining the grouped product gallery label. Post-fix evidence: browser role lookup found one 事事顺516 button; click changed `aria-pressed` to `true` and updated the detail copy/spec.
4. Earlier finding [P2]: the mobile product heading left “品” alone on a second line. Fix: reduced the mobile-only heading scale and letter spacing and kept the heading on one line. Post-fix evidence: 390 px responsive capture.
5. Earlier finding [P2]: the bespoke-section link had inadequate contrast. Fix: returned it to the warm-gold link treatment on the red surface. Post-fix evidence: full desktop and mobile captures.
6. Earlier finding [P2]: the mobile menu overlay covered the brand lockup. Fix: raised the real brand image above the menu surface. Post-fix evidence: mobile open-menu interaction test.

## Primary Interactions Tested

- Adult-age confirmation dismisses the gate and persists the accepted state.
- Desktop navigation and anchor destinations render correctly.
- Mobile menu opens, closes, and reports `aria-expanded` accurately.
- 事事顺516 selector changes active state and updates the product meaning, description, and specification.
- Scroll reveal activates all 39 reveal elements on desktop and mobile.
- Broken image count: 0.
- Browser console warnings/errors: 0.

## Follow-up Polish

- [P3] The supplied marketplace-origin product images contain faint source watermarks. They are retained to preserve exact bottle and packaging identity. Replace them one-for-one if clean official cutouts become available; no layout change is required.

## Implementation Checklist

- [x] Exact brand wordmark used.
- [x] Master slogan fixed across principal brand placements.
- [x] Four flagship products and meanings updated.
- [x] Other products grouped as bespoke.
- [x] Humanistic copy added without commercial-sensitive details.
- [x] Desktop and mobile responsive layouts verified.
- [x] Core navigation, menu, age gate, and product selection verified.
- [x] SEO metadata, canonical URL, robots file, and sitemap prepared for GitHub Pages.

final result: passed
