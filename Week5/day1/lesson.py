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