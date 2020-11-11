# Task

### Use a Json file to show exchange rates by country
1. Copy the data from the json file on github to your new project
2. Display all the data from the json file
3. Iterate through the data and display exchange rate by country

**Acceptance Criteria**

- Create a New Repo for this task
- .gitignore and README in a new pycharm project/folder
- have the exchange_rates.json file available in your pycharm project/folder
- Display all the data from .json file
- iterate through the data display exchange rate by country

## Guide

### Preparation
1. Create a new project with PyCharm and a new repository on GitHub
2. Create a .gitignore file within the new project to ignore all irrelevant files.
```
venv/
/.idea/
```
3. Create a README file for documentation
4. Create a new .json file using the correct naming convetions
5. Create a new .py file also using the correct naming conventions
6. Initialise the empty repo by following the commands on GitHub

### Coding
**After completing the preparation,you can start coding**
1. Copy the  exchange rate data from github to new json file
2. On your .py file import json with `import json`
3. Access the json file containing the data using `as` to create an alias called 'jsonfile'
```
with open('exchange_rates.json') as jsonfile:
```
4. Use the load method to store the data in a variable
```
 exchange_rate = json.load(jsonfile)
```
5. Print the newly created variable to see the data from jsonfile
```
print(exchange_rate)
```
6. Create a for loop to iterate through the nested dictionary, 'rates' (a dictionary within a dictionary) and print the exchange rates per country
```
for country, rate in exchange_rate['rates'].items():
    print(f'The exchange rate for {country} is {rate}')
```
7. Run the page

