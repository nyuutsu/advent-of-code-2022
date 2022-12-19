from ast import literal_eval
from os import path
from pprint import pprint
from typing import Optional

def get_next_from(source: list[Optional: int, Optional: list]) -> list[Optional: int, Optional: list] or None:
  """
  helper function for compare_this_pair()
  get next thing; don't explode if one
  """
  try:
    return next(source)
  except StopIteration:
    return None

def compare_this_pair(left: list[Optional: int, list: Optional],
                      right: list[Optional: int, list: Optional]):
  
  left, right = iter(left), iter(right)
  next_left, next_right = get_next_from(left), get_next_from(right)
  
  if next_left is None and next_right is not None:
    return True
  if next_right is None and next_left is not None:
    return False
  
  while next_left or next_right or type(next_left) is list and type(next_right) is list:

    if type(next_left) is int and type(next_right) is int:
      if next_left < next_right:
        return True
      elif next_left > next_right:
        return False
      
    if type(next_left) is list and type(next_right) is list:
      return compare_this_pair(next_left, next_right)

    if type(next_left) is not type(next_right):
      if type(next_left) is int:
        next_left = [next_left]
      if type(next_right) is int:
        next_right = [next_right]
      return compare_this_pair(next_left, next_right)

    next_left = get_next_from(iter(left))
    next_right = get_next_from(iter(right))
    
    if next_left is None:
      return True
    if next_right is None:
      return False
      
def main() -> None:
  with open(path.join('13', 'example'), 'r') as file:  # 13
  #with open(path.join('13', 'input'), 'r') as file:  # 4832 too low
    data = [x.strip() for x in file.readlines() if x != '\n']
  parsed_data = iter([literal_eval(x) for x in data])

  p1_index_accumulator = 0

  for index, comparison_pair in enumerate(list(zip(parsed_data, parsed_data))):
    left, right = comparison_pair[0], comparison_pair[1]    
    outcome = compare_this_pair(left, right)
    if outcome:
      p1_index_accumulator += index + 1
  print(f'Sum of 1-indexed indices of ordered pairs: {p1_index_accumulator}')

if __name__ == '__main__':
  main()