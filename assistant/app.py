from datetime import datetime
import pytz
import typer

app = typer.Typer()

@app.command()
def tell_time(city="San Francisco"):
    city_tz = pytz.timezone("US/Pacific")
    city_datetime = datetime.now(city_tz)
    city_current_time = city_datetime.strftime("%H:%M:%S")
    print(f"The time in {city} is {city_current_time}")

@app.command()
def zones():
    print(pytz.all_timezones)

def main():
    app()