# This program will sell a total of 20 cinema tickets
# at 4 tickets per customer, and will display the total
# number of buyers after all tickets have been sold

# main() function will print the results
def main():
    # Initialize accumulator variables
    tickets = 20
    buyers = 0

    # Call a tally() function to calculate tickets and buyers
    tickets, buyers = tally(tickets, buyers)

    # Display the total number of buyers when all
    # tickets have been sold.
    print("\nAll tickets have been sold.")
    print(f"Total number of buyers: {buyers}")

# Calculate the tickets and buyers
def tally(tickets, buyers):
    # Use a while loop to sell the total of tickets.
    while tickets > 0:
        # Ask if the user would like to buy a ticket.
        buy = input("Would you like to buy tickets? (y/n): ").strip().lower()

        # If user says no, say goodbye. If they say the wrong letter,
        # then prompt the user again
        if buy == "n":
            print("Goodbye!\n")
            continue
        elif buy != "y":
            print("Please enter 'y' or 'n'.\n")
            continue

        # Ask user how many tickets.
        valid_purchase = False # ensure a sale can be made
        while not valid_purchase:
            try:
                # This prompt will loop to ask each user.
                print("---------------------------------------")
                tickets_purchased = int(input("How many tickets would you like to buy? (Max 4): "))
                print("---------------------------------------")

                # Ensure user cannot buy more than 4 tickets
                if 1 <= tickets_purchased <= 4:
                    # Ensure no more than 20 tickets sold in total
                    if tickets_purchased > tickets:
                        print(f"Sorry, only {tickets} ticket(s) left. Try a smaller number.\n")

                    # tally the accumulator variables and display information.
                    else:
                        tickets -= tickets_purchased
                        buyers += 1

                        # display number of tickets purchased,
                        # and display how many left
                        print(f"You purchased {tickets_purchased} ticket(s).")
                        print(f"{tickets} ticket(s) remaining.\n")
                        print("--------------------------------------")
                        valid_purchase = True  # Ends this inner loop

                # Make sure users cannot buy more than 4 tickets
                else:
                    print("You can only buy between 1 and 4 tickets.\n")
            except ValueError:
                print("Please enter a valid number.\n")

    return tickets, buyers

# Call the main function
if __name__ == '__main__':
    main()