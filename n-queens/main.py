
import pygame
import time
import argparse
from graphics import *
from n_queens_problem import n_queens_problem

def prepare_window(n):
    pygame.init()
    screen_info = pygame.display.Info()
    window_size = min(screen_info.current_w, screen_info.current_h) - 100
    window = pygame.display.set_mode((window_size, window_size))
    width = window_size // n

    draw_board(window, n, width)
    display()
    time.sleep(1)
    return window, width

def get_board_size():
    parser = argparse.ArgumentParser()
    parser.add_argument("number_n", type=int)
    parser.add_argument("max_number_of_iterations", type=int)
    parser.add_argument("-s", "--slow_down", type=float, default=0)
    return parser.parse_args()

if __name__ == "__main__":
    input = get_board_size()
    n = input.number_n
    number_iterations = input.max_number_of_iterations
    sleep_time = input.slow_down

    window, width = prepare_window(n)
    n_queens_problem(window, n, width, number_iterations, sleep_time)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()
