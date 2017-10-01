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
        self.end_tournament = False
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
                                 "[Q] Quit\n",["L","B","Q"])
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
        result = "          │"
        
        for x in player_list:
            offset = 10-len(x)
            result += " " + x + (" "*offset) + "│"

        count  = 0
        count2 = 0
        result += "\n" + "─"*10

        for x in player_list:
            result += "┼"
            if x != player_list[-1]:
                result += "─"*11
            else:
                result += "─"*11 + "┤"
        for x in player_list:
            offset = 10-len(x)
            result = result + "\n" + player_list[count] + (" "*offset) + "│"
            for x2 in player_list:
                if count2 == count:
                    result += "     x     "
                elif scoreboard[count][0] == winner.undef:
                    result += "           "
                elif count2 < count:
                    if scoreboard[count][1] == winner.draw:
                        result +="    Draw   "
                    elif scoreboard[count][1] == winner.home:
                        result +=" " + x + (" "*(10-len(x)))
                    else:
                        result +=" " + x2 + (" "*(10-len(x2)))
                else:
                    if scoreboard[count][1] == winner.draw:
                        result +="    Draw   "
                    elif scoreboard[count][0] == winner.home:
                        result +=" " + x + (" "*(10-len(x)))
                    else:
                        result  +=" " + x2 + (" "*(10-len(x2)))
                count2 += 1
                result += "│"
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
                                 "[Q] Quit\n",["S","B","Q"])
        if answer == "s":
            self.show_scoreboard = True
            self.show_leaderboard = False
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
        result = "  │           │   win    draws    losses    points\n"
        count = 0
        for x in leaderboard:
            offset = 10-len(x[0])
            result += str(count+1) + " │"
            result += " " + x[0] + (" "*offset) + "│"
            result += "    " + str(x[1])
            result += "       " + str(x[2])
            result += "        " + str(x[3])
            result += "         " + str(x[4])
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
        ended = not a and not b
        if ended:
            winner = self.backend.getWinner()
            question += "All Games in this tournament have been played. Winner is " + winner + "\n\n"
            question += "\n\nCongratulations! \n\n[B] Back to Main Menu \n"
            alts = ["B","S","L","Q"]
        else:
            question += "Tournament - Next Match \n\nNext Match will be "
            question += str(a) + " vs. " + str(b) + "\n\n[M] Start match \n"
            alts = ["M","S","L","Q"]

        answer = self.ask_action(question +
                                 "[S] Show Scoreboard \n"+
                                 "[L] Show Leaderboard \n"+
                                 "[Q] Quit",alts)
        
        if answer == "m":
            print("The new tournament game "+
                  str(a)+
                  " vs. "+
                  str(b)+
                  " is going to start.")
            time.sleep(10)
            os.system('clear')  # on linux / os x
            #TODO startMatch
            #TODO setMatchResult(enum.winner)
            
            pass
        elif answer == "b":
            self.end_tournament = True
            self.start_tournament = False
            self.back = True
            pass
        elif answer == "s":
            self.start_tournament = False
            self.show_scoreboard  = True
        elif answer == "l":
            self.start_tournament = False
            self.show_leaderboard = True
        elif answer == "q":
            self.quit_game = True
        
    def tournament_menu(self):
        """
        Draw the main tournament menu and then give a choice of where to procced.
        Also displays which players are currently in the tournament.
        :return: returns nothing
        """
        can_start = (len(self.backend.getListOfPlayerNames()) > 1)
        no_player = len(self.backend.getListOfPlayerNames())
        no_games = no_player * no_player
        question = "Tournament \n\nYour options: \n\n[A] Add New Player\n"
        if can_start:
            question += "[S] Start Tournament ("+str(no_player)+" players → "+str(no_games)+" games)\n"              
        question += "[B] Back \n[Q] Quit \n\nPlayers in tournament so far:\n"
        question += "\n".join(self.backend.getListOfPlayerNames()) + "\n"

        if can_start:
            answer = self.ask_action(question,["A","S","B","Q"])
        else:
            answer = self.ask_action(question,["A","B","Q"])
        self.tournament = False
        self.addNewPlayer = False
        
        if answer == "a":
            self.addNewPlayer = True

        elif answer == "s":
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
                self.start_tournament_show()
                
            elif self.show_scoreboard:
                self.draw_scoreboard()
                
            elif self.show_leaderboard:
                self.draw_leaderboard()
                
            elif self.back:
                if self.end_tournament:
                    self.backend.endTournament()
                self.tournament = True
                self.back = False
                return False
            
        os.system('clear')  # on linux / os x
        self.quit_game = False
        return True
        
