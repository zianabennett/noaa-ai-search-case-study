# Evaluation results

Computed from the invented corpus and query judgments included in this repository. This is a deliberately small educational fixture, not a NOAA or Booz Allen benchmark.

The exercise contains 12 invented documents and 8 authored queries. Both approaches use the same documents and relevance judgments.

| Approach | Hit rate at 3 | Mean precision at 3 | Mean recall at 3 | Mean reciprocal rank |
| --- | ---: | ---: | ---: | ---: |
| title only | 37.5% | 0.125 | 0.375 | 0.375 |
| metadata expanded | 100.0% | 0.375 | 1.000 | 1.000 |

## Query results

| Query | Title only top 3 | Expanded metadata top 3 | Relevant documents |
| --- | --- | --- | --- |
| ocean heat readings | No match | D01, D12, D11 | D01, D12 |
| hurricane rain | No match | D02 | D02 |
| river flood extent | D03, D06 | D03, D06 | D03 |
| wildfire smoke | No match | D04 | D04 |
| crop water stress | No match | D05, D01, D03 | D05 |
| mountain snow cover | D06 | D06, D08 | D06 |
| offshore wind speed | No match | D07 | D07 |
| polar frozen ocean | D10 | D10, D01, D12 | D10 |

## Interpretation

Metadata and a small synonym dictionary recover relevant records for vocabulary mismatches deliberately represented in this fixture. The corpus, queries, labels, and dictionary were authored together. The difference illustrates the evaluation method and cannot estimate performance on unseen tasks or a real collection.

The metadata approach changes both the searchable fields and token normalization. This comparison does not isolate their individual effects. A follow-up experiment would test those changes separately on held-out queries.

[Evaluation design](../docs/evaluation-design.md) · [Return to overview](../README.md)
