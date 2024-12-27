import requests

URL='https://api.pokemonbattle.ru/v2/'
HEADER={'Content-Type':'application/json','trainer_token':'f4d14fed5d564f9ac7f96f93e3ebfaca'}
JSON={
    "name": "generate",
    "photo_id": 67
}




response=requests.post(url=f'{URL}pokemons', headers=HEADER, json=JSON)
print(response.text)

POKEMON_ID=response.json()['id']
JSON_poceball={
    "pokemon_id": POKEMON_ID
}


response_poceball=requests.post(url=f'{URL}trainers/add_pokeball', headers=HEADER, json=JSON_poceball)
print(response_poceball.text)

JSON_UPGRADE={
    "pokemon_id": POKEMON_ID,
    "name": "win",
    "photo_id": 2
}


response_upgrade=requests.put(url=f'{URL}pokemons', headers=HEADER, json=JSON_UPGRADE)
print(response_upgrade.text)