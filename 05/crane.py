from functools import partial
from itertools import chain, groupby
from os import path
import string

class Crane:
  def __init__(self, model):
    try:
      assert model in ['CrateMover 9000', 'CrateMover 9001']
      self.name = model
    except ValueError:
      raise Exception('Crane not found')
    with open(path.join('05', '05_input'), 'r') as file:
      self.data = [line.strip('\n') for line in file.readlines()] 
    self.stacks = [[] for _ in self.data[self.data.index('') - 1].strip().split()]

  def _populate_stacks(self):
    STACK_SPACING = 4
    for row in reversed(range(self.data.index('') - 1)):
      columnator = 0
      for column in range(1, len(self.data[row]) + 1, STACK_SPACING):
        if self.data[row][column] in string.ascii_letters:
          self.stacks[columnator].append(self.data[row][column])
        columnator += 1
  
  def _one_at_time(self, quantity, start, target):
    self.stacks[target - 1].extend(reversed(self.stacks[start - 1][-quantity:]))
    self.stacks[start - 1] = self.stacks[start - 1][:-quantity]

  def _in_batches(self, quantity, start, target):
    self.stacks[target - 1].extend(self.stacks[start - 1][-quantity:])
    self.stacks[start - 1] = self.stacks[start - 1][:-quantity]

  @classmethod
  def _process_one_row(cls, row):
    grouped = [[''.join(i)] if j else list(i) for j, i in groupby(
      list(filter(lambda x: x not in string.ascii_letters, row)), key=str.isdigit)]
    return [int(x) for x in list(filter(lambda x: x not in ' ', list(chain.from_iterable(grouped))))]

  def _parse_instructions(self):
    return map(self._process_one_row, self.data[self.data.index('') + 1:])
    
  def _apply_instructions(self, instructions, behavior):
    [partial(behavior)(*i) for i in instructions]
      
  def move_crates(self):
    self._populate_stacks()
    instructions = self._parse_instructions()
    self._apply_instructions(instructions,
                             self._one_at_time if self.name == 'CrateMover 9000' else self._in_batches)
    print(f"{self.name}: {''.join([stack[-1] for stack in self.stacks])}")

Crane('CrateMover 9000').move_crates()
Crane('CrateMover 9001').move_crates()