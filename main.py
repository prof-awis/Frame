# Simple pygame program
import frames

# Import and initialize the pygame library
import pygame
pygame.init()

# # importing os module 
# import os 
      
# self.index = 0


# Set up the drawing window
screen = pygame.display.set_mode([600, 700])

images=[]
frame = pygame.image.load("frames/1.png")

    

# images = [
#  pygame.image.load("frames/1.png"),
#  pygame.image.load("frames/2.png"),
#  pygame.image.load("frames/3.png"),
#  pygame.image.load("frames/4.png"),
#  pygame.image.load("frames/5.png"),
#  pygame.image.load("frames/6.png"),
#  pygame.image.load("frames/7.png"),
#  pygame.image.load("frames/8.png"),
#  pygame.image.load("frames/9.png")
# ]

# def animate(images, image_index):
#     image_index = increase_index()
#     images = frames[image_index]
#     screen.blit(images, (0,0))
x=0
y=0
screen.blit(frame, (x, y))

pygame.display.flip()
# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))
    # screen.blit(frame, (0, 0))
    


    # Flip the display
    

# Done! Time to quit.
pygame.quit()