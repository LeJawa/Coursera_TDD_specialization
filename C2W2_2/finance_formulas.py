
class Finance:
    """
    This is a class which implements several
    finance formulas using the TDD
    approach:
    """

    @staticmethod
    def cash_flow(income, expenses):
        if income < 0:  
            return
        return income - expenses

    @staticmethod
    def net_worth(assets, debts):
        return assets - debts

    @staticmethod
    def net_income(revenue, expenses):
        return revenue - expenses

    @staticmethod
    def simple_interest(principal, annual_interest_rate, time_in_years):
        return principal * (1 + annual_interest_rate)**time_in_years

    @staticmethod
    def gains(market_price, purchase_price):
        return (market_price - purchase_price) / purchase_price
