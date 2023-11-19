# Visit the URL https://www.openbrewerydb.org/ write a Python script which will do the following :- 
# 1.) List the names of all breweries present in the states of Alaska, Maine and New York 

import requests
def fetch_breweries(url, state):
    response = requests.get(url,params={'by_state': state})
    # print("Status_code:", response)
    json_data = response.json()
    return json_data

def brewery_by_states(url, states):

    for state in states:
        print("Breweries in ",state)
        breweries_data = fetch_breweries(url, state)

        if breweries_data:
            for brewery in breweries_data:
                brewery_name = brewery.get('name')
                print("  - ",brewery_name)   
                            
        else:
            print("Failed to fetch data.")

        print("\n")

url = "https://api.openbrewerydb.org/breweries"
states = ['Alaska', 'Maine', 'New York']
brewery_by_states(url, states)