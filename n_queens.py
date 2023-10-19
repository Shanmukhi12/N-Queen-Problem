import numpy as np
import random
from board import Board ,Queen , Hill_Climbing ,HC_Sideways_Move ,\
                    Random_Restart_Hill_Climbing , Random_Restart_Sideways


board_size = int(input("Enter the value for number of queens in n-Queen problem: "))
runtime = int(input("Enter Runtime: "))


Board.set_size(board_size)




def create_board():
    start=[]
    for i in range(board_size):
        start.append( Queen(random.randint(0,board_size-1) ,i))
    return start    

hill_climbing_sum_success=0
hill_climbing_average_success=0
hill_climbing_success_steps=0
hill_climbing_average_success_steps=0
hill_climbing_fail_steps=0
hill_climbing_average_fail_steps=0

side_moves_sum_success=0
side_moves_average_success=0
side_moves_success_steps=0
side_moves_average_success_steps=0
side_moves_fail_steps=0
side_moves_average_fail_steps=0

random_restart_hill_climbing_sum_success=0
random_restart_hill_climbing_average_success=0
random_restart_hill_climbing_success_steps=0
random_restart_hill_climbing_average_success_steps=0
random_restart_hill_climbing_count=0

random_restart_side_moves_sum_success=0
random_restart_side_moves_average_success=0
random_restart_side_moves_success_steps=0
random_restart_side_moves_average_success_steps=0
random_restart_side_moves_count=0


count_for_HC=0
count_for_HC_with_sideways=0
random_values_for_HC= random.sample(range(10,runtime),8)
random_values_for_HC.sort()

for current_test in range(1,runtime+1):
    initial_board= create_board()
    
    hill_climbing= Hill_Climbing(initial_board)
    random_restart_hill_climbing = Random_Restart_Hill_Climbing(initial_board)
    sideways_move= HC_Sideways_Move(initial_board)
    random_restart_sideways_move= Random_Restart_Sideways(initial_board)
    
    hill_climbing_board= hill_climbing.climbing_algorithm()
    random_restart_hill_climbing_board = random_restart_hill_climbing.climbing_algorithm(initial_board)
    sideways_move_board= sideways_move.climbing_algorithm()
    random_restart_sideways_move_board= random_restart_sideways_move.climbing_algorithm(initial_board)
    
    #Hill Climbing Search
    
    if hill_climbing_board.calculate_heuristic()==0:
        hill_climbing_sum_success+=1
        hill_climbing_success_steps= hill_climbing.get_steps()
        hill_climbing_average_success_steps+=hill_climbing_success_steps
        
    else:
        hill_climbing_fail_steps=hill_climbing.get_steps()
        hill_climbing_average_fail_steps += hill_climbing_fail_steps

    temp = ["First","Second","Third","Fourth"]
    
    if count_for_HC<4:
        if current_test==random_values_for_HC[count_for_HC]:
            print("Search sequences for {} random initial configuration in Hill Climbing Search".format(temp[count_for_HC]))
            x = hill_climbing.printList()
            hill_climbing.print_path(x)
            print("Path cost for {} random initial configuration in Hill Climbing Search : {}".format(temp[count_for_HC],len(x)))
            print("\n")
            count_for_HC = count_for_HC+1

    #Random Restart Hill Climbing
    
    if random_restart_hill_climbing_board.get_heuristic() == 0 :
        random_restart_hill_climbing_sum_success+=1
        random_restart_hill_climbing_success_steps=random_restart_hill_climbing.get_step_count()
        random_restart_hill_climbing_average_success_steps+=random_restart_hill_climbing_success_steps
        random_restart_hill_climbing_count+=random_restart_hill_climbing.get_random_used()
                
    #Hill Climbing with sideways move
    if sideways_move_board.get_heuristic() == 0:
        side_moves_sum_success+=1
        side_moves_success_steps=sideways_move.get_step_count()
        side_moves_average_success_steps+=side_moves_success_steps

    else:
        side_moves_fail_steps=sideways_move.get_step_count()
        side_moves_average_fail_steps+=side_moves_fail_steps
    
    if count_for_HC_with_sideways<4:
        if current_test==random_values_for_HC[count_for_HC_with_sideways+4]:
            print("search sequences for {} random initial configuration in Hill-climbing search with sideways move".format(temp[count_for_HC_with_sideways]))
            x = hill_climbing.printList()
            hill_climbing.print_path(x)
            print("Path cost for {} random initial configuration in Hill Climbing Search with sideways move : {}".format(temp[count_for_HC_with_sideways],len(x)))
            print("\n")
            count_for_HC_with_sideways = count_for_HC_with_sideways+1

        
    #Random Restart without sideways move
    if random_restart_sideways_move_board.get_heuristic() == 0:
        random_restart_side_moves_sum_success+=1
        random_restart_side_moves_success_steps=random_restart_sideways_move.get_step_count()
        random_restart_side_moves_average_success_steps+= random_restart_side_moves_success_steps;
        random_restart_side_moves_count+=(random_restart_sideways_move.get_random_used());
                
                
hill_climbing_average_success=(hill_climbing_sum_success/runtime)*100
random_restart_hill_climbing_average_success = (random_restart_hill_climbing_sum_success / runtime)*100;
side_moves_average_success= (side_moves_sum_success/ runtime)*100
random_restart_side_moves_average_success =(random_restart_side_moves_sum_success / runtime)*100;


print("Hill Climbing Search:\n"

                    + "         Success Count       = " , hill_climbing_sum_success , "\n" 
                    + "         Success Rate        = " , hill_climbing_average_success , "%"+"\n"
                    + "         Fail Count          = " , (runtime - hill_climbing_sum_success) , "\n"
                    + "         Failure Rate        = " , (100 - hill_climbing_average_success) , "%"+"\n"
                    + "         Avg Success Steps   = " , (hill_climbing_average_success_steps/hill_climbing_sum_success) , "\n"
                    + "         Avg Failure Steps   = " , ((hill_climbing_average_fail_steps)/(runtime-hill_climbing_sum_success)));
print("\n")

print("Hill Climbing with Sideways Move :\n"

                    + "         Success Count       = " , side_moves_sum_success , "\n"
                    + "         Success rate        = " , side_moves_average_success , "%"+"\n"
                    + "         Fail count          = " , (runtime - side_moves_sum_success) , "\n"
                    + "         Failure rate        = " , (100 - side_moves_average_success) , "%"+"\n"
                    + "         Avg Success Steps   = " , (side_moves_success_steps/side_moves_sum_success) , "\n"
                    + "         Avg Failure Steps   = " , (np.float64(side_moves_average_fail_steps)/(runtime-side_moves_sum_success)));

print("\n")


print("Random Restart Hill Climbing:\n"

                    + "         Success Count       = " , random_restart_hill_climbing_sum_success , "\n"
                    + "         Success rate        = " , random_restart_hill_climbing_average_success , "%"+"\n"
                    + "         Fail Count          = " , (runtime - random_restart_hill_climbing_sum_success) , "\n"
                    + "         Failure rate        = " , (100 - random_restart_hill_climbing_average_success) , "%"+"\n"
                    + "         Avg Success Steps   = " , ((random_restart_hill_climbing_average_success_steps)/runtime) , "\n"
                    + "         Avg Random Restart  =" , (random_restart_hill_climbing_count/runtime));

print("\n")


print("Random Restart Sideways : \n"

                + "         Success Count           = " , random_restart_side_moves_sum_success , "\n"
                + "         Success rate            = " , random_restart_side_moves_average_success , "%"+"\n"
                + "         Fail Count              = " , (runtime - random_restart_side_moves_sum_success) , "\n"
                + "         Failure rate            = " , (100 - random_restart_side_moves_average_success) , "%"+"\n"
                + "         Avg Success Steps       = " , ((random_restart_side_moves_average_success_steps)/runtime) , "\n"
                + "         Avg Random Restart      = " , (random_restart_side_moves_count)/runtime);

        