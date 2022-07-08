import requests
#Importing required packages.

    url = 'https://pokeapi.co/api/v2/ability/'

    def search_pokeapi(search_term=''):

    #Cleaning the search term.
        search_term = str(search_term).strip().lower()

    #assigning value to header parameter to json file.
        header = {'Accept': 'application/json'}

    #Assigning parameter to search and response message.
        search_url = url + 'search'
        response_msg = requests.get(search_url, headers=header )

    #defining the response message in poke_api dictionary.
        if response_msg.status_code == requests.codes.ok:
    #returning to the response message.
            return response_msg.json()
        else:
            Print(f'status code: {response_msg.status_code}, Reason of Error occurrence: {response_msg.reason} ')
        pass
