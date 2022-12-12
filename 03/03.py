from os import path
import string

with open(path.join('03', '03_input'), 'r') as file:
  lines = [line.strip() for line in file.readlines()]

print(f"P1: {sum([int(string.ascii_letters.index(''.join(set(line[:len(line) // 2]).intersection(line[len(line) // 2:])))) + 1 for line in lines])}")
  
print(f"P2: {sum([int(string.ascii_letters.index(''.join(set(lines[i]).intersection(lines[i+1]).intersection(lines[i+2])))) + 1 for i in range(0, len(lines), 3)])}")