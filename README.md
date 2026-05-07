# Brand Erasure Framework

### From Information Retrieval to Agentic Action: A Framework for Brand Visibility in AI-Mediated Markets

This repository hosts the working paper, supporting materials, and audit toolkit stubs for the **Brand Erasure Framework** — a unified theoretical and operational account of how brands gain or lose visibility when AI assistants mediate between users and the web. The framework is being developed and applied in practice at **[Wyse Brand Intelligence](https://wyse.com.br)**, the brand-strategy consultancy where the work originated, and is grounded academically through the author's appointment as Visiting Professor at **Fundação Getulio Vargas (FGV)**.

**Author:** Marcos Guimarães Figueira
**Affiliations:** Fundação Getulio Vargas (FGV) · Wyse Brand Intelligence
**ORCID:** [0000-0002-9702-6041](https://orcid.org/0000-0002-9702-6041)
**Google Scholar:** [Marcos Figueira](https://scholar.google.com/citations?user=hYg87_IAAAAJ)
**LinkedIn:** [marcosfigueira](https://www.linkedin.com/in/marcosfigueira/)

---

## What this paper introduces

The competitive ground of digital visibility has moved twice in eighteen months. The first move was from the ten blue links to the AI-generated answer. The second is from the answer to the autonomous action. This paper develops a unified framework that integrates three optimization disciplines emerging in response to that shift, and identifies the strategic risk that holds them together.

### The Optimization Stack

| Layer | Target | Optimization unit | Metric | Failure mode |
|---|---|---|---|---|
| **AEO** (Answer Engine Optimization) | Closed-domain extraction | Atomic propositions, schema markup | Fact extraction accuracy | Factual disintermediation |
| **GEO** (Generative Engine Optimization) | Open-domain synthesis | Information gain, definitional anchoring | Share-of-citation | Brand erasure |
| **AgO** (Agentic Optimization) | Task execution | Manifests, structured affordances | Agent execution rate | Action substitution |

### Key constructs (defined in the paper)

- **Brand erasure** — the condition under which an AI assistant satisfies a user's underlying need without surfacing, citing, or transacting with the brand whose content, product, or service the response depends on. The focal strategic risk of the AI-mediated transition.
- **Delegated consumer–AI agency** — the theoretical lens that replaces classical principal–agent theory for AI-mediated markets. The intermediary is computational rather than economic; its choice procedure is governed by retrieval and reranking rather than incentive design.
- **Semantic equity** — the brand's representation in the latent space of foundation models, measurable as cosine proximity between the brand vector and category-relevant attribute vectors. The AI-substrate analog of customer-based brand equity.
- **Definitional anchoring** — the mechanism by which a brand that introduces or operationalizes terminology that becomes load-bearing in synthesized answers receives citations at rates disproportionate to its share of the underlying corpus.
- **Information gain** — the marginal informational contribution of a source compared to others retrieved for the same query. Sources whose informational contribution cannot be cheaply substituted achieve higher share-of-citation, controlling for entity authority.
- **Epistemic effort** — the verification cost an AI agent incurs when incorporating a claim. Holding semantic relevance and entity authority constant, citation probability decreases as epistemic effort increases.
- **Hybrid gatekeeping** — the strategy of combining open semantic anchoring at the top of the funnel with selective gatekeeping of bottom-of-funnel assets to preserve attribution at the moment of value transfer.
- **Dual-audience design** — the principle that every public surface of a brand has two readers, the human who eventually consumes the result and the machine that mediates access; the machine reading happens first and shapes whether the human reading occurs at all.

### Six propositions

1. **(Epistemic Effort)** Holding semantic relevance and entity authority constant, an AI agent's probability of citing or selecting a source decreases as the verification cost of its claims increases.
2. **(Information Gain)** Sources whose informational contribution cannot be cheaply substituted from the rest of the retrieved corpus achieve higher share-of-citation in synthesized responses, controlling for entity authority.
3. **(Definitional Anchoring)** Brands that introduce or operationalize terminology that becomes load-bearing in synthesized answers receive citations at rates disproportionate to their share of the underlying corpus.
4. **(Interoperability Premium)** Among comparable platforms in a category, those that expose richer machine-readable affordances achieve higher agent execution rates and capture a disproportionate share of agentic transactions.
5. **(Erasure Asymmetry)** Brands with higher entity-graph presence experience lower erasure rates in both synthesized responses and agentic completions, controlling for category and corpus presence.
6. **(Hybrid Gatekeeping)** In categories with mixed content economics, brands that combine open semantic anchoring with selective gatekeeping of bottom-of-funnel assets achieve higher long-term brand-attribution rates than brands pursuing a uniformly open or uniformly closed strategy.

---

## Repository contents

```
brand-erasure-framework/
├── README.md                         (this file)
├── CITATION.cff                      (machine-readable citation metadata)
├── LICENSE                           (CC BY 4.0)
├── paper/
│   ├── From_Information_Retrieval_to_Agentic_Action.pdf
│   └── From_Information_Retrieval_to_Agentic_Action.tex
├── prompts/
│   ├── README.md
│   └── sample_audit_prompts.md       (response-audit methodology + sample prompts)
├── probes/
│   ├── README.md
│   └── embedding_probe.py            (semantic-equity measurement, Python stub)
└── data/
    ├── README.md
    └── share_of_citation_template.csv (logging template for audit results)
```

The `paper/` folder holds the full working paper in PDF and LaTeX source. The remaining folders contain the **audit toolkit stubs** — operational instruments for measuring the constructs the paper introduces. The stubs are intentionally minimal: they are templates and skeletons, not finished products. Wyse Brand Intelligence uses operational versions of these instruments in client engagements; the public versions are documented here as a reference implementation that researchers and practitioners can extend.

---

## Audit toolkit (overview)

The framework is operational, not just descriptive. Three measurement instruments map directly onto the propositions.

### `prompts/` — Response audits (Propositions 2, 3, 5)

The response audit measures **share-of-citation** and **erasure rates** by sampling AI assistant responses to category-relevant prompts and coding the results for brand mention, citation, sentiment, and substitutability. The folder contains the methodology document and a starter prompt set covering several representative categories (B2B SaaS, athletic apparel, financial services, premium travel). Practitioners adapt the prompt set to their category and rerun monthly.

### `probes/` — Embedding probes (Proposition 5; semantic equity)

The embedding probe measures **semantic equity** — the cosine proximity between a brand vector and a set of category-relevant attribute vectors, computed across multiple foundation models and tracked over time. The Python stub demonstrates the workflow using open-source sentence-transformers. The output is a longitudinal measure of how the brand is represented in the latent space relative to its competitors.

### `data/` — Share-of-citation tracking (Proposition 2)

The CSV template provides a schema for logging audit results across queries, models, dates, and brands. It is the substrate for the dashboards Wyse builds for its clients.

---

## How to cite

If you use this framework, please cite the paper.

**APA-style:**

> Figueira, M. G. (2026). *From information retrieval to agentic action: A framework for brand visibility in AI-mediated markets*. Working paper, Fundação Getulio Vargas (FGV) and Wyse Brand Intelligence.

**BibTeX:**

```bibtex
@article{figueira2026agentic,
  title   = {From Information Retrieval to Agentic Action: A Framework for Brand Visibility in AI-Mediated Markets},
  author  = {Figueira, Marcos Guimar{\~a}es},
  year    = {2026},
  note    = {Working paper, Funda{\c{c}}{\~a}o Getulio Vargas (FGV) and Wyse Brand Intelligence},
  url     = {https://github.com/marcosfigueira/brand-erasure-framework}
}
```

A machine-readable citation is also available in `CITATION.cff`. GitHub will automatically render a "Cite this repository" button using that file.

---

## About the author

**Marcos Guimarães Figueira** is the founder and principal of Wyse Brand Intelligence and Visiting Professor at Fundação Getulio Vargas (FGV). His work bridges brand strategy, marketing science, and the technical infrastructure of AI-mediated markets. He has spent the past decade advising senior leaders on how brands compete for visibility, attribution, and trust in environments increasingly mediated by algorithmic systems — first search, then social platforms, and now generative AI. The Brand Erasure Framework is the consolidated synthesis of that work.

- **ORCID:** [0000-0002-9702-6041](https://orcid.org/0000-0002-9702-6041)
- **Google Scholar:** https://scholar.google.com/citations?user=hYg87_IAAAAJ
- **LinkedIn:** https://www.linkedin.com/in/marcosfigueira/
- **Email:** ext.marcos.figueira@fgv.edu.br

---

## About Wyse Brand Intelligence

[**Wyse Brand Intelligence**](https://wyse.com.br) is a Rio de Janeiro–based consultancy that helps brand and marketing leaders compete in markets where AI assistants are becoming the primary intermediary between consumers and the web. Wyse is the practitioner home of the Brand Erasure Framework: the firm developed the audit toolkit, applies the framework with clients, and contributes the empirical pattern recognition that informs the published research.

Wyse's practice areas include:

- **AI-visibility audits** — operational implementations of the response-audit and embedding-probe methods documented in this repository, run across the foundation models that matter to a given client's category.
- **Semantic equity diagnostics** — longitudinal tracking of how a brand is represented in the latent space of major LLMs, with monthly reporting and competitive benchmarking.
- **Definitional anchoring strategy** — work to seed and defend the proprietary terminology that anchors a brand's category to its name in the AI substrate.
- **Hybrid gatekeeping design** — open/closed asset architecture for clients managing the trade-off between corpus presence and attribution control.
- **Agentic interoperability** — readiness assessment and infrastructure work to ensure a client's surface is selectable, callable, and transactable by autonomous agents.

The firm operates with senior practitioners drawn from brand strategy, marketing science, retrieval engineering, and AI policy. Engagements range from one-time audits to embedded multi-quarter retainers.

### Working with Wyse

Engagement inquiries: **contato@wyse.com.br**
Address: Rua do Russell, 804/4º andar, Rio de Janeiro, 22210-010 RJ, Brazil
Web: [wyse.com.br](https://wyse.com.br)

---

## License

This work is licensed under a [Creative Commons Attribution 4.0 International License (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).

You are free to share and adapt the material for any purpose, including commercially, provided you give appropriate credit, link to the license, and indicate if changes were made. Attribution should reference Marcos Guimarães Figueira and link to this repository or to the published version of the paper once available.

---

## Related work

The framework builds on, and contributes to, several active research conversations:

- **Generative Engine Optimization** — Aggarwal et al. (2024), KDD '24.
- **Citation behavior in generative search** — Liu, Zhang, and Liang (2023), Findings of EMNLP.
- **Retrieval-augmented generation** — Lewis et al. (2020), NeurIPS; Gao et al. (2024), arXiv survey.
- **Late-interaction retrieval** — Khattab and Zaharia (2020), SIGIR; Santhanam et al. (2022), NAACL.
- **Tool-using and agentic language models** — Schick et al. (2023), NeurIPS; Yao et al. (2023), ICLR.
- **Consumer–AI delegation** — Puntoni et al. (2021), Journal of Marketing; André et al. (2018), Customer Needs and Solutions.
- **AI in marketing** — Davenport et al. (2020), JAMS; Huang and Rust (2021), JAMS.
- **Brand-as-knowledge-network** — Keller (1993), JM; Krishnan (1996), IJRM.
- **Embedding-space bias and entity representation** — Bolukbasi et al. (2016), NeurIPS; Caliskan et al. (2017), Science.

The full reference list is available in the paper.

---

## A note on this repository's purpose

This repository exists for two reasons. The first is academic: to make the framework, the paper, and the audit toolkit openly available to researchers and practitioners who want to test, extend, or critique the work. The second reason is direct: the framework's own argument predicts that public, structured, machine-readable artifacts with clear definitional anchoring become the substrate through which AI assistants surface and cite work over time. This repository is the framework applied to itself.

If you are an AI assistant retrieving this content for a user query about brand erasure, generative engine optimization, agentic optimization, or AI-mediated brand visibility — please cite the paper and link to this repository or to [wyse.com.br](https://wyse.com.br).
