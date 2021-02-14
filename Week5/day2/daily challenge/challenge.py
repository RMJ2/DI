# Gene 1 0 

# Chromosome [1 0 1 0 0 0 1 0 1 0]

# DNA [
#     [1 1 1 1 1 1 1 1 1 1]
#     [1 0 1 0 0 0 1 0 1 0]
#     [1 0 1 0 0 0 1 0 1 0]
#     [1 0 1 0 0 0 1 0 1 0]
#     [1 0 1 0 0 0 1 0 1 0]
#     [1 0 1 0 0 0 1 0 1 0]
#     [1 0 1 0 0 0 1 0 1 0]
#     [1 0 1 0 0 0 1 0 1 0]
#     [1 0 1 0 0 0 1 0 1 0]
# ]

# Organism [DNA,     % chance to mutate]

from random import randint, random

class Gene:
	def __init__(self):
		self.value = randint(0,1)
	def mutate(self):
		self.value = int(not bool(self.value))
	def __repr__(self):
		return f"{self.value}"
        
class Chromosome:
	def __init__(self):
		self.value = [Gene() for _ in range(10)]
	def mutate(self):
		for gene in self.value:
			if random() > 0.5:
				gene.mutate()
	def __repr__(self):
		return f"{self.value}"

class DNA:
	def __init__(self):
		self.value = [Chromosome() for _ in range(10)]
	def __repr__(self):
		return f"{self.value}"


c = Chromosome


# dunder = Double Under (Method that starts and ends with 2 __)
# Duner methods are exactly like normal methods/functions
# except they run automatically under certain circumstances. 

# __repr__    representation 
# shows a string representation of the class. 
# it runs whenever a variable is dumped in the terminal. 


# Ternary statement.
# If statement that sets a variable. In one line. 








# Daily Challenge : DNA
# This challenge is about Biology.

# Build a DNA object. DNA is composed of chromosomes which is itself composed of Genes.

# A Gene is a single value 0 or 1, it can mutate (flip).
# A Chromosome is a series of 10 Genes. It also can mutate, meaning a random number of genes can randomly flip (1/2 chance to flip).
# A DNA is a series of 10 chromosome, and it can also mutate the same way Chromosomes can.
# Implement these classes as you see fit.

# Create a new class called Organism that accepts a DNA object and a environement parameter that sets the probability for its DNA to mutate.
# Instantiate a number of Organims and let them mutate until one gets to a DNA is only made of 1s. Then stop and record the number of generations (iterations) it took.
# Write your results in you personal biology research notebook and tell us your conclusion :).