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
    

def draw_board(window, sudoku, width):
    size = len(sudoku)
    for row in range(size):
        for column in range(size):
            draw_rectangle(window, column, row, width, WHITE)
    draw_grid_lines(window, size, width)


def draw_numbers(window, sudoku, width, color):
    pygame.font.init()
    font = pygame.font.SysFont('Arial', width // 2)
    for row in range(len(sudoku)):
        for col in range(len(sudoku[row])):
            number = sudoku[row][col]
            if number != 0:
                text = font.render(str(number), True, color)
                text_rect = text.get_rect(center=(col * width + width // 2, row * width + width // 2))
                window.blit(text, text_rect)


def draw_one_number(window, number, row, col, width, color):
    clear_rectangle(window, col, row, width)
    pygame.font.init()
    font = pygame.font.SysFont('Arial', width // 2)
    if number != 0:
        text = font.render(str(number), True, color)
        text_rect = text.get_rect(center=(col * width + width // 2, row * width + width // 2))
        window.blit(text, text_rect)


def draw_grid_lines(window, n, width):
    block_size = int(n ** 0.5)
    for i in range(n + 1):
        line_width = 1
        if i % block_size == 0:
            line_width = 5
        pygame.draw.line(window, BLACK, (i * width, 0), (i * width, n * width), line_width)
        pygame.draw.line(window, BLACK, (0, i * width), (n * width, i * width), line_width)
    

def clear_rectangle(window, col, row, width):
    pygame.draw.rect(window, WHITE,(col * width + 5, row * width + 5, width - 2 * 5, width - 2 * 5))


def display():
    pygame.display.update()
