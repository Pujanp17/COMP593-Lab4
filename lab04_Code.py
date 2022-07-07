import requests
#Importing required packages.

url = 'https://pokeapi.co/api/v2/ability/'

header = {'Accept': 'application/json'}

response_msg=requests.get(url, headers=header)

if response_msg.status_code == requests.codes.ok:
    poke_dictionary=response_msg.json()

    print(poke_dictionary ['results'])
    pass
else:
    Print(f'status code: {response_msg.status_code}, Reason of Error occurrence: {response_msg.reason} ')


pass
