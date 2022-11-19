# Import and initialize the pygame library
import pygame

from sys import exit

pygame.init()

clock = pygame.time.Clock()
# Set up the drawing window
screen = pygame.display.set_mode([600, 700])

# images=[]
frame = pygame.image.load("frames/1.png").convert
font = pygame.font.SysFont('arialblack', 20)

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
robot_surface = images[0]

#RObot image selection index
index = 0
run_animation = True

# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with color and add the images
    screen.fill((255, 255, 255))
    screen.blit(images, (0,332))
    
    # Drawing the buttonn and text written on it
    button = pygame.draw.rect(window, 'blue', (10, 10, 120, 50), 0, 10)
    draw_text('Animate', font, 'white', 23, 18)
    
    #Get mouse position
    mouse_pos = pygame.mouse.get_pos()
    
    #Check for collison of mouse with button
    #if button.collidepoint(mouse_pos)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP and button.collidepoint(event.pos):
            #run_animation = TRUE
            print('animation true')

# Done! Time to quit.
pygame.quit()