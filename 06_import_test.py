import csv


def capital_cities(lookup, dictionary):
    if lookup in dictionary:
        capital = dictionary.get(lookup)
    else:
        capital = None
    return capital

# Create a dictionary to hold the data
city_dictionary = {}

# set up dictionary of conversion factors for ingredients
# open file using appropriately named variable
countries = open('data.csv')


csv_countries = csv.reader(countries)
# Add the data from the list into the dictionary
# (first item in row is key, and next is definition)
for row in csv_countries:
    city_dictionary[row[0]] = row[1]

print(city_dictionary)

country_to_find = input("For which country do you want to find the capital: ")
capital_city = capital_cities(country_to_find, city_dictionary)
if capital_city is None:
    print(f"{country_to_find} is not listed")
else:
    print(f"The capital of {country_to_find} is {capital_city}")
