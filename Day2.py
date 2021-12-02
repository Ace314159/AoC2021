with open("inputs/2.txt") as f:
    lines = f.readlines()
    lines = list(map(lambda x: x.strip(), lines))


def part_one():
    pos = 0
    depth = 0
    for command in lines:
        dir, dist = command.split(" ")
        dist = int(dist)
        if dir == "forward":
            pos += dist
        elif dir == "down":
            depth += dist
        elif dir == "up":
            depth -= dist

    return pos * depth


def part_two():
    aim = 0
    pos = 0
    depth = 0
    for command in lines:
        dir, dist = command.split(" ")
        dist = int(dist)
        if dir == "forward":
            pos += dist
            depth += aim * dist
        elif dir == "down":
            aim += dist
        elif dir == "up":
            aim -= dist

    return pos * depth


print(part_one())
print(part_two())
