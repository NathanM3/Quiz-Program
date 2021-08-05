# Test version of alpha_check using .isalpha() to check for valid strings
def alpha_check(request):
    while True:  # Loop does not end
        try:
            string = str(input(request))
            if string.isalpha():
                print(string)  # for testing
            else:
                raise TypeError
        except TypeError:
            print("Please enter letters only")
            continue
        except EOFError:
            print("Please enter something: ")
            continue


alpha_check("Enter your name: ")
