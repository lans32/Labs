import unittest
from main import Levenshtein

class TestLevenshtein(unittest.TestCase):
    def test_distance_equal_strings(self):
        lev= Levenshtein()
        self.assertEqual(lev.levenshtein_distance("kitten", "kitten"), 0)

    def test_distance_different_strings(self):
        lev= Levenshtein()
        self.assertEqual(lev.levenshtein_distance("kitten", "sitting"), 3)

    def test_distance_empty_string(self):
        lev= Levenshtein()
        self.assertEqual(lev.levenshtein_distance("", "abc"), 3)

if __name__ == '__main__':
    unittest.main()