import json


def read_settings():
    with open('data/settings/settings.json') as file:
        settings = json.load(file)
        return settings
