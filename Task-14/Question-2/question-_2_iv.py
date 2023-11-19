# Visit the URL https://www.openbrewerydb.org/ write a Python script which will do the following :- 
# 4.) Count and list how many breweries have websites in the states of Alaska, Maine and New Yorkimport requests

def fetch_breweries(url, state):
    response = requests.get(url,params={'by_state': state})
    # print("Status_code:", response)
    json_data = response.json()
    return json_data

def brewery_by_website(url, states):
    for state in states:
        breweries_data = fetch_breweries(url, state)

        if breweries_data:
            breweries_with_websites = [brewery for brewery in breweries_data if 'website_url' in brewery]
            print("Number of breweries with websites in" ,state,":", len(breweries_with_websites))
            print("Breweries with websites in", state)
            
            for brewery in breweries_with_websites: 
                brewery_name = brewery.get('name')
                brewery_website = brewery.get('website_url', 'N/A')             
                print(" - ",brewery_name,":",brewery_website)
            print("\n")               
                                
        else:
            print("Failed to fetch data.")  

url = "https://api.openbrewerydb.org/breweries"
states = ['Alaska', 'Maine', 'New York']
brewery_by_website(url, states)