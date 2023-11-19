# Using the URL https://restcountries.com/v3.1/all write a Python program which will do the fallowing 
# 1.) Using the OOPS concept for the following task. 
# 2) Use the Class Constructor for taking input the above mentioned URL for the task. 
# 3.) Create a Method that will Fetch all the JSON data from the URL mentioned above 
# 4.) Create a Method that will display the name of countries, currencies & currency symbols. 
# 5.) Create a Method that will display all those countries which have DOLLAR as its currency. 
# 6.) Create a Method that will display all those countries which have EURO as its currency.

import requests

def fetch_json_data(url):
    response = requests.get(url)
    print("Status_code:", response)
    json_data = response.json()
    return json_data

def country_info(country_data):
    count = []
    for country in country_data:
        name = country.get('name').get('common')
        currencies = country.get('currencies')
        
        if currencies: 
                    
            for currency_code, currency_info in currencies.items():
                    currency_name = currency_info.get('name')
                    currency_symbol = currency_info.get('symbol')
                    if (currency_code.lower() == 'usd'):
                        count.append(currency_code)                       
                        print("Country:",name)
                        print("Currencies:")
                        print("    Currency Code:",currency_code)
                        print("    Currency Name:",currency_name)
                        print("    Currency Symbol:",currency_symbol)
                    
            print("\n")
                  
    length = len(count)
    print("Country_with_dollar:",length)

url = "https://restcountries.com/v3.1/all"
countries_data = fetch_json_data(url)

if countries_data:
    country_info(countries_data)
   
else:
    print("Failed to fetch data.")


    
