class BankAccount:
    """Represents a bank account with encapsulated operations."""

    def __init__(self, initial_balance=0):
        """Initializes account balance."""
        self.__account_balance = initial_balance

    def deposit(self, amount):
        """Deposits specified amount into the account."""
        self.__account_balance += amount

    def withdraw(self, amount):
        """Withdraws specified amount if sufficient funds exist."""
        if amount > self.__account_balance:
            return False
        self.__account_balance -= amount
        return True

    def display_balance(self):
        """Displays current account balance."""
        print(f"Current Balance: ${self.__account_balance:.2f}")

import sys
from bank_account import BankAccount

def main():
    account = BankAccount(100)  # Example starting balance
    if len(sys.argv) < 2:
        print("Usage: python main.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    command, *params = sys.argv[1].split(':')
    amount = float(params[0]) if params else None

    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${amount}")
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${amount}")
        else:
            print("Insufficient funds.")
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()