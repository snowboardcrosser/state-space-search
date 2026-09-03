import pygame
import time
import argparse
from bfs import bfs
from dfs import dfs
from random_search import random_search
from greedy_search import greedy_search
from a_star import a_star
from graphics import *

def load_maze(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()

    maze = []
    start = None
    end = None

    for line in lines:
        line = line.strip()
        if line.startswith("start"):
            start = tuple(map(int, line[6:].split(',')))
        elif line.startswith("end"):
            end = tuple(map(int, line[4:].split(',')))
        else:
            maze.append(list(line))

    return maze, start, end

def parse_algorithms():
    parser = argparse.ArgumentParser()
    parser.add_argument("algorithm", type=str)
    parser.add_argument("file", type=str)
    parser.add_argument("-s", "--slow_down", type=float, default=0)
    return parser.parse_args()

def prepare_window(maze, start, end):
    pygame.init()
    screen_info = pygame.display.Info()
    window_size = min(screen_info.current_w, screen_info.current_h) - 100
    window = pygame.display.set_mode((window_size, window_size))
    width = window_size // max(len(maze), len(maze[0]))

    draw_init(window, maze, width, start, end)
    display()
    time.sleep(1)
    return window, width

if __name__ == "__main__":
    input = parse_algorithms()

    file = input.file
    filepath = "./dataset/" + file
    (maze, start, end) = load_maze(filepath)

    sleep_time = input.slow_down

    if(input.algorithm == "bfs"):
        window, width = prepare_window(maze, start, end)
        bfs(window, maze, start, end, width, sleep_time)
    elif(input.algorithm == "dfs"):
        window, width = prepare_window(maze, start, end)
        dfs(window, maze, start, end, width, sleep_time)
    elif(input.algorithm == "random_search"):
        window, width = prepare_window(maze, start, end)
        random_search(window, maze, start, end, width, sleep_time)
    elif(input.algorithm == "greedy_search"):
        window, width = prepare_window(maze, start, end)
        greedy_search(window, maze, start, end, width, sleep_time)
    elif(input.algorithm == "a_star"):
        window, width = prepare_window(maze, start, end)
        a_star(window, maze, start, end, width, sleep_time)
    else:
        print("Unsupported algorithm.")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()
    