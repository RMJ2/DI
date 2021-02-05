# Exercise 1 : What Are You Learning ? DONE
# Write a function called display_message() that prints one sentence telling everyone what you are learning about in this chapter.
# Call the function, and make sure the message displays correctly.

# def display_message():
    
#     print('We are learning functions!')
# display_message()


# Exercise 2: What’s Your Favorite Book ? DONE
# Write a function called favorite_book() that accepts one parameter, title.
# The function should print a message, such as “One of my favorite books is Alice in Wonderland”.
# Call the function, making sure to include a book title as an argument in the function call.

# def favorite_book(book_name):
#     print(f'One of my favorite books is {book_name}')
# favorite_book('Alice in wonderland')    


# Exercise 3 : Some Geography DONE
# Write a function called describe_city() that accepts the name of a city and its country.
# The function should print a simple sentence, such as “Reykjavik is in Iceland”.
# Give the parameter for the country a default value.
# Call your function for three different cities, at least one of which is not in the default country.

# def describe_city(city_name, country = 'UK'):
#     print(f'{city_name} is in the {country}')

# describe_city('London')
# describe_city('Machester')
# describe_city('Leeds', 'United Kingdom')



# Exercise 4 : Random _DONE
# Create a function that accepts a number between 1 and 100 and generates another number randomly between 1 and 100.
# Compare the two numbers, if it’s the same number, display a success message to the user, otherwise show a fail message and display both numbers

# import random

# def guess_num(number_list):
#     for number in number_list:                      # how to create this with multiple number options (list).
        
#         if number in range(1,101):
#             random_num = random.randint(1,100)
#             if number == random_num: 
#                 print('Success!')
#             else:
#                 print('Fail :( ')
#                 print(f'The random number was {random_num}, your number was {number}. Better luck next time.')

# guess_num([20, 30, 40, 50])




# Exercise 5 : Let’s Create Some Personalized Shirts ! - DONE
# Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt.
# The function should print a sentence summarizing the size of the shirt and the message printed on it.
# Call the function once using positional arguments to make a shirt.
# Call the function a second time using keyword arguments.
# Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python.
# Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.

# def make_shirt(size = 'large', message = 'I love python'):

#     print(f'The shirt size is {size} and your message is: {message}')

# make_shirt('medium', 'hello')
# make_shirt(size = 'small', message = 'goodbye')
# make_shirt('large')
# make_shirt('medium')
# make_shirt('xs', 'final message')



# Exercise 6 : Magicians …          DONE  
# Make a list of magician’s names.
# Pass the list to a function called show_magicians(), which prints the name of each magician in the list.
# Write a function called make_great() that modifies the list of magicians by adding the phrase "the Great" to each magician’s name.
# Call show_magicians() to see that the list has actually been modified.

# name_list = ['Harry', 'Brian', 'Jamie']

# def show_magicians(magicians_names):
#     for name in magicians_names:
#         print(name)

# def make_great(magicians_names):
#     new_list = []
#     for name in magicians_names:
#         new_list.append(f'The great {name}')
#     return new_list

# show_magicians(name_list)
# name_list = make_great(name_list)
# show_magicians(name_list)


# Exercise 7: When Will I Retire ?   STUCK
# The point of the exercise is to check is a person can retire depending on his age and his gender.
# Note : Retirement age in Israel is 67 for men, and 62 for women (born after April, 1947).

# Create a function get_age(year, month, day)
# Hard-code the current year and month in your code (there are better ways of doing this, but for now it will be enough.)
# After calculating the age of a person, the function should return it (the age is an integer).
# Create a function can_retire(gender, date_of_birth).
# It should call the get_age function (with what arguments?) in order to receive an age back.
# Now it has all the information it needs in order to determine if the person with the given gender and date of birth is able to retire or not.
# Calculate. You may need to do a little more hard-coding here.
# Return True if the person can retire, and False if he/she can’t.
# Some Hints

# Ask for the user’s gender as “m” or “f”.
# Ask for the user’s date of birth in the form “yyyy/mm/dd”, eg. “1993/09/21”.
# Call can_retire to get a definite value for whether the person can or can’t retire.
# Display a message to the user informing them whether they can retire or not.
# As always, test your code to ensure it works.

def get_age(year, month, day):
   
    current_year = 2021
    current_month = 2
    current_day = 3
    users_age_year = current_year - year 
    if current_month > month:
        return users_age_year
    elif current_month == month:
        if current_day > day:
            return users_age_year 
        else: 
            return users_age_year -1
    else:
        return users_age_year -1
print(get_age(1993, 2, 5))



def can_retire (gender, DOB):
    year, month, day = DOB.split('/')               # split the year, month, day at position / into 3 strings
    age = get_age(int(year), int(month), int(day))  # age is put into 3 integers year, month year and definied as a variable. 

    if age >= 67 and gender == 'm' or age >= 62 and gender == 'f':  #if age/gender is more or == to retirement age
        print('You can retire')
    else:                                                           #if users age is less then retirement age
        print('Go back to work')  

user_gender = input('what is your gender m/f')                      #variable input for gender
user_dob = input('what is your DOB: yyyy/mm/dd')                    #variable input DOB

can_retire(user_gender, user_dob)                                   # call function on gender/age



# Exercise 7:
# Write a function that accepts one parameter (an int: X) and returns the value of X+XX+XXX+XXXX.
# Example:
# If X=3 the output when calling our function should be 3702 (3 +33 +333 + 3333)
# Hint: treating our number as a int or a str at different points in our code may be helpful


