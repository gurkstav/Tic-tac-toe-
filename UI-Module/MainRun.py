import sys
import os


class MainRun(object):
    def __init__(self):
        self.main_menu = True
        self.change_name = False
        self.quit = False

        self.Main()

    #
    def ask_action(self,prompt):
        answer = ""
        print(prompt)
        while not answer:
            answer = input()

        #os.system('cls')  # on windows
        os.system('clear')  # on linux / os x
        return answer[0]
        


    def Main(self):
        welcome_message = "Welcome to Tic-Tac-Toe. \nMenus are navigated by entering the key inside the [ ] on each alternative"
        print (welcome_message)
        while not self.quit:
            if self.main_menu:
                answer = self.ask_action("Change player name [N] \nStart new game [S] \n[Q]uit")
                if answer == "n":
                    #TODO
                    pass
                if answer == "s":
                    #TODO
                    pass
                if answer == "q":
                    self.quit = True
                pass
            pass
        #os.system('cls')  # on windows
        os.system('clear')  # on linux / os x
        print("Sad to see you go!")

if  __name__ =='__main__':
    MainRun()
