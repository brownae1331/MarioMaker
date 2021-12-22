import pygame
from settings import *
from tiles import Tile
from level import Level
from player import Player

pygame.init()

# Define images
bg_img = pygame.image.load('Images/background.jpg')

# List of all sprits
spritesList = pygame.sprite.Group()

# Size of screen
screen = pygame.display.set_mode([screenWidth, screenHeight])

done = False
clock = pygame.time.Clock()
level = Level(levelMap, screen)

# Main game loop
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    level.run()

    # Draw the sprites
    spritesList.draw(screen)
    pygame.display.flip()
    clock.tick(60)
    screen.fill(BLACK)


pygame.quit()
