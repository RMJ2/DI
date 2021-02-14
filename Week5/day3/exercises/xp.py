# exercise 1 Built in functions

# class Example():

#     def abs(self):

# print(abs.__doc__)

# def abs(number):
#     """ absolute takes int, float and returns a positive output.  """
#     pass

# print(abs)

# def int(number):
#     """The int() function converts the specified value into an integer number. 
#     The int() function returns an integer object constructed from a number or string x, 
#     or return 0 if no arguments are given. A number or string to be converted to integer object. 
#     """
#     pass 

# print(int)

# def raw_input(): 
#     """ 
#     aw_input() function is used to accept user input.It presents a prompt to the user , 
#     gets input from the user and returns the data input by the user in a string. 
#     It is available in Python 2. x only, and is renamed to input() from Python 3. 
#     x version. Hence, in Python 3.
#     """
#     pass 

# print(raw_input)


class Money():
    def __init__ (self, currency, amount):
        self.amount = amount
        if self.amount > 1: 
            self.currency = currency + 's'      # if amount is more than 1, add s to end of currency
        else: 
            self.currency = currency


    def __str__ (self):                 #str(c1) '5 dollars'
        return f'{self.amount} {self.currency}'     # makes a string


    def __int__ (self):                             # int(c1) 5
        return amount 


    def __repr__ (self):                            # repr(c1) '5 dollars'
        return f'{self.amount} {self.currency}'  
    

    def __add__(self, number):          #c1+=5
        if type(number) == int:
            total = self.amount + number
        else:    
            total = self.amount + number.amount
        return total    

    def __iadd__ (self, other):         #c1+=c2
        if type(other) == int: 
            self.amount = self.amount + other
        else: 
            self.amount + other.amount
        return self

c1 = Money('dollar', 5)
c2 = Money('dollar', 10)
c4 = Money('shekel', 1)
c3 = Money('shekel', 10)

# str(c1)
# print(c1 + 5)
# print(c1 + c2)
# print(c1)
# print(c1 += 5) 
# print(c1)


# ----------exercise 3 - time------------------------------



