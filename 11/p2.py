# https://adventofcode.com/2022/day/11

from os import path
from pprint import pprint

class ApeMinder:
  def __init__(self):
    self.apes = []

  # TODO:
  def load_instructions(self):
    with open(path.join('11', 'input_file'), 'r') as file:
      instructions = [[x for x in line.strip().split()] for line in file.readlines() if line != '\n']
    _apes = []
    for i in range(0, len(instructions), 6):
      _apes.append(instructions[i:i+6])
    for i in _apes:
      self.apes.append(Ape(i))

class Ape:
  def __init__(self, ape_data):
    _id, _items, _operation, _test, _if_true, _if_false = [x for x in ape_data]
    self.id = int(_id[1].strip(':'))
    self.items = [int(x.strip(',')) for x in _items[2:]]
    if _operation[5] == 'old':
      self.operation = [_operation[4], _operation[5]]
    else:
      self.operation = [_operation[4], int(_operation[5])]
    self.test_for = int(_test[3])
    self.test_true = int(_if_true[5])
    self.test_false = int(_if_false[5])
    self.inspections = 0

  def inspect(self):
    if self.operation[1] == 'old':
      self.items[0] = (self.items[0]**2) % 9699690
    elif self.operation[0] == '+':
      self.items[0] = (self.items[0] + self.operation[1]) % 9699690
    elif self.operation[0] == '*':
      self.items[0] = (self.items[0] * self.operation[1]) % 9699690
    else:
      raise TypeError('inspect parse failed')
    self.inspections += 1

  def test(self):
    if self.items[0] % self.test_for == 0:
      return True
    return False

  def throw(self, truth: bool, game: ApeMinder):
    if truth:
      game.apes[self.test_true].items.append(self.items[0])
    else:
      game.apes[self.test_false].items.append(self.items[0])
    self.items = self.items[1:]

minder = ApeMinder()
minder.load_instructions()

def play_round():
  for ape in minder.apes:
    while ape.items:
      ape.inspect()
      result = ape.test()
      ape.throw(result, minder)

desired_rounds = 10000
for i in range(desired_rounds):
  play_round()

minder.apes.sort(key=lambda x: x.inspections, reverse=True)
print(minder.apes[0].inspections * minder.apes[1].inspections)