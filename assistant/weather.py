import requests
import yaml


def get_weather(city: str):
    city = "cheltenham"
    weather_data = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&APPID={api_key()}"
    )

    weather_json = weather_data.json()
    weather = weather_json["weather"][0]["main"]
    temperature = weather_json["main"]["temp"]
    temp_low = weather_json["main"]["temp_min"]
    temp_high = weather_json["main"]["temp_max"]
    city_name = weather_json["name"]

    print(
        f"\nThe weather in {city_name} is {weather.lower()}. \n\nThe temperature is {temperature}°C with" 
        f" a high of {temp_high}°C and a low of {temp_low}°C.\n"
    )

def api_key():
    with open("assistant/data/api_keys.yaml", "r") as file:
        return yaml.safe_load(file)["open_weather"]

