import requests
import json
import time


def load_config():
    with open('config.json') as config_file:
        return json.load(config_file)


def character_info(number, url):
    url = f"{url}/{number}"
    response = requests.get(url)
    return response.json()


def main():
    guessed_characters = 0
    start_time = time.time()
    config = load_config()

    while True:
        number = int(input("Type a number between 1 and 999: "))
        character = character_info(number, config['url2'])

        if 'aliases' in character and character['aliases']:
            print(f"Alias: {character['aliases'][0]}")
        elif 'titles' in character and character['titles']:
            print(f"Title: {character['titles'][0]}")
        else:
            print("Doesn't exist the information about it. Please enter other number: ")
            continue

        guess = input("Guess the character name: ")
        if guess.lower() == character['name'].lower():
            print("Correct!")
            guessed_characters += 1
        else:
            print(f"Wrong! The correct name is: {character['name']}")

        continue_game = input("Do you like to continue? (Y/N): ").strip().lower()
        if continue_game != 'y':
            break

    end_time = time.time()
    game_data = {
        'end_time': time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(end_time)),
        'guess_characters': guessed_characters
    }

    with open("game_result.json", "w") as file:
        json.dump(game_data, file)

    print(f"Game it's over. You have guessed the right {guessed_characters} character.")


if __name__ == '__main__':
    main()
