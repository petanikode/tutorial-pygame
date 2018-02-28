# 1 - Import Library ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import pygame
from pygame.locals import *

# 2 - Initialize the Game ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))

running = True

playerpos = [100, 100] # initial position for player

# 3 - Load Game Assets ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3.1 - Load Images
player = pygame.image.load("resources/images/dude.png")
grass = pygame.image.load("resources/images/grass.png")
castle = pygame.image.load("resources/images/castle.png")

## 4 - The Game Loop ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
while(running):
    
    # 5 - Clear the screen ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    screen.fill(0)
    
    # 6 - Draw the game object ~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # draw the grass
    for x in range(int(width/grass.get_width()+1)):
        for y in range(int(height/grass.get_height()+1)):
            screen.blit(grass, (x*100, y*100))
	
	# draw the castle
    screen.blit(castle, (0, 30))
    screen.blit(castle, (0, 135))
    screen.blit(castle, (0, 240))
    screen.blit(castle, (0, 345))

    screen.blit(player, playerpos)

    # 7 - Update the sceeen ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    pygame.display.flip()

    # 8 - Event Loop ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    for event in pygame.event.get():
        # event saat tombol exit diklik
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)