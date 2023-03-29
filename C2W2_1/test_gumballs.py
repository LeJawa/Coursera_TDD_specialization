import unittest
from C2W2_1.GumBallMachine import GumBallMachine

class TestGumBalls(unittest.TestCase):
    """
    Convert the requirements into
    unit tests here.
    """

    def test_GumBallMachine_exists(self):
        self.assertTrue(GumBallMachine())

    def test_max_gumballs_per_machine_is_defined(self):
        self.assertTrue(GumBallMachine.MAX_GUMBALLS)

    def test_add_few_gumballs_to_empty_machine(self):
        machine = GumBallMachine()
        machine.add_gumballs(1)

        self.assertEqual(machine.amount, 1)

    def test_raises_typeerror_if_add_string(self):
        machine = GumBallMachine()
        with self.assertRaises(TypeError):
            machine.add_gumballs("0")

    def test_raises_valueerror_if_add_negative_number_of_gumballs(self):
        machine = GumBallMachine()
        with self.assertRaises(ValueError):
            machine.add_gumballs(-1)

    def test_creation_of_non_empty_machine_contains_gumballs(self):
        machine = GumBallMachine(1)

        self.assertEqual(machine.amount, 1)

    def test_add_few_gumballs_to_non_empty_machine(self):
        machine = GumBallMachine(1)
        machine.add_gumballs(1)

        self.assertEqual(machine.amount, 2)

    def test_create_machine_with_max_gumballs(self):
        machine = GumBallMachine(GumBallMachine.MAX_GUMBALLS)

        self.assertEqual(machine.amount, GumBallMachine.MAX_GUMBALLS)

    def test_raises_valueerror_when_max_gumballs_surpassed(self):
        machine = GumBallMachine(GumBallMachine.MAX_GUMBALLS)
        with self.assertRaises(ValueError):
            machine.add_gumballs(1)

    def test_gumball_price_defined(self):
        self.assertTrue(GumBallMachine.GUMBALL_PRICE)

    def test_balls_per_transaction_defined(self):
        self.assertTrue(GumBallMachine.BALLS_PER_TRANSACTION)

    def test_low_indicator_defined(self):
        self.assertTrue(GumBallMachine.LOW_INDICATOR_AMOUNT)

    def test_get_three_gumballs_for_exact_price_amount(self):
        machine = GumBallMachine(GumBallMachine.MAX_GUMBALLS)
        gumballs_returned = machine.pay(GumBallMachine.GUMBALL_PRICE)
        self.assertEqual(gumballs_returned, GumBallMachine.BALLS_PER_TRANSACTION)

    def test_raises_typeerror_for_non_number_amount_of_money(self):
        machine = GumBallMachine()
        with self.assertRaises(TypeError):
            machine.pay("0")

    def test_raises_valueerror_for_less_than_price_amount(self):
        machine = GumBallMachine()
        with self.assertRaises(ValueError):
            machine.pay(0)

    def test_raises_valueerror_for_more_than_price_amount(self):
        machine = GumBallMachine()
        with self.assertRaises(ValueError):
            machine.pay(GumBallMachine.GUMBALL_PRICE + 1)

    def test_raises_valueerror_if_not_enough_gum_balls_available(self):
        machine = GumBallMachine()
        with self.assertRaises(ValueError):
            machine.pay(GumBallMachine.GUMBALL_PRICE)

    def test_log_message_when_machine_is_on_low(self):
        machine = GumBallMachine(GumBallMachine.LOW_INDICATOR_AMOUNT + GumBallMachine.BALLS_PER_TRANSACTION - 1)

        with self.assertLogs() as log:
            machine.pay(GumBallMachine.GUMBALL_PRICE)

        self.assertEqual(log.output, ["INFO:logger:"+GumBallMachine.LOW_INDICATOR_TEXT])



if __name__ == '__main__':
    unittest.main(argv=['ignored', '-v'], exit=False)