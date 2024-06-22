from datetime import datetime
import json
import pytz
import typer

from assistant.weather import get_weather

app = typer.Typer()

# cities with 2 or more words require apostraphes
@app.command()
def tell_time(city: str):
    time_zone = get_time_zone(city)
    pytz_time_zone = pytz.timezone(time_zone)
    city_datetime = datetime.now(pytz_time_zone)
    city_current_time = city_datetime.strftime("%H:%M:%S")
    print(f"The time in {city.capitalize()} is {city_current_time}")


def get_time_zone(city: str):
    with open("assistant/data/cities.json", "r") as file:
        time_zones = json.load(file)
        return time_zones[city.lower()]

@app.command()
def weather_forcast(city: str):
    get_weather(city)

@app.command()
def zones():
    print(pytz.all_timezones)


def main():
    app()
