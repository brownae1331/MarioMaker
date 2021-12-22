import pygame
from settings import *


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill(GREY)
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, xShift):
        self.rect.x += xShift
