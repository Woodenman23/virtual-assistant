import requests
import yaml
from pathlib import Path

ASSITANT_PATH = Path(__file__).parent

def get_city_json(city: str, temp_scale: str = "metric"):
    city_data = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={city}&units={temp_scale}&APPID={api_key()}"
    )
    return city_data.json()

def api_key():
    with open(Path.home() / ".api_keys.yaml", "r") as file:
        return yaml.safe_load(file)["open_weather"]
