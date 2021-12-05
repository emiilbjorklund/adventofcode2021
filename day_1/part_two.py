from sys import stdin



def run(data, k = 3):
    count = 0
    for i in range(len(data) - k):
        if sum(data[i:i+k]) < sum(data[i+1: i+1+k]):
            count += 1
    print(count)


if __name__ == "__main__":
    data = []

    for line in stdin:
        if line == '\n':
            break
        data.append(int(line))

    run(data)