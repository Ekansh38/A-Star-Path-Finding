import pygame
from pygame.math import Vector2

from cell import Cell


class Grid:
    def __init__(self, rows, cols, cell_size):
        self.rows = rows
        self.cols = cols
        self.cell_size = cell_size
        self.line_thickness = 3
        self.line_color = "black"
        self.start_cell = None
        self.end_cell = None
        self.cells = []
        self.start = False
        self.open_set = []
        self.closed_set = []
        self.create_cells()

    def start_pathfinding(self):
        self.start = True

    def retrace_path(self):
        path = []
        current = self.end_cell
        while current != self.start_cell:
            path.append(current)
            current = current.parent
        path.append(self.start_cell)
        for cell in path:
            cell.path = True

    def update(self, screen):
        self.draw_cells(screen)
        self.draw_grid(screen)
        if self.start and self.start_cell is not None and self.end_cell is not None:
            lowest_f_cost = 1000000
            current = self.open_set[0]
            for cell in self.open_set:
                if cell.f_cost < lowest_f_cost:
                    current = cell
                    lowest_f_cost = cell.f_cost

            self.open_set.remove(current)
            current.open_set = False
            self.closed_set.append(current)
            current.closed_set = True

            if current == self.end_cell:
                self.retrace_path()
                self.start = False
                return

            current.find_neighbors(self.cells)

            for neighbor in current.neighbors:
                if neighbor.wall or neighbor in self.closed_set:
                    continue

                start_pos = self.start_cell.pos
                g_cost = start_pos.distance_to(neighbor.pos) * 10
                h_cost = neighbor.pos.distance_to(self.end_cell.pos) * 10
                f_cost = g_cost + h_cost
                if neighbor not in self.open_set and neighbor.parent is None:
                    neighbor.parent = current
                    neighbor.f_cost = f_cost
                    if neighbor not in self.open_set:
                        neighbor.open_set = True
                        self.open_set.append(neighbor)
                elif f_cost < neighbor.f_cost:
                    neighbor.parent = current
                    neighbor.f_cost = f_cost
                    if neighbor not in self.open_set:
                        neighbor.open_set = True
                        self.open_set.append(neighbor)
        else:
            self.check_input()

    def create_cells(self):
        for x in range(0, self.cols):
            for y in range(0, self.rows):
                cell = Cell(Vector2(x, y))
                self.cells.append(cell)

    def check_input(self):
        if not self.start:
            mouse_pos = pygame.mouse.get_pos()
            mouse_pos = Vector2(
                mouse_pos[0] // self.cell_size, mouse_pos[1] // self.cell_size
            )
            for cell in self.cells:
                if cell.pos == mouse_pos:
                    if pygame.mouse.get_pressed()[0]:
                        if self.start_cell is None:
                            cell.start_cell = True
                            self.start_cell = cell
                            self.open_set.append(self.start_cell)
                        elif self.end_cell is None and cell != self.start_cell:
                            cell.end_cell = True
                            self.end_cell = cell
                        elif cell != self.start_cell and cell != self.end_cell:
                            cell.wall = True

                    elif pygame.mouse.get_pressed()[2]:
                        if cell == self.start_cell:
                            self.start_cell = None
                            cell.start_cell = False
                        elif cell == self.end_cell:
                            self.end_cell = None
                            cell.end_cell = False
                        else:
                            cell.wall = False

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

    def draw_cells(self, screen):
        for cell in self.cells:
            cell.draw(screen, self.cell_size)
