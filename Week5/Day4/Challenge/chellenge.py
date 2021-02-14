class Text():

    def __init__(self,text):
        self.words = text.split(' ')         # text is stored in words


    def frequency(self,my_word):
        count = 0 
        for each_word in self.words:
            if each_word == my_word:
                count += 1 
        return count

    # def most_common_word(self):          # come back to this


    def unique_words(self):
        unique_word_list = []                 #1
        for each_word in self.words:          #2
            if not each_word in unique_word_list:
                unique_word_list.append(each_word)
        return unique_word_list #5


# c1 = Text('a method to return the frequency of a word in the text (assume words are separated by whitespace) return None or meaningful message')
# print(c1.frequency('the'))

c1 = Text('this is a test to see how many the there is in the sentence of the string')
print(c1.unique_words())


