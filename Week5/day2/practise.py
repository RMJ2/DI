# foods = ['Cucumber', 'tomato', 'tuna', 'tehina']

# for f in foods[::2]: 
#     print(f)
#     print(len(f))


# for x in range(1,500000,10000):
#     print(x)


# example = 5

# while example < 10:
#     print (example)
#     example += 1


# magic_number = 26

# for n in range(101):
#     if n is magic_number:
#         print(n, ' is the magic number')
#         break
#     else:
#         print(n)


# username = input('what is you name: ')
# age = int(input('what is your age? '))
# year = str((2021 - age)+100)
# print(f'{username} will be 100 years old in the year {year}')


# num = int(input('Input a number: '))
# mod = num % 2
# if mod > 0: 
#     print('number is odd')
# else: 
#     print('number is even')


# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# n = []
# user = int(input('enter a number: '))

# n.append(user) 
# # print(n)

# for n in a:
#     if n <= user:
#         print (n)


# num = int(input("Please choose a number to divide: "))

# listRange = list(range(1,num+1)) 

# divisorList = []

# for number in listRange:
#     if num % number == 0:
#         divisorList.append(number)

# print(divisorList)


# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# c = []

# for i in b:
#     if i in a:
#         c.append(i)
# print(c)


# string = 'example'
# for c in string:
#     print('one letter: ' + c) 

# s = string[0:5]
# print(s) 

# def isPalindrome(s):
#     return s ==s[::-1]

# s = input('Write here to check for Palindrome: ')
# ans = isPalindrome(s)

# if ans:
#     print('Yes')
# else: 
#     print('No')



# years_of_birth = [1990, 1991, 1990, 1993, 1995]
# # ages = []
# # for year in years_of_birth:
# #     ages.append(2021 - year)
# #     print(ages)
# ages = [2021 - year for year in years_of_birth]
# print(ages)

# a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# # for num in a: 
# #     if num % 2 == 0: 
# #         print(num, end = ' ')
# even = [num for num in a if num % 2 == 0]
# print(even)

# a = 0
# while (a < 5):
#     print(a)
#     a +=1

# quit = input('type "enter to quit:')
# while quit != "enter":
#     quit = input('type "enter to quit:')


# import random

# while True:
#     user_action = input("Enter a choice (rock, paper, scissors): ")
#     possible_actions = ["rock", "paper", "scissors"]
#     computer_action = random.choice(possible_actions)
#     print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

#     if user_action == computer_action:
#         print(f"Both players selected {user_action}. It's a tie!")
    elif user_action == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user_action == "paper":
        if computer_action == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_action == "scissors":
        if computer_action == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")
    
    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break



a = [5, 10, 15, 20, 25]

# b = [a[0], a[-1]]
# print(b)

def first_last(numbers): 
    global new_list
    new_list.append(numbers[0])
    new_list.append(numbers[-1])

new_list = []
first_last(a)

for a in new_list:
    print('New list contains:' + str(a)) 





