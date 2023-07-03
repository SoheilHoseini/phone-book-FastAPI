from fastapi import FastAPI
from random import randrange
from enum import Enum

app = FastAPI()

class Weapon(str, Enum):
    rock = 'rock'
    paper = 'paper'
    scissors = 'scissors'

@app.get('/')
async def read_root():
    return {'message': 'Hello World'}

@app.get('/shoot/{weapon}')
async def shoot(weapon: Weapon):

    game_key = {
        ('rock', 'rock'): "It's a tie.",
        ('rock', 'paper'): "You lost.",
        ('rock', 'scissors'): "You won!",
        ('paper', 'rock'): "You won!",
        ('paper', 'paper'): "It's a tie.",
        ('paper', 'scissors'): "You lost.",
        ('scissors', 'rock'): "You lost.",
        ('scissors', 'paper'): "You won!",
        ('scissors', 'scissors'): "It's a tie.",
    }
    weapons = ['rock', 'paper', 'scissors']
    opp_weapon = weapons[randrange(0, 3)]
    message = game_key[(weapon, opp_weapon)]
    result = {'user_weapon': weapon, 'opponent_weapon': opp_weapon, 'message': message}

    return result
