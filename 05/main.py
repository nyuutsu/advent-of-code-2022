from pprint import pprint
from itertools import chain, groupby
import string

def solve_one():
  with open('input') as file:
    data = [line.strip('\n') for line in file.readlines()] 
  #pprint(data)

  stacks = []
  for entity in data[data.index('') - 1].strip().split():
    stacks.append([])

  for row in reversed(range(data.index('') - 1)): # make me a function
    columnator = 0
    for column in range(1, len(data[row]) + 1, 4):
      if data[row][column] in string.ascii_letters:
        stacks[columnator].append(data[row][column])
      columnator += 1

  for row in data[data.index('') + 1:]: # make me a function, also, don't do this in intermingled like this
    temp = list(filter(lambda x: x not in string.ascii_letters, row))
    res = [''.join([i for i in temp if not i.isalpha()]), *[j for j in temp if j.isalpha()]] 
    num_group = groupby(temp, key = str.isdigit)
    both_group = [[''.join(i)] if j else list(i) for j, i in num_group]
    result = list(filter(lambda x: x not in ' ', res))    
    result = [int(x) for x in result]

    for i in range(result[0]): # make me one-line
      stacks[result[2] - 1].append(stacks[result[1] - 1].pop())

  for stack in stacks:
    print(stack[-1], end='')
  print('')

def solve_two():
  with open('input') as file:
    data = [line.strip('\n') for line in file.readlines()] 

  stacks = []
  for entity in data[data.index('') - 1].strip().split():
    stacks.append([])

  for row in reversed(range(data.index('') - 1)):
    columnator = 0
    for column in range(1, len(data[row]) + 1, 4):
      if data[row][column] in string.ascii_letters:
        stacks[columnator].append(data[row][column])
      columnator += 1

  for row in data[data.index('') + 1:]:
    for item in row:
      if item in string.digits:
        item = int(item)
    temp = list(filter(lambda x: x not in string.ascii_letters, row))
    res = [''.join([i for i in temp if not i.isalpha()]), *[j for j in temp if j.isalpha()]] 
    num_group = groupby(temp, key = str.isdigit)
    both_group = [[''.join(i)] if j else list(i) for j, i in num_group]
    res = list(chain.from_iterable(both_group))
    result = list(filter(lambda x: x not in ' ', res))    
    result = [int(x) for x in result]
    
    to_be_moved = stacks[result[1] - 1][-result[0]:]
    
    for item in to_be_moved:
      stacks[result[2] - 1].append(item)
    stacks[result[1] - 1] = stacks[result[1] - 1][:-result[0]]

  for stack in stacks:
    print(stack[-1], end='')

solve_one()
solve_two()
