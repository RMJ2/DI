# Exercise 1 - cats - Done 
# Instantiate 3 Cat objects using our class
# Create a function that finds the oldest cat and returns the cat
# Print out: “The oldest cat is , and is years old.” using the method previously created

# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# def oldest_cat(cats):                     #A function for cats 
#     oldest_for_now = 0                    # starts at 0 
#     oldest_cat = None                     # becomes cat 1, then cat 2 - grows with age of cat. 
#     for cat in cats:                      
#         if cat.age > oldest_for_now:
#             oldest_cat = cat
#             oldest_for_now = cat.age    
#     return oldest_cat

# cat1 = Cat('Nico', 1)
# cat2 = Cat('Fluffy', 5)
# cat3 = Cat('Rory', 3)

# list_of_cats = [cat1, cat2, cat3]


# print(oldest_cat(list_of_cats)) 


# Exercise 2 : Dogs     - DONE
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



# Exercise 3 : Who’s The Song Producer ? - STUCK
# Define a class called Song, it will show the lyrics of a song.
# Its __init__() method should have two arguments: self and lyrics(a list).
# Inside your class create a method called sing_me_a_song that prints each element of lyrics on his own line.
# Create an object, for example:
#   stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])

# Then, call the method sing_me_a_song. The output should be:
#   There’s a lady who's sure
#   all that glitters is gold
#   and she’s buying a stairway to heaven

# class Song:

#     def __init__(self, lyrics):
#         self.lyrics = lyrics

#     def sing_me_a_song(self):
#        for line in self.lyrics:
#         print(line)

# stairway = Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])
# stairway.sing_me_a_song()



# Exercise 4 : Afternoon At The Zoo
# Create a class Zoo
# In this class create a method __init__ that takes one parameter: zoo_name
# It instantiates two attributes: animals (an empty list) and name (name of the zoo).
# Create a method add_animal that takes one parameter new_animal. This method adds the new_animal to the animals list, only if the new_animal isn’t already in the list.
# Create a method get_animals that prints all the of animals in the zoo.
# Create a method sell_animal that takes one parameter animal_sold. This method removes the animal from the list, only if he was already in the list.
# Create a method sort_animals that sorts the animals alphabetically and groups them together based on their first letter.
# { 
#     1: "Ape",
#     2: ["Baboon", "Bear"],
#     3: ['Cat', 'Cougar'],
#     4: ['Eel', 'Emu']
# }
# Create a method get_groups that prints the animal/animals inside each group.
# Create an object ramat_gan_safari and call all the methods.
# Tip: for each method, the argument should be the answer of the zoo keeper.
# Example

# Which animal should we add to the zoo --> Giraffe
# x.add_animal(Giraffe)


class Zoo: 

    def __init__(self, zoo_name='The Zoo'):             #DONE - initialise class, make list outside parameter so that it is not always called
        self.zoo_name = zoo_name
        self.animals = []

    def add_animal(self,new_animal):                    # DONE adds the new_animal to the animals list, only if the new_animal isn’t already in the list.
        if animal not in self.animals:                   # if animal is not in self.animals list add to the list.  
            self.animals.append(animal)
        

    def get_animals(self):                              # DONE prints all the of animals in the zoo.
        print(f'The animals in {self.zoo_name} are:')   # print initial message before for loop
        for animal in self.animals:                     # for loop the animal in self.animals
            print(animal)                               

    def sell_animal(self, animal_sold):                  # DONE takes one parameter animal_sold. This method removes the animal from the list, only if he was already in the list.
        if animal_sold in self.animals: 
            self.animals.remove(animal_sold)
        

    def sort_animals(self):                             # STUCK sorts animals alphabetically and sorts them into groups basded on the first letter. 
        x = sorted(animals)
        print(x)

    # make a list of lists
    [
        []
        []
        []
    ]


    def get_groups(self):                                # NOT FINISHED  - prints the animals inside the groups
        print()
