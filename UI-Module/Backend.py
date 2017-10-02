import re
from enum import IntEnum
from random import choice

class Backend(object):
  """
  A class to manage players' information.
  """

  def __init__(self):
    """
    Name of main player is written in a specific function (setMainPlayerName), basically the same 
    as addNewPlayerName.
    Name of main player is set as 'Player1' by default.
    player_list is used to return player's name according to index (set are not indexed).    
    """
    self.main_player = 'Player1'
    self.player_list = [[self.main_player, playertype.human]]
    self.player_set = {self.main_player}
    self.in_tournament = False
    
  def _name_process(self, name):
    """
    Name cannot be empty, longer than ten and most of special characters.
    """
    try:
      name = str(name)
      if len(name) == 0:
        return False, "The name cannot be empty!"
      elif len(name) > 11:
        return False, "The length of the name should be at most 10 characters!"
      else:
        if len(re.sub(r'[^\w.]', '', name)) != len(name):
          return False, "This name contains one or more invalid characters!"
        else:        
          return True, "Player \'"+ name +"\' has been added!"
    except:
      return False, "Something wrong happened! Try again."

  def setMainPlayerName(self, name):
    name_valid, current_message = self._name_process(name)
    if name_valid is True:
      current_message = "Main player's name successfully set to \'" + name +"\'!"
      self.player_set.remove(self.main_player)
      self.player_set.add(name)
      self.main_player = name
      self.player_list[0] = [name, playertype.human]
    return name_valid, current_message

  def addNewPlayerName(self, name):
    name_valid, current_message = self._name_process(name)
    if name in self.player_set:
      name_valid = False
      current_message = "There is already a player with the same name!"
    else:
      if name_valid is True:
        self.player_set.add(name)
        self.player_list.append([name, playertype.human])
    return name_valid, current_message

  def addNewAIPlayerName(self, name, ptype):
    if ptype != playertype.human:
      name_valid, current_message = self._name_process(name)
      if name in self.player_set:
        name_valid = False
        current_message = "There is already a player with the same name!"
      else:
        if name_valid is True:
          self.player_list.append([name, ptype])
      return name_valid, current_message
    else:
      return False, "AI players need to have an AI player type!"

  def getPlayerName(self, player_num):
    try:
      if (player_num-1) < 0 or (player_num-1) >= len(self.player_list):
        return "The provided number is outside the range of the player list!"  
      else: 
        return self.player_list[player_num-1][0]
    except:
      return "Please input the player's number in numerical form."

  def getPlayerType(self, player_num):
    try:
      if (player_num-1) < 0 or (player_num-1) >= len(self.player_list):
        return "The provided number is outside the range of the player list!"  
      else: 
        return self.player_list[player_num-1][1]
    except:
      return "Please input the player's number in numerical form."

  def getListOfPlayerNames(self):
    name_list = []
    for player in self.player_list:
      name_list.append(player[0])
    return name_list


  def deletePlayerSet(self):
    """
    When press back, delete all players except main player.
    It is designed because main user can change his/her name whenever he/she want.
    """
    self.player_list = [self.main_player]
    self.player_set = {self.main_player}


class winner(IntEnum):
  undef = 0
  """
  Game not yet played
  """
  draw = -1
  """
  Game ended in a draw
  """
  home = 1
  """
  Starting/first player won
  """
  away = 2
  """
  Other/second player won
  """


class playertype(IntEnum):
  human = 0
  """
  Human player
  """
  ai_easy = 1
  """
  Easy AI player
  """
  ai_medium = 2
  """
  Medium AI player
  """
  ai_hard = 3
  """
  Hard AI player
  """
