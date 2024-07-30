# VIRTUAL ASSISTANT

This app simulates an assistant.

It has three main functions
* Telling the current time in any town worldwide.
* Displaying the current weather in any town worldwide.
* Displaying a summary of information about a chosen topic.

## Prerequisites

* python3
* poetry
    https://python-poetry.org/docs/
* open weather map API key 
    https://home.openweathermap.org/users/sign_up
    Save key in this format: `open-weather: "key"` in `.api_keys.yaml` file in user's home directory.

## Installation

Clone github repo and type `poetry install` into the command line at the project root. 

# Commands

`poetry run virtual-assistant <sub-command> <option>`

`tell-time`, `weather`, `tell-me-about`

`weather` has CLI option `--temp-scale` which defaults to metric
