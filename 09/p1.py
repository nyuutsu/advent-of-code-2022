import string
from enum import Enum
from pprint import pprint

class Direction(Enum):
  L = (-1, 0)
  R = (1, 0)
  U = (0,1)
  D = (0,-1)

class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def __add__(self, other_point):
    return Point(self.x + other_point[0], self.y + other_point[1])

  def __str__(self):
    return f'({self.x},{self.y})'

class Rope:
  def __init__(self):
    self.H = Point(0, 0)
    self.T = Point(0, 0)
    self.log = set()
    self.log.add((self.T.x, self.T.y))

  def update(self, direction, amount):
    print(f'update by: {direction} {amount}')
    for i in range(amount):
      self.H += Direction[direction].value
      if abs(self.H.x - self.T.x) >= 2 or abs(self.H.y - self.T.y) >= 2:
        self.T += Direction[direction].value
        if Direction[direction] in {Direction.U, Direction.D}:
          self.T.x = self.H.x
        elif Direction[direction] in {Direction.L, Direction.R}:
          self.T.y = self.H.y
        else:
          raise ValueError('should never happen')
        print(f'current location of tail: {str(self.T)}')
        self.log.add((self.T.x, self.T.y))

def get_instructions(file_name):
  with open(f'{file_name}', encoding='utf-8') as file:
    instructions = [[x if x.isalpha() else int(x) for x in line.strip().split()] for line in file.readlines()]
  return instructions
  
def main():
  input = 'example_2'
  rope = Rope()
  instructions = get_instructions(input)
  for direction, amount in instructions:
    rope.update(direction, amount)
  pprint(f'locations visited by tail: {len(rope.log)}:')
  if input == 'example':
    try:
      assert(len(rope.log) == 13)
    except:
      raise ValueError('test input must return 13')
  #else:
    #assert(len(rope.log) == 6044)

main()