from collections import deque
from os import path
from re import match
from anytree import Node, RenderTree

class FileSystem:
  def __init__(self, file_flag: str):
    self._FILE_NAME = file_flag
    self._DISK_CAPACITY = 70000000
    self._TARGET_UNUSED = 30000000
    self._MAX_SIZE = 100000
    self._unused_space = None
    self.head = Node('', parent=None, type='dir', size=0)
    self.cursor = self.head

  def _increase_folder_sizes(self, amount: int):
    tmp = self.cursor
    while tmp is not None:
      tmp.size += amount
      tmp = tmp.parent
  
  def _perform_ls(self, line: str):
    try:
      sh_symbol, command = line.split(' ')
    except ValueError as e:
      print(f'Error: Expected one command line argument for \'cd\': {e}')
    if match('^dir', line):
      Node(f'{command}', parent=self.cursor, type='dir', size=0)
    elif match('^[^a-z]', sh_symbol):  # create file
      Node(f'{command}', parent=self.cursor, type='file', size=int(sh_symbol))
      self._increase_folder_sizes(int(sh_symbol))
    else:
      raise TypeError(f'ls parsing exception for line: {line}')

  def _perform_cd(self, line: str):
    try:
      sh_symbol, command, directory = line.split(' ')
    except ValueError as e:
      print(f'Error: Expected one command line argument for \'cd\': {e}')
    if match('^\.\.', directory): # go to parent
      self.cursor = self.cursor.parent
    elif match('^[a-z]', directory[0]): # go to child
      self.cursor = next(filter(lambda n: n.name == directory, self.cursor.children))
    elif match('^/', directory):  # go to /
      self.cursor = self.head
    else:
      raise TypeError(f'cd type: {line}')
    
  def populate(self):
    with open(path.join('07', self._FILE_NAME), 'r', encoding='utf-8') as file:
      inputs = file.readlines()
    for line in inputs:
      line = line.strip()
      if match('^\$\ cd', line):
        self._perform_cd(line)
      elif match('^[^\$]', line):
        self._perform_ls(line)
    self._unused_space = self._DISK_CAPACITY - self.head.size

  def print(self):
    for pre, _, node in RenderTree(self.head):
      print(f'{pre}{node.name}')
    
  def traverse(self, flag: str, initializer: int):
    tracker = initializer
    stack = deque()
    stack.append(self.head)
    while stack:
      current = stack.pop()
      if flag == 'p1':
        if current.size <= self._MAX_SIZE:
          tracker += current.size
      elif flag == 'p2':
        if self._unused_space + current.size >= self._TARGET_UNUSED and current.size < tracker:
          tracker = current.size
      for node in current.children:
        if node.type == 'dir':
          stack.append(node)
    print(f'{flag}: {tracker}')