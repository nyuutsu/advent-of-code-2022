import math, re, string
from collections import deque
from anytree import Node, RenderTree
from tqdm import tqdm, trange

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
    temp = line.split(' ')
    if re.match('^dir', line):
      Node(f'{temp[1]}', parent=self.cursor, type='dir', size=0)
    elif re.match('^[^a-z]', temp[0]):  # create file
      Node(f'{temp[1]}', parent=self.cursor, type='file', size=int(temp[0]))
      self._increase_folder_sizes(int(temp[0]))    
    else:  # this was useful for testing. do I keep it in now?
      raise Exception(f'ls parsing exception for line: {line}')

  def _perform_cd(self, line: str):
    temp = line.split(' ')
    if re.match('^\.\.', temp[2]): # go to parent
      self.cursor = self.cursor.parent
    elif re.match('^[a-z]', temp[2][0]): # go to child
      for node in self.cursor.children:
        if node.name == temp[2]:  # "if [...] if" -- avoidable??
          self.cursor = node
    elif re.match('^/', temp[2]):  # go to /
      self.cursor = self.head
    else:  # this was useful for testing. do I keep it in now?
      raise Exception(f'cd type: {line}')
    
  def populate(self):
    with open(f'{self._FILE_NAME}', encoding='utf-8') as file:
      inputs = file.readlines()
    for line in tqdm(inputs):  # go for a walk
      line = line.strip()
      if re.match('^\$\ cd', line):
        self._perform_cd(line)
      elif re.match('^[^\$]', line):
        self._perform_ls(line)
    self._unused_space = self._DISK_CAPACITY - self.head.size

  def print(self):
    for pre, _, node in RenderTree(self.head):
      print(f'{pre}{node.name}')
    
  def traverse(self, flag: str, initializer: int):
    tracker = initializer
    stack = deque()
    stack.append(self.head)
    while(stack):
      tmp = stack.pop()
      if flag == 'p1':
        if tmp.size <= self._MAX_SIZE:
          tracker += tmp.size
      elif flag == 'p2':
        if self._unused_space + tmp.size >= self._TARGET_UNUSED and tmp.size < tracker:
          tracker = tmp.size
      for node in tmp.children:
        if node.type=='dir':
          stack.append(node)
    print(f'{flag}: {tracker}')