import requests
#Importing required packages.

    url = 'https://pokeapi.co/api/v2/ability/

    def search_pokeapi(search_term='', page_number=1, page_ability=2):

            """
    This fetches the information regarding the pokemon that contains a specified search term.

    :param search_term: search term to use (empty string = all pokemon)
    :param page_number: The number of page which result need to fetch.
    :param page_ability: Numbers of results per page.
    :returns: Dictionary of pokeapi is successful either none.
    """

    #Cleaning the search term.
        search_term = str(search_term).strip().lower()

    print(f'Searching for pokemon that contains {search_term}...',end='')


    #Assigning parameter to search and response message.
        search_url = url + 'search'
        response_msg = requests.get(search_url)

    #defining the response message in poke_api dictionary.
        if response_msg.status_code == requests.codes.ok:
    #returning to the response message.
            print('success')
            return response_msg.json()
        else:
            print('Error')
            Print(f'status code: {response_msg.status_code}, Reason of Error occurrence: {response_msg.reason} ')


            #Creating pokeapi dictionary.
            pokeapi_dictionary = search_pokeapi('pikachu')
            return None
