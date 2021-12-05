with open("inputs/4.txt") as f:
    lines = f.read().split("\n\n")

numbers = list(map(int, lines[0].split(",")))
boards = lines[1:]
for i in range(len(boards)):
    boards[i] = boards[i].strip().split("\n")
    for j in range(len(boards[i])):
        boards[i][j] = list(map(int, boards[i][j].strip().replace("  ", " ").split(" ")))

BOARD_SIZE = len(boards[0][0])


def part_one():
    for num in numbers:
        for board in boards:
            for i, row in enumerate(board):
                for j, board_num in enumerate(row):
                    if board_num == num:
                        board[i][j] = None
                        if all(val is None for val in row) or all(board[i][j] is None for i in range(BOARD_SIZE)):
                            s = 0
                            for row in board:
                                for col in row:
                                    if col is not None:
                                        s += col
                            return num * s


def part_two():
    left = set(range(len(boards)))
    for num in numbers:
        for board_i, board in enumerate(boards):
            for i, row in enumerate(board):
                for j, board_num in enumerate(row):
                    if board_num == num:
                        board[i][j] = None
                        if all(val is None for val in row) or all(board[i][j] is None for i in range(BOARD_SIZE)):
                            if board_i in left:
                                left.remove(board_i)
                            if len(left) == 0:
                                s = 0
                                for row in boards[board_i]:
                                    for col in row:
                                        if col is not None:
                                            s += col
                                return num * s


print(part_one())
print(part_two())
