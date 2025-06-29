# This program will validate a users phone number, social security
# number, and zip code.
# The program will create a dictionary for user_info, then check if
# user_info is in the correct pattern using regular expressions.

# Import regular expressions
import re

# This function will validate the user_info
def validate_info(user_info):
    # Create patters for phone, social security number, and zip code
    phone_pattern = r'\d\d\d[ -]\d\d\d[ -]\d\d\d\d'
    ssn_pattern = r'\d\d\d[ -]\d\d[ -]\d\d\d\d'
    zip_pattern = r'\d\d\d\d\d'

    # Validate if user_info is in the right pattern using re.fullmatch
    if re.fullmatch(phone_pattern, user_info["phone number"]):
        phone_valid = True
    else:
        phone_valid = False

    if re.fullmatch(ssn_pattern, user_info["ssn number"]):
        ssn_valid = True
    else:
        ssn_valid = False

    if re.fullmatch(zip_pattern, user_info["zip number"]):
        zip_valid = True
    else:
        zip_valid = False

    # Return validation result
    return phone_valid, ssn_valid, zip_valid

def main():

    # Create a dictionary to get user input for phone, ssn, and zip
    user_info = {"phone number": input("Enter your phone number (e.g. 123-456-7890): "),
                 "ssn number": input("Enter your Social Security Number (e.g. 123-45-6789): "),
                 "zip number": input("Enter your zip code (e.g. 12345): ")}

    # Create a function to validate user_info dictionary
    phone_valid, ssn_valid, zip_valid = validate_info(user_info)

    # Display if the users phone, ssn, and zip are valid or invalid
    print(f"The phone number you entered is: {'Valid' if phone_valid else 'Invalid'}\n"
          f"The Social Security Number you entered is: {'Valid' if ssn_valid else 'Invalid'}\n"
          f"The zip code you entered is: {'Valid' if zip_valid else 'Invalid'}")

# Call the main function
if __name__ == "__main__":
    main()