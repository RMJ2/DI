# Exercise 3 : Dogs Domesticated

class Dog():
    
    def __init__(self, name, age, weight, breed):
        self.name = name
        self.age = age
        self.weight = weight
        self.breed = breed 

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

    def mate(self, other_dog):
        puppy_name = self.name + '-' + other_dog.name 
        puppy_breed =  self.breed + '-' + other_dog.breed
        return Dog(puppy_name, 0.1, 1, puppy_breed) 
        

d1 = Dog('Sesame', 2, 30, 'Bulldog')
d2 = Dog('Schnitzel', 7, 5, 'Shitsu')

puppy = d1.mate(d2)
