from pokemon import *
from battle import battle_simulator

moves = load_moves()
pokemons = load_pokemons(moves)

# Adding pokemons 
charizard =   pokemons["charizard"]
meowscarada = pokemons["meowscarada"]
tinkaton =     pokemons["tinkaton"]
# Adding moves
flamethrower = moves["Flamethrower"]
flower_trick = moves["Flower Trick"]
iron_head =    moves["Iron Head"]
iron_tail =    moves["Iron Tail"]

# Adding moves to pokemons
charizard.add_move(flamethrower)
meowscarada.add_move(flower_trick)
tinkaton.add_move(iron_head)
tinkaton.add_move(iron_tail)

battle_simulator(tinkaton,meowscarada)
