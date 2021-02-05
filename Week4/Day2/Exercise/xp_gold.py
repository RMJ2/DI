# Exercise 1 : Concatenate Lists - DONE
# Write a script that concatenate two lists together without using the + sign.

# list_1 = [1,2,3,4]
# list_2 = [5,6,7,8]

# for i in list_2:
#     list_1.append(i)

# print(list_1)

# Exercise 2: Greatest Number   DONE
# Take three numbers from the user and print the greatest number.
#     Test Data
#     Input the 1st number: 25
#     Input the 2nd number: 78
#     Input the 3rd number: 87

#     The greatest number is: 87

# create empty list for the int(input) 
# ask the user for 3 numbers 
# if the highest number is x, select it


# num1 = int(input('select a number: '))
# num2 = int(input('select s second number: '))
# num3 = int(input('select a third number: '))

# if (num1 > num2) and (num1 > num3):
#     largest = num1
# elif (num2 > num1) and (num2 > num3):
#     largest = num2
# else:
#     largest = num3

# print(f'the largest number is: {largest}')



# Exercise 3 : The Alphabet - DONE
# Create a string of all the letters in the alphabet
# Loop over each letter and print a message that contains the letter and whether its a vowel or a consonant

# alphabet = "abcdefghijklmnopqrstuvwxyz"
# vowels = "aeiou"
# for letter in alphabet:
# 	if letter in vowels:
# 		print(letter, "is a vowel")
# 	else:
# 		print(letter, "is a consonant")
   


# Exercise 4 : - STUCK
# names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
# 1. Write a script with the list of names provided. This code should ask the user for input
# * if the input exists in the list print the index of the first occurence
# Example: if input is ‘Cortana’ we should be printing the index 1  

# 1. list of names 
# 2. for loop the name of names 
# 3. use the for loop to get the index
# 4. attach the index to the print for chosen name. 

# names= ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']

# selected_name = input(f'pick a name: {names}')

# for name in names: 
#     if name == selected_name:
#         print(names.index(selected_name))




# Exercise 5 : Words And Letters
# Take 7 words as input from a user and store them for use in a list named words
#   should not be done on 7 lines
#   Mad props if you can do it in one :)
# Ask a single character input from the user and store it in a variable letter
# Tell the user what index letter is in each item in words
# If the letter doesn’t exist in a given word, print a friendly message saying so

# words = []

# for x in range(1,8):
#     words.append(input(f'enter word {x}: ')) 

# print(words) 

# letter = input('enter a letter: ')

# for word in words: 
#     if letter in word: 
#         print(word.index(letter))

# Exercise 6 :  DONE
# Make a list of the numbers from one to one million, and then use min() and max() to make sure your list actually starts at one and ends at one million. Also, use the sum() function to see how quickly Python can add a million numbers .

# numbers = range(1,1000001)
# # print(min(numbers))
# # print(max(numbers))
# # print(sum(numbers))

# total = 0                   # sum()
# for number in numbers: 
#     total += number
#     print(total)


# Exercise 7 :
# Write a program which accepts a sequence of comma-separated numbers from the console and generate a list and a tuple which contains every number.
# Suppose the following input is supplied to the program: 34,67,55,33,12,98

# Then, the output should be:

# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')

# num = input('type 4 numbers: ')

# print(num.split(' '))
# print(tuple(num.split(' ')))




# Exercise 8 : Random Number
# Accept input from a user if its between 1 and 9 (including).
# Get a random number between 1 and 9. Hint: random module.
# Print a message if the user guessed the correct number or not.
# Bonus: use a menu to let the user keep guessing until he wants to quit
# Bonus 2: on exit tally up and display total games, wins and losses