from sys import stdin



def run(data, x = 0, y = 0):
    for d in data:
        command =  d.split(" ")[0]
        if command == 'forward': x += int(d.split()[-1])
        if command == 'up': y -= int(d.split()[-1])
        if command == 'down': y += int(d.split()[-1])
   
    print(x*y)


if __name__ == "__main__":
    data = []

    for line in stdin:
        if line == '\n':
            break
        data.append(line)

    run(data)