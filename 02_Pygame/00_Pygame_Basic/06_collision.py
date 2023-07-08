import pygame

pygame.init()  # first task always.

# set up size of screen
screen_width = 480
screen_height = 640

screen = pygame.display.set_mode((screen_width, screen_height))

# set up name of title
pygame.display.set_caption("Mov game")

# FPS
clock = pygame.time.Clock()

# load bcakground
background = pygame.image.load("02_Pygame/00_Pygame_basic/Data/background.png")

# load character
character = pygame.image.load("02_Pygame/00_Pygame_basic/Data/character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - \
    (character_width / 2)  # set up middle position
character_y_pos = screen_height - character_height  # s shown character from bottom


# coordinates to move
to_x = 0
to_y = 0

# character speed
character_speed = 0.5


# Enermy
enemy = pygame.image.load("02_Pygame/00_Pygame_basic/Data/enemy.png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = (screen_width / 2) - (enemy_width / 2)  # set up middle position
enemy_y_pos = (screen_height / 2) - \
    (enemy_height / 2)  # s shown enemy from bottom


# event roof
running = True  # the game still running?
while running:
    dt = clock.tick(60)  # setup frame

# if character need to move 100
# 10 fps : move 10 per second
# 20 fps : move 20 per second
# if need to sync all fps?

    print("FPS : " + str(clock.get_fps()))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # is it closed screen?
            running = False  # game is done

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    # limited area set up
    if character_x_pos < 0:
        character_x_pos = 0

    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
        # error occur because  character_width - character_width instead of screen_width - character_width

    if character_y_pos < 0:
        character_y_pos = 0

    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    # collision between charactors
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

    screen.blit(background, (0, 0))  # drawing background
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))

    pygame.display.update()  # screen roof


pygame.quit()
