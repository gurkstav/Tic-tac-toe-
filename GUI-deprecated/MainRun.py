import pygame
from Button import *
from Player import *
from Board import *

class MainRun(object):
    def __init__(self):
        self.display_width  = 1024
        self.display_height = 768
        self.background_image = "placeholder/background.jpg"
        self.quit = False
        import pygame
        self.pg = pygame
        pygame.init()
        self.window = pygame.display.set_mode((self.display_width,self.display_height))
        self.Main()

    def draw_game_plattform(self,players_list):
        self.window.fill((0,0,0))
        game_board = Board(players_list,self.display_width,self.display_height,self.window)
        game_board.draw()

    def draw_main_menu(self,button_list):
        self.window.fill((0,0,0))
        background = pygame.image.load(self.background_image).convert()
        background = pygame.transform.scale(background, (self.display_width, self.display_width))
        self.window.blit(background, (0, 0))

        button_list.append(Button("start_pvc",self.display_width/4, (self.display_height/5)*1 , 500, 50, "placeholder/placeholder_1.png"))
        button_list.append(Button("start_pvp",self.display_width/4, (self.display_height/5)*2 , 500, 50, "placeholder/placeholder_2.png"))
        button_list.append(Button("start_trn",self.display_width/4, (self.display_height/5)*3 , 500, 50, "placeholder/placeholder_3.png"))
        button_list.append(Button("Quit",self.display_width/4, (self.display_height/5)*4 , 500, 50, "placeholder/placeholder.png"))
        for item in button_list:
            item.draw(self.window)

    def respond_event(self,button_list):
        for button in button_list:
            if button.click():
                if button.name == "start_pvc":
                    # TODO: Start the game here without names and agaisnt AI
                    players_list = []
                    players_list.append(Player("Player",False,0))
                    players_list.append(Player("Computer",True,0))
                    self.draw_game_plattform(players_list)
                    pass
                if button.name == "start_pvp":
                    # TODO: start against another player - names not necessary?
                    players_list = []
                    players_list.append(Player("Player 1",False,0))
                    players_list.append(Player("Player 2",True,0))
                    self.draw_game_plattform(players_list)
                    pass
                if button.name == "start_trn":
                    # TODO: request redraw to tournamnet mode instead
                    pass
                if button.name == "Quit":
                    self.quit = True

                print(button.name)
                pass


    def Main(self):
        #Clock
        windowclock = pygame.time.Clock()

        button_list = []
        self.draw_main_menu(button_list)

        while not self.quit:
            for event in self.pg.event.get():
                if event.type == self.pg.MOUSEBUTTONDOWN:
                    self.respond_event(button_list)

            #Remember to update clock....
            self.pg.display.update()
            windowclock.tick(60)

if  __name__ =='__main__':
    MainRun()
