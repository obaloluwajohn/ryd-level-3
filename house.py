
# pygame boiler plate

import pygame
from pygame import draw, display

# Set up pygame window
pygame.init()
window = display.set_mode((800, 600))

# practising with arguments and properties

# variable definitions and assignment
house = pygame.Rect(150,150,500,400)


draw.rect(window,"blue",house)


#  A sample of while loops to Update the display
while True:
  display.update()


