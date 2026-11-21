# Evaluating search quality before adding complexity

A reproducible search-evaluation exercise connected to my work on an AI-assisted knowledge-discovery project during Booz Allen Hamilton's Summer Games program.

## The question

How should a team determine whether a search approach helps a user find the information they need? This project makes that question concrete with a small corpus, explicit relevance judgments, and a comparison of two retrieval methods.

The current exercise contains **12 invented records and 8 authored queries**. It compares title matching with a method that searches additional metadata and normalizes selected terms. The code and data are new AI-assisted portfolio work. They are separate from the original NOAA NESDIS project and its results.

## My experience and contribution

In my Summer Games work, I researched comparable solutions and real-world use cases, explored Ollama and AI queries, participated in benchmarking and testing, refined user stories, and led the structure of the final presentation. Those activities connected technical exploration with the user's task and the explanation presented to stakeholders.

For this portfolio extension, the focus is a complete evaluation workflow that a reviewer can inspect. It includes a defined baseline, transparent scoring, a relevance set with reasons, calculated metrics, and tests for edge cases. There is no dependency on an external model service or paid API.

## What the exercise does

The baseline scores words found in document titles. The candidate expands the searchable material to include tags and descriptions, then applies a small synonym dictionary. Both methods use the same corpus and judgments, and both leave the result set empty when there is no match.

The output reports hit rate at 3, precision at 3, recall at 3, and mean reciprocal rank. A query-level table makes it possible to see which records moved and whether the improvement matches the intended information need. The [computed results](results/evaluation.md) include the interpretation and the important limits of the comparison.

## Product judgment

The central decision was to keep the quality criteria visible. An aggregate score is useful only when its numerator, denominator, and relevance judgments are clear. A team should also distinguish finding any useful result from placing the best result early enough for the user to notice it.

This fixture deliberately includes vocabulary mismatches. Because the records, queries, and dictionary were authored together, the results are an illustration of the evaluation method. They do not estimate performance on unseen queries or a real document collection. A next experiment would introduce held-out queries and isolate the effects of additional fields and normalization.

## Explore the work

| Material | Purpose |
| --- | --- |
| [Product case](docs/product-case.md) | Internship context and decisions behind the new exercise |
| [Evaluation design](docs/evaluation-design.md) | Methods, metric definitions, and limits |
| [Fictional corpus](data/corpus.json) | The complete set of invented records |
| [Queries and judgments](data/queries.json) | Information needs and inspectable relevance labels |
| [Computed results](results/evaluation.md) | Summary and query-level comparisons |
| [Evaluator](evaluate.py) | Dependency-free implementation |

## Run locally

Python 3.9 or later is sufficient. From this repository's folder:

```sh
python3 evaluate.py
python3 -m unittest -v
```

The first command regenerates the JSON and Markdown results. The second checks the metric calculations, data validation, empty-result behavior, and stable ordering. No client data or external credentials are required.

