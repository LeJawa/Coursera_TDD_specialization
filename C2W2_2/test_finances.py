
import unittest
from C2W2_2.finance_formulas import Finance


class TestFinances(unittest.TestCase):
    def test_cash_flow(self):
        t1 = Finance()
        self.assertEqual(t1.cash_flow(10000, 5500), 4500)

    def test_net_worth(self):
        t2 = Finance()
        self.assertEqual(t2.net_worth(10000, 2000), 8000)

    def test_net_income(self):
        t3 = Finance()
        self.assertEqual(t3.net_income(10000, 5000), 5000)

    def test_simple_interest(self):
        t4 = Finance()
        self.assertEqual(round(t4.simple_interest(100, 0.1, 10), 2), 259.37)

    def test_gains_or_losses(self):
        t5 = Finance()
        self.assertEqual(t5.gains(100, 80), 0.25)


if __name__ == '__main__':
    unittest.TestCase()
