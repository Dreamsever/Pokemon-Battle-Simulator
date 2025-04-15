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
    def add_move(self, move:Move):
            self.moves. ppend(move)
    

miascarade = Pokemon('miascarade',10,10,10,10,10,10,'Protéen','Grass')
flower_trick = Move('flower trick', 70, 15, 'Grass')
u_turn = Move('U_turn', 70, 15, 'Bug')

# print(flower_trick)