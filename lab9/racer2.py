# Imports
import pygame, sys
from pygame.locals import *
import random, time

# Initialzing Pygame
pygame.init()

# Setting up FPS
FPS = 60
FramePerSec = pygame.time.Clock()

# Creating colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Screen dimensions
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

# Initial speed of enemies
SPEED = 5

# Score variable
SCORE = 0

# Variable to track score increments
sc = 0

# Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

# Load background image
background = pygame.image.load("AnimatedStreet.png")

# Create the display surface
DISPLAYSURF = pygame.display.set_mode((400, 600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Racer 2")


# Enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    # Method to move the enemy sprite
    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if (self.rect.bottom > 600):
            # Reset the position when the enemy reaches the bottom
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)


# Coin class
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("coin.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    # Method to move the coin sprite
    def move(self):
        global SCORE
        self.rect.move_ip(0, 3)
        if (self.rect.bottom > 600):
            # Reset the position when the coin reaches the bottom
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    # Method to make the coin disappear
    def disappear(self):
        self.rect.top = 0
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)


# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    # Method to move the player sprite
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)


# Create instances of player, enemy, and coin
P1 = Player()
E1 = Enemy()
C1 = Coin()

# Create sprite groups
enemies = pygame.sprite.Group()
enemies.add(E1)
coins = pygame.sprite.Group()
coins.add(C1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)


# Game Loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Clear the display surface and draw the background
    DISPLAYSURF.blit(background, (0, 0))
    
    # Display the score
    scores = font_small.render(str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10, 10))

    # Move and redraw all sprites
    for entity in all_sprites:
        entity.move()
        DISPLAYSURF.blit(entity.image, entity.rect)

    # Check for collision between player and coins
    if pygame.sprite.spritecollideany(P1, coins):
        # Make the coin disappear
        Coin.disappear(C1)
        # Increment score randomly between 1 and 3
        x = random.randint(1,3)
        SCORE += x

    # Increase speed and score increment level
    if SCORE // 4 >> sc:
        SPEED += 1
        sc += 1

    # Display current speed
    font = pygame.font.SysFont('Bauhaus 93', 20)
    text = font.render('Level: ' + str(SPEED - 4), True, BLACK)
    DISPLAYSURF.blit(text, (SCREEN_WIDTH - 140, 10))

    # Check for collision between player and enemies
    if pygame.sprite.spritecollideany(P1, enemies):
        # Play crash sound
        pygame.mixer.Sound('crash.wav').play()
        # Pause for a moment
        time.sleep(1)

        # Display game over message
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30, 250))

        pygame.display.update()

        # Remove all sprites
        for entity in all_sprites:
            entity.kill()

        # Pause for 2 seconds
        time.sleep(2)
        pygame.quit()
        sys.exit()

    # Update the display
    pygame.display.update()
    
    # Cap the frame rate
    FramePerSec.tick(FPS)
