# first import json
import json

# Open the json file
with open('exchange_rates.json') as jsonfile:
    exchange_rate = json.load(jsonfile)

print(exchange_rate)

for country, rate in exchange_rate['rates'].items():
    print(f'The exchange rate for {country} is {rate}')
