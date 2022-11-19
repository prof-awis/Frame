# Import and initialize the pygame library
import pygame
import time

pygame.init()

#set interval clock
clock = pygame.time.Clock()

# Set up the drawing window
window = pygame.display.set_mode([600, 700])

# images=[]
frame = pygame.image.load("frames/1.png")

 #the robot images  and the robot surface

images = [
 pygame.image.load("frames/1.png"),
 pygame.image.load("frames/2.png"),
 pygame.image.load("frames/3.png"),
 pygame.image.load("frames/4.png"),
 pygame.image.load("frames/5.png"),
 pygame.image.load("frames/6.png"),
 pygame.image.load("frames/7.png"),
 pygame.image.load("frames/8.png"),
 pygame.image.load("frames/9.png")
]
images2 = [
 pygame.image.load("frames/8.png"),
#  pygame.image.load("frames/9.png"),
 pygame.image.load("frames/7.png"),
 pygame.image.load("frames/6.png"),
 pygame.image.load("frames/5.png"),
 pygame.image.load("frames/4.png"),
 pygame.image.load("frames/3.png"),
 pygame.image.load("frames/2.png"),
 pygame.image.load("frames/1.png")
]           
# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
  
        
    for image in images:
        # pygame.image.load(image)
        time.sleep(0.3)
        window.blit(image, (0 ,0))
        pygame.display.flip()
        pygame.display.update()
        #overidding the image with a black background
        window.fill((0, 0, 0))
        
    for image in images2:
        # pygame.image.load(image)
        time.sleep(0.3)
        window.blit(image, (0 ,0))
        pygame.display.flip()
        pygame.display.update()
        #overidding the image with a black background
        window.fill((0, 0, 0))
        
    
  

    # Fill the background with color and add the images
    # window.fill((255, 255, 255))
    # window.blit(frame, (0, 0))
    

# Done! Time to quit.
pygame.quit()