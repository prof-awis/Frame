import pygame


# initializing the constructor
pygame.init()

# screen resolution
res = (600,700)

# opens up a window
screen = pygame.display.set_mode(res)

#loads the first image on the window
frame = pygame.image.load("frames/1.png")
image = pygame.transform.scale(frame, (300, 600))
screen.blit(image, (150 ,50))
pygame.display.flip()
pygame.display.update()


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
text = smallfont.render('Quit' , True , color)


while True:
	
	for ev in pygame.event.get():
		
		if ev.type == pygame.QUIT:
			pygame.quit()
   	
			
		#checks if a mouse is clicked
		if ev.type == pygame.MOUSEBUTTONDOWN:
			
			#if the mouse is clicked on the
			# button the game is terminated
			if 500 <= mouse[0] <= 400 and 500 <= mouse[1] <= 400:
				pygame.quit()
		
											
	# fills the screen with a color
	# screen.fill((60,25,60))
	
	# stores the (x,y) coordinates into
	# the variable as a tuple
	mouse = pygame.mouse.get_pos()
	
	# if mouse is hovered on a button it
	# changes to lighter shade
	if 500 <= mouse[0] <= 400 and 500 <= mouse[1] <= 400:
		pygame.draw.rect(screen,color_light,[500,400,140,40])
		
	else:
		pygame.draw.rect(screen,color_dark,[500,400,140,40])
	
	# superimposing the text onto our button
	screen.blit(text , (width/2+25,height/2+10))
	
	# updates the frames of the game
	pygame.display.update()
