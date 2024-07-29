import pygame
from pygame.math import Vector2


class Cell:
    def __init__(self, pos):
        self.pos = pos
        self.color = "white"
        self.wall = False
        self.start_cell = False
        self.end_cell = False
        self.open_set = False
        self.closed_set = False
        self.path = False
        self.f_cost = 10000
        self.parent = None
        self.neighbors = []

    def set_color(self):
        if self.wall:
            self.color = "black"
        elif self.start_cell:
            self.color = (0, 140, 168)
        elif self.end_cell:
            self.color = (0, 140, 168)
        elif self.path:
            self.color = (0, 140, 168)
        elif self.closed_set:
            self.color = "green"
        elif self.open_set:
            self.color = "red"
        else:
            self.color = "white"

    def draw(self, screen, size):
        self.set_color()
        pygame.draw.rect(
            screen,
            self.color,
            (
                self.pos.x * size,
                self.pos.y * size,
                size,
                size,
            ),
        )

    def find_neighbors(self, cells):
        self.neighbors = []
        dirs = [
            Vector2(0, 1),
            Vector2(0, -1),
            Vector2(1, 0),
            Vector2(-1, 0),
            Vector2(1, 1),
            Vector2(1, -1),
            Vector2(-1, 1),
            Vector2(-1, -1),
        ]

        for cell in cells:
            for dir in dirs:
                if cell.pos == self.pos + dir:
                    self.neighbors.append(cell)
                    break
