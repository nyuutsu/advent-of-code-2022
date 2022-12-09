def populate(file_name):
  grid = []
  with open(f'{file_name}', encoding='utf-8') as file:
    [grid.append([int(x) for x in line.strip()]) for line in file.readlines()]
  return grid

def detect_up(grid, outer, inner):
  return not any(grid[outer][inner] <= grid[i][inner] for i in range(0, outer))

def detect_down(grid, outer, inner):
  return not any(grid[outer][inner] <= grid[i][inner] for i in range(outer + 1, len(grid)))

def detect_left(grid, outer, inner):
  return not any(grid[outer][inner] <= grid[outer][i] for i in range(0, inner))

def detect_right(grid, outer, inner):
  return not any(grid[outer][inner] <= grid[outer][i] for i in range(inner + 1, len(grid[0])))
  
def detect(grid, outer, inner):
  return any(fn(grid, outer, inner) for fn in [detect_left, detect_right, detect_up, detect_down])

def quantify(the_grid):
  return sum(sum(detect(the_grid, outer, inner) for inner in range(len(the_grid[0]))) for outer in range(len(the_grid)))
  
def main():
  print(f'unobstructed trees: {quantify(populate("input"))}')
  
main()