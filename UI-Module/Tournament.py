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
        :param show_scoreboard: True if scoreboard is to be shown
        :param show_leaderboard: True if leaderboard is to be shown
        :param addNewPlayer: True if addNewPlayer is to be shown
        :param start_tournament: True if start tournament menu is to be shown
        :param back: is to be true if the user want to be back to the main menu
        :param quit: is to be true if quitting the game is wished
        :param Main(): starts the main loop
        """
        self.tournament = True
        self.show_scoreboard = False
        self.show_leaderboard = False
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


    def draw_scoreboard(self):
        """
        Draws the scoreboard for the players and menu options
        :return: nothing
        """
        answer = self.ask_action("Tournament - Scoreboard \n\n"+
                                 self.stringify_scoreboard()+
                                 "\n\n"+
                                 "[L] Show Leaderboard\n"+
                                 "[B] Back to next match\n"+
                                 "[Q] Quit\n")
        if answer == "l":
            self.show_scoreboard = False
            self.show_leaderboard = True
        elif answer == "b":
            self.start_tournament = True
        elif answer == "q":
            self.quit_game = True
        else:
            self.draw_scoreboard()


    def stringify_scoreboard(self):
        """
        Support function for draw_scoreboard. 
        Is supposed to create a string visualising the actual scoreboard.
        :return: A string containing the scoreboard
        """
        scoreboard  = self.backend.getScoreboard()
        player_list = self.backend.getListOfPlayerNames()
        result = "          | "
        
        for x in player_list:
            offset = 9-len(x)
            result += x + (" "*offset) + "| "

        count  = 0
        count2 = 0
        result += "\n"+"-"*(10*len(player_list))
        
        for x in player_list:
            offset = 10-len(x)
            result = result + "\n" + player_list[count] + (" "*offset) + "| "
            for x in player_list:
                if count2 == count:
                    result += "     x    |"
                elif scoreboard[count][0] == winner.undef:
                    result += "          |"
                elif count2 < count:
                    result += str(scoreboard[count][1]) + " |"                    
                else:
                    result += str(scoreboard[count][0]) + " |"                    
                count2 += 1
            count  = count+1
            count2 = 0
            
        return (result)

    
    def draw_leaderboard(self):
        """
        Draws the leaderboard and the associated menu options.
        :return:nothing.
        """
        answer = self.ask_action("Tournament - Leaderboard\n\n"+
                                 self.stringify_leaderboard()+
                                 "\n\n"+
                                 "[S] Show Scoreboard\n"+
                                 "[B] Back to next match\n"+
                                 "[Q] Quit\n")
        if answer == "s":
            self.show_scoreboard = False
            self.show_leaderboard = True
        elif answer == "b":
            self.start_tournament = True
        elif answer == "q":
            self.quit_game = True
        else:
            self.draw_leaderboard()


    def stringify_leaderboard(self):
        """
        support function for draw_leaderboard.
        Creates a string visualising the leaderboard.
        :return: A string containing the leaderboard.
        """
        leaderboard = self.backend.getLeaderboard()
        result = "          |   win    draws    losses    points\n"
        count = 0
        for x in leaderboard:
            #TODO: Fix spacing for a more aesthetically pleasing result...
            offset = 9-len(x)
            result += " " + str(x[0]) +" | " + str(x[1]) + (" "*offset) + "|"
            result += " " + str(x[1]) + "   "+str(x[2])+"    "+str(x[3])
            result += "\n"
            count += 1
        return (result)
        
            
    def start_tournament_show(self):
        """
        Draws the current tournament state with upcoming
        match and current alternativs.
        :return:nothing
        """
        self.backend.startTournament()
        a,b = self.backend.getNextMatch()
        answer = self.ask_action("Tournament - Next Match \n\nNext Match will be "+
                                 str(a)+
                                 " vs. "+
                                 str(b)+
                                 "\n\n"+
                                 "[M] Start match \n"+
                                 "[S] Show Scoreboard \n"+
                                 "[L] Show Leaderboard \n"+
                                 "[Q] Quit")
        if answer == "m":
            print("The new tournament game "+
                  str(a)+
                  " vs. "+
                  str(b)+
                  " is going to start.")
            time.sleep(10)
            os.system('clear')  # on linux / os x
            #TODO startMatch
            pass
        elif answer == "s":
            self.start_tournament = False
            self.show_scoreboard = True
        elif answer == "l":
            self.start_tournament = False
            self.show_leaderboard = True
        elif answer == "q":
            self.quit_game = True
        else:
            self.start_tournament.show()

        
    def tournament_menu(self):
        """
        Draw the main tournament menu and then give a choice of where to procced.
        Also displays which players are currently in the tournament.
        :return: returns nothing
        """
        can_start = (len(self.backend.getListOfPlayerNames()) > 1)
        no_player = len(self.backend.getListOfPlayerNames())
        no_games = "x" #TODO forgot if rematch was a thing
        print ("Tournament \n\n"+
               "Your options: \n\n"+
               "[A] Add New Player")
        if can_start:
               print ("[S] Start Tournament ("+
                      str(no_player)+
                      " players → "+
                      str(no_games)+
                      " games)")
               
        print ("[B] Back \n"+
               "[Q] Quit \n\n"+
               "Players in tournament so far:\n")
        print(*self.backend.getListOfPlayerNames(), sep='\n')
        

        
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
        else:
            self.tournament_menu()
        

        
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
                
            elif self.show_scoreboard:
                self.draw_scoreboard()
                
            elif self.show_leaderboard:
                self.draw_leaderboard()
                
            elif self.back:
                self.tournament = True
                self.back = False
                return False
            
        os.system('clear')  # on linux / os x
        self.quit_game = False
        return True
        
