import pygame
from pygame.locals import *

class Attack(pygame.sprite.Sprite):
    def __init__(self, player_facing_direction, player_x_pos, player_y_pos, player_width):
        super(Attack, self).__init__()

        self.width = 70
        self.length = 140

        if player_facing_direction == "top" or player_facing_direction == "bottom":
            self.image = pygame.Surface((self.width,self.length))
        if player_facing_direction =="left" or player_facing_direction == "right":
            self.image = pygame.Surface((self.length,self.width))
        
        
        self.image.fill((255,0,0))

        self.rect = self.image.get_rect()

        self.direction = "right"

        if player_facing_direction == "top":
            self.direction = "top"
            self.rect.x = player_x_pos - (player_width / 2)
            self.rect.y = player_y_pos - self.length

        if player_facing_direction == "left":
            self.direction = "left"
            self.rect.x = player_x_pos - self.length
            self.rect.y = player_y_pos - (player_width / 2)

        if player_facing_direction == "right":
            self.direction = "right"
            self.rect.x = player_x_pos + player_width
            self.rect.y = player_y_pos - (player_width / 2)

        if player_facing_direction == "bottom":
            self.direction = "bottom"
            self.rect.x = player_x_pos - (player_width / 2)
            self.rect.y = player_y_pos + player_width

    def move_with_player(self, player_facing_direction, player_x_pos, player_y_pos, player_width):
        if self.direction == "top":
            self.rect.x = player_x_pos - (player_width / 2)
            self.rect.y = player_y_pos - self.length
        if self.direction == "left":
            self.rect.x = player_x_pos - self.length
            self.rect.y = player_y_pos - (player_width / 2)
        if self.direction == "right":
            self.rect.x = player_x_pos + player_width
            self.rect.y = player_y_pos - (player_width / 2)
        if self.direction == "bottom":
            self.rect.x = player_x_pos - (player_width / 2)
            self.rect.y = player_y_pos + player_width

    
