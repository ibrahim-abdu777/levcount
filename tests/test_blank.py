import unittest
from src.levcount import count


class TestBlank(unittest.TestCase):
    def test_blank(self):
        self.assertEqual(count(["", "   "]), {})


if __name__ == "__main__":
    unittest.main()
