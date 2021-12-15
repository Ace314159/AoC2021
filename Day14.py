from collections import Counter

with open("inputs/14.txt") as f:
    start, rulesStr = f.read().split("\n\n")
rules = {}
for line in rulesStr.splitlines():
    rule, char = line.split(" -> ")
    rules[rule] = char


def simulate(num):
    types = Counter()
    polymer = start
    for i in range(len(polymer) - 1):
        t = polymer[i] + polymer[i + 1]
        types[t] += 1
    for _ in range(num):
        new_types = Counter()
        for t, count in types.items():
            if t in rules:
                char = rules[t]
                new_types[t[0] + char] += count
                new_types[char + t[1]] += count
            else:
                new_types[t] += count
        types = new_types
    counts = Counter()
    for t, count in new_types.items():
        counts[t[0]] += count
        counts[t[1]] += count
    most = counts.most_common()
    return (most[0][1] - most[-1][1] + 1) // 2


def day_one():
    return simulate(10)


def day_two():
    return simulate(40)


print(day_one())
print(day_two())
