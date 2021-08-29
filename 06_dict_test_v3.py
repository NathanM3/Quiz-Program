# Based on 06_dict_test_v2.py
import csv
import random


def location_search(value, lookup, location_dict):
    # outputs the paired location name
    if location_dict.get(lookup) == value:
        location_name = value
    # Returns None for all other cases
    else:
        location_name = None
    return location_name


# Create a dictionary to hold the data
country_dictionary = {}
# set up dictionary of conversion factors for ingredients
# open file using appropriately named variable
countries = open('Capital_Country.csv')

csv_countries = csv.reader(countries)
# Add the data from the list into the dictionary
# (first item in row is key, and next is definition)
for row in csv_countries:
    country_dictionary[row[0]] = row[1]

# this line of code rearranges the value and key to create a inverted dict.
city_dictionary = {value: key for (key, value) in country_dictionary.items()}

# Printing both of the dictionaries to help with testing.
print(country_dictionary)
print(city_dictionary)

# asking for a mode replicates the mode given in the actual GUI
mode = input("Do you want to guess 'country' or 'capital'?: ")

if mode == "capital":
    dictionary = city_dictionary
# If mode is countries the settings have to change from default
else:
    dictionary = country_dictionary

# This gives a list of keys that can be shuffled and called to randomly
# select countries or capitals
keys_list = list(dictionary.keys())
random.shuffle(keys_list)
# A key can be selected randomly from dict_keys to quiz the user:
for key in keys_list:
    location_find = input(f"What is the {mode} of {dictionary.get(key)}: ")

    # universal variables for both modes
    answer = location_search(dictionary.get(key), location_find, dictionary)
    # if location is not found inside the dictionary.
    if answer is None:
        print(f"{location_find} is not the {mode} of {dictionary.get(key)}")
        # '' is the capital of '' or '' is the country of ''
    else:
        print(f"{location_find} is the {mode} of {dictionary.get(key)}")
