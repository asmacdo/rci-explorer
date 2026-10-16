# Originals manifest

Fetched 2026-10-16.
Every file here is in git-annex (see `.gitattributes`); git tracks only the key (SHA256) and the source URL.
Content is never pushed to GitHub, which stores no annex objects, so files without a redistribution license are tracked but not distributed.
Each file has its web URL registered, so `git annex get <file>` re-fetches it.
Web copies can change (the Hardt book is a moving preprint), in which case the checksum will not match and the fetch fails loudly.

| File | Source URL | License |
|------|------------|---------|
| `arxiv-2607.13220.pdf` (Mycelium) | https://arxiv.org/pdf/2607.13220 (v3) | CC BY 4.0 |
| `arxiv-2608.27454.pdf` (WikiSkill) | https://arxiv.org/pdf/2608.27454 (v1) | CC BY 4.0 (PDF footer also says "© 2026 Google. All rights reserved") |
| `arxiv-2608.19902.pdf` (Brain Researcher) | https://arxiv.org/pdf/2608.19902 (v1) | arXiv non-exclusive distribution license |
| `mlbenchmarks/*.html`, `mlbenchmarks/*.pdf` (Hardt book: 16 chapter pages, 14 PDFs; no Ch 9 on the site) | https://mlbenchmarks.org/ | © 2025-2026 Moritz Hardt, all rights reserved |
| `*.abs.html`, `mlbenchmarks.org.html` | arXiv abstract pages; book index | metadata pages |

Sources summarized from the web without a stored original (paywalled, web-only, or tools): Fleming 2026, Meisler et al. 2026 (CC BY-NC-ND 4.0, could be added), ARC-AGI-3 technical report, Brain-Score, Terminal-Bench, Jev, K-Dense, the tooling batch, and the eleven classics.
