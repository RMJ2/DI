# import random
# # library that we use in order to choose 
# # on random words from a list of words
 
# name = input("What is your name? ")
# # Here the user is asked to enter the name first
 
# print("Good Luck ! ", name)
 
# words = ['rainbow', 'computer', 'science', 'programming', 
#          'python', 'mathematics', 'player', 'condition', 
#          'reverse', 'water', 'board', 'geeks'] 
 
# # Function will choose one random
# # word from this list of words
# word = random.choice(words)
 
 
# print("Guess the characters")
 
# guesses = ''
 
# # any number of turns can be used here
# turns = 12
 
# while turns > 0:
     
#     # counts the number of times a user fails
#     failed = 0
     
#     # all characters from the input
#     # word taking one at a time.
#     for char in word: 
         
#         # comparing that character with
#         # the character in guesses
#         if char in guesses: 
#             print(char)
             
#         else: 
#             print("_")
             
#             # for every failure 1 will be
#             # incremented in failure
#             failed += 1
             
 
#     if failed == 0:
#         # user will win the game if failure is 0
#         # and 'You Win' will be given as output
#         print("You Win") 
         
#         # this print the correct word
#         print("The word is: ", word) 
#         break
     
#     # if user has input the wrong alphabet then
#     # it will ask user to enter another alphabet
#     guess = input("guess a character:")
     
#     # every input character will be stored in guesses 
#     guesses += guess 
     
#     # check input with the character in word
#     if guess not in word:
         
#         turns -= 1
         
#         # if the character doesn’t match the word
#         # then “Wrong” will be given as output 
#         print("Wrong")
         
#         # this will print the number of
#         # turns left for the user
#         print("You have", + turns, 'more guesses')
         
         
#         if turns == 0:
#             print("You Loose")



import random, time
fruits = ['pear', 'mango', 'apple', 'banana', 'apricot', 'pineapple','cantaloupe', 'grapefruit','jackfruit','papaya']
superHeroes = ['hawkeye', 'robin', 'Galactus', 'thor', 'mystique', 'superman', 'deadpool', 'vision', 'sandman', 'aquaman']
userGuesslist = []
userGuesses = []
playGame = True
category = ""
continueGame = "Y"

name = input("Enter your name")
print("Hello", name.capitalize(), "let's start playing Hangman!")
time.sleep(1)
print("The objective of the game is to guess the secret word chosen by the computer.")
time.sleep(1)
print("You can guess only one letter at a time. Don't forget to press 'enter key' after each guess.")
time.sleep(2)
print("Let the fun begin!")
time.sleep(1)

while True:
    #Choosing the Secret word
    while True:
        if category.upper() == 'S':
            secretWord = random.choice(superHeroes)
            break
        elif category.upper() == 'F':
            secretWord = random.choice(fruits)
            break
        else:
            category = input("Please select a valid categary: F for Fruits / S for Super-Heroes; X to exit")

        if category.upper() == 'X':
            print("Bye. See you next time!")
            playGame = False
            break

    if playGame:
        secretWordList = list(secretWord)
        attempts = (len(secretWord) + 10)

        #Utility function to print User Guess List
        def printGuessedLetter():
            print("Your Secret word is: " + ''.join(userGuesslist))


        #Adding blank lines to userGuesslist to create the blank secret word
        for n in secretWordList:
            userGuesslist.append('_')
        printGuessedLetter()

        print("The number of allowed guesses for this word is:", attempts)


        #starting the game
        while True:

            print("Guess a letter:")
            letter = input()

            if letter in userGuesses:
                print("You already guessed this letter, try something else.")

            else:
                attempts -= 1
                userGuesses.append(letter)
                if letter in secretWordList:
                    print("Nice guess!")
                    if attempts > 0:
                        print("You have ", attempts, 'guess left!')
                    for i in range(len(secretWordList)):
                        if letter == secretWordList[i]:
                            letterIndex = i
                            userGuesslist[letterIndex] = letter.upper()
                    printGuessedLetter()

                else:
                    print("Oops! Try again.")
                    if attempts > 0:
                        print("You have ", attempts, 'guess left!')
                    printGuessedLetter()


            #Win/loss logic for the game
            joinedList = ''.join(userGuesslist)
            if joinedList.upper() == secretWord.upper():
                print("Yay! you won.")
                break
            elif attempts == 0:
                print("Too many Guesses!, Sorry better luck next time.")
                print("The secret word was: "+ secretWord.upper())
                break

        #Play again logic for the game
        continueGame = input("Do you want to play again? Y to continue, any other key to quit")
        if continueGame.upper() == 'Y':
            category = input("Please select a valid categary: F for Fruits / S for Super-Heroes")
            userGuesslist = []
            userGuesses = []
            playGame = True
        else:
            print("Thank You for playing. See you next time!")
            break
    else:
        break