from pathlib import Path
import requests
import yaml

def get_city_json(city: str, temp_scale: str = "metric") -> str:
    city_data = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={city}&units={temp_scale}&APPID={api_key()}"
    )
    return city_data.json()

def api_key() -> None:
    with open(f"{Path.home()}/.api_keys.yaml", "r") as file:
        return yaml.safe_load(file)["open_weather"]
