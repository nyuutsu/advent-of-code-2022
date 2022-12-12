from enum import Enum
from os import path
from itertools import chain, groupby
import string

class Crane:
  def __init__(self, model):
    Models = Enum('Models', ['CrateMover 9000', 'CrateMover 9001'])
    try:
      Models[model].value
      self.name = model
    except ValueError:
      raise Exception('Crane not found')
    with open(path.join('05', '05_input'), 'r') as file:
      self.data = [line.strip('\n') for line in file.readlines()] 

  # TODO: I'd like a hint on how to do this better
  def _populate_stacks(self, stacks):
    for row in reversed(range(self.data.index('') - 1)):
      columnator = 0
      for column in range(1, len(self.data[row]) + 1, 4):
        if self.data[row][column] in string.ascii_letters:
          stacks[columnator].append(self.data[row][column])
        columnator += 1

  def _one_at_time(self, stacks, quantity, start, target):
    [stacks[target - 1].append(stacks[start - 1].pop()) for i in range(quantity)]

  def _in_batches(self, stacks, quantity, start, target):
    to_be_moved = stacks[start - 1][-quantity:]
    [stacks[target - 1].append(item) for item in to_be_moved]
    stacks[start - 1] = stacks[start - 1][:-quantity]

  def _process_one_row(self, row):
    return [int(x) for x in list(filter(lambda x: x not in ' ', list(chain.from_iterable([[''.join(i)] if j else list(i) for j, i in groupby(list(filter(lambda x: x not in string.ascii_letters, row)), key = str.isdigit)]))))]

  def _parse_instructions(self):
    return [self._process_one_row(row) for row in self.data[self.data.index('') + 1:]]

  def _apply_instructions(self, stacks, instructions, behavior):
    for instruction in instructions:
      quantity, start, target = instruction
      behavior(stacks, quantity, start, target)
      
  def move_crates(self):
    self.stacks = [[] for _ in self.data[self.data.index('') - 1].strip().split()]
    self._populate_stacks(self.stacks)
    self.instructions = self._parse_instructions()
    if self.name == 'CrateMover 9000':
      self._apply_instructions(self.stacks, self.instructions, self._one_at_time)
    else:
      self._apply_instructions(self.stacks, self.instructions, self._in_batches)
    print(f"{self.name}: {''.join([stack[-1] for stack in self.stacks])}")

Crane('CrateMover 9000').move_crates()
Crane('CrateMover 9001').move_crates()