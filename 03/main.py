import string

with open('input', 'r') as file:
  sum = 0
  for line in file:
    midpoint = len(line) // 2
    first_half, second_half = line[:midpoint], line[midpoint:].strip()
    sum += int(string.ascii_letters.index(''.join(set(first_half).intersection(second_half)))) + 1
  print(f'Part 1: {sum}')

with open('input', 'r') as file:
  sum = 0
  lines = file.readlines()
  for i in range(0, len(lines), 3):
    sum += int(string.ascii_letters.index(''.join(set(lines[i].strip()).intersection(lines[i+1].strip()).intersection(lines[i+2].strip())))) + 1
  print(f'Part 2: {sum}')

  # turn 14+15 into sum of list comprehension