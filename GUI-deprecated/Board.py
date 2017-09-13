from Button import *

class Board:
    def __init__(self,players_list,display_width,display_height,surface):
        self.pieces_list = list()
        self.players_list = players_list
        self.background_image = "placeholder/background.jpg"
        self.display_width = display_width
        self.display_height = display_height
        import pygame
        self.pg = pygame
        self.surface = surface

    def draw(self):
        background = self.pg.image.load(self.background_image).convert()
        background = self.pg.transform.scale(background, (self.display_width, self.display_width))
        self.surface.blit(background, (0, 0))
        self.draw_player_name(0)

        #To be removed later
        b = Button("Quit",self.display_width/4, (self.display_height/5)*4 , 500, 50, "placeholder/placeholder.png")
        b.draw(self.surface)

    def draw_player_name(self,player_no):
        font = self.pg.font.SysFont("arial", 72)
        size = font.size(self.players_list[0].name)
        label = font.render(self.players_list[player_no].name, True, (135,206,250))
        self.surface.blit(label, ((self.display_width/2) - (size[0]/2), 25))
