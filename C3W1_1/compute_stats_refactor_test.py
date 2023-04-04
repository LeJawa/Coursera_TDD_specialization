from C3W1_1.compute_stats_refactor import harmonic_mean, variance, standard_dev, count, average, minimum, maximum, summation
import unittest

class TestComputeStats(unittest.TestCase):

    def test_harmonic_mean(self):
        self.assertAlmostEqual(harmonic_mean(), 129.72817300624072)

    def test_variance(self):
        self.assertAlmostEqual(variance(), 81476.493996)

    def test_standard_dev(self):
        self.assertAlmostEqual(standard_dev(), 285.44087653313)

    def test_count(self):
        self.assertEqual(1000, count())

    def test_average(self):
        self.assertAlmostEqual(499.498, average())

    def test_summation(self):
        self.assertEqual(499498, summation())

    def test_minimum(self):
        self.assertEqual(1, minimum())

    def test_maximum(self):
        self.assertEqual(997, maximum())

