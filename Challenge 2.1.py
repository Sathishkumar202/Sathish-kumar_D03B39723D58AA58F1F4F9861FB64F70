class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance=0):
        self._account_number = account_number
        self._account_holder_name = account_holder_name
        self._account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self._account_balance += amount
            print(f"Deposited ${amount}. New balance: ${self._account_balance:.2f}")
        else:
            print("Invalid deposit amount. Please enter a positive value.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self._account_balance:
            self._account_balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self._account_balance:.2f}")
        else:
            print("Invalid withdrawal amount or insufficient balance.")

    def display_balance(self):
        print(f"Account Number: {self._account_number}")
        print(f"Account Holder Name: {self._account_holder_name}")
        print(f"Account Balance: ${self._account_balance:.2f}")

# Create an instance of the BankAccount class
account1 = BankAccount("123456", "John Doe", 1000)

# Test deposit and withdrawal functionality
account1.display_balance()
account1.deposit(500)
account1.withdraw(200)
account1.display_balance()
account1.withdraw(2000)
account1.display_balance()