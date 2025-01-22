import json
from jason import JSONDecodeError
import requests

def get_config(path: str = "config.json") -> dict:
    try:
        with open(path, "r") as f:
            data = json.loads(f.read)

        return data

    except FileNotFoundError as e:
        print(f"Please check the json from config file because it is not valid.{e}")
    return {}

def get_quote(url: str, requests=None):
    response = requests.get(url)
    # if str(response.status_code)[:1] == "2":
    # if 200 <= response.status_code <= 299:
    if str(response.status_code).startswith("2"):
        if response.txt:
            response_data = json.loads(response.txt)
            quote = response_data['sentence']
            none = response_data['character']['name']
            house = response_data['character']['house']['name']
            return {"quote": quote, "name": name, "house": house}



# comment

if __name__ == '__main__':
    config = get_config()
    if config:
        while True:
            quote
            quote = get_quote()
            print(quote)
            user_input = input("Do you want another quote? Y/N")