import sys
import os
from Backend import *

class Tournament(object):
    """
    Main_Tournament is the class that take care of the user with 
    initial options and also forward the user to start tournament.
    """
    def __init__(self):
        """
        'Main_Tournament' object.
        :param tournament: True if the tournament menu is to be shown
        :param addNewPlayer: True if addNewPlayer is to be shown
        :param start_tournament: True if start tournament menu is to be shown
        :param back: is to be true if the user want to be back to the main menu
        :param quit: is to be true if quitting the game is wished
        :param Main(): starts the main loop
        """
        self.tournament = True
        self.addNewPlayer = False
        self.start_tournament = False
        self.back = False
        self.quit_game = False
        self.backend = Backend()

        
    def ask_action(self,prompt):
        """
        Purpose is to prompt the user a question and return a 
        single lowercase letter or number as a response.
        :param prompt: The question to the user
        :return: The first letter of the response
        """
        answer = ""
        print(prompt)
        while not answer:
            answer = input()
        os.system('clear')  # on linux / os x
        return answer[0]


    def start_tournament_show(self):
        self.backend.startTournament()
        a,b = self.backend.getNextMatch()
        print ("Tournament - Next Match \n\nNext Match will be "+str(a)+" vs. "+str(b)+"\n\n[M] Start match \n[S] Show Scoreboard \n[S] Show Leaderboard \n[Q] Quit")
        answer = self.ask_action("")

        
        
    
    def print_players(self):
        player_list = self.backend.getListOfPlayerNames()
        print(*player_list, sep='\n')

        
    def tournament_menu(self):
        """
        Draw the main tournament menu and then give a choice of where to procced.
        :return: returns nothing
        """
        can_start = (len(self.backend.getListOfPlayerNames()) > 1)
        no_player = len(self.backend.getListOfPlayerNames())
        no_games = "x" #TODO forgot if rematch was a thing
        print ("Tournament \n\nYour options: \n\n[A] Add New Player")
        if can_start:
            print ("[S] Start Tournament ("+str(no_player)+" players → "+no_games+" games)")
        print ("[B] Back \n[Q] Quit \n\nPlayers in tournament so far:\n")
        self.print_players()

        
        answer = self.ask_action("")
        self.tournament = False
        self.addNewPlayer = False
        
        if answer == "a":
            self.addNewPlayer = True

        elif answer == "s" and can_start:
            self.start_tournament = True
            pass
            
        elif answer == "b":
            self.back = True
          
        elif answer == "q":
            self.quit_game = True

            
    def addNewPlayer_name(self):   
        """
        Presents the user with a option to add his or her name and save
        it for the entire tournament. It returns the user to the tournament menu
        :return: returns nothing.
        """ 
        
        print ("Tournament - Add New Player \n\nPlease enter a new name and then press enter to confirm. \n\nPlayer Name:")
        answer = ""
        while not answer:
            answer = input()
            self.tournament = True
            self.addNewPlayer = True
        self.backend.addNewPlayerName(answer)
        os.system('clear')  # on linux / os x        
        
    
    def Main(self):
        """
        The main loop that is taking care of the tournament menu for the player. 
        So that the player has possibilites to add his or her name and 
        then start the tournament or quit the session.
        :return: Returns nothing.
        """   
        while not self.quit_game:
            if self.tournament:
                self.tournament_menu()
            elif self.addNewPlayer:
                self.addNewPlayer_name()
            elif self.start_tournament:
                self.start_tournament_show()
            elif self.back:
                self.tournament = True
                self.back = False
                return False
        os.system('clear')  # on linux / os x
        self.quit_game = False
        return True
        
