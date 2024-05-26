import pygame
from pygame.locals import *

class Wall(pygame.sprite.Sprite):
    def __init__(self, color, left, top, width, height):
        super(Wall, self).__init__()

        self.image = pygame.Surface((width,height))
        self.image.fill(pygame.Color(color))

        self.rect = self.image.get_rect()
        self.rect.x = left
        self.rect.y = top
        pygame.draw.rect(self.image, color, pygame.Rect(left, top, width, height))
