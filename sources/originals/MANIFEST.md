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
| `engelbart-1962/Doug_Engelbart-AugmentingHumanIntellect.pdf` (scan; OCR text layer is unusable) | https://www.dougengelbart.org/pubs/papers/scanned/Doug_Engelbart-AugmentingHumanIntellect.pdf | 1962 SRI report under US Air Force contract; hosted by the Doug Engelbart Institute; license not stated |
| `engelbart-1962/augmenting-human-intellect.html` (Institute full-text edition, used for reading) | https://www.dougengelbart.org/content/view/138/ | © Doug Engelbart Institute |
| `engelbart-1962/about-nics.html` | https://www.dougengelbart.org/content/view/191/ | © Doug Engelbart Institute |
| `drexler-2019-reframing-superintelligence.pdf` | https://www.futureofhumanityinstitute.org/s/2019-1.pdf | FHI Technical Report 2019-1; license not stated |
| `arxiv-2505.22954.pdf` (Darwin Gödel Machine) | https://arxiv.org/pdf/2505.22954 | CC BY 4.0 |
| `arxiv-2512.05356.pdf` (Weston & Foerster, co-improvement) | https://arxiv.org/pdf/2512.05356 | arXiv non-exclusive distribution license |
| `arxiv-2106.11184.pdf` (Park et al., preprint of the 2023 Nature paper) | https://arxiv.org/pdf/2106.11184 | CC BY 4.0 |
| `nber-w23782.pdf` (Bloom et al., working paper of the 2020 AER paper) | https://www.nber.org/system/files/working_papers/w23782/w23782.pdf | NBER working paper; © the authors |
| `nielsen-qiu-2022-vision-of-metascience.html` | https://scienceplusplus.org/metascience/index.html | © the authors |
| `repronim.org/*.html` (21 pages: about, why, approach, principles and sub-pages, EAB, publications, collaborators, fellowship, participate, resources, tools, ReproLake, training, pond-lake tutorial, news, home) | https://repronim.org/ (each file's URL registered) | © ReproNim; license not stated |
| `narayanan-kapoor-2025-ai-as-normal-technology.html` | https://knightcolumbia.org/content/ai-as-normal-technology | © the authors / Knight Institute |

Sources summarized from the web without a stored original (paywalled, web-only, or tools): Bryk et al. NIC work (Carnegie site blocks scripted fetches), Fleming 2026, Meisler et al. 2026 (CC BY-NC-ND 4.0, could be added), ARC-AGI-3 technical report, Brain-Score, Terminal-Bench, Jev, K-Dense, the tooling batch, and the eleven classics.
