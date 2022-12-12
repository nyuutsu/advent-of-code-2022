from os import path

with open(path.join('04', '04_input'), 'r') as file:
  data = file.readlines()

def solve(comparator):
  parsed_lines = [
    [[i for i in range(
        int([line.strip() for line in line.split(',')][i].split('-')[0]),
        int([line.strip() for line in line.split(',')][i].split('-')[-1]) + 1)
      ] for i in range(2)
    ] for line in data]  
  return sum(1 for line in parsed_lines
    if comparator(line[1], line[0])
    or comparator(line[0], line[1]))
  
print(solve(lambda l1, l2: not len(set(l1).difference(l2))))
print(solve(lambda l1, l2: len(set(l1).intersection(l2))))