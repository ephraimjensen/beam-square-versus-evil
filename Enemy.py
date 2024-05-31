import pygame
import random
import math
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

        self.speed = 2

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
        
    def do_trig(self, character_speed, x_difference, y_difference):
        
        #sides a and b are absolute value of distance to player a is x. b is y.
        triangle_side_a = abs(x_difference)
        triangle_side_b = abs(y_difference)
        # triangle_side_c = math.sqrt(triangle_side_a**2 + triangle_side_b**2)

        triangle_angle_A = math.atan(triangle_side_a / triangle_side_b)
        triangle_angle_B = math.atan(triangle_side_b / triangle_side_a)

        # print(triangle_side_c)

        # print(triangle_angle_A)
        # print(triangle_angle_B)

        movement = character_speed

        move_triangle_side_c = movement
        #how far to move x
        move_triangle_side_a = round(move_triangle_side_c * (math.sin(triangle_angle_A)))
        #how far to move y
        move_triangle_side_b = round(move_triangle_side_c * (math.sin(triangle_angle_B)))

        return [move_triangle_side_a, move_triangle_side_b]

        
    def update(self, player_x_position, player_y_position):

        x_difference = player_x_position - self.rect.x
        y_difference = player_y_position - self.rect.y
        
        move_vector = [0,0]

        abs_x = abs(x_difference)
        abs_y = abs(y_difference)
        
        move_negative_x = False
        move_negative_y = False

        if x_difference < 0:
            move_negative_x = True
        if y_difference < 0:
            move_negative_y = True

        # if y_difference > 0 and x_difference < 0:
        #     move_negative_x = False
        #     move_negative_y = True
        
        
        if x_difference != 0 and y_difference !=0:
            move_vector = self.do_trig(self.speed, x_difference, y_difference)
        else:
            if x_difference == 0:
                move_vector = [0, 5]
            if y_difference == 0:
                move_vector = [5, 0]

        

        if move_negative_x:
            self.rect.x += (-1 * move_vector[0])
        else: 
            self.rect.x += (1 * move_vector[0])
        if move_negative_y:
            self.rect.y += (-1 * move_vector[1])
        else: 
            self.rect.y += (1 * move_vector[1])

        
        
        
        
        
