


def solve(matrix):
    (M, N) = (len(matrix), len(matrix[0]))

    T = [[0 for x in range(N)] for y in range(M)]

    for i in range(M):
        for j in range(N):
            T[i][j] = matrix[i][j]

            if i == 0 and j > 0:
                T[0][j] += T[0][j - 1]
 
            elif j == 0 and i > 0:
                T[i][0] += T[i - 1][0]
 
            elif i > 0 and j > 0:
                T[i][j] += min(T[i - 1][j], T[i][j - 1])

    return T[M - 1][N - 1] - 1


if __name__ == "__main__":
    with open('sample.txt', 'r') as f:
        matrix = [[int(num) for num in line.strip()] for line in f]

        print(solve(matrix))
