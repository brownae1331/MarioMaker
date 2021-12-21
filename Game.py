import pygame

pygame.init()

# Define colors
BLACK = (0,   0,   0)
WHITE = (255, 255, 255)
RED = (255,   0,   0)
BLUE = (0, 0, 255)
GREY = (211, 211, 211)
YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)

# Define images
bg_img = pygame.image.load('Images/background.jpg')

# Define variables
tileSize = 10


def drawGrid():
    for line in range(0, screenWidth, tileSize):
        pygame.draw.line(screen, WHITE, (0, line * tileSize),
                         (screenWidth, line * tileSize))
        pygame.draw.line(screen, WHITE, (line * tileSize, 0),
                         (line * tileSize, screenHeight))


class Player(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()

    def moveLeft(self):
        if self.rect.x < 0:
            self.rect.x = 0
        else:
            self.rect.x -= 5

    def moveRight(self):
        if self.rect.x > 1580:
            self.rect.x = 1580
        else:
            self.rect.x += 5


# List of all sprits
spritesList = pygame.sprite.Group()

# Size of screen
screenWidth = 1600
screenHeight = 800
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

    # Draw the background
    screen.blit(bg_img, (0, 0))
    drawGrid()

    # Draw the sprites
    spritesList.draw(screen)
    pygame.display.flip()
    clock.tick(60)
    screen.fill(WHITE)


pygame.quit()
