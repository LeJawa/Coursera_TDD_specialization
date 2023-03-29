import unittest

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

    def test_add_few_gumballs_to_non_empty_machine(self):
        machine = GumBallMachine()
        machine.add_gumballs(1)
        machine.add_gumballs(1)

        self.assertEqual(machine.amount, 2)

    def test_add_max_gumballs_in_machine(self):
        machine = GumBallMachine()
        machine.add_gumballs(GumBallMachine.MAX_GUMBALLS)

        self.assertEqual(machine.amount, GumBallMachine.MAX_GUMBALLS)

    def test_raises_valueerror_when_max_gumballs_surpassed(self):
        machine = GumBallMachine()
        with self.assertRaises(ValueError):
            machine.add_gumballs(GumBallMachine.MAX_GUMBALLS + 1)


if __name__ == '__main__':
    unittest.main(argv=['ignored', '-v'], exit=False)