import itertools

with open("inputs/11.txt") as f:
    original_lines = list(map(lambda x: list(map(int, list(x.strip()))), f.readlines()))


def flash(x, y, lines, flashed):
    if (x, y) in flashed or lines[y][x] <= 9:
        return 0
    flashed.add((x, y))
    count = 1
    for dx, dy in itertools.product(range(-1, 1 + 1), range(-1, 1 + 1)):
        new_x = x + dx
        new_y = y + dy
        if 0 <= new_y < len(lines) and 0 <= new_x < len(lines[y]):
            lines[new_y][new_x] += 1
            count += flash(new_x, new_y, lines, flashed)
    return count


def step(lines):
    count = 0
    for line in lines:
        for x in range(len(line)):
            line[x] += 1
    flashed = set()
    for y, line in enumerate(lines):
        for x, value in enumerate(line):
            if value > 9:
                count += flash(x, y, lines, flashed)
    for x, y in flashed:
        lines[y][x] = 0
    return count


def part_one():
    lines = [line.copy() for line in original_lines]
    ans = 0
    for _ in range(100):
        ans += step(lines)
    return ans


def part_two():
    lines = [line.copy() for line in original_lines]
    size = len(lines) * len(lines[0])
    i = 0
    while True:
        i += 1
        if step(lines) == size:
            return i


print(part_one())
print(part_two())
