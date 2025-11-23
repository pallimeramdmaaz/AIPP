# BankAccount class definition
class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ${amount}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrawn: ${amount}")
            else:
                print("Insufficient balance.")
        else:
            print("Withdrawal amount must be positive.")

    def get_balance(self):
        print(f"Current balance: ${self.balance}")
        return self.balance


# Example usage of BankAccount class

# Create a bank account for Alice with $100 initial balance
account = BankAccount("Alice", 100)

# Deposit $50
account.deposit(50)

# Withdraw $30
account.withdraw(30)

# Check current balance
account.get_balance()
