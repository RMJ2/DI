class Farm: 
    def __init__(self, name): 
    
        self.name = name
        self.animals = {}
        

    def add_animal(self, name, amount=1):
        if name in self.animals:
            self.animals[name] += amount 
        else:
            self.animals[name] = amount


    def get_info(self):
        print(f"{self.name}'s Farm")
        for name, amount in self.animals.items():
            print(f"{name} : {amount}")
        print("E-I-E-I-O")





# Create the code that is needed to recreate the code above. Here are a few questions to help give you some direction:
# 1. Create a Farm class. How do we implement that?
# 2. Does the Farm class need an __init__ method? If so, what parameters should it take?
# 3. How many method does the Farm class need ?
# 4. Do you notice anything interesting about the way we are calling the add_animal method? What parameters should this function have? How many…?
# 5. Test that your code works and gives the same results as the example above.
# 6. Bonus: line up the text nicely in columns like in the example using string formatting
# macdonald = Farm("McDonald")
# macdonald.add_animal('cow',5)
# macdonald.add_animal('sheep')
# macdonald.add_animal('sheep')
# macdonald.add_animal('goat', 12)
# print(macdonald.get_info())


# Output

# McDonald's farm

# cow : 5
# sheep : 2
# goat : 12

#     E-I-E-I-0!