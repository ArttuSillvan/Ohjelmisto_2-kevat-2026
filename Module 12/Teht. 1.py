import json
import requests

def joke():
    sivusto = "https://api.chucknorris.io/jokes/random"

    try:
        vastaus = requests.get(sivusto)
        if vastaus.status_code == 200:
            json_vastaus = vastaus.json()
            print(json_vastaus["value"])
        else:
            print("Error")

    except requests.exceptions.RequestException as e:
        print("Hakua ei voitu suorittaa.")

joke()