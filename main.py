import pygame
from pygame.math import Vector2

from button import Button
from grid import Grid

# Constants
grid = Grid(25, 50, 50)
MARGIN = 200
SCREEN_SIZE = Vector2(grid.cols * grid.cell_size, grid.rows * grid.cell_size + MARGIN)
FPS = 60

# Basic setup
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()
running = True

# Button
button_size = Vector2(200, 100)
button_pos = Vector2(
    ((grid.cols * grid.cell_size) // 2) - (button_size.x // 2),
    (grid.rows * grid.cell_size) + (MARGIN // 2) - (button_size.y // 2),
)

button = Button(
    button_pos,
    "START",
    button_size,
    "darkgreen",
    "black",
)


# Main loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("white")
    button.draw(screen)

    grid.update(screen)

    if button.check_click():
        grid.start_pathfinding()

    pygame.display.update()
    clock.tick(FPS)
