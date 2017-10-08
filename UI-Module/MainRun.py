import sys
import os
import time

from Backend import *
from Tournament import *

class MainRun(object):
    """
    MainRun is the main menu and the class with the main() method.
    Its job is to present the user with initial options and forward 
    the user to the type of game he or she wants to play.
    """
    def __init__(self):
        """
        Construct a new 'MainRun' object.
        :param main_menu: True if the main menu is to be shown
        :param change_name: True if change name is to be shown
        :param start_game: True if start game menu is to bes shown
        :param quit: is to be true if quitting the game is wished
        :param Main(): starts the main loop
        """
        self.main_menu = True
        self.change_name = False
        self.start_game = False
        self.tournament = Tournament()
        self.quit_game = False
        self.Main()

    def set_main_menu(self):
        """
        Purpose is to draw main menu and give the use a choice of where to procced.
        :return: returns nothing
        """
        answer = self.tournament.ask_action("Main Menu \n\n"+
                                 "Your options: \n\n"+
                                 "[N] Change Player Name \n"+
                                 "[S] Start new game \n"+
                                 "[Q] Quit \n\n"+
                                "Please type a command and press enter:",["N","S","Q"])
        self.main_menu = False
        self.change_name = False
        self.start_game = False
        if answer == "n":
            self.change_name = True
        elif answer == "s":
            self.start_game = True  
        elif answer == "q":
            self.quit_game = True
            
    def set_change_name(self):
        """
        presents the user with a option to change his or hers name and save
        it for the entirity of the gaming session. returns the user to the main 
        menu afterwards
        :return: returns nothing.
        """
        print ("Change Player Name \n\n"+
               "Please enter a new name and then press enter to confirm. \n\n"+
               "New name:")
        answer = ""
        while not answer:
            answer = input()
            
        succes, msg = self.tournament.backend.setMainPlayerName(answer)
        if not succes:
            os.system('clear')  # on linux / os x 
            print (msg)
            self.set_change_name()
            
        self.main_menu = True
        self.change_name = False
        os.system('clear')  # on linux / os x
               
    def set_start_game(self):
        """
        Presents the player with the menu where he or she can start a new game in various forms.
        The player can also choose to return to the main menu or quit the game.
        :return: returns nothing.
        """
        answer = self.tournament.ask_action("Start new game \n\n"+
                                 "What type of game do you want to play? \n\n"+
                                 "[P] Player vs. Player \n"+
                                 "[C] Player vs. Computer \n"+
                                 "[T] Tournament \n"+
                                 "[B] Back \n"+
                                 "[Q] Quit\n\n"+
                                "Please type a command and press enter:",["P","C","T","B","Q"])
        self.main_menu = False
        self.change_name = False
        player1Name = self.tournament.backend.getPlayerName(1)

        if answer == "p":
            #TODO F: create a list of two players, including player1Name 
            pass
        elif answer == "c":
            difficulty = self.tournament.set_difficulty(False,1)
            tier = ["undef","Easy","Medium","Hard"]
            if difficulty:

                #Difficulty Easy
                if difficulty == 1:
                    #TODO F: Start a game with player1Name and AI 
                    pass
                #Difficulty Medium
                elif difficulty == 2:
                    #TODO F: Start a game with player1Name and AI 
                    pass
                #Difficulty Hard
                elif difficulty == 3:
                    #TODO F: Start a game with player1Name and AI 
                    pass

        elif answer == "t":
            self.quit_game = self.tournament.Main()
         
        elif answer == "b":
            self.start_game = False
            self.main_menu = True
       
        elif answer == "q":
            self.quit_game = True

        os.system('clear')  # on linux / os x
            
    def Main(self):
        """
        The main loop which initiates the main menu for the player. 
        He or she then got the possibilites to change his or her name, 
        start a new game or quit the seesion.
        :return: Returns nothing.
        """
        welcome_message = "Welcome to Tic-Tac-Toe. \nMenus are navigated by entering the key inside the [ ] on each alternative\n\n\n"
        print (welcome_message)
        while not self.quit_game:
            if self.main_menu:
                self.set_main_menu()
            if self.change_name:
                self.set_change_name()
            if self.start_game:
                self.set_start_game()
            pass
        os.system('clear')  # on linux / os x
        print("Sad to see you go!")

if  __name__ =='__main__':
    MainRun()
