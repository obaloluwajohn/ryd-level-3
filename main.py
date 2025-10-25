
# pygame boiler plate

import pygame
from pygame import draw, display

# Set up pygame window
pygame.init()
window = display.set_mode((800, 600))

# practising with arguments and properties

# variable definitions and assignment
tail = pygame.Rect(50,150,150,50)
backleg = pygame.Rect(210,150, 50, 200)
stomach = pygame.Rect(270,150,50,120)
frontleg = pygame.Rect(330,150,50,200)
neck = pygame.Rect(390,110,50,80)
head = pygame.Rect(450,80,90,65)
nose = pygame.Rect(510,100,60,45)
eye1 = pygame.Rect(465,90,10,10)
eye2 = pygame.Rect(495,90,10,10)

draw.rect(window,"blue",tail)
draw.rect(window, "blue", backleg)
draw.rect(window,"red",stomach)
draw.rect(window,"green",frontleg)
draw.rect(window,"red",neck)
draw.rect(window,"red",head)
draw.rect(window,"red",nose)
draw.rect(window,"black",eye1)
draw.rect(window,"black",eye2)

#  A sample of while loops to Update the display
while True:
  display.update()


