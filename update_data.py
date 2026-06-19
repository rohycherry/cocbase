import json
import requests

URL = "https://raw.githubusercontent.com/openfootball/worldcup.json/master/2026/worldcup.json"

response = requests.get(URL)
response.raise_for_status()

source = response.json()

matches = []

for m in source["matches"]:

    stage = m.get("group", m.get("round", "World Cup"))

    matches.append({
        "stage": stage,
        "home": m["team1"],
        "away": m["team2"],
        "date": m["date"]
    })

with open("matches.json", "w", encoding="utf-8") as f:
    json.dump({"matches": matches}, f, indent=2, ensure_ascii=False)

print("matches.json updated successfully")
