import logging

class GumBallMachine:
    LOW_INDICATOR_AMOUNT = 100
    LOW_INDICATOR_TEXT = f"The machine has less than {LOW_INDICATOR_AMOUNT} gum balls left."
    BALLS_PER_TRANSACTION = 3
    GUMBALL_PRICE = 0.75
    MAX_GUMBALLS = 1000

    LOGGER = logging.getLogger("logger")

    def __init__(self, starting_gumballs = 0):
        self.amount = 0
        self.add_gumballs(starting_gumballs)

    def add_gumballs(self, amount):
        if type(amount) is not int:
            raise TypeError("Number of gum ball needs to be an integer")

        if amount < 0:
            raise ValueError("No negative amount allowed")

        if self.amount + amount > GumBallMachine.MAX_GUMBALLS:
            raise ValueError("Maximum amount of gum balls reached")

        self.amount += amount

    def pay(self, money):
        if not (type(money) is int or type(money) is float):
            raise TypeError("Amount of money is not valid")

        if money < GumBallMachine.GUMBALL_PRICE or money > GumBallMachine.GUMBALL_PRICE:
            raise ValueError("Please enter exact amount")

        if self.amount < GumBallMachine.BALLS_PER_TRANSACTION:
            raise ValueError("Not enough gum balls in the machine")

        self.amount -= GumBallMachine.BALLS_PER_TRANSACTION

        if self.amount < GumBallMachine.LOW_INDICATOR_AMOUNT:
            GumBallMachine.LOGGER.info(GumBallMachine.LOW_INDICATOR_TEXT)

        return GumBallMachine.BALLS_PER_TRANSACTION


