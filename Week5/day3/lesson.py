# class Person: 

#     def __init__(self, weight, height, friends):
#         self.weight = weight
#         self.height = height 
#         self.friends = friends

#     def __gt__(self, other):
#         if self.friends > other.friends: 
#             return True
#         return False

# class Dog: 


# ----------------------------------

# What is the difference between Class vs Object.
# What is an instance 

# Instance Attributes vs Class Attributes 
# Class is the blue print: its the plan 
# Object is the final product. (its alive), created from the class. 

# d1 is the object 
# Dog is the class 

# ----------------------------------
#A little bit of sys and terminal scripts.

import sys
if __name__ == "__main__":
# if this file was loaded from the terminal
	total = 0
	for num in sys.argv[1:]:
		total += int(num)
	print(total)

#---------------------------------
# A simple clock in python using the datetime and time modules.
from time import sleep
from cprint import cprint  # IF YOU DONT HAVE CPRINT INSTALLED. USE NORMAL PRINT
from datetime import datetime
while True:
	x = datetime.now()
	cprint.info(x.strftime("%H:%M:%S"))
	sleep(1)
