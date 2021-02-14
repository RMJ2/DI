# Step 1
# Create a new class called Animal.
# It should take 2 parameters, "species" and "habitat"
# (make the class defintion and the init method)

# Step2
# add another parameter to your class, which is the sound that the animal makes.
# write a method called talk, that prints out the animals sound.

# Step3
# create 2 instance of animals, and make each one talk.

class Animal:                                       #class name

    def __init__(self, species, habitat, sound):        # initialise with parameters. 
        self.species = species                          # create definition and the init method. 
        self.habitat = habitat 
        self.sound = sound

    def talk(self):                                     # method called talk (must add self.)
        print(self.sound)                               # prints the animals sound

''' Step 3 '''
a1 = Animal('lion', 'mountains', 'meow')                #instance (Instantiate) 1 - including the parameters
a1.talk()                                               # call the function inside the class. 

a2 = Animal('cat', 'house', 'roar')
a2.talk()

#---------------------------------------------------------------------------------------------

# Exercise 2 : Dogs
# Create a class Dog.
# In this class, create a method __init__, that takes two parameters : nameand height. This function instantiates two attributes, which values are the parameters.
# Create a method named bark that prints “ goes woof!”
# Create a method jump that prints the following “ jumps cm high!” where x is the height*2.
# Outside of the class, create an object davids_dog. His dog’s name is “Rex” and his height is 50cm.
# Print the details of his dog by calling the methods.
# Create an object sarahs_dog. Her dog’s name is “Teacup” and his height is 20cm.
# Print the details of her dog by calling the methods.
# Create an if statement outside of the class to check which dog is bigger. Print the name of the bigger dog.

# class Dog:
#     def __init__(self, name, height):
#         self.name = name
#         self.height = height

#         def bark(self):
#             print('goes woof!')

#         def jump(self): 
#             x = height*2
#             print(f'jumps {x}cm high!')    


# davids_dog = Dog('Rex', 50)
# print(f'{davids_dog.name} is {davids_dog.height}cm.')

# sarahs_dog = Dog('Teacup', 20)
# print(f'{sarahs_dog.name} is {sarahs_dog.height}cm.')

# list_of_dogs = [davids_dog, sarahs_dog]
# tallest_for_now = 0
# tallest_dog = None
# for dog in list_of_dogs: 
#     if dog.height > tallest_for_now:
#         tallest_dog = dog
#         tallest_for_now = dog.height
# print(f' The tallest dog is {tallest_dog.name}')


#---------------------------------------------------------------------------------------------
# Bank Account


class Bank():                                           
    def __init__(self, account, pin):                   #initialise parameters
        self.account = account                          
        self.pin = pin 
        self.balance = 0                                # value for starting balance
        self.history = []                               # empty list to store history of deposits and withdrawels. 

    def deposit(self, amount): 
        if amount <= 0:                                 # to ensure no negative deposit can be made
            print('You must deposit a positive amount')
        else:
            self.balance += amount                      # new balance, made by amount deposited
            self.history.append(f'Deposit: {amount}')   # update list of history for amount deposited. 

    
    def withdraw(self, amount):
        if amount > self.balance:                       #to ensure no withdrawal of negative funds is made
            print('You do not have enough funds')
        else:
            self.balance -= amount                      # new balance, made by amount withdrawn
            self.history.append(f'Withdraw: {amount}')  # update history listfor amount withdrawn
            return amount                               # returns amount in terminal


    def show_balance(self): 
        print(self.balance)                             # print balance


    def show_history(self):                             # 
        for thing in self.history:                      # item in list (instead of printing on one line) 
           print(thing)                                 # prints item line by line 


b1 = Bank(12345, 54321)
b1.deposit(100)
b1.deposit(100)
b1.withdraw(30)


#---------------------------------------------------------------------------------------------
# Calculator 

class Calc: 

    def add(x,y):
        answer = x + y
        print(answer)

    def sub(x,y):
        answer = x - y
        print(answer)

    def mult(x,y):
        answer = x * y
        print(answer)

    def div(x,y):
        answer = x / y
        print(answer)

print(Calc.add(5,5))
print(Calc.sub(5,5))
print(Calc.mult(5,5))
print(Calc.div(5,5))