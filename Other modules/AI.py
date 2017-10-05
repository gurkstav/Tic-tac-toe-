from enum import IntEnum
from random import random
from random import choice

""" Playfield is currently assumed to be a list-of-lists-of-lists "2D Array" indexed [x][y] ranging from 0, 0 as upper left to 2, 2 as bottom right containing ints which are 0 for empty, 1 for X and 2 for O. Initialization is currently done by calling a method init(int difficulty, int myplayer) where difficulty is 1, 2 or 3 for easy, medium or hard respectively and int myplayer is 1 for X and 2 for O. Moves are currently requested by calling the method makeMove(playfield) and are currently returned as [int x, int y] according to the same coordinate system. """

class AI(object):

  def __init__(self):
    self.myplayer = 0
    self.theirplayer = 0
    self.offensiveprob = 0
    """ Probability that the AI doesn't play a defensive move when better moves are available. """
    self.blockingprob = 0
    """ Probability that the AI doesn't play an offensive move when better moves are available. """
    self.winningprob = 0
    """ Probability that the AI doesn't play a blocking move when winning moves are available. """
    self.bestprob = 0
    """ Probability that the AI plays the best move of a particular type rather than the second best. """

  def init(self, difficulty, myplayer):
    self.myplayer = myplayer
    if self.myplayer == 1:
      self.theirplayer = 2
    else:
      self.theirplayer = 1
    if difficulty == 1:
      self.offensiveprob = 0.5
      self.blockingprob = 0.66
      self.winningprob = 0.7
      self.bestprob = 0.68
    elif difficulty == 2:
      self.offensiveprob = 0.75
      self.blockingprob = 0.9
      self.winningprob = 0.8
      self.bestprob = 0.85
    elif difficulty == 3:
      self.offensiveprob = 1
      self.blockingprob = 1
      self.winningprob = 1
      self.bestprob = 1
    return True

  def makeMove(self, playfield):
    moves = [[],[],[],[]]
    lines = [[[0,0], [0,1], [0,2]], [[1,0], [1,1], [1,2]], [[2,0], [2,1], [2,2]], [[0,0], [1,0], [2,0]], [[0,1], [1,1], [2,1]], [[0,2], [1,2], [2,2]], [[0,0], [1,1], [2,2]], [[0,2], [1,1], [2,0]]]
    linestates = [[],[],[],[],[],[],[],[]]
    linenum = 0
    movetype = Movetype.impossible
    for line in lines:
      linetiles = [playfield[line[0][0]][line[0][1]], playfield[line[1][0]][line[1][1]], playfield[line[2][0]][line[2][1]]]
      if 0 in linetiles and self.myplayer not in linetiles and self.theirplayer not in linetiles:
        linestates[linenum] = linestate.empty
      elif 0 in linetiles and self.myplayer in linetiles and self.theirplayer not in linetiles:
        if linetiles.count(self.myplayer) == 2:
          linestates[linenum] = linestate.winning
        else:
          linestates[linenum] = linestate.leaningus
      elif 0 in linetiles and self.myplayer not in linetiles and self.theirplayer in linetiles:
        if linetiles.count(self.theirplayer) == 2:
          linestates[linenum] = linestate.losing
        else:
          linestates[linenum] = linestate.leaningthem
      elif 0 in linetiles and self.myplayer in linetiles and self.theirplayer in linetiles:
        linestates[linenum] = linestate.split
      elif 0 not in linetiles:
        linestates[linenum] = linestate.full
      linenum += 1
    if linestates == [linestate.empty,linestate.empty,linestate.empty,linestate.empty,linestate.empty,linestate.empty,linestate.empty,linestate.empty]:
      if random() > self.bestprob:
        return [0, 0]
      else:
        return [1, 1]
    moverank = 0
    linenum = 0
    for x in range(0, 3):
      for y in range(0, 3):
        for z in range(0, 7):
          line = lines[z]
          if [x,y] in line:
            if linestates[z] == linestate.winning:
              Movetype.winning
            elif linestates[z] == linestate.losing:
              if movetype < Movetype.blocking:
                movetype = Movetype.blocking
            elif linestates[z] == linestate.leaningus or linestates[z] == linestate.leaningthem:
              if movetype < Movetype.offensive:
                movetype = Movetype.offensive
            elif linestates[z] == linestate.empty or linestates[z] == linestate.split:
              if movetype < Movetype.defensive:
                movetype = Movetype.defensive
        linenum = 0
        for line in lines:
          if [x,y] in line:
            if movetype == Movetype.winning:
              if linestates[linenum] == linestate.winning:
                moverank += 1
            elif movetype == Movetype.blocking:
              if linestates[linenum] == linestate.losing:
                moverank += 1
            elif movetype == Movetype.offensive:
              if linestates[linenum] == linestate.leaningus:
                moverank += 1
              elif linestates[linenum] == linestate.leaningthem:
                moverank += 1
            elif movetype == Movetype.defensive:
              if linestates[linenum] == linestate.empty:
                moverank += 1
          linenum += 1
        if movetype != Movetype.impossible:
          if moves[movetype] == []:
            moves[movetype] = [[[x, y], movetype]]
          else:
            index = 0
            inserted = False
            while index < len(moves[movetype]):
              if moverank > moves[movetype][index][1]:
                moves[movetype].insert(index, [[x, y], movetype])
                inserted = True
                break
              index += 1
            if inserted is False:
              moves[movetype].append([[x, y], movetype])
    for movelist in moves:
      index = 0
      while index < len(movelist):
        if playfield[movelist[index][0][0]][movelist[index][0][1]] != 0:
          movelist.remove(movelist[index])
          index = 0
        else:
          index += 1
    typetoplay = 3
    while typetoplay > 0:
      if moves[typetoplay] == []:
        typetoplay -= 1
      else:
        break
    secondtype = -1
    if typetoplay != 0:
      secondtype = typetoplay
      while secondtype > -1:
        if moves[secondtype] == []:
          secondtype -= 1
        else:
          break
      if secondtype != -1:
        if typetoplay == Movetype.winning:
          if random() > self.winningprob:
            typetoplay = secondtype
        elif typetoplay == Movetype.blocking:
          if random() > self.blockingprob:
            typetoplay = secondtype
        elif typetoplay == Movetype.offensive:
          if random() > self.offensiveprob:
            typetoplay = secondtype
    if len(moves[typetoplay]) > 1:
      if moves[typetoplay][0][1] > moves[typetoplay][1][1]:
        if random() > self.bestprob:
          return moves[typetoplay][1][0]
        else:
          return moves[typetoplay][0][0]
      else:
        if moves[typetoplay][0][0] in [[0,0],[2,0],[0,2],[2,2],[1,1]] and moves[typetoplay][1][0] not in [[0,0],[2,0],[0,2],[2,2],[1,1]]:
          if random() > self.bestprob:
            return moves[typetoplay][1][0]
          else:
            return moves[typetoplay][0][0]
        else:
          return choice([moves[typetoplay][0][0], moves[typetoplay][1][0]])
    else:
      return moves[typetoplay][0][0]
            

class Movetype(IntEnum):
  impossible = -1
  """
  Any move which cannot be played because its tile is already occupied.
  """
  defensive = 0
  """
  Any move which doesn't involve any rows of more than one of either symbol or any rows with more of one symbol than the other.
  """
  offensive = 1
  """
  Any move which does involve one or more rows of one or more of either symbol but doesn't involve winning or giving the opponent an opening to win.
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
