"""
embedding_probe.py — minimal reference implementation of a semantic equity probe.

Measures cosine proximity between a target brand's embedding and a set of
category-relevant attribute embeddings, with comparisons against competitor
brands. Output is a CSV with one row per (brand, attribute) pair.

This is a stub. The pipeline Wyse Brand Intelligence runs in client
engagements extends it with cross-model probing, bootstrapped confidence
intervals, and longitudinal change-point detection.

Reference: Figueira, M. G. (2026). From Information Retrieval to Agentic
Action: A Framework for Brand Visibility in AI-Mediated Markets. See
https://github.com/marcosfigueira/brand-erasure-framework.

Usage:
    pip install sentence-transformers numpy pandas
    python embedding_probe.py

Author: Marcos Guimarães Figueira (marcos@wyse.com.br)
License: CC BY 4.0
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
from pathlib import Path
from typing import Iterable, Sequence

import numpy as np


# -----------------------------------------------------------------------------
# Configuration — edit for your category
# -----------------------------------------------------------------------------

TARGET_BRAND = "Wyse Brand Intelligence"

COMPETITORS: list[str] = [
    # Add competitor brand names here
    # "Competitor A",
    # "Competitor B",
]

ATTRIBUTES: list[str] = [
    # Category-relevant attribute terms. The set should reflect the dimensions
    # the brand wants to be associated with — and a few it does NOT want to be
    # associated with, for negative-space measurement.
    "expertise",
    "innovation",
    "trustworthy",
    "premium",
    "data-driven",
    "accessible",
    "generic",   # negative-space attribute
    "outdated",  # negative-space attribute
]

DEFAULT_MODEL = "sentence-transformers/all-MiniLM-L6-v2"


# -----------------------------------------------------------------------------
# Core probe
# -----------------------------------------------------------------------------


def cosine(a: np.ndarray, b: np.ndarray) -> float:
    """Cosine similarity between two 1-D vectors."""
    denom = float(np.linalg.norm(a) * np.linalg.norm(b))
    if denom == 0.0:
        return 0.0
    return float(np.dot(a, b) / denom)


def embed(texts: Sequence[str], model_name: str) -> np.ndarray:
    """
    Encode a list of strings into an embedding matrix of shape (n, d).

    Uses sentence-transformers; swap in a proprietary embedding API for
    cross-model probing.
    """
    from sentence_transformers import SentenceTransformer

    model = SentenceTransformer(model_name)
    return np.asarray(model.encode(list(texts), normalize_embeddings=False))


def probe(
    brands: Iterable[str],
    attributes: Iterable[str],
    model_name: str = DEFAULT_MODEL,
) -> list[dict]:
    """
    Run the probe. Returns a list of records, one per (brand, attribute) pair,
    suitable for direct conversion to CSV or DataFrame.
    """
    brands = list(brands)
    attributes = list(attributes)
    all_texts = brands + attributes
    vectors = embed(all_texts, model_name=model_name)
    brand_vecs = vectors[: len(brands)]
    attr_vecs = vectors[len(brands):]

    today = dt.date.today().isoformat()
    rows: list[dict] = []
    for i, brand in enumerate(brands):
        for j, attr in enumerate(attributes):
            rows.append(
                {
                    "date": today,
                    "model": model_name,
                    "brand": brand,
                    "attribute": attr,
                    "cosine_similarity": round(cosine(brand_vecs[i], attr_vecs[j]), 6),
                }
            )
    return rows


def write_csv(rows: list[dict], path: Path) -> None:
    if not rows:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


# -----------------------------------------------------------------------------
# Reporting helpers
# -----------------------------------------------------------------------------


def summarize(rows: list[dict]) -> None:
    """Print a compact terminal summary grouped by brand."""
    by_brand: dict[str, list[tuple[str, float]]] = {}
    for r in rows:
        by_brand.setdefault(r["brand"], []).append(
            (r["attribute"], r["cosine_similarity"])
        )

    print()
    print("Semantic equity probe results")
    print("=" * 60)
    for brand, items in by_brand.items():
        items.sort(key=lambda x: x[1], reverse=True)
        print(f"\n{brand}")
        print("-" * len(brand))
        for attr, sim in items:
            bar = "█" * int(max(0, sim) * 30)
            print(f"  {attr:<20} {sim:+.3f}  {bar}")
    print()


# -----------------------------------------------------------------------------
# Entry point
# -----------------------------------------------------------------------------


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Semantic equity probe — cosine proximity between brand and attribute vectors."
    )
    parser.add_argument(
        "--model",
        default=DEFAULT_MODEL,
        help=f"Embedding model name (default: {DEFAULT_MODEL})",
    )
    parser.add_argument(
        "--out",
        default="../data/probe_output.csv",
        help="Output CSV path (default: ../data/probe_output.csv)",
    )
    args = parser.parse_args()

    brands = [TARGET_BRAND] + COMPETITORS
    if len(brands) == 1:
        print(
            "Note: only the target brand is configured. Add competitors in "
            "COMPETITORS for relative interpretation."
        )

    rows = probe(brands=brands, attributes=ATTRIBUTES, model_name=args.model)
    write_csv(rows, Path(args.out))
    summarize(rows)
    print(f"Wrote {len(rows)} rows to {args.out}")


if __name__ == "__main__":
    main()
