from sys import argv
from lab04_Code import search_pokeapi
from pastbin_api import post_new_paste


def main()

    #Get the Pokémon name from command line parameters
    pokemon_name = str(pokemon_name).strip().lower()

    #Fetch Pokémon information from the PokéAPI
    pokeapi_dictionary = search_pokeapi(pokemon_name)

    #If Pokémon information is fetched successfully
    if pokeapi_dictionary:

    #Determine the title of the new PasteBin paste
    paste_title = get_paste_title(pokemon_name)

    #Determine the body text of the new PasteBin paste
    paste_body = get_paste_body(pokeapi_dictionary)

    #Create the new PasteBin paste
   paste_url = (paste_title, paste_body, '1M')

    #Print the URL of the new PasteBin paste
    print(paste_url)


def get_paste_body(pokeapi_dictionary):
    ability_list = [p['pokemon']for p in pokeapi_dictionary['results']]
    pokeapi_dic = '-->\n'.join(ability_list)
    get_paste_body = '->\n'.join(pokeapi_dic)
    paste_body = '-->\n'.join(ability_list)
    return paste_body

def get_paste_title(pokemon_name):
    return f'Ability of the {pokemon_name.capitalization()}s'


main()