import pygame
import os

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Music Player")

music_dir = "C:/Users/User/projects/PP2-2024"  
music_files = [f for f in os.listdir(music_dir) if f.endswith(".mp3")]

current_song_index = 0
current_song = os.path.join(music_dir, music_files[current_song_index])
pygame.mixer.music.load(current_song) 

blue = (0, 0, 255)
font = pygame.font.SysFont("comicsansms", 72)
text = font.render("Music", True, blue)
x = 320 - text.get_width() // 2
y = 240 - text.get_height() // 2

playing = False

done = True
while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if playing:
                    pygame.mixer.music.pause()
                    playing = False
                else:
                    pygame.mixer.music.unpause()
                    playing = True
            elif event.key == pygame.K_n:
                current_song_index = (current_song_index + 1) % len(music_files)
                current_song = os.path.join(music_dir, music_files[current_song_index])
                pygame.mixer.music.load(current_song)
                pygame.mixer.music.play()
            elif event.key == pygame.K_p:
                current_song_index = (current_song_index - 1) % len(music_files)
                current_song = os.path.join(music_dir, music_files[current_song_index])
                pygame.mixer.music.load(current_song)
                pygame.mixer.music.play()

    screen.fill(black)
    screen.blit(text, (x, y))
    pygame.display.flip()

pygame.quit()
