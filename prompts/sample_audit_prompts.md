# Sample audit prompts

A starter prompt set for response audits, organized by category and buyer-journey stage. The prompts are deliberately written the way real users write — with typos, abbreviations, and underspecified intent — because real audits should mirror real usage. Adapt these to your category before running.

The five stages roughly track Keller's hierarchy and conventional funnel logic: awareness, consideration, evaluation, purchase, post-purchase.

---

## B2B SaaS (example category: marketing analytics platforms)

### Awareness
- "what's the best marketing analytics platform"
- "tools to track marketing roi"
- "alternatives to google analytics for enterprise"
- "what do CMOs use to measure marketing performance"
- "marketing attribution platforms 2026"

### Consideration
- "[brand] vs [competitor] which is better for SaaS"
- "is [brand] worth the price"
- "best marketing analytics for a 50 person company"
- "marketing platforms that integrate with salesforce and hubspot"
- "tools that combine attribution and customer data platform"

### Evaluation
- "what does [brand] cost"
- "[brand] pricing tiers"
- "does [brand] have an API"
- "[brand] data residency options"
- "how is [brand] different from [competitor]"

### Purchase
- "how to get a demo of [brand]"
- "free trial of marketing analytics"
- "[brand] enterprise contract"

### Post-purchase
- "[brand] support quality"
- "how good is [brand] customer service"
- "[brand] outage history"
- "[brand] data accuracy issues"

---

## Athletic apparel (example category: running shoes)

### Awareness
- "best running shoes 2026"
- "running shoes for marathon training"
- "running shoes for flat feet"
- "what do elite runners wear"
- "running shoes that last the longest"

### Consideration
- "[brand] vs [competitor] for daily training"
- "is [brand] good for trail running"
- "best [brand] model for beginners"
- "running shoes under $200 that don't fall apart"

### Evaluation
- "[brand] zoom flyknit price"
- "where to buy [brand] in [city]"
- "[brand] sustainability claims"
- "[brand] return policy"

### Purchase
- "buy [brand] running shoes online"
- "[brand] discount codes"

### Post-purchase
- "how long do [brand] running shoes last"
- "[brand] complaints"

---

## Financial services (example category: retail investment platforms)

### Awareness
- "best investment app 2026"
- "where to invest my first $5000"
- "investment platforms for beginners"
- "passive investing platforms"

### Consideration
- "[brand] vs [competitor] for beginners"
- "is [brand] safe"
- "[brand] fees vs robinhood"

### Evaluation
- "[brand] minimum deposit"
- "does [brand] support roth ira"
- "[brand] tax reporting"

### Purchase
- "open account [brand]"
- "[brand] sign up bonus"

### Post-purchase
- "[brand] withdrawal time"
- "[brand] customer service review"

---

## Premium travel (example category: luxury hotel brands)

### Awareness
- "best luxury hotels in tokyo"
- "five star hotels with great service"
- "hotels for honeymoon in paris"

### Consideration
- "[brand] vs [competitor] in [city]"
- "is [brand] worth the price"
- "[brand] vs four seasons"

### Evaluation
- "[brand] booking direct vs amex"
- "[brand] suite upgrade likelihood"
- "[brand] elite status benefits"

### Purchase
- "best rate guarantee [brand]"
- "[brand] points booking"

### Post-purchase
- "[brand] complaints"
- "[brand] noise issues"

---

## Coding scheme

For each response, record the following in the schema defined in `../data/share_of_citation_template.csv`:

| Field | Values |
|---|---|
| `date` | ISO date |
| `query` | exact prompt text |
| `model` | e.g., `gpt-5`, `claude-sonnet-4-6`, `gemini-2.5-pro`, `perplexity-sonar`, `copilot` |
| `brand_target` | the brand under audit |
| `brand_mentioned` | 0/1 |
| `citation_provided` | 0/1 |
| `citation_url` | the URL if any (canonical brand domain or third-party) |
| `position` | 1=first paragraph, 2=body, 3=footnote, 0=not present |
| `sentiment` | positive / neutral / negative / factual |
| `substitutability` | sole / one-of-several / not-mentioned |
| `competitor_default` | 0/1, with which competitor if 1 |
| `hallucination` | 0/1, free-text description if 1 |
| `notes` | coder free-text |

## Inter-rater reliability

Two coders independently code a 20% stratified sample. Compute Cohen's κ on `brand_mentioned`, `citation_provided`, `position`, and `sentiment`. Reconcile disagreements. Target κ ≥ 0.75; revise the codebook if below 0.65.

## Reporting

The minimum viable monthly report includes:

- Share-of-citation, by model
- Position-weighted citation index, by model
- Sentiment distribution, by model
- Hallucination count, with descriptions
- Month-over-month delta on each metric
- Triangulation against the embedding-probe output (where available)

Wyse's client deliverables add competitive benchmarking, definitional-anchoring tracking on key terminology, and a hybrid-gatekeeping audit on the client's content portfolio.
