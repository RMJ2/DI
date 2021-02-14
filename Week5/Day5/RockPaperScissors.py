# import random 
# from cprint import cprint

# 

# while True: 
#     user_action = input('Enter an option, rock, paper or scissors: ')
#     possible_actions = ['rock', 'paper', 'scissors']
#     computer_actions = random.choice(possible_actions)
#     print(f'Your choice is {user_action}, Good luck')

#     if user_action == computer_actions: 
#         cprint.warn(f'Both players selected {user_action}, Its a tie!')

#     elif user_action == 'rock':
#         if computer_actions == 'scissors':
#             cprint.ok('Rock beats scissors, you win!')
#         else: 
#             cprint.fatal('Paper beats Rock, you lose!')

#     elif user_action == 'paper':
#         if computer_actions == 'rock':
#             cprint.ok('Paper covers Rock, you win!')
#         else: 
#             cprint.fatal('Scissors cuts Paper, you lose!')

#     elif user_action == 'scissors': 
#         if computer_actions == 'paper': 
#             cprint.ok('Scissors cuts paper, you Win!')
#         else: 
#             cprint.fatal(' Rock breaks scissors, you lose!')

#     answer = play_again1()
#     if answer == False: 
#         break 


    # play_again = input('Would you like to play again? select y/n: ')
    # if play_again.lower() == 'n':
    #     break 
    # elif play_again.lower() != 'y':
    #     print('Invlaid selection, select y/n: ')
        
    # else: 
    #     continue 

# -----
import random 
tools = ['r', 'p', 's']

def get_computer_move():
    random_tool = random.choice(tools)
    return random_tool


def get_user_move():
    while True:
        user_action = input('Select one of the following options to play: r, p, s: ')
        
        if user_action in tools:
            return user_action
        else:
            print('Invalid selection, try again.')


def get_result(my_move, computer_move):
    # 1. check the move of the user vs the computer
    # how do you check the move??? 
    # who wins:       draw        computer        player

    if my_move == computer_move:
        return ('Draw')

    if my_move == 'r': 
        if computer_move == 's':
            return 'computer' 
        return 'player' 
    
    if my_move == 's': 
        if computer_move == 'p':
            return 'player'
        return 'computer' 

    if my_move == 'p':
        if computer_move == 'r':
            return 'player'
        return 'computer' 

    
def play_again1(): 
    
    while True: 
        a = input('Enter y/n to continue: ')
        if a == 'y': 
            return True 
        elif a == 'n': 
            return False
        else:
            print('Invalid choice, enter y/n: ')



def main():
    cPoints = 0
    pPoints = 0

    _ = get_result(get_user_move(), get_computer_move())
    print(_ + ' wins')      

    if _  == 'computer':
        cPoints += 1
    elif _ == 'player':
        pPoints += 1 

    while play_again1():
        _ = get_result(get_user_move(), get_computer_move())
        print(_ + ' wins')       
        if _  == 'computer':
            cPoints += 1
        elif  _  ==  'player':
            pPoints+=1

    print('Computer:' + str(cPoints)  +  ' Player:'  +  str(pPoints))


    
    









