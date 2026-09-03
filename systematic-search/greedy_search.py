import heapq
import time
import math
from structure import *
from graphics import *

def greedy_search(window, maze, start, end, width, sleep_time=0.02):
    priority_queue = [(heuristic(start, end), start)]
    parent = {start: None}
    expanded = 0

    while priority_queue:
        _, current = heapq.heappop(priority_queue)
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
                parent[neighbor] = current
                heapq.heappush(priority_queue, (heuristic(neighbor, end), neighbor))
                draw_rectangle(window, neighbor[0], neighbor[1], width, YELLOW)

        display()
  
    return None

def heuristic(pos, end):
    return abs(pos[0] - end[0]) + abs(pos[1] - end[1]) #Manhattan
    return math.sqrt((pos[0] - end[0])**2 + (pos[1] - end[1])**2) #Euclidean
