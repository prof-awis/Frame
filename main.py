# Import and initialize the pygame library
import pygame
import time

from animate import *
from loopingFrames import *

pygame.init()

animate()
loopingFrames()

# Done! Time to quit.
pygame.quit()