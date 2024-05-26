import pygame
import random
from pygame.locals import *

class Enemy(pygame.sprite.Sprite):
    def __init__(self,screen_width, screen_height, wall_thickness, player_x_position, player_y_position, player_width, player_height):
        super(Enemy, self).__init__()

        self.width = 35

        spawn_coordinates = self.generate_spawn_point(screen_width, screen_height, wall_thickness, player_x_position, player_y_position, player_width, player_height)
        
        self.facing = "right"

        self.image = pygame.Surface((self.width, self.width))
        self.image.fill((0,200,0))

        self.rect = self.image.get_rect()
        self.rect.x = spawn_coordinates[0]
        self.rect.y = spawn_coordinates[1]

        self.speed = 10

    def generate_spawn_point(self, screen_width, screen_height, wall_thickness, player_x_position, player_y_position, player_width, player_height):
        
        coin_flip = random.randint(1, 2)
        if coin_flip == 1: #work for the x value
            
            x_positions = []

            r_bound = 0 + wall_thickness
            l_bound = screen_width - wall_thickness - self.width

            if player_x_position - 200 > r_bound: #if possible to find a pos1
                x_position1 = random.randrange(r_bound, player_x_position - 200)
                x_positions.append(x_position1)
            if l_bound > player_x_position + 200 + player_width:
                x_position2 = random.randrange(player_x_position + 200 + player_width, l_bound)
                x_positions.append(x_position2)

            chosen_x_position =  random.choice(x_positions)
            chosen_y_position = random.randrange(0 + wall_thickness, screen_height - wall_thickness - self.width)

            return [chosen_x_position, chosen_y_position]

        if coin_flip == 2: #work for the y value
            t_bound = 0 + wall_thickness
            b_bound = screen_height - wall_thickness - self.width

            y_positions = []

            if player_y_position - 200 > t_bound:
                y_position1 = random.randrange(t_bound, player_y_position - 200)
                y_positions.append(y_position1)

            if b_bound > player_y_position + player_height + 200:
                y_position2 = random.randrange(player_y_position + player_height + 200, b_bound)
                y_positions.append(y_position2)

            chosen_y_position =  random.choice(y_positions)
            chosen_x_position = random.randrange(0 + wall_thickness, screen_width - wall_thickness - self.width)

            return [chosen_x_position, chosen_y_position]