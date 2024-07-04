
import typer
from rich import print
from typing_extensions import Annotated, Optional


from assistant.weather import get_weather
from assistant.time_info import get_time
from assistant.wiki_search import wiki_search

app = typer.Typer()

def main():
    """
    Ask me about the time or weather anywhere in the world
    or ask me about a subject.
    """
    app()

# cities with 2 or more words require apostraphes
@app.command()

def tell_time(city: Annotated[str, typer.Argument()] = "San Francisco") -> None:
    """
    I can tell you the time anywhere in the world.
    """
    get_time(city)


@app.command()
def weather(city: Annotated[str, typer.Argument()] = "San Francisco", temp: Optional[str] = "c") -> None:
    """
    Ask me about the weather anywhere in the world. 
    I can display the temperature in farenheit with 
    the --temp f option.
    """
    try:
        get_weather(city, temp)
    except(KeyError):
        print("\nPlease enter a valid temperature scale")

@app.command()
def tell_me_about(subject: str) -> None:
    wiki_search(subject)

if __name__ == "__main__":
    typer.run(main)
