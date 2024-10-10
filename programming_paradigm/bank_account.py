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