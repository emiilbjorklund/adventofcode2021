

chars = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
}
points_part_one = {
    ')': 3,
    ']': 57,
    '}':1197,
    '>': 25137
}

points_part_two = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

def part_one(row, stack):
    for char in row:
        if char in chars:
            stack.append(chars.get(char))
        else:
            element = stack.pop()
            if char != element:
                return points_part_one.get(char)
    return 0

def part_two(row, stack):
    points = 0
    for char in row:
        if char in chars:
            stack.append(chars.get(char))
        elif len(stack) > 0:
            element = stack.pop()
            if char != element: 
                return 
    stack.reverse()
    for reminder in stack:
        points = points * 5
        points = points + points_part_two.get(reminder)
    return points

with open('input.txt', 'r') as f:
    matrix = [[char for char in line.strip()] for line in f]

sum = 0
for row in matrix:
   sum = sum + part_one(row, [])

incomplete = []
for row in matrix:
    incomplete.append(part_two(row, []))

incomplete = list(filter(None, incomplete))
incomplete.sort()

print(sum)
print(incomplete[int((len(incomplete) - 1)/2)])
