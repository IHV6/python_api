import pytest
import requests


@pytest.mark.parametrize("flight_number", [60, 65, 70])
def test_launches_by_id(url, flight_number):
    response = requests.get(url + f'launches/{flight_number}')
    assert response.json()['flight_number'] == flight_number
    assert response.status_code == 200
    print(response.json()['mission_name'])


def test_all_launches(url):
    response = requests.get(url + 'launches')
    assert response.status_code == 200
    print(response.headers)


def test_all_launches_error(url):
    response = requests.get(url + 'launches?flight_number=0')
    assert response.status_code == 200
    assert response.json() == []
    print(response.json())
