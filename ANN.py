from numpy import exp,zeros ,random, dot
import GameClass
import BoardEnvironment as BE

from AgentObject import oksearch,Agent

#single layer nearal netowrk
#   intputs           output
#   x_1 
#   x_2     
#   .           
#   .                outputNode 
#   .
#   .  
#   x_n

class ANN(oksearch, Agent):
        def __init__(self):
            self.c=7    #This is the number of inputs into the network. 7 choices in connect four
            self.r=6    # number of rows ib the board
            self.inputs=zeros(7) #the number of inputs
            
            # randomly generated weights that is weight x 1. "weights"rows and 1 column 
            # this is weighted matrix that will be multiplied by the input 
            self.W1=2*random.rand(self.c,1)
                

            def program(self, board):
                s =oksearch()
                if(s.boardempty(board)):
                    return 3
                    
                self.train(board, 4, 'X')
                moves = self.move(board, 4, 'X')
                #s.listOrder(board, 4, 'X')
                #print('final move')
                #print(moves)
                return moves
            
            self.program = program
        
        #sigmoid function
        def activationFunction(self,x):
            return (0.7/(1+exp(-x)))
        
        
        # The derivative of the Sigmoid function.
        #gradient of acivation function
        def functionDerivative(self, x):
            return exp(-x)/((exp(-x)+0.7)**2)
        
        
        
        # trains the ANN.
        def train(self,board, depth, player):
            
            needToLearn=True
            
            while needToLearn:
                AI_Move= self.feedforward(board, depth, player) # what the computer thought was the best move
                best_move=(self.moves( board, depth, player)/10.0)# what the search algorithm got
                
                # the error
                error= AI_Move - best_move
                print str(error) 
            
                adjustment = dot(self.inputs.T , (error * self.functionDerivative(AI_Move)))

                self.W1 += adjustment
                if error<0.001:
                    needToLearn=False
                
                    
          #
        def feedforward(self, board, depth, player):
           # gives the value of each move in a pair(value, move) 
            generateInputs=self.listOrder( board, depth, player)
            
            
            #extract each move
            for i in  range(len(generateInputs)):
                self.inputs[i]=(float((generateInputs[i][0])/100.0))
            
             
            # feed forward
            r1=dot(self.inputs,self.W1)
            tMove=self.activationFunction(r1)
            
            return tMove
            
            
        def move(self, board, depth, player):
            
            move=int(self.feedforward(board, depth, player) *10) 
            print str(move) 
            while not self.valid_move(board,move):
                move=int(self.feedforward(board, depth+1, player) *10) 
                print str(move)   
            
            return move
        
            
            
if __name__ == '__main__':
    a = BE.BasicEnvironment()
    ok = ANN()
    playAgain=True
    
    while playAgain:
        row = input('Go First or Second. Input 1 or 2: ')
        order = (int(row)-1 )
        a.play(ok, order) 
        row = input('play Again? maybe the computer will do better[Y/N]')    
            
        if row =='N':
                playAgain=False
            
    
            