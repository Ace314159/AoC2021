with open("inputs/1.txt") as f:
    lines = f.readlines()
    lines = list(map(lambda x: int(x.strip()), lines))


def part_one():
    count = 0
    prev = lines[0]
    for num in lines[1:]:
        if num > prev:
            count += 1
        prev = num

    return count


def part_two():
    count = 0
    prev_i = 0
    for num in lines[3:]:
        if num > lines[prev_i]:
            count += 1
        prev_i += 1

    return count


print(part_one())
print(part_two())
