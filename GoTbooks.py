import requests
import json


def load_config():
    with open('config.json') as config_file:
        return json.load(config_file)

def get_books_published_after(year, url):
    response = requests.get(url)
    books = response.json()

    filter_books = [book['name'] for book in books if int(book['released'][:4]) > year]
    return filter_books

if __name__ == '__main__':
    config = load_config()
    year = int(input("Input the year: "))
    books = get_books_published_after(year, config['book_url'])
    print(f"Books published after the {year}: {books}")