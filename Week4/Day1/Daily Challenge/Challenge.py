# Using the input function, ask the user for a string. The string must be 10 characters long.
# If it’s less than 10 characters, print a message which states “string not long enough”
# If it’s more than 10 characters, print a message which states “string too long”
# Then, print the first and last characters of the given text
# Construct the string character by character: Print the first character, then the second, then the third, until the full string is printed
# Example:
# The user enters “Hello Word”
# Then, you have to construct the string character by character
# H
# He
# Hel
# … etc
# Hello World
# Swap some characters around then print the newly jumbled string (hint: look into the shuffle method)
# Example:
# Hlrolelwod
#DONE

string = input('write Hello World:')


if len(string)<10:
    print('String is too short')
elif len(string)>10:
    print('String is too long')

empty=''
for x in string:
    # empty+=x
    empty = empty + x
    print(empty)

# letter is a new variable in the loop for each letter in the string/word.
# H
# e
# l
# etc etc
# for letter in string:
#     print(letter)



   
