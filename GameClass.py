class Game:
	def __init__ (self, cols = 7, rows = 6, requiredToWin = 4):
		"""Create a new game with empty board"""
		self.c = cols
           	self.r = rows
		self.win = requiredToWin
		self.board = [['.'] * rows for _ in range(cols)]

	def insert(self, c, player):
	    """
	    trys to insert into the board and if the col is full
	    they get messages and get's nother try in valid row
	    """
            for i in range(0,self.r): # checks for open spot
                if(self.board[c][self.r - 1 - i] == '.'):
                    self.board[c][self.r - 1 - i]= player
                    break
                        
        def getBoard(self):
            return self.board

	def printBoard (self):
		"""Print the board."""
		print('  '.join(str(x+1) for x in range(self.c)))
		for y in range(self.r):
			print('  '.join(str(self.board[x][y]) for x in range(self.c)))
                print('____________________')
                
        def full(self):
            for x in range(self.r):
                if(self.board[x][0] == '.'):
                    return False
            return True
                        
        def CheckWin(self, player):
        # check horizontal spaces
            for y in range(self.r):
                for x in range(self.c - 3):
                    if self.board[x][y] == player and self.board[x+1][y] == player and self.board[x+2][y] == player and self.board[x+3][y] == player:
                        return True

            # check vertical spaces
            for x in range(self.c):
                for y in range(self.r - 3):
                    if self.board[x][y] == player and self.board[x][y+1] == player and self.board[x][y+2] == player and self.board[x][y+3] == player:
                        return True

            # check / diagonal spaces
            for x in range(self.c - 3):
                for y in range(3, self.r):
                    if self.board[x][y] == player and self.board[x+1][y-1] == player and self.board[x+2][y-2] == player and self.board[x+3][y-3] == player:
                        return True

    # check \ diagonal spaces
            for x in range(self.c - 3):
                for y in range(self.r - 3):
                    if self.board[x][y] == player and self.board[x+1][y+1] == player and self.board[x+2][y+2] == player and self.board[x+3][y+3] == player:
                        return True

            return False