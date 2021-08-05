# Based on 03_Letter_Checker_re_v2.py
# This is the final version of component 03. Uses custom errors and has been
# changed from alpha_check to name_check as the conditions are not typical
# for strings.

import re


# Creating my own Errors that apply to my functions conditions
class Error(Exception):
    """Bass Class for other exceptions"""
    pass


# Is a custom Error to be raised when conditions are not met in try except
class NamingError(Error):
    """Raised when there is more than one sequential space or a string with
    less than 3 characters"""
    pass


def name_check(request):
    valid_char = "[A-Za-z ]"
    while True:  # Loop does not end
        try:
            name = str(input(request))
            for letter in name:
                if not re.match(valid_char, letter):
                    print("(no {}'s allowed)".format(letter))
                    raise NamingError
                elif len(name) < 3 or "  " in name:
                    raise NamingError
            # If conditions are met, name will be returned
            return name
        except NamingError:
            print("Please enter a name that contains at least 3 letters and "
                  "only 1 space between names: ")


# user name is received using name_check to validate the string
user_name = name_check("Enter your full name: ")
print(user_name)
