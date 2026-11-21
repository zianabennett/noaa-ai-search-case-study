# Evaluation design

## Decision to support

Can richer searchable metadata help a user find a relevant record when the user's wording differs from the title? This exercise uses twelve invented records and eight explicit information needs to make the comparison reproducible.

## Comparison

The baseline ranks records by the number of query tokens appearing in the title. The candidate searches the title, descriptive tags, and description after a small dictionary normalizes selected terms. Title matches receive weight 3, tag matches weight 2, and description matches weight 1. Those weights are chosen for this demonstration and are not learned or validated production settings.

Only positive-score records are returned. Ties are broken by document ID to keep the output deterministic. The comparison changes both the indexed fields and normalization, which means it cannot attribute an observed difference to either change individually.

## Judgments and measures

Each query has an explicit set of relevant document IDs and a brief reason. These judgments belong to the fictional fixture and can be inspected in [queries.json](../data/queries.json).

| Measure | Definition | Why it is included |
| --- | --- | --- |
| Hit rate at 3 | Fraction of queries with at least one relevant result in the first three | Whether the user can begin from a relevant result |
| Precision at 3 | Relevant results among the first three divided by 3 | How much irrelevant material appears in the first screen |
| Recall at 3 | Relevant results in the first three divided by all judged relevant records | Coverage of the known useful material |
| Reciprocal rank | 1 divided by the rank of the first relevant result, or 0 when none exists | How far the user must look before finding useful material |

The reported averages weight each query equally. Precision retains a denominator of three when fewer than three results are returned. Reciprocal rank uses the complete positive-score ranking, while the other measures use the first three results.

## Acceptance checks

The evaluator rejects duplicate document IDs and judgments referencing unknown records. Tests cover the metric denominators, an empty result set, a short result set, a deterministic tie, and a representative vocabulary mismatch.

## Limits and next experiment

The query set is small and authored alongside the dictionary. There is no held-out evaluation, independent relevance reviewer, embedding model, language model, or real user study. The fixture cannot demonstrate commercial or scientific search performance.

A stronger next experiment would freeze the method, collect unseen queries, obtain independently reviewed labels, and test title-only, additional fields, and normalization as separate conditions. Timing would distinguish machine response time from the user's complete information-finding task.

[Return to overview](../README.md)
