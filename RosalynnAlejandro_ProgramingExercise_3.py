# This program will help a user with their monthly expenses,
# such as housing, travel, personal, food, medical, and bills.
# This program will display the highest and lowest expense, and the total.

from functools import reduce

# main function
def main():
    # Variables
    choice = 0
    amount = 0

    # Create a list for the users input (expense type, amount)
    expenses = []

    divider = "-"
    print("This program will calculate your monthly expenses.")
    print(divider * 45)

    # Create a numbered list
    menu_expenses = ["Housing", "Transportation", "Personal", "Food", "Medical", "Bills", "Exit"]
    print("Types of Expenses:")
    for expense in list(enumerate(menu_expenses, start=1)):
        print(f"{expense[0]}. {expense[1]}")
    print(divider * 45)

    while True:
        # Get the type of expense
        try:
            choice = int(input("Enter your choice: "))
            if choice < 1 or choice > 7:
                print("Invalid choice, please try again")
                continue
        except ValueError:
            print("Invalid choice, please try again.")
            continue

        if choice == 7:
            break  # Exits the program

        # Get the expense amount
        try:
            amount = float(input(f"Enter total monthly {menu_expenses[choice - 1].lower()} expenses: "))
            # Store expense in the expenses list as a tuple (expense type, amount)
            expenses.append((menu_expenses[choice - 1], amount))
        except ValueError:
            print("Please choose an expense from the menu.")

    # Calculate the max, min, and total
    if expenses:

        # Find max using reduce/lambda
        max_expense = reduce(lambda x, y: x if x[1] > y[1] else y, expenses)
        # Find min using reduce/lambda
        min_expense = reduce(lambda x, y: x if x[1] < y[1] else y, expenses)
        # Calculate total using reduce/lambda
        total_expenses = reduce(lambda x, y: x + y[1], expenses, 0)

        # Display the entered (expenses, amount)
        print(divider * 45)
        print("Your monthly expenses:")
        for e in list(enumerate(expenses, start=1)):
            print(f"{e[0]}. {e[1]}")

        # Display the type and max, min, and total
        print(divider * 45)
        print(f"Your highest expense: {max_expense[0]} - ${max_expense[1]:.2f}")
        print(f"Your lowest expense: {min_expense[0]} - ${min_expense[1]:.2f}")
        print(f"Your total expenses: ${total_expenses:.2f}")

        print("Thank you for using this program.\nHave a nice day!")
    else:
        print("Thank you for using this program.")

# Execute the main function
if __name__ == '__main__':
    main()