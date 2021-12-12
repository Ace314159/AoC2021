from collections import defaultdict

with open("inputs/12.txt") as f:
    lines = list(map(lambda x: x.strip().split("-"), f.readlines()))

edges = defaultdict(set)
for a, b in lines:
    edges[a].add(b)
    edges[b].add(a)


def part_one():
    def explore(cave, visited):
        if cave in visited:
            return 0
        if cave == "end":
            return 1
        if cave.islower():
            visited.add(cave)
        count = 0
        for child in edges[cave]:
            count += explore(child, visited)
        if cave.islower():
            visited.remove(cave)
        return count

    visited = set()
    return explore("start", visited)


def part_two():
    def explore(cave, visited):
        if cave == "end":
            return 1
        if visited[cave] == 2:
            return 0
        if visited[cave] == 1:
            if cave == "start":
                return 0
            for count in visited.values():
                if count == 2:
                    return 0
        if cave.islower():
            visited[cave] += 1
        count = 0
        for child in edges[cave]:
            count += explore(child, visited)
        if cave.islower():
            visited[cave] -= 1
        return count

    visited = defaultdict(int)
    return explore("start", visited)


print(part_one())
print(part_two())
