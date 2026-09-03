import time
from graphics import BLUE, RED, clear_rectangle, display, draw_one_number

def is_valid(board, row, col, num):
    n = len(board)
    block = int(n ** 0.5)
    for i in range(n):
        if board[row][i] == num or board[i][col] == num:
            return False

    start_row, start_col = (row // block) * block, (col // block) * block
    for i in range(block):
        for j in range(block):
            if board[start_row + i][start_col + j] == num:
                return False

    return True


def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                return i, j
    return None


def solve(board, window, width, sleep_time):
    empty = find_empty(board)
    if not empty:
        return True

    row, col = empty
    for num in range(1, len(board) + 1):
        if is_valid(board, row, col, num):
            board[row][col] = num
            draw_one_number(window, num, row, col, width, BLUE)
            display()
            time.sleep(sleep_time)

            if solve(board, window, width, sleep_time):
                return True

            board[row][col] = 0
            draw_one_number(window, num, row, col, width, RED)
            display()
            time.sleep(sleep_time)
            clear_rectangle(window, col, row, width)
            display()

    return False
