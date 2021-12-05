with open("inputs/5.txt") as f:
    lines = list(map(lambda x: x.strip().split(" -> "), f.readlines()))
    lines = list(map(lambda x: [tuple(map(int, x[0].split(","))), tuple(map(int, x[1].split(",")))], lines))


def make_grid(lines):
    max_x = 0
    max_y = 0
    for line in lines:
        if line[0][0] > line[1][0]:
            line[0], line[1] = line[1], line[0]
        elif line[0][1] > line[1][1]:
            line[0], line[1] = line[1], line[0]
        max_x = max(max_x, line[0][0], line[1][0])
        max_y = max(max_y, line[0][1], line[1][1])
    max_x += 1
    max_y += 1
    grid = []
    for _ in range(max_y):
        grid.append([0 for _ in range(max_x)])
    return grid


def part_one():
    filtered = list(filter(lambda x: x[0][0] == x[1][0] or x[0][1] == x[1][1], lines))
    grid = make_grid(filtered)
    for line in filtered:
        for x in range(line[0][0], line[1][0] + 1):
            for y in range(line[0][1], line[1][1] + 1):
                grid[y][x] += 1
    count = 0
    for row in grid:
        count += sum(val >= 2 for val in row)
    return count


def part_two():
    grid = make_grid(lines)
    for line in lines:
        x = line[0][0]
        y = line[0][1]
        x_diff = line[1][0] - line[0][0]
        y_diff = line[1][1] - line[0][1]
        dx = (x_diff > 0) - (x_diff < 0)
        dy = (y_diff > 0) - (y_diff < 0)
        while x != line[1][0] or y != line[1][1]:
            grid[y][x] += 1
            x += dx
            y += dy
        grid[y][x] += 1
    count = 0
    for row in grid:
        count += sum(val >= 2 for val in row)
    return count


print(part_one())
print(part_two())
