import numpy as np

# Makes PART 2 much easier :P (only using np for displaying matrix)
np.set_printoptions(edgeitems=10,linewidth=180)

sum = 0

cords = []
folds = []

with open('input.txt') as f:
    lines = f.readlines()
    for i in range(len(lines)):
        if lines[i] == '\n':
            folds = [(x.strip().split(' ')[-1].split('=')[0], int(x.strip().split(' ')[-1].split('=')[1]))
                     for x in list(filter(lambda s: s.startswith('fold along'), lines[i + 1:]))]
            break
        else:
            cords.append(tuple(map(int, lines[i].split(','))))


grid = [[0 for col in range(max(cords, key=lambda item:item[0])[0] + 1)]
        for row in range(max(cords, key=lambda item:item[1])[1] + 1)]

for cord in cords:
    grid[cord[1]][cord[0]] = 1

for i in range(len(folds)):
# PART 1
#for i in range(1):
    if folds[i][0] == 'x':
        f1 = []
        f2 = []
        for row in grid:
            f1.append(row[:folds[i][1]])
            f2.append(row[folds[i][1] + 1:][::-1])
        for i in range(len(f1)):
            for j in range(len(f1[0])):
                f1[i][j] = f1[i][j] + f2[i][j]
        grid = f1
    elif folds[i][0] == 'y':
        f1 = grid[:folds[i][1]]
        f2 = grid[folds[i][1] + 1:][::-1]
        for i in range(len(f1)):
            for j in range(len(f1[0])):
                f1[i][j] = f1[i][j] + f2[i][j]
        grid = f1

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] > 0:
            grid[i][j] = '#'
            sum += 1
        else:
            grid[i][j] = '.'


print(np.matrix(grid))
print(sum)
