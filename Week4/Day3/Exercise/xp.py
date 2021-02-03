# Exercise 1 : Convert Lists Into Dictionaries
# Convert the two following lists, into dictionaries.
# Hint: Use the zip method
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# Expected output:
# {'Ten': 10, 'Twenty': 20, 'Thirty': 30}

# keys = ['Ten', 'Twenty', 'Thirty'] #list 1
# values = [10, 20, 30]               # list 2

# x = zip(keys, values)

# num_dict = {}

# for info in x:
#     num_dict[info[0]] = info[1]

# print(num_dict)



# Exercise 2 : Cinemax #2
# “Continuation of Exercise Cinemax of Week4Day2 XP”

# A movie theater charges different ticket prices depending on a person’s age. v
# if a person is under the age of 3, the ticket is free v
# if they are between 3 and 12, the ticket is $10; v
# and if they are over age 12, the ticket is $15 . v
# Here is the object you will work with : family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
# Using a for loop, the dictionary above, and the instructions, print out how much each family member will need to pay alongside their name
# After the loop print out the family’s total cost for the movies
# Bonus: let the user input the names and ages instead of using the provided family variable (Hint: ask the user for names and ages and add them into a family dictionary that is initially empty)


# family_dict = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
# total_price = 0

# for person in family_dict:
#     # print(family_dict[person])
#     if family_dict[person] < 4:
#         print('You are too young')
#         continue
#     elif family_dict[person] >= 4 and family_dict[person] < 12:
#         total_price += 10
#     else:
#         total_price += 15

# print(total_price)



# Exercise 3: Zara

# Here is some information about a brand.
# 1. Create a dictionary called brand, and translate the information above into keys and values.
# Change the number of stores to 2.
# Print a sentence that explains who the clients of Zara are.
# Add a key called country_creation with a value of Spain, to brand
# If the key international_competitors is in the dictionary, add the store Desigual.
# Delete the information about the date of creation.
# Print the last international competitor.
# Print in a sentence, the major clothes’ colors in the US.
# Print the amount of key value pairs (length of the dictionary).
# Print only the keys of the dictionary.
# Create another dictionary called more_on_zara with the following information:
# creation_date: 1975 
# number_stores: 10 000 
# Use a method to add the information from the dictionary more_on_zara to the dictionary brand.
# Print the value of the key number_stores. What just happened ?

brand = {                                            #no.1
    'name': 'Zara', 
    'creation_date': 1975, 
    'creator_name': 'Amancio Ortega Gaona', 
    'type_of_clothes': ['men', 'women', 'children', 'home'],    #List
    'international_competitors': ['Gap', 'H&M', 'Benetton'],    #List
    'number_stores': 7000, 
    'major_color':{
        'France': 'blue',
        'Spain': 'red', 
        'US': ['pink', 'green'] 
    }, 
}

brand['number_stores'] = 2                          #no.2
# print(brand)
customers = brand['type_of_clothes']
# print(f'We provide services for {customers}')     #no.3

brand['country_creation'] = 'Spain'                 #no.4


if brand.get['international_competitors']:
    brand['international_competitors'].append('Desigual')   #no.5 1/2

# OR

if 'international_competitors' in brand:                    #no.5 2/2
    brand['international_competitors'].append('Desigual')
else: 
    brand['international_competitors'] = ['Desigual']



brand.pop('creation_date')                          #no.6

# print(brand['international_competitors'][-1])     #no.7

# print(brand['major_color']['US'])                 #no.8


# print(brand.keys())                               #no.9


more_on_zara = {                                    #no.9
    'creation_date': 1975, 
    'number_stores': 10000 
}

brand.update(more_on_zara)                          #no.10
# print(brand)

print(brand.get('creation_date'))





# Exercise 4 : Disney Characters
# Consider this list :

# users = [ "Mickey", "Minnie", "Donald","Ariel","Pluto"] 
# Analyse these results :

# 1/ print(disney_users_A) >> {"Mickey": 0, "Minnie": 1, "Donald": 2, "Ariel": 3, "Pluto": 4}

# 2/ print(disney_users_B) >> {0: "Mickey",1: "Minnie", 2: "Donald", 3: "Ariel", 4: "Pluto"}

# 3/ print(disney_users_C) >> {"Ariel": 0, "Donald": 1, "Mickey": 2, "Minnie": 3, "Pluto": 4}

# Use a for loop to recreate the #1 result. Tip : don’t hardcode the numbers
# Use a for loop to recreate the #2 result. Tip : don’t hardcode the numbers
# Use a method to recreate the #3 result
# Hint: The 3rd result is in the alphabetical order
# Recreate the #1 result, only if:
# The characters’ names contain the letter “i”.
# The characters’ names start with the letter “m” or “p”.


#no.1 
users = [ "Mickey", "Minnie", "Donald","Ariel","Pluto"] 
counter = 0
disney_user_a = {}      #create empty dict

for character in users:             
    disney_user_a[character] = counter          #create a key(character) = to counter(new value)
    counter += 1 
print(disney_user_a)



if 'Mickey' in user:'
    print ('YES')
else:
    print('NO')

for name in users:                              #bonus 4
    if 'i' in name and name[0] in ['M','P']:    #bonus 5
        print(name)

