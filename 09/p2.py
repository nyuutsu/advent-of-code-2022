from enum import Enum
from pprint import pprint

class Direction(Enum):
  L = (-1,0)
  R = (1,0)
  U = (0,1)
  D = (0,-1)
  RU = (1,1)
  LU = (-1,1)
  RD = (1,-1)
  LD = (-1,-1)

class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def __add__(self, other_point):
    return Point(self.x + other_point[0], self.y + other_point[1])

  def __str__(self):
    return f'({self.x},{self.y})'

  def set_x(self, new_x):
    self.x = new_x

  def set_y(self, new_y):
    self.y = new_y

  def get_x(self):
    return self.x

  def get_y(self):
    return self.y


class Rope:
  def __init__(self):
    self.state = []
    for i in range(10):
      self.state.append(Point(0, 0))
    self.log = set()
    self.log.add((self.state[-1].x, self.state[-1].y))

  def update(self, direction, amount):
    print(f'update by: {direction} {amount}')
    for rel_head in range(len(self.state) - 1): # to each sequential pair

      for i in range(amount): # for each n moved
        self.state[rel_head] += Direction[direction].value # move head by one in a cardinal direction

        if abs(self.state[rel_head].get_x() - self.state[rel_head + 1].get_x()) >= 2 and abs(self.state[rel_head].get_y() - self.state[rel_head + 1].get_y()) >= 2:
          print(f'!!!!!{self.state[rel_head].get_y()}')
          print('the following two pairs should be two apart on at both axises')
          print(f'rel head: {self.state[rel_head].get_x()}, {self.state[rel_head].get_y()}')
          print(f'rel tail: {self.state[rel_head+1].get_x()}, {self.state[rel_head+1].get_y()}')
          if self.state[rel_head].get_x() > self.state[rel_head + 1].x and self.state[rel_head].get_y() > self.state[rel_head + 1].y:
            self.state[rel_head + 1] += Direction['RU'].value
          
          elif self.state[rel_head].get_x() < self.state[rel_head + 1].x and self.state[rel_head].get_y() < self.state[rel_head + 1].y:
            self.state[rel_head + 1] += Direction['LD'].value
          
          elif self.state[rel_head].get_x() > self.state[rel_head + 1].x and self.state[rel_head].get_y() < self.state[rel_head + 1].y:
            self.state[rel_head + 1] += Direction['RD'].value
          
          elif self.state[rel_head].get_x() < self.state[rel_head + 1].x and self.state[rel_head].get_y() > self.state[rel_head + 1].y:
            self.state[rel_head + 1] += Direction['LU'].value
          
          else:
            raise ValueError('should never happen')          
          self.log.add((self.state[-1].x, self.state[-1].y))
          
        elif abs(self.state[rel_head].get_x() - self.state[rel_head + 1].x) >= 2:
          if self.state[rel_head].get_x() > self.state[rel_head + 1].x:
            self.state[rel_head + 1] += Direction['R'].value

          elif self.state[rel_head].get_x() < self.state[rel_head + 1].x:
            self.state[rel_head + 1] += Direction['L'].value
          
          else:
            raise ValueError('should never happen')
          self.log.add((self.state[-1].x, self.state[-1].y))
          
        elif abs(self.state[rel_head].get_y() - self.state[rel_head + 1].y) >= 2:
          if self.state[rel_head].get_y() > self.state[rel_head + 1].y:
            self.state[rel_head + 1] += Direction['U'].value
          
          elif self.state[rel_head].get_y() < self.state[rel_head + 1].y:
            self.state[rel_head + 1] += Direction['D'].value
          
          else:
              raise ValueError('should never happen')
          self.log.add((self.state[-1].x, self.state[-1].y))
        
def get_instructions(file_name):
  with open(f'{file_name}', encoding='utf-8') as file:
    instructions = [[x if x.isalpha() else int(x) for x in line.strip().split()] for line in file.readlines()]
  return instructions
  
def main():
  input = 'example'
  rope = Rope()
  instructions = get_instructions(input)
  for direction, amount in instructions:
    rope.update(direction, amount)
  pprint(f'locations visited by final tail: {len(rope.log)}:')

main()