import pygame
from pygame.math import Vector2

from grid import Grid

# Constants
grid = Grid(20, 35, 50)
SCREEN_SIZE = Vector2(grid.cols * grid.cell_size, grid.rows * grid.cell_size)
FPS = 60

# Basic setup
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()
running = True

# Main loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("white")

    grid.draw_grid(screen)

    pygame.display.update()
    clock.tick(FPS)
