from __future__ import print_function
import re

class players_data(object):
  """A class to manage players' information."""

  def __init__(self):
    """
    Name of main player is written in a specific function, basicaly is the same as setNewPlayerName.
    Name of main player is set as 'Player1' defaultly
    player_list is used to return player's name according to index (set do not have index)    
    """
    self.main_player = 'Player1'
    self.player_list = [self.main_player]
    self.player_set = {self.main_player}

  def _name_process(self, name):
    """
    Name cannot be empty, longer than ten and most of special characters.
    """
    try:
      name = str(name)
      if len(name) == 0:
        return False, "Name can not be empty"
      elif len(name) > 11:
        return False, "Length of name should be in 10 character."
      else:
        if len(re.sub(r'[^\w.]', '', name)) != len(name):
          return False, "Not allowed character in this name."
        else:        
          return True, "Player \'"+ name +"\' has been added!"
    except:
      return False, "Some thing wrong happens! Try again."

  def setMainPlayerName(self, name):
    name_valid, current_message = self._name_process(name)
    if name_valid is True:
      current_message = "Main player's name is set as \'" + name "\'!"
      self.player_set.remove(self.main_player)
      self.player_set.add(name)
      self.main_player = name
      self.player_list[0] = name
    return name_valid, current_message

  def setNewPlayerName(self, name):
    name_valid, current_message = self._name_process(name)
    if name in self.player_set:
      name_valid = False
      current_message = "There is a player with the same name."
    else:
      if name_valid is True:
        self.player_set.add(name)
        self.player_list.append(name)
    return name_valid, current_message

  def getPlayerName(self, player_num):
    try:
      if (player_num-1) < 0 or (player_num-1) >= len(self.player_list):
        return "Out of the range of the player list/"  
      else: 
        return self.player_list[player_num -1]
    except:
      return "Please input player's number (nNmeric)"