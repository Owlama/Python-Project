from account import Account
class SavingsAccount(Account):
    def __init__(self, account_number, balance):
        super().__init__(account_number, balance)
        self.withdrawal_limit = 5000

    def withdraw(self, amount):
        if amount > self.withdrawal_limit:
            return "Sorry, you have exceeded the maximum withdrawal limit of $5,000"
        else:
            return super().withdraw(amount)



