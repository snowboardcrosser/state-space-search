from graphics import *

DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def is_valid(maze, pos):
    x, y = pos
    return 0 <= y < len(maze) and 0 <= x < len(maze[0]) and maze[y][x] == ' '

def print_metrics(start, end, expanded, path_lenght):
    print(f"Start: {start}")
    print(f"End: {end}")
    print(f"Expanded: {expanded}")
    print(f"Path length: {path_lenght}")

def reconstruct_path(window, current, parent, width):
    path_length = 0
    while current:
        path_length += 1
        draw_rectangle(window, current[0], current[1], width, BLUE)
        current = parent[current]

    return path_length
