import pprint

sudoku = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]


# check if a particular can fit in a row


def check_row(n, x):
    for i in range(9):
        if sudoku[x][i] == n:
            return False
    return True


def check_column(n, y):
    for i in range(9):
        if sudoku[i][y] == n:
            return False
    return True


def check_box(n, x, y):
    box_edge_x = (x // 3) * 3
    box_edge_y = (y // 3) * 3
    for i in range(3):
        for j in range(3):
            if sudoku[i + box_edge_x][j + box_edge_y] == n:
                return False
    return True


def check_if_possible(n, x, y):
    if check_column(n, y) and check_row(n, x) and check_box(n, x, y):
        return True
    return False


def solve_sudoku():
    for x in range(9):
        for y in range(9):
            item = sudoku[x][y]
            if item == 0:
                for n in range(1, 10):
                    if check_if_possible(n, x, y):
                        sudoku[x][y] = n
                        solve_sudoku()
                        sudoku[x][y] = 0
                return
    print(pprint.pprint(sudoku))
    input('More?')

solve_sudoku()
