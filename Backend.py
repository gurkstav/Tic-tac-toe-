import re
from enum import IntEnum
import random

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
    self.scoreboard = []
    self.match_list = []
    self.next_match_num = 0
    self.tiebreakpts = [0, 0, 0, 0, 0, 0, 0, 0]
    self.winners = []
    self.winnername = ""
    
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

  """getNextMatch gets the players participating in the upcoming match from the match list.
     Returns the names of the players participating in the upcoming match according to the match list if the tournament is currently in progress, returns two empty strings otherwise."""
  def getNextMatch(self):
    if self.in_tournament is True:
      if self.next_match_num < len(self.player_list)*(len(self.player_list)-1):
        return [
          [self.getPlayerName(self.match_list[self.next_match_num][0]+1),
           self.getPlayerType(self.match_list[self.next_match_num][0]+1)],
          [self.getPlayerName(self.match_list[self.next_match_num][1]+1),
           self.getPlayerType(self.match_list[self.next_match_num][1]+1)]
        ]
      else:
        self.calculateWinners()
        if len(self.winners) == 1:
          self.winner = self.winners[0]
          return "", ""
        else:
          self.resolveDraw()
          return self.getNextMatch()
    else:
      return "", ""
    
  """setMatchResult sets the reult in the scoreboard for the current match and increments the internal counter which keeps track of which match the tournament is on.
     Takes in an IntEnum winner, returns True upon success and False otherwise."""
  def setMatchResult(self, winner):
    if self.in_tournament is True and self.next_match_num < len(self.player_list)*(len(self.player_list)-1):
      if len(self.match_list) <= len(self.player_list):
        if winner == winner.home:
          self.tiebreakpts[self.next_match_num[0]] += 1
        elif winner == winner.away:
          self.tiebreakpts[self.next_match_num[1]] += 1          
      else:
        x,y = self.match_list[self.next_match_num]
        self.scoreboard[x][y] = winner
        self.match_list[self.next_match_num][0] = winner
        self.next_match_num += 1
      return True
    else:
      return False

  """startTournament generates the necessary data structures (scoreboard, match_list, next_match_num) in memory and sets the in_tournament flag to indicate that the tournament is currently in progress.
     Returns a tuple boolean, string where the boolean is True on success, False otherwise and the string shall in such cases contain a descriptive error message."""
  def startTournament(self, difficulty):
    if self.in_tournament is False:
      if False:
        return False, "Cannot start a tournament with less than 2 players!"
      else:
        self.in_tournament = True
        """
        Fill any remaining player slots with AI players
        """
        ainum = 0
        for x in range(len(self.player_list), 8):
          aidiff = playertype.human
          if difficulty == 1:
            aidiff = playertype.ai_easy
          elif difficulty == 2:
            aidiff = playertype.ai_medium
          elif difficulty == 3:
            aidiff = playertype.ai_hard
          ainame = "AI" + str(ainum)
          while True:
            boolean, msg = self.addNewAIPlayerName(ainame, aidiff)
            if boolean is False:
              ainum += 1
              ainame = "AI" + str(ainum)
            else:
              break
          print("Added AI player \"" + ainame + "\".")
          ainum += 1
          print(self.player_list)
        """ 
        Set up the empty table (full of 'winner.undef' because no matches have been played yet)
        """
        for x in range(0, len(self.player_list)):
          self.scoreboard.append([])
          self.tiebreakpts.append([0])
          for y in range(0, len(self.player_list)):
            self.scoreboard[x].append(winner.undef)
        """ 
        Generate the first half of the match list
        """
        for x in range(1, len(self.player_list)):
          for y in range(0, len(self.player_list)):
            player2num = y+x
            while player2num >= len(self.player_list):
              player2num -= len(self.player_list)
            self.match_list.append([y, player2num])
        """ 
        Generate the second half of the match list by mirroring the first 
        """
        for x in range(0, len(self.player_list)*(len(self.player_list)-1)-1):
          self.match_list.append([self.match_list[x][1], self.match_list[x][0]])
        return True, self._name_process(self.main_player)
    else:
      return False, "The tournament has already been started!"

  """endTournament clears the necessary memory structures (scoreboard, match_list, next_match_num and unsets the in_tournament flag to indicate that the tournament is no longer in progress.
     Returns boolean, string where the boolean is True on success, False otherwise and the string shall in such cases contain a descriptive error message."""
  def endTournament(self):
    if self.in_tournament is False:
      return False, "No tournament to end!"
    else:
      self.in_tournament = False
      self.scoreboard = []
      self.match_list = []
      self.next_match_num = 0
      self.tiebreakpts = [0, 0, 0, 0, 0, 0, 0, 0]
      return True, ""

  """getScoreboard gets the scoreboard if the tournament is in progress. The scoreboard is the table which keeps track of who has won/lost/drawn against who. 
     If the tournament is in progress, the scoreboard is returned. Else boolean, string is returned where the boolean is False and the string is a suitable error message."""
  def getScoreboard(self):
    if self.in_tournament is False:
      return False, "No tournament in progress!"
    else:
      return self.scoreboard

  """getLeaferboard returns the leaderboard if the tournament is in progress. The leaderboard is a list of lists of the form playername, wins, draws, losses, score. The leaderboard is ordered according to 
     If the tournament is in progress, the leaderboard is returned. Else boolean, string is returned where the boolean is False and the string is a suitable error message."""
  def getLeaderboard(self):
    if self.in_tournament is False:
      return False, "No tournament to end!"
    else:
      leaderboard = []
      for x in range(0, len(self.player_list)):
        name = self.getPlayerName(x+1)
        wins = 0
        draws = 0
        losses = 0
        score = 0
        ptype = self.getPlayerType(x+1)
        """ 
        compute score for home games 
        """ 
        for y in range(0, len(self.player_list)):
          if self.scoreboard[y][x] == winner.home:
            wins += 1
          elif self.scoreboard[y][x] == winner.away:
            losses += 1
          elif self.scoreboard[y][x] == winner.draw:
            draws += 1
        """ 
        compute score for away games 
        """
        for y in range(0, len(self.player_list)):
          if self.scoreboard[x][y] == winner.home:
            losses += 1
          elif self.scoreboard[x][y] == winner.away:
            wins += 1
          elif self.scoreboard[y][x] == winner.draw:
            draws += 1
        """
        This is where the point values for win, draw and loss are defined,
        """
        winpts = 1
        losspts = -1
        drawpts = 0
        score = winpts*wins+drawpts*draws+losspts*losses+self.tiebreakpts[x]
        if leaderboard == []:
          leaderboard.append([name, wins, draws, losses, score, ptype])
        else:
          """
          insert score at the right point on the leaderboard 
          """
          index = 0
          inserted = False
          while index < len(leaderboard):
            if score > leaderboard[index][4]:
              leaderboard.insert(index, [name, wins, draws, losses, score, ptype])
              inserted = True
              break
            index += 1
          if inserted is False:
            """ 
            append score because it was the lowest yet 
            """
            leaderboard.append([name, wins, draws, losses, score])
    return leaderboard

  def calculateWinners(self):
    leaderboard = self.getLeaderboard(self)
    if leaderboard[0][4] != leaderboard[1][4]:
      self.winners = [leaderboard[0][0]]
    else:
      for x in range(0, len(self.player_list)):
        if leaderboard[x][4] != leaderboard[0][4]:
          break
        else:
          self.winners.append(leaderboard[x][0])

  def resolveDraw(self):
    if len(self.winners) == 2 and len(self.match_list) != 2:
      player1num = -1
      player2num = -1
      for x in range(0, len(self.player_list)):
        if self.player_list[x] == winners[0]:
          player1num = x
          break
      for x in range(0, len(self.player_list)):
        if self.player_list[x] == winners[1]:
          player2num = x
          break
      if player1num > player2num:
        self.issueDoubleRematch(player1num, player2num)
      else:
        self.issueDoubleRematch(player2num, player1num)
    else:
      self.winner = random.choice(winners)

  def issueDoubleRematch(self, player1num, player2num):
    self.matchlist = []
    self.match_list.append([player2num, player1num])
    self.match_list.append([player1num, player2num])
    self.next_match_num = 0
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
