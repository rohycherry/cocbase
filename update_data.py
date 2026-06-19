import json
import requests

URL = "https://raw.githubusercontent.com/openfootball/worldcup.json/master/2026/worldcup.json"

response = requests.get(URL)
response.raise_for_status()

source = response.json()

print(type(source))
print(source)
