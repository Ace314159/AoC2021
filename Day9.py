import math

with open("inputs/9.txt") as f:
    grid = list(map(lambda x: list(map(int, list(x.strip()))), f.readlines()))

low_points = []


def day_one():
    risk = 0
    for y in range(0, len(grid)):
        for x in range(0, len(grid[y])):
            low = True
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                check_x = x + dx
                check_y = y + dy
                inside = 0 <= check_x < len(grid[y]) and 0 <= check_y < len(grid)
                if inside and grid[check_y][check_x] <= grid[y][x]:
                    low = False
                    break
            if low:
                low_points.append((x, y))
                risk += grid[y][x] + 1
    return risk


def day_two():
    def grow(pos, checked):
        x = pos[0]
        y = pos[1]

        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            check_x = x + dx
            check_y = y + dy
            if 0 <= check_x < len(grid[y]) and 0 <= check_y < len(grid):
                check = grid[check_y][check_x]
                if check != 9 and check >= grid[y][x] and (check_x, check_y) not in checked:
                    checked.add((check_x, check_y))
                    grow((check_x, check_y), checked)

    basin_sizes = []
    for pos in low_points:
        checked = {pos}
        grow(pos, checked)
        basin_sizes.append(len(checked))
    basin_sizes.sort()
    return math.prod(basin_sizes[-3:])


print(day_one())
print(day_two())
