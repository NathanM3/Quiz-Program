# Based on 03_Letter_Checker_Test_v1.py
# This version is refined to use two alpha_check functions to create the
# user name (lines 21-22).
# The issue is that for my GUI, this may require changes/additional buttons.
# I would like to avoid this if possible.
def alpha_check(request):
    while True:  # Loop does not end
        try:
            string = str(input(request))
            if string.isalpha():
                return string
            else:
                raise TypeError
        except TypeError:
            print("Please enter letters only")
            continue
        except EOFError:
            print("Please enter something: ")
            continue


user_name = alpha_check("Enter your first name: ").title() + " " + \
            alpha_check("Enter your last name: ").title()
print(user_name)
