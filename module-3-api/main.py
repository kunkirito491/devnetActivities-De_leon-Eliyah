import requests
import random

pokemon_list = [
    "Pikachu",
    "Charmander",
    "Squirtle",
    "Bulbasaur",
    "Pidgey",
    "Caterpie",
     "Weedle"
]

pokemon_name = random.choice(pokemon_list)

url= f"https://pokeapi.co/api/v2/pokemon/" + pokemon_name

try:
    response = requests.get(url,timeout=10)

    if response.status_code == 200:
        data = response.json()

        name = data["name"]
        height = data["height"]/10
        weight = data["weight"]/10

        print("Who's that pokemon")
        print("Height:", height, "m")
        print("Weight:", weight, "kg")

        for attempt in range(3):
            answer = input("Guess the pokemon:").lower().strip()

            if answer == name:
                print("correct")
                break
            else:
                print("incorrect")
        else:
            print("The pokemon is: ", name.title())

    elif response.status_code == 404:
        print("Pokemon not found.")

    else:
        print("Error:", response.status_code)

except requests.exceptions.RequestException:
    print("An error occurred:")




