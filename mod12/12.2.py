import requests
def hae_saa(kaupunki, API):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={kaupunki}&lang=fi&units=metric&appid={API}"
    response = requests.get(url)
    data = response.json()
    lämpötila = data["main"]["temp"]
    lämpötila = lämpötila
    sää = data["weather"][0]["description"]
    print(f"{sää}, {lämpötila:.1f}C")

kaupunki = input("Kaupunki: ")
API = input("Anna OpenWeather API-avain: ")

hae_saa(kaupunki, API)