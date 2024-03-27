import pygame
import datetime

pygame.init()
screen = pygame.display.set_mode((870, 800))
miki = pygame.image.load("mainclock.png")
larm = pygame.image.load("leftarm.png")
rarm = pygame.image.load("rightarm.png")
done = False
original_rect_l = larm.get_rect(center=(440, 430))
original_rect_r = rarm.get_rect(center=(440, 430))

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True 
    
    current_time = datetime.datetime.now()
    
    seconds_angle = current_time.second * 6
    minutes_angle = (current_time.minute * 6) + (current_time.second / 10)

    rotated_image_l = pygame.transform.rotate(larm, -seconds_angle)
    rotated_rect_l = rotated_image_l.get_rect(center=original_rect_l.center)
    rotated_image_r = pygame.transform.rotate(rarm, -minutes_angle)
    rotated_rect_r = rotated_image_r.get_rect(center=original_rect_r.center)

    screen.fill((0, 0, 0))
    screen.blit(miki, (0, 0))
    screen.blit(rotated_image_l, rotated_rect_l)
    screen.blit(rotated_image_r, rotated_rect_r)

    pygame.display.flip()