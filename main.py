import pygame
from pygame.locals import *
import time
from Square import *
from Wall import *
from Attack import *
from Enemy import *

# init pygame, window, square1
pygame.init()

screen_width = 1200
screen_height = 600
window = pygame.display.set_mode((screen_width, screen_height))

player_character = Square(screen_width, screen_height)

wall_thickness = 35
left_wall = Wall((128, 128, 128), 0, 0, wall_thickness, screen_height)
top_wall = Wall((128, 128, 128), 0, 0, screen_width, wall_thickness)
right_wall = Wall((128, 128, 128), screen_width - wall_thickness, 0, wall_thickness, screen_height)
bottom_wall = Wall((128, 128, 128), 0, screen_height - wall_thickness, screen_width, wall_thickness)

# Create a sprite group
all_sprites = pygame.sprite.Group()
all_sprites.add(player_character)
all_sprites.add(left_wall)
all_sprites.add(top_wall)
all_sprites.add(right_wall)
all_sprites.add(bottom_wall)

enemies = pygame.sprite.Group()


#debugging mask control
no_spawn_enemy_mask_on = False
bool_to_only_do_this_once = True

#define start time -- could make bool with if statement later
spawn_time = time.time()
spawn_interval = 2

#define background color -- remove this later
background_color = (0,0,0)

#define bool to help with attack cooldown
is_first_attack = True
attack_ready = True
attack_duration = 2
attack_cooldown = 1

#define exit bool
exit = False
you_died = False

while not exit:
    
    left_collide = False
    top_collide = False
    right_collide = False
    bottom_collide = False

    if player_character.rect.colliderect(left_wall.rect):
        left_collide = True
    if player_character.rect.colliderect(top_wall.rect):
        top_collide = True
    if player_character.rect.colliderect(right_wall.rect):
        right_collide = True
    if player_character.rect.colliderect(bottom_wall.rect):
        bottom_collide = True

   

    #handles quitting
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True


    keys = pygame.key.get_pressed()

    #moves the player
    if keys[pygame.K_w] and not top_collide:
        player_character.rect.y -= player_character.speed
        player_character.facing = "top"
        if keys[pygame.K_a]:
            player_character.facing = "left"
        if keys[pygame.K_d]:
            player_character.facing = "right"

    if keys[pygame.K_a] and not left_collide:
        player_character.rect.x -= player_character.speed
        player_character.facing = "left"

    if keys[pygame.K_s] and not bottom_collide:
        player_character.rect.y += player_character.speed
        player_character.facing = "bottom"
        if keys[pygame.K_a]:
            player_character.facing = "left"
        if keys[pygame.K_d]:
            player_character.facing = "right"

    if keys[pygame.K_d] and not right_collide:
        player_character.rect.x += player_character.speed
        player_character.facing = "right"

    if (is_first_attack or time.time() - attack_creation_time >= attack_cooldown + attack_duration):
        attack_ready = True

    if attack_ready:
        player_character.change_color((0, 200, 150))
    else:
        player_character.change_color((0, 100, 255))

    if keys[pygame.K_SPACE]:
        if 'player_attack' not in locals() and attack_ready:
            player_attack = Attack(player_character.facing
                                      , player_character.rect.x
                                      , player_character.rect.y
                                      , player_character.width)
            all_sprites.add(player_attack)
            attack_creation_time = time.time()
            is_first_attack = False
            attack_ready = False

    # Check if attack needs to be removed -- ChatGPT Wrote these 5 lines after I showed it how I was trying to delete the attack I have modified the code a little after I copied it and adjusted other code to integrate what I have learned from this code chunk
    if 'player_attack' in locals():
        if time.time() >= attack_creation_time + attack_duration:
            all_sprites.remove(player_attack)
            del player_attack  # Remove the reference to the attack sprite
        else:
            player_attack.move_with_player(player_character.facing
                                      , player_character.rect.x
                                      , player_character.rect.y
                                      , player_character.width)
    
    # if keys[pygame.K_e]:
    if time.time() - spawn_time >= spawn_interval:
        new_enemy = Enemy(screen_width
                          , screen_height
                          , wall_thickness
                          , player_character.rect.x
                          , player_character.rect.y
                          , player_character.width
                          , player_character.width
                          )
        all_sprites.add(new_enemy)
        enemies.add(new_enemy)
        spawn_time = time.time()


    if no_spawn_enemy_mask_on:
        if bool_to_only_do_this_once:
            debugging_mask = Wall( "blue" 
                            , player_character.rect.x - 200
                            , player_character.rect.y - 200
                            , 400 + player_character.width
                            , 400 + player_character.width)
            bool_to_only_do_this_once = False
        all_sprites.add(debugging_mask)
        debugging_mask.rect.x = player_character.rect.x - 200
        debugging_mask.rect.y = player_character.rect.y - 200



    #ChatGPT generated the following 4 lines in repsonse to me describing an error that my sprite removal method was having
    if 'player_attack' in locals():
        collided_enemies = pygame.sprite.spritecollide(player_attack, enemies, dokill=True)
        for enemy in collided_enemies:
            all_sprites.remove(enemy)

    
    for enemy in enemies:
        if player_character.rect.colliderect(enemy.rect):
            you_died=True
            

    #my old way to remove sprites
    # kill_enemy = False
    # kill_player = False

    # for enemy in enemies:
    #     if player_character.rect.colliderect(enemy.rect):
    #         kill_player = True
    #     if 'player_attack' in locals():
    #         if player_attack.rect.colliderect(enemy.rect):
    #             kill_enemy = True

    #     if kill_enemy:
    #         all_sprites.remove(enemy)
    #         enemies.remove(enemy)

        # if kill_player:
        #     all_sprites.remove(player_character)
        #     exit = True
        #     del player_character

    while you_died:
        #handles quitting
        

        image = pygame.image.load("you_died.png")
        window.fill((255, 255, 255))
        window.blit(image, (0,0))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
                you_died = False
                exit = True
        pygame.display.flip()
        
    

    # Fill the screen with black
    window.fill(background_color)

    all_sprites.draw(window)
   
    pygame.display.flip()

    pygame.time.Clock().tick(60)        

        


    

