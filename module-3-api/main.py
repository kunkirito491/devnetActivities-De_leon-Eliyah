
import requests
import random

pokemon_list = [
     "Pikachu"
     "Charmander"
     "Squirtle"
     "Bulbasaur"
     "Pidgey"
     "Caterpie"
     "Weedle"

]

pokemon_name = random.choice(pokemon_list)

url= f"https://pokeapi.co/api/v2/pokemon/" + pokemon_name

try:
    response = requests.get(url,timeout=10)

    if response




