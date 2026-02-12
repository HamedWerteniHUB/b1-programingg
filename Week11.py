import requests
import json
import time
from datetime import datetime

# ----------------------------------------------
# EU CAPITALS (list)
# ----------------------------------------------
eu_capitals = [
    {"city": "Vienna", "country": "Austria", "lat": 48.2082, "lon": 16.3738},
    {"city": "Brussels", "country": "Belgium", "lat": 50.8503, "lon": 4.3517},
    {"city": "Sofia", "country": "Bulgaria", "lat": 42.6977, "lon": 23.3219},
    {"city": "Zagreb", "country": "Croatia", "lat": 45.8150, "lon": 15.9819},
    {"city": "Nicosia", "country": "Cyprus", "lat": 35.1856, "lon": 33.3823},
    {"city": "Prague", "country": "Czechia", "lat": 50.0755, "lon": 14.4378},
    {"city": "Copenhagen", "country": "Denmark", "lat": 55.6761, "lon": 12.5683},
    {"city": "Tallinn", "country": "Estonia", "lat": 59.4370, "lon": 24.7536},
    {"city": "Helsinki", "country": "Finland", "lat": 60.1695, "lon": 24.9354},
    {"city": "Paris", "country": "France", "lat": 48.8566, "lon": 2.3522},
    {"city": "Berlin", "country": "Germany", "lat": 52.5200, "lon": 13.4050},
    {"city": "Athens", "country": "Greece", "lat": 37.9838, "lon": 23.7275},
    {"city": "Budapest", "country": "Hungary", "lat": 47.4979, "lon": 19.0402},
    {"city": "Dublin", "country": "Ireland", "lat": 53.3498, "lon": -6.2603},
    {"city": "Rome", "country": "Italy", "lat": 41.9028, "lon": 12.4964},
    {"city": "Riga", "country": "Latvia", "lat": 56.9496, "lon": 24.1052},
    {"city": "Vilnius", "country": "Lithuania", "lat": 54.6872, "lon": 25.2797},
    {"city": "Luxembourg", "country": "Luxembourg", "lat": 49.6116, "lon": 6.1319},
    {"city": "Valletta", "country": "Malta", "lat": 35.8989, "lon": 14.5146},
    {"city": "Amsterdam", "country": "Netherlands", "lat": 52.3676, "lon": 4.9041},
    {"city": "Warsaw", "country": "Poland", "lat": 52.2297, "lon": 21.0122},
    {"city": "Lisbon", "country": "Portugal", "lat": 38.7223, "lon": -9.1393},
    {"city": "Bucharest", "country": "Romania", "lat": 44.4268, "lon": 26.1025},
    {"city": "Bratislava", "country": "Slovakia", "lat": 48.1486, "lon": 17.1077},
    {"city": "Ljubljana", "country": "Slovenia", "lat": 46.0569, "lon": 14.5058},
    {"city": "Madrid", "country": "Spain", "lat": 40.4168, "lon": -3.7038},
    {"city": "Stockholm", "country": "Sweden", "lat": 59.3293, "lon": 18.0686}
]

# ----------------------------------------------
# FUNCTION: get weather from API
# ----------------------------------------------
def get_weather(lat, lon):
    url = "https://api.open-meteo.com/v1/forecast"
    today = datetime.now().strftime("%Y-%m-%d")

    params = {
        "latitude": lat,
        "longitude": lon,
        "current_weather": True,
        "hourly": "temperature_2m,precipitation_probability,weathercode",
        "start_date": today,
        "end_date": today,
        "timezone": "auto"
    }

    try:
        response = requests.get(url, params=params)
        return response.json()
    except:
        print("Error getting data")
        return None


# ----------------------------------------------
# FUNCTION: collect all capitals weather
# ----------------------------------------------
def collect_weather():
    all_data = {}

    for cap in eu_capitals:
        city = cap["city"]
        country = cap["country"]

        print("Getting weather for", city)

        data = get_weather(cap["lat"], cap["lon"])

        if data is None:
            print("Failed for", city)
            continue

        current = data.get("current_weather", {})
        hourly = data.get("hourly", {})

        city_data = {
            "country": country,
            "coordinates": {
                "latitude": cap["lat"],
                "longitude": cap["lon"]
            },
            "current_weather": current,
            "hourly_forecast": []
        }

        if "time" in hourly:
            for i in range(len(hourly["time"])):
                hour_info = {
                    "time": hourly["time"][i],
                    "temperature": hourly["temperature_2m"][i],
                    "precipitation_probability": hourly["precipitation_probability"][i],
                    "weathercode": hourly["weathercode"][i]
                }
                city_data["hourly_forecast"].append(hour_info)

        all_data[city] = city_data

        time.sleep(1)  # delay to respect API

    return all_data


# ----------------------------------------------
# FUNCTION: save to JSON file
# ----------------------------------------------
def save_json(data):
    with open("eu_weather_data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


# ----------------------------------------------
# MAIN PROGRAM
# ----------------------------------------------
def main():
    print("Collecting EU weather data...")
    weather = collect_weather()
    save_json(weather)
    print("Finished! Data saved to eu_weather_data.json")


main()
