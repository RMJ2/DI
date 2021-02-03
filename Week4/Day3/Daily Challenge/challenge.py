# Chaims notes: 

word = input('please input a word we will encrypt: \n')

encrypted_word = []

for letter in word:
    number_version = ord(letter) + 3
    letter_version = chr(number_version)
    encrypted_word.append(letter_version)

print(''.join(encrypted_word))


