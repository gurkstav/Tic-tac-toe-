from __future__ import print_function
import random
import os

class game_engine(object):
  """A class to handle gamming process."""

  def __init__(self):
    """
    Initial setting of current game:
    end_game: True when have a winner, False for no or not yet.
    current_OX: 0 means have not been place thing, 1 means O and -1 means X.
    first_put: let user define wheather to play first (1) or not (0), 
      default is play first.
    user_use: let user choose symbolic, O (1) or X (0), default is O.
    win_line: to recode which line win in block level.
    winner: player win is 1, computer win is -1 and draw is the same as default 0.
    """
    self.current_OX = 9*[0]
    self.end_game = False
    self.first_put = 1
    self.X = -1
    self.O = 1
    self.user_use = self.O
    self.win_line = [-1,-1,-1]
    self.winner = 0

  def _be_first(self,user_or_cpu):
    """This part will be connected to GUI in the future"""
    if user_or_cpu.lower() == "y":
      self.first_put = 1
    elif user_or_cpu.lower() =="n":
      self.first_put = 0
    else:
      pass

  def _change_use(self,X_or_O):
    """This part will be connected to GUI in the future"""
    if X_or_O.lower() == "o":
      self.user_use = self.O
    elif X_or_O.lower() == "x":
      self.user_use = self.X
    else:
      pass

  def _assign_value(self,place):
    """Assign user's desicion"""
    try:
      place = int(place) - 1
      if self.current_OX[place] != 0:
        self._assign_value(raw_input("Already exsits! Choose again:"))

      else:
        if self.user_use == self.O:
          self.current_OX[place] = self.O
        else:
          self.current_OX[place] = self.X
    except:
      self._assign_value(raw_input("Out of range or invalid input! Choose again:"))

  def _win_line_recode(self,end_flag,who_win,which_line):
    self.end_game = end_flag
    self.winner = who_win
    self.win_line = which_line

  def _reshape_to_matrix(self):
    OX_matrix = []
    current_row = []
    for x in range(len(self.current_OX)):
      current_row.append(self.current_OX[x])
      if (x+1) % 3 == 0:
        OX_matrix.append(current_row)
        current_row = []
    return OX_matrix

  def _diag_left_down(self,matix):
    line_sum = 0
    for x in range(3):
      line_sum = matix[x][2-x] + line_sum
    return line_sum

  def _diag_right_down(self,matix):
    line_sum = 0
    for x in range(3):
      line_sum = matix[x][x] + line_sum
    return line_sum

  def _row_count(self,matix,row):
    line_sum = 0
    for x in range(3):
      line_sum = matix[row][x] + line_sum
    return line_sum

  def _column_count(self,matix,col):
    line_sum = 0
    for x in range(3):
      line_sum = matix[x][col] + line_sum
    return line_sum

  def _compute_output(self):
    """
    Compute wheather the game is over by end_game flag.
    Record winner and win_line if the match is not draw. 
    (If needed, here can add a function to execute early stop before end in draw)
    """
    if self.current_OX.count(0) == 0:
      self.end_game = True      
    
    current_OX_matrix = self._reshape_to_matrix()

    if self._diag_right_down(current_OX_matrix) == (3*self.O):
      self._win_line_recode(True,self.O,[0,4,8])
    elif self._diag_right_down(current_OX_matrix) == (3*self.X):
      self._win_line_recode(True,self.X,[0,4,8])
    elif self._diag_left_down(current_OX_matrix) == (3*self.O):
      self._win_line_recode(True,self.O,[2,4,6])
    elif self._diag_left_down(current_OX_matrix) == (3*self.X):
      self._win_line_recode(True,self.X,[2,4,6])

    for x in range(3):
      if self._row_count(current_OX_matrix,x) == (3*self.O):
        self._win_line_recode(True,self.O,[3*x,3*x+1,3*x+2])
      elif self._row_count(current_OX_matrix,x) == (3*self.X):
        self._win_line_recode(True,self.X,[3*x,3*x+1,3*x+2])
      elif self._column_count(current_OX_matrix,x) == (3*self.O):
        self._win_line_recode(True,self.O,[x,x+3,x+6])
      elif self._column_count(current_OX_matrix,x) == (3*self.X):
        self._win_line_recode(True,self.X,[x,x+3,x+6])
    return self.end_game
    
  def show_game(self):
    """This part will be replaced to GUI in the future"""
    
    show_up_list = []
    for x in range(len(self.current_OX)):
      if self.current_OX[x] == self.X:
        show_up_list.append(" X ")
      elif self.current_OX[x] == self.O:
        show_up_list.append(" O ")
      else:
        show_up_list.append("   ")

      if x != len(self.current_OX)-1:
        if x % 3==2:
          show_up_list.append("\n-----------\n")
        else:
          show_up_list.append("|")
    return show_up_list
  
  def display_result(self):
    """This part will be raplaced to GUI"""
    
    """Summary of result"""
    if self.winner is self.user_use:
      print('\033[1;31m' + "You win!" + '\033[0m')
    elif self.winner != 0:
      print("CPU win!")
    
    """Highlight the line"""
    for x in range(len(self.current_OX)):
      if x in self.win_line:
        if self.current_OX[x] == self.X:
          print('\033[1;31m' + " X " + '\033[0m',end="")
        elif self.current_OX[x] == self.O:
          print('\033[1;31m' + " O " + '\033[0m',end="")
      
      else:
        if self.current_OX[x] == self.X:
          print(" X ",end="")
        elif self.current_OX[x] == self.O:
          print(" O ",end="")
        else:
          print("   ",end="")
      
      if x != len(self.current_OX)-1:
        if x % 3==2:
          print("\n-----------\n",end="")
        else:
          print("|",end="")
    print()

  def cpu_put(self):
    """Here only apply random seletion, we can develop some fancy strategy in the future"""
    cpu_select_set = []
    for element in self.current_OX:
      if element == 0:
        cpu_select_set.append(self.current_OX.index(element))
    cpu_select_place = (random.choice(cpu_select_set))
    
    if self.user_use == self.O:
      self.current_OX[cpu_select_place] = self.X
    else:
      self.current_OX[cpu_select_place] = self.O
  
  def _intro(self):
    """A basic tutorial of how to playing tic-tac-toe"""
    for x in range(len(self.current_OX)):
      print("",x+1,"",end="")
      if x != len(self.current_OX)-1:
        if x % 3==2:
          print("\n-----------\n",end="")
        else:
          print("|",end="")
    print()

  def play(self):
    """The whole section will be replaced so as to connect to GUI"""

    self._be_first(raw_input("Do you want to play first? \
      \n(\"y\" for yes or \"n\" for no, default is y, other input will be ingored) "))
    
    self._change_use(raw_input("Which symbolic you want to use? \
      \n(\"o\" for O or \"x\" for X, default is O, other input will be ingored) "))
    
    print("Enter the number to put your symbolic")
    self._intro()
    
    raw_input("Now press Enter to start the game!")
    os.system('clear')

    if self.first_put == 1:
      print('\033[1;34m' + "Your turn" + '\033[0m ')
      for block in self.show_game():
        print(block,end="")


      while(True):
        self._assign_value(raw_input())
        if (self._compute_output()):
          os.system('clear')
          if self.winner == self.user_use:
            self.display_result()
          else: 
            os.system('clear')
            print("Draw")
            for block in self.show_game():
              print(block,end="")
            
          break

        else:
          for block in self.show_game():
            print(block,end="")
          
          os.system('clear')
        print("CPU turn")
        
        if not self._compute_output():
          self.cpu_put()
          if self._compute_output():
            if self.winner == 0:
              os.system('clear')
              print("Draw")
              for block in self.show_game():
                print(block,end="")
              
            else:            
              os.system('clear')
              self.display_result()
            break
          else:
            os.system('clear')
            print("\n",'\033[1;34m' + "Your turn" + '\033[0m ')
            for block in self.show_game():
              print(block,end="")

          
    else:
      while(True):
        print("CPU turn")
        if not (self._compute_output()):
          self.cpu_put()
          if (self._compute_output()):
            if self.winner == 0:
              os.system('clear')
              print("Draw")
              for block in self.show_game():
                print(block,end="")

            else:
              os.system('clear')
              self.display_result()
            break
          else:
            for block in self.show_game():
              print(block,end="")
            os.system('clear')
            print('\n\033[1;34m' + "Your turn" + '\033[0m ')
            for block in self.show_game():
              print(block,end="")


        self._assign_value(raw_input())
        os.system('clear')
        if (self._compute_output()):
          if self.winner == self.user_use:
            self.display_result()
          else:
            os.system('clear')
            print("Draw")
            for block in self.show_game():
              print(block,end="")

          break
        else:
          print("CPU turn")

