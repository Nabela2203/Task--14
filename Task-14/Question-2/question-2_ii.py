# Visit the URL https://www.openbrewerydb.org/ write a Python script which will do the following :- 
# 2. What is the count of breweries in each of the states mentioned above? 

import requests
def fetch_breweries(url, state):
    response = requests.get(url,params={'by_state': state})
    # print("Status_code:", response)
    json_data = response.json()
    return json_data

def count_brewery_by_states(url, states):
    

    for state in states:
        breweries_data = fetch_breweries(url, state)

        if breweries_data:
            count = len(breweries_data)
            print("count_breweries_in",state, ":",count)
                                
        else:
            print("Failed to fetch data.")

        print("\n")

url = "https://api.openbrewerydb.org/breweries"
states = ['Alaska', 'Maine', 'New York']
count_brewery_by_states(url, states)