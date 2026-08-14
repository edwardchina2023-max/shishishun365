# Design QA

## Evidence

- Direction board: `/Users/huangshifu/Documents/Codex/2026-07-26/https-chatgpt-com-share-6a65d6fa-d4b4/outputs/shishishun365/design-reference.png`
- Pass 3 desktop render: `/Users/huangshifu/Documents/Codex/2026-07-26/https-chatgpt-com-share-6a65d6fa-d4b4/work/site-rebuild/redesign-pass3-desktop-full.png`
- Pass 3 culture render: `/Users/huangshifu/Documents/Codex/2026-07-26/https-chatgpt-com-share-6a65d6fa-d4b4/work/site-rebuild/redesign-pass3-culture.png`
- Pass 3 flagship render: `/Users/huangshifu/Documents/Codex/2026-07-26/https-chatgpt-com-share-6a65d6fa-d4b4/work/site-rebuild/redesign-pass3-products.png`
- Side-by-side comparison input: `/Users/huangshifu/Documents/Codex/2026-07-26/https-chatgpt-com-share-6a65d6fa-d4b4/work/site-rebuild/design-comparison-pass3.png`

## Verified Direction

- Header logo is recomposed from the supplied Gujing emblem and the exact photographed `IMG_7090.JPG` wordmark. The Chinese wordmark is deliberately smaller than the previous combined lockup.
- Hero remains a full-bleed dark product scene with the sole master slogan “喝事事顺酒 事事顺”; the removed first-screen subtitle does not return.
- Screen two is one continuous dark spread. Its exact title is “顺 / 是一生的修行。” and the right side shows the requested Laozi-by-the-Guo-River, looking across the water.
- Screen three starts directly with “事事顺四大旗舰系列”. Four real product bottles share one uninterrupted exhibition stage, with no cream photo cards or bright-red panels.
- The fabricated award medal image is absent. The following brand-history section is text-led and contains no replacement image of uncertain provenance.
- The entire “其余产品，归于特订” section is removed.
- Palette is unified around lacquer black, muted wine red, antique gold, warm ivory, and low-saturation photography.

## Responsive and Interaction Checks

- Desktop viewport: 916 × 900, DPR 1; four flagship bottles remain in one row.
- Mobile viewport: 390 × 844, DPR 1; flagship bottles form a legible two-column gallery.
- Broken image count: 0 at both viewports.
- Horizontal overflow: none (`scrollWidth = innerWidth`) at both viewports.
- Browser console warnings/errors from the website: 0.
- Mobile navigation opens and closes; `aria-expanded` changes correctly.
- Product selector updates active product name, meaning, copy, and specification.
- Semantic headings, landmarks, native buttons, visible focus styles, and reduced-motion support are retained.

## Remaining Low-Risk Note

- Three supplied marketplace product sources contain faint marks within the photographed bottle area. They are kept because product identity must remain exact; clean official bottle cutouts can replace these PNGs one-for-one later without changing the layout.

final result: passed
