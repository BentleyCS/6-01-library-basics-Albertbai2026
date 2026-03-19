import unittest
from unittest.mock import patch
import analytics

from assignment import (
    process_expenses,
    test_analyze_scores,
    sanitize_usernames,
    identify_outliers,
    search_and_report,
)

class TestMainFunctions(unittest.TestCase):

    def test_process_expenses(self):
        prices = [100, 200, 0]
        expected = [analytics.apply_markup(p, 0.15) for p in prices]
        self.assertEqual(process_expenses(prices), expected)

    @patch("builtins.input", side_effect=["80", "90", "100"])
    def test_analyze_scores(self, mock_input):
        highest, avg = analyze_scores(3)
        self.assertAlmostEqual(highest, 100.0)
        self.assertAlmostEqual(avg, (80 + 90 + 100) / 3)

    def test_sanitize_usernames(self):
        raw = ["  User One ", "USER_two", "  THIRD  "]
        expected = analytics.clean_text(raw)
        self.assertEqual(sanitize_usernames(raw), expected)

    def test_identify_outliers(self):
        vals = [50, 100, 101, 150]
        expected = analytics.filter_threshold(vals, 100)
        self.assertEqual(identify_outliers(vals), expected)

    @patch("builtins.input", return_value="cherry")
    def test_search_and_report_sorted(self, mock_input):
        items = ["  Apple", "Banana ", "  CHERRY  ", " date "]
        idx = search_and_report(items)
        self.assertEqual(idx, 2)

    @patch("builtins.input", return_value="banana")
    def test_search_and_report_unsorted(self, mock_input):
        items = ["Banana ", "  apple", "CHERRY"]
        idx = search_and_report(items)
        self.assertEqual(idx, 0)

    @patch("builtins.input", return_value="kiwi")
    def test_search_and_report_not_found(self, mock_input):
        items = ["apple", "banana"]
        idx = search_and_report(items)
        self.assertEqual(idx, -1)


if __name__ == "__main__":
    unittest.main()


def process_expenses():
    return None
