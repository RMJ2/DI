# # Exercise 1 : Pets
# # Consider this code
# class Pets():
#     animals = []
#     def __init__(self, animals):
#         self.animals = animals

#     def walk(self):
#         for animal in self.animals:
#             print(animal.walk())

# class Cat():
#     is_lazy = True

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def walk(self):
#         return f'{self.name} is just walking around'

# class Bengal(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# class Chartreux(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# # 1. Add another cat breed
# # 2. Create a list of all of the pets (create 3 cat instances from the above) my_cats = []
# # 3. Instantiate the Pet class with all your cats. Use the variable my_pets
# # 4. Output all of the cats walking using the my_pets instance

# class Tabby(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# my_cats = [Bengal('Fluffy', 3), Chartreux('Felix', 5), Tabby('Nico', 1)]

# my_pets = Pets(my_cats) 

# my_pets.walk()


#----------------------------------------------------------------------------
# Exercise 2 - Dogs 

# Create a class named Dog with the attributes name, age, weight
# Implement the following methods for the class:
# bark: returns a string of “ barks”.
# run_speed: returns the dogs running speed (weight/age *10).
# fight : gets parameter of other_dog, returns string of which dog won the fight between them, whichever has a higher run_speedweight* should win.
# Create 3 dogs and use some of your methods

class Dog():
    
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        print(f'{self.name} is barking') 
    
    
    def run_speed(self):    #DONE
        return (self.weight/self.age)*10
        

    # def fight(self, other_dog):
    #     if self.run_speed() * self.weight > other_dog.run_speed() * other_dog.weight:
    #         print(f'{self.name} wins!')
    #     elif self.run_speed() * self.weight < other_dog.run_speed() * other_dog.weight:
    #         print(f'{other_dog.name} wins!')
    #     else: 
    #         print('Draw!')

#OR

    def fight(self, other_dog):
            self_score = self.run_speed() * self.weight
            other_score = other_dog.run_speed() * other_dog.weight
            winner = None
            if self_score > other_score:
                winner = self
            elif self_score < other_score:
                winner = other_dog
            if winner:
                print(f"{winner.name} wins the fight!")
            else:
                print("Draw")

d1 = Dog('Rex', 5, 30)
d2 = Dog('Lemon', 1, 3)
d3 = Dog('Fluff', 7, 15)

d1.bark()
d1.fight(d3) 
d2.fight(d3)
d3.fight(d1)

# Exercise 3 : Dogs Domesticated
# Create a new python file and import your Dog class from the previous exercise.
# Create a class named PetDog that inherits from Dog.
# Add the attribute trained (boolean) to the PetDog class, should always start False
# Add the following methods:
# train: prints the output of bark and switches the trained boolean to True
# play: gets parameter of any amount of other dogs (look up args) and prints “the dogs: dog_names play together” each of the dogs that plays has their trained boolean switched to False
# do_a_trick: will print one of the following sentences randomly ONLY IF the dogs trained boolean is True, after doing the trick the trained boolean moves to False
# “dog_name does a barrel roll”
# “dog_name stands on their back legs”
# “dog_name shakes your hand”
# “dog_name plays dead”

# see filename xp_dog.py

       




