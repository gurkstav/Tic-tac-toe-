import gameplatform as g
from Player import PlayerAI

#Intiate Player1 and player2
player1 = g.RealPlayer('foo', 'X')
player2 = g.RealPlayer('bar', 'O')
game = g.Game(player1, player2)

# Initiate AI and Players
Playerone = g.PlayerAI("Player",False,3)
AIplayer1 = g.PlayerAI("AI",True,1)
AIplayer2 = g.PlayerAI("AI",True,2)
AIplayer3 = g.PlayerAI("AI",True,3)
AIdiff1 = g.AIGame(Playerone,AIplayer1)
AIdiff2 = g.AIGame(Playerone,AIplayer2)
AIdiff3 = g.AIGame(Playerone,AIplayer3)

ask = True
while ask == True:
	playerchoice = input('Do you wish to play vs a Player (P) or Computer (C)').strip()
	if(playerchoice == 'P' or playerchoice == 'p'):
		print("You will now play vs another player")
		ask = False
		winner = game.enter_game_loop()

	if(playerchoice == 'c' or playerchoice == 'C'):
		while ask == True:
			AIdifficulity = input('Which difficulity do you want to play against (1-3)').strip()
			if(AIdifficulity == '1'):
				print("You will now play vs a computer on difficulity 1")
				ask = False
				winner = AIdiff1.startGame()
			if(AIdifficulity == '2'):
				print("You will now play vs a computer on difficulity 2")
				ask = False
				winner = AIdiff2.startGame()
			if(AIdifficulity == '3'):
				print("You will now play vs a computer on difficulity 3")
				ask = False
				winner = AIdiff3.startGame()
