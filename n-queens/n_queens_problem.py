import random
import time
from graphics import *


def random_initial_queens(n):
    board = list(range(n))
    random.shuffle(board)
    return board


def get_number_of_threatened_queens(queen, board):
    number = 0
    for attacker in range(len(board)):
        if queen == attacker:
            continue
        if board[queen] == board[attacker] or abs(board[queen] - board[attacker]) == abs(queen - attacker):
            number += 1

    return number


def overall_thread(board):
    number_of_threatened_queens = 0
    for queen in range(len(board)):
        number_of_threatened_queens += get_number_of_threatened_queens(queen, board)
    return number_of_threatened_queens


def move_queen(window, board, width, number_of_threatened_queens, sleep_time = 0):
    random_number = random.randrange(0, len(board))
    previous_row = board[random_number]
    board[random_number] = random.randrange(0, len(board))
    if previous_row == board[random_number]:
        return number_of_threatened_queens

    new_number_of_threatened_queens = 0
    for queen in range(len(board)):
        new_number_of_threatened_queens += get_number_of_threatened_queens(queen, board)

    if number_of_threatened_queens >= new_number_of_threatened_queens:
        number_of_threatened_queens = new_number_of_threatened_queens
        draw_queen(window, previous_row, random_number, width, GREEN)
        display()
        time.sleep(sleep_time)
        draw_queen(window, board[random_number], random_number, width)
        draw_rectangle(window, random_number, previous_row, width, WHITE)
        display()
        time.sleep(sleep_time)
    else:
        board[random_number] = previous_row
    
    return number_of_threatened_queens
    

def n_queens_problem(window, n, width, max_number_of_iterations, sleep_time = 0):
    board = random_initial_queens(n)
    draw_board_with_queens(window, board, width)
    number_of_threatened_queens = overall_thread(board)

    iterations = 0
    iterations_until_reset = max_number_of_iterations / 10
    while number_of_threatened_queens != 0 and iterations < max_number_of_iterations:
        number_of_threatened_queens = move_queen(window, board, width, number_of_threatened_queens, sleep_time)
        iterations += 1
        iterations_until_reset -=1
        if iterations_until_reset <= 0:
            board = random_initial_queens(n)
            draw_board(window, n, width)
            draw_board_with_queens(window, board, width)
            iterations_until_reset = max_number_of_iterations / 10
            number_of_threatened_queens = overall_thread(board)

    if iterations < max_number_of_iterations:
        draw_result(window, board, width)

    print(f"Number of iterations: {iterations}")
    