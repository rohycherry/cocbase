import json
import requests

URL = "https://raw.githubusercontent.com/openfootball/worldcup.json/master/2026/worldcup.json"

response = requests.get(URL)
response.raise_for_status()

source = response.json()

print("TYPE:", type(source))

# পুরো data print করবে
print(source)

# আপাতত খালি matches.json তৈরি করবে
with open("matches.json", "w", encoding="utf-8") as f:
    json.dump({"matches": []}, f, indent=2)

print("Done")
