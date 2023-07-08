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

# input Ball (each ball mention)
ball_images = [
    pygame.image.load(os.path.join(image_path, "Ballon1.png")),
    pygame.image.load(os.path.join(image_path, "Ballon2.png")),
    pygame.image.load(os.path.join(image_path, "Ballon3.png")),
    pygame.image.load(os.path.join(image_path, "Ballon4.png"))]

# Start speed each ball
ball_speed_y = [-18, -15, 12, 9]

# Balls
balls = []

# first big ball
balls.append({
   "pos_x" : 50, # X
   "pos_y" : 50, # Y
   "img_idx" : 0, # index ball image
   "to_x" : 3, # moving coordinate "X" 3
   "to_y" : -6, # movement coordinate "Y
   "init_spd_y" : ball_speed_y[0]})


# gone weapon and ball
weapon_to_remove = -1
ball_to_remove = -1

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
    
    # Ball location set
    for ball_idx, ball_val in enumerate(balls):
        ball_pos_x = ball_val["pos_x"]
        ball_pos_y = ball_val["pos_y"]
        ball_img_idx = ball_val["img_idx"]

        ball_size = ball_images[ball_img_idx].get_rect().size
        ball_width = ball_size[0]
        ball_height = ball_size[1]

        # On the side of the bouncing condition
        if ball_pos_x < 0 or ball_pos_x > screen_width - ball_width:
            ball_val["to_x"] = ball_val["to_x"] * -1

        # On the side of the bouncing condition
        if ball_pos_y >= screen_height - stage_height - ball_height:
            ball_val["to_y"] = ball_val["init_spd_y"]
        else:
            ball_val["to_y"] += 0.5

        ball_val["pos_x"] += ball_val["to_x"]
        ball_val["pos_y"] += ball_val["to_y"]

    # 4 collision handling
   
    # Character update coordinate
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    for ball_idx, ball_val in enumerate(balls):
        ball_pos_x = ball_val["pos_x"]
        ball_pos_y = ball_val["pos_y"]
        ball_img_idx = ball_val["img_idx"]

        ball_rect = ball_images[ball_img_idx].get_rect()
        ball_rect.left = ball_pos_x
        ball_rect.top = ball_pos_y

        if character_rect.colliderect(ball_rect):
            running = False
            break        

        # ball and weapon collision
        for weapon_idx, weapon_val in enumerate(weapons):
            weapon_pos_x = weapon_val[0]
            weapon_pos_y = weapon_val[1]

            weapon_rect = weapon.get_rect()
            weapon_rect.left = weapon_pos_x
            weapon_rect.top = weapon_pos_y

            if weapon_rect.colliderect(ball_rect):
                weapon_to_remove = weapon_idx # weapon remove
                ball_to_remove = ball_idx # ball remove
                
                # if it is not smallest one divide 2
                
                
                if ball_img_idx < 3:
                    # current ball data
                    ball_width = ball_rect.size[0]
                    ball_heioght = ball_rect.size[1]

                    small_ball_rect = ball_images[ball_img_idx + 1].get_rect()
                    small_ball_width = small_ball_rect.size[0]
                    small_ball_height = small_ball_rect.size[1]

                    # divide to left
                    balls.append({   
                        "pos_x" : ball_pos_x + ball_width /2 - small_ball_width /2, # X
                        "pos_y" : ball_pos_y + ball_height /2 - small_ball_height /2, # Y
                        "img_idx" : ball_img_idx +1, # index ball image
                        "to_x" : -3, # moving coordinate "X" 3
                        "to_y" : -6, # movement coordinate "Y
                        "init_spd_y" : ball_speed_y[ball_img_idx +1]})
                    # divide to right
                    balls.append({   
                        "pos_x" : ball_pos_x + ball_width /2 - small_ball_width /2, # X
                        "pos_y" : ball_pos_y + ball_height /2 - small_ball_height /2, # Y
                        "img_idx" : ball_img_idx +1, # index ball image
                        "to_x" : 3, # moving coordinate "X" 3
                        "to_y" : -6, # movement coordinate "Y
                        "init_spd_y" : ball_speed_y[ball_img_idx +1]})

                
                break

    if ball_to_remove > -1:
        del balls[ball_to_remove]
        ball_to_remove = -1

    if weapon_to_remove > -1:
        del weapons[weapon_to_remove]
        weapon_to_remove = -1

    # 5. Drawing on the screen
    screen.blit(background, (0, 0))

    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon, (weapon_x_pos, weapon_y_pos))

    for idx, val in enumerate(balls):
        ball_pos_x = val["pos_x"]
        ball_pos_y = val["pos_y"]
        ball_img_idx = val["img_idx"]
        screen.blit(ball_images[ball_img_idx], (ball_pos_x, ball_pos_y))

    screen.blit(stage, (0, screen_height - stage_height))
    screen.blit(character, (character_x_pos, character_y_pos))

 


    pygame.display.update()


# Dely before closed
pygame.time.delay(2000) # 2000 ms / 2 second 

# Pygame quit
pygame.quit()
