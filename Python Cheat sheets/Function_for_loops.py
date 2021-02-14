# PART 1
# make an empty list
# loop 3 times and each time, ask the user to enter a word.
# add that word to the list
# once you have all 3 words, print the list to see if it worked

# PART 2
# ask the user to enter a number...
# Then loop that many times and do the same as part 1
# So if they enter 5, you need to loop 5 times and ask them for words and append to the list.

# PART 3
# make a function that asks the user to enter a word.
# the function should return the uppercase of that word.  (KEY WORD:  RETURN )

# once that works...
# put that function in your loop from part 2.

# PART 4
# Write a function that takes a list as an argument
# Find the longest word in the list
# return it.

# print the returned value

# now run this code on the list that the user entered in part 3

def uppercase():
    new_word = input('Enter a word:')
    word_upper = new_word.upper()
    return word_upper 

new_num = int(input('Enter a number'))
new_list = []

for i in range(new_num):
    new_word = uppercase()
    new_list.append(new_word)
print(new_list)

# list_of_strings = ['hello', 'testing', 'construction']

def longest_word(words):
    longest = 0
    for word in words: 
        if len(word) > longest:
            longest = len(word)
    return longest
        
print(longest_word(new_list))

#------------------------------------------------------------------------------------------

# Exercise 3 : The Alphabet - DONE
# Create a string of all the letters in the alphabet
# Loop over each letter and print a message that contains the letter and whether its a vowel or a consonant

alphabet = "abcdefghijklmnopqrstuvwxyz"
vowels = "aeiou"
for letter in alphabet:
	if letter in vowels:
		print(letter, "is a vowel")
	else:
		print(letter, "is a consonant")

#------------------------------------------------------------------------------------------

# Exercise 7: When Will I Retire ?   DONE
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

#------------------------------------------------------------------------------------------

# Exercise 6 : Magicians …          DONE  
# Make a list of magician’s names.
# Pass the list to a function called show_magicians(), which prints the name of each magician in the list.
# Write a function called make_great() that modifies the list of magicians by adding the phrase "the Great" to each magician’s name.
# Call show_magicians() to see that the list has actually been modified.

name_list = ['Harry', 'Brian', 'Jamie']

def show_magicians(magicians_names):
    for name in magicians_names:
        print(name)

def make_great(magicians_names):
    new_list = []
    for name in magicians_names:
        new_list.append(f'The great {name}')
    return new_list

show_magicians(name_list)
name_list = make_great(name_list)
show_magicians(name_list)