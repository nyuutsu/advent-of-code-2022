with open('input') as file:
  data = file.read()

def solve_for(arg):
  for i in range(len(data) - arg):
    if len(set(data[i:i+arg])) == arg:
      print(f'solve_for({arg}): {i+arg}')
      break

solve_for(4)
solve_for(14)

print([x + 4 for x in range(0,len(data)) if len(data[x:x+4]) == len(set(data[x:x+4]))][0])

print([x + 14 for x in range(0,len(data)) if len(data[x:x+14]) == len(set(data[x:x+14]))][0])