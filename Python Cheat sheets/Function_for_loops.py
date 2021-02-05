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


# list_of_strings = ['hello', 'kittycat', 'construction']

def longest_word(words):
    longest = 0
    for word in words: 
        if len(word) > longest:
            longest = len(word)
    return longest
        
print(longest_word(new_list))



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