#!/usr/bin/python3
"""Unittests for max_integer."""


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Define unitests for max integers."""

    def test_with_sorted_list(self):
        """Test max_integer with sorted list."""
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)

    def test_with_unosorted_list(self):
        """Test max_integer with unsorted list."""
        max_int = max_integer([-1, 2, -4, 3, -6, 1, 7, 4])
        self.assertEqual(max_int, 7)

    def test_empty_list(self):
        """Test max_integer with empty list."""
        self.assertIsNone(max_integer())

    def test_with_string(self):
        """Test max_integer with string."""
        self.assertEqual(max_integer("Banana"), "n")

    def test_max_at_beginning(self):
        """Test max integer with max at the begining."""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)


if __name__ == '__main__':
    unittest.main()
