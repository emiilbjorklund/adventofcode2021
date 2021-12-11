from sys import stdin



def run(data, depth = 0, horizontal = 0, aim = 0):
    for d in data:
        command =  d.split(" ")[0]
        if command == 'forward':
            horizontal += int(d.split()[-1])
            depth += (aim * int(d.split()[-1]))
        if command == 'up': aim -= int(d.split()[-1])
        if command == 'down': aim += int(d.split()[-1])
        print(horizontal, depth, aim)
   
    print(horizontal*depth)


if __name__ == "__main__":
    data = []

    for line in stdin:
        if line == '\n':
            break
        data.append(line)

    run(data)