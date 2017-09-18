import re

class players_data(object):
  """A class to manage players' information."""

  def __init__(self):
    """
    Name of main player is written in a specific function, basicaly is the same 
    as setNewPlayerName.
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
      current_message = "Main player's name is set as \'" + name +"\'!"
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

  """
  This part is desined to make sure the program will not been crashed by some situation.
  Also, some functions are provided if we want to use.
  """

  def deletePlayerSet(self):
    """
    When press back, delete all players except main player.
    It is desined because main user can chage his/her name whenever he/she want.
    """
    self.player_list = [self.main_player]
    self.player_set = {self.main_player}

  def remainTornamentPlayer(self):
    """
    Before use the deletePlayerSet, using this function can remain players except 
    main player.
    """
    self.last_time_players = set(self.player_set)
    self.last_time_players.remove(self.main_player)
  
  def reloadTornamentPlayer(self):
    """
    Once useing deletePlayerSet, this function can help to check whether there is a
    confliction between the remained tornament Players and main player(if changed).
    Besides, reload to the players set.
    """
    try:
      current_message = "Reload players last time successfully"
      for player in self.last_time_players:
        if self.main_player is player:
          current_message = "Reload players and remove a player last time, who is named the same as main player now"
        else:
          self.player_set.add(name)
          self.player_list.append(name)
    except:
      current_message = "No tornament players have been set before"
    return current_message