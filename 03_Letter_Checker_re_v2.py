# Based on 03_Letter_Checker_Test_v2.py and 03_Letter_Checker_re_v1.py
# Has used re from the latter file and recycled the alpha_check function
# from the prior file.
import re


def alpha_check(request):
    valid_char = "[A-Za-z ]"
    while True:  # Loop does not end
        try:
            string = str(input(request))
            # Checks every character to see if the string is valid
            for letter in string:
                # Raises errors if conditions are not met
                if not re.match(valid_char, letter):
                    # It will print which character is invalid
                    print("(no {}'s allowed)".format(letter))
                    raise TypeError
                elif len(string) < 3 or "  " in string:
                    raise EOFError
            # String is returned if it is valid.
            return string
        # If errors are raised, program prints the messages below and
        # loops due to while loop
        except TypeError:
            print("Please enter letters only and spaces only")
        except EOFError:
            print("Please enter a name that contains at least 3 letters and "
                  "only 1 space between names: ")


# user name is received using alpha_check to validate the string
user_name = alpha_check("Enter your full name: ")
print(user_name)
