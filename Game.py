import pygame

pygame.init()

# Define some colors
BLACK = (0,   0,   0)
WHITE = (255, 255, 255)
RED = (255,   0,   0)
BLUE = (0, 0, 255)
GREY = (211, 211, 211)
YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)


class Player(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()

    def moveLeft(self):
        if self.rect.x < 20:
            self.rect.x = 20
        else:
            self.rect.x -= 5

    def moveRight(self):
        if self.rect.x > 1900:
            self.rect.x = 1900
        else:
            self.rect.x += 5


# List of all sprits
spritesList = pygame.sprite.Group()

# Size of screen
screenWidth = 1920
screenHeight = 1080
screen = pygame.display.set_mode([screenWidth, screenHeight])

# Add the player
player = Player(RED, 20, 100)
player.rect.x = 215
player.rect.y = 550
spritesList.add(player)

done = False
clock = pygame.time.Clock()

# Main game loop
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Player movement
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        player.moveLeft()
    if key[pygame.K_RIGHT]:
        player.moveRight()
    spritesList.update()

    # Draw the sprites on the screen
    spritesList.draw(screen)
    pygame.display.flip()
    clock.tick(60)
    screen.fill(WHITE)

pygame.quit()
