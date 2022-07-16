# 1 - Import library
from ntpath import join
import time
import pygame
from pygame.locals import *
import pathlib
path = pathlib.Path().resolve()

# 2 - Initialize the game
pygame.init()
pygame.mixer.init()
width, height = 640*2, 480*2
SOUNDS = f'{path}/sounds'

screen=pygame.display.set_mode((width, height), pygame.RESIZABLE)


# 3 - Load images
# player = pygame.image.load("rgo.png")
pygame.font.init()

font = pygame.font.Font(None, int(screen.get_height()))
fontSmall = pygame.font.Font(None, 64)
text = font.render("O", True, (200,0,0), (0,0,0))


enteredText = []
summary = fontSmall.render("_", True, (200,0,0), (0,0,0))

def get_key(key):
    if key[pygame.K_a]:
        return 'a'
    if key[pygame.K_b]:
        return 'b'
    if key[pygame.K_c]:
        return 'c'
    if key[pygame.K_d]:
        return 'd'
    if key[pygame.K_e]:
        return 'e'
    if key[pygame.K_f]:
        return 'f'
    if key[pygame.K_g]:
        return 'g'
    if key[pygame.K_h]:
        return 'h'
    if key[pygame.K_i]:
        return 'i'
    if key[pygame.K_j]:
        return 'j'
    if key[pygame.K_k]:
        return 'k'
    if key[pygame.K_l]:
        return 'l'
    if key[pygame.K_m]:
        return 'm'
    if key[pygame.K_n]:
        return 'n'
    if key[pygame.K_o]:
        return 'o'
    if key[pygame.K_p]:
        return 'p'
    if key[pygame.K_q]:
        return 'q'
    if key[pygame.K_r]:
        return 'r'
    if key[pygame.K_s]:
        return 's'
    if key[pygame.K_t]:
        return 't'
    if key[pygame.K_u]:
        return 'u'
    if key[pygame.K_w]:
        return 'w'
    if key[pygame.K_x]:
        return 'x'
    if key[pygame.K_y]:
        return 'y'
    if key[pygame.K_v]:
        return 'v'
    if key[pygame.K_z]:
        return 'z'
    if key[pygame.K_1]:
        return '1'
    if key[pygame.K_2]:
        return '2'
    if key[pygame.K_3]:
        return '3'
    if key[pygame.K_4]:
        return '4'
    if key[pygame.K_5]:
        return '5'
    if key[pygame.K_6]:
        return '6'
    if key[pygame.K_7]:
        return '7'
    if key[pygame.K_8]:
        return '8'
    if key[pygame.K_9]:
        return '9'
    if key[pygame.K_0]:
        return '0'

# 4 - keep looping through
clock = pygame.time.Clock()
prev_key = ""

while 1:
    clock.tick(30)
    # 5 - clear the screen before drawing it again
    screen.fill(0)
    # 6 - draw the screen elements
    # screen.blit(player, (100,100))
    screen.blit(text, text.get_rect(center=(screen.get_width()/2, screen.get_height()/2)))
    screen.blit(summary, (32, screen.get_height()-64))
    pygame.display.flip()

    for event in pygame.event.get():
        # check if the event is the X button 
        if event.type==pygame.QUIT:
            # if it is quit the game
            print('Exit')
            pygame.quit() 
            exit(0) 

        if event.type == pygame.VIDEORESIZE:
            font = pygame.font.Font(None, int(screen.get_height()))
    
    
    keyPressed = pygame.key.get_pressed()
    
    if keyPressed[pygame.K_DELETE] or keyPressed[K_BACKSPACE]:
        if len(enteredText)>1:
            key = enteredText[-2]
            enteredText = enteredText[:-1]

        if len(enteredText) == 1:
            enteredText = []
            key = "_"
    key = get_key(keyPressed)

    if (key):
        if (len(enteredText) == 25):
            enteredText = []
        else:
            if (len(enteredText) > 0):
                if enteredText[-1] != key.upper():
                    enteredText.append(key.upper())
            else:
                enteredText.append(key.upper())

        text = font.render( key.upper(), True, (200,0,0), (0,0,0))

        if prev_key != key:
            prev_key = key
            sound = pygame.mixer.Sound( f'{SOUNDS}/{key}.ogg')
            sound.play()
        
        # prev_key = key

    summary = fontSmall.render( " ".join(enteredText)+"_", True, (200,0,0), (0,0,0))
        

