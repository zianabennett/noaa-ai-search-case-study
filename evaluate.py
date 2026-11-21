"""Reproducible search-evaluation exercise using invented records only."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SYNONYMS = {"heat": "temperature", "thermal": "temperature", "rain": "precipitation", "rainfall": "precipitation", "hurricane": "storm", "winds": "wind", "inundation": "flood"}


def tokens(text, expanded=False):
    words = re.findall(r"[a-z0-9]+", text.lower())
    return {SYNONYMS.get(word, word) if expanded else word for word in words}


def rank(query, corpus, expanded=False):
    terms = tokens(query, expanded)
    scored = []
    for doc in corpus:
        title = tokens(doc["title"], expanded)
        if expanded:
            tags = tokens(" ".join(doc["tags"]), True)
            description = tokens(doc["description"], True)
            score = 3 * len(terms & title) + 2 * len(terms & tags) + len(terms & description)
        else:
            score = len(terms & title)
        if score > 0:
            scored.append((score, doc["id"]))
    return [doc_id for _, doc_id in sorted(scored, key=lambda item: (-item[0], item[1]))]


def metrics(ranking, relevant, k=3):
    relevant = set(relevant)
    if not relevant or k <= 0:
        raise ValueError("A positive k and nonempty relevance set are required")
    retrieved = ranking[:k]
    hits = sum(doc in relevant for doc in retrieved)
    reciprocal_rank = next((1.0 / index for index, doc in enumerate(ranking, 1) if doc in relevant), 0.0)
    return {"hit_at_3": int(hits > 0), "precision_at_3": hits / k, "recall_at_3": hits / len(relevant), "reciprocal_rank": reciprocal_rank}


def evaluate(corpus, queries):
    ids = [doc["id"] for doc in corpus]
    if len(ids) != len(set(ids)):
        raise ValueError("Duplicate document IDs")
    query_ids = [query["id"] for query in queries]
    if len(query_ids) != len(set(query_ids)) or not queries:
        raise ValueError("A nonempty query set with unique IDs is required")
    if any(not set(query["relevant_ids"]) <= set(ids) for query in queries):
        raise ValueError("Relevance judgments reference an unknown document")
    output = {}
    for label, expanded in [("title_only", False), ("metadata_expanded", True)]:
        rows = []
        for query in queries:
            ranking = rank(query["text"], corpus, expanded)
            rows.append({"query_id": query["id"], "text": query["text"], "top_3": ranking[:3], **metrics(ranking, query["relevant_ids"])})
        summary = {key: sum(row[key] for row in rows) / len(rows) for key in ["hit_at_3", "precision_at_3", "recall_at_3", "reciprocal_rank"]}
        output[label] = {"summary": summary, "queries": rows}
    return output


def main():
    corpus = json.loads((ROOT / "data/corpus.json").read_text())
    queries = json.loads((ROOT / "data/queries.json").read_text())
    results = evaluate(corpus, queries)
    output = ROOT / "results"
    output.mkdir(exist_ok=True)
    (output / "evaluation.json").write_text(json.dumps(results, indent=2) + "\n")
    lines = ["# Evaluation results", "", "Computed from the invented corpus and query judgments included in this repository. This is a deliberately small educational fixture, not a NOAA or Booz Allen benchmark.", "", f"The exercise contains {len(corpus)} invented documents and {len(queries)} authored queries. Both approaches use the same documents and relevance judgments.", "", "| Approach | Hit rate at 3 | Mean precision at 3 | Mean recall at 3 | Mean reciprocal rank |", "| --- | ---: | ---: | ---: | ---: |"]
    for label, result in results.items():
        s = result["summary"]
        lines.append(f"| {label.replace('_', ' ')} | {s['hit_at_3']:.1%} | {s['precision_at_3']:.3f} | {s['recall_at_3']:.3f} | {s['reciprocal_rank']:.3f} |")
    lines += ["", "## Query results", "", "| Query | Title only top 3 | Expanded metadata top 3 | Relevant documents |", "| --- | --- | --- | --- |"]
    for i, query in enumerate(queries):
        base = ", ".join(results["title_only"]["queries"][i]["top_3"]) or "No match"
        improved = ", ".join(results["metadata_expanded"]["queries"][i]["top_3"]) or "No match"
        lines.append(f"| {query['text']} | {base} | {improved} | {', '.join(query['relevant_ids'])} |")
    lines += ["", "## Interpretation", "", "Metadata and a small synonym dictionary recover relevant records for vocabulary mismatches deliberately represented in this fixture. The corpus, queries, labels, and dictionary were authored together. The difference illustrates the evaluation method and cannot estimate performance on unseen tasks or a real collection.", "", "The metadata approach changes both the searchable fields and token normalization. This comparison does not isolate their individual effects. A follow-up experiment would test those changes separately on held-out queries.", "", "[Evaluation design](../docs/evaluation-design.md) · [Return to overview](../README.md)", ""]
    (output / "evaluation.md").write_text("\n".join(lines))
    print(json.dumps({label: result["summary"] for label, result in results.items()}, indent=2))


if __name__ == "__main__":
    main()
