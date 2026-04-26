# Como conectar um API usando python

import requests

url_base = 'https://pokeapi.co/api/v2/'

def pega_pokemon_info(nome):
    url = f'{url_base}/pokemon/{nome}'
    resposta = requests.get(url)

    if resposta.status_code == 200:
        return resposta.json()
        
    else:
        print(f'Falha ao receber data {resposta.status_code}')

nome_pokemon = 'charmander'
pokemon_info = pega_pokemon_info(nome_pokemon)

if pokemon_info:
    print(f'{pokemon_info["name"]}')