from assistant import get_city_json

def get_weather(city: str, temp_scale: str):

    weather_json = get_city_json(city, temp_scale)
    if weather_json == {'cod': '404', 'message': 'city not found'}:
        print("\nPlease enter a valid city name.")
    else:
        weather = weather_json["weather"][0]["main"]
        temperature = weather_json["main"]["temp"]
        temp_low = weather_json["main"]["temp_min"]
        temp_high = weather_json["main"]["temp_max"]
        city_name = weather_json["name"]
        
        temp_symbols = {"metric": "°C", "imperial" : "°F"}
        temp_symbol = temp_symbols[temp_scale]

        print(
            f"\nThe weather in {city_name.title()} is {weather.lower()}. \n\nThe temperature is {temperature}{temp_symbol} with" 
            f" a high of {temp_high}{temp_symbol} and a low of {temp_low}{temp_symbol}.\n"
        )


