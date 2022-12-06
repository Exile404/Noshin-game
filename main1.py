import random
import sys
import time
import pygame
from pygame.locals import *
from pygame import mixer


pygame.init()

# SCREEN HEIGHT/WIDTH
width, height = (700, 500)
size = (width, height)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("wack-a-cloud")

# COLOURS
black = (3, 21, 48)
white = (242, 244, 247)
sky_blue = (177, 213, 229)
baby_blue = (186, 194, 207)

# MENU VARIABLES
num_buttons = 4
button_distance_y = 75
button_x = 200
button_y = 50



# STATS

# running = True
# menu = True
# game = False
# is_clicked = False

# FONT
my_font = pygame.font.SysFont('COURIER SANS', 110)
#Courier New
my_font_2 = pygame.font.SysFont('BUNGEE SHADE', 80)
my_font_3 = pygame.font.SysFont('BUNGEE SHADE', 50)
my_font_4 = pygame.font.SysFont('BUNGEE SHADE', 30)

mixer.init()
mixer.music.load('output_screen_background_music_pygame.mp3')

mixer.music.play(-1)
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Loop until the user clicks the close button.

start = time.time()

mouse_x,mouse_y = 0,0
def game_start(start,num=20):
    # CLOUD VARIABLES

    cloud_radius = 25
    cloud_x, cloud_y = (100, 100)
    cloud_distance_x = (width - (cloud_x * 2)) / 3
    cloud_distance_y = (height - (cloud_y * 2)) / 2
    cloud_speed = 0.8

    # ROWS AND COLUMNS
    num_rows = 3
    num_cols = 4

    # Randomizing the position of the mole/cloud
    random_col = random.randrange(0, num_cols)
    random_row = random.randrange(0, num_rows)
    screen.fill(sky_blue)
    attempts = 0

    score = 0
    max_score = num

    max_attempts = num
    num_clicks = 0

    while attempts<=max_attempts:
        for row in range(num_rows):
            for col in range(num_cols):
                x_offset = col * cloud_distance_x
                y_offset = row * cloud_distance_y
                pygame.draw.circle(screen, white, (cloud_x + x_offset, cloud_y + y_offset),
                                   cloud_radius * 2)

            end = time.time()
            if end - start >= cloud_speed:
                random_col = random.randrange(0, num_cols)
                random_row = random.randrange(0, num_rows)
                start = time.time()
                end = time.time()
                attempts += 1


            mole_x = cloud_x + random_col * cloud_distance_x
            mole_y = cloud_y + random_row * cloud_distance_y
            mole = pygame.draw.circle(screen, baby_blue, (mole_x, mole_y), cloud_radius)
            for event in pygame.event.get():  # Checks all events
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:  # If the current event is the mouse button down event
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    is_clicked_x = mole_x - cloud_radius < mouse_x < mole_x + cloud_radius
                    is_clicked_y = mole_y - cloud_radius < mouse_y < mole_y + cloud_radius
                    if is_clicked_x and is_clicked_y:
                        score += 1

                        break
        # DISPLAY SCORE
        pygame.draw.rect(screen, sky_blue, (410, 0, 50, 50))
        score_text = my_font_3.render(f"SCORE: {str(score)}", True, (43, 55, 74))
        screen.blit(score_text, (270, 10))

        pygame.display.flip()
    return score,max_attempts

def endScreen(score,attempts):

    screen.fill(sky_blue)

    while True:

        final_score = my_font.render(f"SCORE: {str(score)}/{attempts}", True,(43, 55, 74))
        screen.blit(final_score, (125, 100))
        pygame.draw.rect(screen, white,(120, 190,430, 50))
        button_RTM = my_font_3.render("RETURN TO MAIN MENU", True, (43, 55, 74))
        screen.blit(button_RTM, (130, 200))
        pygame.draw.rect(screen, white, (275, 260, 130 , 50))
        button_quit = my_font_3.render("QUIT", True, (43, 55, 74))
        screen.blit(button_quit, (300, 270))
        pygame.display.flip()
        for event in pygame.event.get():  # Checks all events
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:  # If the current event is the mouse button down event
                mouse_x, mouse_y = pygame.mouse.get_pos()  # Stores the mouse position
                if 125<=mouse_x<=542 and 198<=mouse_y<=234:
                    return True
                else:
                    return False
def HTM():
    while True:
        screen.fill(sky_blue)

        rule1 = my_font_4.render(f"Rule 1: ", True,(43, 55, 74))
        screen.blit(rule1, (30, 50))
        rule2 = my_font_4.render(f"Rule 2: ", True, (43, 55, 74))
        screen.blit(rule2, (30, 100))
        rule3 = my_font_4.render(f"Rule 3: ", True, (43, 55, 74))
        screen.blit(rule3, (30, 150))
        rule4 = my_font_4.render(f"Rule 4: ", True, (43, 55, 74))
        screen.blit(rule4, (30, 200))
        pygame.draw.rect(screen, white, (120, 310, 430, 50))
        button_RTM = my_font_3.render("RETURN TO MAIN MENU", True, (43, 55, 74))
        screen.blit(button_RTM, (130, 320))
        # --- Go  ahead and update the screen with what we've drawn.
        pygame.display.flip()
        for event in pygame.event.get():  # Checks all events
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:  # If the current event is the mouse button down event
                mouse_x, mouse_y = pygame.mouse.get_pos()  # Stores the mouse position
                print(mouse_x,mouse_y)
                if 122<=mouse_x<=544 and 314<=mouse_y<=356:
                    return True
def settings():
    while True:

        screen.fill(sky_blue)

        rule1 = my_font_4.render(f"Attempts: ", True, (43, 55, 74))
        screen.blit(rule1, (30, 50))
        pygame.draw.rect(screen, white, (150, 30, 50, 50))
        score1 = my_font_4.render(f"10", True, (43, 55, 74))
        screen.blit(score1, (160, 40))
        pygame.draw.rect(screen, white, (210, 30, 50, 50))
        score2 = my_font_4.render(f"15", True, (43, 55, 74))
        screen.blit(score2, (220, 40))
        pygame.draw.rect(screen, white, (270, 30, 50, 50))
        score3 = my_font_4.render(f"20", True, (43, 55, 74))
        screen.blit(score3, (280, 40))
        # --- Go  ahead and update the screen with what we've drawn.
        pygame.display.flip()
        for event in pygame.event.get():  # Checks all events
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:  # If the current event is the mouse button down event
                mouse_x, mouse_y = pygame.mouse.get_pos()  # Stores the mouse position
                print(mouse_x, mouse_y)
                if 122 <= mouse_x <= 544 and 314 <= mouse_y <= 356:
                    return True
                elif 155<=mouse_x<=192 and 35<=mouse_y<=68:
                    return 10
                elif 220<=mouse_x<=252 and 37<=mouse_y<=72:
                    return 15
                elif 279<=mouse_x<=311 and 38<=mouse_y<=70:
                    return 20

def menu():
    screen.fill((177, 213, 229))



    # MENU TEXT
    menu_title = my_font.render("WHACK-A-CLOUD", True, (66, 93, 133))
    screen.blit(menu_title, (15, 75))
    # play button
    pygame.draw.rect(screen, white,(265,180, 170, 50))
    button_play = my_font_2.render("PLAY", True, (43, 55, 74))
    screen.blit(button_play, (280, 180))
    # How to play button
    pygame.draw.rect(screen, white, (180, 250, 360, 60))
    button_how = my_font_2.render("How To play", True, (43, 55, 74))
    screen.blit(button_how, (200, 250))
    #Settings
    pygame.draw.rect(screen, white, (220, 325, 270, 60))
    button_how = my_font_2.render("Settings", True, (43, 55, 74))
    screen.blit(button_how, (240, 325))
    #Quit
    pygame.draw.rect(screen, white, (265, 400, 170, 50))
    button_quit = my_font_2.render("QUIT", True, (43, 55, 74))
    screen.blit(button_quit, ((width - 140) / 2, height / 2 + 150))
    pygame.display.flip()
check = True
num=20
while check!=False:
    menu()
    for event in pygame.event.get():  # Checks all events
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:  # If the current event is the mouse button down event
            mouse_x,mouse_y = pygame.mouse.get_pos()  # Stores the mouse position
            print(mouse_x,mouse_y)
            if 268<=mouse_x<=424 and 405<=mouse_y<=444:
                check=False
                break

            elif 274<=mouse_x<=428 and 185<=mouse_y<=225:
                if num!=True:
                    score,attempts = game_start(start,num)
                    clock.tick(120)
                check = endScreen(score,attempts)
            elif 184<=mouse_x<=533 and 258<=mouse_y<=301:
                check = HTM()
            elif 228<=mouse_x<=479 and 328<=mouse_y<=375:
                num = settings()


pygame.quit()


