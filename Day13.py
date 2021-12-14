with open("inputs/13.txt") as f:
    points, folds = f.read().split("\n\n")
points = list(map(lambda x: list(map(int, x.split(","))), points.splitlines()))
folds = list(map(lambda x: x.split(" ")[-1].split("="), folds.strip().splitlines()))

x_size, y_size = 0, 0
for x, y in points:
    x_size = max(x_size, x)
    y_size = max(y_size, y)
x_size += 1
y_size += 1

original_grid = []
for y in range(y_size):
    original_grid.append([0] * x_size)
for x, y in points:
    original_grid[y][x] = 1


def fold(grid, cmd):
    dir, coord = cmd
    coord = int(coord)
    new_grid = []
    if dir == "x":
        for line in grid:
            new_grid.append([])
            x_size = len(line)
            for x in range(coord):
                diff = coord - x
                x2 = coord + diff
                if x2 >= x_size:
                    new_grid[-1].append(line[x])
                else:
                    new_grid[-1].append(line[x] | line[x2])
    else:
        y_size = len(grid)
        x_size = len(grid[0])
        for y in range(coord):
            new_grid.append([])
            diff = coord - y
            for x in range(x_size):
                y2 = coord + diff
                if y2 >= y_size:
                    new_grid[-1].append(grid[y][x])
                else:
                    new_grid[-1].append(grid[y][x] | grid[y2][x])
    return new_grid


def day_one():
    new_grid = fold(original_grid, folds[0])
    ans = 0
    for line in new_grid:
        ans += sum(line)
    return ans


def day_two():
    grid = original_grid
    for cmd in folds:
        grid = fold(grid, cmd)
    for line in grid:
        str_line = map(lambda x: "#" if x == 1 else ".", line)
        print("".join(str_line))


print(day_one())
print(day_two())
