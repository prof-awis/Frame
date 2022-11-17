# Simple pygame program
import frames

# Import and initialize the pygame library
import pygame
pygame.init()

# # importing os module 
# import os 
      
self.index = 0


# Set up the drawing window
screen = pygame.display.set_mode([600, 700])

# images=[]
# for num in range(9):
#     image = pygame.image.load(os.getcwd() + f'/frames/{num + 1}.png')
#     images.append(image)
    
    
#  def update(self):
#      self.index += 1


    
   

# frame = pygame.image.load("frames/1.png")
# frame = pygame.image.load("frames/2.png")
# frame = pygame.image.load("frames/3.png")
# frame = pygame.image.load("frames/4.png")
# frame = pygame.image.load("frames/5.png")
# frame = pygame.image.load("frames/6.png")
# frame = pygame.image.load("frames/7.png")
# frame = pygame.image.load("frames/8.png")
# frame = pygame.image.load("frames/9.png")

# x=0
# y=0
# screen.blit(frame, (x, y))

# pygame.display.flip()
# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))


    # Flip the display
    

# Done! Time to quit.
pygame.quit()