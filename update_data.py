import json
import requests

# OpenFootball source (change if needed)
URL = "https://raw.githubusercontent.com/openfootball/worldcup.json/master/2026/worldcup.json"

try:
    response = requests.get(URL)
    response.raise_for_status()

    source = response.json()

    matches = []

    for m in source.get("matches", []):

        home = m["team1"]["name"]
        away = m["team2"]["name"]

        stage = m.get("group", "")
        if not stage:
            stage = m.get("round", "World Cup")

        date = m.get("date")

        matches.append({
            "stage": stage,
            "home": home,
            "away": away,
            "date": date
        })

    output = {
        "matches": matches
    }

    with open("matches.json", "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print("matches.json updated successfully")

except Exception as e:
    print("Error:", e)
