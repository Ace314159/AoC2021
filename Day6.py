from collections import Counter

with open("inputs/6.txt") as f:
    fish = list(map(int, f.read().strip().split(",")))

NEW_FISH = 8
RESET = 6


def simulate(days):
    fish_counts = Counter(fish)
    for _ in range(days):
        new_fish_counts = Counter()
        new_fish_counts[NEW_FISH] = fish_counts[0]
        for i in range(1, NEW_FISH + 1):
            new_fish_counts[i - 1] = fish_counts[i]
        new_fish_counts[RESET] += fish_counts[0]
        fish_counts = new_fish_counts

    count = 0
    for i in range(NEW_FISH + 1):
        count += fish_counts[i]
    return count


def day_one():
    return simulate(80)


def day_two():
    return simulate(256)


print(day_one())
print(day_two())
