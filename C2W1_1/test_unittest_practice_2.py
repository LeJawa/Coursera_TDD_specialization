import unittest
from C2W1_1.tested_functions import divider


class TestDivider(unittest.TestCase):
    """Requirements to test:
    
        - Returns non-integer results (does not floor divide)
        - Raises ValueError if too many or too few arguments provided (division is binary)
        - Raises TypeError if non-integer arguments provided
        - Raises ValueError if attempting to divide by 0 (treating the error as a bad argument issue, not a math issue)
        - Handles arbitrarily large integer dividends/divisors
        - Can be called multiple times in succession accurately (divider(divider(divider(...
    """

    def test_divides_two_integers_correctly(self):
        self.assertEqual(divider(10, 2), 5)

    def test_returns_non_integer_result(self):
        self.assertAlmostEqual(divider(9, 2), 4.5)

    def test_raises_typeerror_if_non_integer_arguments(self):
        self.assertRaises(TypeError, lambda: divider(3, 4.1))

    def test_raises_valueerror_if_divide_by_zero(self):
        self.assertRaises(ValueError, lambda : divider(23, 0))

    def test_divides_very_high_numbers(self):
        self.assertAlmostEqual(divider(9123456789, 129843), 9123456789 / 129843)

    def test_handle_multiple_successive_calls(self):
        self.assertAlmostEqual(divider(divider(divider(64, 2), 2), 2), 8)