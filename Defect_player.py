
import random
COOPERATE = False  # Define COOPERATE as False
DEFECT = True      # Define DEFECT as True

class MyPlayer:
    '''Hrac hraje posledni tah defect, ostatni - cooparate, je moznost strategii random'''

    def __init__(self, payoff_matrix, number_of_iterations = 0):
        self.payoff_matrix = payoff_matrix
        self.number_of_iterations = number_of_iterations
        self.history =  []
        self.first_values()
        self.cur_iteration = 0
        self.my_points = 0 
        self.opponent_points = 0 
        

    def first_values(self):
        #ziskavam hodnoty matrice sveho hrace 
        self.C_1 = self.payoff_matrix[0][0][0] #First row, first parentheses, first number
        self.C_2 = self.payoff_matrix[0][1][0]
        self.C_3 = self.payoff_matrix[1][0][0]
        self.C_4 = self.payoff_matrix[1][1][0]

   
    def select_move (self):
        return DEFECT
        
             
    def record_last_moves(self, my_last_move, opponent_last_move): 
        self.history.append([my_last_move,opponent_last_move])
        


if __name__ == "__main__" :
    payoff_matrix = ( ((4,4),(1,6)) , ((6,1),(2,2)) )
    Matrix_1 = MyPlayer(payoff_matrix,3)
    Matrix_1.select_move()
    
    

'''How self.history works
self.history = [
    [0, 1],  # Round 1: I Cooperated, Opponent Defected
    [1, 0],  # Round 2: I Defected, Opponent Cooperated
    [1, 1],  # Round 3: Both Defected
]
self.history[-1] refers to the last pair of moves, which is [1, 1] (Round 3).
self.history[-1][1] refers to the opponent's move in the last round, which is 1 (Defect).

'''