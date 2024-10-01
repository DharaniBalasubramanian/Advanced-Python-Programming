# Task 2: Object-Oriented Programming (OOP)

#  2.1 Design a Bank Account System
# - Objective: Apply OOP principles to design a real-world application.
# - Instructions:
#   - Step 1: Create a `BankAccount` class with attributes like `account_number`, `account_holder_name`, `balance`, and `account_type`.
#   - Step 2: Implement methods for common operations such as `deposit`, `withdraw`, and `check_balance`. Ensure the `withdraw` method checks for sufficient balance before proceeding.
#   - Step 3: Extend the system by creating subclasses such as `SavingsAccount` and `CurrentAccount`. Each subclass should have specific attributes and methods (e.g., interest calculation for `SavingsAccount`).
#   - Step 4: Add features like transaction history and overdraft protection for `CurrentAccount`.
# - Expected Output: A set of classes representing different types of bank accounts with full functionality, including transaction management and subclass-specific features.


class BankAccount:
    def __init__(self, account_number, account_holder_name, account_type, balance=0):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.account_type = account_type
        self.balance = balance
        self.transaction_history = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited {amount}")
            print(f"Deposited {amount}. New balance is {self.balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew {amount}")
            print(f"Withdrew {amount}. New balance is {self.balance}.")

    def check_balance(self):
        print(f"Current balance is {self.balance}.")

    def show_transaction_history(self):
        if not self.transaction_history:
            print("No transactions available.")
        else:
            print("Transaction History:")
            for transaction in self.transaction_history:
                print(transaction)

# Savings Account class with interest calculation
class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder_name, balance=0, interest_rate=0.05):
        super().__init__(account_number, account_holder_name, "Savings", balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest = self.balance * self.interest_rate
        print(f"Interest for current balance: {interest}")
        return interest

# Current Account class with overdraft protection
class CurrentAccount(BankAccount):
    def __init__(self, account_number, account_holder_name, balance=0, overdraft_limit=1000):
        super().__init__(account_number, account_holder_name, "Current", balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount > self.balance + self.overdraft_limit:
            print("Withdrawal exceeds overdraft limit.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            if self.balance < 0:
                self.overdraft_balance = -self.balance
                print(f"Overdraft of {self.overdraft_balance} used.")
            else:
                self.overdraft_balance = 0
            self.transaction_history.append(f"Withdrew {amount}")
            print(f"Withdrew {amount}. New balance is {self.balance}. Overdraft balance is {self.overdraft_balance}.")

# **Execution and Separation**
print("--- Common Operations on a General Bank Account ---")
account = BankAccount(12345678, "Dharani", "Savings")

# Deposit and check balance
account.deposit(1000)  
account.check_balance()  
print("---------------------------------")

# Withdraw and check balance
account.withdraw(500)  
account.check_balance() 
print("---------------------------------\n")

# *** Savings Account Section ***
print("--- Savings Account Section ---")
# Create a Savings Account with interest
savings_account = SavingsAccount(23456789, "Dharani", 2000, 0.03)
savings_account.deposit(500)
savings_account.check_balance()  
savings_account.calculate_interest() 
savings_account.show_transaction_history()
print("---------------------------------\n")

# *** Current Account Section ***
print("--- Current Account Section ---")
# Create a Current Account with overdraft
current_account = CurrentAccount(34567890, "Dharani", 1000, overdraft_limit=500)
current_account.withdraw(1200)
current_account.withdraw(400)   
current_account.show_transaction_history()
print("---------------------------------")
