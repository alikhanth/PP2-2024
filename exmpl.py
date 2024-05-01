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

def play_song():
    pygame.mixer.music.play()
def stop_song():
    pygame.mixer.music.stop()
def next_song():
    global current_song_index
    current_song_index = (current_song_index + 1) % len(music_files)
    load_and_play_current_song()
def previous_song():
    global current_song_index
    current_song_index = (current_song_index - 1) % len(music_files)
    load_and_play_current_song()
def load_and_play_current_song():
    global current_song
    current_song = os.path.join(music_dir, music_files[current_song_index])
    pygame.mixer.music.load(current_song)
    play_song() 
blue = (0, 0, 255)
font = pygame.font.SysFont("comicsansms", 72)

text = font.render("Music", True, blue) 

x = 320 - text.get_width() // 2
y = 240 - text.get_height() // 2

done = True
while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if pygame.mixer.music.get_busy():
                    stop_song()
                else:
                    play_song()
            elif event.key == pygame.K_n:
                next_song()
            elif event.key == pygame.K_p:
                previous_song()

    screen.fill(black) 

    screen.blit(text, (x , y))
    pygame.display.flip()
pygame.quit()
