import os
import pygame
#################################################################
# Must do for start 
pygame.init() 

# Set up size of screen
screen_width = 480 # width size
screen_height = 640 # height size

screen = pygame.display.set_mode((screen_width, screen_height))

# Set up name of title
pygame.display.set_caption("Escape from \"POOP\"")

# FPS
clock = pygame.time.Clock()

# Address shotcut set up
currnt_path = os.path.dirname(__file__) # return current file location
image_path = os.path.join(currnt_path, "images") # images folder return
#################################################################


# 1. custom init (background, game images, coorinates, speed, font, time, )



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


    # delay before time out


    pygame.display.update()


# Dely before closed
pygame.time.delay(2000) # 2000 ms / 2 second 

# Pygame quit
pygame.quit()
