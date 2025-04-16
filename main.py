from pokemon import *
from battle import battle_simulator

moves = load_moves()
pokemons = load_pokemons(moves)

charizard = pokemons["charizard"]
meowscarada = pokemons["meowscarada"]
flamethrower = moves["Flamethrower"]

meowscarada.add_move(flamethrower)

print(flamethrower)
