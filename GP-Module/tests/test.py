import unittest
from gameplatform import Player, Game, GameBoard

fresh_gameboard_string = """
1|2|3
-+-+-
4|5|6
-+-+-
7|8|9

             To chose a spot to place your
             marker enter the designated number (1-9)
 | | 
-+-+-
 | | 
-+-+-
 | | 
"""
full_gameboard_string = """
1|2|3
-+-+-
4|5|6
-+-+-
7|8|9

             To chose a spot to place your
             marker enter the designated number (1-9)
X|O|X
-+-+-
O|X|O
-+-+-
X|O|X
"""

class TestGame(unittest.TestCase):

    def setUp(self):
        self.player1 = Player('name1', 'X')
        self.player2 = Player('name2', 'O')

    def test_who_plays_first(self):
        c1 = 0
        c2 = 0
        game = Game(self.player1, self.player2)
        n_samples = 1000
        for i in range(n_samples):
            first = game.who_plays_first()
            if first == self.player1:
                c1 += 1
            elif first == self.player2:
                c2 += 1

        p = c1/n_samples
        self.assertTrue(0.4 < p and p < 0.6)

    def test_toggle_player(self):
        game = Game(self.player1, self.player2)
        previous_player = game.current_player
        game.toggle_player()
        current_player = game.current_player
        self.assertFalse(current_player == previous_player)

    def test_who_is_playing(self):
        game = Game(self.player1, self.player2)
        game.current_player = self.player1
        self.assertEqual(game.who_is_moving(), self.player1)

    def test_make_valid_move1(self):
        game = Game(self.player1, self.player2)
        gb = game.game_board
        game.who_plays_first()
        gb.update_board(game.who_is_moving(), 1)
        self.assertFalse(gb.is_space_free(1))
        self.assertTrue(gb.is_space_free(3))

    def test_make_valid_move2(self):
        game = Game(self.player1, self.player2)
        gb = game.game_board
        game.who_plays_first()
        gb.update_board(game.who_is_moving(), 1)
        game.toggle_player()
        gb.update_board(game.who_is_moving(), 2)
        game.toggle_player()
        gb.update_board(game.who_is_moving(), 3)
        game.toggle_player()
        gb.update_board(game.who_is_moving(), 4)
        game.toggle_player()
        gb.update_board(game.who_is_moving(), 5)
        game.toggle_player()
        gb.update_board(game.who_is_moving(), 6)
        game.toggle_player()
        gb.update_board(game.who_is_moving(), 7)
        game.toggle_player()
        gb.update_board(game.who_is_moving(), 8)
        game.toggle_player()
        self.assertFalse(gb.is_board_full())
        gb.update_board(game.who_is_moving(), 9)
        game.toggle_player()
        self.assertTrue(gb.is_board_full())

    def test_make_invalid_move1(self):
        game = Game(self.player1, self.player2)
        gb = game.game_board
        game.current_player = self.player1
        gb.update_board(game.who_is_moving(), 2)
        game.toggle_player()
        gb.update_board(game.who_is_moving(), 2)
        self.assertFalse(gb.is_space_free(2))        

class TestGameBoard(unittest.TestCase):

    def setUp(self):
        self.player1 = Player('player1', 'X')
        self.player2 = Player('player2', 'O')

    def test_represent_gameboard_fresh(self):
        game = Game(self.player1, self.player2)
        game.turn = 1
        self.assertEqual(str(game.game_board), fresh_gameboard_string)

    def test_represent_gameboard_with_pieces(self):
        game = Game(self.player1, self.player2)
        game.game_board.board = [
            'x', 'o', 'x',
            'o', 'x', 'o',
            'x', 'o', 'x'
        ]
        self.assertTrue(str(game.game_board), full_gameboard_string)

    def test_is_not_full(self):
        gameboard = GameBoard()
        self.assertFalse(gameboard.is_board_full())

    def test_is_board_full(self):
        gameboard = GameBoard()
        gameboard.board = [
            'x', 'o', 'x',
            'o', 'x', 'o',
            'x', 'o', 'x'
        ]
        self.assertTrue(gameboard.is_board_full())

    def test_is_there_a_winner(self):
        gameboard = GameBoard()
        gameboard.board = [
            'x', 'o', 'x',
            'o', 'x', 'o',
            'x', 'o', 'x'
        ]
        self.assertTrue(gameboard.is_there_a_winner('x'))

    def test_is_space_free(self):
        gameboard = GameBoard()
        gameboard.board = [
            'x', 'o', 'x',
            'o', ' ', 'o',
            'x', 'o', 'x'
        ]
        self.assertTrue(gameboard.is_space_free(5))
        self.assertFalse(gameboard.is_space_free(6))

class StrategyPlayer(Player):
        def __init__(self, name, piece_string, moves):
            super().__init__(name, piece_string)
            self.moves = (move for move in moves)

        def get_move(self, gameboard):
            return(next(self.moves))

class TestWholeGameRun(unittest.TestCase):

    def test_winner(self):
        losing_player = StrategyPlayer('loser', 'X', [1, 4, 7])
        winning_player = StrategyPlayer('winner', 'O', [2, 5, 8])

        game = Game(losing_player, winning_player);
        game.current_player = winning_player
        winner = game.enter_game_loop()
        self.assertEqual(winner, winning_player)

    def test_draw(self):
        player1 = StrategyPlayer('player1', 'X', [1, 3, 6, 8])
        player2 = StrategyPlayer('player2', 'O', [2, 4, 5, 7, 9])

        game = Game(player1, player2)
        game.current_player = player2
        result = game.enter_game_loop()
        self.assertEqual(result, None)
