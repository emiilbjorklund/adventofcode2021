

def solve(itr, polymer: dict, rules: dict, sum):
    for i in range(itr):
        temp = {}
        for pair in polymer:
            if polymer[pair] > 0:
                insert = rules[pair]
                if insert in sum:
                    sum[insert] = sum[insert] - polymer[pair]
                else:
                    sum[insert] = 0 - polymer[pair]

                print(pair[0] + insert)
                if pair[0] + insert in temp:
                    temp[pair[0] + insert] = temp[pair[0] +
                                                  insert] + polymer[pair]
                else:
                    temp[pair[0] + insert] = polymer[pair]
                print(insert + pair[1])
                if insert + pair[1] in temp:
                    temp[insert + pair[1]] = temp[insert +
                                                  pair[1]] + polymer[pair]
                else:
                    temp[insert + pair[1]] = polymer[pair]
                polymer[pair] = 0

        for new in temp:
            polymer[new] = temp[new]
    for p in polymer:
        if p[0] not in sum:
            sum[p[0]] = polymer[p]
        else:
            sum[p[0]] = sum[p[0]] + polymer[p]
        if p[1] not in sum:
            sum[p[1]] = polymer[p]
        else:
            sum[p[1]] = sum[p[1]] + polymer[p]
            
    # print(sum)
    return sum


if __name__ == "__main__":
    sum = {}
    polymer = {}
    rules = {}

    with open('input.txt') as f:
        lines = f.readlines()
        raw_polymer = lines.pop(0)
        for i in range(len(raw_polymer) - 2):
            polymer[raw_polymer[i:i+2]] = 1
            # if raw_polymer[i+2] in sum:
            #     sum[raw_polymer[i+2]] = sum[raw_polymer[i+2]] - 1
            # else:
            #     sum[raw_polymer[i+2]] = -1

        lines.pop(0)

        for line in lines:
            rule = line.split(' ')
            rules[rule[0].strip()] = rule[2].strip()

        # print(polymer.values)
        result = solve(10, polymer, rules, sum)

        print(max(result.values()) - min(result.values()))
        # print(rules)

