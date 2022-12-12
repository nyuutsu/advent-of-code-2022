from os import path

with open(path.join('06', '06_input'), 'r') as file:
  data = file.read()

def solve_for(arg):
  return next(x + arg for x in range(len(data)) if len(data[x:x+arg]) == len(set(data[x:x+arg])))
  
print(f'solving for 4: {solve_for(4)}')
print(f'solving for 14: {solve_for(14)}')