import requests
import yaml

def get_city_json(city: str):
    city_data = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&APPID={api_key()}"
    )
    return city_data.json()

def api_key():
    with open("assistant/data/api_keys.yaml", "r") as file:
        return yaml.safe_load(file)["open_weather"]
