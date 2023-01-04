# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 22:21:42 2023

@author: simao
"""

import pygame
import random

# Initialize pygame
pygame.init()

# Set screen size
screen_size = (600, 600)

# Create screen
screen = pygame.display.set_mode(screen_size)

# Set title
pygame.display.set_caption("Snake")

# Set frame rate
clock = pygame.time.Clock()

# Set snake starting position and size
snake_pos = [300, 300]
snake_body = [[300, 300], [290, 300], [280, 300]]

# Set food starting position
food_pos = [random.randrange(1, (screen_size[0]//10)) * 10, random.randrange(1, (screen_size[1]//10)) * 10]
food_spawn = True

# Set direction
direction = 'RIGHT'
change_to = direction

# Set score
score = 0

# Set game over
game_over = False

# Game loop
while not game_over:
    # Check for user input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

    # If snake collides with boundary, game over
    if snake_pos[0] == screen_size[0] or snake_pos[0] < 0:
        game_over = True
    if snake_pos[1] == screen_size[1] or snake_pos[1] < 0:
        game_over = True

    # If snake collides with itself, game over
    for block in snake_body[1:]:
        if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
            game_over = True

    # If snake is moving, change direction
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # Move snake
    if direction == 'UP':
        snake_pos[1] -= 10
    if direction == 'DOWN':
        snake_pos[1] += 10
    if direction == 'LEFT':
        snake_pos[0] -= 10
    if direction == 'RIGHT':
        snake_pos[0] += 10

    # Snake body growing mechanism
    snake_body.insert(0, list(snake_pos))
    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        score += 1
        food_spawn = False
    else:
        snake_body.pop()

    if not food_spawn:
        food_pos = [random.randrange(1, (screen_size[0]//10)) * 10, random.randrange(1, (screen_size[1]//10)) * 10]
    food_spawn = True

    screen.fill((0, 0, 0))

    # Draw snake
    for pos in snake_body:
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(pos[0], pos[1], 10, 10))

    # Draw food
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(food_pos[0], food_pos[1], 10, 10))

    # Refresh screen
    pygame.display.update()

    # Set frame rate
    clock.tick(20)

# Game over message
msg = "Game Over. Your score is: " + str(score)
game_over_font = pygame.font.Font('freesansbold.ttf', 18)
game_over_screen = game_over_font.render(msg, True, (255, 255, 255))
game_over_rect = game_over_screen.get_rect()
game_over_rect.midtop = (screen_size[0]/2, 10)
screen.blit(game_over_screen, game_over_rect)
pygame.display.update()
pygame.time.delay(3000)

# Quit game
pygame.quit()
quit()
