import requests

API_key = "58e5f5b44d9a57c1b070340be22c0253"

municipality = input("Enter municipality name: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={municipality}&appid={API_key}&units=metric"

try:
    vastaus = requests.get(url)
    if vastaus.status_code == 200:
        data = vastaus.json()

        description = data["weather"][0]["description"]
        temperature = data["main"]["temp"]

        print("Weather:", description)
        print("Temperature:", temperature, "Celsius")
    else:
        print("Error")

except requests.exceptions.RequestException:
    print("Hakua ei voitu suorittaa.")