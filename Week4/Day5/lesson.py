# # Exercise 2 : Box Of Stars
# # Write a function named box_printer that takes any amount of strings (not in a list) and prints them, one per line, in a rectangular frame.
# # For example calling box_printer("Hello", "World", "in", "reallylongword", "a", "frame") will result as:
# # ******************
# # * Hello          *
# # * World          *
# # * in             *
# # * reallylongword *
# # * a              *
# # * frame          *
# # ******************



# # def get_longest_word(words):
# #     longest = 0
# #     for word in words:
# #         if len(word) > longest:
# #             longest = len(word)
# #     return longest 

# # def draw_starline(length):
# #     print('*'*(length + 4))

# # def draw_wordlines(text_list):
# #     for word in word:
# #         spaces = ' '*(longest - len(word))
# #         print(f'* {word}')

# # def run():
# #     text = 'this is a reallylongword test sentance'    # sentence
# #     text_list = text.split('')                          #split the sentence into strings 
# #     longest = get_longest_word(text_list)
# #     draw_starline(longest)
# #     draw_wordlines(text_list, longest)
# #     draw_starline(longest)

# # run()

# exercises and recap with Jonathan--------------

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


# answers ---------------

# def write_hello(word):
   
#     print(word)

# write_hello('bonjour')

# user_word = input("Tell me a word: ")

# write_hello (user_word)

# def favorite_book(book_name):
#     print(f'One of my favorite books is {book_name}')
# favorite_book('Alice in wonderland')   


# for i in range(1,11):
#   print(i)


# foods = ['sushi', 'pasta', 'pizza']
# for food in foods: 
#     print(food) 




# def uppercase():
#     new_word = input('Enter a word:')
#     word_upper = new_word.upper()
#     return word_upper 

# new_num = int(input('Enter a number'))

# new_list = []

# for i in range(new_num):
#     new_word = uppercase()
#     new_list.append(new_word)
# print(new_list)




list_of_strings = ['hello', 'kittycat', 'construction']

def longest_word(list_of_strings):
    longest = words[0]
    for word in words: 
        if word > longest:
            longest = word
    return longest
        
print(longest)