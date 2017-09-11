import pygame
from Button import *

pygame.init()

#Window Resolution
display_width  = 1024
display_height = 768
background_color = [255,255,0]
window = pygame.display.set_mode((display_width,display_height))

#Clock
windowclock = pygame.time.Clock()

#Load other things such as images and sound files here
#background = pygame.image.load("background.png").convert #Use conver_alpha() for images with transparency


class MainRun(object):
    def __init__(self,display_width,display_height):
        self.display_width  = display_width
        self.display_height = display_height
        self.Main()

    def Main(self):
        quit = False

        window.fill((background_color[0],background_color[1],background_color[2]))

        button_list = []
        button_list.append(Button("Quit",display_width/2.25, display_height/4, 50, 50, "placeholder.png"))
        button_list[0].draw(window)

        while not quit:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    window.fill((255,255,255)) #Tuple for filling display... Current is white
                    quit = True

            #Remember to update your clock and display at the end
            pygame.display.update()
            windowclock.tick(60)




if  __name__ =='__main__':
    MainRun(display_width,display_height)
