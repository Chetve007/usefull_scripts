import requests

city = "Москва"
url = f"https://wttr.in/{city}?format=4"
print(requests.get(url).text)
