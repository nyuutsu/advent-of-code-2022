from collections import deque
from os import path

class Instruction:
  def __init__(self, line):
    if line[0] == 'noop':
      self.duration = 1
      self.value = 0
    else:
      self.duration = 2
      self.value = int(line[1])
      
class CRT:
  def __init__(self):
    self.TERMINAL_WIDTH = 40
    self.queue = deque()
    self.register = 1
    self.clock = 0
    self.cursor = 0
    self.interesting_signals = 0

  def get_instructions(self):
    with open(path.join('10', '10_input'), 'r') as file:
      instructions = [[x for x in line.strip().split()] for line in file.readlines()]
    for instruction in instructions:
      self.queue.append(Instruction(instruction))
  
  def do_cycle_cleanup(self):
    self.queue[0].duration -= 1
    if self.queue[0].duration == 0:
      self.register += self.queue[0].value
      self.queue.popleft()

  def track_signal(self):
    if self.clock == 20 or self.clock % 40 - 20 == 0:
      self.interesting_signals += self.clock * self.register

  def print_cursor(self):
    if abs(self.cursor - self.register) % self.TERMINAL_WIDTH <= 1:
      print('█', end='')
    else:
      print(' ', end='')
    if self.clock % self.TERMINAL_WIDTH == 0:
      print('')
      self.cursor = 0
    else:
      self.cursor += 1

  def follow_instructions(self):
    while(self.queue):
      self.clock += 1
      self.track_signal()
      self.print_cursor()
      self.do_cycle_cleanup()
    print(f'interesting signals: {self.interesting_signals}')

crt = CRT()
crt.get_instructions()
crt.follow_instructions()