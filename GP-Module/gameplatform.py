from __future__ import print_function
import random
from random import randint
from random import shuffle
from copy import deepcopy
from Player import PlayerAI
import time
#from GameEngine import GameEngine

TTT_SIZE = 3

class Player:
    """
    Class for interaction with the player. Handeling inputs from the player
    """

    def __init__(self, name, piece_string):
        """
        init function for the Player class
        
        :param arg1: Instance attributes
        :param arg2: name for the player
        :param arg3: piece string for the player represented as an int
        :type arg1: self
        :type arg2: string
        :type arg3: int
        :return: None
        :rtype: NoneType
        """
        self.name = name
        self.piece_string = piece_string
        

    def get_move(self):
        """
        Queries the player for a move
        :param arg1: Instance attributes for the move
        :type arg1: self
        :return: TODO
        :rtype: TODO
        """
        raise NotImplementedError

    def __str__(self):
        return(self.piece_string)
        """
        Queries the player for a move
        :return: a move
        :rtype: int (1-9)
        """

class RealPlayer(Player):

    def __init__(self, name, piece_string):
        """
        init function for the RealPlayer class
        
        :param arg1: Instance attributes
        :param arg2: name for the player
        :param arg3: piece string for the player represented as an int
        :type arg1: self
        :type arg2: string
        :type arg3: int
        :return: None
        :rtype: NoneType
        """
        super().__init__(name, piece_string)
        

    def get_move(self, game_board):
        """
        Queries handeling user input for the move
        :param arg1: Instance attributes
        :param arg1: The current game_board 
        :type arg1: self
        :type arg1: array
        :return: a move
        :rtype: int (1-9)
        """

        while True:
            inputStr = input('Player "{}" ({}) : Where will you place your marker (1-9)'.format(self.name, self)).strip()
            if inputStr.isdigit():
                move = int(inputStr)
                if game_board.valid_move(move):
                    if game_board.is_space_free(move):
                        return(move)
                    else:
                        print ("")
                        print ("There is already a piece placed on this slot, try another")
                        print ("")
                else:
                    print ("")
                    print ("Please enter a number between 1 and 9")
                    print ("")
            else:
                print ("")
                print ("Please enter a number between 1 and 9")
                print ("")

class Game:
    """ 
    Class for running the game logic and keeping track of game state
    """

    def __init__(self, player1, player2):

        """
        init function for the Game class
        
        :param arg1: Instance attributes
        :param arg2: player1 
        :param arg3: player2
        :type arg1: self
        :type arg2: player
        :type arg3: player
        :return: None
        :rtype: NoneType
        """

        if not isinstance(player1, Player) or not isinstance(player2, Player):
            raise TypeError
        self.players = [player1, player2]
        self.game_board = GameBoard()
        self.current_player = self.who_plays_first()

    def enter_game_loop(self):

        """
        Loop until game is finished,return the winning player
        :return: Returns the winning player, 0 if draw
        :rtype: player 
        """
        print(self.game_board)
        print('Player "{}" starts'.format(self.current_player.name))
        while True:
            move = self.current_player.get_move(self.game_board)    
            self.game_board.update_board(self.current_player, move)
            print(self.game_board)
            
            if self.game_board.is_there_a_winner(self.current_player):
                print ('Game: Player "{}" ({}) has won the game!'.format(self.current_player.name, self.current_player))
                print (str(self.current_player.name))
                return(self.current_player.name)
            if self.game_board.is_board_full():
                print ("Game: The game resulted in a draw")
                return 0
            self.toggle_player()


        

    def toggle_player(self):
        """
        Switch player
        
        :param arg1: Instance attributes for player
        :type arg1: self
        :return: None
        :rtype: NoneType
        """
        if self.current_player == self.players[0]:
            self.current_player = self.players[1]
        else:
            self.current_player = self.players[0]

    def who_plays_first(self):
        """
        Randomly picks starting player from self.players
        
        :param arg1: Instance attributes for player
        :type arg1: self
        :return: None
        :rtype: NoneType
        """
        return(random.choice(self.players))

    def who_is_moving(self):
        """
        Returns the current player
        :return: The current player
        :rtype: player
        """
        return(self.current_player)

class AIGame:
    """ 
    Class for running the game while playing vs an AI and keeping track of game state
    """

    def __init__(self, player1, player2):

        self.players = [player1, player2]
        self.playerTurn = 1
        self.game_board = GameBoard()  

    """
    Main loop
    returns winner name or 0 if tie
    """
    def startGame(self):
        Player_winner = 0
        AI_winner = 0
        while True:
            if not self.players[self.playerTurn-1].getIsAI():
                print(self.game_board)
                inputMove = self.askForMove(self.players[self.playerTurn-1].name, "Choose your move: ")
                if inputMove in ('q', 'Q', 'quit', 'Quit'):
                    print(self.players[self.playerTurn-1].name, "has quit the game")
                    break
                while True:
                    moveIsValid = self.game_board.is_space_free(inputMove)
                    if moveIsValid:  # or inputMove == 0:
                        break
                    else:
                        inputMove = self.askForMove(self.players[self.playerTurn-1].name, "Invalid move, input a new move: ")
               
                self.game_board.updateAIboard(inputMove, 'X')
            else:
                self.game_board.AImove(self.players[self.playerTurn-1].getAIlevel(), self.playerTurn)
            Player_winner = self.game_board.is_there_a_winner_player()
            AI_winner = self.game_board.is_there_a_winner_ai()
            if Player_winner != 0:
                print(self.game_board)
                print("The Winner is " + self.players[Player_winner-1].name + "!")
                print("Congratulations!")
                winner = self.players[Player_winner-1].name
                break
            if AI_winner != 0:
                print(self.game_board)
                print("The AI has won!")
                print("Better luck next time")
                winner = self.players[AI_winner-1].name
                break
            if self.game_board.is_board_full():
                print(self.game_board)
                print("The Game Ended in a Tie!")
                break
            if self.playerTurn == 1:
                self.playerTurn = 2
            elif self.playerTurn == 2:
                self.playerTurn = 1
            else:
                print("Something has gone wrong while switching players")
        return winner

    def askForMove(self, player, string):
        """
        :return: The current player
        :rtype: player
        """
        while True:
            inputString = input(str(player)+", "+string)
            if len(inputString) > 0 and inputString in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                return int(inputString)
            elif len(inputString) > 0 and inputString in ['q', 'Q', 'quit', 'Quit']:
                return inputString
            else:
                print("Invalid input, should be 1-9")
        return(self.current_player)
            
class GameBoard:
    """ 
    Class for representing the game board
    0 represents an available square
    1 represents a square occupied by player 1
    2 represents a square occupied by player 2
    """

    def __init__(self):
        """
        init function for the GameBoard class which setting the size of the board for the game
        
        :param arg1: Instance attributes
        :type arg1: self
        :return: None
        :rtype: NoneType
        """
        self.board = [' ' for i in range(TTT_SIZE*TTT_SIZE)]
        self.winningCombinations = (
            [0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        )

    def winner_exists(self):
        """
        Check if winner exists
        :param arg1: Instance attributes for player
        :type arg1: self
        :return: None
        :rtype: NoneType
        """
      
    def is_there_a_winner(self, player):
        """
        Checks if the player who just made a move have 3 in a row and won the game, 
        returns true if the player won and then the game will stop and add a point to the player that won and start a new game, 
        if false, play the game as usual
                
        :param arg1: Instance attributes for player
        :param arg2: player to check for winning
        :type arg1: self
        :type arg2: player
        :return: return true if there is a winner
        :rtype: bool
        """
        win_conditions = [
            [0,1,2],[3,4,5],[6,7,8],
            [0,3,6],[1,4,7],[2,5,8],
            [0,4,8],[2,4,6]]
        for winCombo in win_conditions:
            for win in winCombo:
                if player != self.board[win]:
                    break
            else:
                return True
        return False


    def is_there_a_winner_player(self):
        """
        Checks if the player who just made a move have 3 in a row and won the game, 
        returns true if the player won and then the game will stop and add a point to the player that won and start a new game, 
        if false, play the game as usual
                
        :param arg1: Instance attributes for player
        :param arg2: player to check for winning
        :type arg1: self
        :type arg2: player
        :return: return true if there is a winner
        :rtype: bool
        """
        win_conditions = [
            [0,1,2],[3,4,5],[6,7,8],
            [0,3,6],[1,4,7],[2,5,8],
            [0,4,8],[2,4,6]]
        for winCombo in win_conditions:
            for win in winCombo:
                if 'X' != self.board[win]:
                    break
            else:
                return 1
        return 0


    def is_there_a_winner_ai(self):
        """
        Checks if the player who just made a move have 3 in a row and won the game, 
        returns true if the player won and then the game will stop and add a point to the player that won and start a new game, 
        if false, play the game as usual
                
        :param arg1: Instance attributes for player
        :param arg2: player to check for winning
        :type arg1: self
        :type arg2: player
        :return: return true if there is a winner
        :rtype: bool
        """
        win_conditions = [
            [0,1,2],[3,4,5],[6,7,8],
            [0,3,6],[1,4,7],[2,5,8],
            [0,4,8],[2,4,6]]
        for winCombo in win_conditions:
            for win in winCombo:
                if 'O' != self.board[win]:
                    break
            else:
                return 1
        return 0

    def is_board_full(self):
        """Check if board is full"""
        for i in range(TTT_SIZE*TTT_SIZE):
            if self.board[i] == ' ':
                return(False)

        return(True)

    def valid_move(self, move):
        """
        Takes in the same integer as makeAMove and checks that there is no "gamepiece" already on the int position, 
        returns false and writes out invalid move to player and allows them to go back and make another move instead
        
        :param arg1: Instance attributes for player
        :param arg2: move
        :type arg1: self
        :type arg2: move
        :return: return true if the move is valid
        :rtype: bool
        """
        return(1 <= move <= 9)

    def update_board(self, player, move):
        """
        Updates the gameboard
        
        :param arg1:  Instance attributes for board
        :param arg2: The current player
        :param arg3: The move the current player want to do
        :type arg1: self
        :type arg2: player
        :type arg3: move
        :return: None
        :rtype: NoneType
        """
        self.board[move - 1] = player

    def updateAIboard(self, move, player):
        """"
        Updates the gameboard, differs from update_board in the order of arguments
        
        :param arg1:  Instance attributes for board
        :param arg2: The current player
        :param arg3: The move the current player want to do
        :type arg1: self
        :type arg2: move
        :type arg3: player
        :return: self
        :rtype: self
        """
        self.board[move - 1] = player
        return self

    def is_space_free(self, move):
        """
        Returns true if the move is valid, otherwise false
        :param arg1: Instance attributes for board
        :param arg2: The move we want to check if it is valid
        :type arg1: self
        :type arg2: move
        :return: return true if the spaces is free
        :rtype: bool
        """
        return(self.board[move - 1] == ' ')


    def AImove(self, AIlevel, player):
        """
        This function returns the board updated with the new move. If the move or the player is invalid
        -1 will be returned.
        :param arg1: move - the move the player choose to make, should be a number between 1 and 9
        :param arg2: player - who the current player is, should be either the number 1 or 2
        :type arg1: int
        :type arg2: int
        :return: board
        :rtype: list
        """

        AI = GameEngine()
        if player != 1 and player != 2:
            return 0

        if AIlevel == 1:
            AImove1 = AI.getAImove1(self)
            self.updateAIboard(AImove1, 'O')
            print("AI moved to position: ", AImove1)
            return self.board
        elif AIlevel == 2:
            AImove2 = AI.getAImove2(player,self)
            self.updateAIboard(AImove2, 'O')
            print("AI moved to position: ", AImove2)
            return self.board
        elif AIlevel == 3:
            AImove3 = AI.getAImove3(player,self)
            self.updateAIboard(AImove3, 'O')
            print("AI moved to position: ",AImove3)
            return self.board
        else:
            return 0


    def checkWinner(self):
        """
        This function checks if any player has won
        :return: 0 if no winner, 1 or 2 if winner
        :rtype: int
        """
        for combination in self.winningCombinations:
            if self.board[combination[0]] == self.board[combination[1]] == self.board[combination[2]] == 1:
                return 1
            elif self.board[combination[0]] == self.board[combination[1]] == self.board[combination[2]] == 2:
                return 2
        return 0

    def checkValidMove(self, move):
        """
        This function checks if the move is valid.
        :return: return true if the move is valid
        :rtype: bool
        """
        if move not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            return False
        elif self.board[move-1] != ' ':
            return False
        return True


    def __str__(self):
        """
        Will write out a representation of the game board for the player to see it in it's basic form (no moves played), 
        would like the player names as well as their points to be represented below the playing field, 
        as well as the players name who is making a move being written above the game board
        
        :param arg1: nstance attributes for board
        :type arg1: self
        :return: None
        :rtype: NoneType
        """
        lines = []
        lines.append('')
        lines.append('1|2|3')
        lines.append('-+-+-')
        lines.append('4|5|6') # board template
        lines.append('-+-+-')
        lines.append('7|8|9')
        lines.append('')
        lines.append("             To chose a spot to place your") 
        lines.append("             marker enter the designated number (1-9)")
        lines.append('|'.join([str(self.board[i]) for i in range(0,3)]))
        lines.append('-+-+-')
        lines.append('|'.join([str(self.board[i]) for i in range(3,6)]))
        lines.append('-+-+-')
        lines.append('|'.join([str(self.board[i]) for i in range(6,9)]))
        lines.append('')
        return_string = '\n'.join(lines)
        return(return_string)

class GameEngine():
    """
    A class for the AI and it's functions
    """


    def getAImove1(self, board):
        """
        This function simulates an easy AI level and generates next move on a given board.
        :param arg1: player - who the current player is, should be either the number 1 or 2
        :type arg1: int
        :return: move (1-9)
        :rtype: int 
        """
        while not (board.is_board_full()):
            returnMove = randint(1, 9)
            if board.checkValidMove(returnMove):
                return returnMove
        return 0


    def getAImove2(self, player,board):
        """
        This function simulates an intermediate AI level and generates next move on a given board.
        :param arg1: player - who the current player is, should be either the number 1 or 2
        :type arg1: int
        :return: move (1-9)
        :rtype: int 
        """
        if player == 1:
            notPlayer = 2
        elif player == 2:
            notPlayer = 1
        else:
            return 0

        for i in range(1, 10):
            boardCopy = deepcopy(board)
            if boardCopy.checkValidMove(i):
                boardCopy.update_board(i, player)
                if boardCopy.checkWinner():
                    # print("winning")
                    return i

        for i in range(1, 10):
            boardCopy = deepcopy(board)
            if boardCopy.checkValidMove(i):
                boardCopy.update_board(i, notPlayer)
                if boardCopy.checkWinner():
                    # print("blocking")
                    return i

        possibleMoves = [5, 1, 3, 7, 9, 2, 4, 6, 8]
        shuffle(possibleMoves)

        for i in possibleMoves:
            if board.checkValidMove(i):
                return i

        return 0


    def checkWinMove(self, board, player, i):
        """
        This function checks if a move can make player 1 or player 2 win
        :param arg1: player - who the current player is, should be either the number 1 or 2
        :param arg2: i - location to check if it can make a win
        :type arg1: int
        :type arg1: int
        :return: True or False depending on if the checked location can make it win
        :rtype: bool
        """
        boardCopy = deepcopy(board)
        ##player eller notPlayer
        if player == 1:
            boardCopy.board[i-1] = player
            return player == 1 and boardCopy.checkWinner() == 1
        elif player == 2:
            boardCopy.board[i-1] = player
            return player == 2 and boardCopy.checkWinner() == 1


    def checkForkMove(self, board, player, i):
        """
        This function determines if a move opens up a fork
        :param arg1: player - who the current player is, should be either the number 1 or 2
        :param arg2: i - location to check if it can make a win
        :type arg1: int
        :type arg1: int
        :return: move (1-9)
        :rtype: int
        """
        # Determines if a move opens up a fork opportunity
        boardCopy = deepcopy(board)
        boardCopy.board[i-1] = player
        winningMoves = 0
        for j in range(1, 10):
            if self.checkWinMove(boardCopy, player, j) and boardCopy.checkValidMove(j):
                winningMoves += 1
                return winningMoves >= 2



    def getAImove3(self, player,board):
        """
        This function simulates an impossible AI level and generates next move on a given board.
        :param arg1: player - who the current player is, should be either the number 1 or 2
        :type arg1: int
        :return: move (1-9)
        :rtype: int
        """
        if player == 1:
            notPlayer = 2
        elif player == 2:
            notPlayer = 1
        else:
            return 0

        for i in range(1, 10):
            boardCopy = deepcopy(board)
            if boardCopy.checkValidMove(i):
                boardCopy.update_board(i, player)
                if boardCopy.checkWinner():
                    # print("winning")
                    return i

        for i in range(1, 10):
            boardCopy = deepcopy(board)
            if boardCopy.checkValidMove(i):
                boardCopy.update_board(i, notPlayer)
                if boardCopy.checkWinner():
                    # print("blocking")
                    return i

        for i in range(1, 10):
            boardCopy = deepcopy(board)
            if boardCopy.checkValidMove(i) and self.checkForkMove(boardCopy, player, i):
                return i

        for i in range(1, 10):
            boardCopy = deepcopy(board)
            if boardCopy.checkValidMove(i) and self.checkForkMove(boardCopy, notPlayer, i):
                return i

        middle = [5]
        cornerMoveList = [1, 3, 7, 9]
        edgeMoveList = [2, 4, 6, 8]

        shuffle(cornerMoveList)
        shuffle(edgeMoveList)

        if self.numberOfFilledSquares(board) == 0:
            return cornerMoveList[0]

        possibleMoves = middle + cornerMoveList + edgeMoveList

        for i in possibleMoves:
            if board.checkValidMove(i):
                return i

        return 0


    def numberOfFilledSquares(self,board):
        """
        This function checks the board for how many squares that are not used
        :return: square
        :rtype: int
        """
        square = 0
        for i in range(0, 9):
            if board.board[i]!=0:
                square=square+1
        return square
