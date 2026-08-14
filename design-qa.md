# Design QA

## Evidence

- Source visual truth: `/Users/huangshifu/Documents/Codex/2026-07-26/https-chatgpt-com-share-6a65d6fa-d4b4/outputs/shishishun365/design-reference.png`
- Corrected logo source: `/Users/huangshifu/Desktop/事事顺酒现场照片/IMG_7090.JPG`
- Browser-rendered desktop implementation: `/Users/huangshifu/Documents/Codex/2026-07-26/https-chatgpt-com-share-6a65d6fa-d4b4/work/site-rebuild/redesign-pass2-desktop-full.png`
- Browser-rendered mobile hero: `/Users/huangshifu/Documents/Codex/2026-07-26/https-chatgpt-com-share-6a65d6fa-d4b4/work/site-rebuild/redesign-pass2-mobile-top.png`
- Browser-rendered mobile culture section: `/Users/huangshifu/Documents/Codex/2026-07-26/https-chatgpt-com-share-6a65d6fa-d4b4/work/site-rebuild/redesign-pass2-mobile-culture.png`
- Full comparison input: `/Users/huangshifu/Documents/Codex/2026-07-26/https-chatgpt-com-share-6a65d6fa-d4b4/work/site-rebuild/design-comparison-pass2.png`
- Focused hero comparison input: `/Users/huangshifu/Documents/Codex/2026-07-26/https-chatgpt-com-share-6a65d6fa-d4b4/work/site-rebuild/design-comparison-pass2-hero.png`

## Normalization

- Source pixels: 916 × 1717. It is a three-section direction board rather than a literal viewport capture.
- Desktop CSS viewport: 916 × 900; device pixel ratio 1; implementation pixels: 916 × 6040.
- Mobile CSS viewport: 390 × 844; device pixel ratio 1; implementation document: 390 × 11201.
- Full comparison keeps both source and implementation at native 916 px width. The implementation evidence is cropped after the first three visual chapters (hero, culture, and four-product gallery); differing section heights remain visible instead of being distorted.
- State: age confirmation accepted, navigation closed, initial product selected unless explicitly testing 事事顺516.
- The floating white controls and occasional purple dot visible at the far edge of Chrome captures are browser-extension overlays, not website UI, and were excluded from visual judgment.

## Findings

- No remaining P0, P1, or P2 visual or interaction findings.
- Fonts and typography: Noto Serif SC provides the high-contrast Song-style hierarchy visible in the direction board; navigation and body use Noto Sans SC. The master slogan is one unbroken desktop line and a deliberate two-line mobile lockup. The second-screen title is exactly “顺 / 是最好的祝愿 / 是一生的修行”.
- Spacing and layout rhythm: the first three chapters now follow the direction board's sequence and structure—full-bleed cinematic hero, asymmetrical two-panel culture spread, and one-row four-product museum display. At 916 px the product row remains four columns rather than collapsing prematurely.
- Colors and visual tokens: the page now stays within near-black lacquer, deep wine red, antique gold, and restrained warm ivory. The second-screen right panel is intentionally dark, overriding the earlier cream reference in accordance with the user's later instruction.
- Image quality and asset fidelity: the header, age gate, and footer use a transparent asset extracted from the exact lettering in `IMG_7090.JPG`, not the earlier rounded wordmark. The four product displays use the user's real product photographs. The hero and culture art use the selected cinematic assets from the approved direction.
- Copy and content: the first-screen “一杯酒，敬……” subtitle is absent. The total slogan is exactly “喝事事顺酒 事事顺”. Public-facing copy excludes pricing, channel tactics, targets, distributor identities, equity, and other commercial-sensitive material.
- Accessibility and behavior: headings and landmarks remain semantic; focus styles are visible; all product choices remain native buttons; reduced motion is respected; no horizontal overflow occurs at 916 px or 390 px.

## Comparison History

1. Earlier finding [P1]: the live header used a rounded legacy “事事顺” wordmark, while the user explicitly required the lettering photographed in `IMG_7090.JPG`. Fix: extracted the photographed Gujing emblem and exact three-character wordmark into transparent PNG assets and replaced all principal brand placements. Post-fix evidence: `redesign-pass2-top.png` and the focused hero comparison.
2. Earlier finding [P1]: the hero was divided into two hard columns and allowed the gift box to dominate, unlike the reference's full-bleed cinematic scene. Fix: rebuilt the hero as one photographic field with a left lacquer-black gradient, one-line master slogan, restrained gold CTA, and the product scene held on the right. Post-fix evidence: `design-comparison-pass2-hero.png`.
3. Earlier finding [P1]: at the target 916 px width the four products collapsed into a two-column card grid. Fix: retained a four-column museum row through the desktop breakpoint, removed generic card gaps, and introduced continuous gold dividers and restrained pedestal behavior. Post-fix evidence: `redesign-pass1-products.png` and `design-comparison-pass2.png`.
4. Earlier finding [P1]: large cream sections after the flagship gallery broke the black-red-gold direction and made the page feel like a different site. Fix: remapped story, craft, moments, partnership, and footer surfaces to one continuous lacquer-black/wine-red system. Post-fix evidence: `redesign-pass2-desktop-full.png`.
5. Earlier finding [P2]: the right culture heading wrapped “事” onto an orphan line at 916 px. Fix: widened the editorial text track and reduced the image track while retaining the intended asymmetry. Post-fix evidence: `redesign-pass2-culture.png`.
6. Earlier finding [P2]: the hero still carried the removed “一杯酒，敬……” direction in visible or sharing copy. Fix: removed it from the hero and replaced the social description with the fixed master slogan.

## Primary Interactions Tested

- Mobile menu opens and closes; `aria-expanded` changes from `false` to `true` and back.
- 事事顺516 selector changes the active product, meaning, description, and specification.
- Broken image count: 0.
- Browser console warnings/errors: 0.
- Desktop horizontal overflow: none at 916 px.
- Mobile horizontal overflow: none at 390 px (`scrollWidth = innerWidth = 390`).

## Follow-up Polish

- [P3] Three supplied product photos contain faint marketplace-origin watermarks. They are retained because exact product identity is more important than substituting clean but incorrect generated packaging. Clean official cutouts can replace them one-for-one without a layout change.
- [P3] The direction board is a compressed concept collage; the production hero remains viewport-height on desktop and mobile so the main scene reads at a premium scale. This is an intentional responsive translation rather than a literal section-height copy.

## Implementation Checklist

- [x] Exact photographed `IMG_7090` wordmark used in all principal brand placements.
- [x] Full-bleed hero composition aligned with the direction board.
- [x] First-screen subtitle removed and master slogan fixed.
- [x] Second-screen three-line title fixed and both panels dark.
- [x] Four flagship products held in one desktop row.
- [x] Lower-page palette unified with the black-red-gold system.
- [x] Desktop and mobile responsive layouts verified.
- [x] Core navigation, mobile menu, age gate, and product selection preserved.
- [x] SEO metadata points to the intended GitHub Pages address.

final result: passed
