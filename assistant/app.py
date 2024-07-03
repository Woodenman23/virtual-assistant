import typer
from typing_extensions import Annotated, Optional

from assistant.weather import get_weather
from assistant.time_info import get_time
from assistant.wiki_search import wiki_search

app = typer.Typer()

# cities with 2 or more words require apostraphes
@app.command()
def tell_time(city: Annotated[str, typer.Argument()] = "San Francisco") -> None:
    get_time(city)


@app.command()
def weather(city: Annotated[str, typer.Argument()] = "San Francisco", temp_scale: Optional[str] = "metric") -> None:
    try:
        get_weather(city, temp_scale)
    except(KeyError):
        print("\nPlease enter a valid temperature scale")

@app.command()
def tell_me_about(subject: str) -> None:
    wiki_search(subject)

def main():
    app()
