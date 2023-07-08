import pygame

pygame.init() # first task always.

# set up size of screen
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))



# set up name of title
pygame.display.set_caption("Mov game")

# load bcakground
background = pygame.image.load("02_Practice_Pygame/00_Pygame_basic/Data/background.png")
# C:\Users\yacmo\OneDrive\Desktop\
# event roof
running = True # the game still running?
while running:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: # is it closed screen?
            running = False # game is done
    
    screen.blit(background, (0,0)) # drawing background
    # screen.fill((0, 0, 255))
    
    pygame.display.update() # screen roof

pygame.quit()
