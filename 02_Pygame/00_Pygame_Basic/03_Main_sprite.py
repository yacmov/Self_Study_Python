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
character_x_pos = screen_width / 2 - character_size[0] /2 # set up middle position
character_y_pos = screen_height - character_size[0] #s shown character from bottom



# event roof
running = True # the game still running?
while running:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: # is it closed screen?
            running = False # game is done
    
    screen.blit(background, (0,0)) # drawing background
    screen.blit(character, (character_x_pos, character_y_pos))


    pygame.display.update() # screen roof

pygame.quit()
