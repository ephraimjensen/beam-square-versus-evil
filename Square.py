import pygame
from pygame.locals import *
import math

class Square(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height):
        super(Square, self).__init__()
        
        self.width = 35
        self.color = (0, 200, 0)

        self.facing = "right"

        self.image = pygame.Surface((self.width,self.width))
        self.image.fill(self.color)

        self.rect = self.image.get_rect()
        self.rect.x = (screen_width / 2) - (self.width / 2)
        self.rect.y = (screen_height / 2) - (self.width / 2)

        self.speed = 5
        self.diagonal_speed = (self.speed / math.sqrt(2))

    def print_direction(self):
        print(self.facing)

    def change_color(self, new_color):
        self.image.fill(new_color)

    def update(self, top_collide, left_collide, right_collide, bottom_collide):
        keys = pygame.key.get_pressed()

        #moves the player
        if keys[pygame.K_w] and keys[pygame.K_a] and not top_collide and not left_collide:
            self.rect.y -= self.diagonal_speed
            self.rect.x -= self.diagonal_speed
            self.facing = "left"

        elif keys[pygame.K_w] and keys[pygame.K_d] and not top_collide and not right_collide:
            self.rect.y -= self.diagonal_speed
            self.rect.x += self.diagonal_speed
            self.facing = "right"

        elif keys[pygame.K_s] and keys[pygame.K_a] and not bottom_collide and not left_collide:
            self.rect.y += self.diagonal_speed
            self.rect.x -= self.diagonal_speed
            self.facing = "left"

        elif keys[pygame.K_s] and keys[pygame.K_d] and not bottom_collide and not right_collide:
            self.rect.y += self.diagonal_speed
            self.rect.x += self.diagonal_speed
            self.facing = "right"

        elif keys[pygame.K_w] and not top_collide:
            self.rect.y -= self.speed
            self.facing = "top"

        elif keys[pygame.K_a] and not left_collide:
            self.rect.x -= self.speed
            self.facing = "left"

        elif keys[pygame.K_s] and not bottom_collide:
            self.rect.y += self.speed
            self.facing = "bottom"

        elif keys[pygame.K_d] and not right_collide:
            self.rect.x += self.speed
            self.facing = "right"




# def __init__(self, pos):
#     walls.append(self)
#     self.rect = pygame.Rect(pos[0], pos[1], 16, 16)
#     self.image = pygame.image.load("/path/to/image_file.png")
# and then, on your game loop, instead of drawing a rect, call the blit method of the "screen" (which is a pygame.Surface object) passing the image:

# for jewel in jewels:
#     screen.blit(jewel.image, jewel.rect)