import sys
import os


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
        print ("\033c") #Unknown compability but should work on most bash, if windows, please test
        return answer[0]




    
    def set_main_menu(self):
        """
        Purpose is to draw main menu and give the use a choice of where to procced.
        :return: returns nothing
        """
        answer = self.ask_action("Main Menu \n\nYour options: \n\n[N] Change Player Name \n[S] Start new game \n[Q] Quit")
        self.main_menu = False
        self.change_name = False
        self.start_game = False
        if answer == "n":
            self.change_name = True
            
        elif answer == "s":
            self.start_game = True
          
        elif answer == "q":
            self.quit = True




            
    def set_change_name(self):
        """
        presents the user with a option to change his or hers name and save
        it for the entirity of the gaming session. returns the user to the main 
        menu afterwards
        :return: returns nothing.
        """
        print ("Change Player Name \n\nPlease enter a new name and then press enter to confirm. \n\nNew name:")
        answer = ""
        while not answer:
            answer = input()
        #TODO: someModule.set_new_player_name(answer)
        self.main_menu = True
        self.change_name = False
        #os.system('cls')  # on windows
        #os.system('clear')  # on linux / os x
        print ("\033c") #Unknown compability but should work on most bash, if windows, please test




        
    def set_start_game(self):
        """
        Presents the player with the menu where he or she can start a new game in various forms.
        The player can also choose to return to the main menu or quit the game.
        :return: returns nothing.
        """
        answer = self.ask_action("Start new game \n\nWhat type of game do you want to play? \n\n[P] Player vs. Player \n[C] Player vs. Computer \n[T] Tournament \n[B] Back \n[Q] Quit")
        self.main_menu = False
        self.change_name = False
        self.start_game = False
        if answer == "p":
            #TODO: player1 = somemodule.get_player_name()
            #TODO: gameModule.start_game(player1, "Player2")
            self.main_menu = True
            pass
        elif answer == "c":
            #TODO: player1 = somemodule.get_player_name()
            #TODO: gameModule.start_game_ai(player1)
            self.main_menu = True
            pass
        elif answer == "t":
            #TODO: player1 = somemodule.get_player_name()
            #TODO: tournament_class.start_tournament_ui( player1 )
            self.main_menu = True
            pass
        elif answer == "b":
            self.main_menu = True
            pass
        elif answer == "q":
            self.quit = True
            pass
        
        #os.system('cls')  # on windows
        #os.system('clear')  # on linux / os x
        print ("\033c") #Unknown compability but should work on most bash, if windows, please test



        
    
    def Main(self):
        """
        The main loop which initiates the main menu for the player. 
        He or she then got the possibilites to change his or her name, 
        start a new game or quit the seesion.
        :return: Returns nothing.
        """
        print ("\033c") #Unknown compability but should work on most bash, if windows, please test
        welcome_message = "Welcome to Tic-Tac-Toe. \nMenus are navigated by entering the key inside the [ ] on each alternative\n\n\n"
        print (welcome_message)
        while not self.quit:
            if self.main_menu:
                self.set_main_menu()
            if self.change_name:
                self.set_change_name()
            if self.start_game:
                self.set_start_game()
            pass
        #os.system('cls')  # on windows
        #os.system('clear')  # on linux / os x
        print ("\033c") #Unknown compability but should work on most bash, if windows, please test
        print("Sad to see you go!")

if  __name__ =='__main__':
    MainRun()
