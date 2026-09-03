import argparse
import pygame
import time
from graphics import *
from solve_sudoku import solve

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("file", type=str)
    parser.add_argument("-s", "--slow_down", type=float, default=0)
    return parser.parse_args()


def load_sudoku(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()

    sudoku = []
    for line in lines:
        line = line.strip()
        if line:
            row = [int(num) for num in line.split()]
            sudoku.append(row)

    return sudoku


def prepare_window(sudoku):
    pygame.init()
    screen_info = pygame.display.Info()
    window_size = min(screen_info.current_w, screen_info.current_h) - 100
    window = pygame.display.set_mode((window_size, window_size))
    size = len(sudoku)
    width = window_size // size

    draw_board(window, sudoku, width)
    draw_numbers(window, sudoku, width, BLACK)
    display()
    return window, width


if __name__ == "__main__":
    input = parse_arguments()

    file = input.file
    sleep_time = input.slow_down
    filepath = "./dataset/" + file
    sudoku = load_sudoku(filepath)
    window, width = prepare_window(sudoku)
    time.sleep(sleep_time)

    solve(sudoku, window, width, sleep_time)
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
