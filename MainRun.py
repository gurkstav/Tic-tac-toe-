import pygame
from Button import *

pygame.init()

"""
Window Resolution
"""
display_width  = 1024
display_height = 768
background_color = [255,255,0]
window = pygame.display.set_mode((display_width,display_height))

"""
Clock
"""
windowclock = pygame.time.Clock()

"""
Load other things such as images and sound files here
background = pygame.image.load("background.png").convert #Use conver_alpha() for images with transparency
"""

class MainRun(object):
    def __init__(self,display_width,display_height):
        self.display_width  = display_width
        self.display_height = display_height
        self.quit = False
        self.Main()

    def draw_main_menu(self,button_list):

        button_list.append(Button("start_pvc",display_width/4, (display_height/5)*1 , 500, 50, "placeholder_1.png"))
        button_list.append(Button("start_pvp",display_width/4, (display_height/5)*2 , 500, 50, "placeholder_2.png"))
        button_list.append(Button("start_trn",display_width/4, (display_height/5)*3 , 500, 50, "placeholder_3.png"))
        button_list.append(Button("Quit",display_width/4, (display_height/5)*4 , 500, 50, "placeholder.png"))
        for item in button_list:
            item.draw(window)

    def respond_event(self,button_list):
        for button in button_list:
            if button.click():
                if button.name == "start_pvc":
                    # TODO: Start the game here without names and agaisnt AI
                    pass
                if button.name == "start_pvp":
                    # TODO: start against another player - names not necessary?
                    pass
                if button.name == "start_trn":
                    # TODO: request redraw to tournamnet mode instead
                    pass
                if button.name == "Quit":
                    self.quit = True

                print(button.name)
                pass

    def Main(self):
        button_list = []
        
        window.fill((background_color[0],background_color[1],background_color[2]))
        self.draw_main_menu(button_list)

        while not self.quit:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.respond_event(button_list)

            """
            Remember to update clock....
            """
            pygame.display.update()
            windowclock.tick(60)

if  __name__ =='__main__':
    MainRun(display_width,display_height)
