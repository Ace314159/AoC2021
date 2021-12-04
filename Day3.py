with open("inputs/3.txt") as f:
    lines = f.readlines()
    lines = list(map(lambda x: x.strip(), lines))


def part_one():
    counts = [0 for _ in range(len(lines[0]))]
    for line in lines:
        for i, char in enumerate(line):
            if char == '1':
                counts[i] += 1
            else:
                counts[i] -= 1
    gamma = ""
    for count in counts:
        if count > 0:
            gamma += '1'
        else:
            gamma += '0'
    bits = len(gamma)
    gamma = int(gamma, 2)
    epsilon = 2**bits - 1 - gamma
    return gamma * epsilon


def part_two():
    bits = len(lines[0])
    possible_oxygen = lines.copy()
    possible_co2 = lines.copy()
    for i in range(bits):
        if len(possible_oxygen) != 1:
            count = 0
            for line in possible_oxygen:
                if line[i] == '1':
                    count += 1
                else:
                    count -= 1
            if count >= 0:
                use = '1'
            else:
                use = '0'
            possible_oxygen = list(filter(lambda x: x[i] == use, possible_oxygen))
        if len(possible_co2) != 1:
            count = 0
            for line in possible_co2:
                if line[i] == '1':
                    count += 1
                else:
                    count -= 1
            if count >= 0:
                use = '0'
            else:
                use = '1'
            possible_co2 = list(filter(lambda x: x[i] == use, possible_co2))
        if len(possible_oxygen) == 1 and len(possible_co2) == 1:
            break
    
    return int(possible_oxygen[0], 2) * int(possible_co2[0], 2)


print(part_one())
print(part_two())
