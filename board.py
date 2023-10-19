import numpy as np
import random
class Queen:
    
    def __init__(self,row,column):
        self.row=row
        self.column=column
        
    def check(self,q):
        return  self.row ==q.get_rows() or self.column==q.get_columns() or abs(self.column - q.get_columns()) == abs(self.row - q.get_rows())
    
    def move_down(self,steps):
        self.row = (self.row + steps) % Board.get_size();
        
    def get_rows(self):
        return self.row
    
    def get_columns(self):
        return self.column
    
    def stringConversion(self):
        return "(" + str(self.row) + ", " + str(self.column) + ")"
    
class Board:
    board_size=8

    def __init__(self):  
        self.state=[]
        self.next_board=[]
        self.h=0
        
    def Board(self,n):  
        for i in range(Board.board_size):
            self.state.append(Queen(n.state[i].get_rows(), n.state[i].get_columns()))
    
    
    def get_size():
        return Board.board_size
    
    def set_size(size):
        Board.board_size=size
        
    def create_board(self, initial_state):
        count=0
        for i in range(Board.board_size):
            for j in range(1,Board.board_size):
                new_board=Board()
                new_board.Board(initial_state)
                self.next_board.insert(count, new_board )
                self.next_board[count].state[i].move_down(j)
                self.next_board[count].calculate_heuristic()
                count+=1
    
        return self.next_board
    
    def calculate_heuristic(self):
        for i in range(Board.board_size-1):
            for j in range(i+1,Board.board_size):
                if (self.state[i].check(self.state[j])):
                    self.h+=1
        return self.h
    
    def get_heuristic(self):
        return self.h
    
    def compare(self,n):
        if(self.h<n.get_heuristic()):
            return -1
        elif(self.h>n.get_heuristic()):
            return 1
        else:
            return 0
    
    def set_state_board(self,s):
        for i in range(Board.board_size):
            self.state.append( Queen(s[i].get_rows(), s[i].get_columns()))
        
    def stringConversion(self):
        result=""
        board = np.zeros((Board.get_size(),Board.get_size()), dtype=str)
        for i in range(Board.board_size):
            for j in range(Board.board_size):
                board[i][j]="*"
        for i in range(Board.board_size):
            board[self.state[i].get_rows()][self.state[i].get_columns()]="Q"
        for i in range(Board.board_size):
            for j in range(Board.board_size):
                result+=board[i][j]
            result += "\n"
        return result



class Hill_Climbing:
    
    
    def __init__(self,s):  
        self.steps=0
        self.print_nodes=[]
        self.start_board= Board()
        start_state= []
        for i in range(Board.get_size()):
            start_state.append((Queen(s[i].get_rows(),s[i].get_columns())))
        self.start_board.set_state_board(start_state)
        self.start_board.calculate_heuristic()
    

    
    def climbing_algorithm(self):
        current_board=self.start_board
        
        while True:
            successors=current_board.create_board(current_board)
            exist_better = False
            self.print_nodes.append(current_board)
            self.steps+=1
            
            for i in range(len(successors)):
                if(successors[i].compare(current_board) < 0):
                    current_board=successors[i]
                    exist_better=True
                    
            if not exist_better:
                return current_board
    def printList(self):
        return self.print_nodes
    
    def print_path(self,print_nodes):
        for i in range(len(self.print_nodes)):
            print(self.print_nodes[i].stringConversion())
    
    def get_start_board(self):
        return self.start_board
    
    def get_steps(self):
        return self.steps



class HC_Sideways_Move:
    
    def __init__(self,s):
        first_state=[]
        self.initial=Board()
        self.steps=0
        self.print_nodes=[]
        for i in range(Board.get_size()):
            first_state.append((Queen(s[i].get_rows(),s[i].get_columns())))
        self.initial.set_state_board(first_state)
        self.initial.calculate_heuristic()
        
    def climbing_algorithm(self):
        current_board=self.initial
        count=0
        
        while True:
            successors=current_board.create_board(current_board)
            select_random_successors=[]
            
            exist_better =False;
            exist_best=False
            
            self.print_nodes.append(current_board)
            
            for i in range(len(successors)):
                if count==100:
                    break
                if(successors[i].compare(current_board) <= 0):
                    if(successors[i].compare(current_board) < 0):
                        count=0
                        select_random_successors=[]
                        current_board=successors[i]
                        exist_better=True
                        self.steps+=1
                    elif(successors[i].compare(current_board) == 0):
                        select_random_successors.append(successors[i])
                        
            if not exist_better and not not select_random_successors:
                
                current_board= select_random_successors[random.randint(0,len(select_random_successors))-1]
                exist_best=True
                count +=1
                self.steps+=1
            if not exist_best and not exist_better:
                
                return current_board
            
    def get_start_board(self):
        return self.initial
    
    def print_path(self,print_nodes):
        for i in range(len(self.print_nodes)):
            print(self.print_nodes[i].stringConversion())
            
    def printList(self):
        return self.print_nodes
    
    def get_step_count(self):
        return self.steps



class Random_Restart_Hill_Climbing:
    
    
    def __init__(self,s):  
        self.steps=0
        self.start=0
        self.steepest_ascent_object= Hill_Climbing(s)
        Random_Restart_Hill_Climbing.restart_used=1
        
    def climbing_algorithm(self,s):
        current_board=self.steepest_ascent_object.get_start_board()
        self.set_start_board(current_board)
        h= current_board.get_heuristic()
        self.steps=0
        
        while h!=0:
            next_board= self.steepest_ascent_object.climbing_algorithm()
            self.steps+= self.steepest_ascent_object.get_steps()
            h = next_board.get_heuristic()
        
            if h!=0:
                s=Random_Restart_Hill_Climbing.create_board()
                self.steepest_ascent_object= Hill_Climbing(s)
                Random_Restart_Hill_Climbing.restart_used+=1
            else:
                current_board=next_board
                self.steps-= self.steepest_ascent_object.get_steps()
                Random_Restart_Hill_Climbing.restart_used+=1
        return current_board
    
    
    def create_board():
        start=[]
        for i in range(8):
            start.append( Queen(random.randint(0,Board.get_size()-1) ,i))
        return start
    def set_start_board(self, current_board):
        self.start = current_board
    def get_step_count(self):
        return self.steps
    def get_random_used(self):
        return Random_Restart_Hill_Climbing.restart_used


class Random_Restart_Sideways:
    
    def __init__(self,s):  
        self.steps=0
        self.start=0
        self.sideways_move_object= HC_Sideways_Move(s)
        Random_Restart_Sideways.restart_used=1
        
    def climbing_algorithm(self,s):
        current_board=self.sideways_move_object.get_start_board()
        self.set_start_board(current_board)
        h= current_board.get_heuristic()
        self.steps=0
        
        while h!=0:
            next_board= self.sideways_move_object.climbing_algorithm()
            self.steps+= self.sideways_move_object.get_step_count()
            h = next_board.get_heuristic()
            
            if h!=0:
                s=Random_Restart_Sideways.create_board()
                self.sideways_move_object= HC_Sideways_Move(s)
                Random_Restart_Sideways.restart_used+=1
            else:
                current_board=next_board
        return current_board
    
    def create_board():
        start=[]
        for i in range(8):
            start.append( Queen(random.randint(0,Board.get_size()-1) ,i))
        return start
    
    def set_start_board(self, current_board):
        self.start = current_board
    def get_step_count(self):
        return self.steps
    def get_random_used(self):
        return Random_Restart_Sideways.restart_used
