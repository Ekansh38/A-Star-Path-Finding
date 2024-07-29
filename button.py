import pygame
from pygame.math import Vector2


class Button:
    def __init__(self, pos, text, size, color, outline_color):
        self.pos = pos
        self.text = text
        self.size = size
        self.color = color
        self.outline_color = outline_color
        self.text_offset = Vector2(80, 20)

    def draw(self, screen):
        pygame.draw.rect(
            screen,
            self.color,
            (
                self.pos.x,
                self.pos.y,
                self.size.x,
                self.size.y,
            ),
        )

        pygame.draw.rect(
            screen,
            self.outline_color,
            (
                self.pos.x - 1,
                self.pos.y - 1,
                self.size.x + 1,
                self.size.y + 1,
            ),
            6,
        )
        font = pygame.font.Font(None, 72)
        text = font.render(self.text, True, (0, 0, 0))
        screen.blit(
            text,
            (
                self.pos.x + (self.size.x // 2) - self.text_offset.x,
                self.pos.y + (self.size.y // 2) - self.text_offset.y,
            ),
        )

    def check_click(self):
        mouse_pos = Vector2(pygame.mouse.get_pos())
        if (
            self.pos.x < mouse_pos.x < self.pos.x + self.size.x
            and self.pos.y < mouse_pos.y < self.pos.y + self.size.y
        ):
            if pygame.mouse.get_pressed()[0]:
                return True
        return False
