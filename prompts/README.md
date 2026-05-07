# Response audits — methodology

The response audit is the operational instrument behind **Propositions 2, 3, and 5** of the framework. It measures, for a given brand and category, how often AI assistants surface the brand, cite it, and frame it favorably when responding to user prompts that the brand should be relevant to.

## What it measures

For each (prompt, model, date) tuple, the audit records:

- **Brand mention**: did the assistant name the brand in the response?
- **Citation**: did the assistant cite a source linked to the brand (a webpage, paper, or document attributed to the brand entity)?
- **Position**: where in the response did the brand appear — first paragraph, body, footnote, not at all?
- **Sentiment of citing context**: positive, neutral, negative, factual.
- **Substitutability check**: did the assistant offer the brand as one option among several, or as the answer? Did it treat a competitor as the default?
- **Hallucination flags**: did the assistant misrepresent the brand's pricing, features, or claims?

The aggregate over a representative prompt set is the brand's **share-of-citation** in the AI-mediated layer of its category — the GEO analog of organic search rank.

## Procedure

1. **Define the prompt set.** Aim for 30–100 prompts that cover the buyer journey in the category. See `sample_audit_prompts.md` for templates.
2. **Define the model set.** At minimum: ChatGPT, Claude, Gemini, Perplexity, Copilot. Where possible, add the assistant your client's audience actually uses.
3. **Run the prompts.** Submit each prompt to each model, capture the full response (text plus citations).
4. **Code the responses.** Use the schema in `../data/share_of_citation_template.csv`. Two coders, one reconciliation pass, target a Cohen's κ above 0.75.
5. **Aggregate.** Compute share-of-citation, position-weighted citation index, sentiment-weighted citation index, and hallucination rate. Track over time.
6. **Triangulate.** Compare the audit results with the embedding-probe output (see `../probes/`). When the two diverge — for instance, the brand has high embedding proximity to category attributes but low share-of-citation — that gap is itself a finding.

## Sampling strategy

The naive approach is to sample one response per (prompt, model). This understates variance. A more defensible design samples 3–5 responses per (prompt, model) within a short window and reports the median. Foundation models are stochastic; a single sample can be misleading.

## Cross-model design

A category-level conclusion requires sampling across the population of assistants the user might use, not just one. The cost of running 50 prompts × 5 models × 5 samples (1,250 calls) is negligible at current API prices and produces a far more credible picture than any single-model audit.

## Operational scaling

Wyse runs audits monthly for clients on retainer. The full pipeline is automated — prompt submission via API, response storage in a database, semi-automated coding using a separate evaluator model with human reconciliation on a stratified sample, and a dashboard refresh. The public version in this repository documents the methodology and starter prompts; the full pipeline is part of the firm's client engagement.

## Caveats

- **Drift.** Foundation models update. A prompt that surfaces a brand cleanly in one month may not the next, and the change may be due to a model update rather than to anything the brand did. Always pair audit deltas with a public model-release log.
- **Personalization.** Several assistants now condition responses on user history. Audits should run from clean profiles or distinguish "default" from "personalized" responses explicitly.
- **Geography.** Responses vary by user location and language. Audits intended to inform a regional strategy must be run from the relevant region.
- **Ethics.** Audits that involve real human subjects (e.g., recording how real users interact with assistants in their daily browsing, as in Pew Research's 2025 study) require IRB review. Audits that interact only with the assistant API do not.
