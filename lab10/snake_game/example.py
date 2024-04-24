import pygame
from pygame.locals import *
import time
import random
import psycopg2

# Constants for the game
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE
SNAKE_SIZE = 10
FPS = 10

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Function to connect to database
def connect_db():
    try:
        conn = psycopg2.connect("dbname=your_db user=your_user password=your_password")
        return conn
    except psycopg2.Error as e:
        print("Unable to connect to the database.")
        print(e)
        return None

# Function to save score
def save_score(user_id, score, level):
    conn = connect_db()
    if conn is None:
        return
    
    cur = conn.cursor()
    cur.execute("INSERT INTO user_scores (user_id, score, level) VALUES (%s, %s, %s)", (user_id, score, level))
    conn.commit()
    print("Score saved successfully.")
    conn.close()

def snake_game():
    # Initialize Pygame
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Snake Game")
    clock = pygame.time.Clock()

    # Snake and food
    snake = [(100, 100), (90, 100), (80, 100)]
    snake_direction = "RIGHT"
    food_position = (random.randint(0, GRID_WIDTH-1) * GRID_SIZE, random.randint(0, GRID_HEIGHT-1) * GRID_SIZE)

    # Game variables
    score = 0
    level = 1

    # Main game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[K_UP] and snake_direction != "DOWN":
            snake_direction = "UP"
        elif keys[K_DOWN] and snake_direction != "UP":
            snake_direction = "DOWN"
        elif keys[K_LEFT] and snake_direction != "RIGHT":
            snake_direction = "LEFT"
        elif keys[K_RIGHT] and snake_direction != "LEFT":
            snake_direction = "RIGHT"

        # Update snake position
        if snake_direction == "UP":
            head = (snake[0][0], snake[0][1] - SNAKE_SIZE)
        elif snake_direction == "DOWN":
            head = (snake[0][0], snake[0][1] + SNAKE_SIZE)
        elif snake_direction == "LEFT":
            head = (snake[0][0] - SNAKE_SIZE, snake[0][1])
        else:
            head = (snake[0][0] + SNAKE_SIZE, snake[0][1])

        snake.insert(0, head)

        # Check for collisions
        if head == food_position:
            score += 10
            food_position = (random.randint(0, GRID_WIDTH-1) * GRID_SIZE, random.randint(0, GRID_HEIGHT-1) * GRID_SIZE)
        else:
            snake.pop()

        # Draw everything
        screen.fill(BLACK)
        pygame.draw.rect(screen, GREEN, (food_position[0], food_position[1], SNAKE_SIZE, SNAKE_SIZE))
        for segment in snake:
            pygame.draw.rect(screen, WHITE, (segment[0], segment[1], SNAKE_SIZE, SNAKE_SIZE))

        # Check for game over
        if (head[0] < 0 or head[0] >= SCREEN_WIDTH or
            head[1] < 0 or head[1] >= SCREEN_HEIGHT or
            head in snake[1:]):
            # Game over
            print("Game Over")
            running = False

        # Update display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(FPS)

    # After game over
    print("Final Score:", score)
    save_score(user_id, score, level)

    pygame.quit()

if __name__ == "__main__":
    # User enters their username
    username = input("Enter your username: ")

    # Check if user exists or add them
    user_id = (username)

    # Run the Snake game
    snake_game()
