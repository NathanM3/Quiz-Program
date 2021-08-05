# Second test 03 component. This one uses regular expression library to filter
# out characters that I do not want in a user's name.
# This initial version is only for testing how re filters data.
# Next version will use try/except
# Importing regular expression library re
import re

# Data to be tested
data = ["Nathan", "1", "Nathan Morrison", "Nathan1", "hi", "Nathan_Morrison"]

# the text must only have alphabet characters and spaces
# Using regular expression to define what types of characters are allowed
valid_char = "[A-Za-z ]"
for item in data:
    for char in item:
        # Checks every character in the string to see if it meets conditions
        if not re.match(valid_char, char):
            print("{} is not valid".format(item))
            data.remove(item)
# List only contains valid strings after the for loop has been used.
print(data)
