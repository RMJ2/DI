# Exercise 1 : Favorite Numbers DONE
# 1. Create a set called my_fav_numbers with your favorites numbers.
# 2. Add two new numbers to it.
# 3. Remove the last one.
# 4. Create a set called friend_fav_numbers with your friend’s favorites numbers.
# 5. Concatenate my_fav_numbers and friend_fav_numbers to our_fav_numbers.

# my_fav_numbers = {5,7,15}
# friend_fav_numbers = {2,4,6}
# print(my_fav_numbers)
# my_fav_numbers.add(17)
# my_fav_numbers.add(20)
# my_fav_numbers.remove(20)

# # my_fav_numbers.extend(friend_fav_numbers)
# # all_friends = my_fav_numbers + friend_fav_numbers
# print(my_fav_numbers.union(friend_fav_numbers))






# Exercise 2: Tuple - DONE
# 1. Given a tuple with integers is it possible to add more integers to the tuple?
#   No


# Exercise 3: Print A Range Of Numbers
# 1. Use a for loop to print the numbers from 1 to 20, inclusive.

# for i in range (1,21): 
#     print(i)


# Exercise 4: Floats - DONE 
# 1. Recap – What is a float? What is the difference between an integer and a float?
# 2. Can you think of another way of generating a sequence of floats?
# 3. Create a list containing the sequence 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5 without hard-coding the sequence.

# A float has a decimal, integers have only whole number. 

# num_list = []                   #create an empty list
# for num in range(3,11):         # for loop to get 3-10 
#     if num % 2 == 1:            # condition to identify the odd numbers ( even numbers would be % 2 == 0)
#         num_list.append(num/2)      # appending foor loop into num_list /2 to get float.  
# print(num_list)                 # 



# Exercise 5: Shopping List  DONE
# 1. Consider this list basket = ["Banana", "Apples", "Oranges", "Blueberries"];
# 2. Remove “Banana” from the list.
# 3. Remove “Blueberries” from the list.
# 4. Put “Kiwi” at the end of the list.
# 5. Add “Apples” at the beginning of the list.
# 6. Count how many apples are in the basket.
# 7. Empty the basket.
# 8. Print(basket)

# list1 = ["Banana", "Apples", "Oranges", "Blueberries"]      #1.
# list1.remove("Banana",)         #2. 
# list1.remove("Blueberries")     #3.
# print(list1)

# list1.append('Kiwi')        #4.
# list1.insert(0,"Apples")    #5. 
# x = list1.count("Apples")
# print(x)                    #6. 
# list1 = ' '                 #7.
# print(list1)                #8. 



# Exercise 6 : Loop - DONE
# 1. Write a while loop that will keep asking the user for input until the input is the same as your name.

# name = input('Enter your name: ')
# # keep_going = True
# while True:
#     name = input('Enter your name: ')
#     if name == 'joshua':
#         break

# or

# name = input('enter your name: ')
# while name != 'joshua':
#     name = input('enter your name: ')

    


# Exercise 7 - DONE
# 1. Given a list, use a while loop to print out every element which has an even index.

# letters = 'hello world' 
# index = 0
# while len(letters) != index:
#     if index % 2 == 0:
#         print(letters[index]) 
#     index = index + 1
#     # if len(letters) == index:
#     #     break



# Exercise 8 - DONE
# 1. Make a list of the multiples of 3 from 3 to 30. Use a for loop to print the numbers in your list.

# #create an empty list
# l = []
# #31 because it is the end of the range
# for i in range(3,31):
#     #if equal to zero it is a multiple of 3
#     if i % 3 == 0:
#         #add it to the list
#         l.append(i)
# print(l)



# Exercise 9 = DONE 
# 1. Use a for loop to find numbers between 1500 and 2700, which are divisible by 7 and multiples of 5.

# num = []
# for i in range(1500, 2701):
#     if (i%7==0) and (i%5==0):
#         num.append(str(i))
# print (','.join(num))





# Exercise 10: Favorite Fruits
# Ask the user to type in his/her favorite fruit(s) (one or several fruits).
# Hint : Use the input built in method. Ask the user to separate the fruits with a single space, eg. "apple mango cherry".
# Store the favorite fruit(s) in a list. (How can we ‘convert’ a string of words into a list of words?).
# Now that we have a list of fruits, ask the user to type in the name of any fruit.
# If the user’s input is a fruit name existing in the list above, print “You chose one of your favorite fruits! Enjoy!”.
# If the user’s input is NOT a fruit name existing in the list above, print, “You chose a new fruit. I hope you enjoy it too!”.
# Bonus: Display the list in a user friendly way : add the word “and” before the last fruit in the list – but only if there are more than 1 favorites!


# fav_fruit = input('What are your favourite fruits: ')
# fruit_list= fav_fruit.split(' ')
# new_input = input('pick a fruit, any fruit: ')

# if new_input in fruit_list:
#     print('You chose one of your favorite fruits! Enjoy!')
# else:
#     print('You chose a new fruit. I hope you enjoy it too!')



# Exercise 11: Who Ordered A Pizza ?
# Write a loop that prompts the user to enter a series of pizza toppings until they enter a ‘quit’ value.
# As they enter each topping, print a message saying you’ll add that topping to their pizza.
# Upon exit print all the toppings on the pizza and what the total is (10 + 2.5 for each topping)

# toppings = [input('enter your toppings: ')]             # variable for input, empty string + input 

# while 'quit' not in toppings:                           # while quit is not written, print 'i added {topping [-1]}' the last written string. 
#     print(f'I added {toppings[-1]} to your pizza ')
#     toppings.append(input('Enter your topping: '))      # append to toppings plus add message
# toppings.pop()                                          # remove the last topping = 'quit' when the loop stops so it is not seen 
# print(10 + 2.5*len(toppings))                           # pizza price + 2.5 x length of toppings


# Exercise 12: Cinemax - DONE
# A movie theater charges different ticket prices depending on a person’s age.              age
# if a person is under the age of 3, the ticket is free                                     if 3 = free
# if they are between 3 and 12, the ticket is $10;                                          elif 3-12 = 10
# and if they are over age 12, the ticket is $15 .                                          else 12 + = 15
# Apply it to a family, ask the user what the age of each of the people that want a ticket is.      
# Store the total cost of all the tickets for this group and print it out.
# A group of teenagers is coming to your movie theater and want to see a movie that is restricted for people between 16 and 21 years old.
# Write a program that ask every user their age, and then tell them which one can see the movie.
# Tip: Try to add the allowed ones to a list.

# if age < 4: 
#     print('the ticket price is free') 
# elif age >= 3 and age < 12:
#     print('the tickeet is $10')
# else: 
#     print('the ticket is $15')
# # print(age)

# family_list = []

# name_age = input('Please input your name, your age. Put a comma inbetween name/age; then write exit:  ')
# while name_age != 'exit':
#     person_info = name_age.split(',')
#     family_list.append(person_info) 
#     name_age = input('Please input your name, your age. Put a comma inbetween name/age; then write exit:  ')

# # print(family_list)

# # age = int(input('what is your age: '))
# total_price = 0
# for person_info in family_list:
#     if int(person_info[1]) < 4:
#         print('You are too young')
#         continue
#     elif int(person_info[1]) >= 4 and int(person_info[1]) < 12:
#         total_price += 10
#     else:
#         total_price += 15

# print(total_price)

# permitted = []

# for person_info in family_list:
#     if int(person_info[1]) >= 16 and int(person_info[1])<= 21:
#         print(f'{person_info[0]} you can watch the movie')
#         permitted.append(person_info[0])
#     else: 
#         print(f'{person_info[0]} you are too young or old')




# Exercise 13 : Who Is Under 16? - DONE 
# This time you have a list of users, and you want to remove every user that is below 16 years old.

# Write a program that ask every user their age, and if they are less than 16 years old, remove them from the list.
# At the end, print the final list.

# users = ['Max', 'Josh', 'Joe']                          # list of users
# users_over_16 = []                                      # empty list for user over 16
# for user in users:                                      #for loop to seprate user
#     age = int(input(f'Hi {user}, how old are you? '))   # age input with function
#     if age >= 16:                                       # if age is == or over 16 only, append to new list 
#         users_over_16.append(user)
# print(users_over_16)


# Exercise 14: Family Members - DONE
# Using a while loop keep asking a user for input, these inputs will be used to control a menu
# On the menu we will have 4 options:
# Add a name
# If the user selects this ask for the name to add
# Remove an existing name
# If the user selects this ask for the name to remove
# View family members
# Print a nice list of the family members names
# Exit

# users = []
# while True: 
#     selection = int(input('Select a number 1 -4: '))

#     if selection == 1: 
#         new_name = input('add a name: ')
#         users.append(new_name)
#     elif selection == 2:
#         rem_name = input('What name should I remove?')
#         users.remove(rem_name)
#     elif selection == 3:
#         print(users)
#     elif selection == 4: 
#         break
#     else:
#         print('Invalid request')


