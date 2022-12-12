from cProfile import Profile
from os import path
from pstats import Stats

def solve_one():
  with open(path.join('04', '04_input'), 'r') as file:
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
    print(f'P Old: {counter}')

def solve_one_new():
  with open(path.join('04', '04_input'), 'r') as file:
    data = file.readlines()
  parsed_lines = [[[i for i in range(int([line.strip() for line in line.split(',')][i].split('-')[0]), int([line.strip() for line in line.split(',')][i].split('-')[-1]) + 1)] for i in range(2)] for line in data]
  print(f'P1 New: {sum(1 for line in parsed_lines if len(set(line[1]).difference(line[0])) == 0 or len(set(line[0]).difference(line[1])) == 0)}')

def solve_two():
  with open(path.join('04', '04_input'), 'r') as file:
    data = file.readlines()
  counter = 0
  for line in data:
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

def solve_two_new():
  with open(path.join('04', '04_input'), 'r') as file:
    data = file.readlines()
  parsed_lines = [[[i for i in range(int([line.strip() for line in line.split(',')][i].split('-')[0]), int([line.strip() for line in line.split(',')][i].split('-')[-1]) + 1)] for i in range(2)] for line in data]
  print(f'P2 New: {sum(1 for line in parsed_lines if len(set(line[1]).intersection(line[0])) or len(set(line[0]).intersection(line[1])))}')

def main():
  for func in [solve_one, solve_one_new, solve_two, solve_two_new]:
    pr = Profile()
    pr.enable()
    func()
    pr.disable()
    stats = Stats(pr)
    stats.sort_stats('tottime').print_stats(10)
  
if __name__ == "__main__":
  main()
  