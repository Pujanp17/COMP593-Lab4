import requests
#Importing required packages.

url = 'https://pokeapi.co/api/v2/ability/'

header = {'Accept': 'application/json'}

response_msg=requests.get(url, headers=header)

if response_msg.status_code == requests.codes.ok:
    response_msg.json()
    

pass
