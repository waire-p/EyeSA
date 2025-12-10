import json


def read_settings():
    with open('data/settings.json') as file:
        settings = json.load(file)
        return settings
