from rich import print

from assistant import get_city_json

def get_weather(city: str, temp_scale: str):
    emojis = {
        "clear": ":sun-emoji:",
        "rain": ":rain-emoji",
        "clouds": ":cloud-emoji:"
        }
        
    api_temp_scale = {"c": "metric", "f": "imperial"}

    weather_json = get_city_json(city, api_temp_scale[temp_scale])
    if weather_json == {'cod': '404', 'message': 'city not found'}:
        print("\nPlease enter a valid city name.")
    else:
        weather = weather_json["weather"][0]["main"].lower()
        emoji = emojis[weather]

        temperature = weather_json["main"]["temp"]
        temp_low = weather_json["main"]["temp_min"]
        temp_high = weather_json["main"]["temp_max"]
        city_name = weather_json["name"]
        
        temp_symbols = {"c": "°C", "f" : "°F"}
        temp_symbol = temp_symbols[temp_scale]

        print(
            f"\nThe weather in {city_name.title()} is {weather} {emoji} \n\nThe temperature is {temperature}{temp_symbol} with" 
            f" a high of {temp_high}{temp_symbol} and a low of {temp_low}{temp_symbol}.\n"
        )

