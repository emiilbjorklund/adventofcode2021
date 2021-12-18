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

def _(n):
    return int(''.join(map(str, n)),2)

def literal(input):
    seq = input[0:5];del input[0:5]
    if seq[0] == 0:
        return seq[1:5]
    
    return seq[1:5] + literal(input)

def solve(packet):
    print("Packet: ", packet)

    version = _(packet[0:3]);del packet[0:3]
    id = _(packet[0:3]);del packet[0:3]
    print("Version: " , version , " Id: " , id)

    if id == 4:
        print("Literal: ", _(literal(packet)))
        return version

    lengthId = _([packet[0]]);del packet[0]
    print("OP LengthId: ", lengthId)

    if lengthId == 0:
        subLength = _(packet[0:15]);del packet[0:15]
        print("Sub length: ", subLength)
        sub = packet[0:subLength];del packet[0:subLength]
        s = 0
        while(len(sub) > 0):
            s += solve(sub) 
        return s + version
    else:
        subCount = _(packet[0:11]);del packet[0:11]
        print("Sub count: ", subCount)
        s = 0
        for i in range(subCount):
            s += solve(packet) 
        return s + version
    


if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        input = []

        for line in f:
            for char in line:
                input += ct[char]

        print(solve(input))