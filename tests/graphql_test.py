import requests


def test_launches_by_id(url):
    data = {'query': '{ country (code: "UA") {name native capital emoji currency languages {code  name}}}'}
    response = requests.post('https://countries.trevorblades.com/', json=data)
    assert response.status_code == 200
    print(response.text)
