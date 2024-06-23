from datetime import datetime, timedelta, timezone
import pytz
import json

from assistant import get_city_json

def get_time(city: str) -> None:
    
    try:
        time_zone_name = get_time_zone(city)
        time_zone = pytz.timezone(time_zone_name)
        city_datetime = datetime.now(time_zone)
    except(KeyError):
        city_json = get_city_json(city)
        time_zone_offset = city_json["timezone"]
        offest_timedelta = timedelta(seconds=time_zone_offset)
        time_zone = timezone(offest_timedelta)
        now_utc = datetime.now(timezone.utc)
        city_datetime = now_utc.astimezone(time_zone)
    city_current_time = city_datetime.strftime("%H:%M:%S")
    print(f"The time in {city.capitalize()} is {city_current_time}.")

def get_time_zone(city: str) -> str:
    with open("assistant/data/cities.json", "r") as file:
        time_zones = json.load(file)
        return time_zones[city.lower()]
            