# first import json
import json

# Open the json file
with open('exchange_rates.json') as jsonfile:
    exchange_rate = json.load(jsonfile) # assign the data from the json file to a variable

# Display all the data from file
print(exchange_rate)

# iterate through the data dictionary printing each country's exchange rate
for country, rate in exchange_rate['rates'].items():
    print(f'The exchange rate for {country} is {rate}')
