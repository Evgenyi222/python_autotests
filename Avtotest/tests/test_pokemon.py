import requests
import pytest

URL='https://api.pokemonbattle.ru/v2/'
HEADER={'Content-Type':'application/json','trainer_token':'f4d14fed5d564f9ac7f96f93e3ebfaca'}
TRAINER_ID='12563'

def test_status_code():
    response=requests.get(url=f'{URL}trainers', headers=HEADER)
    assert response.status_code==200
    
def test_trainers():
    response_trainers=requests.get(url=f'{URL}trainers', headers=HEADER,trainer_id=TRAINER_ID)
    assert response.trainers.json()['data'][0]['trainer_id']=='12563'