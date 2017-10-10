class PlayerAI:

    def __init__(self, name, isAI, level, piece_string):
        self.name = name
        self.isAI = isAI
        self.AIlevel = level
        self.piece_string = piece_string

    def __str__(self):
        return(self.piece_string)

    def getPlayerName(self):
        return self.name

    def setPlayerName(self, name):
        self.name=name

    def getIsAI(self):
        return self.isAI

    def setIsAI(self, AI):
        self.isAI = AI

    def getAIlevel(self):
        return self.AIlevel

    def setIsAI(self, AIlevel):
        self.AIlevel = AIlevel
