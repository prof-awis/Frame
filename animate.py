import pygame
import sys
import time

# from main import *


# initializing the constructor
pygame.init()

# screen resolution
res = (600,700)

# opens up a window
screen = pygame.display.set_mode(res)

# white color
color = (255,255,255)

# light shade of the button
color_light = (170,170,170)

# dark shade of the button
color_dark = (100,100,100)

# stores the width of the
# screen into a variable
width = screen.get_width()

# stores the height of the
# screen into a variable
height = screen.get_height()

# defining a font
smallfont = pygame.font.SysFont('Corbel',35)

# rendering a text written in
# this font
text = smallfont.render('Animate' , True , color)

while True:
	
	for ev in pygame.event.get():
		
		if ev.type == pygame.QUIT:
			pygame.quit()
			
		#checks if a mouse is clicked
		if ev.type == pygame.MOUSEBUTTONDOWN:
			
			#if the mouse is clicked on the
			# button the game is terminated
			if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:
				# pygame.quit()
				# Set up the drawing window
							clock = pygame.time.Clock()

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
										
							
									
								for image in images:
									# scaling image to whatever size you'd like
									image = pygame.transform.scale(image, (300, 600))
									# pygame.image.load(image)
									time.sleep(0.3)
									window.blit(image, (150 ,50))
									pygame.display.flip()
									pygame.display.update()
									#overidding the image with a black background
									window.fill((0, 0, 0))
									
								for image in images2:
									# scaling image to whatever size you'd like
									image = pygame.transform.scale(image, (300, 600))
									# pygame.image.load(image)
									time.sleep(0.3)
									window.blit(image, (150 ,50))
									pygame.display.flip()
									pygame.display.update()
									#overidding the image with a black background
									window.fill((0, 0, 0))
										

							# Done! Time to quit.
							# pygame.quit()
											
											
	# fills the screen with a color
	screen.fill((60,25,60))
	
	# stores the (x,y) coordinates into
	# the variable as a tuple
	mouse = pygame.mouse.get_pos()
	
	# if mouse is hovered on a button it
	# changes to lighter shade
	if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:
		pygame.draw.rect(screen,color_light,[width/2,height/2,140,40])
		
	else:
		pygame.draw.rect(screen,color_dark,[width/2,height/2,140,40])
	
	# superimposing the text onto our button
	screen.blit(text , (width/2+25,height/2+10))
	
	# updates the frames of the game
	pygame.display.update()
