import random as rand
from operator import itemgetter
import cs156_logic as cl
from utils_lpw import*
class Object:
    def __repr__(self):
        return '<%s>' % getattr(self, '__name__', self.__class__.__name__)

    def is_alive(self):
        """Objects that are 'alive' should return true."""
        return hasattr(self, 'alive') and self.alive

    def display(self, canvas, x, y, width, height):
        """Display an image of this Object on the canvas."""
        pass

class Agent(Object):
    """baise to make multiple agents off"""
    def __init__(self):
        def program(percept):
            return raw_input('Percept=%s; action? ' % percept)
        self.program = program
        self.alive = True

class KB(Agent):
    def __init__(self):
        Agent.__init__(self)
        self.c = 7
        self.r = 6
        self.following = False
        self.holdZugzwang = True 
        
        def program(self, board):
                s = KBsearch(self)
                if(s.boardempty(board)):
                   return 3
                moves = s.moves(board, self, 'X')
                return moves
            
        self.program = program
        
class KBsearch():
    def __init__(self, agent):
        self.c = 7
        self.r = 6
        self.kb = cl.PropKB()
        self.KB = cl.PropKB()
        self.agent = agent
    
   
    def hThreats(self, board):
        """Gives column with the highest threat"""
        self.Threat(board) #add any threats to KB
        for x in range(7):
            c = "C%d" % (x)
            for clause in self.kb.clauses:
                if self.kb.ask(cl.expr(c)) == {}: #find which threat to stop
                   self.uselessThreats(board, x)
        for x in range(7):
            c = "C%d" % (x)
            for clause in self.KB.clauses:
                if self.KB.ask(cl.expr(c)) == {}:
                    return x   
        return 0 #else no threats, proceed with holdZugzwang
        
    def uselessThreats(self, board, col):
        """Gives columns with no threat by columns, Id useless squares of O or X, columns which need one or more squares below it before a threat"""
        if col < 5 and col > 0:
            for r in range(1,6):
                if board[col-1][r] == "O"and board[col-1][r-1] != ".":
                    c = "C%d" % (col)
                    self.KB.tell(cl.expr(c))
                if board[col+1][r] == "O" and board[col+1][r-1] != ".":
                    c = "C%d" % (col)
                    self.KB.tell(cl.expr(c))
        if col == 0:
            for r in range(1,6):
                if board[col+1][r] == "O" and board[col+1][r-1] != ".":
                    c = "C%d" % (col)
                    self.KB.tell(cl.expr(c))
        if col == 5:
            for r in range(1,6):
                if board[col-1][r] == "O" and board[col-1][r-1] != ".":
                    c = "C%d" % (col)
                    self.KB.tell(cl.expr(c))
    
    def moves(self, board, agent, player):
        action = self.hThreats(board)
        if action != 0:
            return action #return move to stop threat
        else:
            for x in range(7):
                """check for rules to be held true for each possible move"""
                if not self.claimeven(board, x):
                    #doesnt hold true, move on to next col
                    next
                elif not self.baseinverse(board, x):
                    #doesnt hold true, move on to next col
                    next
                elif not self.lowinverse(board, x):
                    #doesnt hold true, move on to next col
                    next
                elif not self.vertical(board, x):
                    #doesnt hold true, move on to next col
                    next
                else:
                    return x
        #no holdZugzwang action, return random action
        """
        numbers = list(range(6))
        for n in range(6):
            if board[n][5] != ".":
                numbers.remove(n)
        """
        return rand.randrange(7)
    
    def claimeven(self, board, col):
        if(self.agent.holdZugzwang == True):
            for i in range(6):
                if board[col][i] == ".":
                    break
            row = i
            if row < 4:
                if board[col][row] == "." and board[col][row+1] == "." and (self.even(row+1)):
                    return True
        return False
    
    def baseinverse(self, board, col):
        if(self.agent.holdZugzwang == True):
            for i in range(6):
                if board[col][i] == ".":
                    break
            row = i
            if row < 4 and row > 1 and col > 1 and col < 5:
                if board[col][row] == "." and (board[col][row+1] == "." or board[col+1][row] == "." or board[col-1][row] == "." or board[col][row-1] == "." or board[col+1][row+1] == "." or board[col-1][row-1] == "." or board[col-1][row+1] == "." or board[col+1][row-1] == "."):
                    return True
            elif row < 4 and row > 0 and col == 0:
                if board[col][row] == "." and (board[col][row+1] == "." or board[col+1][row] == "." or board[col+1][row+1] == "." or board[col+1][row-1] == "."):
                    return True
            elif col == 6 and row < 4 and row > 0:
                if board[col][row] == "." and (board[col-1][row] == "." or board[col][row+1] == "." or board[col-1][row+1] == "." or board[col-1][row-1] == "."):
                    return True
            elif row == 0 and col > 0 and col < 5:
                if board[col][row] == "." and (board[col][row+1] == "." or board[col+1][row] == "." or board[col-1][row] == "." or board[col-1][row+1] == "." or board[col+1][row+1] == "."):
                    return True
            elif row == 0 and col == 0:
                if board[col][row] == "." and (board[col+1][row] == "." or board[col+1][row+1] == "." or board[col][row+1] == "."):
                    return True
            elif row == 0 and col == 6:
                if board[col][row] == "." and (board[col-1][row] == "." or board[col-1][row+1] == "." or board[col][row+1] == "."):
                    return True
            elif row == 5 and col < 5 and col > 0:
                if board[col][row] == "." and (board[col-1][row] == "." or board[col-1][row-1] == "." or board[col+1][row] == "." or board[col+1][row-1] == "." or board[col][row-1] == "."):
                    return True
            elif row == 5 and col == 0:
                if board[col][row] == "." and (board[col][row-1] == "." or board[col+1][row] == "." or board[col+1][row-1] == "."):
                    return True
            elif row == 5 and col == 6:
                if board[col][row] == "." and (board[col-1][row] == "." or board[col-1][row-1] == "." or board[col][row-1] == "."):
                    return True
        return False
            
    def lowinverse(self, board, col):
        if(self.agent.holdZugzwang == True):
            for i in range(6):
                if board[col][i] == ".":
                    break
            row = i
            if col < 5 and col > 0 and row < 4:
                if self.vertical(board, col, row) and (self.vertical(board, col+1, row) or self.vertical(board, col-1, row)):
                    return True
            if col == 6 and row < 4:
                if self.vertical(board, col, row) and self.vertical(board, col-1, row):
                    return True
            if col == 0 and row < 4:
                if self.vertical(board, col, row) and self.vertical(board, col+1, row):
                    return True
        return False
    
    def vertical(self, board, col):
        if (self.agent.holdZugzwang == True):
            for i in range(6):
                if board[col][i] == ".":
                    break
            row = i
            if row < 4:
                if (board[col][row] == ".") and (board[col][row+1] == ".") and (self.odd(row+1)):
                    return True
        return False
        
    def Threat(self, board):
        player = "O"
        for y in range(self.r):
            for x in range(self.c - 2):
                if board[x][y] == player and board[x+1][y] == player and board[x+2][y] == player:
                    if x > 0 and x < 4:
                        #Threat col-1
                        c = "C%d" % (x-1)
                        if self.kb.ask(cl.expr(c)) == {}:
                            pass
                        else:
                            self.kb.tell(cl.expr(c))
                        #Threat col+3
                        c = "C%d" % (x+3)
                        if self.kb.ask(cl.expr(c)) == {}:
                            pass
                        else:
                            self.kb.tell(cl.expr(c))
                    elif x == 0:
                        #Threat col+3
                        c = "C%d" % (x+3)
                        if self.kb.ask(cl.expr(c)) == {}:
                            pass
                        else:
                            self.kb.tell(cl.expr(c))
                    elif x == 4:
                        #Threat col-1
                        c = "C%d" % (x-1)
                        if self.kb.ask(cl.expr(c)) == {}:
                            pass
                        else:
                            self.kb.tell(cl.expr(c))
        for x in range(self.c):
            for y in range(self.r - 2):
                if board[x][y] == player and board[x][y+1] == player and board[x][y+2] == player:         
                    if y < 3:
                        #Threat row+3
                        c = "C%d" % (x)
                        if self.kb.ask(cl.expr(c)) == {}:
                            pass
                        else:
                            self.kb.tell(cl.expr(c))
        for x in range(self.c - 2):
            for y in range(2, self.r):                
                if board[x][y] == player and board[x+1][y-1] == player and board[x+2][y-2] == player:         
                    if x < 4 and x > 0 and y < 5 and y > 2:
                        #Threat col-1 row+1
                        c = "C%d" % (x-1)
                        if self.kb.ask(cl.expr(c)) == {}:
                            pass
                        else:
                            self.kb.tell(cl.expr(c))
                        #Threat col+3 row-3
                        c = "C%d" % (x+3)
                        if self.kb.ask(cl.expr(c)) == {}:
                            pass
                        else:
                            self.kb.tell(cl.expr(c))
                    elif y > 2 and x == 0:
                        #Threat col+3 row-3
                        c = "C%d" % (x+3)
                        if self.kb.ask(cl.expr(c)) == {}:
                            pass
                        else:
                            self.kb.tell(cl.expr(c))
                    elif x == 4 and y < 5:
                        #Threat col-1 row +1
                        c = "C%d" % (x-1)
                        if self.kb.ask(cl.expr(c)) == {}:
                            pass
                        else:
                            self.kb.tell(cl.expr(c))
        for x in range(self.c - 2):
            for y in range(self.r - 2):              
                if board[x][y] == player and board[x+1][y+1] == player and board[x+2][y+2] == player:         
                    if x < 4 and y < 3 and x > 0 and y > 0:
                        #Threat col-1 row-1
                        c = "C%d" % (x-1)
                        if self.kb.ask(cl.expr(c)) == {}:
                            pass
                        else:
                            self.kb.tell(c)
                        #Threat col+3 row+3
                        c = "C%d" % (x+3)
                        if self.kb.ask(cl.expr(c)) == {}:
                            pass
                        else:
                            self.kb.tell(c)
                    elif y == 0 and x < 4:
                        #Threat col+3 row+3
                        c = "C%d" % (x+3)
                        if self.kb.ask(cl.expr(c)) == {}:
                            pass
                        else:
                            self.kb.tell(c)
                    elif y > 0 and x == 4:
                        #Threat col-1 row-1
                        c = "C%d" % (x-1)
                        if self.kb.ask(cl.expr(c)) == {}:
                            pass
                        else:
                            self.kb.tell(c)
                
    def boardempty(self,board):
        for x in range(self.c):
            if(board[x][5] != "."):
                return False
        return True
    
    def odd(self, x):
        if (x % 2 == 0):
            return False
        else:
            return True
            
    def even(self, x):
        if (x % 2 == 0):
            return True
        else:
            return False