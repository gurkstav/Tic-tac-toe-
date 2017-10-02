import sys
import os
import time

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
        """
        self.tournament = True
        self.addNewPlayer = False
        self.back = False
        self.start_tournament = False
        self.tournamnet_diff = 0
        self.quit_game = False
        self.backend = Backend()

        
    def ask_action(self,prompt, alts):
        """
        Purpose is to prompt the user a question and return a 
        single lowercase letter or number as a response.
        :param prompt: The question to the user
        :return: The first letter of the response
        """
        os.system('clear')  # on linux / os x
        print(prompt)
        answer = input()
        errorMSG = "Invalid input, acceptable: " + ", ".join(alts) + "\n" + prompt
        while True:
            while not answer:
                os.system('clear')  # on linux / os x
                print (errorMSG)
                answer = input()
    
            if answer[0].upper() not in alts:
                os.system('clear')  # on linux / os x
                print (errorMSG)
                answer = input()
            else:
                os.system('clear')  # on linux / os x
                return answer[0].lower()

    def set_difficulty(self,tournament,no_player):
        """
        Used to prompt player what difficulty he or she wants.
        :param tournament: A bool indicating if this is tournamnet difficulty
        :param no_player: int indicating how many players the difficulty adresses.
        :return: returns the difficulty in the range from 1-3. If back return value is False.
        """
        if tournament:
            question = "You have started a tournament with "
            question += str(no_player) + " human players and "
            question += str(8-no_player) + " AI players. Please select the maximum difficulty for the AI players. The difficulty of the AI players will be randomly assigned, but with an upper limit of your choice. \n\nMaximum AI difficulty:\n"
        else:
            question =  "Choose difficulty against Computer Player \n"
        question += "\n[1] Easy \n[2] Medium \n[3] Hard \n[B] Back"
        question += "\n\nPlease type a command and press enter:"
        answer = self.ask_action(question,["1","2","3","B"])
        if answer == "b":
            return False
        elif answer not in ("1","2","3"):
            self.set_difficulty()
        return int(answer)
            
    def tournament_menu(self):
        """
        Draw the main tournament menu and then give a choice of where to procced.
        Also displays which players are currently in the tournament.
        :return: returns nothing
        """
        can_start = (len(self.backend.getListOfPlayerNames()) > 1)
        no_player = len(self.backend.getListOfPlayerNames())
        """
        removed because tournamnet is to be filled with AI. 
        If not this calculates the number of games. 
        exldued code in "if can start" belongs to this issue
        """
        #no_games = no_player * no_player
        question = "Tournament \n\nYour options: \n\n[A] Add New Player\n"
        if can_start:
            # question += "[S] Start Tournament ("+str(no_player)
            # question += " players → "+str(no_games)+" games)\n"
            question += "[S] Start Tournament ("+str(no_player)
            question += " players → will be filled up with "+str(8-no_player)+" AI players)\n"

        question += "[B] Back \n[Q] Quit \n\nPlayers in tournament so far:\n"
        question += "\n".join(self.backend.getListOfPlayerNames()) + "\n"
        question += "\nPlease type a command and press enter:"
        if can_start:
            answer = self.ask_action(question,["A","S","B","Q"])
        else:
            answer = self.ask_action(question,["A","B","Q"])

        self.tournament = False
        self.addNewPlayer = False
        
        if answer == "a":
            self.addNewPlayer = True

        elif answer == "s":
            if no_player < 8 and not self.tournamnet_diff:
                """
                If ai is included a difficulty is needed for the opponents. 
                Main player chooses difficulty.
                """
                self.tournamnet_diff = self.set_difficulty(True,no_player)
            if self.tournamnet_diff:
                self.start_tournament = True
            else:
                self.tournament = True

            
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
        print ("Tournament - Add New Player \n\n"+
               "Please enter a new name and then press enter to confirm. \n\n"+
               "Player Name:")
        answer = ""
        while not answer:
            answer = input()
            self.tournament = True
            self.addNewPlayer = False

        succes, msg = self.backend.addNewPlayerName(answer)
        if not succes:
            os.system('clear')  # on linux / os x 
            print (msg)
            self.addNewPlayer_name()
            
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
                difficulty = self.tournamnet_diff
                player_list = self.backend.getListOfPlayerNames()
                self.start_tournament = False
                self.back = True
                #TODO group F GP
                #self.F_GP.startGame(player_list,difficulty)
                #TODO kill tournament object?
                self.backend.deletePlayerSet()
                
            elif self.back:
                self.tournament = True
                self.back = False
                return False
            
        os.system('clear')  # on linux / os x
        self.quit_game = False
        return True
        
