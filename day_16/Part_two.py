ct = {
    '0': [0,0,0,0],
    '1': [0,0,0,1],
    '2': [0,0,1,0],
    '3': [0,0,1,1],
    '4': [0,1,0,0],
    '5': [0,1,0,1],
    '6': [0,1,1,0],
    '7': [0,1,1,1],
    '8': [1,0,0,0],
    '9': [1,0,0,1],
    'A': [1,0,1,0],
    'B': [1,0,1,1],
    'C': [1,1,0,0],
    'D': [1,1,0,1],
    'E': [1,1,1,0],
    'F': [1,1,1,1]
}

op = {
    0: lambda x, y: x + y if x != -1 else y,
    1: lambda x, y: x * y if x != -1 else  1 * y,
    2: lambda x, y: x if x < y and x != -1 else y,
    3: lambda x, y: x if x > y and x != -1 else y,
    5: lambda x, y: int(x > y) if x != -1 else y,
    6: lambda x, y: int(x < y) if x != -1 else y,
    7: lambda x, y: int(x == y) if x != -1 else y,
}

convert = lambda x: int(''.join(map(str, x)),2)

def literal(input):
    seq = input[0:5];del input[0:5]
    if seq[0] == 0:
        return seq[1:5]
    
    return seq[1:5] + literal(input)

def solve(packet):
    ver = convert(packet[0:3]);del packet[0:3]
    id = convert(packet[0:3]);del packet[0:3]

    #Base case
    if id == 4:
        return convert(literal(packet))

    #Operator length
    length = convert([packet[0]]);del packet[0]

    if length == 0:
        sub_length = convert(packet[0:15]);del packet[0:15]
        sub_packet = packet[0:sub_length];del packet[0:sub_length]
        res = -1
        while(len(sub_packet) > 0):
            res = op[id](res, solve(sub_packet))
        return res
    else:
        sub_count = convert(packet[0:11]);del packet[0:11]
        res = -1
        for i in range(sub_count):
             res = op[id](res, solve(packet))
        return res
    

if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        input = []
        for line in f:
            for char in line:
                input += ct[char]

        print(solve(input))
