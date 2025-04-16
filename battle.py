# Importing pokemons and moves
from pokemon import *
import random
import math
import time


def battle_simulator(pokemon1: Pokemon, pokemon2: Pokemon):
    print(f'Battle started ! {pokemon1.name.title()} vs {pokemon2.name.title()}')
    time.sleep(0.5)
    while pokemon1.hp > 0 and pokemon2.hp > 0:
        # Player 1 should choose a move
        for i in range(1,999):
            print(f'Turn {i} !')
            if pokemon1.speed > pokemon2.speed: # Player 1 goes first if he's faster
                print(f'{pokemon1.name.title()} is faster, it goes first !')
                time.sleep(0.5)
                print(f'{pokemon1.name.title()} moves : {pokemon1.moves}')
                choice = str(input('Choose a move ! ')).strip().lower()
                # Check if  the choosen move exists 
                move_found = False
                for move in pokemon1.moves:
                    if choice == move.name.lower():
                        move_found = True
                        print(f'{pokemon1.name} used {choice} !🐲')
                        if critical ==2:
                            print("Critical hit !")
                        pokemon2.take_move(move,pokemon1)
                        print(f'{pokemon2.name} HP : {pokemon2.hp}/{pokemon2.max_hp}')
                        break # Exit the loop once the move is found
                if pokemon1.hp == 0 or pokemon2.hp == 0:
                            print(f'{pokemon1.name} fainted !' if pokemon1.hp ==0 else f'{pokemon2.name} fainted !')
                            break

                if not move_found:
                    raise Exception("Move given is not in the move list")
                
                # Opponent move choice
                print(f"{pokemon2.name}'s turn !")
                time.sleep(0.5)
                ai_choice = random.choice(pokemon2.moves)
                print(f'{pokemon2.name} used {ai_choice.name} !🐲')
                time.sleep(0.3)
                pokemon1.take_move(ai_choice,pokemon2)
                print(f'{pokemon1.name} HP : {pokemon1.hp}/{pokemon1.max_hp}')
                if pokemon1.hp == 0 or pokemon2.hp == 0:
                    print(f'{pokemon1.name} fainted !' if pokemon1.hp ==0 else f'{pokemon2.name} fainted !')
                    break

            
            else:
                # If the ai is faster, it goes first
                print(f'{pokemon2.name} is faster, it goes first !')
                time.sleep(0.5)
                print(f'{pokemon2.name} moves : {pokemon2.moves}')
                ai_choice = random.choice(pokemon2.moves)
                print(f'{pokemon2.name} used {ai_choice.name} !🐲')
                time.sleep(0.5)
                pokemon1.take_move(ai_choice, pokemon2)
                print(f'{pokemon1.name} HP : {pokemon1.hp}/{pokemon1.max_hp}')
                if pokemon1.hp == 0 or pokemon2.hp == 0:
                    print(f'{pokemon1.name} fainted !' if pokemon1.hp ==0 else f'{pokemon2.name} fainted !')
                    break

                # Player's turn
                print(f"{pokemon1.name}'s turn !")
                print(f'{pokemon1.name} moves : {pokemon1.moves}')
                choice = str(input('Choose a move ! ')).strip().lower()
                # Check if choosen move exists 
                move_found = False
                for move in pokemon1.moves:
                    if choice == move.name.lower():
                        move_found = True
                        print(f'{pokemon1.name} used {choice} !🐲')
                        pokemon2.take_move(move, pokemon1)
                        print(f'{pokemon2.name} HP : {pokemon2.hp}/{pokemon2.max_hp}')
                        if pokemon1.hp == 0 or pokemon2.hp == 0:
                            print(f'{pokemon1.name} fainted !' if pokemon1.hp ==0 else f'{pokemon2.name} fainted !')
                            break
                        break # Exit the loop once the move is found

                if not move_found:
                    raise Exception("Move given is not in the move list")

    if pokemon1.hp > pokemon2.hp:
        print(f'Battle finished, {pokemon1.name} won !')
    else:
        print(f'Battle finished, {pokemon2.name} won !')            

