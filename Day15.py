import networkx as nx

with open("inputs/15.txt") as f:
    grid = list(map(lambda x: list(map(int, list(x.strip()))), f.readlines()))


def find_total_risk(grid):
    x_size = len(grid[0])
    y_size = len(grid)
    G = nx.DiGraph()
    for y, row in enumerate(grid):
        for x, risk in enumerate(row):
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                other_x = x + dx
                other_y = y + dy
                if 0 <= other_x < x_size and 0 <= other_y < y_size:
                    G.add_edge((other_x, other_y), (x, y), weight=risk)
    return nx.algorithms.shortest_path_length(G, (0, 0), (x_size - 1, y_size - 1), weight="weight")


def day_one():
    return find_total_risk(grid)


def day_two():
    new_grid = []
    for dy in range(5):
        for row in grid:
            new_grid.append([])
            for dx in range(5):
                new_row = list(map(lambda x: x + dx + dy, row))
                for i in range(len(new_row)):
                    if new_row[i] > 9:
                        new_row[i] -= 9
                new_grid[-1].extend(new_row)

    return find_total_risk(new_grid)


print(day_one())
print(day_two())
