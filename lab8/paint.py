# Import the pygame module
import pygame

# Function to draw a rectangle on the surface
def rectangle(surf, cur, end, d, color):
    # Extract coordinates from current and end points
    x1, y1, x2, y2 = cur[0], cur[1], end[0], end[1] 
    # Calculate width and height of the rectangle
    a = abs(x1-x2)
    b = abs(y1-y2)
    # Draw the rectangle on the surface
    pygame.draw.rect(surf, color, (min(x1, x2), min(y1, y2), a, b), d)

# Function to draw a line (pen tool) on the surface
def pen(surf, cur, end, d, color):
    # Draw a line on the surface
    pygame.draw.line(surf, color, cur, end, d)

# Function to draw a circle on the surface
def circle(surf, cur, end, d, color):
    # Extract coordinates from current and end points
    x1, y1, x2, y2 = cur[0], cur[1], end[0], end[1]
    # Calculate width and height of the rectangle enclosing the circle
    a = abs(x1-x2)
    b = abs(y1-y2)
    # Draw the circle on the surface
    pygame.draw.circle(surf, color, (min(x1,x2)+a/2, min(y1, y2)+b/2), min(a, b)/2, d)

# Function to erase on the surface
def eraser(surf, cur):
    # Draw a black circle (simulating eraser)
    x1, y1 = cur[0], cur[1]
    pygame.draw.circle(surf, "Black", (x1, y1), 20)

# Set up constants
FPS = 60
WIDTH = 640
HEIGHT = 480

# Initialize Pygame
pygame.init()
# Set up the display window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# Set the title of the window
pygame.display.set_caption('Paint')
# Create a surface for drawing
baseLayer = pygame.Surface((640, 480))
# Create a clock object to control the frame rate
clock = pygame.time.Clock()

# Initialize variables
mode = "Rectangle"  # Default drawing mode
color = "Red"  # Default drawing color
isMouseDown = False
currentX = -1
currentY = -1
prevX = -1
prevY = -1

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            # Switch drawing colors
            if event.key == pygame.K_r:
                color = "Red"
            if event.key == pygame.K_b:
                color = "Blue"
            if event.key == pygame.K_g:
                color = "Green"
            if event.key == pygame.K_w:
                color = "White"
            
            # Switch drawing tools
            if event.key == pygame.K_2:
                mode = "Rectangle"
            if event.key == pygame.K_3:
                mode = "Circle"
            if event.key == pygame.K_1:
                mode = "Pen"
            if event.key == pygame.K_4:
                mode = "Eraser"

        if event.type == pygame.MOUSEBUTTONDOWN:
            xnow = event.pos[0]
            ynow = event.pos[1]
            last_pos = (xnow, ynow)
            isMouseDown = True
        if event.type == pygame.MOUSEBUTTONUP:
            isMouseDown = False
            baseLayer.blit(screen, (0,0))
        if event.type == pygame.MOUSEMOTION:
            if isMouseDown == True:
                if mode == 'Pen':
                    pen(baseLayer, last_pos, (xnow, ynow), 1, color)
                    last_pos = (xnow, ynow)
                xnow = event.pos[0]
                ynow = event.pos[1]

    if isMouseDown == True and last_pos[0] != -1 and last_pos[1] != -1 and xnow != -1 and ynow != -1:
        screen.blit(baseLayer, (0, 0))
        if mode == 'Rectangle':
            rectangle(screen, last_pos, (xnow, ynow), 1, color)
        elif mode == 'Circle':
            circle(screen, last_pos, (xnow, ynow), 1, color)
        elif mode == "Eraser":
            eraser(baseLayer, (xnow, ynow))

    pygame.display.update()
    clock.tick(144)  # Limit the frame rate to 144 frames per second
