import unittest
from src.levcount import count


class TestCount(unittest.TestCase):
    def test_counts(self):
        self.assertEqual(count(["INFO hi", "ERROR bad", "ERROR worse"]), {"INFO": 1, "ERROR": 2})


if __name__ == "__main__":
    unittest.main()
