
import random

wordslist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share', 'credit card', 'rush', 'south']
word = random.choice(wordslist) 

    ### YOUR CODE STARTS FROM HERE ###
# 1. a loop for everytime it runs will take a letter. 
# 2. if a letter is in a word or not. 

username = input('what is your name?')

print('Good Luck', username)


# step 1. 
guesses = ''                                # str for letter guesses

turns = 2                                   # number of turns allocated 

# step 2. 

while turns > 0:                            # while loop for game.

    failed = 0                              # counts number of failed attempts

    for letter in word:                     # letter guess in word 
        if letter in guesses:               # if letter picked in guesses
            print(letter)                   # print the letter
        else: 
            print('_')
            failed += 1

    if failed == 0:                         #if failed is equal to 0 print ('You win + the word is '') then break
        print('You win')
        print('The word is', word)
        break

    guess = input('pick a letter: ')        # guess = new input letter

    guesses += guess                        # guesses = guesses + guess. each guess will add a turn from countdown. 

    if guess not in word:                   # if guess not in word

        turns -= 1                          # turns = turns - 1
        
        print('Wrong')                              # if you guess wrong print(wrong, you have x amount of turns left.)
        print(f'You have {turns} more guesses.')

        if turns == 0:
            print('You Loose')                      # if turns == 0, print you loose









# 1.the computer:   
#     chooses a selection of random words in secret. 
#     1. word will be chosen per game. 
#     2. the computer will allocate x amount of points to the player.  def points()
#         if these points run out they will be executed. 
#         if they guess the letters correct, they can live. 


# 2. the user: 
#     while the game is still running the user will be able to ask.
#     write a letter into the program 
#         if the letter is correct, it is shown. 
#         elif the letter is wrong, a point is taken away. 
        

# game_in_progress = True
# while game_in_progress:
#     if input(continue)
#     elif: break (end of game - loser)
#     else: break (end of game - winner)
        


