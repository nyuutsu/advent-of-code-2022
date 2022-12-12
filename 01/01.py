from os import path

with open(path.join('01', '01_input'), 'r') as file:
  elves = sorted([sum([int(x) for x in line.split()]) for line in file.read().strip().split('\n\n')])
print(f'(P1) Elf with most calories has {elves[-1]}')
print(f'(P2) Top three combined are carrying {sum(elves[-3:])}')