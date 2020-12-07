import pytest
import requests


@pytest.mark.parametrize("flight_number", [60, 65, 70])
def test_launches_by_id(url, flight_number):
    response = requests.get(url + f'launches/{flight_number}')
    assert response.json()['flight_number'] == flight_number
    assert response.status_code == 200


def test_all_launches(url):
    response = requests.get(url + 'launches')
    assert response.status_code == 200


def test_all_launches_error(url):
    response = requests.get(url + 'launches?flight_number=0')
    assert response.status_code == 200
    assert response.json() == []


def test_all_ships(url):
    response = requests.get(url + 'ships')
    assert response.status_code == 200
    assert response.json()[0]['ship_id'] == 'AMERICANCHAMPION'


def test_all_ships_roles(url):
    response = requests.get(url + 'ships')
    assert response.status_code == 200
    assert response.json()[0]['roles'][0] == 'Support Ship'


def test_get_ship_by_id(url):
    ship_id = requests.get(url + 'ships').json()[0]['ship_id']
    response = requests.get(url + f'ships/{ship_id}')
    assert response.status_code == 200
    assert response.json()['ship_id'] == ship_id


def get_ships_id():
    ships = requests.get('https://api.spacexdata.com/v3/ships').json()
    ships_id = []
    for i in ships:
        ships_id.append(i['ship_id'])
    return ships_id


@pytest.mark.parametrize("ship_id", get_ships_id())
def test_get_all_ship_by_id(url, ship_id):
    response = requests.get(url + f'ships/{ship_id}')
    assert response.status_code == 200
    assert response.json()['ship_id'] == ship_id
