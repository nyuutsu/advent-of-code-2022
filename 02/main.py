from enum import Enum

with open('input', 'r') as file:
  score = 0
  for line in file:
    if ((line[0] == 'A' and line[2] == 'Y') or (line[0] == 'B' and line[2] == 'Z') or (line[0] == 'C' and line[2] == 'X')):  # if you win
      score += 6
    elif((line[0] == 'A' and line[2] == 'X') or (line[0] == 'B' and line[2] == 'Y') or (line[0] == 'C' and line[2] == 'Z')):  # if you draw
      score += 3  #  else: you lose; do nothing
    # regardless, add the value of the choice
    if line[2] == 'X':
      score += 1
    elif line[2] == 'Y':
      score += 2
    elif line[2] == 'Z':
      score += 3
  print(f'Part 1: {score}')

with open('input', 'r') as file:
  score = 0
  Symbol = Enum('Symbol', ['rock', 'paper', 'scissors'])
  Instruction = Enum('Instruction', ['A', 'B', 'C'])

  def make_enemy_win(enemy_action):
    return Symbol((Symbol[enemy_action].value + 1) % 3 + 1).name

  def make_hero_win(enemy_action):
    global score
    score += 6
    return Symbol((Symbol[enemy_action].value + 3) % 3 + 1).name

  def make_draw(enemy_action):
    global score
    score += 3
    return enemy_action

  def add_choice_score(my_action):
    global score
    score += Symbol[my_action].value

  for line in file:
    if line[2] == 'X':  # lose
      my_action = make_enemy_win(Symbol(Instruction[line[0]].value).name)
      add_choice_score(my_action)
    elif line[2] == 'Y':  # draw
      my_action = make_draw(Symbol(Instruction[line[0]].value).name)
      add_choice_score(my_action)
    else:  # win
      my_action = make_hero_win(Symbol(Instruction[line[0]].value).name)
      add_choice_score(my_action)
  
  print(f'Part 2: {score}')