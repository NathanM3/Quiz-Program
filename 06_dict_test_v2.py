# Based on 06_dict_test_v1.py
# This version reworks the function to work for both modes
# re writing main routine code to suit both modes as well.
import csv


def location_search(lookup, location_dict):
    # Checks if the given name is inside the given dictionary
    if lookup in location_dict:
        # outputs the paired location name
        location_name = location_dict.get(lookup)
        # outputs that there is no location
    else:
        location_name = None
    return location_name


# Create a dictionary to hold the data
country_dictionary = {}
# set up dictionary of conversion factors for ingredients
# open file using appropriately named variable
countries = open('data.csv')

csv_countries = csv.reader(countries)
# Add the data from the list into the dictionary
# (first item in row is key, and next is definition)
for row in csv_countries:
    country_dictionary[row[0]] = row[1]

# this line of code rearranges the value and key to create a inverted dict.
city_dictionary = {value: key for (key, value) in country_dictionary.items()}

# Printing both of the dictionaries to help with testing.
print(city_dictionary)
print(country_dictionary)

# asking for a mode replicates the mode given in the actual GUI
mode = input("Do you want to guess 'country' or 'capital'?: ")

if mode == "capital":
    location_find = input("Enter a capital: ")
    dictionary = city_dictionary
# If mode is countries the settings have to change from default
else:
    location_find = input("Enter a country: ")
    dictionary = country_dictionary

# universal variables for both modes
location = location_search(location_find, dictionary)
# if location is not found inside the dictionary.
if location is None:
    print(f"{location_find} is not listed")
    # '' is the capital of '' or '' is the country of ''
else:
    print(f"{location_find} is the {mode} of {location}")
