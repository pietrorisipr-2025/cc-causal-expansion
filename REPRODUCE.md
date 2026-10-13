# Reproducibility and archive boundaries

## English overview (LaTeX)

From the `report/` directory, run:

```bash
pdflatex -interaction=nonstopmode -halt-on-error CC_CAUSAL_EXPANSION_OPEN_RESEARCH_REPORT_v0.2.tex
pdflatex -interaction=nonstopmode -halt-on-error CC_CAUSAL_EXPANSION_OPEN_RESEARCH_REPORT_v0.2.tex
```

The bibliography is included inline. `REFERENCES.bib` is the citation-audited RC0.2 editable bibliography source. The GitHub copy changes only editorial status labels relative to RC0.2; the scientific main body and bibliography were not changed.

## Full notebook

The cumulative master TeX and all **104 PDF figures** are in `notebook/source/`. From that directory:

```bash
pdflatex -interaction=nonstopmode -halt-on-error CC_CAUSAL_EXPANSION_WORKING_PAPER_v1.03.tex
pdflatex -interaction=nonstopmode -halt-on-error CC_CAUSAL_EXPANSION_WORKING_PAPER_v1.03.tex
pdflatex -interaction=nonstopmode -halt-on-error CC_CAUSAL_EXPANSION_WORKING_PAPER_v1.03.tex
```

**PDF builds may differ byte-for-byte** due to metadata, even if their text and layout agree. Compare page counts and text if validating a rebuild; do not claim matching hashes of non-identical binaries.

## Mathematical audit

The `audits/v1.03/` directory preserves the v1.03 corrected branch's derivation, scripts, protocol and JSON. The complete provenance and older audit executables are in the **canonical v1.03 recovery ZIP**, distributed separately as a GitHub Release asset. Use its own `AUDIT/VERIFY_MANIFEST_V103.py` and `AUDIT/REPLAY_V103.py` as documented in its handoff, from the extracted recovery root.

The older high-cost exhaustive replay of v0.95 was **not rerun** in v1.03. Do not mistake a saved historical PASS result for a new execution.

## Earlier archives

The v1.03 archive inventory identifies **76 scientific ZIPs** from v0.27 through v1.02 retained outside the light recovery. They are **not all included** here. This public starter does not pretend to reproduce every old simulation without their original code/data.
