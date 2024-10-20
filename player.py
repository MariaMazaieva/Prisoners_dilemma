
import random
COOPERATE = False  # Define COOPERATE as False
DEFECT = True      # Define DEFECT as True

class MyPlayer:
    '''Hrac hraje posledni tah defect, ostatni - random, je moznost detekce strategii'''

    def __init__(self, payoff_matrix, number_of_iterations = 0):
        self.payoff_matrix = payoff_matrix
        self.number_of_iterations = number_of_iterations
        self.history =  []
        self.first_values()
        self.cur_iteration = 0
        self.my_points = 0 
        self.opponent_points = 0 
        self.avarage_value()                 #call function to read matrix values
        

    def first_values(self):
        #ziskavam hodnoty matrice sveho hrace 
        self.C_1 = self.payoff_matrix[0][0][0] #First row, first parentheses, first number
        self.C_2 = self.payoff_matrix[0][1][0]
        self.C_3 = self.payoff_matrix[1][0][0]
        self.C_4 = self.payoff_matrix[1][1][0]

   
    def select_move (self):
        self.cur_iteration += 1
        print(self.cur_iteration, self.number_of_iterations)
        
        if (self.defect_last_move() == DEFECT): 
            return DEFECT
        
        if (self.detect_copycat()):
            return self.copy_cat()  
            
        if(self.detect_always_cooparate()):
            return DEFECT
        
        if(self.detect_always_defect()):
            return DEFECT
        
        if (self.my_points > self.opponent_points):
            return DEFECT
        
        else:
            return self.random_func() #standart strategy
        
        
       
    '''Check for copycat strategy within first 5 rounds'''
    def detect_copycat(self):
        count = 0
        if len(self.history) > 5:
            for i in range(len(self.history)-5, len(self.history)):
                if self.history[-i][1] == self.history[-i-1][0]:
                    count +=1
                if count == 5:
                    return True #Je copycat
        return False
                

    #self.history[-1][1]  = -1 is last  parentheses, 1 is opponents move
        
    def detect_always_defect(self):
        count = 0
        if len(self.history) > 5:
            for i in range(len(self.history)-5, len(self.history)):
                if self.history[-i][1] == DEFECT:
                    count +=1
                if count == 5:
                    return True #Je always DEFECT
        return False
    
    def detect_always_cooparate(self):
        count = 0
        if len(self.history) > 5:
            for i in range(len(self.history)-5, len(self.history)):
                if self.history[-i][1] == COOPERATE:
                    count +=1
                if count == 5:
                    return True #Je always COOPERATE
        return False
                

    def copy_cat(self):
        return self.opponent_last_move()
        
        
    def random_func (self):
        value = random.randint(0,1)
        return bool(value)
    
    def defect_last_move (self):
        print(self.cur_iteration, self.number_of_iterations)
        if self.cur_iteration   ==  self.number_of_iterations:
            return DEFECT 
        
    
    '''Analyz matrix and then make a choice'''
    
    def avarage_value(self):
        if ((self.C_1 + self.C_2)/2) > ((self.C_3 + self.C_4)/2):
            return COOPERATE == DEFECT, DEFECT == COOPERATE 
            #Change values if matrix is reversed 
         
        
    def always_defect(self):
        return DEFECT


    '''Getting my last move and opponents'''
   
    def my_last_move(self):
        if self.history:
             return self.history[-1][0]
        return DEFECT
       
        
    
    def opponent_last_move(self):
        if self.history:
            return self.history[-1][1] 
        return COOPERATE
    
    """Keep aomunt of points"""

    def points(self,my_move, opponent_move):
        my_move_points = self.payoff_matrix[my_move][opponent_move][0]
        opponent_move_points = self.payoff_matrix[my_move][opponent_move][1]

        self.my_points += my_move_points
        self.opponent_points += opponent_move_points

    '''Getting points'''   
    def get_my_points(self):
        return self.my_points
    
    def get_opponent_points(self):
        return self.opponent_points
             
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