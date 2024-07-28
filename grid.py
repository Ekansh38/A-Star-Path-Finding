import pygame
from pygame.math import Vector2


class Grid:
    def __init__(self, rows, cols, cell_size):
        self.rows = rows
        self.cols = cols
        self.cell_size = cell_size
        self.line_thickness = 3
        self.line_color = "black"

    def draw_grid(self, screen):
        for x in range(0, self.cols + 1):
            pygame.draw.line(
                screen,
                self.line_color,
                (x * self.cell_size, 0),
                (x * self.cell_size, self.rows * self.cell_size),
                self.line_thickness,
            )
            for y in range(0, self.rows + 1):
                pygame.draw.line(
                    screen,
                    self.line_color,
                    (0, y * self.cell_size),
                    (self.cols * self.cell_size, y * self.cell_size),
                    self.line_thickness,
                )
