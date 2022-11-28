import pygame
import time


def loopingFrames():
    #set interval clock
    clock = pygame.time.Clock()

    # Set up the drawing window
    window = pygame.display.set_mode([600, 700])

    # frame = pygame.image.load("frames/1.png").convert_alpha()
    # small_frame = pygame.transform.scale(frame, (200, 500))


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
    pygame.image.load("frames/9.png"),
    pygame.image.load("frames/8.png"),
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
                pygame.quit()
                
    
            
        for image in images:
            # scaling image to whatever size you'd like
            image = pygame.transform.scale(image, (300, 600))
            # pygame.image.load(image)
            clock.tick(7)
            window.blit(image, (150 ,50))
            pygame.display.flip()
            pygame.display.update()
            #overidding the image with a black background
            window.fill((0, 0, 0))
            
        for image in images2:
            # scaling image to whatever size you'd like
            image = pygame.transform.scale(image, (300, 600))
            # pygame.image.load(image)
            clock.tick(7)
            window.blit(image, (150 ,50))
            pygame.display.flip()
            pygame.display.update()
            #overidding the image with a black background
            window.fill((0, 0, 0))
                
