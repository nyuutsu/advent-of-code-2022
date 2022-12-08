import string
import cProfile
import re

def solve_one():
  with open('input', 'r') as file:
    counter = 0
    data = file.readlines()
    for line in data:
      unroll = line.split(',')
      unroll[1] = unroll[1].strip()
      left, right = unroll[0].split('-'), unroll[1].split('-')
      list1, list2 = [], []
      for i in range(int(left[0]), int(left[-1]) + 1):
        list1.append(i)
      for i in range(int(right[0]), int(right[-1]) + 1):
        list2.append(i)
      if len(set(list2).difference(list1)) == 0 or len(set(list1).difference(list2)) == 0:
        counter += 1
    print(f'Part 1: {counter}')

def solve_two():
  with open('input', 'r') as file:
    counter = 0
    for line in file:
      unroll = line.split(',')
      unroll[1] = unroll[1].strip()
      left, right = unroll[0].split('-'), unroll[1].split('-')
      list1, list2 = [], []
      for i in range(int(left[0]), int(left[-1]) + 1):
        list1.append(i)
      for i in range(int(right[0]), int(right[-1]) + 1):
        list2.append(i)
      if len(set(list2).intersection(list1)) or len(set(list1).intersection(list2)):
        counter += 1
    print(f'Part 2: {counter}')

solve_one()
solve_two()

cProfile.run('solve_one()')
cProfile.run('solve_two()')