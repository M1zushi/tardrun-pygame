# Sprites by Arks
# https://arks.itch.io/dino-characters

import pygame
from pygame.locals import *
import os

# Initiating Enviroment
pygame.init()
screen = pygame.display.set_mode( (720, 480) )
pygame.display.set_caption('Tard')

# Constant Variables
GRAY = (200,200,200)
BLUE = (0,0,200)
GROUND = (0, 0, 100)
FPS = 30

active = True
clock = pygame.time.Clock()

player_x = 30
player_y = 250
new_player_x = player_x
new_player_y = player_y
oldx = player_x

player_speed = 0
player_acceleration = 0.5
max_player_speed = 7.5

vertical_velocity = 0
vertical_acceleration = 0.25
max_jump = -6
jump = False

# Sets Drawings
player_sprite = pygame.image.load('Assets/tardsprites/tard_00.png')

platforms = [
    pygame.Rect(0, 380, 720, 30),
    pygame.Rect(225, 250, 300, 30)
]

def draw():
    screen.fill(GRAY)
    for r in platforms:
        if platforms.index(r) == 0:
            pygame.draw.rect(screen, GROUND, r)
        else:
            pygame.draw.rect(screen, BLUE, r)

    screen.blit(player_sprite, (player_x, player_y))

    pygame.display.flip()

# Loops Game
while active == True:
    # Allows to quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            active = False

    # Moves the player horizontally with respective speed and acceleration (Shift doubles speed)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        if keys[pygame.K_RSHIFT]:
            if player_speed < max_player_speed:
                player_speed += player_acceleration
            new_player_x += player_speed * 2
        elif keys[pygame.K_LSHIFT]:
            if player_speed < max_player_speed:
                player_speed += player_acceleration
            new_player_x += player_speed * 2
        else:
            if player_speed < max_player_speed:
                player_speed += player_acceleration
            new_player_x += player_speed

    if keys[pygame.K_LEFT]:
        if keys[pygame.K_RSHIFT]:
            if player_speed < max_player_speed:
                player_speed += player_acceleration
            new_player_x -= player_speed * 2
        elif keys[pygame.K_LSHIFT]:
            if player_speed < max_player_speed:
                player_speed += player_acceleration
            new_player_x -= player_speed * 2
        else:
            if player_speed < max_player_speed:
                player_speed += player_acceleration
            new_player_x -= player_speed

    # Initiates vertical physics and allows player to jump
    if jump == False:
        vertical_velocity += vertical_acceleration
    new_player_y += vertical_velocity

    if keys[pygame.K_UP]:
        if vertical_velocity > max_jump:
            vertical_velocity = -2
            jump = True
        else:
            jump = False

    # Checks for vertical collisions and if the player can move
    new_player_rect = pygame.Rect(player_x, new_player_y, 60, 60)
    y_collision = False

    for r in platforms:
        if r.colliderect(new_player_rect):
            y_collision = True
            vertical_velocity = 0
            break

    if y_collision == False:
        player_y = new_player_y
        vertical_velocity = 0

    # Checks for horizontal colisions and if the player can move
    new_player_rect = pygame.Rect(new_player_x, player_y, 60, 60)
    x_collision = False

    for r in platforms:
        if r.colliderect(new_player_rect):
            x_collision = True
            break

    if x_collision == False:
        player_x = new_player_x
        # Updates the "current" frame
        newx = new_player_x

    # Compares this frame's position with the previous before it updates
    # Check if player = static
    if oldx == newx:
        player_speed = 0

    # Updates the "previous" frame
    oldx = player_x

    # Updates Game Display
    draw()
    clock.tick(FPS)

# Actually quits
pygame.quit()
