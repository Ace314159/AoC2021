import math

with open("inputs/17.txt") as f:
    x_range, y_range = f.read().strip().split(": ")[-1].split(", ")
x_range = list(map(int, x_range[2:].split("..")))
y_range = list(map(int, y_range[2:].split("..")))


def part_one():
    max_height = 0
    for y in range(y_range[0], y_range[1] + 1):
        t = 1
        y_max_height = 0
        while True:
            v = (y + 0.5 * t ** 2) / t
            calc_y = lambda t: -0.5 * t ** 2 + v * t
            # v is also the t for which the height is maximized
            if v.is_integer():
                cur_max_height = calc_y(v)
            else:
                cur_max_height = calc_y(int(v))
                cur_max_height = max(cur_max_height, calc_y(int(v) + 1))
            if cur_max_height > y_max_height:
                y_max_height = cur_max_height
            else:
                break
        max_height = max(max_height, y_max_height)
    return int(max_height)


def part_two():
    ans = 0
    dx_start = min(0, x_range[0])
    dx_end = max(1, x_range[1] + 1)
    dy_start = min(0, y_range[0])
    dy_end = 500
    for original_dx in range(dx_start, dx_end):
        for original_dy in range(dy_start, dy_end):
            dx, dy = original_dx, original_dy
            x, y = 0, 0
            while True:
                x += dx
                y += dy
                x_in_range = x_range[0] <= x <= x_range[1]
                y_in_range = y_range[0] <= y <= y_range[1]
                if x_in_range and y_in_range:
                    ans += 1
                    break
                if dx > 0:
                    dx -= 1
                elif dx < 0:
                    dx += 1
                dy -= 1

                y_bad = dy < 0 and y < y_range[0]
                x_bad = (dx < 0 and dx < x_range[0]) or (dx > 0 and dx > x_range[1]) or (dx == 0 and not x_in_range)
                if x_bad or y_bad:
                    break
    return ans


print(part_one())
print(part_two())
