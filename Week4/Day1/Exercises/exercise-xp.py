## ------------ exercise 1 - Hello World *4 - DONE
# print('Hello world \n' *4)


## ------------ Exercise 2 - DONE
# Calculate the result of: (99^3) * 8

# print((99**3)*8)



## ------------ Exercise 3 - Whats the output? -DONE

# 1.  >>> 5 < 3     False
# 2.  >>> 3 == 3    True
# 3.  >>> 3 == "3"  False
# 4.  >>> "3" > 3   True
# 5. >>> "Hello" == "hello"     False

## ------------ Exercise 4 - Your computer Brand - DONE
# 1. Create a variable called computer_brand that contains the brand of your computer.
# 2. Insert and print the above variable in a sentence,like "I have a razer computer".

# computer_brand = "apple"
# print(f"I have a {computer_brand} computer")



## ------------Exercise 5 - Your information - DONE
# 1. Create a variable called name, and give it your name as a value (text)
# 2. Create a variable called age, and give it your age as a value (number)
# 3. Create a variable called shoe_size, and give it your shoe size as a value
# 4. Create a variable called info. Its value should be an interesting sentence about yourself, including your name, age, and shoe size. Use the variables you created earlier.
# 5. Have your code print the info message.
# 6. Run your code

# name = 'Joshua'
# age = 27 
# shoe_size = 44
# info = f'my name is {name} and i am {age}, my shoe size is {shoe_size}'
# print(info)



# # ------------Exercise 6 : A & B - DONE
# Given two variables a and b that you need to define, make a program that print Hello World only if a is greater than b.
# 
# a = 10
# b = 5
# if a > b: 
#     print('Hello World')


## ------------ Exercise 7 : Odd Or Even - DONE
# Write a script that asks the user for a number and determines whether this number is odd or even.

# num = int(input('Enter a number: '))

# if (num % 2) == 0:
#     print(f'{num} is Even number')
# else: 
#     print(f'{num} is Odd Number')


## ------------     Exercise 8 : What’s Your Name ? - DONE
# Write a script that asks the user for his name and determines whether or not you have the same name, print out a funny message based on the outcome

# my_name = 'Joshua'
# name = input('What is your name? ')
# if name == my_name:
#     print('You copied my nam')
# else: 
#     print('You arn\'t welcome here')



## ------------ Exercise 9 : Tall Enough To Ride A Roller Coaster - DONE
# Write a script that will ask the user for their height in inches, print a message if they can ride a roller coaster or not based on if they are taller than 145cm
# Please note that the input is in inches and you’re calculating vs cm, you’ll need to convert your data accordingly

# inches = int(input('What is your height in inches? '))
# cm = inches*2.54
# print(cm)

# if cm >= 145:
#     print('You can ride the roller coster')
# else:
#     print('You are too short')