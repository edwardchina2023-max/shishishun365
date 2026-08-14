# Design QA

## Evidence

- Direction board: `/Users/huangshifu/Documents/Codex/2026-07-26/https-chatgpt-com-share-6a65d6fa-d4b4/outputs/shishishun365/design-reference.png`
- Final desktop render: `/Users/huangshifu/Documents/Codex/2026-07-26/https-chatgpt-com-share-6a65d6fa-d4b4/work/site-rebuild/final-full-page.png`
- Final side-by-side comparison input: `/Users/huangshifu/Documents/Codex/2026-07-26/https-chatgpt-com-share-6a65d6fa-d4b4/work/site-rebuild/final-direction-comparison.png`

## Verified Direction

- Header logo uses a standalone, true-path SVG production lockup. The Gujing emblem and supplied wordmark artwork are preserved, while wordmark scale, optical center, symbol spacing, registered mark, wine seal, and clear space are tightened to a single repeatable proportion.
- Hero remains a full-bleed dark product scene with the sole master slogan “喝事事顺酒 事事顺”; the removed first-screen subtitle does not return.
- Screen two is one continuous full-bleed image rather than stacked panels. Its exact title is “顺 / 是一生的修行” and the requested Laozi-by-the-Guo-River appears on the right, looking across the water.
- Screen three starts directly with “事事顺四大旗舰系列”. Four real product bottles share one uninterrupted exhibition stage, with no cream photo cards or bright-red panels.
- The fabricated award medal image is absent. The following brand-history section is text-led and contains no replacement image of uncertain provenance.
- The entire “其余产品，归于特订” section is removed.
- The banquet moment now uses the supplied hall composition with China Red bottles placed across near, middle, and distant tables using distance-appropriate scale, occlusion, contact shadow, and warm reflected light.
- All visible `h1`–`h6` titles are free of Chinese or Western commas and periods.
- Palette is unified around lacquer black, muted wine red, antique gold, warm ivory, and low-saturation photography.

## Responsive and Interaction Checks

- Desktop viewport: 1440 × 900, DPR 1; four flagship bottles remain in one row.
- Mobile viewport: 390 × 844, DPR 1; flagship bottles form a legible two-column gallery.
- Broken image count: 0 at both viewports.
- Horizontal overflow: none (`scrollWidth = innerWidth`) at both viewports.
- Browser console warnings/errors from the website: 0.
- Mobile navigation opens and closes; `aria-expanded` changes correctly.
- Product selector updates active product name, meaning, copy, and specification.
- Semantic headings, landmarks, native buttons, visible focus styles, and reduced-motion support are retained.

## Production Assets

- Vector logo: `assets/images/brand/shishishun-logo-4a.svg`; no embedded raster image or data URI.
- Banquet composite: `assets/images/gen/scene-wedding-china-red.jpg`; the full-resolution PNG master remains archived outside the deployment folder.

## Remaining Low-Risk Note

- Three supplied marketplace product sources contain faint marks within the photographed bottle area. They are kept because product identity must remain exact; clean official bottle cutouts can replace these PNGs one-for-one later without changing the layout.

final result: passed
