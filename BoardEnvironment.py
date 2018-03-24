import GameClass
import AgentObject


class Environment():

    def __init__(self):
        """creating game as environment"""
        self.objects = []; self.agents = []

    def percept(self, agent):
	   """TBA"""
    def step(self):
	"""TBA"""

    def execute_action(self, agent, action):
	    """ TBA"""
	    
    def run(self):
        """TBA"""
    
    def play(self, agent):
        """ TBA"""
        
    def step(self):
        """TBA"""
            
class BasicEnvironment(Environment):
    def __init__(self):
        """creating game as environment"""
        Environment.__init__(self)
        self.game = GameClass.Game() # sets up game
        self.board = self.game.getBoard() # gets memory of board #
        
    def execite_action(self, agent, action):
        self.game.insert(int(action),  'X') # puts in col that and marks it as robot   
            
    def play(self, agent, order):
        print("You = 'O' and Robot = 'X'")
        Win = False # checks if the game is won
        i = order # turn checker
        while(Win == False):
            if i == 0:
                self.game.printBoard()
                row = input('Your turn: ')
                self.game.insert(int(row) - 1, 'O') # players insert assuming he puts it in correct
                Win = self.game.CheckWin('O')
                i = 1
            else:
                self.step(agent) # gets the call to the agent's move
                Win = self.game.CheckWin('X')
                i = 0    
            if(self.game.full()):
                i = 2
                Win = True
                
        print('')
        if(i == 1): # selects winner
            print("PLAYER WON!!")
        elif(i == 2):
            print("Tie Game!!")
        else:
            print("ROBOT WON!!")
        print('')
        self.game.printBoard()
        
        """adding playablilty here"""
    def step(self, agent):
        temp = self.board
        action = agent.program(agent, temp) # takes agents move from memory
        self.execite_action(agent, action) # does action form agent
        """make the agent make a move"""


if __name__ == '__main__':
    a = BasicEnvironment()
    #simple = AgentObject.RandomAgent()
    #ok = AgentObject.OkAgent()
    KB = AgentObject.KB()
    row = input('Go First or Second. Input 1 or 2: ')
    order = (int(row)-1 )
    a.play(KB, order)
    
    