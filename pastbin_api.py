
def post_new_paste(title, body_text, expirations='N', listed=True)
    """
    posts a new paste to PasteBin

    :param title: Paste to PasteBin
    :param body_text: Paste body text
    :param expiration: Expiration date
    :param listed: defines that past is public or  unlisted
    :returns: URL of new paste, whether successful or not.

    """

    print('posting a new paste to paste bin',end='')


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