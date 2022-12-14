import pygame

from loopingFrames import *
pygame.init()
screen = pygame.display.set_mode((600, 700))

#loads the first image on the window
frame = pygame.image.load("frames/1.png")
image = pygame.transform.scale(frame, (300, 600))
screen.blit(image, (150 ,50))
pygame.display.flip()
pygame.display.update()

clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 20)


class Button2:
    """Create a button, then blit the surface in the while loop"""

    def __init__(self, text,  pos, font, bg="yellow", feedback=""):
        self.x, self.y = pos
        self.font = pygame.font.SysFont("Arial", font)
        if feedback == "":
            self.feedback = "text"
        else:
            self.feedback = feedback
        self.change_text(text, bg)

    def change_text(self, text, bg="black"):
        """Change the text when you click"""
        self.text = self.font.render(text, 1, pygame.Color("White"))
        self.size = self.text.get_size()
        self.surface = pygame.Surface(self.size)
        self.surface.fill(bg)
        self.surface.blit(self.text, (0, 0))
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])

    def show(self):
        screen.blit(button2.surface, (self.x, self.y))

    def click(self, event):
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if self.rect.collidepoint(x, y):
                    # loopingFrames()
                    pygame.quit()
                    self.change_text(self.feedback, bg="red")
                    
                    


def mainloop():
    """ The infinite loop where things happen """
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            button2.click(event)
        button2.show()
        clock.tick(30)
        pygame.display.update()


button2 = Button2(
    "Quit",
    (50, 600),
    font=30,
    bg="navy",
    feedback="Quit Game")

mainloop() 