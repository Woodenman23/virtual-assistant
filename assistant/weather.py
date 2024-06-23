from assistant import get_city_json

def get_weather(city: str):

    weather_json = get_city_json(city)
    weather = weather_json["weather"][0]["main"]
    temperature = weather_json["main"]["temp"]
    temp_low = weather_json["main"]["temp_min"]
    temp_high = weather_json["main"]["temp_max"]
    city_name = weather_json["name"]
    print(weather_json)

    print(
        f"\nThe weather in {city_name} is {weather.lower()}. \n\nThe temperature is {temperature}°C with" 
        f" a high of {temp_high}°C and a low of {temp_low}°C.\n"
    )


