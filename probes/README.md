# Embedding probes — semantic equity measurement

The embedding probe is the operational instrument behind **Proposition 5** of the framework and the construct of **semantic equity**. It measures how a brand is represented in the latent space of foundation models, relative to category-relevant attributes and competing brands.

## What it measures

For a target brand B and a set of category-relevant attribute terms A, the probe computes the cosine similarity cos(v_B, v_A) for each attribute, where v_x is the embedding of x in some foundation model's representation space. The same is computed for direct competitors. The output is a brand-by-attribute matrix that quantifies the brand's positioning in the model's substrate.

### Why this matters

When a user asks an AI assistant "what is a reliable mid-range running shoe," the assistant's retrieval and generation layers operate in a representation space where each of those words is a vector. Brands whose vectors cluster near {reliable, mid-range, running, shoe} surface in the response; brands whose vectors cluster elsewhere do not. Semantic equity captures this in a measurable form. It is the AI-substrate analog of customer-based brand equity (Keller, 1993).

## What's in this folder

`embedding_probe.py` — a runnable Python stub that demonstrates the workflow using open-source sentence-transformers. It is intentionally minimal. The full pipeline used in Wyse client engagements adds:

- Cross-model probing across multiple proprietary embedding APIs
- Bootstrapped confidence intervals
- Statistical tests for proximity differences against competitor distributions
- Longitudinal change-point detection
- Visual reports

## Running the stub

```bash
pip install sentence-transformers numpy pandas
python embedding_probe.py
```

The stub uses `all-MiniLM-L6-v2` as a fast default. For real work, run across multiple models — the model choice materially affects results, and a single-model probe is easy to misread.

## Caveats

- **Embedding ≠ retrieval.** Cosine proximity in an embedding model is a useful proxy for retrieval prominence but not identical to it. A full picture combines the embedding probe with the response audit (see `../prompts/`).
- **Tokenizer effects.** Brands with unusual spellings, multi-word names, or non-Latin scripts may have unstable embeddings. Sanity-check the brand vector against simple paraphrases.
- **Model substrate ≠ assistant substrate.** Modern assistants combine multiple representations (retrieval embeddings, generation-model internal states, tool-call signatures). The probe captures one, well-defined slice of that stack.
- **Comparative interpretation.** Absolute cosine values are not meaningful in isolation; comparisons against competitors and against the brand's own history are what carry signal.

## Methodology references

- Bolukbasi et al. (2016), NeurIPS — original analogy-based probe of embedding space.
- Caliskan, Bryson, and Narayanan (2017), Science — WEAT (Word Embedding Association Test).
- Khattab and Zaharia (2020), SIGIR — late-interaction retrieval scoring; useful for moving from embedding similarity to retrieval probability.
