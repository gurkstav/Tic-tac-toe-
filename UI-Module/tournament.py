import sys
import os
from backend import backend




class Main_Tournament(object):
    """
    Main_Tournament is the class that take care of the user with initial options and also forward the user to start tournament.
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
        self.quit = False
        self.Main()

        
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
        #os.system('cls')  # on windows
        os.system('clear')  # on linux / os x
        return answer[0]



    def tournament_menu(self):
        
        """
        Draw the main tournament menu and then give a choice of where to procced.
        :return: returns nothing
        """
        
        answer = self.ask_action("Tournament \n\nYour options: \n\n[A] Add New Player \n[B] Back \n[Q] Quit")
        self.tournament = False
        self.addNewPlayer = False
        
        if answer == "a":
            self.addNewPlayer = True
            
        elif answer == "b":
            self.back = True
          
        elif answer == "q":
            self.quit = True
        
    
    
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
        #os.system('cls')  # on windows
        os.system('clear')  # on linux / os x
        


class Tournament(object):
    
    """
    This tournament object will hold an object to start the tournament.
    Once another name has been filled in (add new player) the "start tournament" should appear. 
    The player can also choose to return to the main menu or quit the game.
    :return: returns nothing.
    """
    
    current_backend = backend()
    
    
    def set_players(self):
        
        
        self.addNewPlayer = 'Player1'
        self.player_list = [self.addNewPlayer]
        self.player_set = {self.addNewPlayer}
    
    
    
    def set_start_tournament(self):
        
        
        answer = self.ask_action("Tournament \n\nYour Options: \n\n[A] Add New Player \n[S] Start tournament \n[B] Back \n[Q] Quit")
        self.tournament = False
        self.addNewPlayer = False
        self.start_tournament = False
        if answer == "a":
        	
        	"""This print is just used to show current player list"""
        	print current_backend.getListOfPlayerNames()
        	
        	current_backend.addNewPlayerName(input("Please enter player's name"))
            
            """This print is just used to show player list after adding new one"""
            print current_backend.getListOfPlayerNames()
        
            self.tournament = True
            pass
            
        elif answer == "s":
            self.tournament = True
            pass
 
        elif answer == "b":
            self.tournament = True
            pass
            
        elif answer == "q":
            self.quit = True
            pass
        
        #os.system('cls')  # on windows
        os.system('clear')  # on linux / os x
        



        
    
    def Main(self):
        
        """
        The main loop that is taking care of the tournament menu for the player. 
        So that the player has possibilites to add his or her name and then start the tournament or quit the session.
        :return: Returns nothing.
        """
        
       
        while not self.quit:
            if self.tournament:
                self.tournament_menu()
            elif self.addNewPlayer:
                self.addNewPlayer_name()
            elif self.start_tournament:
                self.set_start_tournament()
            pass
        #os.system('cls')  # on windows
        os.system('clear')  # on linux / os x
        print("Sad to see you go!")

if  __name__ =='__main__':
    Tournament()
# Have to merge it to MainRun()
