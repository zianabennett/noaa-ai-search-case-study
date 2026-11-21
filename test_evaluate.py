import copy
import json
import unittest
from pathlib import Path
from evaluate import evaluate, metrics, rank

ROOT = Path(__file__).resolve().parent


class SearchEvaluationTests(unittest.TestCase):
    def setUp(self):
        self.corpus = json.loads((ROOT / "data/corpus.json").read_text())
        self.queries = json.loads((ROOT / "data/queries.json").read_text())

    def test_metrics_use_correct_denominators_and_rank(self):
        result = metrics(["X", "A", "B"], ["A", "B"])
        self.assertAlmostEqual(result["precision_at_3"], 2/3)
        self.assertEqual(result["recall_at_3"], 1)
        self.assertEqual(result["reciprocal_rank"], 0.5)

    def test_no_matches_are_not_filled_with_arbitrary_documents(self):
        self.assertEqual(rank("zzzzunmatched", self.corpus, True), [])
        self.assertEqual(metrics([], ["D01"])["hit_at_3"], 0)

    def test_short_results_still_use_fixed_precision_cutoff(self):
        self.assertAlmostEqual(metrics(["D01"], ["D01"])["precision_at_3"], 1/3)

    def test_duplicate_ids_rejected(self):
        with self.assertRaises(ValueError):
            evaluate(self.corpus + [self.corpus[0]], self.queries)

    def test_unknown_judgment_rejected(self):
        queries = copy.deepcopy(self.queries)
        queries[0]["relevant_ids"].append("MISSING")
        with self.assertRaises(ValueError):
            evaluate(self.corpus, queries)

    def test_ties_are_stable_under_input_reordering(self):
        self.assertEqual(rank("ocean", self.corpus, True), rank("ocean", list(reversed(self.corpus)), True))

    def test_dictionary_maps_rain_query_to_precipitation_record(self):
        self.assertEqual(rank("hurricane rain", self.corpus, True)[0], "D02")


if __name__ == "__main__":
    unittest.main()
