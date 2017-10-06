import sys
import os
import time

import gameplatform as g

from Backend import *
from Player import PlayerAI

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
                                 "[Q] Quit \n\n"+
                                "Please type a command and press enter:",["L","B","Q"])
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

        row  = 0
        column = 0
        result += "\n" + "─"*10

        #creates row under player names
        for x in player_list:
            result += "┼"
            if x != player_list[-1]:
                result += "─"*11
            else:
                result += "─"*11 + "┤"
        #traverses and creates each player row.
        for away in player_list:
            offset = 10-len(away)
            result = result + "\n" + player_list[row] + (" "*offset) + "│"
            for home in player_list:
                if row == column:
                    result += "     x     "
                elif scoreboard[column][row] == winner.undef:
                    result += "           "
                elif scoreboard[column][row] == winner.draw:
                    result +="    Draw   "
                #players home matches
                elif row < column:
                    if scoreboard[column][row] == winner.home:
                        result +=" " + away + (" "*(10-len(away)))
                    else:
                        result +=" " + home + (" "*(10-len(home)))
                #players away matches
                else:
                    if scoreboard[column][row] == winner.home:
                        result +=" " + home + (" "*(10-len(home)))
                    else:
                        result  +=" " + away + (" "*(10-len(away)))
                column += 1
                result += "│"
            row    = row+1
            column = 0
            
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
                                 "[Q] Quit\n\n"+
                                "Please type a command and press enter:",["S","B","Q"])
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
        
    def report_winner(self,home,away,result):
        if not result:
            self.backend.setMatchResult(winner.draw)
            
        elif result == home:
            self.backend.setMatchResult(winner.home)

        elif result == away:
            self.backend.setMatchResult(winner.away)
            
    def start_tournament_show(self):
        """
        Draws the current tournament state with upcoming
        match and current alternativs.
        :return:nothing
        """
        self.backend.startTournament(self.tournamnet_diff)
        a,b = self.backend.getNextMatch()
        print(a)
        print(b)
        ended = not a[0] and not b[0]
        if ended:
            winner = self.backend.getWinner()
            question = "All Games in this tournament have been played. Winner is " + winner + "\n\n"
            question += "\n\nCongratulations! \n\n[B] Back to Main Menu \n"
            alts = ["B","S","L","Q"]
        else:
            question = "Tournament - Next Match \n\nNext Match will be "
            question += str(a[0]) + " vs. " + str(b[0]) + "\n\n[M] Start match \n"
            alts = ["M","S","L","Q"]

        answer = self.ask_action(question +
                                 "[S] Show Scoreboard \n"+
                                 "[L] Show Leaderboard \n"+
                                 "[Q] Quit\n\n"+
                                "Please type a command and press enter:",alts)
        
        if answer == "m":
            print("The new tournament game "+
                  str(a[0])+
                  " vs. "+
                  str(b[0])+
                  " is going to start.")
         #   time.sleep(3)
            os.system('clear')  # on linux / os x
            players = self.backend.getListOfPlayerNames()
            
            if a[1] and b[1]:
                #BOTH AI, a[1] is 1-3 if AI, same for b[1]
                #winner = self.gameModule.start_game_AIAI(players,a[1],b[1])
                AIplayer1 = g.PlayerAI(a[0],True,a[1])
                AIplayer2 = g.PlayerAI(b[0],True,b[1])
                AIGame = g.AIGame(AIplayer1,AIplayer2)
                winner = AIGame.startGame()
                self.report_winner(a[0],b[0],winner)
                time.sleep(5)
                                 
            elif a[1]:
                #a = AI
                print("vs AI")
                #winner = self.gameModule.start_game_AI(players,a[1],b[1])
                AIplayer1 = g.PlayerAI(a[0],True,a[1])
                Playerone = g.PlayerAI(b[0],False,3)
                PvAIGame = g.AIGame(Playerone,AIplayer1)
                winner = PvAIGame.startGame()
                self.report_winner(b[0],a[0],winner)
                print("vs AI")
                time.sleep(5)                

            elif b[1]:
                #b = AI
                print("vs AI")
                Playerone = g.PlayerAI(a[0],False,3)
                AIplayer1 = g.PlayerAI(b[0],True,b[1])
                PvAIGame = g.AIGame(Playerone,AIplayer1)
                winner = PvAIGame.startGame()
                self.report_winner(a[0],b[0],winner)
                time.sleep(5)                
            else:
                print ("PVP")
                #TODO winner = self.gameModule.start_game(players)
                #TODO IF home or away (a or b)
                #TODO self.backend.setMatchResult(enum.winner)
                player1 = g.RealPlayer(a[0], 'X')
                player2 = g.RealPlayer(b[0], 'O')
                game = g.Game(player1, player2)
                winner = game.enter_game_loop()
                self.report_winner(a[0],b[0],winner)
                time.sleep(5)                
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
        
