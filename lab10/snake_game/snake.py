import random
import pygame 
import psycopg2 

conn = psycopg2.connect(
    host='localhost', 
    dbname='phonebook', 
    user='postgres', 
    password='318520'
    )

# Create a cursor to work with the database
cur = conn.cursor()


conn.commit()  
'''
# Create a new table
cur.execute("""CREATE TABLE snake (
            username VARCHAR(255) PRIMARY KEY,
            score VARCHAR(255)                      
);
""")

conn.commit()
'''
username = input("Enter your username: ") 

def insert_data(username):
    conn = psycopg2.connect("dbname=phonebook user=postgres password=318520")
    cur = conn.cursor()
    
    cur.execute("INSERT INTO snake (username, score) VALUES (%s, %s)", (username, score))
    
    conn.commit()
    conn.close()

# Initialize Pygame
pygame.init()

# Set the screen dimensions
WIDTH, HEIGHT = 600, 600

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GRAY = (50, 50, 50)

# Set up the screen
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

# Set up the clock for controlling the frame rate
clock = pygame.time.Clock()

# Define the size of each block in the grid
BLOCK_SIZE = 20

# Set the window title
pygame.display.set_caption('Snake')


# Define a Point class to represent a point in 2D space
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# Define a Food class to represent the food that the snake will eat
class Food:
    def __init__(self, x, y):
        # Create a Point object to store the location of the food
        self.location = Point(x, y)

    # Getter method for the x-coordinate of the food
    def x(self):
        return self.location.x

    # Getter method for the y-coordinate of the food
    def y(self):
        return self.location.y

    # Method to generate a new random location for the food
    def generate_new_food(self):
        x = random.randint(0, WIDTH // BLOCK_SIZE - 1)
        y = random.randint(0, HEIGHT // BLOCK_SIZE - 1)
        return self(x, y)

    # Method to update the display of the food
    def update(self):
        pygame.draw.rect(
            SCREEN,
            YELLOW,
            pygame.Rect(
                self.location.x * BLOCK_SIZE,
                self.location.y * BLOCK_SIZE,
                BLOCK_SIZE,
                BLOCK_SIZE,
            )
        )


# Define a Snake class to represent the snake in the game
class Snake:
    def __init__(self):
        # Initialize the snake with two points, forming a horizontal line
        self.points = [
            Point(WIDTH // BLOCK_SIZE // 2, HEIGHT // BLOCK_SIZE // 2),
            Point(WIDTH // BLOCK_SIZE // 2 + 1, HEIGHT // BLOCK_SIZE // 2),
        ]

    # Method to update the display of the snake
    def update(self):
        # Draw the head of the snake in red
        head = self.points[0]
        pygame.draw.rect(
            SCREEN,
            RED,
            pygame.Rect(
                head.x * BLOCK_SIZE,
                head.y * BLOCK_SIZE,
                BLOCK_SIZE,
                BLOCK_SIZE,
            )
        )
        # Draw the body of the snake in blue
        for body in self.points[1:]:
            pygame.draw.rect(
                SCREEN,
                BLUE,
                pygame.Rect(
                    body.x * BLOCK_SIZE,
                    body.y * BLOCK_SIZE,
                    BLOCK_SIZE,
                    BLOCK_SIZE,
                )
            )

    # Method to move the snake in a given direction
    def move(self, dx, dy):
        # Move each point of the snake to the position of the point in front of it
        for idx in range(len(self.points) - 1, 0, -1):
            self.points[idx].x = self.points[idx - 1].x
            self.points[idx].y = self.points[idx - 1].y

        # Move the head of the snake in the specified direction
        self.points[0].x += dx
        self.points[0].y += dy

        # Wrap the snake around the screen if it goes out of bounds
        head = self.points[0]
        if head.x > WIDTH // BLOCK_SIZE:
            head.x = 0
        elif head.x < 0:
            head.x = WIDTH // BLOCK_SIZE - 1
        elif head.y > HEIGHT // BLOCK_SIZE:
            head.y = 0
        elif head.y < 0:
            head.y = HEIGHT // BLOCK_SIZE - 1

    # Method to check if the snake has collided with the food
    def check_collision(self, food):
        if self.points[0].x != food.x():
            return False
        if self.points[0].y != food.y():
            return False
        return True


# Function to draw the grid lines on the screen
def draw_grid():
    for x in range(0, WIDTH, BLOCK_SIZE):
        pygame.draw.line(SCREEN, GRAY, (x, 0), (x, HEIGHT), width=1)
    for y in range(0, HEIGHT, BLOCK_SIZE):
        pygame.draw.line(SCREEN, GRAY, (0, y), (WIDTH, y), width=1)


# Main function to run the game
def main():
    running = True
    snake = Snake()
    food = Food(5, 5)
    dx, dy = 0, 0 
    global score
    score = 0
    speed = 5
    level = 0
    sc = 0

    last_food_time = pygame.time.get_ticks()

    # Main game loop
    while running:
        SCREEN.fill(BLACK)

        # Event handling loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    dx, dy = 0, -1
                elif event.key == pygame.K_DOWN:
                    dx, dy = 0, +1
                elif event.key == pygame.K_LEFT:
                    dx, dy = -1, 0
                elif event.key == pygame.K_RIGHT:
                    dx, dy = +1, 0

        # Move the snake
        snake.move(dx, dy)

        # Check for collision with food
        if snake.check_collision(food):
            g = random.randint(1, 3)
            score += g
            if score // 4 >> sc:
                level += 1
                speed += 2
                sc += 1

            # Add a new segment to the snake
            snake.points.append(Point(food.x(), food.y()))
            # Move the food to a new random location
            food.location.x = random.randint(0, WIDTH // BLOCK_SIZE - 1)
            food.location.y = random.randint(0, HEIGHT // BLOCK_SIZE - 1)

        current_time = pygame.time.get_ticks()
        if current_time - last_food_time >= 12345:
            food = Food.generate_new_food(Food)
            last_food_time = current_time 
            
        # Update the display of the food and snake
        food.update()
        snake.update()

        # Draw the grid lines
        draw_grid()

        # Display the score and level
        font = pygame.font.SysFont('Bauhaus 93', 30)
        text = font.render('Score: ' + str(score), True, WHITE)
        SCREEN.blit(text, (10, 10))

        font = pygame.font.SysFont('Bauhaus 93', 30)
        text = font.render('Level: ' + str(level), True, WHITE)
        SCREEN.blit(text, (10, 50))

        font = pygame.font.SysFont('Bauhaus 93', 30)
        text = font.render('User: ' + str(username), True, WHITE)
        SCREEN.blit(text, (10, 90))


        # Update the display
        pygame.display.flip()

        # Control the frame rate
        clock.tick(speed)


if __name__ == '__main__': 
    #username = input("Enter your username: ")
    main() 
    insert_data(username)
