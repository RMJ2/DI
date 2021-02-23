from pprint import pprint 
import functions 

# strings     = 'hello world' + name    or      f'hello world {name}' 

# int
# float 


# exercise: winter months... 

# month = int(input('select a month between 1-12: ' ))

# if month >= 3 and month <= 5: 
#     print('Spring')
# elif month >=6 and month <=8: 
#     print ('Summer') 
# elif month >= 9 and month <=11: 
#     print('Autumn')
# elif month == 0 or month >= 13:
#     print('Invalid selection, please select between 1-12')
# else: 
#     print('Winter')


# exercise:
#ask the user for their name if the name begins with the letter a print a if b print b if c print c if none of the above print does not start with a b or c

# name = input('what is your name? ')

# initial = name[0].lower()

# if initial == 'a': 
#     print('a')
# elif initial == 'b': 
#     print('b')
# elif initial == 'c': 
#     print('c')
# else: 
#     print('I dont know')



# name = ['josh', 'lior', 'harry']
# name.append('aviva')
# name.insert(1,'ester')
# name.pop(3)
# print(name)

# name = 'joshua'
# print(list(name))


# exercise:
# basket = ["Banana", "Apples", "Oranges", "Blueberries"]

# basket.pop(0)
# basket.pop()
# basket.append('Kiwi')
# basket.insert(0,'Apples')
# count = basket.count('Apples')
# basket.clear()

# print(basket)
# print(count)


#DICTIONARY
#Basic

# phonebook = {
#     'name': {
#         'fname': 'Aviva',
#         'lname': 'Drozd'
#     },
#     'phone': 111111
# }
# #we grab items from dictionaries via KEYS!!!! NOT position
# print(phonebook['name']['lname']) = Drozd
# print(phonebook['phone']) = 11111
# #More Complex
# phonebook = {
#     'person1': {'name': {'fname': 'adam', 'lname': 'adamson'}, 'phone': 1234},
#     'person2': {'name': {'fname': 'bob', 'lname': 'boo'}, 'phone': 5678},
#     'person1': {'name': {'fname': 'cindy', 'lname': 'chin'}, 'phone': 9123},
# }
# # print(phonebook['person2']['phone']) # = prints person 2 phone number
# # print(phonebook['person1']['name']['fname']) # = prints person1 first name
# phonebook['person2']['phone'] = 1111 #= reassigns phone nr to 1111
# phonebook['person1']['name']['fname'] = 'Tom' # = ressigns person 1 fist name to Tom

# phonebook['person']= {
#     'name': {'f_name': 'joshua', 'l_name': 'duetel'}, 'phone': 57483947}

# pprint(phonebook.items())

# exercise 3: zara



# brand = {

# 'name': 'Zara',
# 'creation_date': 1975, 
# 'creator_name': 'Amancio Ortega Gaona',
# 'type_of_clothes': ['men', 'women', 'children', 'home'] ,
# 'international_competitors': ['Gap', 'H&M', 'Benetton'], 
# 'number_stores': 7000 ,
# 'major_color': {'France': 'blue', 'Spain': 'red', 'US': ['pink', 'green']} 

# }

# brand['number_stores'] = 2

# customers = brand['type_of_clothes']
# # print(f'We provide services for {customers}') 

# brand['country_creation'] = 'Spain'

# if 'international_competitors' in brand:
#     brand['international_competitors'].append('Desigual')
# else: 
#     brand['international_competitors'] = ('Desigual')

# brand.pop('creation_date')

# # print(brand['international_competitors'][-1])

# # print(brand['major_color']['US'])

# # print(len(brand.items()))

# # print(brand.keys())

# more_on_zara = {
#     'creation_date': 1975,
#     'number_stores': 10000
# }

# brand.update(more_on_zara)

# print(brand['number_stores'])


# for i in range(20,51,2): 
#     print(i)

# exercise range 50-250, divisible by 3 
# for i in range(50,251,3):
#     if (i%3== 0):
#         print (i)


# names = ['aviva', 'ben', 'charlie']

# a_list = []
# b_list = []
# c_list = []

# for name in names: 
#     if name.startswith('a'): 
#         a_list.append(name)
#     elif name.startswith('b'): 
#         b_list.append(name)
#     elif name.startswith('c'): 
#         c_list.append(name)

# print(a_list)
# print(b_list)
# print(c_list)


# counter=0
# while counter <= 50: 
#     print(counter)
#     counter+=1 

# counter = 50
# while counter <= 250:
#     if counter % 3 == 0:
#         print(counter)
#     counter+=1

# active = True
# name_list = []
# while active: 
#     name = input('input your name, when finished write exit.\n')
#     if name != 'exit':
#         name_list.append(name)
#     else: 
#         active = False
# print(f'Your list of names is: {name_list}')


# active = True 
# city_list = []
# while active: 
#     city = input('Which cities have you visited? (input exit to finish)')
#     if city != 'exit':
#         city_list.append(city)
#     else: 
#         active = False
# print(f'You have visited these cities: {city_list}')


# print(functions.add(2,4))



# exercise: hangman

import random 
wordslist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share', 'credit card', 'rush', 'south']
word = random.choice(wordslist)

while 