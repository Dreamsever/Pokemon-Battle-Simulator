import random
import json
import time 
import tkinter as tk
# Listing all pokemon types for later
types = ['normal', 'fire', 'grass', 'water', 'fairy', 'electrik', 'ground', 'rock', 'flying', 'fighting', 'psychic', 'ghost', 'ice', 'dark', 'steel', 'poison', 'dragon', 'bug']
nature = ['special', 'physical']
critical = 2 if random.randint(1,100) >=90 else 1.0
# Creating a move class
class Move:
    """A class that has all of a move characteristics"""
    def __init__(self, name:str, power:int, move_type:str, move_nature : str):
        move_type = move_type.lower()
        move_nature = move_nature.lower()
        if move_type in types and move_nature in nature:
            self.name = name.lower() # 'Flower trick' -> # 'flower trick'
            self.power = power
            self.move_type = move_type
            self.move_nature = move_nature
            
        else:
            raise Exception("Type given is not in the type list")
    def __str__(self):
        return (
            f'Move name : {self.name}\n'
            f'Move power : {self.power}\n'
            f'Move type : {self.move_type}\n'
            f'Move nature : {self.move_nature}'
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
            self.name = name.lower() # 'meowscarada' -> 'meowscarada'
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
            raise TypeError("Argument given is not a Move object or more than one were given")
        
    def take_move(self, move: Move, attacker, level=50):
        roll = random.uniform(0.85, 1.0) # Random damage range
        stab = 1.5 if move.move_type == attacker.pokemon_type else 1.0 # Move gets a boost if it's the same type as the attacking pokemon
        if move.move_nature == 'special':
            damage = (((2 * level / 5 + 2) * move.power * attacker.attack_sp / self.defense_sp) / 50 + 2) * roll * stab * critical
        else:
            damage = (((2 * level / 5 + 2) * move.power * attacker.attack / self.defense) / 50 + 2) * roll * stab * critical
        self.hp = max(0, round(self.hp - damage))





def load_moves(filepath="moves.json"):
    with open(filepath, "r") as f:
        data = json.load(f)
    return {move_data["name"]: Move(**move_data) for move_data in data}

def load_pokemons(moves_dict, filepath="pokemons.json"):
    with open(filepath, "r") as f:
        data = json.load(f)
    pokemons = {}
    for poke_data in data:
        poke = Pokemon(
            name=poke_data["name"],
            pokemon_type=poke_data["pokemon_type"],
            hp=poke_data["hp"],
            attack=poke_data["attack"],
            defense=poke_data["defense"],
            attack_sp=poke_data["attack_sp"],
            defense_sp=poke_data["defense_sp"],
            speed=poke_data["speed"],
            ability=None  # Add a placeholder for ability if not provided
        )
        # Add moves to the Pokémon
        for move_name in poke_data["moves"]:
            if move_name in moves_dict:
                poke.add_move(moves_dict[move_name])
        pokemons[poke_data["name"]] = poke
    return pokemons

