import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

red = (255, 0, 0)
blue = (0, 0, 255)

done = False
is_red = True

x = 400
y = 300

clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT] and x<800-25: 
        x += 20
    if keys[pygame.K_LEFT] and x>25: 
        x -= 20
    if keys[pygame.K_DOWN] and y<600-25:
        y += 20
    if keys[pygame.K_UP] and y>25:
        y -= 20
        
    screen.fill((255, 255, 255))

    pygame.draw.circle(screen, red,(x, y),25)

    pygame.display.flip()
    clock.tick(60)
    