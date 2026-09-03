import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)

def draw_rectangle(window, left, top, width, color):
    border_thickness = 1
    pygame.draw.rect(window, BLACK, (left * width, top * width, width, width))
    pygame.draw.rect(window, color, (left * width + border_thickness, top * width + border_thickness, 
                                     width - 2 * border_thickness, width - 2 * border_thickness))
    
def draw_init(window, maze, width, start, end):
    for row in range(len(maze)):
        for column in range(len(maze[row])):
            if maze[row][column] == 'X':
                draw_rectangle(window, column, row, width, BLACK)
            elif (column,row) == start:
                draw_rectangle(window, column, row, width, RED)
            elif (column,row) == end:
                draw_rectangle(window, column, row, width, BLUE)
            else:
               draw_rectangle(window, column, row, width, WHITE)
    
def display():
    pygame.display.update()
