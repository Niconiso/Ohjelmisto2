import requests


def vitsi():
    url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(url)
    vitsilataus = response.json()
    print(vitsilataus["value"])
vitsi()
