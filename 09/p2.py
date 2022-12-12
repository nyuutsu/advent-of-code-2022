# Alyssa's attempt at fixing my answer; close! We'll have to try this one again.

import string
from enum import Enum
from pprint import pprint

class Direction(Enum):
  L = (-1, 0)
  R = (1, 0)
  U = (0, 1)
  D = (0, -1)

class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def __add__(self, other_point):
    return Point(self.x + other_point[0], self.y + other_point[1])

  def __str__(self):
    return f'({self.x},{self.y})'

class Rope:
  def __init__(self, num_points=10):
    self.points = [Point(0, 0) for _ in range(num_points)]
    self.log = set()
    self.log.add((self.T.x, self.T.y))

  @property
  def H(self):
    return self.points[0]

  @property
  def T(self):
    return self.points[-1]

  def update(self, direction, amount):
    print(f'update by: {direction} {amount}')
    for i in range(amount):
      self.points[0] += Direction[direction].value
      for point in range(1, len(self.points)):
        head_point, tail_point = self.points[point - 1], self.points[point]

        if head_point.x - tail_point.x >= 2:
          new_direction = Direction['R']
        elif head_point.x - tail_point.x <= -2:
          new_direction = Direction['L']
        elif head_point.y - tail_point.y >= 2:
          new_direction = Direction['U']
        elif head_point.y - tail_point.y <= -2:
          new_direction = Direction['D']
        else:
          new_direction = None

        if new_direction:
          tail_point += new_direction.value
          if new_direction in {Direction.U, Direction.D}:
            tail_point.x = head_point.x
          elif new_direction in {Direction.L, Direction.R}:
            tail_point.y = head_point.y
          else:
            raise ValueError('should never happen')
          self.points[point] = tail_point
      print(f'current location of tail: {str(self.T)}')
      self.log.add((self.T.x, self.T.y))

def get_instructions(file_name):
  with open(f'{file_name}', encoding='utf-8') as file:
    instructions = [[x if x.isalpha() else int(x)for x in line.strip().split()]
                    for line in file.readlines()]
  return instructions
  
def main():
  fname = 'input'
  rope = Rope()
  instructions = get_instructions(fname)
  for direction, amount in instructions:
    rope.update(direction, amount)
  pprint(f'locations visited by tail: {len(rope.log)}:')
  if fname == 'example':
    try:
      assert(len(rope.log) == 36)
    except AssertionError as e:
      raise ValueError('test input must return 36')
  # else:
    # assert(len(rope.log) == 6044)

main()