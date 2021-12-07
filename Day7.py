with open("inputs/7.txt") as f:
    crabs = list(map(int, f.read().strip().split(",")))


def day_one():
    min_fuel = min(crabs)
    max_fuel = max(crabs)
    best = float("inf")
    for fuel in range(min_fuel, max_fuel + 1):
        total = sum(abs(crab - fuel) for crab in crabs)
        best = min(best, total)
    return best


def day_two():
    min_fuel = min(crabs)
    max_fuel = max(crabs)
    best = float("inf")
    for fuel in range(min_fuel, max_fuel + 1):
        total = 0
        for crab in crabs:
            num = abs(crab - fuel)
            total += num * (num + 1) // 2
        best = min(best, total)
    return best


print(day_one())
print(day_two())
