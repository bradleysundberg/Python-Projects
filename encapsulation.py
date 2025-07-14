# Define a class that uses encapsulation
class BankAccount:
    def __init__(self, owner, initial_balance):
        self._owner = owner                 # Protected attribute: can be accessed by subclasses
        self.__balance = initial_balance    # Private attribute: name mangled, not accessible directly outside

    # Public method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__balance}")
        else:
            print("Deposit amount must be positive.")

    # Public method to withdraw money
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ${amount}. Remaining balance: ${self.__balance}")
        else:
            print("Insufficient funds or invalid amount.")

    # Protected method to display account info (could be used by subclasses)
    def _display_info(self):
        print(f"Account owner: {self._owner}")
        print(f"Balance: ${self.__balance}")

    # Public method to show balance using private attribute
    def show_balance(self):
        print(f"Current balance: ${self.__balance}")


# Create an object of BankAccount
account = BankAccount("Alice", 1000)

# Use public methods to interact with private and protected members
account.deposit(250)          # Uses public method to modify private balance
account.withdraw(100)         # Uses public method to access private balance
account.show_balance()        # Accesses private balance

# Accessing protected method
account._display_info()

# Accessing protected attribute
print(f"Accessing protected attribute _owner: {account._owner}")

# Accessing private attribute
print(f"Accessing private attribute __balance via name mangling: {account._BankAccount__balance}")
