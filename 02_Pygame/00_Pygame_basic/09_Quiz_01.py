# Make a game about avoiding the "POOP" falling from the sky

# [Game conditions]
# 1. The character is located at the bottom of the screen and can only be moved left and right
# 2. Poop falls from the top of the screen, and the X coordinate is set randomly each time
# 3. If the character dodges the poop, the next poop drops again
# 4. Game over when character collides with poop
# 5. FPS fixed at 30

# [Game image]
# 1. Background: 680 * 480 (vertical and horizontal) - 02_Practive_Pygame_basic/Pygame_project_00/Data/background.Png
# 2. Characters: 70*70 - 02_Practive_Pygame_basic/Pygame_project_00/Data/characters.Png
# 3. Poop: 70*70 - 02_Practive_Pygame_basic/Pygame_project_00/Data/enemy.Png

# images from pixabay
# 
# 
import pygame
from random import *

#################################################################
# Must do for start
pygame.init()

# Set up size of screen
screen_width = 480  # width size
screen_height = 640  # height size

screen = pygame.display.set_mode((screen_width, screen_height))

# Set up name of title
pygame.display.set_caption("Escape \"POOP\"")

# FPS
clock = pygame.time.Clock()
#################################################################


# 1. custom init (background, game images, coorinates, speed, font, time, )
# Background
background = pygame.image.load("02_Practice_Pygame/00_Pygame_basic/Data/background.png")

# Character
character = pygame.image.load("02_Practice_Pygame/00_Pygame_basic/Data/character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - \
    (character_width / 2)  # set up middle position
character_y_pos = screen_height - character_height  # s shown character from bottom

# Character location 
to_x = 0
character_speed = 0.5

# enermy
enemy = pygame.image.load("02_Practice_Pygame/00_Pygame_basic/Data/enemy.png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = randint(1, screen_width - enemy_width)  # set up random x position
enemy_y_pos = -enemy_height  # set up y 0 - start from top

# Character location 
enemy_speed = 15

# font
game_font = pygame.font.Font(None, 40)  # setup font

# Total time
total_time = 10

# start time
start_ticks = pygame.time.get_ticks()


running = True
while running:
    dt = clock.tick(60)

    # 2. Event handling (keyboard, mouose ETC)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0

    # 3. Set up character location
    character_x_pos += to_x * dt

    if character_x_pos < 0:
        character_x_pos = 0

    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
        # error occur because  character_width - character_width instead of screen_width - character_width

    enemy_y_pos += enemy_speed
    if enemy_y_pos >= screen_height:
        enemy_y_pos = -enemy_height
        enemy_x_pos = randint(1, screen_width - enemy_width)



    # 4 collision handling
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    # check collision
    if character_rect.colliderect(enemy_rect):
        print("Collision")
        running = False


    # 5. Drawing on the screen
    screen.blit(background, (0, 0))  # drawing background
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))

    pygame.display.update()

# Dely before closed
pygame.time.delay(2000)  # 2000 ms / 2 second

# Pygame quit
pygame.quit()
