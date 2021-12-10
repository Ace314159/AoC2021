from collections import deque

with open("inputs/10.txt") as f:
    lines = list(map(lambda x: x.strip(), f.readlines()))

closing = {
    ")": "(",
    "]": "[",
    "}": "{",
    ">": "<",
}

incomplete = []


def part_one():
    points = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137,
    }

    ans = 0
    for line in lines:
        searched = deque()
        is_incomplete = True
        for char in line:
            if char in closing:
                if searched.pop() != closing[char]:
                    ans += points[char]
                    is_incomplete = False
                    break
            else:
                searched.append(char)
        if is_incomplete:
            incomplete.append(line)
    return ans


def part_two():
    points = {
        "(": 1,
        "[": 2,
        "{": 3,
        "<": 4,
    }

    scores = []
    for line in incomplete:
        searched = deque()
        for char in line:
            if char in closing:
                searched.pop()
            else:
                searched.append(char)
        score = 0
        for char in reversed(searched):
            score = score * 5 + points[char]
        scores.append(score)
    scores.sort()
    return scores[len(scores) // 2]


print(part_one())
print(part_two())
