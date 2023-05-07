class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit of ${amount} successful. New balance: ${self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Sorry, insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrawal of ${amount} successful. New balance: ${self.balance}")

    def get_balance(self):
        print(f"Current balance: ${self.balance}")
