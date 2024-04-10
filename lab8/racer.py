# Imports
import pygame, sys
from pygame.locals import *
import random, time

# Initialzing Pygame
pygame.init()

# Setting up FPS (Frames Per Second)
FPS = 60
FramePerSec = pygame.time.Clock()

# Creating colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5  # Initial speed of the game
SCORE = 0  # Initial score

# Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

# Load background image
background = pygame.image.load("AnimatedStreet.png")

# Create a white screen
DISPLAYSURF = pygame.display.set_mode((400, 600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")


# Enemy Class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)  # Move the enemy down
        if (self.rect.bottom > 600):  # If enemy moves off the screen
            self.rect.top = 0  # Reset its position to the top
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)  # Randomize its horizontal position


# Coin Class
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("coin.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, 3)  # Move the coin down
        if (self.rect.bottom > 600):  # If coin moves off the screen
            self.rect.top = 0  # Reset its position to the top
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)  # Randomize its horizontal position

    def disappear(self):
        self.rect.top = 0
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)


# Player Class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()

        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)  # Move player left
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)  # Move player right


# Setting up Sprites
P1 = Player()
E1 = Enemy()
C1 = Coin()

# Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
coins = pygame.sprite.Group()
coins.add(C1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)


# Adding a new User event to increase speed
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)  # Trigger event every second

# Game Loop
while True:
    
    # Cycles through all events occurring
    for event in pygame.event.get(): 
        
        # Increase game speed event
        if event.type == INC_SPEED:
            SPEED += 0.1  # Increase game speed every second

        # Quit event
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Draw background
    DISPLAYSURF.blit(background, (0, 0))

    # Display score
    scores = font_small.render(str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10, 10))

    # Move and re-draw all sprites
    for entity in all_sprites:
        entity.move()
        DISPLAYSURF.blit(entity.image, entity.rect) 

    # Check for collision with coins
    if pygame.sprite.spritecollideany(P1, coins):
        Coin.disappear(C1)  # Make the coin disappear
        SCORE += 1  # Increment score

    # Check for collision with enemies
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('crash.wav').play()  # Play crash sound
        time.sleep(1)  # Pause for 1 second

        # Display game over message
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30, 250))

        pygame.display.update()

        # Remove all sprites
        for entity in all_sprites:
            entity.kill()

        time.sleep(2)  # Pause for 2 seconds
        pygame.quit()
        sys.exit()

    pygame.display.update()  # Update the display
    FramePerSec.tick(FPS)  # Control the frame rate
