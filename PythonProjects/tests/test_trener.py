import requests
import pytest

URL='https://api.pokemonbattle.ru/v2'
TOKEN = ''
HEADER={'Content-Type':'application/json', 'trainer_token': TOKEN}
TRAINER_ID = '41448'

def test_status_code():
    response = requests.get(url=f'{URL}/trainers')
    assert response.status_code == 200


def test_my_trainer():
    response_my_trainer = requests.get(url=f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID} )

    assert response_my_trainer.json()["data"][0]["id"] == TRAINER_ID
