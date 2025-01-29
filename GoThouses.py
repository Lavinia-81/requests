import requests
import json


def load_config():
    with open('config.json') as config_file:
        return json.load(config_file)


def get_all_houses(api_url):
    houses = []
    page = 1
    while True:
        response = requests.get(f"{api_url}?page={page}&pageSize=50")
        page_houses = response.json()
        if not page_houses:
            break
        houses.extend(page_houses)
        page += 1
    return houses

def houses_and_leaders(houses):
    for house in houses:
        name = house['name']
        current_lord = house['currentLord']
        ruler_name = "Unknown"
        if current_lord:
            ruler_response = requests.get(current_lord)
            ruler = ruler_response.json()
        print(f"House: {name}, Current Leader: {ruler_name}")


if __name__ == '__main__':
    config = load_config()
    houses = get_all_houses(config['house_url'])
    houses_and_leaders(houses)







