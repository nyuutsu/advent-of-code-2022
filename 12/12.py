from os import path
from string import ascii_lowercase
import matplotlib.pyplot as plot
from networkx import MultiDiGraph, NetworkXNoPath, draw, get_node_attributes, shortest_path_length

class LazyMan:
  def __init__(self, player='S', goal='E', hierarchy=ascii_lowercase):
    self.ELEV_MAP = None
    self.elev_graph = MultiDiGraph()
    self.PLAYER = player
    self.PLAYER_COORD = None
    self.GOAL = goal
    self.GOAL_COORD = None
    self.p2_player_coords = []
    self.HIERARCHY = f'S{hierarchy}E'

  def read_map(self) -> None:
    with open(path.join('12', 'input'), 'r') as file:
      self.ELEV_MAP = [list(x.strip()) for x in file.readlines()]
    for row in range(len(self.ELEV_MAP)):
      for column, value in enumerate(self.ELEV_MAP[row]):
        self.elev_graph.add_node((column, row), v=self.HIERARCHY.find(value), l=value)
        rel_node = self.elev_graph.nodes[(column, row)]
        if column > 0: # if not the first column add + get ref to previous item
          new_node = self.elev_graph.nodes[(column - 1, row)]
          if rel_node['v'] + 1 >= new_node['v']:
            self.elev_graph.add_edge((column, row), (column - 1, row))
          if new_node['v'] + 1 >= rel_node['v']:
            self.elev_graph.add_edge((column - 1, row), (column, row))
        if row > 0: # if not first row add + get ref to previous item
          new_node = self.elev_graph.nodes[(column, row - 1)]
          if new_node['v'] + 1 >= rel_node['v']:
            self.elev_graph.add_edge((column, row - 1), (column, row))
          if rel_node['v'] + 1 >= new_node['v']:
            self.elev_graph.add_edge((column, row), (column, row - 1))

  def detect_poles(self) -> None:
    nodes = get_node_attributes(self.elev_graph, 'l')
    self.PLAYER_COORD = list(nodes.keys())[list(nodes.values()).index('S')]
    self.GOAL_COORD = list(nodes.keys())[list(nodes.values()).index('E')]
    for coordinate, letter in nodes.items():
      if letter == 'a' or letter == 'S':
        self.p2_player_coords.append(coordinate)
            
  def visualize(self) -> None:
    labels = get_node_attributes(self.elev_graph, 'l')
    print(labels)
    # how do I flip the axes on this?
    pos = {(x,y):(y,-x) for x,y in self.elev_graph.nodes()}
    draw(self.elev_graph, pos=pos, node_color='lightgreen', labels=labels)
    plot.show() 

  def recite_map(self) -> None:
    print(*self.ELEV_MAP, sep='\n')

  def solve(self) -> None:
    p2_route_lengths = []
    print(f'P1: {shortest_path_length(self.elev_graph, self.PLAYER_COORD, self.GOAL_COORD) = }')
    amount_errors = 0
    for start_coord in self.p2_player_coords:
      try:
        p2_route_lengths.append(shortest_path_length(self.elev_graph, start_coord, self.GOAL_COORD))
      except NetworkXNoPath:
        amount_errors += 1  # 2299 of these. What should I do with them?
    print(f'P2: {sorted(p2_route_lengths)[0] = }')
    print(f'# NetworkXNoPath exceptions: {amount_errors}')

def main() -> None:
  walker = LazyMan()
  walker.read_map()
  walker.detect_poles()
  #walker.visualize()
  walker.solve()
  
if __name__ == '__main__':
  main()
