import pygame
import sys
import time

from loopingFrames import *

def	 animate():
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
					loopingFrames()
												
												
		# fills the screen with a color
		screen.fill((255,255,0))
		
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
