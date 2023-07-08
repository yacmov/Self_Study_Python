import os
import pygame

#################################################################
# Must do for start 
pygame.init() 

# Set up size of screen
screen_width = 640 # width size
screen_height = 480 # height size

screen = pygame.display.set_mode((screen_width, screen_height))

# Set up name of title
pygame.display.set_caption("Mov \"Pang\"")

# FPS
clock = pygame.time.Clock()
#################################################################


# 1. custom init (background, game images, coorinates, speed, font, time, )
currnt_path = os.path.dirname(__file__) # return current file location
image_path = os.path.join(currnt_path, "images") # images folder return

# Background
background = pygame.image.load(os.path.join(image_path, "Background.png"))

# Stage 
stage = pygame.image.load(os.path.join(image_path, "Stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1]

# Character
character = pygame.image.load(os.path.join(image_path, "Character.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height - stage_height



running = True  
while running:
    dt = clock.tick(30)

    # 2. Event handling (keyboard, mouose ETC)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
            running = False  

        
    # 3. Set up character location

    # 4 collision handling
   
    # 5. Drawing on the screen
    screen.blit(background, (0, 0))
    screen.blit(stage, (0, screen_height - stage_height))
    screen.blit(character, (character_x_pos, character_y_pos))


    pygame.display.update()


# Dely before closed
pygame.time.delay(2000) # 2000 ms / 2 second 

# Pygame quit
pygame.quit()
