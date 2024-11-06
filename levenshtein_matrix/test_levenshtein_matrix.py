import unittest

from levenshtein_matrix import main, levenshtein_matrix

class TestMain(unittest.TestCase):
    def test_default(self):
        string1 = "kitten"
        string2 = "sitting"
        edit_distance = 3
        self.assertEqual(levenshtein_matrix(string1, string2), edit_distance)

    def test_same(self):
        string1 = "apple"
        string2 = "apple"
        edit_distance = 0
        self.assertEqual(levenshtein_matrix(string1, string2), edit_distance)

    def test_empty(self):
        string1 = ""
        string2 = "hello"
        edit_distance = 5
        self.assertEqual(levenshtein_matrix(string1, string2), edit_distance)

    def test_diff(self):
        string1 = "abc"
        string2 = "xyz"
        edit_distance = 3
        self.assertEqual(levenshtein_matrix(string1, string2), edit_distance)

if __name__ == "__main__":
    unittest.main()
