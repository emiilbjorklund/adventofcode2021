import numpy as np


flashes = 0
itr = 0

def flash(matrix, dy, dx):
    matrix[dx][dy] +=1

    if(matrix[dx][dy] -1 == 9):
        for i in range(dy - 1, dy + 2):
            for j in range(dx -1, dx + 2):
                if (0 <= i < len(matrix) and 0 <= j < len(matrix[0]) and not (i == dy and  j == dx) ):
                    matrix = flash(matrix, i, j)
    return matrix


with open('input.txt', 'r') as f:
    matrix = [[int(num) for num in line.strip()] for line in f]


for day in range(0,100):
# Uncomment for part 2
# while(1):
    if (sum(sum(matrix,[])) == 0):
        break
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
                matrix = flash(matrix, i, j)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if(matrix[i][j] > 9):
                flashes += 1
                matrix[i][j] = 0
    itr += 1



print(np.matrix(matrix))
print (flashes) # Part 1
print(itr) # Part 2
