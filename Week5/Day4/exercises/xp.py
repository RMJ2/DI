# import json 
# import random

# def get_words_from_file():
#     with open ('wordlist.txt', 'r') as f:
#         return f.readlines()
     

# def get_random_sentence(words, count):
#     sentence = ''

#     for i in range(count):
#         random_word = random.choice(words)
#         sentence += random_word.strip('\n')
#         sentence += ' '
#     return sentence.lower() 


# def main(): 
#     '''
#     def get_words_from_file():
#     with open ('wordlist.txt', 'r') as f:
#         return f.readlines()
     

#     def get_random_sentence(words, count):
#         sentence = ''

#         for i in range(count):
#             random_word = random.choice(words)
#             sentence += random_word.strip('\n')
#             sentence += ' '
#         return sentence.lower() 
#     '''
# main() 

# number = int(input('How long should the sentance be? Pick a number between 2-20 words? '))
# # print(user)


# if number > 20 or number < 2: 
#     print('Invalid input, choose a number between 2-20')
# else: 
#     all_words = get_words_from_file()
#     sentence = get_random_sentence(all_words, number)
#     print(sentence)

   
#---------------Exercise 2 - Working with JSON

import json
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

thing = json.loads(sampleJson)
print(thing['company']['employee']['payable']['salary'])

thing['company']['employee']['birth_date'] = '1.1.2000'
print(thing)

newFile = 'newExample.json'

with open(newFile, 'w') as f:               # save to new file
    json.dump(thing, f, indent=4, sort_keys=False)




