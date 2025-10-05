import requests
URL='https://api.pokemonbattle.ru/v2'
TOKEN = '3867b6550810443a45aced88cd9fe986'
HEADER={'Content-Type':'application/json', 'trainer_token': TOKEN}

body_creat_pokemon ={
    "name": "generate",
    "photo_id": "-1"
}

body_changeName_pokemon = {
    "pokemon_id": "403459",
    "name": "generate",
    "photo_id": 2
}

body_catch_pokemon = {
    "pokemon_id": "377894"
}


response_creat_pokemon=requests.post(url=f'{URL}/pokemons', headers=HEADER, json = body_creat_pokemon )
print(response_creat_pokemon.json())

response_changeName_pokemon = requests.put(url=f'{URL}/pokemons', headers= HEADER,json=body_changeName_pokemon)
print(response_changeName_pokemon.json())

response_catch_pokemon=requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER,json=body_catch_pokemon)
print(response_catch_pokemon.json())