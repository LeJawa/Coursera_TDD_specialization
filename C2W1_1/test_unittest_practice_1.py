import unittest
from C2W1_1.tested_functions import adder


class TestAdder(unittest.TestCase):
    def test_adds_two_integers_correctly(self):
        self.assertEqual(adder(3, 5), 8)

    def test_adds_negative_numbers_correctly(self):
        self.assertEqual(adder(-2, -5), -7)

    def test_adds_numbers_to_zero_correctly(self):
        self.assertEqual(adder(-9, 9), 0)

    def test_adds_three_integers_correctly(self):
        self.assertEqual(adder(1, 2, -8), -5)

    def test_adds_forty_integers_correctly(self):
        self.assertEqual(adder(1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,3,1,1,1,3,1,1,1,1,1,1,1,1,1,1), 45)

    def test_raises_an_exception_when_given_one_argument(self):
        self.assertRaises(ValueError, lambda: adder(7))

    def test_raises_an_exception_on_string_arguments(self):
        self.assertRaises(TypeError, lambda: adder(2, "12"))