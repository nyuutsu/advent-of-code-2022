elves = []
with open('input', 'r') as file:
  calories = 0
  for line in file:
    if line == '' or line == '\n':
      elves.append(calories)
      calories = 0
    else: 
      calories += int(line)
  elves.append(calories)  # I don't like this

print(f'Elf with most calories has {sorted(elves)[-1]}')
print(f'Top three combined are carrying {sum(sorted(elves)[-3:])}')

print(elves)