from enum import Enum
from os import path

class Score:
  def __init__(self):
    self.score = 0
  
  def __add__(self, amount):
    self.score += amount

def score_p1():
  p1_score = Score()
  game_scores = {('A', 'Y'): 6, ('B', 'Z'): 6, ('C', 'X'): 6,
                 ('A', 'X'): 3, ('B', 'Y'): 3, ('C', 'Z'): 3,
                 ('A', 'Z'): 0, ('B', 'X'): 0, ('C', 'Y'): 0}

  with open(path.join('02', '02_input'), 'r') as file:
    instructions = file.readlines()    
  for your_move, _, enemy_move, _ in instructions:
    p1_score.score += game_scores[(your_move, enemy_move)]
    choice_bonus = {'X': 1, 'Y': 2, 'Z': 3}
    p1_score.score += choice_bonus[enemy_move]
  return p1_score.score

def score_p2():
  p2_score = Score()
  Instruction = Enum('Instruction', ['A', 'B', 'C'])
  Symbol = Enum('Symbol', ['rock', 'paper', 'scissors'])
  
  def make_enemy_win(enemy_action):
    return Symbol((Symbol[enemy_action].value + 1) % 3 + 1).name

  def make_hero_win(enemy_action):
    p2_score.score += 6
    return Symbol((Symbol[enemy_action].value + 3) % 3 + 1).name

  def make_draw(enemy_action):
    p2_score.score += 3
    return enemy_action

  def add_choice_score(my_action):
    p2_score.score += Symbol[my_action].value

  with open(path.join('02', '02_input'), 'r') as file:
    instructions = file.readlines()    

  for your_play, _, enemy_play, _ in instructions:
    name = Symbol(Instruction[your_play].value).name
    outcome = {'X': make_enemy_win, 'Y': make_draw, 'Z': make_hero_win}
    add_choice_score(outcome[enemy_play](name))
    
  return p2_score.score

print(f'P1: {score_p1()}')
print(f'P2: {score_p2()}')