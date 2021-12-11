from sys import stdin

ROUND = ("(", ")")
SQUARE = ("[", "]")
CURLY = ("{", "}")
ANGLE = ("<", ">")


def run(data):
    points = 0
    chars = [list(char) for char in data]
    d_ascii = [[ord(x) for x in char] for char in chars]

    for arr in data:
        valid = filter(lambda num: num % 2 == 0, arr)
        a1 = [_a1 + 1 if _a1 == 40 else _a1 +
              2 for _a1 in valid[:len(valid)//2]]
        a2 = valid[len(valid)//2:]

        for n in range(len(a1)):
            if (a1[n] != a2[2]):
                if valid[len(valid)//2:][n] == 41:
                    points = points + 3
                elif valid[len(valid)//2:][n] == 93:
                    points = points + 57
                elif valid[len(valid)//2:][n] == 125:
                    points = points + 1197
                elif valid[len(valid)//2:][n] == 62:
                    points = points + 25137
                break

    print(points)


if __name__ == "__main__":
    data = []

    for line in stdin:
        if line == '\n':
            break
        data.append(line)

    run(data)
