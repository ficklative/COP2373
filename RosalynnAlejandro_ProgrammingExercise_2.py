# user input email
# scan the email for keywords and phrases used in spam
# for every word or phrase found, add a point to the spam_score
# display the spam score
# display the likelihood it's spam
# display the words or phrases found in the email


def main():
    # Variable
    message = 0
    matched_phrases = []
    spam_score = 0

    while True:
        # Ask the user to input their message
        print("This program will scan your email messages for spam")
        message = input("Please enter an email message: ").lower()

        # Calculate the spam_score
        spam_score, matched_phrases = scan(message, spam_score, matched_phrases)

        # Display the spam_score
        print("--------------------------")
        print("The spam score is:", spam_score)

        # Display the likelihood that it is spam.
        if spam_score > 2:
            print("Your message is likely spam.")
        else:
            print("Your message is likely not spam.")

        # Display the matched phrases.
        if matched_phrases:
            print("--------------------------")
            print("Spam phrases found in your email message:")
            for phrase in matched_phrases:
                print(f"> {phrase}")

        # Ask if the user wants to scan another email
        while True:
            run_again = input("Would you like to scan another email? (y/n): ").lower()
            if run_again == "y":
                break
            elif run_again == "n":
                print("Thank you for using this program. Goodbye.")
                return
            else:
                print("Please enter y or n.")

def scan(message, spam_score, matched_phrases):
    # List of common words and phrases used in spam email
    phrases = ["make money fast", "guaranteed success",
               "in as little as", "best deal", "click below",
               "great news", "risk-free", "limited time deal",
               "act now", "deal", "pre-approved", "offer",
               "cash bonus", "click here", "get it now",
               "double your money", "lowest price", "best bargain",
               "action required", "click to win", "hot deal",
               "instant winnings", "jackpot", "exclusive",
               "only now", "special promotion", "amazing deal",
               "no obligation", "prize", "ending soon"
               ]

    # Calculate the emails spam_score
    for phrase in phrases:
        if phrase in message:
            spam_score += 1
            matched_phrases.append(phrase)
    return spam_score, matched_phrases

if __name__ == "__main__":
    main()