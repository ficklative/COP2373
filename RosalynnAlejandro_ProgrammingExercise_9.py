# This program will allow a user to enter a bank account
# details, such as name, account number, amount, and interest rate.
# The program will help the user with deposits and withdraws,
# and also with calculating interests rates in a given number of days.
# This program will display
    # Account Holder
    # Account Number
    # Current Balance
    # Interest Rate

class BankAcct:
    '''This class will take name, account_number, amount, and
    interest_rate to adjust accordingly per user input from the
    test_bank_account function'''

    # Initialize name, account_number, amount, and interest_rate
    def __init__(self, name, account_number, amount, interest_rate):
        self.name = name
        self.account_number = account_number
        self.amount = amount
        self.interest_rate = interest_rate

    # Set mutator for amount to calculate total after a deposit
    def deposit(self, amount):
        if amount > 0:
            self.amount += amount
            print(f"Deposited ${amount:.2f}")
        else:
            print("Deposit amount must be positive.")

    # Set mutator for amount to calculate total after a withdraw
    def withdraw(self, amount):
        if amount > 0 and amount <= self.amount:
            self.amount -= amount
            print(f"Withdrew ${amount:.2f}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    # Set mutator to adjust the interest rate
    def adjust_interest_rate(self, new_rate):
        if new_rate >= 0:
            self.interest_rate = new_rate
            print(f"Interest rate adjusted to {new_rate}%")
        else:
            print("Interest rate cannot be negative.")

    # Accessor for amount
    def get_balance(self):
        return self.amount

    # Accessor for rate calculator
    def calculate_interest(self, days):
        daily_rate = self.interest_rate / 100 / 365
        return self.amount * daily_rate * days

    # Use the __str__ method to calculate deposit, withdraw,
    # adjust and calculate interest rate
    def __str__(self):
        return (f"\nAccount Holder: {self.name}\n"
                f"Account Number: {self.account_number}\n"
                f"Current Balance: ${self.amount:.2f}\n"
                f"Interest Rate: {self.interest_rate}%\n")


def test_bank_acct():
    print("Welcome to the Bank Account Setup")
    name = input("Enter account holder's name: ")
    account_number = input("Enter account number: ")
    amount = float(input("Enter starting balance: "))
    interest_rate = float(input("Enter annual interest rate (e.g, 3 for 3%): "))

    acct = BankAcct(name, account_number, amount, interest_rate)
    print(acct)

    while True:
        print("\nChoose an option:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Adjust Interest Rate")
        print("4. Calculate Interest")
        print("5. Show Account Info")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            deposit_amount = float(input("Enter amount to deposit: "))
            acct.deposit(deposit_amount)

        elif choice == "2":
            withdraw_amount = float(input("Enter amount to withdraw: "))
            acct.withdraw(withdraw_amount)

        elif choice == "3":
            new_rate = float(input("Enter new interest rate: "))
            acct.adjust_interest_rate(new_rate)

        elif choice == "4":
            days = int(input("Enter number of days to calculate interest for: "))
            interest = acct.calculate_interest(days)
            print(f"Interest earned in {days} days: ${interest:.2f}")

        elif choice == "5":
            print(acct)

        elif choice == "6":
            print("Exiting program. Final Account Summary:")
            print(acct)
            break

        else:
            print("Invalid choice. Please select a valid option (1-6).")

# Start the interactive test
test_bank_acct()
