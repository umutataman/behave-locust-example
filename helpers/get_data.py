import json


def get_city_data(city):
    with open(f'data/cities.json') as f:
        cities = json.load(f)
    return cities[city]
