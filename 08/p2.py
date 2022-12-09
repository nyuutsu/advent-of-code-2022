from functools import reduce

def populate(file_name):
  grid = []
  with open(f'{file_name}', encoding='utf-8') as file:
    [grid.append([int(x) for x in line.strip()]) for line in file.readlines()]
  return grid

def score_up(grid, outer, inner):
  scenicness = 0
  for i in reversed(range(0, outer)):
    scenicness += 1
    if grid[outer][inner] <= grid[i][inner]:
      break
  return scenicness

def score_left(grid, outer, inner):
  scenicness = 0
  for i in reversed(range(0, len(grid[outer][:inner]))):  # !?
    scenicness += 1
    if grid[outer][inner] <= grid[outer][i]:
      break
  return scenicness

def score_down(grid, outer, inner):
  scenicness = 0
  for i in range(outer + 1, len(grid[inner])):
    scenicness += 1
    if grid[outer][inner] <= grid[i][inner]:
      break
  return scenicness
  
def score_right(grid, outer, inner):
  scenicness = 0
  for i in range(inner + 1, len(grid[outer])):
    scenicness += 1
    if grid[outer][inner] <= grid[outer][i]:
      break
  return scenicness

def detect(grid, outer, inner):
  return reduce(lambda a, b: a * b,
         [fn(grid, outer, inner) for fn in [
           score_up, score_down, score_left, score_right]])
  
def quantify(the_grid):
  return max(max(detect(the_grid, outer, inner) for inner in range(len(the_grid[0]))) for outer in range(len(the_grid)))

def main():
  print(f'highest scenic score: {quantify(populate("input"))}')
  
main()