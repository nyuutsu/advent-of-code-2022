import filetree
import math
import pytest

def routine(filename: str):
  fs = filetree.FileSystem(filename)
  fs.populate()
  fs.print()
  fs.traverse('p1', 0)
  fs.traverse('p2', math.inf)
  
def main():
  #routine('test')
  routine('input')

if __name__ == '__main__':
  main()