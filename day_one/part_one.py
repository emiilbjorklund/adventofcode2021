from sys import stdin



def run(data):
    count = 0
    for i in range(len(data)):
        if data[i-1] < data[i]:
            count += 1
    print(count)


if __name__ == "__main__":
    data = []

    for line in stdin:
        if line == '\n':
            break
        data.append(int(line))

    run(data)