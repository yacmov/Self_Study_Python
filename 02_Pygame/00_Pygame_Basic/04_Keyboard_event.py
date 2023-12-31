import pygame

pygame.init() # first task always.

# set up size of screen
screen_width = 480
screen_height = 640

screen = pygame.display.set_mode((screen_width, screen_height))

# set up name of title
pygame.display.set_caption("Mov game")

# load bcakground
background = pygame.image.load("02_Pygame/00_Pygame_basic/Data/background.png")

# load character 
character = pygame.image.load("02_Pygame/00_Pygame_basic/Data/character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width /2) # set up middle position
character_y_pos = screen_height - character_height #s shown character from bottom


# coordinates to move
to_x = 0
to_y = 0


# event roof
running = True # the game still running?
while running:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: # is it closed screen?
            running = False # game is done

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= 5
            elif event.key == pygame.K_RIGHT:
                to_x += 5
            elif event.key == pygame.K_UP:
                to_y -= 5
            elif event.key == pygame.K_DOWN:
                to_y += 5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0
    
    character_x_pos += to_x
    character_y_pos += to_y


# limited area set up
    if character_x_pos < 0:
        character_x_pos = 0

    elif character_x_pos > screen_width - character_width:
        character_x_pos =  screen_width - character_width 
        # error occur because  character_width - character_width instead of screen_width - character_width
  
    if character_y_pos < 0:
        character_y_pos = 0

    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height


    
    screen.blit(background, (0,0)) # drawing background
    screen.blit(character, (character_x_pos, character_y_pos))


    pygame.display.update() # screen roof

 
pygame.quit()
