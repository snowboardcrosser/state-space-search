import time
from structure import *
from graphics import *

def dfs(window, maze, start, end, width, sleep_time):
    stack = [start]
    parent = {start: None}
    expanded = 0

    while stack:
        current = stack.pop()
        if current == end:
                path_length = reconstruct_path(window, current, parent, width)
                display()
                print_metrics(start, end, expanded, path_length - 1)
                return
        
        expanded += 1
        if current != start:
            draw_rectangle(window, current[0], current[1], width, GREEN)
            display()
            time.sleep(sleep_time)

        for dx, dy in DIRECTIONS:
            neighbor = (current[0] + dx, current[1] + dy)
            if is_valid(maze, neighbor) and neighbor not in parent:
                stack.append(neighbor)
                parent[neighbor] = current
                draw_rectangle(window, neighbor[0], neighbor[1], width, YELLOW)

        display()
  
    return None
