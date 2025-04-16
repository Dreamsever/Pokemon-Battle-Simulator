from pokemon import *
from battle import battle_simulator

moves = load_moves()
pokemons = load_pokemons(moves)

charizard = pokemons["charizard"]
meowscarada = pokemons["meowscarada"]
flamethrower = moves["Flamethrower"]
flower_trick = moves["Flower Trick"]

charizard.add_move(flamethrower)
meowscarada.add_move(flower_trick)

battle_simulator(meowscarada,charizard)
