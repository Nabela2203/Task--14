# Visit the URL https://www.openbrewerydb.org/ write a Python script which will do the following :- 
# 3.) Count the number of types of breweries present in individual cities of the state mentioned above 

import requests
def fetch_breweries(url, state):
    response = requests.get(url,params={'by_state': state})
    # print("Status_code:", response)
    json_data = response.json()
    return json_data

def brewery_by_type(url, state):
    breweries_data = fetch_breweries(url, state)

    if breweries_data:
        cities_data = {}
        
        for brewery in breweries_data:
            brewery_city = brewery.get('city', 'N/A')
            brewery_type = brewery.get('brewery_type', 'N/A')

            if brewery_city not in cities_data:
                cities_data[brewery_city] = set()

            cities_data[brewery_city].add(brewery_type)

        for brewery_city, brewery_types in cities_data.items():
            print("City: ",brewery_city)
            print("Number of Brewery Types: ",len(brewery_types))
            print("Brewery Types:",', '.join(brewery_types))
            print("\n")               
                            
    else:
        print("Failed to fetch data.")  

url = "https://api.openbrewerydb.org/breweries"
state = ['Alaska', 'Maine', 'New York']
brewery_by_type(url, state)