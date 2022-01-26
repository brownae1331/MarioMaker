import pygame
from settings import *
from support import importFolder


class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.importCharacterAssets()
        self.frameIndex = 0
        self.animationSpeed = 0.15
        self.image = self.animations['idle'][self.frameIndex]
        self.rect = self.image.get_rect(topleft=pos)

        # PLayer movement
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 8
        self.gravity = 0.8
        self.jumpSpeed = -16

        # Player status
        self.status = 'idle'
        self.facingRight = True
        self.onGround = False

    def importCharacterAssets(self):
        characterPath = 'C:/Users/Andy/Documents/GitHub/MarioMaker/graphics/character'
        self.animations = {'idle': [], 'run': [], 'jump': []}

        for animation in self.animations.keys():
            fullPath = characterPath + animation
            self.animations[animation] = importFolder(fullPath)

    def animate(self):
        animation = self.animations[self.status]

        # Loop over the frame index
        self.frameIndex += self.animationSpeed
        if self.frameIndex >= len(animation):
            self.frameIndex = 0

        image = animation[int(self.frameIndex)]
        if self.facingRight:
            self.image = image
        else:
            flippedImage = pygame.transform.flip(image, True, False)
            self.image = flippedImage

    def getInput(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.facingRight = True
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.facingRight = False
        else:
            self.direction.x = 0

        if keys[pygame.K_SPACE] and self.onGround:
            self.jump()

    def getStatus(self):
        if self.onGround == False:
            self.status = 'jump'
        else:
            if self.direction.x != 0:
                self.status = 'run'
            else:
                self.status = 'idle'

    def applyGravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        self.direction.y = self.jumpSpeed

    def update(self):
        self.getInput()
        self.getStatus()
        self.animate()
