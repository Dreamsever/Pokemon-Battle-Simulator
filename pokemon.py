import random
import json
import time 
import tkinter as tk
# Listing all pokemon types for later
types = ['normal', 'fire', 'grass', 'water', 'fairy', 'electrik', 'ground', 'rock', 'flying', 'fighting', 'psychic', 'ghost', 'ice', 'dark', 'steel', 'poison', 'dragon', 'bug']

# Creating a move class
class Move:
    """A class that has all of a move characteristics"""
    def __init__(self, name:str, power:int, pp:int, move_type:str):
        move_type = move_type.lower()
        if move_type in types:
            self.name = name.title() # 'flower trick' -> # 'Flower Trick'
            self.power = power
            self.pp = pp # Number of times a move can be used
            self.move_type = move_type
            
        else:
            raise Exception("Type given is not in the type list")
    def __str__(self):
        return (
            f'Move name : {self.name}\n'
            f'Move power : {self.power}\n'
            f'Move pp : {self.pp}\n'
            f'Move type : {self.move_type}'
        )
    def __repr__(self):
        return f"{self.name}"



# Creating a Pokémon class
class Pokemon:
    """A class that has all of a Pokémon's characteristics"""
    def __init__(self, name: str, hp: int, attack: int, defense: int, 
                 attack_sp: int, defense_sp: int, speed: int, ability: str, pokemon_type:str):
        pokemon_type = pokemon_type.lower()
        if pokemon_type in types:
            self.name = name.title() # 'miascarade' -> 'Miascarade'
            self.max_hp = hp
            self.hp = hp
            self.attack = attack
            self.defense = defense
            self.attack_sp = attack_sp
            self.defense_sp = defense_sp
            self.speed = speed
            self.ability = ability
            self.pokemon_type = pokemon_type
            self.moves = []  # List of Move objects
        else:
            raise Exception("Type given is not in the type list")

    def __str__(self):
        return (f'Name: {self.name}\n'
            f'HP: {self.hp}/{self.max_hp}\n'
            f'Attack: {self.attack}\n'
            f'Defense: {self.defense}\n'
            f'Special Attack: {self.attack_sp}\n'
            f'Special Defense: {self.defense_sp}\n'
            f'Speed: {self.speed}\n'
            f'Ability: {self.ability}\n'
            f'Moves : {self.moves}')


    def add_move(self, move: Move):
        if len(self.moves) >= 4:
            print("Cannot add more than 4 moves.")
        elif isinstance(move, Move):
            self.moves.append(move)
        else:
            raise TypeError("Argument given is not a Move object or more than one was given")
        
# Creating a Pokémon object
miascarade = Pokemon('Meowscarada', 76, 110, 70, 81, 70, 123, 'Protean', 'Grass')
charizard = Pokemon('Charizard', 78, 84, 78, 109, 85, 100, 'Blaze', 'Fire')

# Creating a move object
flower_trick = Move('flower trick', 70, 15, 'Grass')
u_turn = Move('u_turn', 70, 15, 'Bug')
flamethrower = Move('flamethrower', 90, 15, 'Fire')
sucker_punch = Move('sucker_punch', 70, 8, 'Dark')
knock_off = Move('knock off', 65, 20, 'Dark')


#Creating a move list
move_list_miascarade = [flower_trick, u_turn, sucker_punch, knock_off]

# Adding moves with a loop
for move in move_list_miascarade:
    miascarade.add_move(move)

# Adding moves to charizard
charizard.add_move(flamethrower)


# Verifying Pokemon objects