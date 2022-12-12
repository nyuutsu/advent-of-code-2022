from os import path

with open(path.join('04', '04_input'), 'r') as file:
    data = file.readlines()

print(f"P1 New: {sum(1 for line in [[[i for i in range(int([line.strip() for line in line.split(',')][i].split('-')[0]), int([line.strip() for line in line.split(',')][i].split('-')[-1]) + 1)] for i in range(2)] for line in data] if len(set(line[1]).difference(line[0])) == 0 or len(set(line[0]).difference(line[1])) == 0)}")

print(f"P2 New: {sum(1 for line in [[[i for i in range(int([line.strip() for line in line.split(',')][i].split('-')[0]), int([line.strip() for line in line.split(',')][i].split('-')[-1]) + 1)] for i in range(2)] for line in data] if len(set(line[1]).intersection(line[0])) or len(set(line[0]).intersection(line[1])))}")