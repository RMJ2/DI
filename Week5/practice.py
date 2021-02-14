# def multiply_by2(li):
#     new_list = []
#     for item in li: 
#         new_list.append(item*2)
#     return(new_list)

# print(multiply_by2([1,2,3,55]))



# #square 
# my_list = [5,4,3]

# new_list = list(map(lambda num: num**2, my_list))
# print(new_list)

# #List sorting
# a = [(0,2), (4,3), (9,9), (10,-1)] 
# a.sort(key=(lambda x: x[1]))
# print(a)


#OOP
# class PlayerCharacter:
#     def __init__(self, name):
#         self.name = name

#     def run(self):
#         print('run')

# player1 = PlayerCharacter()
# print(player1)


class Pets():
    animals = []
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Tabby(Cat):
    def sing(self, sounds):
        return f'{sounds}'

my_cats = [Tabby, Bengal, Chartreux]

print(my_cats)
