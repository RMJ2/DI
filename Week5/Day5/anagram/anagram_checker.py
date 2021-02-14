import json

class AnagramChecker: 

    def __init__ (self): 
        with open('words.txt',) as f: 
            self.wordlist = f.readlines()
            self.dict = {} 

            for word in self.wordlist: 
                word = word.strip('\n')
                self.dict[word] = 1

anagram1 = AnagramChecker()
# print(anagram1.dict)

    # def is_valid_word(word):
    #         # should check if the given word (‘word’) is a valid word.
    

    # def get_anagrams(word):
