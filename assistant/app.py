import typer

from assistant.weather import get_weather
from assistant.time_info import get_time

app = typer.Typer()

# cities with 2 or more words require apostraphes
@app.command()
def tell_time(city: str) -> None:
    get_time(city)


@app.command()
def weather(city: str):
    get_weather(city)


def main():
    app()
