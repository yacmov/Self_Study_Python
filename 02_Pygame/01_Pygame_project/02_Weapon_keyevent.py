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

# Character moving drection
character_to_x = 0

# Character moving speed
character_speed = 5

# make Weapon
weapon = pygame.image.load(os.path.join(image_path, "Weapon.png"))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]

# Weapon can multiful shoot
weapons = []

# Speed for weapon
weapon_speed = 10




running = True  
while running:
    dt = clock.tick(30)

    # 2. Event handling (keyboard, mouose ETC)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
            running = False  

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT: # if left botton is down character move left
                character_to_x -= character_speed
            
            elif event.key == pygame.K_RIGHT:
                character_to_x += character_speed # if right botton is down character move right
            
            elif event.key == pygame.K_SPACE: # # if space botton is down character attack
                weapon_x_pos = character_x_pos + character_width / 2 - weapon_width / 2
                weapon_y_pos = character_y_pos - character_height
                weapons.append([weapon_x_pos, weapon_y_pos])

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or pygame.K_RIGHT:
                character_to_x = 0
            pass
            

             


        
    # 3. Set up character location
    character_x_pos += character_to_x

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos >= screen_width - character_width:
        character_x_pos = screen_width - character_width

    # relocation weapon coodinate - moving from bottom to top
    weapons = [[w[0], w[1] - weapon_speed] for w in weapons]

    # remove weapon when reach ceiling
    weapons = [[w[0], w[1] - weapon_speed] for w in weapons if w[1] > 0 ]
    


    # 4 collision handling
   
    # 5. Drawing on the screen
    screen.blit(background, (0, 0))

    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon, (weapon_x_pos, weapon_y_pos))

    screen.blit(stage, (0, screen_height - stage_height))
    screen.blit(character, (character_x_pos, character_y_pos))

 


    pygame.display.update()


# Dely before closed
pygame.time.delay(2000) # 2000 ms / 2 second 

# Pygame quit
pygame.quit()
