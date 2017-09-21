import re
from enum import Enum

class winner(IntEnum):
  undef = 0 """Game not yet played"""
  draw = -1 """Game ended in a draw"""
  home = 1  """Starting/first player won"""
  away = 2  """Other/second player won"""

class backend(object):
  """
  A class to manage players' information.
  """

  def __init__(self):
    """
    Name of main player is written in a specific function, basically the same 
    as setNewPlayerName.
    Name of main player is set as 'Player1' by default.
    player_list is used to return player's name according to index (set are not indexed).    
    """
    self.main_player = 'Player1'
    self.player_list = [self.main_player]
    self.player_set = {self.main_player}
    self.in_tournament = False
    self.scoreboard = []
    self.match_list = []
    self.next_match_num = 0
    
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
      self.player_list[0] = name
    return name_valid, current_message

  def addNewPlayerName(self, name):
    name_valid, current_message = self._name_process(name)
    if name in self.player_set:
      name_valid = False
      current_message = "There is already a player with the same name!"
    else:
      if name_valid is True:
        self.player_set.add(name)
        self.player_list.append(name)
    return name_valid, current_message

  def getPlayerName(self, player_num):
    try:
      if (player_num-1) < 0 or (player_num-1) >= len(self.player_list):
        return "The provided number is outside the range of the player list!"  
      else: 
        return self.player_list[player_num-1]
    except:
      return "Please input the player's number in numerical form."

  def getListOfPlayerNames(self):
    return self.player_list

  def getNextMatch(self):
    if self.in_tournament is True and next_match_num < len(self.player_list)*(len(self.player_list)-1):
      return getPlayerName(self.match_list[self.next_match_num][0]), getPlayerName(self.match_list[self.next_match_num][1])
    else:
      return "", ""

  def setMatchResult(self, winner):
    self.scoreboard[self.match_list[self.next_match_num][1], self.match_list[self.next_match_num][0]] = winner
    return True
    
  def startTournament(self):
    if self.in_tournament is True:
      if len(self.player_list) < 2:
        return False, "Cannot start a tournament with less than 2 players!"
      else:
        self.in_tournament = True
        """ Set up the empty table (full of 'winner.undef' because no matches have been played yet) """
        for x in range(0, len(self.player_list)):
          self.scoreboard.append([])
          for y in range(0, len(self.player_list)):
            self.scoreboard[x].append(winner.undef)
        """ Generate the first half of the match list """
        for x in range(1, len(self.player_list)):
          for y in range(0, len(self.player_list)):
            player2num = y+x
            while player2num >= len(self.player_list):
              player2num -= len(self.player_list)
            matchlist.append([y, player2num])
        """ Generate the second half of the match list by mirroring the first """
        for x in range(0, len(self.player_list)*(len(self.player_list)-1)-1):
          matchlist.append([matchlist[x][1], matchlist[x][0]]) 
        return True, self._name_process(name)
    else:
      return False, "The tournament has already been started!"

  def endTournament(self):
    if self.in_tournament is False:
      return False, "No tournament to end!"
    else:
      self.in_tournament = False
      self.scoreboard = []
      self.match_list = []
      self.next_match_num = 0
      return True, self._name_process(name)

  def getScoreboard(self):
    if self.in_tournament is False:
      return False, "No tournament in progress!"
    else:
      return self.scoreboard

  def getLeaderboard(self):
    leaderboard = []
    for x in range(0, len(self.player_list)):
      name = getPlayerName(x)
      score = 0;
      """ compute score for home games """ 
      for y in range(0, len(self.player_list)):
        if self.scoreboard[y][x] == winner.home:
          score += 1
        elif self.scoreboard[y][x] == winner.away:
          score -= 1
      """ compute score for away games """
      for y in range(0, len(self.player_list)):
        if self.scoreboard[x][y] == winner.home:
          score -= 1
        elif self.scoreboard[x][y] == winner.away:
          score += 1
      if leaderboard == []:
        leaderboard.append([name, score])
      else:
        """ insert score at the right point on the leaderboard """
        index = 0
        while index < len(leaderboard):
          if score > leaderboard[index][1]:
            leaderboard.insert(index, [name, score])
            break
          index += 1
    return leaderboard
      
  """
  This part is desined to make sure the program will not been crashed by some situation.
  Also, some functions are provided if we want to use.
  """

  def deletePlayerSet(self):
    """
    When press back, delete all players except main player.
    It is designed because main user can change his/her name whenever he/she want.
    """
    self.player_list = [self.main_player]
    self.player_set = {self.main_player}

  def remainTournamentPlayer(self):
    """
    Before use the deletePlayerSet, using this function can remain players except 
    main player.
    """
    self.last_time_players = set(self.player_set)
    self.last_time_players.remove(self.main_player)
  
  def reloadTournamentPlayer(self):
    """
    Once useing deletePlayerSet, this function can help to check whether there is a
    confliction between the remained tornament Players and main player(if changed).
    Besides, reload to the players set.
    """
    try:
      current_message = "Reloaded last time players successfully"
      for player in self.last_time_players:
        if self.main_player is player:
          current_message = "Reload players and removed a last time player who is named the same as the main player now."
        else:
          self.player_set.add(name)
          self.player_list.append(name)
    except:
      current_message = "No tournament players have been set before."
    return current_message
