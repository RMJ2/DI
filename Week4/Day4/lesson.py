# nums = [1,2,3]      # = 6 

# def get_total(numbers):
#     total = 0
#     for num in numbers: 
#         total += num
#     return total

# default arguments
# def say_hello(name):            # name = whatever you write in the terminal 
#     print(f'Hello {name}')      



# --------------- exercises ------------------------------

# 1 Create a function that has 2 parameters:    - DONE
# Your age, and your friends age.
# Return the older age

# def age(my_age, your_age)
#     if my_age > your_age: 
#         return my_age
#     else: 
#         return your_age 

# 2. Create a function that takes 2 words       
# It must return the lenght of the longer word
# longest_word = ['hello', 'goodbye']

# def find_longest_word(word_list):
#     for word in word_list: 
#         if len(word) > len(longest_word):
#             longest_word = word
# # print(word)
# find_longest_word(longest_word)

# list_words = ['hello', 'gooodbye']

# def get_longest_word(word1, word2):
#     return max(len(word1), len(word2))

#     # or
#     if len(word1) > len(word2):
#         return len(word1)
#     return 




# def find_longest_word(words_list):                  #function
#     word_len = []                                   #variable empty list
#     for n in words_list:                            #loop number in words_list
#         word_len.append((len(n), n))                #append words in list (length of letters), and letters. 
#     word_len.sort()                                 #sort the list by length of letters.
#     return word_len[-1][0], word_len[-1][1]         # returns the lists [last str] and [first str], and also [last] and [second]
# result = find_longest_word(['Hello', 'pneumonoultramicroscopicsilicovolcanoconiosis', 'supercalifragilisticexpialidocious'])   #variable for function with list of words. 
# print('\nLongest word:', result[1])                 #(print) /n = new line, prints the longest word.
# print('The length of the longest word: ',result[0]) #str + number of letters in longest word. 


# # or 

# text = 'thids is a reallylongowrd test sentance'    # sentence
# text_list = text.split('')                          #split the sentence into strings 

# def get_longest_word(words):
#     longest = 0
#     for word in words:
#         if len(word) > longest:
#             longest = len(word)
#     return longest 


# # 3. Write the max() function yourself...

# def getmax(numbers):
    biggest = numbers[0] 
    for num in numbers:
        if num > biggest:
            biggest = num
        
    return biggest 

# # same as using max()


# 4.  Create a function that takes a list as an argument
# The list should contain any number of entries.
# each entry should have a name and grade
# return the name of the person with the highest grade

students = [
    {'name': 'Adam', 'grade': 80},
    {'name': 'Bob', 'grade': 70},
    {'name': 'Charlie', 'grade': 81},
]

def top_students(list_of_students):
    top = students[0]
    for student in students:
        if student['grade'] > top['grade']:
            top = student
    return top['name']

top_students(students)