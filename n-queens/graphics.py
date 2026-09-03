import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

def draw_rectangle(window, left, top, width, color):
    border_thickness = 1
    pygame.draw.rect(window, BLACK, (left * width, top * width, width, width))
    pygame.draw.rect(window, color, (left * width + border_thickness, top * width + border_thickness, 
                                     width - 2 * border_thickness, width - 2 * border_thickness))
    
def draw_board(window, n, width):
    for row in range(n):
        for column in range(n):
            draw_rectangle(window, column, row, width, WHITE)

def draw_queen(window, row, col, width, color=BLACK):
    center_x = col * width + width // 2
    center_y = row * width + width // 2
    pygame.draw.circle(window, color, (center_x, center_y), width // 3)
    pygame.display.update()

def draw_board_with_queens(window, board, width):
    for col in range(len(board)):
        draw_queen(window, board[col], col, width)

def draw_result(window, board, width):
    for column in board:
        draw_queen(window, board[column], column, width, BLUE)
    
def display():
    pygame.display.update()
