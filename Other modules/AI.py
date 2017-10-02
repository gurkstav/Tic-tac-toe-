from enum import IntEnum
from random import random

""" Playfield is currently assumed to be a list-of-lists-of-lists "2D Array" indexed [x][y] ranging from 0, 0 as upper left to 2, 2 as bottom right containing ints which are 0 for empty, 1 for X and 2 for O. Initialization is currently done by calling a method init(int difficulty, int myplayer) where difficulty is 1, 2 or 3 for easy, medium or hard respectively and int myplayer is 1 for X and 2 for O. Moves are currently requested by calling the method makeMove(playfield) and are currently returned as [int x, int y] according to the same coordinate system. """

class AI(object):

  def __init__(self):
    self.myplayer = 0
    self.offensiveprob = 0 """ Probability that the AI plays a defensive move even though offensive moves are available. """
    self.blockingprob = 0 """ Probability that the AI plays an offensive move even though blocking moves are available. """
    self.winningprob = 0 """ Probability that the AI plays a blocking move even though winning moves are available. """

  def init(difficulty, myplayer):
    self.myplayer = myplayer
    if difficulty == 1:
      self.offensiveprob = 0.5
      self.blockingprob = 0.6
      self.winningprob = 0.7
    elif difficulty == 2:
      self.offensiveprob = 0.75
      self.blockingprob = 0.9
      self.winningprob = 0.8
    elif difficulty == 3:
      self.offensiveprob = 1
      self.blockingprob = 1
      self.winningprob = 1
    return True

  def analyzeMove(playfield, x, y):
      
  def makeMove(playfield):
    moves = []
    

class movetype(IntEnum):
  defensive = 0
  """
  Any move which doesn't involve any rows of more than one of either symbol.
  """
  offensive = 1
  """
  Any move which does involve one or more rows of more than one of either symbol but doesn't involve winning or giving the opponent an opening to win.
  """
  blocking = 2
  """
  Any move which involves directly preventing the opponent from winning by finishing a line containing two of their symbol (i.e. X|X|_ becoming X|X|O)
  """
  winning = 3
  """
  Any move which directly results in this AI player winning the game (i.e. X|X|_ becoming X|X|X).
  """
    
class linestate(IntEnum):
  empty = 0
  """
  Empty line
  """
  full = 1
  """
  Full line
  """
  split = 2
  """
  Line contains one of our symbol and one of their symbol
  """
  leaningus = 3
  """
  Line contains one of our symbol and two empty spaces
  """
  leaningthem = 4
  """
  Line contains one of their symbol and two empty spaces
  """
  winning = 5
  """
  Line contains two of our symbol and an empty space
  """
  losing = 6
  """
  Line contains two of their symbol and an empty space
  """
