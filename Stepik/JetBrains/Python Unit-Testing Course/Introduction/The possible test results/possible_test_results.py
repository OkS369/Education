import unittest


class TestPossibleResults(unittest.TestCase):
    def test_success(self):
        self.assertEqual(1, 1)

    def test_failure(self):
        self.assertEqual(1, 2)

    def test_error(self):
        self.assertEqual(1/0, 1)
