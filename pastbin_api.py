import requests
 
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

    p = {
        'api_dev_key': lBf-u7pU3ls6dYLR4eD3EURjDVhhEn3K,
        'api_option': paste,
        'api_paste_code': body_text,
        'api_paste_name':title,
        'api_paste_private': 0 if listed else 1,
        'api_paste_expire_date': expiration
    }


    #Assigning parameter to search and response message
        paste_url = 'https://pastebin.com/api/api_post.php',
        response_msg = requests.post(paste_url, data=p)

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